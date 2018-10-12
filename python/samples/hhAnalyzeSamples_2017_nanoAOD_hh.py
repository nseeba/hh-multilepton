from collections import OrderedDict as OD

# file generated at 2018-10-12 13:16:14 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh.py -p /hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26 -Z zeroes.txt -z zombies.txt -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_nanoAOD_hh.py -M

samples_2017 = OD()
samples_2017["/GluGluToHHTo4Tau_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_node_9_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     850198053), # 850.20MB, avg file size 106.27MB
  ("fsize_db",                        21901746830), # 21.90GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/GluGluToHHTo4Tau_node_9_13TeV-madgraph_correctedcfg/NanoProduction_v2_2018Sep26_GluGluToHHTo4Tau_node_9_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_161339"),
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

samples_2017["/VBFHHTo4Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_4t"),
  ("nof_files",                       9),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     666422417), # 666.42MB, avg file size 74.05MB
  ("fsize_db",                        20516924301), # 20.52GB, avg file size 892.04MB
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26/VBFHHTo4Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/NanoProduction_v2_2018Sep26_VBFHHTo4Tau_CV_1_C2V_1_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/180926_161658"),
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

samples_2017["sum_events"] = [
]

