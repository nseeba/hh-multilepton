#!/usr/bin/env python
import os, logging, sys, getpass
from collections import OrderedDict as OD
from hhAnalysis.tttt.configs.analyzeConfig_SVfit4tau import analyzeConfig_SVfit4tau
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser

parser = tthAnalyzeParser()
parser.add_lep_mva_wp()
args = parser.parse_args()

# Common arguments
era                  = args.era
version              = args.version
dry_run              = args.dry_run
no_exec              = args.no_exec
auto_exec            = args.auto_exec
check_output_files   = not args.not_check_input_files
debug                = args.debug
sample_filter        = args.filter
num_parallel_jobs    = args.num_parallel_jobs
running_method       = args.running_method

# Additional arguments
lep_mva_wp           = args.lep_mva_wp

# Use the arguments
max_job_resubmission = 3;
central_or_shift     = [ "central" ]
max_files_per_job    = 1

if era == "2016":
  from hhAnalysis.tttt.samples.hhAnalyzeSamples_2016 import samples_2016 as samples
elif era == "2017":
  from hhAnalysis.tttt.samples.hhAnalyzeSamples_2017 import samples_2017 as samples
elif era == "2018":
  from hhAnalysis.tttt.samples.hhAnalyzeSamples_2018 import samples_2018 as samples
else:
  raise ValueError("Invalid era: %s" % era)

if era == "2016":
  from tthAnalysis.HiggsToTauTau.analysisSettings import lumi_2016 as lumi
elif era == "2017":
  from tthAnalysis.HiggsToTauTau.analysisSettings import lumi_2017 as lumi
elif era == "2018":
  from tthAnalysis.HiggsToTauTau.analysisSettings import lumi_2018 as lumi
else:
  raise ValueError("Invalid era: %s" % era)

for sample_name, sample_info in samples.items():
  if not isinstance(sample_info, OD):
    continue
  if sample_info["process_name_specific"] in [ "x_to_hh_300", "x_to_hh_500", "x_to_hh_800" ]:
    sample_info["use_it"] = True
  else:
    sample_info["use_it"] = False

if __name__ == '__main__':
  logging.basicConfig(
    stream = sys.stdout,
    level  = logging.INFO,
    format = '%(asctime)s - %(levelname)s: %(message)s',
  )

  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shift)
  )
  
  analysis = analyzeConfig_SVfit4tau(
    configDir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze              = "analyze_SVfit4tau",
    cfgFile_analyze                 = "analyze_SVfit4tau_cfg.py",
    samples                         = samples,
    lepton_selection                = "Tight",
    lep_mva_wp                      = lep_mva_wp,
    hadTau_selection                = "Tight|dR03mvaMedium",
    SVfit4tau_logM_wMassConstraint  = [ 0., 2., 4., 6., 8., 10. ],
    SVfit4tau_logM_woMassConstraint = [ 0., 2., 4., 6., 8., 10. ],
    modes                           = [ "rec", "gen", "gen_smeared" ],
    central_or_shifts               = central_or_shift,
    max_files_per_job               = max_files_per_job,
    era                             = era,
    use_lumi                        = True,
    lumi                            = lumi,
    check_output_files              = check_output_files,
    running_method                  = "sbatch",
    num_parallel_jobs               = 100, # KE: run up to 100 'hadd' jobs in parallel on batch system
    dry_run                         = dry_run,
    isDebug                         = debug,
  )

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
