from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017 import samples_2017

from collections import OrderedDict as OD

for sample_name, sample_info in samples_2017.items():

  if not isinstance(sample_info, OD):
    continue

  if sample_name.find('HHTo4Tau') != -1:
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
## from collections import OrderedDict as OD
## samples_2017["dummy_signal"] = OD([
##   ("type",                            "mc"),
##   ("sample_category",                 "signal_nonresonant"),
##   ("process_name_specific",           "signal_nonresonant"),
##   ("nof_files",                       15),
##   ("nof_db_files",                    204),
##   ("nof_events",                      {
##     'Count'                                  : [      6960289, ],
##     'CountFullWeighted'                      : [      9222143,      9222155,      9221194, ],
##     'CountWeighted'                          : [      6889926,      6890489,      6890703, ],
##     'CountFullWeightedNoPU'                  : [      9226179, ],
##     'CountWeightedNoPU'                      : [      6890129, ],
##     'CountWeightedLHEWeightScale'            : [      6609896,      7035521,      7270942,      6424340,      6889926,      7186405,      6276790,      6774670,      7119048, ],
##     'CountWeightedLHEWeightScaleNoPU'        : [      6609918,      7035554,      7270992,      6424353,      6890129,      7186420,      6276767,      6774523,      7118960, ],
##     'CountFullWeightedLHEWeightScale'        : [      8846685,      9416403,      9731421,      8598355,      9222143,      9618281,      8400869,      9067135,      9528147, ],
##     'CountFullWeightedLHEWeightScaleNoPU'    : [      8846737,      9416372,      9731495,      8598374,      9226179,      9618305,      8400832,      9067034,      9528022, ],
##   }),
##   ("nof_tree_events",                 6960289),
##   ("nof_db_events",                   6960289),
##   ("fsize_local",                     9479023450), # 9.48GB, avg file size 631.93MB
##   ("fsize_db",                        322020515003), # 322.02GB, avg file size 1.58GB
##   ("use_it",                          True),
##   ("xsection",                        1.256),
##   ("genWeight",                       True),
##   ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
##   ("has_LHE",                         True),
##   ("local_paths",
##     [
##       OD([
##         ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Jul12_woPresel_nom_all/ntuples/ZZTo4L"),
##         ("selection", "*"),
##         ("blacklist", []),
##       ]),
##     ]
##   ),
##   ("missing_from_superset",           [
##     # not computed
##   ]),
##   ("missing_hlt_paths",               [
##
##   ]),
##   ("hlt_paths",               [
##     # not computed
##   ]),
## ])
