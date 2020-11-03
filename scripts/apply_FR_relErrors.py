#!/usr/bin/env python

'''
Example usage:

apply_FR_relErrors.py -i data/FR_lep_mva_hh_multilepton_2018_KBFI_2020Oct27_woTightCharge.root \
                      -r ../../tthAnalysis/HiggsToTauTau/data/FR_lep_ttH_mva_2018_CERN_2019Jul08.root \
                      -o data/FR_lep_mva_hh_multilepton_2018_KBFI_2020Oct27_woTightCharge_wSysUnc.root
'''

from tthAnalysis.HiggsToTauTau.safe_root import ROOT
from tthAnalysis.HiggsToTauTau.common import SmartFormatter

import argparse
import os
import prettytable
import shutil
import array

SUFFIXES = [ "pt1", "pt2", "be1", "be2", "up", "down" ]
MEASUREMENT_MAP = {
  'el_data_comb_NC' : 'el_data_comb',
  'el_QCD_NC'       : 'el_data_comb_QCD_fakes',
  'mu_data_comb'    : 'mu_data_comb',
  'mu_QCD'          : 'mu_data_comb_QCD_fakes',
}

parser = argparse.ArgumentParser(
  formatter_class = lambda prog: SmartFormatter(prog, max_help_position = 35)
)
parser.add_argument('-i', '--input',
  type = str, dest = 'input', metavar = 'file', required = True,
  help = 'R|Measured fake rates w/o the uncertainties',
)
parser.add_argument('-r', '--reference',
  type = str, dest = 'reference', metavar = 'file', required = True,
  help = 'R|Measured fake rates w/ the uncertainties',
)
parser.add_argument('-o', '--output',
  type = str, dest = 'output', metavar = 'file', required = True,
  help = 'R|Output file name',
)
parser.add_argument('-v', '--verbose',
  dest = 'verbose', action = 'store_true', default = False,
  help = 'R|Enable verbose output',
)
args = parser.parse_args()

input_filename = os.path.abspath(args.input)
ref_filename = os.path.abspath(args.reference)
out_filename = os.path.abspath(args.output)
verbose = args.verbose

assert(input_filename != ref_filename)
assert(input_filename != out_filename)
assert(ref_filename != out_filename)

if not os.path.isfile(input_filename):
  raise RuntimeError("No such file: %s" % input_filename)

if not os.path.isfile(ref_filename):
  raise RuntimeError("No such file: %s" % ref_filename)

out_dirname = os.path.dirname(out_filename)
if not os.path.isdir(out_dirname):
  try:
    os.makedirs(out_dirname)
  except OSError as err:
    raise RuntimeError("Cannot create directory %s because: %s" % (out_dirname, err))

ref_file = ROOT.TFile.Open(ref_filename, 'read')
ref_histogram_names = [ key.GetName() for key in ref_file.GetListOfKeys() ]

histogram_names_base_ref = {}
for ref_histogram_name in ref_histogram_names:
  has_missing_suffix = False
  for suffix in SUFFIXES:
    histogram_name_sys = "{}_{}".format(ref_histogram_name, suffix)
    has_missing_suffix |= histogram_name_sys not in ref_histogram_names
    if has_missing_suffix:
      break
  if not has_missing_suffix and ref_histogram_name.endswith(tuple(MEASUREMENT_MAP.keys())):
    measurement_map_key_match = ''
    for measurement_map_key in MEASUREMENT_MAP:
      if ref_histogram_name.endswith(measurement_map_key):
        measurement_map_key_match = measurement_map_key
        break
    assert(measurement_map_key_match)
    if measurement_map_key_match in histogram_names_base_ref:
      raise RuntimeError(
        "Found duplicates for key %s in file %s: %s and %s" % \
        (measurement_map_key_match, ref_filename, ref_histogram_name, histogram_names_base_ref[measurement_map_key_match])
      )
    histogram_names_base_ref[measurement_map_key_match] = ref_histogram_name
missing_ref_keys = set(MEASUREMENT_MAP.keys()) - set(histogram_names_base_ref.keys())
if missing_ref_keys:
  raise RuntimeError("Missing reference histograms ending with: %s" % ', '.join(sorted(missing_ref_keys)))

def get_binning(histogram, axis_type):
  assert(axis_type in [ 'x', 'y' ])
  axis = histogram.GetXaxis() if axis_type == 'x' else histogram.GetYaxis()
  histogram_binning = [ round(axis.GetBinLowEdge(bin_idx), 3) for bin_idx in range(1, axis.GetNbins() + 2) ]
  return histogram_binning

def get_content(histogram):
  xaxis = histogram.GetXaxis()
  yaxis = histogram.GetYaxis()
  content = []
  for yidx in range(1, yaxis.GetNbins() + 1):
    row = []
    for xidx in range(1, xaxis.GetNbins() + 1):
      row.append(histogram.GetBinContent(xidx, yidx))
    content.append(row)
  return content

def print_histogram(histogram_dict):
  xbins = histogram_dict['xbins']
  ybins = histogram_dict['ybins']
  histogram = histogram_dict['histogram']
  header = [ histogram_dict['name'] ] + [
    '{:.0f}..{:.0f}'.format(xbins[xbin_idx], xbins[xbin_idx + 1]) for xbin_idx in range(len(xbins) - 1)
  ]
  p = prettytable.PrettyTable(header)
  for ybin_idx in reversed(range(len(ybins) - 1)):
    row = ['{}..{}'.format(str(ybins[ybin_idx]), str(ybins[ybin_idx + 1]))]
    row.extend(['{:.6f}'.format(xbin) for xbin in histogram[ybin_idx]])
    p.add_row(row)
  print(p)

def read_histogram(fptr, histogram_name_base, read_sys):
  suffixes = [ '' ]
  if read_sys:
    suffixes.extend(SUFFIXES)
  histograms = {}
  for suffix in suffixes:
    histogram_name = histogram_name_base + ('_{}'.format(suffix) if suffix else '')
    histogram = fptr.Get(histogram_name)
    assert(histogram)
    assert(suffix not in histograms)
    histograms[suffix] = {
      'histogram' : get_content(histogram),
      'xbins'     : get_binning(histogram, 'x'),
      'ybins'     : get_binning(histogram, 'y'),
      'name'      : histogram_name,
    }
  return histograms

ref_histograms = {}
for measurement_map_key in histogram_names_base_ref:
  ref_histograms[measurement_map_key] = read_histogram(ref_file, histogram_names_base_ref[measurement_map_key], True)
ref_file.Close()

rel_histograms = {}
for measurement_map_key in ref_histograms:
  rel_histograms[measurement_map_key] = {}
  ref_xbins = ref_histograms[measurement_map_key]['']['xbins']
  ref_ybins = ref_histograms[measurement_map_key]['']['ybins']
  nbins_x = len(ref_xbins)
  nbins_y = len(ref_ybins)
  for syst in ref_histograms[measurement_map_key]:
    if not syst:
      continue
    for axis_type in [ 'x', 'y' ]:
      if ref_histograms[measurement_map_key]['']['{}bins'.format(axis_type)] != \
         ref_histograms[measurement_map_key][syst]['{}bins'.format(axis_type)]:
        raise RuntimeError(
          "Binning of the %s-axis different b/w nominal and %s in %s" % (axis_type, syst, measurement_map_key)
        )
    rel_histograms[measurement_map_key][syst] = {
      'xbins'     : ref_xbins,
      'ybins'     : ref_ybins,
      'histogram' : [],
      'name'      : '{}_{}_ratio'.format(measurement_map_key, syst),
    }
    for yidx in range(nbins_y - 1):
      row = []
      for xidx in range(nbins_x - 1):
        nominal_content = ref_histograms[measurement_map_key]['']['histogram'][yidx][xidx]
        syst_content = ref_histograms[measurement_map_key][syst]['histogram'][yidx][xidx]
        row.append(syst_content / nominal_content)
      rel_histograms[measurement_map_key][syst]['histogram'].append(row)

input_file = ROOT.TFile.Open(input_filename, 'read')
input_histogram_names = [ key.GetName() for key in input_file.GetListOfKeys() ]
histogram_names_base_input = {}
for input_histogram_name in input_histogram_names:
  for measurement_map_key in MEASUREMENT_MAP:
    measurement_map_key_input = MEASUREMENT_MAP[measurement_map_key]
    if input_histogram_name.endswith(measurement_map_key_input):
      assert(measurement_map_key not in histogram_names_base_input)
      histogram_names_base_input[measurement_map_key] = input_histogram_name
missing_input_keys = set(MEASUREMENT_MAP.keys()) - set(histogram_names_base_input.keys())
if missing_ref_keys:
  raise RuntimeError("Missing input histograms ending with: %s" % ', '.join(sorted(missing_input_keys)))

input_histograms = {}
for measurement_map_key in histogram_names_base_input:
  input_histograms[measurement_map_key] = read_histogram(input_file, histogram_names_base_input[measurement_map_key], False)
input_file.Close()

output_histograms = {}
for measurement_map_key in input_histograms:
  input_histogram = input_histograms[measurement_map_key]['']
  assert(measurement_map_key in rel_histograms)
  output_histograms[measurement_map_key] = {}
  for syst in rel_histograms[measurement_map_key]:
    rel_histogram = rel_histograms[measurement_map_key][syst]
    for axis_type in [ 'x', 'y' ]:
      if input_histogram['{}bins'.format(axis_type)] != rel_histogram['{}bins'.format(axis_type)]:
        raise RuntimeError(
          "Binning of the %s-axis different b/w input and relative %s in %s" % (axis_type, syst, measurement_map_key)
        )
    nbins_x = len(input_histogram['xbins'])
    nbins_y = len(input_histogram['ybins'])
    output_content = []
    for yidx in range(nbins_y - 1):
      row = []
      for xidx in range(nbins_x - 1):
        row.append(rel_histogram['histogram'][yidx][xidx] * input_histogram['histogram'][yidx][xidx])
      output_content.append(row)
    output_histogram_name = '{}_{}'.format(input_histogram['name'], syst)
    assert(output_histogram_name not in input_histogram_names)
    output_histograms[measurement_map_key][syst] = {
      'xbins'     : input_histogram['xbins'],
      'ybins'     : input_histogram['ybins'],
      'histogram' : output_content,
      'name'      :  output_histogram_name,
    }

if verbose:
  for measurement_map_key in ref_histograms:
    for syst in ref_histograms[measurement_map_key]:
      if not syst:
        continue
      print_histogram(ref_histograms[measurement_map_key][''])
      print_histogram(rel_histograms[measurement_map_key][syst])
      print_histogram(input_histograms[measurement_map_key][''])
      print_histogram(output_histograms[measurement_map_key][syst])
      print('=' * 120)

shutil.copy(input_filename, out_filename)
out_file = ROOT.TFile.Open(out_filename, 'update')
out_file.cd()
for measurement_map_key in output_histograms:
  for syst in output_histograms[measurement_map_key]:
    output_histogram = output_histograms[measurement_map_key][syst]
    xaxis = array.array('f', output_histogram['xbins'])
    yaxis = array.array('f', output_histogram['ybins'])
    nbins_x = len(xaxis)
    nbins_y = len(yaxis)
    histogram = ROOT.TH2F(output_histogram['name'], output_histogram['name'], nbins_x - 1, xaxis, nbins_y - 1, yaxis)
    for yidx in range(nbins_y - 1):
      for xidx in range(nbins_x - 1):
        histogram.SetBinContent(xidx + 1, yidx + 1, output_histogram['histogram'][yidx][xidx])
    histogram.Write()
out_file.Close()
