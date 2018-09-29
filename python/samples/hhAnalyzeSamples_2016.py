from collections import OrderedDict as OD

# file generated at 2018-09-19 09:28:28 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016.py -p /hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples -Z zeroes.txt -z zombies.txt -N samples_2016 -E 2016 -g hhAnalyzeSamples_2016.py -o python/samples -M

samples_2016 = OD()
samples_2016["/GluGluToRadionToHHTo4Tau_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99988,        99997,       100000, ],
    'CountWeighted'                          : [        99988,        99997,       100000, ],
    'CountFullWeightedNoPU'                  : [       100000, ],
    'CountWeightedNoPU'                      : [       100000, ],
    'CountWeightedLHEWeightScale'            : [       101618,        99987,        97817,       101618,        99987,        97817,       101618,        99987,        97817, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       101612,       100000,        97822,       101612,       100000,        97822,       101612,       100000,        97822, ],
    'CountFullWeightedLHEWeightScale'        : [       101618,        99987,        97817,       101618,        99987,        97817,       101618,        99987,        97817, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       101612,       100000,        97822,       101612,       100000,        97822,       101612,       100000,        97822, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     222306675), # 222.31MB, avg file size 222.31MB
  ("fsize_db",                        3867669738), # 3.87GB, avg file size 276.26MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                  : [        99204, ],
    'CountFullWeighted'                      : [        99210,        99196,        99193, ],
    'CountWeighted'                          : [        99210,        99196,        99193, ],
    'CountFullWeightedNoPU'                  : [        99204, ],
    'CountWeightedNoPU'                      : [        99204, ],
    'CountWeightedLHEWeightScale'            : [       101099,        99210,        96800,       101099,        99210,        96800,       101099,        99210,        96800, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       101095,        99204,        96802,       101095,        99204,        96802,       101095,        99204,        96802, ],
    'CountFullWeightedLHEWeightScale'        : [       101099,        99210,        96800,       101099,        99210,        96800,       101099,        99210,        96800, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       101095,        99204,        96802,       101095,        99204,        96802,       101095,        99204,        96802, ],
  }),
  ("nof_tree_events",                 99204),
  ("nof_db_events",                   99204),
  ("fsize_local",                     222544647), # 222.54MB, avg file size 222.54MB
  ("fsize_db",                        3825455757), # 3.83GB, avg file size 239.09MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99992,        99993,        99983, ],
    'CountWeighted'                          : [        99992,        99993,        99983, ],
    'CountFullWeightedNoPU'                  : [       100000, ],
    'CountWeightedNoPU'                      : [       100000, ],
    'CountWeightedLHEWeightScale'            : [       102214,        99988,        97337,       102214,        99988,        97337,       102214,        99988,        97337, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       102220,       100000,        97323,       102220,       100000,        97323,       102220,       100000,        97323, ],
    'CountFullWeightedLHEWeightScale'        : [       102214,        99988,        97337,       102214,        99988,        97337,       102214,        99988,        97337, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       102220,       100000,        97323,       102220,       100000,        97323,       102220,       100000,        97323, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     226328260), # 226.33MB, avg file size 226.33MB
  ("fsize_db",                        3828027078), # 3.83GB, avg file size 255.20MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-280_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                  : [        98567, ],
    'CountFullWeighted'                      : [        98559,        98573,        98576, ],
    'CountWeighted'                          : [        98559,        98573,        98576, ],
    'CountFullWeightedNoPU'                  : [        98567, ],
    'CountWeightedNoPU'                      : [        98567, ],
    'CountWeightedLHEWeightScale'            : [       101009,        98558,        95734,       101009,        98558,        95734,       101009,        98558,        95734, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       101019,        98567,        95742,       101019,        98567,        95742,       101019,        98567,        95742, ],
    'CountFullWeightedLHEWeightScale'        : [       101009,        98558,        95734,       101009,        98558,        95734,       101009,        98558,        95734, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       101019,        98567,        95742,       101019,        98567,        95742,       101019,        98567,        95742, ],
  }),
  ("nof_tree_events",                 98567),
  ("nof_db_events",                   98567),
  ("fsize_local",                     224889853), # 224.89MB, avg file size 224.89MB
  ("fsize_db",                        3819426599), # 3.82GB, avg file size 181.88MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                  : [        88976, ],
    'CountFullWeighted'                      : [        88980,        88965,        88968, ],
    'CountWeighted'                          : [        88980,        88965,        88968, ],
    'CountFullWeightedNoPU'                  : [        88976, ],
    'CountWeightedNoPU'                      : [        88976, ],
    'CountWeightedLHEWeightScale'            : [        91633,        88980,        86058,        91633,        88980,        86058,        91633,        88980,        86058, ],
    'CountWeightedLHEWeightScaleNoPU'        : [        91632,        88976,        86062,        91632,        88976,        86062,        91632,        88976,        86062, ],
    'CountFullWeightedLHEWeightScale'        : [        91633,        88980,        86058,        91633,        88980,        86058,        91633,        88980,        86058, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [        91632,        88976,        86062,        91632,        88976,        86062,        91632,        88976,        86062, ],
  }),
  ("nof_tree_events",                 88976),
  ("nof_db_events",                   88976),
  ("fsize_local",                     206475354), # 206.48MB, avg file size 206.48MB
  ("fsize_db",                        3475966865), # 3.48GB, avg file size 193.11MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-320_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [       100004,        99999,       100008, ],
    'CountWeighted'                          : [       100004,        99999,       100008, ],
    'CountFullWeightedNoPU'                  : [       100000, ],
    'CountWeightedNoPU'                      : [       100000, ],
    'CountWeightedLHEWeightScale'            : [       103474,       100003,        96338,       103474,       100003,        96338,       103474,       100003,        96338, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       103465,       100000,        96340,       103465,       100000,        96340,       103465,       100000,        96340, ],
    'CountFullWeightedLHEWeightScale'        : [       103474,       100003,        96338,       103474,       100003,        96338,       103474,       100003,        96338, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       103465,       100000,        96340,       103465,       100000,        96340,       103465,       100000,        96340, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     235556894), # 235.56MB, avg file size 235.56MB
  ("fsize_db",                        3892930646), # 3.89GB, avg file size 324.41MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-340_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_340_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_340_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [       100000,       100001,       100008, ],
    'CountWeighted'                          : [       100000,       100001,       100008, ],
    'CountFullWeightedNoPU'                  : [       100000, ],
    'CountWeightedNoPU'                      : [       100000, ],
    'CountWeightedLHEWeightScale'            : [       103915,       100000,        95992,       103915,       100000,        95992,       103915,       100000,        95992, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       103912,       100000,        95994,       103912,       100000,        95994,       103912,       100000,        95994, ],
    'CountFullWeightedLHEWeightScale'        : [       103915,       100000,        95992,       103915,       100000,        95992,       103915,       100000,        95992, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       103912,       100000,        95994,       103912,       100000,        95994,       103912,       100000,        95994, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     239055049), # 239.06MB, avg file size 239.06MB
  ("fsize_db",                        3947815706), # 3.95GB, avg file size 281.99MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_340_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                  : [        98356, ],
    'CountFullWeighted'                      : [        98356,        98362,        98356, ],
    'CountWeighted'                          : [        98356,        98362,        98356, ],
    'CountFullWeightedNoPU'                  : [        98356, ],
    'CountWeightedNoPU'                      : [        98356, ],
    'CountWeightedLHEWeightScale'            : [       102415,        98354,        94245,       102415,        98354,        94245,       102415,        98354,        94245, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       102411,        98356,        94245,       102411,        98356,        94245,       102411,        98356,        94245, ],
    'CountFullWeightedLHEWeightScale'        : [       102415,        98354,        94245,       102415,        98354,        94245,       102415,        98354,        94245, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       102411,        98356,        94245,       102411,        98356,        94245,       102411,        98356,        94245, ],
  }),
  ("nof_tree_events",                 98356),
  ("nof_db_events",                   98356),
  ("fsize_local",                     236831125), # 236.83MB, avg file size 236.83MB
  ("fsize_db",                        3939843876), # 3.94GB, avg file size 179.08MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                  : [        97614, ],
    'CountFullWeighted'                      : [        97616,        97617,        97622, ],
    'CountWeighted'                          : [        97616,        97617,        97622, ],
    'CountFullWeightedNoPU'                  : [        97614, ],
    'CountWeightedNoPU'                      : [        97614, ],
    'CountWeightedLHEWeightScale'            : [       102566,        97613,        92815,       102566,        97613,        92815,       102566,        97613,        92815, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       102575,        97614,        92807,       102575,        97614,        92807,       102575,        97614,        92807, ],
    'CountFullWeightedLHEWeightScale'        : [       102566,        97613,        92815,       102566,        97613,        92815,       102566,        97613,        92815, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       102575,        97614,        92807,       102575,        97614,        92807,       102575,        97614,        92807, ],
  }),
  ("nof_tree_events",                 97614),
  ("nof_db_events",                   97614),
  ("fsize_local",                     243607415), # 243.61MB, avg file size 243.61MB
  ("fsize_db",                        3967336020), # 3.97GB, avg file size 208.81MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                  : [       100000, ],
    'CountFullWeighted'                      : [        99996,       100002,        99994, ],
    'CountWeighted'                          : [        99996,       100002,        99994, ],
    'CountFullWeightedNoPU'                  : [       100000, ],
    'CountWeightedNoPU'                      : [       100000, ],
    'CountWeightedLHEWeightScale'            : [       105905,        99996,        94447,       105905,        99996,        94447,       105905,        99996,        94447, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       105909,       100000,        94439,       105909,       100000,        94439,       105909,       100000,        94439, ],
    'CountFullWeightedLHEWeightScale'        : [       105905,        99996,        94447,       105905,        99996,        94447,       105905,        99996,        94447, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       105909,       100000,        94439,       105909,       100000,        94439,       105909,       100000,        94439, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     258082038), # 258.08MB, avg file size 258.08MB
  ("fsize_db",                        4142163410), # 4.14GB, avg file size 197.25MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                  : [        50000, ],
    'CountFullWeighted'                      : [        49999,        49998,        49999, ],
    'CountWeighted'                          : [        49999,        49998,        49999, ],
    'CountFullWeightedNoPU'                  : [        50000, ],
    'CountWeightedNoPU'                      : [        50000, ],
    'CountWeightedLHEWeightScale'            : [        53312,        49998,        46947,        53312,        49998,        46947,        53312,        49998,        46947, ],
    'CountWeightedLHEWeightScaleNoPU'        : [        53314,        50000,        46951,        53314,        50000,        46951,        53314,        50000,        46951, ],
    'CountFullWeightedLHEWeightScale'        : [        53312,        49998,        46947,        53312,        49998,        46947,        53312,        49998,        46947, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [        53314,        50000,        46951,        53314,        50000,        46951,        53314,        50000,        46951, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     134743564), # 134.74MB, avg file size 134.74MB
  ("fsize_db",                        2135623539), # 2.14GB, avg file size 142.37MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                  : [        50000, ],
    'CountFullWeighted'                      : [        50001,        50001,        50003, ],
    'CountWeighted'                          : [        50001,        50001,        50003, ],
    'CountFullWeightedNoPU'                  : [        50000, ],
    'CountWeightedNoPU'                      : [        50000, ],
    'CountWeightedLHEWeightScale'            : [        53645,        50001,        46695,        53645,        50001,        46695,        53645,        50001,        46695, ],
    'CountWeightedLHEWeightScaleNoPU'        : [        53648,        50000,        46697,        53648,        50000,        46697,        53648,        50000,        46697, ],
    'CountFullWeightedLHEWeightScale'        : [        53645,        50001,        46695,        53645,        50001,        46695,        53645,        50001,        46695, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [        53648,        50000,        46697,        53648,        50000,        46697,        53648,        50000,        46697, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     138769735), # 138.77MB, avg file size 138.77MB
  ("fsize_db",                        2093059468), # 2.09GB, avg file size 418.61MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                  : [        50000, ],
    'CountFullWeighted'                      : [        50001,        49999,        50002, ],
    'CountWeighted'                          : [        50001,        49999,        50002, ],
    'CountFullWeightedNoPU'                  : [        50000, ],
    'CountWeightedNoPU'                      : [        50000, ],
    'CountWeightedLHEWeightScale'            : [        53934,        49998,        46475,        53934,        49998,        46475,        53934,        49998,        46475, ],
    'CountWeightedLHEWeightScaleNoPU'        : [        53935,        50000,        46473,        53935,        50000,        46473,        53935,        50000,        46473, ],
    'CountFullWeightedLHEWeightScale'        : [        53934,        49998,        46475,        53934,        49998,        46475,        53934,        49998,        46475, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [        53935,        50000,        46473,        53935,        50000,        46473,        53935,        50000,        46473, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     142512264), # 142.51MB, avg file size 142.51MB
  ("fsize_db",                        2163109704), # 2.16GB, avg file size 180.26MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                  : [        47684, ],
    'CountFullWeighted'                      : [        47685,        47684,        47678, ],
    'CountWeighted'                          : [        47685,        47684,        47678, ],
    'CountFullWeightedNoPU'                  : [        47684, ],
    'CountWeightedNoPU'                      : [        47684, ],
    'CountWeightedLHEWeightScale'            : [        51693,        47685,        44133,        51693,        47685,        44133,        51693,        47685,        44133, ],
    'CountWeightedLHEWeightScaleNoPU'        : [        51697,        47684,        44129,        51697,        47684,        44129,        51697,        47684,        44129, ],
    'CountFullWeightedLHEWeightScale'        : [        51693,        47685,        44133,        51693,        47685,        44133,        51693,        47685,        44133, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [        51697,        47684,        44129,        51697,        47684,        44129,        51697,        47684,        44129, ],
  }),
  ("nof_tree_events",                 47684),
  ("nof_db_events",                   47684),
  ("fsize_local",                     139211665), # 139.21MB, avg file size 139.21MB
  ("fsize_db",                        2147010667), # 2.15GB, avg file size 107.35MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-700_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                  : [        50000, ],
    'CountFullWeighted'                      : [        49998,        50005,        49999, ],
    'CountWeighted'                          : [        49998,        50005,        49999, ],
    'CountFullWeightedNoPU'                  : [        50000, ],
    'CountWeightedNoPU'                      : [        50000, ],
    'CountWeightedLHEWeightScale'            : [        54453,        49996,        46092,        54453,        49996,        46092,        54453,        49996,        46092, ],
    'CountWeightedLHEWeightScaleNoPU'        : [        54448,        50000,        46089,        54448,        50000,        46089,        54448,        50000,        46089, ],
    'CountFullWeightedLHEWeightScale'        : [        54453,        49996,        46092,        54453,        49996,        46092,        54453,        49996,        46092, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [        54448,        50000,        46089,        54448,        50000,        46089,        54448,        50000,        46089, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     148965603), # 148.97MB, avg file size 148.97MB
  ("fsize_db",                        2213964233), # 2.21GB, avg file size 201.27MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-750_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                  : [        49280, ],
    'CountFullWeighted'                      : [        49273,        49281,        49278, ],
    'CountWeighted'                          : [        49273,        49281,        49278, ],
    'CountFullWeightedNoPU'                  : [        49280, ],
    'CountWeightedNoPU'                      : [        49280, ],
    'CountWeightedLHEWeightScale'            : [        53894,        49273,        45263,        53894,        49273,        45263,        53894,        49273,        45263, ],
    'CountWeightedLHEWeightScaleNoPU'        : [        53889,        49280,        45263,        53889,        49280,        45263,        53889,        49280,        45263, ],
    'CountFullWeightedLHEWeightScale'        : [        53894,        49273,        45263,        53894,        49273,        45263,        53894,        49273,        45263, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [        53889,        49280,        45263,        53889,        49280,        45263,        53889,        49280,        45263, ],
  }),
  ("nof_tree_events",                 49280),
  ("nof_db_events",                   49280),
  ("fsize_local",                     149436783), # 149.44MB, avg file size 149.44MB
  ("fsize_db",                        2195753227), # 2.20GB, avg file size 199.61MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                  : [        50000, ],
    'CountFullWeighted'                      : [        50007,        50006,        50001, ],
    'CountWeighted'                          : [        50007,        50006,        50001, ],
    'CountFullWeightedNoPU'                  : [        50000, ],
    'CountWeightedNoPU'                      : [        50000, ],
    'CountWeightedLHEWeightScale'            : [        54895,        50007,        45768,        54895,        50007,        45768,        54895,        50007,        45768, ],
    'CountWeightedLHEWeightScaleNoPU'        : [        54897,        50000,        45761,        54897,        50000,        45761,        54897,        50000,        45761, ],
    'CountFullWeightedLHEWeightScale'        : [        54895,        50007,        45768,        54895,        50007,        45768,        54895,        50007,        45768, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [        54897,        50000,        45761,        54897,        50000,        45761,        54897,        50000,        45761, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     154034494), # 154.03MB, avg file size 154.03MB
  ("fsize_db",                        2222020975), # 2.22GB, avg file size 277.75MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4t"),
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

samples_2016["/GluGluToRadionToHHTo4Tau_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                  : [        50000, ],
    'CountFullWeighted'                      : [        50002,        50005,        49997, ],
    'CountWeighted'                          : [        50002,        50005,        49997, ],
    'CountFullWeightedNoPU'                  : [        50000, ],
    'CountWeightedNoPU'                      : [        50000, ],
    'CountWeightedLHEWeightScale'            : [        55277,        50002,        45489,        55277,        50002,        45489,        55277,        50002,        45489, ],
    'CountWeightedLHEWeightScaleNoPU'        : [        55283,        50000,        45496,        55283,        50000,        45496,        55283,        50000,        45496, ],
    'CountFullWeightedLHEWeightScale'        : [        55277,        50002,        45489,        55277,        50002,        45489,        55277,        50002,        45489, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [        55283,        50000,        45496,        55283,        50000,        45496,        55283,        50000,        45496, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     157775835), # 157.78MB, avg file size 157.78MB
  ("fsize_db",                        2320248894), # 2.32GB, avg file size 128.90MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2018Sep19_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4t"),
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

samples_2016["sum_events"] = [
]

