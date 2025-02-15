#!/usr/bin/env python

from hhAnalysis.multilepton.configs.analyzeConfig_conversions import analyzeConfig_conversions
from hhAnalysis.multilepton.common import get_histograms_to_fit
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_multilepton as load_samples, load_samples_stitched

import os
import sys
import getpass

# E.g.: ./test/hhAnalyzeRun_conversions.py -e 2016 -v version -m default -c -ele_ConvsCR invert_eitherOf_convsVeto_nLostHits -A  -s full -G


mode_choices     = [ 'default', 'forBDTtraining' ]
sys_choices      = [ 'full', 'internal' ] + systematics.an_opts_hh_multilepton_wAK8
systematics.full = systematics.an_hh_multilepton_wAK8
systematics.internal = systematics.an_internal_no_mem

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_preselect()
parser.add_rle_select()
parser.add_lep_mva_wp(default_wp = 'hh_multilepton') # alternative: hh_multilepton
parser.add_ele_ConvsCR(default_option = 'invert_eitherOf_convsVeto_nLostHits') # ['disable_nLostHits_convsVeto', 'invert_nLostHits', 'invert_convsVeto', 'invert_eitherOf_convsVeto_nLostHits', 'invert_both_convsVeto_nLostHits'] 
parser.add_nonnominal()
parser.add_hlt_filter()
parser.add_files_per_job()
parser.add_use_home()
parser.add_jet_cleaning()
parser.add_gen_matching()
parser.add_sideband()
parser.add_tau_id()
parser.enable_regrouped_jerc(default = 'jes')
parser.add_split_trigger_sys()
parser.add_control_region()
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
keep_logs          = args.keep_logs

# Additional arguments
mode              = args.mode
systematics_label = args.systematics
use_preselected   = args.use_preselected
rle_select        = os.path.expanduser(args.rle_select)
use_nonnominal    = args.original_central
hlt_filter        = args.hlt_filter
lep_mva_wp        = args.lep_mva_wp
ele_ConvsCR       = args.ele_ConvsCR
files_per_job     = args.files_per_job
use_home          = args.use_home
sideband          = args.sideband
tau_id            = args.tau_id
jet_cleaning      = args.jet_cleaning
gen_matching      = args.gen_matching
regroup_jerc      = args.enable_regrouped_jerc
split_trigger_sys = args.split_trigger_sys
control_region    = args.control_region

if lep_mva_wp != "hh_multilepton" and use_preselected:
  raise RuntimeError("Cannot use skimmed samples while tightening the prompt lepton MVA cut")

if regroup_jerc:
  if 'full' not in systematics_label:
    raise RuntimeError("Regrouped JEC or split JER was enabled but not running with full systematics")
  if regroup_jerc == 'both':
    systematics.full.extend(systematics.JEC_regrouped + systematics.JER_split)
  elif regroup_jerc == 'jes':
    systematics.full.extend(systematics.JEC_regrouped)
  elif regroup_jerc == 'jer':
    systematics.full.extend(systematics.JER_split)
  else:
    raise RuntimeError("Invalid choice: %s" % regroup_jerc)
if split_trigger_sys == 'yes':
  for trigger_sys in systematics.triggerSF:
    del systematics.internal[systematics.internal.index(trigger_sys)]
    del systematics.full[systematics.full.index(trigger_sys)]
if split_trigger_sys in [ 'yes', 'both' ]:
  systematics.internal.extend(systematics.triggerSF_3l)
  systematics.full.extend(systematics.triggerSF_3l)

# Use the arguments
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)
do_sync = mode.startswith('sync')
lumi = get_lumi(era)
jet_cleaning_by_index = (jet_cleaning == 'by_index')
gen_matching_by_index = (gen_matching == 'by_index')

if sideband == 'disabled':
  leptonChargeSelections = [ "OS" ]
elif sideband == 'enabled':
  leptonChargeSelections = [ "OS", "SS" ]
elif sideband == 'only':
  leptonChargeSelections = [ "SS" ]
else:
  raise ValueError("Invalid choice for the sideband: %s" % sideband)

if mode == "default":
  samples = load_samples(era, suffix = "preselected" if use_preselected else "")
  samples = load_samples_stitched(samples, era, [ 'dy_nlo', 'wjets' ])
elif mode == "forBDTtraining":
  if use_preselected:
    raise ValueError("Producing Ntuples for BDT training from preselected Ntuples makes no sense!")

  samples = load_samples(era, suffix = "BDT")
  samples = load_samples_stitched(samples, era, [ 'dy_lo' ])

else:
  raise ValueError("Invalid mode: %s" % mode)

hadTauWP_veto_map = {
  #'dR03mva' : 'Loose',
  #'deepVSj' : 'Loose',
  'dR03mva' : 'Medium',
  'deepVSj' : 'Medium', 
}
hadTau_selection_veto = tau_id + hadTauWP_veto_map[tau_id]

for sample_name, sample_info in samples.items():
  if sample_name == 'sum_events': continue
  if sample_name.startswith('/Tau/Run'):
    sample_info["use_it"] = False


if __name__ == '__main__':
  print "\n\nget_histograms_to_fit(EventCounter): {}\n\n".format(get_histograms_to_fit("EventCounter"))
  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shifts)
  )
  if not use_preselected:
    logging.warning('Running the analysis on fully inclusive samples!')

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  histograms_to_fit = None
  if control_region:
    histograms_to_fit = {
    "EventCounter" : {},
    "m3l"      : {},
    "dihiggsVisMass_sel"      : {},
    "mSFOS2l_closestToZ"      : {},
    "dr_LeptonIdx3_AK4jNear_Approach2"      : {},
    "dr_LeptonIdx3_2j_inclusive1j_Approach2"      : {},
    "dr_los_min"      : {},
    "dr_los_max"      : {},
    "numSameFlavor_OS_3l"      : {},      
    "met_LD"      : {},
    "numElectrons"      : {},
    "numMuons"      : {},
    "nJetAK4"      : {},
    "nJetAK8_wSelectorAK8_Wjj"      : {},
    #
    "mT_WZctrl_leptonW_MET"      : {},
    #
    "jetMass_sel_WZctrl_2lss"      : {},
    "leptonPairMass_sel_WZctrl_2lss"      : {},      
    "mindr_lep1_jet_WZctrl_2lss"      : {},
    "mT_lep1_WZctrl_2lss"      : {},
    "mindr_lep2_jet_WZctrl_2lss"      : {},      
    "mT_lep2_WZctrl_2lss"      : {},
    "dR_ll_WZctrl_2lss"      : {},
    "max_lep_eta_WZctrl_2lss"      : {},
    "MVAOutput_allBMs"   : {},
  }
  else:
    histograms_to_fit = get_histograms_to_fit("EventCounter","m3l","dihiggsVisMass_sel","mSFOS2l_closestToZ","dr_LeptonIdx3_AK4jNear_Approach2","dr_LeptonIdx3_2j_inclusive1j_Approach2","dr_los_min","dr_los_max","numSameFlavor_OS_3l","met_LD","numElectrons","numMuons","nJetAK4","nJetAK8_wSelectorAK8_Wjj")
  
  analysis = analyzeConfig_conversions(
    configDir = os.path.join("/scratch-persistent", getpass.getuser(), "hhAnalysis", era, version),
    localDir  = os.path.join("/home",               getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local",         getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze_conversions",
    cfgFile_analyze                       = "analyze_conversions_cfg.py",
    samples                               = samples,
    hadTauVeto_selection                  = hadTau_selection_veto,
    applyFakeRateWeights                  = "3lepton",
    leptonChargeSelections                = leptonChargeSelections,
    central_or_shifts                     = central_or_shifts,
    lep_mva_wp                            = lep_mva_wp,
    ele_ConvsCR                           = ele_ConvsCR,
    jet_cleaning_by_index                 = jet_cleaning_by_index,
    gen_matching_by_index                 = gen_matching_by_index,
    max_files_per_job                     = files_per_job,
    era                                   = era,
    isControlRegion                       = control_region,
    use_lumi                              = True,
    lumi                                  = lumi,
    check_output_files                    = check_output_files,
    running_method                        = running_method,
    num_parallel_jobs                     = num_parallel_jobs,
    executable_addBackgrounds             = "addBackgrounds",
    executable_addBackgroundJetToTauFakes = "addBackgroundLeptonFakes",
    histograms_to_fit                     = histograms_to_fit,
    select_rle_output                     = True,
    select_root_output                    = False,
    dry_run                               = dry_run,
    do_sync                               = do_sync,
    isDebug                               = debug,
    rle_select                            = rle_select,
    use_nonnominal                        = use_nonnominal,
    hlt_filter                            = hlt_filter,
    use_home                              = use_home,
    keep_logs                             = keep_logs,
    submission_cmd                        = sys.argv,
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
