from collections import OrderedDict as OD

# file generated at 2020-01-13 17:24:11 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_hh.py -M

samples_2016 = OD()
samples_2016["/GluGluToRadionToHHTo4Tau_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99984,       100003,        99998, ],
    'CountWeightedLHEWeightScale'                                : [       101618,        99984,        97814,       101618,        99984,        97814,       101618,        99984,        97814, ],
    'CountWeightedL1PrefireNom'                                  : [        98540,        98549,        98553, ],
    'CountWeightedL1Prefire'                                     : [        98540,        98152,        98925, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100133,        98540,        96407,       100133,        98540,        96407,       100133,        98540,        96407, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     330561599), # 330.56MB, avg file size 330.56MB
  ("fsize_db",                        3874786969), # 3.87GB, avg file size 1.94GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        99204, ],
    'CountWeighted'                                              : [        99196,        99211,        99225, ],
    'CountWeightedLHEWeightScale'                                : [       101102,        99195,        96802,       101102,        99195,        96802,       101102,        99195,        96802, ],
    'CountWeightedL1PrefireNom'                                  : [        97727,        97730,        97750, ],
    'CountWeightedL1Prefire'                                     : [        97727,        97334,        98116, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        99589,        97726,        95375,        99589,        97726,        95375,        99589,        97726,        95375, ],
  }),
  ("nof_tree_events",                 99204),
  ("nof_db_events",                   99204),
  ("fsize_local",                     331297043), # 331.30MB, avg file size 331.30MB
  ("fsize_db",                        3865138450), # 3.87GB, avg file size 3.87GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99999,        99998,        99998, ],
    'CountWeightedLHEWeightScale'                                : [       102215,        99993,        97336,       102215,        99993,        97336,       102215,        99993,        97336, ],
    'CountWeightedL1PrefireNom'                                  : [        98441,        98437,        98445, ],
    'CountWeightedL1Prefire'                                     : [        98441,        98029,        98850, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100610,        98438,        95830,       100610,        98438,        95830,       100610,        98438,        95830, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     337584166), # 337.58MB, avg file size 337.58MB
  ("fsize_db",                        3829876445), # 3.83GB, avg file size 1.91GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-280_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98567, ],
    'CountWeighted'                                              : [        98563,        98576,        98558, ],
    'CountWeightedLHEWeightScale'                                : [       101012,        98563,        95735,       101012,        98563,        95735,       101012,        98563,        95735, ],
    'CountWeightedL1PrefireNom'                                  : [        97006,        97012,        97007, ],
    'CountWeightedL1Prefire'                                     : [        97006,        96596,        97416, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        99401,        97004,        94232,        99401,        97004,        94232,        99401,        97004,        94232, ],
  }),
  ("nof_tree_events",                 98567),
  ("nof_db_events",                   98567),
  ("fsize_local",                     335720902), # 335.72MB, avg file size 335.72MB
  ("fsize_db",                        3900002340), # 3.90GB, avg file size 1.95GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        94730, ],
    'CountWeighted'                                              : [        94729,        94718,        94717, ],
    'CountWeightedLHEWeightScale'                                : [        97556,        94727,        91626,        97556,        94727,        91626,        97556,        94727,        91626, ],
    'CountWeightedL1PrefireNom'                                  : [        93173,        93165,        93167, ],
    'CountWeightedL1Prefire'                                     : [        93173,        92765,        93579, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        95938,        93171,        90131,        95938,        93171,        90131,        95938,        93171,        90131, ],
  }),
  ("nof_tree_events",                 94730),
  ("nof_db_events",                   94730),
  ("fsize_local",                     328819618), # 328.82MB, avg file size 328.82MB
  ("fsize_db",                        3783167238), # 3.78GB, avg file size 1.89GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-320_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99993,       100014,       100014, ],
    'CountWeightedLHEWeightScale'                                : [       103477,        99993,        96339,       103477,        99993,        96339,       103477,        99993,        96339, ],
    'CountWeightedL1PrefireNom'                                  : [        98258,        98267,        98275, ],
    'CountWeightedL1Prefire'                                     : [        98258,        97808,        98708, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       101661,        98257,        94676,       101661,        98257,        94676,       101661,        98257,        94676, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     352683594), # 352.68MB, avg file size 352.68MB
  ("fsize_db",                        3916703835), # 3.92GB, avg file size 1.96GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-340_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_340_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_340_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99985,       100032,       100019, ],
    'CountWeightedLHEWeightScale'                                : [       103908,        99985,        95996,       103908,        99985,        95996,       103908,        99985,        95996, ],
    'CountWeightedL1PrefireNom'                                  : [        98169,        98192,        98194, ],
    'CountWeightedL1Prefire'                                     : [        98169,        97699,        98636, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       101998,        98169,        94258,       101998,        98169,        94258,       101998,        98169,        94258, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     358885028), # 358.89MB, avg file size 358.89MB
  ("fsize_db",                        3984955042), # 3.98GB, avg file size 1.99GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_340_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98356, ],
    'CountWeighted'                                              : [        98341,        98357,        98369, ],
    'CountWeightedLHEWeightScale'                                : [       102414,        98340,        94246,       102414,        98340,        94246,       102414,        98340,        94246, ],
    'CountWeightedL1PrefireNom'                                  : [        96558,        96569,        96575, ],
    'CountWeightedL1Prefire'                                     : [        96558,        96098,        97018, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100536,        96557,        92545,       100536,        96557,        92545,       100536,        96557,        92545, ],
  }),
  ("nof_tree_events",                 98356),
  ("nof_db_events",                   98356),
  ("fsize_local",                     356033371), # 356.03MB, avg file size 356.03MB
  ("fsize_db",                        4031403477), # 4.03GB, avg file size 2.02GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        97614, ],
    'CountWeighted'                                              : [        97611,        97628,        97620, ],
    'CountWeightedLHEWeightScale'                                : [       102562,        97609,        92819,       102562,        97609,        92819,       102562,        97609,        92819, ],
    'CountWeightedL1PrefireNom'                                  : [        95699,        95704,        95709, ],
    'CountWeightedL1Prefire'                                     : [        95699,        95213,        96184, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100536,        95697,        91012,       100536,        95697,        91012,       100536,        95697,        91012, ],
  }),
  ("nof_tree_events",                 97614),
  ("nof_db_events",                   97614),
  ("fsize_local",                     365937949), # 365.94MB, avg file size 365.94MB
  ("fsize_db",                        4056144350), # 4.06GB, avg file size 2.03GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100036,       100015,        99983, ],
    'CountWeightedLHEWeightScale'                                : [       105910,       100036,        94448,       105910,       100036,        94448,       105910,       100036,        94448, ],
    'CountWeightedL1PrefireNom'                                  : [        97957,        97941,        97931, ],
    'CountWeightedL1Prefire'                                     : [        97957,        97438,        98476, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       103706,        97957,        92512,       103706,        97957,        92512,       103706,        97957,        92512, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     386826454), # 386.83MB, avg file size 386.83MB
  ("fsize_db",                        4254873375), # 4.25GB, avg file size 2.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49999,        50002,        50005, ],
    'CountWeightedLHEWeightScale'                                : [        53312,        49998,        46947,        53312,        49998,        46947,        53312,        49998,        46947, ],
    'CountWeightedL1PrefireNom'                                  : [        48939,        48938,        48944, ],
    'CountWeightedL1Prefire'                                     : [        48939,        48672,        49204, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        52173,        48937,        45957,        52173,        48937,        45957,        52173,        48937,        45957, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     199498480), # 199.50MB, avg file size 199.50MB
  ("fsize_db",                        2208888272), # 2.21GB, avg file size 2.21GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        50001,        50003,        50004, ],
    'CountWeightedLHEWeightScale'                                : [        53645,        50001,        46695,        53645,        50001,        46695,        53645,        50001,        46695, ],
    'CountWeightedL1PrefireNom'                                  : [        48894,        48893,        48897, ],
    'CountWeightedL1Prefire'                                     : [        48894,        48618,        49170, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        52448,        48894,        45668,        52448,        48894,        45668,        52448,        48894,        45668, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     204206543), # 204.21MB, avg file size 204.21MB
  ("fsize_db",                        2111067830), # 2.11GB, avg file size 2.11GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        50001,        50002,        50000, ],
    'CountWeightedLHEWeightScale'                                : [        53935,        49999,        46475,        53935,        49999,        46475,        53935,        49999,        46475, ],
    'CountWeightedL1PrefireNom'                                  : [        48857,        48855,        48860, ],
    'CountWeightedL1Prefire'                                     : [        48857,        48574,        49140, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        52693,        48856,        45419,        52693,        48856,        45419,        52693,        48856,        45419, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     208597091), # 208.60MB, avg file size 208.60MB
  ("fsize_db",                        2253668540), # 2.25GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        48463, ],
    'CountWeighted'                                              : [        48471,        48462,        48468, ],
    'CountWeightedLHEWeightScale'                                : [        52538,        48471,        44855,        52538,        48471,        44855,        52538,        48471,        44855, ],
    'CountWeightedL1PrefireNom'                                  : [        47322,        47318,        47319, ],
    'CountWeightedL1Prefire'                                     : [        47322,        47040,        47605, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51288,        47322,        43801,        51288,        47322,        43801,        51288,        47322,        43801, ],
  }),
  ("nof_tree_events",                 48463),
  ("nof_db_events",                   48463),
  ("fsize_local",                     206281525), # 206.28MB, avg file size 206.28MB
  ("fsize_db",                        2355229431), # 2.36GB, avg file size 2.36GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-700_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49998,        49998,        49996, ],
    'CountWeightedLHEWeightScale'                                : [        54453,        49996,        46092,        54453,        49996,        46092,        54453,        49996,        46092, ],
    'CountWeightedL1PrefireNom'                                  : [        48801,        48797,        48804, ],
    'CountWeightedL1Prefire'                                     : [        48801,        48508,        49095, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53141,        48800,        44995,        53141,        48800,        44995,        53141,        48800,        44995, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     216710254), # 216.71MB, avg file size 216.71MB
  ("fsize_db",                        2263100514), # 2.26GB, avg file size 2.26GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-750_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49996,        50008,        50001, ],
    'CountWeightedLHEWeightScale'                                : [        54679,        49996,        45926,        54679,        49996,        45926,        54679,        49996,        45926, ],
    'CountWeightedL1PrefireNom'                                  : [        48788,        48797,        48788, ],
    'CountWeightedL1Prefire'                                     : [        48788,        48492,        49085, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53349,        48788,        44821,        53349,        48788,        44821,        53349,        48788,        44821, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     220048232), # 220.05MB, avg file size 220.05MB
  ("fsize_db",                        2299577348), # 2.30GB, avg file size 1.15GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        50007,        50002,        49998, ],
    'CountWeightedLHEWeightScale'                                : [        54895,        50007,        45768,        54895,        50007,        45768,        54895,        50007,        45768, ],
    'CountWeightedL1PrefireNom'                                  : [        48787,        48785,        48780, ],
    'CountWeightedL1Prefire'                                     : [        48787,        48488,        49086, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53550,        48786,        44659,        53550,        48786,        44659,        53550,        48786,        44659, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     223168840), # 223.17MB, avg file size 223.17MB
  ("fsize_db",                        2263981849), # 2.26GB, avg file size 2.26GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        50002,        50002,        49994, ],
    'CountWeightedLHEWeightScale'                                : [        55277,        50002,        45489,        55277,        50002,        45489,        55277,        50002,        45489, ],
    'CountWeightedL1PrefireNom'                                  : [        48749,        48747,        48746, ],
    'CountWeightedL1Prefire'                                     : [        48749,        48445,        49054, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53886,        48749,        44356,        53886,        48749,        44356,        53886,        48749,        44356, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     228014726), # 228.01MB, avg file size 228.01MB
  ("fsize_db",                        2478591891), # 2.48GB, avg file size 2.48GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99430, ],
    'CountWeighted'                                              : [        99434,        99436,        99429, ],
    'CountWeightedLHEWeightScale'                                : [       101035,        99434,        97262,       101035,        99434,        97262,       101035,        99434,        97262, ],
    'CountWeightedL1PrefireNom'                                  : [        97938,        97937,        97942, ],
    'CountWeightedL1Prefire'                                     : [        97938,        97542,        98334, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        99506,        97938,        95810,        99506,        97938,        95810,        99506,        97938,        95810, ],
  }),
  ("nof_tree_events",                 99430),
  ("nof_db_events",                   99430),
  ("fsize_local",                     333600026), # 333.60MB, avg file size 333.60MB
  ("fsize_db",                        3877049177), # 3.88GB, avg file size 1.94GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        97772, ],
    'CountWeighted'                                              : [        97742,        97774,        97762, ],
    'CountWeightedLHEWeightScale'                                : [        99651,        97742,        95393,        99651,        97742,        95393,        99651,        97742,        95393, ],
    'CountWeightedL1PrefireNom'                                  : [        96246,        96259,        96262, ],
    'CountWeightedL1Prefire'                                     : [        96246,        95845,        96643, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        98101,        96246,        93932,        98101,        96246,        93932,        98101,        96246,        93932, ],
  }),
  ("nof_tree_events",                 97772),
  ("nof_db_events",                   97772),
  ("fsize_local",                     331761581), # 331.76MB, avg file size 331.76MB
  ("fsize_db",                        3871755682), # 3.87GB, avg file size 1.94GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100004,        99986,        99975, ],
    'CountWeightedLHEWeightScale'                                : [       102211,       100002,        97339,       102211,       100002,        97339,       102211,       100002,        97339, ],
    'CountWeightedL1PrefireNom'                                  : [        98405,        98392,        98389, ],
    'CountWeightedL1Prefire'                                     : [        98405,        97984,        98823, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100565,        98403,        95795,       100565,        98403,        95795,       100565,        98403,        95795, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     343540327), # 343.54MB, avg file size 343.54MB
  ("fsize_db",                        3873301459), # 3.87GB, avg file size 1.94GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-280_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98688, ],
    'CountWeighted'                                              : [        98687,        98678,        98681, ],
    'CountWeightedLHEWeightScale'                                : [       101137,        98682,        95846,       101137,        98682,        95846,       101137,        98682,        95846, ],
    'CountWeightedL1PrefireNom'                                  : [        97052,        97040,        97053, ],
    'CountWeightedL1Prefire'                                     : [        97052,        96623,        97477, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        99446,        97048,        94269,        99446,        97048,        94269,        99446,        97048,        94269, ],
  }),
  ("nof_tree_events",                 98688),
  ("nof_db_events",                   98688),
  ("fsize_local",                     342685670), # 342.69MB, avg file size 342.69MB
  ("fsize_db",                        4085852491), # 4.09GB, avg file size 2.04GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99502, ],
    'CountWeighted'                                              : [        99511,        99514,        99486, ],
    'CountWeightedLHEWeightScale'                                : [       102482,        99510,        96226,       102482,        99510,        96226,       102482,        99510,        96226, ],
    'CountWeightedL1PrefireNom'                                  : [        97793,        97794,        97780, ],
    'CountWeightedL1Prefire'                                     : [        97793,        97348,        98236, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100702,        97792,        94581,       100702,        97792,        94581,       100702,        97792,        94581, ],
  }),
  ("nof_tree_events",                 99502),
  ("nof_db_events",                   99502),
  ("fsize_local",                     353016823), # 353.02MB, avg file size 353.02MB
  ("fsize_db",                        3937638636), # 3.94GB, avg file size 1.97GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-320_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        97676, ],
    'CountWeighted'                                              : [        97681,        97671,        97673, ],
    'CountWeightedLHEWeightScale'                                : [       101064,        97679,        94105,       101064,        97679,        94105,       101064,        97679,        94105, ],
    'CountWeightedL1PrefireNom'                                  : [        95936,        95929,        95937, ],
    'CountWeightedL1Prefire'                                     : [        95936,        95488,        96384, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        99244,        95934,        92440,        99244,        95934,        92440,        99244,        95934,        92440, ],
  }),
  ("nof_tree_events",                 97676),
  ("nof_db_events",                   97676),
  ("fsize_local",                     352847993), # 352.85MB, avg file size 352.85MB
  ("fsize_db",                        3947093624), # 3.95GB, avg file size 3.95GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-340_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_340_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_340_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99226, ],
    'CountWeighted'                                              : [        99223,        99235,        99222, ],
    'CountWeightedLHEWeightScale'                                : [       103125,        99223,        95236,       103125,        99223,        95236,       103125,        99223,        95236, ],
    'CountWeightedL1PrefireNom'                                  : [        97413,        97418,        97413, ],
    'CountWeightedL1Prefire'                                     : [        97413,        96948,        97876, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       101223,        97412,        93511,       101223,        97412,        93511,       101223,        97412,        93511, ],
  }),
  ("nof_tree_events",                 99226),
  ("nof_db_events",                   99226),
  ("fsize_local",                     364933681), # 364.93MB, avg file size 364.93MB
  ("fsize_db",                        4027035901), # 4.03GB, avg file size 2.01GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_340_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98212, ],
    'CountWeighted'                                              : [        98224,        98214,        98197, ],
    'CountWeightedLHEWeightScale'                                : [       102262,        98216,        94111,       102262,        98216,        94111,       102262,        98216,        94111, ],
    'CountWeightedL1PrefireNom'                                  : [        96391,        96384,        96379, ],
    'CountWeightedL1Prefire'                                     : [        96391,        95926,        96857, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100341,        96386,        92374,       100341,        96386,        92374,       100341,        96386,        92374, ],
  }),
  ("nof_tree_events",                 98212),
  ("nof_db_events",                   98212),
  ("fsize_local",                     364239112), # 364.24MB, avg file size 364.24MB
  ("fsize_db",                        4125701387), # 4.13GB, avg file size 2.06GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98789, ],
    'CountWeighted'                                              : [        98782,        98783,        98805, ],
    'CountWeightedLHEWeightScale'                                : [       103797,        98782,        93931,       103797,        98782,        93931,       103797,        98782,        93931, ],
    'CountWeightedL1PrefireNom'                                  : [        96885,        96880,        96902, ],
    'CountWeightedL1Prefire'                                     : [        96885,        96406,        97364, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       101781,        96884,        92140,       101781,        96884,        92140,       101781,        96884,        92140, ],
  }),
  ("nof_tree_events",                 98789),
  ("nof_db_events",                   98789),
  ("fsize_local",                     380466103), # 380.47MB, avg file size 380.47MB
  ("fsize_db",                        4251757973), # 4.25GB, avg file size 2.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100008,       100015,       100004, ],
    'CountWeightedLHEWeightScale'                                : [       105911,       100008,        94441,       105911,       100008,        94441,       105911,       100008,        94441, ],
    'CountWeightedL1PrefireNom'                                  : [        98055,        98053,        98058, ],
    'CountWeightedL1Prefire'                                     : [        98055,        97565,        98544, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       103824,        98054,        92613,       103824,        98054,        92613,       103824,        98054,        92613, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     398083398), # 398.08MB, avg file size 398.08MB
  ("fsize_db",                        4221394903), # 4.22GB, avg file size 2.11GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [        49535, ],
    'CountWeighted'                                              : [        49534,        49537,        49529, ],
    'CountWeightedLHEWeightScale'                                : [        52827,        49534,        46503,        52827,        49534,        46503,        52827,        49534,        46503, ],
    'CountWeightedL1PrefireNom'                                  : [        48555,        48556,        48554, ],
    'CountWeightedL1Prefire'                                     : [        48555,        48312,        48799, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51774,        48555,        45590,        51774,        48555,        45590,        51774,        48555,        45590, ],
  }),
  ("nof_tree_events",                 49535),
  ("nof_db_events",                   49535),
  ("fsize_local",                     203183101), # 203.18MB, avg file size 203.18MB
  ("fsize_db",                        2291615192), # 2.29GB, avg file size 763.87MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        50002,        49995,        50002, ],
    'CountWeightedLHEWeightScale'                                : [        53644,        50001,        46695,        53644,        50001,        46695,        53644,        50001,        46695, ],
    'CountWeightedL1PrefireNom'                                  : [        49008,        49003,        49009, ],
    'CountWeightedL1Prefire'                                     : [        49008,        48763,        49255, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        52570,        49007,        45775,        52570,        49007,        45775,        52570,        49007,        45775, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     210495338), # 210.50MB, avg file size 210.50MB
  ("fsize_db",                        2274028392), # 2.27GB, avg file size 2.27GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        49175, ],
    'CountWeighted'                                              : [        49174,        49177,        49176, ],
    'CountWeightedLHEWeightScale'                                : [        53044,        49173,        45709,        53044,        49173,        45709,        53044,        49173,        45709, ],
    'CountWeightedL1PrefireNom'                                  : [        48210,        48209,        48212, ],
    'CountWeightedL1Prefire'                                     : [        48210,        47971,        48448, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51996,        48209,        44818,        51996,        48209,        44818,        51996,        48209,        44818, ],
  }),
  ("nof_tree_events",                 49175),
  ("nof_db_events",                   49175),
  ("fsize_local",                     211617148), # 211.62MB, avg file size 211.62MB
  ("fsize_db",                        2305398213), # 2.31GB, avg file size 2.31GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        50002,        49993,        49999, ],
    'CountWeightedLHEWeightScale'                                : [        54210,        50001,        46274,        54210,        50001,        46274,        54210,        50001,        46274, ],
    'CountWeightedL1PrefireNom'                                  : [        49022,        49015,        49022, ],
    'CountWeightedL1Prefire'                                     : [        49022,        48781,        49263, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53141,        49021,        45373,        53141,        49021,        45373,        53141,        49021,        45373, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     219430741), # 219.43MB, avg file size 219.43MB
  ("fsize_db",                        2270214311), # 2.27GB, avg file size 2.27GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-700_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        49080, ],
    'CountWeighted'                                              : [        49077,        49082,        49082, ],
    'CountWeightedLHEWeightScale'                                : [        53452,        49077,        45243,        53452,        49077,        45243,        53452,        49077,        45243, ],
    'CountWeightedL1PrefireNom'                                  : [        48107,        48108,        48112, ],
    'CountWeightedL1Prefire'                                     : [        48107,        47870,        48345, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        52388,        48107,        44353,        52388,        48107,        44353,        52388,        48107,        44353, ],
  }),
  ("nof_tree_events",                 49080),
  ("nof_db_events",                   49080),
  ("fsize_local",                     219041086), # 219.04MB, avg file size 219.04MB
  ("fsize_db",                        2393147016), # 2.39GB, avg file size 2.39GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-750_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        50005,        49997,        50001, ],
    'CountWeightedLHEWeightScale'                                : [        54679,        50004,        45927,        54679,        50004,        45927,        54679,        50004,        45927, ],
    'CountWeightedL1PrefireNom'                                  : [        49028,        49022,        49028, ],
    'CountWeightedL1Prefire'                                     : [        49028,        48789,        49267, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53606,        49028,        45036,        53606,        49028,        45036,        53606,        49028,        45036, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     226805071), # 226.81MB, avg file size 226.81MB
  ("fsize_db",                        2439402593), # 2.44GB, avg file size 2.44GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        49178, ],
    'CountWeighted'                                              : [        49168,        49170,        49173, ],
    'CountWeightedLHEWeightScale'                                : [        53982,        49167,        45011,        53982,        49167,        45011,        53982,        49167,        45011, ],
    'CountWeightedL1PrefireNom'                                  : [        48208,        48209,        48212, ],
    'CountWeightedL1Prefire'                                     : [        48208,        47973,        48443, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        52922,        48207,        44135,        52922,        48207,        44135,        52922,        48207,        44135, ],
  }),
  ("nof_tree_events",                 49178),
  ("nof_db_events",                   49178),
  ("fsize_local",                     226295069), # 226.30MB, avg file size 226.30MB
  ("fsize_db",                        2401512581), # 2.40GB, avg file size 2.40GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        49283, ],
    'CountWeighted'                                              : [        49289,        49283,        49282, ],
    'CountWeightedLHEWeightScale'                                : [        54483,        49288,        44839,        54483,        49288,        44839,        54483,        49288,        44839, ],
    'CountWeightedL1PrefireNom'                                  : [        48323,        48317,        48321, ],
    'CountWeightedL1Prefire'                                     : [        48323,        48089,        48557, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53414,        48322,        43965,        53414,        48322,        43965,        53414,        48322,        43965, ],
  }),
  ("nof_tree_events",                 49283),
  ("nof_db_events",                   49283),
  ("fsize_local",                     231170026), # 231.17MB, avg file size 231.17MB
  ("fsize_db",                        2506744879), # 2.51GB, avg file size 2.51GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_SM_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99992,        99993,        99996, ],
    'CountWeightedLHEWeightScale'                                : [       128103,       120945,       114229,       105931,        99991,        94438,        89057,        84063,        79381, ],
    'CountWeightedL1PrefireNom'                                  : [        97877,        97875,        97882, ],
    'CountWeightedL1Prefire'                                     : [        97877,        97346,        98407, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       125368,       118385,       111828,       103668,        97876,        92452,        87152,        82281,        77711, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     395003112), # 395.00MB, avg file size 395.00MB
  ("fsize_db",                        4335254200), # 4.34GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_box_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_box_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99998,        99999,       100021, ],
    'CountWeightedLHEWeightScale'                                : [       127639,       121244,       115116,       105286,        99998,        94935,        88334,        83888,        79635, ],
    'CountWeightedL1PrefireNom'                                  : [        97970,        97963,        97989, ],
    'CountWeightedL1Prefire'                                     : [        97970,        97457,        98480, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       125024,       118784,       112798,       103128,        97969,        93023,        86523,        82185,        78030, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     386879263), # 386.88MB, avg file size 386.88MB
  ("fsize_db",                        4343698408), # 4.34GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_box_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        95878, ],
    'CountWeighted'                                              : [        95876,        95865,        95885, ],
    'CountWeightedLHEWeightScale'                                : [       125439,       114512,       105095,       105068,        95876,        87964,        89299,        81460,        74716, ],
    'CountWeightedL1PrefireNom'                                  : [        93661,        93657,        93663, ],
    'CountWeightedL1Prefire'                                     : [        93661,        93119,        94204, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       122519,       111870,       102688,       102619,        93660,        85946,        87215,        79576,        73000, ],
  }),
  ("nof_tree_events",                 95878),
  ("nof_db_events",                   95878),
  ("fsize_local",                     423857873), # 423.86MB, avg file size 423.86MB
  ("fsize_db",                        4587536778), # 4.59GB, avg file size 2.29GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_3_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [        99000, ],
    'CountWeighted'                                              : [        99012,        99016,        98991, ],
    'CountWeightedLHEWeightScale'                                : [       127159,       119551,       112522,       105320,        99012,        93164,        88664,        83332,        78408, ],
    'CountWeightedL1PrefireNom'                                  : [        96861,        96858,        96852, ],
    'CountWeightedL1Prefire'                                     : [        96861,        96322,        97396, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       124376,       116960,       110104,       103013,        96860,        91160,        86722,        81523,        76720, ],
  }),
  ("nof_tree_events",                 99000),
  ("nof_db_events",                   99000),
  ("fsize_local",                     397576156), # 397.58MB, avg file size 397.58MB
  ("fsize_db",                        4402287226), # 4.40GB, avg file size 1.47GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_4_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        97777, ],
    'CountWeighted'                                              : [        97762,        97776,        97770, ],
    'CountWeightedLHEWeightScale'                                : [       124976,       118448,       112251,       103184,        97762,        92649,        86636,        82086,        77770, ],
    'CountWeightedL1PrefireNom'                                  : [        95765,        95772,        95772, ],
    'CountWeightedL1Prefire'                                     : [        95765,        95261,        96269, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       122393,       116025,       109974,       101047,        95765,        90768,        84841,        80403,        76191, ],
  }),
  ("nof_tree_events",                 97777),
  ("nof_db_events",                   97777),
  ("fsize_local",                     381685313), # 381.69MB, avg file size 381.69MB
  ("fsize_db",                        4296631601), # 4.30GB, avg file size 2.15GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_5_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98210, ],
    'CountWeighted'                                              : [        98201,        98207,        98212, ],
    'CountWeightedLHEWeightScale'                                : [       127343,       117935,       109591,       106082,        98201,        91236,        89746,        83062,        77145, ],
    'CountWeightedL1PrefireNom'                                  : [        95991,        95990,        96004, ],
    'CountWeightedL1Prefire'                                     : [        95991,        95442,        96539, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       124449,       115282,       107147,       103668,        95990,        89198,        87702,        81188,        75420, ],
  }),
  ("nof_tree_events",                 98210),
  ("nof_db_events",                   98210),
  ("fsize_local",                     415399959), # 415.40MB, avg file size 415.40MB
  ("fsize_db",                        4483694248), # 4.48GB, avg file size 2.24GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_6_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99178, ],
    'CountWeighted'                                              : [        99179,        99189,        99202, ],
    'CountWeightedLHEWeightScale'                                : [       126567,       120296,       114307,       104380,        99179,        94214,        87566,        83180,        78999, ],
    'CountWeightedL1PrefireNom'                                  : [        97212,        97213,        97231, ],
    'CountWeightedL1Prefire'                                     : [        97212,        96716,        97709, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       124031,       117916,       112069,       102285,        97211,        92366,        85805,        81529,        77448, ],
  }),
  ("nof_tree_events",                 99178),
  ("nof_db_events",                   99178),
  ("fsize_local",                     384786588), # 384.79MB, avg file size 384.79MB
  ("fsize_db",                        4255863331), # 4.26GB, avg file size 2.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_7_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        97801, ],
    'CountWeighted'                                              : [        97786,        97801,        97812, ],
    'CountWeightedLHEWeightScale'                                : [       123604,       119364,       114932,       101287,        97785,        94162,        84513,        81595,        78553, ],
    'CountWeightedL1PrefireNom'                                  : [        96040,        96047,        96060, ],
    'CountWeightedL1Prefire'                                     : [        96040,        95587,        96490, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       121370,       117228,       112893,        99454,        96039,        92489,        82983,        80134,        77158, ],
  }),
  ("nof_tree_events",                 97801),
  ("nof_db_events",                   97801),
  ("fsize_local",                     355881175), # 355.88MB, avg file size 355.88MB
  ("fsize_db",                        3951072091), # 3.95GB, avg file size 1.98GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_8_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [        99301, ],
    'CountWeighted'                                              : [        99306,        99290,        99282, ],
    'CountWeightedLHEWeightScale'                                : [       127635,       119887,       112766,       105752,        99306,        93378,        89062,        83606,        78603, ],
    'CountWeightedL1PrefireNom'                                  : [        97191,        97180,        97180, ],
    'CountWeightedL1Prefire'                                     : [        97191,        96664,        97719, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       124896,       117341,       110394,       103479,        97191,        91411,        87145,        81827,        76945, ],
  }),
  ("nof_tree_events",                 99301),
  ("nof_db_events",                   99301),
  ("fsize_local",                     400936186), # 400.94MB, avg file size 400.94MB
  ("fsize_db",                        4354193987), # 4.35GB, avg file size 1.45GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_9_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98588, ],
    'CountWeighted'                                              : [        98625,        98592,        98585, ],
    'CountWeightedLHEWeightScale'                                : [       127435,       118590,       110648,       105968,        98613,        91964,        89511,        83259,        77651, ],
    'CountWeightedL1PrefireNom'                                  : [        96411,        96386,        96392, ],
    'CountWeightedL1Prefire'                                     : [        96411,        95865,        96957, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       124569,       115948,       108202,       103581,        96403,        89929,        87494,        81400,        75932, ],
  }),
  ("nof_tree_events",                 98588),
  ("nof_db_events",                   98588),
  ("fsize_local",                     411129625), # 411.13MB, avg file size 411.13MB
  ("fsize_db",                        4491891214), # 4.49GB, avg file size 2.25GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_10_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98724, ],
    'CountWeighted'                                              : [        98726,        98718,        98738, ],
    'CountWeightedLHEWeightScale'                                : [       125017,       120348,       115596,       102575,        98723,        94803,        85684,        82447,        79161, ],
    'CountWeightedL1PrefireNom'                                  : [        96922,        96916,        96929, ],
    'CountWeightedL1Prefire'                                     : [        96922,        96459,        97383, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       122712,       118154,       113508,       100681,        96919,        93088,        84099,        80940,        77727, ],
  }),
  ("nof_tree_events",                 98724),
  ("nof_db_events",                   98724),
  ("fsize_local",                     364982998), # 364.98MB, avg file size 364.98MB
  ("fsize_db",                        4130096263), # 4.13GB, avg file size 2.07GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_11_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99981,        99973,        99990, ],
    'CountWeightedLHEWeightScale'                                : [       127628,       121294,       115255,       105259,        99980,        94991,        88308,        83870,        79649, ],
    'CountWeightedL1PrefireNom'                                  : [        98014,        98011,        98016, ],
    'CountWeightedL1Prefire'                                     : [        98014,        97513,        98513, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       125082,       118903,       113004,       103155,        98013,        93133,        86539,        82211,        78089, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     387702835), # 387.70MB, avg file size 387.70MB
  ("fsize_db",                        4262962926), # 4.26GB, avg file size 2.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_12_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99190, ],
    'CountWeighted'                                              : [        99196,        99183,        99187, ],
    'CountWeightedLHEWeightScale'                                : [       125927,       120695,       115472,       103506,        99196,        94890,        86581,        82962,        79359, ],
    'CountWeightedL1PrefireNom'                                  : [        97308,        97298,        97309, ],
    'CountWeightedL1Prefire'                                     : [        97308,        96828,        97789, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       123514,       118405,       113299,       101520,        97308,        93102,        84919,        81386,        77863, ],
  }),
  ("nof_tree_events",                 99190),
  ("nof_db_events",                   99190),
  ("fsize_local",                     371412477), # 371.41MB, avg file size 371.41MB
  ("fsize_db",                        4123293762), # 4.12GB, avg file size 2.06GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Jan13_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["sum_events"] = [
  [ 'signal_ggf_nonresonant_node_sm_hh_4t',            'signal_ggf_nonresonant_node_box_hh_4t',           'signal_ggf_nonresonant_node_2_hh_4t',             'signal_ggf_nonresonant_node_3_hh_4t',             'signal_ggf_nonresonant_node_4_hh_4t',             'signal_ggf_nonresonant_node_5_hh_4t',             'signal_ggf_nonresonant_node_6_hh_4t',             'signal_ggf_nonresonant_node_7_hh_4t',             'signal_ggf_nonresonant_node_8_hh_4t',             'signal_ggf_nonresonant_node_9_hh_4t',             'signal_ggf_nonresonant_node_10_hh_4t',            'signal_ggf_nonresonant_node_11_hh_4t',            'signal_ggf_nonresonant_node_12_hh_4t',             ],
]

