#!/usr/bin/env python

from hhAnalysis.multilepton.configs.analyzeConfig_hh_2lss import analyzeConfig_hh_2lss
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_multilepton as load_samples

import os
import sys
import getpass

# E.g.: ./test/hhAnalyzeRun_2lss.py -v 2017Dec13 -m default -e 2017

mode_choices     = [ 'default', 'forBDTtraining' ]
sys_choices      = [ 'full' ] + systematics.an_extended_opts_hh
systematics.full = systematics.an_extended_hh

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_nonnominal()
parser.add_hlt_filter()
parser.add_files_per_job()
parser.add_use_home()
parser.add_lep_mva_wp()
args = parser.parse_args()

# Common arguments
era                = args.era
version            = args.version
dry_run            = args.dry_run
no_exec            = args.no_exec
auto_exec          = args.auto_exec
check_output_files = not args.not_check_input_files
debug              = args.debug
sample_filter      = args.filter
num_parallel_jobs  = args.num_parallel_jobs
running_method     = args.running_method

# Additional arguments
mode              = args.mode
systematics_label = args.systematics
use_nonnominal    = args.original_central
hlt_filter        = args.hlt_filter
files_per_job     = args.files_per_job
use_home          = args.use_home
lep_mva_wp        = args.lep_mva_wp

# Use the arguments
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)
lumi = get_lumi(era)

if mode == "default":
  samples = load_samples(era, suffix = "preselected" if use_preselected else "")
  samples_wjets = load_samples(era, suffix = "wjets_preselected" if use_preselected else "wjets")


  for sample_name, sample_info in samples.items():
    if sample_name == 'sum_events':
      continue
    if sample_info['process_name_specific'] in [ 'WpWpJJ_EWK_QCD_v14-v1', 'TTGJets_ext1' ]:
      sample_info['use_it'] = False
    elif sample_info['process_name_specific'] in [ 'WpWpJJ_EWK_QCD', 'TTGJets' ]:
      sample_info['use_it'] = True

    # since we run the regular analysis on "part1" of W+jets samples and reserve "part2" for the BDT training,
    # we have to make sure that we don't use the non-split W+jets samples at all
    if ('%s/part1' % sample_name) in samples_wjets or ('%s/part2' % sample_name) in samples_wjets:
      sample_info['use_it'] = False
    if sample_name.endswith('/part1'):
      sample_info['use_it'] = True
    if sample_name.endswith('/part2'):
      sample_info['use_it'] = False

  hadTau_veto = "dR03mvaMedium"

elif mode == "forBDTtraining":

  samples = load_samples(era, suffix = "BDT")
  samples_wjets = load_samples(era, suffix = "wjets")


  for sample_name, sample_info in samples.items():
    if sample_name == 'sum_events':
      continue
    if sample_info['process_name_specific'] in [ 'WpWpJJ_EWK_QCD_v14-v1', 'TTGJets_ext1' ]:
      sample_info['use_it'] = True
    elif sample_info['process_name_specific'] in [ 'WpWpJJ_EWK_QCD', 'TTGJets' ]:
      sample_info['use_it'] = False

    # since we run the regular analysis on "part1" of W+jets samples and reserve "part2" for the BDT training,
    # we have to make sure that we don't use the non-split W+jets samples at all
    if ('%s/part1' % sample_name) in samples_wjets or ('%s/part2' % sample_name) in samples_wjets:
      sample_info['use_it'] = False
    if sample_name.endswith('/part1'):
      sample_info['use_it'] = False
    if sample_name.endswith('/part2'):
      sample_info['use_it'] = True

  hadTau_veto = "dR03mvaMedium"

else:
  raise ValueError("Internal logic error")

if __name__ == '__main__':
  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shifts)
  )

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  analysis = analyzeConfig_hh_2lss(
    configDir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze_hh_2lss",
    cfgFile_analyze                       = "analyze_hh_2lss_cfg.py",
    samples                               = samples,
    lep_mva_wp                            = lep_mva_wp,
    hadTauVeto_selection                  = hadTau_veto,
    applyFakeRateWeights                  = "2lepton",
    central_or_shifts                     = central_or_shifts,
    max_files_per_job                     = files_per_job,
    era                                   = era,
    use_lumi                              = True,
    lumi                                  = lumi,
    check_output_files                    = check_output_files,
    running_method                        = running_method,
    num_parallel_jobs                     = num_parallel_jobs,
    executable_addBackgrounds             = "addBackgrounds",
    executable_addFakes                   = "addBackgroundLeptonFakes",
    executable_addFlips                   = "addBackgroundLeptonFlips",
    histograms_to_fit                     = {
#      "EventCounter"                      : {},
#      "numJets"                           : {},
      "dihiggsVisMass"                    : {},
#      "HT"                                : {},
#      "STMET"                             : {},
#      "BDTOutput_SUM"                     : {}
      "BDTOutput_SUM_gen_mHH_400"         : {},
      "BDTOutput_SUM_gen_mHH_700"         : {},
    },
    select_rle_output                     = True,
    dry_run                               = dry_run,
    isDebug                               = debug,
    use_nonnominal                        = use_nonnominal,
    hlt_filter                            = hlt_filter,
    use_home                              = use_home,
  )

  if mode == "forBDTtraining":
    analysis.set_BDT_training()

  job_statistics = analysis.create()
  for job_type, num_jobs in job_statistics.items():
    logging.info(" #jobs of type '%s' = %i" % (job_type, num_jobs))

  if auto_exec:
    run_analysis = True
  elif no_exec:
    run_analysis = False
  else:
    run_analysis = query_yes_no("Start jobs ?")
  if run_analysis:
    analysis.run()
  else:
    sys.exit(0)
