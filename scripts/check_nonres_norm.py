#!/usr/bin/env python

from hhAnalysis.multilepton.common import is_nonresonant
from tthAnalysis.HiggsToTauTau.common import logging, load_samples, SmartFormatter
from HHStatAnalysis.AnalyticalModels.NonResonantModel import NonResonantModel

from rootpy.plotting import Hist2D, Hist

import ROOT
import numpy as np

import argparse
import glob
import os

os.environ["MKL_NUM_THREADS"] = "1"
inputTree = "Events"

nof_weights = 13
klJHEP  = [ 1.0,  7.5,  1.0,  1.0, -3.5,  1.0,  2.4,  5.0, 15.0,  1.0, 10.0,  2.4, 15.0 ]
ktJHEP  = [ 1.0,  1.0,  1.0,  1.0,  1.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.5,  1.0,  1.0 ]
c2JHEP  = [ 0.0, -1.0,  0.5, -1.5, -3.0,  0.0,  0.0,  0.0,  0.0,  1.0, -1.0,  0.0,  1.0 ]
cgJHEP  = [ 0.0,  0.0, -0.8,  0.0,  0.0,  0.8,  0.2,  0.2, -1.0, -0.6,  0.0,  1.0,  0.0 ]
c2gJHEP = [ 0.0,  0.0,  0.6, -0.8,  0.0, -1.0, -0.2, -0.2,  1.0,  0.6,  0.0, -1.0,  0.0 ]

assert(nof_weights == len(klJHEP))
assert(nof_weights == len(ktJHEP))
assert(nof_weights == len(c2JHEP))
assert(nof_weights == len(cgJHEP))
assert(nof_weights == len(c2gJHEP))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    formatter_class = lambda prog: SmartFormatter(prog, max_help_position = 55)
  )
  parser.add_argument('-e', '--era',
    type = str, dest = 'era', metavar = 'year', required = True, choices = [ '2016', '2017', '2018' ],
    help = 'R|Era',
  )
  parser.add_argument('-t', '--type',
    type = str, dest = 'type', metavar = 'type', required = True, choices = [ 'multilepton', 'bbww' ],
    help = 'R|Analysis type',
  )
  parser.add_argument('-v', '--verbose',
    dest = 'verbose', action = 'store_true', default = False, required = False,
    help = 'R|Verbose output',
  )
  args = parser.parse_args()
  era = args.era
  analysis_type = args.type

  if args.verbose:
    logging.getLogger().setLevel(logging.DEBUG)

  cmssw_base = os.environ['CMSSW_BASE']
  model = NonResonantModel()
  coef_file = os.path.join(
    cmssw_base, "src/HHStatAnalysis/AnalyticalModels/data/coefficientsByBin_extended_3M_costHHSim_19-4.txt"
  )
  assert(os.path.isfile(coef_file))
  coefs = model.ReadCoefficients(coef_file)
  hist_file = os.path.join(cmssw_base, "src/Support/NonResonant/Distros_5p_SM3M_sumBenchJHEP_13TeV_19-4.root")
  assert(os.path.isfile(hist_file))
  hist_title = "H1bin4"

  norm = []
  for scan_idx in range(len(klJHEP)):
    norm .append(model.getNormalization(
      klJHEP[scan_idx],
      ktJHEP[scan_idx],
      c2JHEP[scan_idx],
      cgJHEP[scan_idx],
      c2gJHEP[scan_idx],
      hist_file,
      hist_title,
    ))
  samples = load_samples(era, False, base = 'hh_{}'.format(analysis_type))
  denom_file = os.path.join(cmssw_base, 'src/hhAnalysis/bbww/data/denom_{}.root'.format(era))
  fileHH = ROOT.TFile(denom_file, 'read')

  weight_sums = {}
  for dbs_name, sample_info in samples.items():
    if dbs_name == 'sum_events':
      continue
    category = sample_info['sample_category']
    if not is_nonresonant(category):
      continue
    if category not in weight_sums:
      weight_sums[category] = { scan_idx : [] for scan_idx in range(nof_weights) }
    root_files = glob.glob(sample_info["local_paths"][0]['path'] + "/*/*.root")
    logging.debug(
      'Found {} files in sample {} (category {})'.format(
        len(root_files),
        sample_info['process_name_specific'],
        category,
      )
    )

    denom_title = category
    logging.debug('Loading denominator histogram {} from file {}'.format(denom_title, denom_file))
    sumEvt = fileHH.Get(denom_title)
    assert(sumEvt)

    for root_file in root_files:
      logging.debug('Processing file: {}'.format(root_file))
      tfile = ROOT.TFile.Open(root_file, 'read')
      assert(tfile)
      tree = tfile.Get(inputTree)
      assert(tree)

      nof_processed = 0
      for event in tree:
        if nof_processed > 0 and nof_processed % 10000 == 0:
          logging.debug('Processing {}th event in file {}'.format(nof_processed, root_file))
        PHH = []
        for lhe_part_idx in range(event.nLHEPart):
          if event.LHEPart_pdgId[lhe_part_idx] != 25:
            continue
          p4 = ROOT.TLorentzVector()
          p4.SetPtEtaPhiM(
            event.LHEPart_pt  [lhe_part_idx],
            event.LHEPart_eta [lhe_part_idx],
            event.LHEPart_phi [lhe_part_idx],
            event.LHEPart_mass[lhe_part_idx],
          )
          PHH.append(p4)
        assert(len(PHH) == 2)

        PHH_SUM = PHH[0] + PHH[1]
        P1boost = PHH[0]
        P1boost.Boost(-PHH_SUM.BoostVector())
        mhh_gen = PHH_SUM.M()
        cost_gen = abs(P1boost.CosTheta())

        for scan_idx in range(nof_weights):
          denominator = sumEvt.GetBinContent(
            sumEvt.GetXaxis().FindBin(mhh_gen), sumEvt.GetYaxis().FindBin(abs(cost_gen))
          )
          weight = model.getScaleFactor(
            mhh_gen,
            cost_gen,
            klJHEP[scan_idx],
            ktJHEP[scan_idx],
            c2JHEP[scan_idx],
            cgJHEP[scan_idx],
            c2gJHEP[scan_idx],
            denominator,
            norm[scan_idx],
          )
          weight_sums[category][scan_idx].append(weight)
        nof_processed += 1

      logging.debug('Processed {} events in file {}'.format(nof_processed, root_file))
      tfile.Close()

  for category in weight_sums:
    print('Category: {}'.format(category))
    for scan_idx in weight_sums[category]:
      weight_name = 'SM' if scan_idx == 0 else 'BM{}'.format(scan_idx)
      weight_sum = np.sum(weight_sums[category][scan_idx])
      weight_len = len(weight_sums[category][scan_idx])
      print('  {} -> {} ({} events)'.format(weight_name, weight_sum, weight_len))
