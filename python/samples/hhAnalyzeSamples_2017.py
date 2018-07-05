from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017 import samples_2017

samples = samples_2017
for sample_name, sample_info in samples.items():
  if sample_name.find('HHTo4Tau'):
    sample_info["use_it"] = True

  if sample_name.startswith('/ZZ'):
    sample_info["sample_category"] = "ZZ"
  elif sample_name.startswith('/WZ'):
    sample_info["sample_category"] = "WZ"
  elif sample_name.startswith('/WW'):
    sample_info["sample_category"] = "WW"
  elif sample_name.startswith('/DY') and sample_name.find('JetsToLL') < 10:
    sample_info["sample_category"] = "DY"
  elif sample_name.startswith('/W') and sample_name.find('JetsToLNu') < 10:
    sample_info["sample_category"] = "W"
  elif sample_name.startswith('/ttH'):
    sample_info["sample_category"] = "TTH"

  if sample_info["sample_category"] == "Rares":
    sample_info["sample_category"] = "Other"
  if sample_info["sample_category"] in [ "tHq", "tHW" ]:
    sample_info["sample_category"] = "TH"

# CV: add dummy signal MC sample for testing
from collections import OrderedDict as OD
samples_2017["dummy_signal"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_nonresonant"),
  ("process_name_specific",           "signal_nonresonant"),
  ("nof_files",                       15),
  ("nof_db_files",                    204),
  ("nof_events",                      { 
    'Count'                                  : [    102677048, ],
    'CountFullWeighted'                      : [    136028285,    136030878,    136039542, ],
    'CountWeightedLHEWeightScale'            : [     97505821,    103781241,    107198791,     94770105,    101623232,    105985610,     92423618,     99723949,    104767273, ],
    'CountWeighted'                          : [    101623232,    101643722,    101637259, ],
  }),
  ("nof_tree_events",                 6960289),
  ("nof_db_events",                   6960289),
  ("fsize_local",                     8954705185), # 8.95GB, avg file size 596.98MB
  ("fsize_db",                        322020515003), # 322.02GB, avg file size 1.58GB
  ("use_it",                          True),
  ("xsection",                        1.256*1.e-2),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Jul02_woPresel_nom_all/ntuples/ZZTo4L"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_from_superset",           [
    # not computed
  ]),
  ("missing_hlt_paths",               [

  ]),
  ("hlt_paths",               [
    # not computed
  ]),
])
