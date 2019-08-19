from collections import OrderedDict as OD

# file generated at 2019-08-19 16:56:45 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh.py -p /hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_hh.py -M

samples_2016 = OD()
samples_2016["/GluGluToRadionToHHTo4Tau_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4t"),
  ("nof_files",                       3),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99988,        99997,       100000, ],
    'CountWeightedLHEWeightScale'                                : [       101618,        99988,        97817,       101618,        99988,        97817,       101618,        99988,        97817, ],
    'CountWeightedL1PrefireNom'                                  : [        98542,        98544,        98555, ],
    'CountWeightedL1Prefire'                                     : [        98542,        98155,        98928, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100132,        98542,        96409,       100132,        98542,        96409,       100132,        98542,        96409, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     652952476), # 652.95MB, avg file size 217.65MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        99204, ],
    'CountWeighted'                                              : [        99210,        99197,        99194, ],
    'CountWeightedLHEWeightScale'                                : [       101099,        99210,        96800,       101099,        99210,        96800,       101099,        99210,        96800, ],
    'CountWeightedL1PrefireNom'                                  : [        97736,        97721,        97731, ],
    'CountWeightedL1Prefire'                                     : [        97736,        97343,        98125, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        99586,        97735,        95374,        99586,        97735,        95374,        99586,        97735,        95374, ],
  }),
  ("nof_tree_events",                 99204),
  ("nof_db_events",                   99204),
  ("fsize_local",                     653224701), # 653.22MB, avg file size 326.61MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4t"),
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
  ("nof_files",                       3),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99992,        99993,        99983, ],
    'CountWeightedLHEWeightScale'                                : [       102214,        99988,        97337,       102214,        99988,        97337,       102214,        99988,        97337, ],
    'CountWeightedL1PrefireNom'                                  : [        98438,        98434,        98437, ],
    'CountWeightedL1Prefire'                                     : [        98438,        98026,        98847, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100609,        98435,        95831,       100609,        98435,        95831,       100609,        98435,        95831, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     665320111), # 665.32MB, avg file size 221.77MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98567, ],
    'CountWeighted'                                              : [        98559,        98573,        98575, ],
    'CountWeightedLHEWeightScale'                                : [       101009,        98558,        95733,       101009,        98558,        95733,       101009,        98558,        95733, ],
    'CountWeightedL1PrefireNom'                                  : [        97004,        97008,        97018, ],
    'CountWeightedL1Prefire'                                     : [        97004,        96594,        97414, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        99399,        97003,        94231,        99399,        97003,        94231,        99399,        97003,        94231, ],
  }),
  ("nof_tree_events",                 98567),
  ("nof_db_events",                   98567),
  ("fsize_local",                     660492604), # 660.49MB, avg file size 330.25MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        94730, ],
    'CountWeighted'                                              : [        94730,        94730,        94738, ],
    'CountWeightedLHEWeightScale'                                : [        97557,        94730,        91625,        97557,        94730,        91625,        97557,        94730,        91625, ],
    'CountWeightedL1PrefireNom'                                  : [        93173,        93173,        93178, ],
    'CountWeightedL1Prefire'                                     : [        93173,        92766,        93579, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        95939,        93173,        90130,        95939,        93173,        90130,        95939,        93173,        90130, ],
  }),
  ("nof_tree_events",                 94730),
  ("nof_db_events",                   94730),
  ("fsize_local",                     645276620), # 645.28MB, avg file size 322.64MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4t"),
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
  ("nof_files",                       3),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100004,        99999,       100008, ],
    'CountWeightedLHEWeightScale'                                : [       103474,       100004,        96338,       103474,       100004,        96338,       103474,       100004,        96338, ],
    'CountWeightedL1PrefireNom'                                  : [        98265,        98258,        98271, ],
    'CountWeightedL1Prefire'                                     : [        98265,        97814,        98714, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       101660,        98264,        94676,       101660,        98264,        94676,       101660,        98264,        94676, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     692481621), # 692.48MB, avg file size 230.83MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_4t"),
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
  ("nof_files",                       3),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100000,       100001,       100008, ],
    'CountWeightedLHEWeightScale'                                : [       103914,       100000,        95992,       103914,       100000,        95992,       103914,       100000,        95992, ],
    'CountWeightedL1PrefireNom'                                  : [        98177,        98172,        98189, ],
    'CountWeightedL1Prefire'                                     : [        98177,        97709,        98645, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       102003,        98177,        94255,       102003,        98177,        94255,       102003,        98177,        94255, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     702447758), # 702.45MB, avg file size 234.15MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_340_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98356, ],
    'CountWeighted'                                              : [        98355,        98362,        98356, ],
    'CountWeightedLHEWeightScale'                                : [       102415,        98354,        94246,       102415,        98354,        94246,       102415,        98354,        94246, ],
    'CountWeightedL1PrefireNom'                                  : [        96567,        96572,        96567, ],
    'CountWeightedL1Prefire'                                     : [        96567,        96107,        97026, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100537,        96566,        92545,       100537,        96566,        92545,       100537,        96566,        92545, ],
  }),
  ("nof_tree_events",                 98356),
  ("nof_db_events",                   98356),
  ("fsize_local",                     696533321), # 696.53MB, avg file size 348.27MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        97614, ],
    'CountWeighted'                                              : [        97616,        97617,        97622, ],
    'CountWeightedLHEWeightScale'                                : [       102567,        97613,        92816,       102567,        97613,        92816,       102567,        97613,        92816, ],
    'CountWeightedL1PrefireNom'                                  : [        95702,        95697,        95709, ],
    'CountWeightedL1Prefire'                                     : [        95702,        95216,        96187, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100538,        95700,        91010,       100538,        95700,        91010,       100538,        95700,        91010, ],
  }),
  ("nof_tree_events",                 97614),
  ("nof_db_events",                   97614),
  ("fsize_local",                     714977331), # 714.98MB, avg file size 357.49MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4t"),
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
  ("nof_files",                       3),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99996,       100002,        99994, ],
    'CountWeightedLHEWeightScale'                                : [       105905,        99996,        94447,       105905,        99996,        94447,       105905,        99996,        94447, ],
    'CountWeightedL1PrefireNom'                                  : [        97935,        97934,        97937, ],
    'CountWeightedL1Prefire'                                     : [        97935,        97415,        98454, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       103702,        97935,        92512,       103702,        97935,        92512,       103702,        97935,        92512, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     752979368), # 752.98MB, avg file size 250.99MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49999,        49998,        49998, ],
    'CountWeightedLHEWeightScale'                                : [        53312,        49998,        46947,        53312,        49998,        46947,        53312,        49998,        46947, ],
    'CountWeightedL1PrefireNom'                                  : [        48939,        48935,        48940, ],
    'CountWeightedL1Prefire'                                     : [        48939,        48672,        49204, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        52173,        48937,        45957,        52173,        48937,        45957,        52173,        48937,        45957, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     385601006), # 385.60MB, avg file size 192.80MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        50001,        50001,        50003, ],
    'CountWeightedLHEWeightScale'                                : [        53645,        50001,        46695,        53645,        50001,        46695,        53645,        50001,        46695, ],
    'CountWeightedL1PrefireNom'                                  : [        48894,        48892,        48897, ],
    'CountWeightedL1Prefire'                                     : [        48894,        48618,        49170, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        52448,        48894,        45668,        52448,        48894,        45668,        52448,        48894,        45668, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     393526170), # 393.53MB, avg file size 196.76MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4t"),
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
    'CountWeighted'                                              : [        50001,        49999,        50002, ],
    'CountWeightedLHEWeightScale'                                : [        53935,        49999,        46475,        53935,        49999,        46475,        53935,        49999,        46475, ],
    'CountWeightedL1PrefireNom'                                  : [        48857,        48852,        48861, ],
    'CountWeightedL1Prefire'                                     : [        48857,        48574,        49140, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        52693,        48856,        45419,        52693,        48856,        45419,        52693,        48856,        45419, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     400991826), # 400.99MB, avg file size 400.99MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4t"),
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
    'CountWeighted'                                              : [        48471,        48459,        48465, ],
    'CountWeightedLHEWeightScale'                                : [        52538,        48471,        44855,        52538,        48471,        44855,        52538,        48471,        44855, ],
    'CountWeightedL1PrefireNom'                                  : [        47322,        47316,        47317, ],
    'CountWeightedL1Prefire'                                     : [        47322,        47040,        47605, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51288,        47322,        43801,        51288,        47322,        43801,        51288,        47322,        43801, ],
  }),
  ("nof_tree_events",                 48463),
  ("nof_db_events",                   48463),
  ("fsize_local",                     395192980), # 395.19MB, avg file size 395.19MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49998,        50006,        49999, ],
    'CountWeightedLHEWeightScale'                                : [        54453,        49996,        46092,        54453,        49996,        46092,        54453,        49996,        46092, ],
    'CountWeightedL1PrefireNom'                                  : [        48801,        48801,        48807, ],
    'CountWeightedL1Prefire'                                     : [        48801,        48508,        49095, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53141,        48800,        44995,        53141,        48800,        44995,        53141,        48800,        44995, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     414488144), # 414.49MB, avg file size 207.24MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        49996,        49992,        50000, ],
    'CountWeightedLHEWeightScale'                                : [        54679,        49996,        45926,        54679,        49996,        45926,        54679,        49996,        45926, ],
    'CountWeightedL1PrefireNom'                                  : [        48788,        48788,        48787, ],
    'CountWeightedL1Prefire'                                     : [        48788,        48492,        49085, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53349,        48788,        44821,        53349,        48788,        44821,        53349,        48788,        44821, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     420234073), # 420.23MB, avg file size 210.12MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4t"),
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
    'CountWeighted'                                              : [        50007,        50006,        50001, ],
    'CountWeightedLHEWeightScale'                                : [        54895,        50007,        45768,        54895,        50007,        45768,        54895,        50007,        45768, ],
    'CountWeightedL1PrefireNom'                                  : [        48787,        48788,        48782, ],
    'CountWeightedL1Prefire'                                     : [        48787,        48488,        49086, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53550,        48786,        44659,        53550,        48786,        44659,        53550,        48786,        44659, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     424662727), # 424.66MB, avg file size 424.66MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4t"),
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
    'CountWeighted'                                              : [        50002,        50005,        49997, ],
    'CountWeightedLHEWeightScale'                                : [        55277,        50002,        45489,        55277,        50002,        45489,        55277,        50002,        45489, ],
    'CountWeightedL1PrefireNom'                                  : [        48749,        48748,        48748, ],
    'CountWeightedL1Prefire'                                     : [        48749,        48445,        49054, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53886,        48749,        44356,        53886,        48749,        44356,        53886,        48749,        44356, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     433433953), # 433.43MB, avg file size 433.43MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99430, ],
    'CountWeighted'                                              : [        99427,        99422,        99421, ],
    'CountWeightedLHEWeightScale'                                : [       101034,        99427,        97259,       101034,        99427,        97259,       101034,        99427,        97259, ],
    'CountWeightedL1PrefireNom'                                  : [        97935,        97926,        97937, ],
    'CountWeightedL1Prefire'                                     : [        97935,        97538,        98329, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        99505,        97934,        95808,        99505,        97934,        95808,        99505,        97934,        95808, ],
  }),
  ("nof_tree_events",                 99430),
  ("nof_db_events",                   99430),
  ("fsize_local",                     657361724), # 657.36MB, avg file size 328.68MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        97772, ],
    'CountWeighted'                                              : [        97768,        97781,        97760, ],
    'CountWeightedLHEWeightScale'                                : [        99652,        97767,        95395,        99652,        97767,        95395,        99652,        97767,        95395, ],
    'CountWeightedL1PrefireNom'                                  : [        96260,        96263,        96261, ],
    'CountWeightedL1Prefire'                                     : [        96260,        95861,        96658, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        98101,        96259,        93934,        98101,        96259,        93934,        98101,        96259,        93934, ],
  }),
  ("nof_tree_events",                 97772),
  ("nof_db_events",                   97772),
  ("fsize_local",                     653436846), # 653.44MB, avg file size 326.72MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4t"),
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
  ("nof_files",                       3),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100015,        99987,        99998, ],
    'CountWeightedLHEWeightScale'                                : [       102216,       100012,        97339,       102216,       100012,        97339,       102216,       100012,        97339, ],
    'CountWeightedL1PrefireNom'                                  : [        98411,        98392,        98402, ],
    'CountWeightedL1Prefire'                                     : [        98411,        97991,        98828, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100568,        98409,        95794,       100568,        98409,        95794,       100568,        98409,        95794, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     675143123), # 675.14MB, avg file size 225.05MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98688, ],
    'CountWeighted'                                              : [        98684,        98697,        98687, ],
    'CountWeightedLHEWeightScale'                                : [       101140,        98683,        95846,       101140,        98683,        95846,       101140,        98683,        95846, ],
    'CountWeightedL1PrefireNom'                                  : [        97050,        97053,        97057, ],
    'CountWeightedL1Prefire'                                     : [        97050,        96622,        97476, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        99448,        97048,        94269,        99448,        97048,        94269,        99448,        97048,        94269, ],
  }),
  ("nof_tree_events",                 98688),
  ("nof_db_events",                   98688),
  ("fsize_local",                     672435006), # 672.44MB, avg file size 336.22MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99502, ],
    'CountWeighted'                                              : [        99507,        99517,        99489, ],
    'CountWeightedLHEWeightScale'                                : [       102485,        99506,        96225,       102485,        99506,        96225,       102485,        99506,        96225, ],
    'CountWeightedL1PrefireNom'                                  : [        97791,        97796,        97781, ],
    'CountWeightedL1Prefire'                                     : [        97791,        97346,        98234, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100704,        97790,        94581,       100704,        97790,        94581,       100704,        97790,        94581, ],
  }),
  ("nof_tree_events",                 99502),
  ("nof_db_events",                   99502),
  ("fsize_local",                     692715880), # 692.72MB, avg file size 346.36MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        97676, ],
    'CountWeighted'                                              : [        97676,        97680,        97681, ],
    'CountWeightedLHEWeightScale'                                : [       101061,        97675,        94104,       101061,        97675,        94104,       101061,        97675,        94104, ],
    'CountWeightedL1PrefireNom'                                  : [        95934,        95934,        95940, ],
    'CountWeightedL1Prefire'                                     : [        95934,        95486,        96381, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        99242,        95933,        92439,        99242,        95933,        92439,        99242,        95933,        92439, ],
  }),
  ("nof_tree_events",                 97676),
  ("nof_db_events",                   97676),
  ("fsize_local",                     689503754), # 689.50MB, avg file size 344.75MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99226, ],
    'CountWeighted'                                              : [        99221,        99225,        99223, ],
    'CountWeightedLHEWeightScale'                                : [       103123,        99220,        95238,       103123,        99220,        95238,       103123,        99220,        95238, ],
    'CountWeightedL1PrefireNom'                                  : [        97411,        97410,        97416, ],
    'CountWeightedL1Prefire'                                     : [        97411,        96947,        97874, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       101222,        97410,        93512,       101222,        97410,        93512,       101222,        97410,        93512, ],
  }),
  ("nof_tree_events",                 99226),
  ("nof_db_events",                   99226),
  ("fsize_local",                     713551121), # 713.55MB, avg file size 356.78MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_340_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98212, ],
    'CountWeighted'                                              : [        98203,        98210,        98205, ],
    'CountWeightedLHEWeightScale'                                : [       102260,        98203,        94110,       102260,        98203,        94110,       102260,        98203,        94110, ],
    'CountWeightedL1PrefireNom'                                  : [        96380,        96379,        96384, ],
    'CountWeightedL1Prefire'                                     : [        96380,        95913,        96844, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       100340,        96379,        92373,       100340,        96379,        92373,       100340,        96379,        92373, ],
  }),
  ("nof_tree_events",                 98212),
  ("nof_db_events",                   98212),
  ("fsize_local",                     712302807), # 712.30MB, avg file size 356.15MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98789, ],
    'CountWeighted'                                              : [        98794,        98796,        98794, ],
    'CountWeightedLHEWeightScale'                                : [       103800,        98793,        93934,       103800,        98793,        93934,       103800,        98793,        93934, ],
    'CountWeightedL1PrefireNom'                                  : [        96891,        96888,        96895, ],
    'CountWeightedL1Prefire'                                     : [        96891,        96412,        97370, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       101782,        96890,        92142,       101782,        96890,        92142,       101782,        96890,        92142, ],
  }),
  ("nof_tree_events",                 98789),
  ("nof_db_events",                   98789),
  ("fsize_local",                     740628690), # 740.63MB, avg file size 370.31MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4t"),
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
  ("nof_files",                       3),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99991,        99997,        99988, ],
    'CountWeightedLHEWeightScale'                                : [       105907,        99990,        94442,       105907,        99990,        94442,       105907,        99990,        94442, ],
    'CountWeightedL1PrefireNom'                                  : [        98044,        98041,        98047, ],
    'CountWeightedL1Prefire'                                     : [        98044,        97555,        98532, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       103822,        98043,        92615,       103822,        98043,        92615,       103822,        98043,        92615, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     771237309), # 771.24MB, avg file size 257.08MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4t"),
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
    'CountWeighted'                                              : [        49534,        49533,        49539, ],
    'CountWeightedLHEWeightScale'                                : [        52827,        49534,        46503,        52827,        49534,        46503,        52827,        49534,        46503, ],
    'CountWeightedL1PrefireNom'                                  : [        48555,        48553,        48560, ],
    'CountWeightedL1Prefire'                                     : [        48555,        48312,        48799, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51774,        48555,        45590,        51774,        48555,        45590,        51774,        48555,        45590, ],
  }),
  ("nof_tree_events",                 49535),
  ("nof_db_events",                   49535),
  ("fsize_local",                     390727951), # 390.73MB, avg file size 390.73MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        50002,        50004,        50008, ],
    'CountWeightedLHEWeightScale'                                : [        53644,        50001,        46695,        53644,        50001,        46695,        53644,        50001,        46695, ],
    'CountWeightedL1PrefireNom'                                  : [        49008,        49008,        49012, ],
    'CountWeightedL1Prefire'                                     : [        49008,        48763,        49255, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        52570,        49007,        45775,        52570,        49007,        45775,        52570,        49007,        45775, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     403986453), # 403.99MB, avg file size 201.99MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4t"),
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
    'CountWeighted'                                              : [        49174,        49171,        49173, ],
    'CountWeightedLHEWeightScale'                                : [        53044,        49173,        45709,        53044,        49173,        45709,        53044,        49173,        45709, ],
    'CountWeightedL1PrefireNom'                                  : [        48210,        48205,        48210, ],
    'CountWeightedL1Prefire'                                     : [        48210,        47971,        48448, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        51996,        48209,        44818,        51996,        48209,        44818,        51996,        48209,        44818, ],
  }),
  ("nof_tree_events",                 49175),
  ("nof_db_events",                   49175),
  ("fsize_local",                     404147330), # 404.15MB, avg file size 404.15MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    1),
  ("nof_events",                      {
    'Count'                                                      : [        50000, ],
    'CountWeighted'                                              : [        50002,        49994,        49993, ],
    'CountWeightedLHEWeightScale'                                : [        54210,        50001,        46274,        54210,        50001,        46274,        54210,        50001,        46274, ],
    'CountWeightedL1PrefireNom'                                  : [        49022,        49015,        49018, ],
    'CountWeightedL1Prefire'                                     : [        49022,        48781,        49263, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53141,        49021,        45373,        53141,        49021,        45373,        53141,        49021,        45373, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     418488111), # 418.49MB, avg file size 209.24MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4t"),
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
    'CountWeighted'                                              : [        49077,        49080,        49078, ],
    'CountWeightedLHEWeightScale'                                : [        53452,        49077,        45243,        53452,        49077,        45243,        53452,        49077,        45243, ],
    'CountWeightedL1PrefireNom'                                  : [        48107,        48107,        48110, ],
    'CountWeightedL1Prefire'                                     : [        48107,        47870,        48345, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        52388,        48107,        44353,        52388,        48107,        44353,        52388,        48107,        44353, ],
  }),
  ("nof_tree_events",                 49080),
  ("nof_db_events",                   49080),
  ("fsize_local",                     416122840), # 416.12MB, avg file size 416.12MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4t"),
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
    'CountWeighted'                                              : [        50005,        49999,        49998, ],
    'CountWeightedLHEWeightScale'                                : [        54679,        50004,        45927,        54679,        50004,        45927,        54679,        50004,        45927, ],
    'CountWeightedL1PrefireNom'                                  : [        49028,        49023,        49026, ],
    'CountWeightedL1Prefire'                                     : [        49028,        48789,        49267, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53606,        49028,        45036,        53606,        49028,        45036,        53606,        49028,        45036, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     430103786), # 430.10MB, avg file size 430.10MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4t"),
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
    'CountWeighted'                                              : [        49168,        49172,        49171, ],
    'CountWeightedLHEWeightScale'                                : [        53982,        49167,        45011,        53982,        49167,        45011,        53982,        49167,        45011, ],
    'CountWeightedL1PrefireNom'                                  : [        48208,        48210,        48211, ],
    'CountWeightedL1Prefire'                                     : [        48208,        47973,        48443, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        52922,        48207,        44135,        52922,        48207,        44135,        52922,        48207,        44135, ],
  }),
  ("nof_tree_events",                 49178),
  ("nof_db_events",                   49178),
  ("fsize_local",                     428418273), # 428.42MB, avg file size 428.42MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4t"),
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
    'CountWeighted'                                              : [        49289,        49282,        49281, ],
    'CountWeightedLHEWeightScale'                                : [        54483,        49288,        44839,        54483,        49288,        44839,        54483,        49288,        44839, ],
    'CountWeightedL1PrefireNom'                                  : [        48323,        48316,        48321, ],
    'CountWeightedL1Prefire'                                     : [        48323,        48089,        48557, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [        53414,        48322,        43965,        53414,        48322,        43965,        53414,        48322,        43965, ],
  }),
  ("nof_tree_events",                 49283),
  ("nof_db_events",                   49283),
  ("fsize_local",                     436508904), # 436.51MB, avg file size 436.51MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4t"),
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
  ("nof_files",                       3),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99998,        99987,       100005, ],
    'CountWeightedLHEWeightScale'                                : [       128106,       120944,       114228,       105931,        99997,        94438,        89055,        84062,        79381, ],
    'CountWeightedL1PrefireNom'                                  : [        97881,        97871,        97888, ],
    'CountWeightedL1Prefire'                                     : [        97881,        97350,        98411, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       125370,       118384,       111828,       103667,        97880,        92452,        87152,        82281,        77712, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     764814998), # 764.81MB, avg file size 254.94MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100003,       100009,        99980, ],
    'CountWeightedLHEWeightScale'                                : [       127639,       121245,       115114,       105285,       100002,        94936,        88334,        83891,        79636, ],
    'CountWeightedL1PrefireNom'                                  : [        97972,        97969,        97964, ],
    'CountWeightedL1Prefire'                                     : [        97972,        97458,        98485, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       125024,       118785,       112798,       103127,        97971,        93024,        86522,        82187,        78031, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     750245195), # 750.25MB, avg file size 375.12MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_box_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        95878, ],
    'CountWeighted'                                              : [        95876,        95881,        95882, ],
    'CountWeightedLHEWeightScale'                                : [       125441,       114512,       105095,       105069,        95875,        87964,        89299,        81461,        74716, ],
    'CountWeightedL1PrefireNom'                                  : [        93660,        93666,        93661, ],
    'CountWeightedL1Prefire'                                     : [        93660,        93118,        94204, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       122521,       111869,       102688,       102619,        93659,        85946,        87215,        79577,        73000, ],
  }),
  ("nof_tree_events",                 95878),
  ("nof_db_events",                   95878),
  ("fsize_local",                     805191994), # 805.19MB, avg file size 402.60MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [        99000, ],
    'CountWeighted'                                              : [        98998,        99010,        98999, ],
    'CountWeightedLHEWeightScale'                                : [       127159,       119552,       112521,       105319,        98998,        93164,        88664,        83332,        78410, ],
    'CountWeightedL1PrefireNom'                                  : [        96852,        96855,        96857, ],
    'CountWeightedL1Prefire'                                     : [        96852,        96315,        97388, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       124377,       116961,       110103,       103012,        96851,        91159,        86721,        81524,        76721, ],
  }),
  ("nof_tree_events",                 99000),
  ("nof_db_events",                   99000),
  ("fsize_local",                     766163832), # 766.16MB, avg file size 383.08MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        97777, ],
    'CountWeighted'                                              : [        97770,        97781,        97777, ],
    'CountWeightedLHEWeightScale'                                : [       124978,       118449,       112251,       103183,        97770,        92648,        86637,        82086,        77771, ],
    'CountWeightedL1PrefireNom'                                  : [        95770,        95774,        95777, ],
    'CountWeightedL1Prefire'                                     : [        95770,        95265,        96274, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       122393,       116025,       109974,       101047,        95769,        90768,        84842,        80403,        76191, ],
  }),
  ("nof_tree_events",                 97777),
  ("nof_db_events",                   97777),
  ("fsize_local",                     739863728), # 739.86MB, avg file size 369.93MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98210, ],
    'CountWeighted'                                              : [        98206,        98224,        98212, ],
    'CountWeightedLHEWeightScale'                                : [       127343,       117934,       109592,       106082,        98205,        91236,        89747,        83063,        77145, ],
    'CountWeightedL1PrefireNom'                                  : [        95994,        95998,        96006, ],
    'CountWeightedL1Prefire'                                     : [        95994,        95446,        96542, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       124449,       115280,       107147,       103668,        95993,        89198,        87702,        81189,        75420, ],
  }),
  ("nof_tree_events",                 98210),
  ("nof_db_events",                   98210),
  ("fsize_local",                     794926682), # 794.93MB, avg file size 397.46MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99178, ],
    'CountWeighted'                                              : [        99184,        99185,        99173, ],
    'CountWeightedLHEWeightScale'                                : [       126566,       120296,       114306,       104379,        99184,        94214,        87566,        83181,        78999, ],
    'CountWeightedL1PrefireNom'                                  : [        97216,        97211,        97214, ],
    'CountWeightedL1Prefire'                                     : [        97216,        96718,        97712, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       124031,       117916,       112068,       102284,        97215,        92366,        85805,        81529,        77448, ],
  }),
  ("nof_tree_events",                 99178),
  ("nof_db_events",                   99178),
  ("fsize_local",                     745013956), # 745.01MB, avg file size 372.51MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        97801, ],
    'CountWeighted'                                              : [        97795,        97805,        97806, ],
    'CountWeightedLHEWeightScale'                                : [       123605,       119363,       114931,       101287,        97795,        94161,        84514,        81597,        78555, ],
    'CountWeightedL1PrefireNom'                                  : [        96046,        96049,        96055, ],
    'CountWeightedL1Prefire'                                     : [        96046,        95594,        96497, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       121370,       117227,       112892,        99454,        96045,        92489,        82983,        80135,        77159, ],
  }),
  ("nof_tree_events",                 97801),
  ("nof_db_events",                   97801),
  ("fsize_local",                     695033762), # 695.03MB, avg file size 347.52MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                      : [        99301, ],
    'CountWeighted'                                              : [        99296,        99305,        99308, ],
    'CountWeightedLHEWeightScale'                                : [       127635,       119887,       112767,       105753,        99295,        93379,        89062,        83607,        78604, ],
    'CountWeightedL1PrefireNom'                                  : [        97186,        97189,        97195, ],
    'CountWeightedL1Prefire'                                     : [        97186,        96658,        97714, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       124896,       117341,       110393,       103479,        97185,        91411,        87146,        81827,        76945, ],
  }),
  ("nof_tree_events",                 99301),
  ("nof_db_events",                   99301),
  ("fsize_local",                     771096882), # 771.10MB, avg file size 385.55MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98588, ],
    'CountWeighted'                                              : [        98601,        98593,        98590, ],
    'CountWeightedLHEWeightScale'                                : [       127436,       118590,       110648,       105968,        98596,        91965,        89511,        83259,        77652, ],
    'CountWeightedL1PrefireNom'                                  : [        96397,        96387,        96396, ],
    'CountWeightedL1Prefire'                                     : [        96397,        95851,        96942, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       124569,       115948,       108202,       103583,        96393,        89930,        87494,        81401,        75932, ],
  }),
  ("nof_tree_events",                 98588),
  ("nof_db_events",                   98588),
  ("fsize_local",                     789032917), # 789.03MB, avg file size 394.52MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        98724, ],
    'CountWeighted'                                              : [        98716,        98712,        98723, ],
    'CountWeightedLHEWeightScale'                                : [       125020,       120351,       115596,       102575,        98711,        94801,        85684,        82448,        79161, ],
    'CountWeightedL1PrefireNom'                                  : [        96915,        96913,        96919, ],
    'CountWeightedL1Prefire'                                     : [        96915,        96451,        97378, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       122714,       118156,       113508,       100681,        96912,        93086,        84100,        80940,        77727, ],
  }),
  ("nof_tree_events",                 98724),
  ("nof_db_events",                   98724),
  ("fsize_local",                     710633284), # 710.63MB, avg file size 355.32MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_4t"),
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
  ("nof_files",                       3),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [       100003,       100008,       100010, ],
    'CountWeightedLHEWeightScale'                                : [       127629,       121295,       115253,       105259,       100002,        94990,        88307,        83870,        79649, ],
    'CountWeightedL1PrefireNom'                                  : [        98026,        98032,        98029, ],
    'CountWeightedL1Prefire'                                     : [        98026,        97526,        98526, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       125083,       118904,       113003,       103155,        98025,        93132,        86539,        82211,        78089, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     750399870), # 750.40MB, avg file size 250.13MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_4t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                      : [        99190, ],
    'CountWeighted'                                              : [        99188,        99181,        99192, ],
    'CountWeightedLHEWeightScale'                                : [       125928,       120693,       115473,       103504,        99187,        94889,        86582,        82963,        79359, ],
    'CountWeightedL1PrefireNom'                                  : [        97304,        97295,        97311, ],
    'CountWeightedL1Prefire'                                     : [        97304,        96823,        97784, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       123515,       118403,       113300,       101518,        97303,        93101,        84920,        81387,        77864, ],
  }),
  ("nof_tree_events",                 99190),
  ("nof_db_events",                   99190),
  ("fsize_local",                     722917701), # 722.92MB, avg file size 361.46MB
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
        ("path",      "/hdfs/local/snandan/ttHNtupleProduction/2016/2019Aug12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4t"),
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

