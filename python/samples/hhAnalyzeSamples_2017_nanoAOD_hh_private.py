from collections import OrderedDict as OD

# file generated at 2018-08-03 20:22:51 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_private_hh.py -p /hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Aug03 -Z zeroes.txt -z zombies.txt -N samples_2017 -E 2017 -g hhAnalyzeSamples_2017_nanoAOD_hh_private.py -o python/samples -M

samples_2017 = OD()
samples_2017["/HHTo4T_madgraph_pythia8_CP5_M400/private/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "hh_4t_400"),
  ("nof_files",                       193),
  ("nof_db_files",                    193),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1199395866), # 1.20GB, avg file size 6.21MB
  ("fsize_db",                        22408025117), # 22.41GB, avg file size 116.10MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Aug03/HHTo4T_madgraph_pythia8_CP5_M400/NanoProduction_v2_2018Aug03_HHTo4T_madgraph_pythia8_CP5_M400__private/000000_000000"),
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

samples_2017["/HHTo4T_madgraph_pythia8_CP5_M700/private/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "hh_4t_700"),
  ("nof_files",                       160),
  ("nof_db_files",                    160),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 311998),
  ("nof_db_events",                   311998),
  ("fsize_local",                     1084228332), # 1.08GB, avg file size 6.78MB
  ("fsize_db",                        19502577906), # 19.50GB, avg file size 121.89MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Aug03/HHTo4T_madgraph_pythia8_CP5_M700/NanoProduction_v2_2018Aug03_HHTo4T_madgraph_pythia8_CP5_M700__private/000000_000000"),
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

