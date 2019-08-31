from collections import OrderedDict as OD

# file generated at 2019-08-31 14:32:08 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_hh.py -M

samples_2017 = OD()
samples_2017["/GluGluToRadionToHHTo4Tau_M-250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399981,       399944,       399952, ],
    'CountWeightedL1PrefireNom'                                  : [       391772,       391736,       391767, ],
    'CountWeightedL1Prefire'                                     : [       391772,       389652,       393812, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2796291343), # 2.80GB, avg file size 349.54MB
  ("fsize_db",                        20114964479), # 20.11GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-260_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399957,       399980,       399971, ],
    'CountWeightedLHEWeightScale'                                : [       406231,       399957,       391167,       406231,       399957,       391167,       406231,       399957,       391167, ],
    'CountWeightedL1PrefireNom'                                  : [       391469,       391466,       391497, ],
    'CountWeightedL1Prefire'                                     : [       391469,       389295,       393567, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       397549,       391469,       382906,       397549,       391469,       382906,       397549,       391469,       382906, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2808792468), # 2.81GB, avg file size 351.10MB
  ("fsize_db",                        19104985604), # 19.10GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-270_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       385000, ],
    'CountWeighted'                                              : [       384990,       384959,       384954, ],
    'CountWeightedLHEWeightScale'                                : [       392246,       384990,       375519,       392246,       384990,       375519,       392246,       384990,       375519, ],
    'CountWeightedL1PrefireNom'                                  : [       376398,       376363,       376384, ],
    'CountWeightedL1Prefire'                                     : [       376398,       374221,       378504, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       383435,       376398,       367191,       383435,       376398,       367191,       383435,       376398,       367191, ],
  }),
  ("nof_tree_events",                 385000),
  ("nof_db_events",                   385000),
  ("fsize_local",                     2728099850), # 2.73GB, avg file size 341.01MB
  ("fsize_db",                        18511645006), # 18.51GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-280_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       400021,       399993,       399949, ],
    'CountWeightedL1PrefireNom'                                  : [       390739,       390699,       390710, ],
    'CountWeightedL1Prefire'                                     : [       390739,       388406,       392998, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2866609319), # 2.87GB, avg file size 358.33MB
  ("fsize_db",                        20219319064), # 20.22GB, avg file size 962.82MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_4t"),
  ("nof_files",                       6),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300000,       299960,       299988, ],
    'CountWeightedLHEWeightScale'                                : [       308250,       300000,       290541,       308250,       300000,       290541,       308250,       300000,       290541, ],
    'CountWeightedL1PrefireNom'                                  : [       292640,       292599,       292653, ],
    'CountWeightedL1Prefire'                                     : [       292640,       290811,       294418, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       300641,       292640,       283458,       300641,       292640,       283458,       300641,       292640,       283458, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2173528525), # 2.17GB, avg file size 362.25MB
  ("fsize_db",                        14610494649), # 14.61GB, avg file size 859.44MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_4t"),
  ("nof_files",                       6),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       284000, ],
    'CountWeighted'                                              : [       283946,       283959,       283961, ],
    'CountWeightedLHEWeightScale'                                : [       295334,       283946,       272282,       295334,       283946,       272282,       295334,       283946,       272282, ],
    'CountWeightedL1PrefireNom'                                  : [       276064,       276069,       276077, ],
    'CountWeightedL1Prefire'                                     : [       276064,       274153,       277934, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       287071,       276064,       264762,       287071,       276064,       264762,       287071,       276064,       264762, ],
  }),
  ("nof_tree_events",                 284000),
  ("nof_db_events",                   284000),
  ("fsize_local",                     2120002853), # 2.12GB, avg file size 353.33MB
  ("fsize_db",                        14267271177), # 14.27GB, avg file size 713.36MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_4t"),
  ("nof_files",                       6),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299987,       299965,       299978, ],
    'CountWeightedLHEWeightScale'                                : [       315123,       299977,       285268,       315123,       299977,       285268,       315123,       299977,       285268, ],
    'CountWeightedL1PrefireNom'                                  : [       291069,       291054,       291054, ],
    'CountWeightedL1Prefire'                                     : [       291069,       288934,       293163, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       305694,       291061,       276840,       305694,       291061,       276840,       305694,       291061,       276840, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2301688820), # 2.30GB, avg file size 383.61MB
  ("fsize_db",                        15112224162), # 15.11GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-450_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_4t"),
  ("nof_files",                       6),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299942,       299951,       299955, ],
    'CountWeightedLHEWeightScale'                                : [       317787,       299942,       283230,       317787,       299942,       283230,       317787,       299942,       283230, ],
    'CountWeightedL1PrefireNom'                                  : [       290447,       290431,       290467, ],
    'CountWeightedL1Prefire'                                     : [       290447,       288201,       292660, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       307647,       290447,       274310,       307647,       290447,       274310,       307647,       290447,       274310, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2364625138), # 2.36GB, avg file size 394.10MB
  ("fsize_db",                        15314286391), # 15.31GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199994,       199993,       200010, ],
    'CountWeightedLHEWeightScale'                                : [       213409,       199993,       187650,       213409,       199993,       187650,       213409,       199993,       187650, ],
    'CountWeightedL1PrefireNom'                                  : [       193304,       193286,       193326, ],
    'CountWeightedL1Prefire'                                     : [       193304,       191734,       194850, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       206222,       193303,       181411,       206222,       193303,       181411,       206222,       193303,       181411, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1607204561), # 1.61GB, avg file size 401.80MB
  ("fsize_db",                        10307241524), # 10.31GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-550_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199969,       199978,       199951, ],
    'CountWeightedLHEWeightScale'                                : [       214722,       199968,       186567,       214722,       199968,       186567,       214722,       199968,       186567, ],
    'CountWeightedL1PrefireNom'                                  : [       192983,       192991,       192966, ],
    'CountWeightedL1Prefire'                                     : [       192983,       191356,       194588, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       207176,       192981,       180091,       207176,       192981,       180091,       207176,       192981,       180091, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1637956140), # 1.64GB, avg file size 409.49MB
  ("fsize_db",                        10435371711), # 10.44GB, avg file size 948.67MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-600_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199968,       199970,       199978, ],
    'CountWeightedLHEWeightScale'                                : [       215952,       199968,       185667,       215952,       199968,       185667,       215952,       199968,       185667, ],
    'CountWeightedL1PrefireNom'                                  : [       192771,       192765,       192784, ],
    'CountWeightedL1Prefire'                                     : [       192771,       191099,       194421, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       208128,       192771,       179016,       208128,       192771,       179016,       208128,       192771,       179016, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1665295566), # 1.67GB, avg file size 416.32MB
  ("fsize_db",                        10556003606), # 10.56GB, avg file size 812.00MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-650_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199963,       199982,       199982, ],
    'CountWeightedLHEWeightScale'                                : [       217053,       199963,       184820,       217053,       199963,       184820,       217053,       199963,       184820, ],
    'CountWeightedL1PrefireNom'                                  : [       192689,       192702,       192701, ],
    'CountWeightedL1Prefire'                                     : [       192689,       191007,       194353, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       209106,       192689,       178129,       209106,       192689,       178129,       209106,       192689,       178129, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1687088879), # 1.69GB, avg file size 421.77MB
  ("fsize_db",                        10638007613), # 10.64GB, avg file size 709.20MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-700_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199978,       199947,       199962, ],
    'CountWeightedLHEWeightScale'                                : [       218024,       199978,       184060,       218024,       199978,       184060,       218024,       199978,       184060, ],
    'CountWeightedL1PrefireNom'                                  : [       192477,       192428,       192495, ],
    'CountWeightedL1Prefire'                                     : [       192477,       190752,       194183, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       209806,       192477,       177196,       209806,       192477,       177196,       209806,       192477,       177196, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1709691925), # 1.71GB, avg file size 427.42MB
  ("fsize_db",                        10705047349), # 10.71GB, avg file size 823.47MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199982,       199985,       199978, ],
    'CountWeightedL1PrefireNom'                                  : [       192286,       192276,       192286, ],
    'CountWeightedL1Prefire'                                     : [       192286,       190520,       194032, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1738710285), # 1.74GB, avg file size 434.68MB
  ("fsize_db",                        11200569052), # 11.20GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-800_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199967,       199955,       199960, ],
    'CountWeightedL1PrefireNom'                                  : [       192242,       192228,       192246, ],
    'CountWeightedL1Prefire'                                     : [       192242,       190473,       193992, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1758859506), # 1.76GB, avg file size 439.71MB
  ("fsize_db",                        11266991203), # 11.27GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-850_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       192000, ],
    'CountWeighted'                                              : [       191956,       191951,       191967, ],
    'CountWeightedL1PrefireNom'                                  : [       184441,       184441,       184441, ],
    'CountWeightedL1Prefire'                                     : [       184441,       182724,       186142, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     1704942135), # 1.70GB, avg file size 426.24MB
  ("fsize_db",                        10933218336), # 10.93GB, avg file size 993.93MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-900_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99989,        99985,        99985, ],
    'CountWeightedLHEWeightScale'                                : [       110679,        99989,        90822,       110679,        99989,        90822,       110679,        99989,        90822, ],
    'CountWeightedL1PrefireNom'                                  : [        96055,        96057,        96045, ],
    'CountWeightedL1Prefire'                                     : [        96055,        95160,        96942, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106300,        96055,        87265,       106300,        96055,        87265,       106300,        96055,        87265, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     891464016), # 891.46MB, avg file size 445.73MB
  ("fsize_db",                        5507575850), # 5.51GB, avg file size 917.93MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-1000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99983,        99979,        99983, ],
    'CountWeightedLHEWeightScale'                                : [       111348,        99983,        90344,       111348,        99983,        90344,       111348,        99983,        90344, ],
    'CountWeightedL1PrefireNom'                                  : [        95968,        95950,        95982, ],
    'CountWeightedL1Prefire'                                     : [        95968,        95058,        96871, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106853,        95968,        86730,       106853,        95968,        86730,       106853,        95968,        86730, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     904709037), # 904.71MB, avg file size 452.35MB
  ("fsize_db",                        5537065038), # 5.54GB, avg file size 1.38GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       391000, ],
    'CountWeighted'                                              : [       390972,       390952,       390961, ],
    'CountWeightedLHEWeightScale'                                : [       395790,       390961,       383408,       395790,       390961,       383408,       395790,       390961,       383408, ],
    'CountWeightedL1PrefireNom'                                  : [       382625,       382579,       382644, ],
    'CountWeightedL1Prefire'                                     : [       382625,       380484,       384686, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       387283,       382616,       375265,       387283,       382616,       375265,       387283,       382616,       375265, ],
  }),
  ("nof_tree_events",                 391000),
  ("nof_db_events",                   391000),
  ("fsize_local",                     2757203085), # 2.76GB, avg file size 344.65MB
  ("fsize_db",                        18879671024), # 18.88GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_4t"),
  ("nof_files",                       9),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                      : [       386000, ],
    'CountWeighted'                                              : [       385993,       385978,       385987, ],
    'CountWeightedLHEWeightScale'                                : [       392027,       385993,       377478,       392027,       385993,       377478,       392027,       385993,       377478, ],
    'CountWeightedL1PrefireNom'                                  : [       377361,       377338,       377371, ],
    'CountWeightedL1Prefire'                                     : [       377361,       375178,       379476, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       383209,       377361,       369087,       383209,       377361,       369087,       383209,       377361,       369087, ],
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     2751391872), # 2.75GB, avg file size 305.71MB
  ("fsize_db",                        18925798715), # 18.93GB, avg file size 727.92MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_4t"),
  ("nof_files",                       9),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                      : [       380000, ],
    'CountWeighted'                                              : [       379949,       379944,       379945, ],
    'CountWeightedLHEWeightScale'                                : [       387118,       379946,       370629,       387118,       379946,       370629,       387118,       379946,       370629, ],
    'CountWeightedL1PrefireNom'                                  : [       371201,       371193,       371197, ],
    'CountWeightedL1Prefire'                                     : [       371201,       369004,       373331, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       378139,       371198,       362139,       378139,       371198,       362139,       378139,       371198,       362139, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     2730618246), # 2.73GB, avg file size 303.40MB
  ("fsize_db",                        18931125504), # 18.93GB, avg file size 728.12MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    30),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399977,       400020,       400013, ],
    'CountWeightedLHEWeightScale'                                : [       408716,       399973,       389180,       408716,       399973,       389180,       408716,       399973,       389180, ],
    'CountWeightedL1PrefireNom'                                  : [       390461,       390483,       390484, ],
    'CountWeightedL1Prefire'                                     : [       390461,       388090,       392765, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       398926,       390457,       379977,       398926,       390457,       379977,       398926,       390457,       379977, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2897314649), # 2.90GB, avg file size 362.16MB
  ("fsize_db",                        19706361148), # 19.71GB, avg file size 656.88MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_4t"),
  ("nof_files",                       9),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399965,       399968,       399955, ],
    'CountWeightedLHEWeightScale'                                : [       411018,       399965,       387360,       411018,       399965,       387360,       411018,       399965,       387360, ],
    'CountWeightedL1PrefireNom'                                  : [       389879,       389853,       389899, ],
    'CountWeightedL1Prefire'                                     : [       389879,       387395,       392300, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       400572,       389879,       377651,       400572,       389879,       377651,       400572,       389879,       377651, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2946045100), # 2.95GB, avg file size 327.34MB
  ("fsize_db",                        20098276225), # 20.10GB, avg file size 773.01MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_4t"),
  ("nof_files",                       6),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       298000, ],
    'CountWeighted'                                              : [       297969,       297955,       297963, ],
    'CountWeightedLHEWeightScale'                                : [       307748,       297969,       287345,       307748,       297969,       287345,       307748,       297969,       287345, ],
    'CountWeightedL1PrefireNom'                                  : [       290160,       290142,       290159, ],
    'CountWeightedL1Prefire'                                     : [       290160,       288258,       292020, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       299624,       290160,       279865,       299624,       290160,       279865,       299624,       290160,       279865, ],
  }),
  ("nof_tree_events",                 298000),
  ("nof_db_events",                   298000),
  ("fsize_local",                     2223551347), # 2.22GB, avg file size 370.59MB
  ("fsize_db",                        15176832017), # 15.18GB, avg file size 758.84MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       384000, ],
    'CountWeighted'                                              : [       383965,       383989,       383997, ],
    'CountWeightedLHEWeightScale'                                : [       399334,       383965,       368162,       399334,       383965,       368162,       399334,       383965,       368162, ],
    'CountWeightedL1PrefireNom'                                  : [       373388,       373385,       373425, ],
    'CountWeightedL1Prefire'                                     : [       373388,       370847,       375879, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       388245,       373388,       358089,       388245,       373388,       358089,       388245,       373388,       358089, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     2918586267), # 2.92GB, avg file size 364.82MB
  ("fsize_db",                        19349982170), # 19.35GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_4t"),
  ("nof_files",                       6),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299964,       299957,       300016, ],
    'CountWeightedLHEWeightScale'                                : [       315121,       299964,       285265,       315121,       299964,       285265,       315121,       299964,       285265, ],
    'CountWeightedL1PrefireNom'                                  : [       291247,       291236,       291277, ],
    'CountWeightedL1Prefire'                                     : [       291247,       289182,       293278, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       305888,       291247,       277028,       305888,       291247,       277028,       305888,       291247,       277028, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2356268987), # 2.36GB, avg file size 392.71MB
  ("fsize_db",                        15427844934), # 15.43GB, avg file size 857.10MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_4t"),
  ("nof_files",                       6),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                      : [       280000, ],
    'CountWeighted'                                              : [       279981,       279970,       279961, ],
    'CountWeightedLHEWeightScale'                                : [       296585,       279981,       264337,       296585,       279981,       264337,       296585,       279981,       264337, ],
    'CountWeightedL1PrefireNom'                                  : [       271531,       271512,       271531, ],
    'CountWeightedL1Prefire'                                     : [       271531,       269559,       273477, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       287570,       271531,       256421,       287570,       271531,       256421,       287570,       271531,       256421, ],
  }),
  ("nof_tree_events",                 280000),
  ("nof_db_events",                   280000),
  ("fsize_local",                     2255229116), # 2.26GB, avg file size 375.87MB
  ("fsize_db",                        14667839164), # 14.67GB, avg file size 637.73MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_4t"),
  ("nof_files",                       7),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                      : [       284000, ],
    'CountWeighted'                                              : [       283992,       283986,       283987, ],
    'CountWeightedLHEWeightScale'                                : [       303028,       283992,       266466,       303028,       283992,       266466,       303028,       283992,       266466, ],
    'CountWeightedL1PrefireNom'                                  : [       275458,       275442,       275463, ],
    'CountWeightedL1Prefire'                                     : [       275458,       273470,       277417, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       293851,       275458,       258516,       293851,       275458,       258516,       293851,       275458,       258516, ],
  }),
  ("nof_tree_events",                 284000),
  ("nof_db_events",                   284000),
  ("fsize_local",                     2336477523), # 2.34GB, avg file size 333.78MB
  ("fsize_db",                        15248320207), # 15.25GB, avg file size 693.11MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199974,       199973,       199966, ],
    'CountWeightedLHEWeightScale'                                : [       214739,       199973,       186585,       214739,       199973,       186585,       214739,       199973,       186585, ],
    'CountWeightedL1PrefireNom'                                  : [       193923,       193920,       193925, ],
    'CountWeightedL1Prefire'                                     : [       193923,       192522,       195305, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       208188,       193921,       180979,       208188,       193921,       180979,       208188,       193921,       180979, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1676140680), # 1.68GB, avg file size 419.04MB
  ("fsize_db",                        10729026481), # 10.73GB, avg file size 536.45MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       198000, ],
    'CountWeighted'                                              : [       197963,       197974,       197962, ],
    'CountWeightedLHEWeightScale'                                : [       213783,       197963,       183801,       213783,       197963,       183801,       213783,       197963,       183801, ],
    'CountWeightedL1PrefireNom'                                  : [       191914,       191913,       191925, ],
    'CountWeightedL1Prefire'                                     : [       191914,       190519,       193293, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       207202,       191914,       178218,       207202,       191914,       178218,       207202,       191914,       178218, ],
  }),
  ("nof_tree_events",                 198000),
  ("nof_db_events",                   198000),
  ("fsize_local",                     1685938741), # 1.69GB, avg file size 421.48MB
  ("fsize_db",                        10881260447), # 10.88GB, avg file size 604.51MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_4t"),
  ("nof_files",                       5),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199985,       199975,       199969, ],
    'CountWeightedLHEWeightScale'                                : [       217058,       199982,       184825,       217058,       199982,       184825,       217058,       199982,       184825, ],
    'CountWeightedL1PrefireNom'                                  : [       193908,       193885,       193912, ],
    'CountWeightedL1Prefire'                                     : [       193908,       192509,       195290, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       210417,       193906,       179245,       210417,       193906,       179245,       210417,       193906,       179245, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1728500899), # 1.73GB, avg file size 345.70MB
  ("fsize_db",                        10995288880), # 11.00GB, avg file size 610.85MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       189000, ],
    'CountWeighted'                                              : [       188957,       188983,       188963, ],
    'CountWeightedLHEWeightScale'                                : [       206033,       188957,       173933,       206033,       188957,       173933,       206033,       188957,       173933, ],
    'CountWeightedL1PrefireNom'                                  : [       183321,       183317,       183347, ],
    'CountWeightedL1Prefire'                                     : [       183321,       182024,       184600, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       199847,       183321,       168772,       199847,       183321,       168772,       199847,       183321,       168772, ],
  }),
  ("nof_tree_events",                 189000),
  ("nof_db_events",                   189000),
  ("fsize_local",                     1654778233), # 1.65GB, avg file size 413.69MB
  ("fsize_db",                        10562893577), # 10.56GB, avg file size 528.14MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_4t"),
  ("nof_files",                       5),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                      : [       196000, ],
    'CountWeighted'                                              : [       195970,       195972,       195993, ],
    'CountWeightedLHEWeightScale'                                : [       214585,       195970,       179716,       214585,       195970,       179716,       214585,       195970,       179716, ],
    'CountWeightedL1PrefireNom'                                  : [       190111,       190097,       190147, ],
    'CountWeightedL1Prefire'                                     : [       190111,       188766,       191438, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       208126,       190111,       174371,       208126,       190111,       174371,       208126,       190111,       174371, ],
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     1740511465), # 1.74GB, avg file size 348.10MB
  ("fsize_db",                        11128480225), # 11.13GB, avg file size 428.02MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_4t"),
  ("nof_files",                       5),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199966,       199973,       199973, ],
    'CountWeightedLHEWeightScale'                                : [       219805,       199966,       182748,       219805,       199966,       182748,       219805,       199966,       182748, ],
    'CountWeightedL1PrefireNom'                                  : [       194028,       194015,       194045, ],
    'CountWeightedL1Prefire'                                     : [       194028,       192667,       195371, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       213239,       194028,       177348,       213239,       194028,       177348,       213239,       194028,       177348, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1792637265), # 1.79GB, avg file size 358.53MB
  ("fsize_db",                        11297900227), # 11.30GB, avg file size 470.75MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       194000, ],
    'CountWeighted'                                              : [       193946,       193943,       193941, ],
    'CountWeightedL1PrefireNom'                                  : [       188187,       188166,       188204, ],
    'CountWeightedL1Prefire'                                     : [       188187,       186868,       189489, ],
  }),
  ("nof_tree_events",                 194000),
  ("nof_db_events",                   194000),
  ("fsize_local",                     1761934142), # 1.76GB, avg file size 440.48MB
  ("fsize_db",                        11268378526), # 11.27GB, avg file size 704.27MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_4t"),
  ("nof_files",                       3),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99995,        99992,        99995, ],
    'CountWeightedLHEWeightScale'                                : [       110549,        99995,        90972,       110549,        99995,        90972,       110549,        99995,        90972, ],
    'CountWeightedL1PrefireNom'                                  : [        97157,        97147,        97167, ],
    'CountWeightedL1Prefire'                                     : [        97157,        96507,        97798, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107395,        97157,        88404,       107395,        97157,        88404,       107395,        97157,        88404, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     913081329), # 913.08MB, avg file size 304.36MB
  ("fsize_db",                        5743750248), # 5.74GB, avg file size 441.83MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99951,        99952,        99954, ],
    'CountWeightedLHEWeightScale'                                : [       111317,        99951,        90317,       111317,        99951,        90317,       111317,        99951,        90317, ],
    'CountWeightedL1PrefireNom'                                  : [        97033,        97026,        97042, ],
    'CountWeightedL1Prefire'                                     : [        97033,        96366,        97690, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       108053,        97033,        87685,       108053,        97033,        87685,       108053,        97033,        87685, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     923880924), # 923.88MB, avg file size 461.94MB
  ("fsize_db",                        5923175401), # 5.92GB, avg file size 311.75MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2v2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       399997, ],
    'CountWeighted'                                              : [       399975,       399976,       399958, ],
    'CountWeightedL1PrefireNom'                                  : [       392705,       392690,       392708, ],
    'CountWeightedL1Prefire'                                     : [       392705,       390794,       394519, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     2880843669), # 2.88GB, avg file size 320.09MB
  ("fsize_db",                        20344351713), # 20.34GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2v2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       399993, ],
    'CountWeighted'                                              : [       399999,       400010,       399966, ],
    'CountWeightedLHEWeightScale'                                : [       406245,       399997,       391167,       406245,       399997,       391167,       406245,       399997,       391167, ],
    'CountWeightedL1PrefireNom'                                  : [       392350,       392341,       392346, ],
    'CountWeightedL1Prefire'                                     : [       392350,       390362,       394244, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       398437,       392348,       383730,       398437,       392348,       383730,       398437,       392348,       383730, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     2903326928), # 2.90GB, avg file size 362.92MB
  ("fsize_db",                        19527920598), # 19.53GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2v2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       399995, ],
    'CountWeighted'                                              : [       399973,       399974,       399983, ],
    'CountWeightedLHEWeightScale'                                : [       407505,       399973,       390157,       407505,       399973,       390157,       407505,       399973,       390157, ],
    'CountWeightedL1PrefireNom'                                  : [       392045,       392030,       392067, ],
    'CountWeightedL1Prefire'                                     : [       392045,       389998,       394000, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       399375,       392045,       382461,       399375,       392045,       382461,       399375,       392045,       382461, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     2934931208), # 2.93GB, avg file size 366.87MB
  ("fsize_db",                        19473148919), # 19.47GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2v2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    27),
  ("nof_events",                      {
    'Count'                                                      : [       379996, ],
    'CountWeighted'                                              : [       379996,       379969,       379948, ],
    'CountWeightedL1PrefireNom'                                  : [       372155,       372128,       372134, ],
    'CountWeightedL1Prefire'                                     : [       372155,       370146,       374078, ],
  }),
  ("nof_tree_events",                 379996),
  ("nof_db_events",                   379996),
  ("fsize_local",                     2830350803), # 2.83GB, avg file size 353.79MB
  ("fsize_db",                        19590423166), # 19.59GB, avg file size 725.57MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2v2t"),
  ("nof_files",                       7),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       299994, ],
    'CountWeighted'                                              : [       300005,       299981,       299973, ],
    'CountWeightedLHEWeightScale'                                : [       308247,       300003,       290535,       308247,       300003,       290535,       308247,       300003,       290535, ],
    'CountWeightedL1PrefireNom'                                  : [       293285,       293260,       293276, ],
    'CountWeightedL1Prefire'                                     : [       293285,       291591,       294915, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301307,       293283,       284071,       301307,       293283,       284071,       301307,       293283,       284071, ],
  }),
  ("nof_tree_events",                 299994),
  ("nof_db_events",                   299994),
  ("fsize_local",                     2271869874), # 2.27GB, avg file size 324.55MB
  ("fsize_db",                        14916149163), # 14.92GB, avg file size 828.67MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2v2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299952,       299968,       299975, ],
    'CountWeightedLHEWeightScale'                                : [       309818,       299952,       289291,       309818,       299952,       289291,       309818,       299952,       289291, ],
    'CountWeightedL1PrefireNom'                                  : [       292934,       292929,       292969, ],
    'CountWeightedL1Prefire'                                     : [       292934,       291174,       294633, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       302514,       292933,       282553,       302514,       292933,       282553,       302514,       292933,       282553, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     2310849104), # 2.31GB, avg file size 385.14MB
  ("fsize_db",                        14997791200), # 15.00GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2v2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       299990, ],
    'CountWeighted'                                              : [       299981,       299963,       299967, ],
    'CountWeightedLHEWeightScale'                                : [       311967,       299978,       287629,       311967,       299978,       287629,       311967,       299978,       287629, ],
    'CountWeightedL1PrefireNom'                                  : [       292373,       292341,       292391, ],
    'CountWeightedL1Prefire'                                     : [       292373,       290493,       294194, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       304010,       292369,       280377,       304010,       292369,       280377,       304010,       292369,       280377, ],
  }),
  ("nof_tree_events",                 299990),
  ("nof_db_events",                   299990),
  ("fsize_local",                     2364541711), # 2.36GB, avg file size 394.09MB
  ("fsize_db",                        15235183188), # 15.24GB, avg file size 952.20MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2v2t"),
  ("nof_files",                       7),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       286992, ],
    'CountWeighted'                                              : [       286985,       286956,       286968, ],
    'CountWeightedLHEWeightScale'                                : [       301464,       286985,       272892,       301464,       286985,       272892,       301464,       286985,       272892, ],
    'CountWeightedL1PrefireNom'                                  : [       278893,       278867,       278890, ],
    'CountWeightedL1Prefire'                                     : [       278893,       276932,       280804, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       292915,       278893,       265247,       292915,       278893,       265247,       292915,       278893,       265247, ],
  }),
  ("nof_tree_events",                 286992),
  ("nof_db_events",                   286992),
  ("fsize_local",                     2332895778), # 2.33GB, avg file size 333.27MB
  ("fsize_db",                        14884438376), # 14.88GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2v2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       291993, ],
    'CountWeighted'                                              : [       291961,       291968,       291924, ],
    'CountWeightedLHEWeightScale'                                : [       309273,       291961,       275680,       309273,       291961,       275680,       309273,       291961,       275680, ],
    'CountWeightedL1PrefireNom'                                  : [       283171,       283170,       283159, ],
    'CountWeightedL1Prefire'                                     : [       283171,       281064,       285232, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       299907,       283171,       267430,       299907,       283171,       267430,       299907,       283171,       267430, ],
  }),
  ("nof_tree_events",                 291993),
  ("nof_db_events",                   291993),
  ("fsize_local",                     2433694514), # 2.43GB, avg file size 405.62MB
  ("fsize_db",                        15416817462), # 15.42GB, avg file size 906.87MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2v2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       269995, ],
    'CountWeighted'                                              : [       269970,       269974,       269979, ],
    'CountWeightedLHEWeightScale'                                : [       288063,       269970,       253310,       288063,       269970,       253310,       288063,       269970,       253310, ],
    'CountWeightedL1PrefireNom'                                  : [       261397,       261387,       261417, ],
    'CountWeightedL1Prefire'                                     : [       261397,       259364,       263393, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       278859,       261397,       245315,       278859,       261397,       245315,       278859,       261397,       245315, ],
  }),
  ("nof_tree_events",                 269995),
  ("nof_db_events",                   269995),
  ("fsize_local",                     2307577248), # 2.31GB, avg file size 384.60MB
  ("fsize_db",                        14437624405), # 14.44GB, avg file size 802.09MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2v2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       299996, ],
    'CountWeighted'                                              : [       299954,       299966,       299981, ],
    'CountWeightedLHEWeightScale'                                : [       322112,       299954,       279887,       322112,       299954,       279887,       322112,       299954,       279887, ],
    'CountWeightedL1PrefireNom'                                  : [       289900,       289897,       289935, ],
    'CountWeightedL1Prefire'                                     : [       289900,       287538,       292225, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       311240,       289900,       270556,       311240,       289900,       270556,       311240,       289900,       270556, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     2606970848), # 2.61GB, avg file size 434.50MB
  ("fsize_db",                        16219407866), # 16.22GB, avg file size 954.08MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       195995, ],
    'CountWeighted'                                              : [       196001,       195974,       195969, ],
    'CountWeightedLHEWeightScale'                                : [       211646,       196001,       181959,       211646,       196001,       181959,       211646,       196001,       181959, ],
    'CountWeightedL1PrefireNom'                                  : [       189212,       189188,       189202, ],
    'CountWeightedL1Prefire'                                     : [       189212,       187629,       190772, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       204276,       189212,       175697,       204276,       189212,       175697,       204276,       189212,       175697, ],
  }),
  ("nof_tree_events",                 195995),
  ("nof_db_events",                   195995),
  ("fsize_local",                     1726492517), # 1.73GB, avg file size 431.62MB
  ("fsize_db",                        10725957373), # 10.73GB, avg file size 893.83MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       199995, ],
    'CountWeighted'                                              : [       199974,       199966,       199961, ],
    'CountWeightedLHEWeightScale'                                : [       217038,       199974,       184816,       217038,       199974,       184816,       217038,       199974,       184816, ],
    'CountWeightedL1PrefireNom'                                  : [       192824,       192820,       192813, ],
    'CountWeightedL1Prefire'                                     : [       192824,       191160,       194463, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       209233,       192824,       178246,       209233,       192824,       178246,       209233,       192824,       178246, ],
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     1781974844), # 1.78GB, avg file size 445.49MB
  ("fsize_db",                        11039880992), # 11.04GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       191997, ],
    'CountWeighted'                                              : [       191989,       191990,       191992, ],
    'CountWeightedLHEWeightScale'                                : [       209334,       191989,       176703,       209334,       191989,       176703,       209334,       191989,       176703, ],
    'CountWeightedL1PrefireNom'                                  : [       184889,       184870,       184912, ],
    'CountWeightedL1Prefire'                                     : [       184889,       183248,       186508, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       201548,       184889,       170207,       201548,       184889,       170207,       201548,       184889,       170207, ],
  }),
  ("nof_tree_events",                 191997),
  ("nof_db_events",                   191997),
  ("fsize_local",                     1725947260), # 1.73GB, avg file size 431.49MB
  ("fsize_db",                        10772500407), # 10.77GB, avg file size 769.46MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       199998, ],
    'CountWeighted'                                              : [       199942,       199943,       199949, ],
    'CountWeightedL1PrefireNom'                                  : [       192516,       192493,       192544, ],
    'CountWeightedL1Prefire'                                     : [       192516,       190804,       194207, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1815725434), # 1.82GB, avg file size 453.93MB
  ("fsize_db",                        11660934047), # 11.66GB, avg file size 832.92MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2v2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       199999, ],
    'CountWeighted'                                              : [       199980,       199964,       199959, ],
    'CountWeightedL1PrefireNom'                                  : [       192393,       192369,       192388, ],
    'CountWeightedL1Prefire'                                     : [       192393,       190652,       194115, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1828438097), # 1.83GB, avg file size 365.69MB
  ("fsize_db",                        11774979133), # 11.77GB, avg file size 692.65MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       191996, ],
    'CountWeighted'                                              : [       191970,       191963,       191992, ],
    'CountWeightedL1PrefireNom'                                  : [       184561,       184541,       184589, ],
    'CountWeightedL1Prefire'                                     : [       184561,       182864,       186241, ],
  }),
  ("nof_tree_events",                 191996),
  ("nof_db_events",                   191996),
  ("fsize_local",                     1764393657), # 1.76GB, avg file size 441.10MB
  ("fsize_db",                        11335819766), # 11.34GB, avg file size 944.65MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                      : [       199997, ],
    'CountWeighted'                                              : [       199946,       199956,       199975, ],
    'CountWeightedLHEWeightScale'                                : [       221332,       199946,       181640,       221332,       199946,       181640,       221332,       199946,       181640, ],
    'CountWeightedL1PrefireNom'                                  : [       192073,       192069,       192107, ],
    'CountWeightedL1Prefire'                                     : [       192073,       190275,       193852, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       212558,       192073,       174514,       212558,       192073,       174514,       212558,       192073,       174514, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1836146223), # 1.84GB, avg file size 459.04MB
  ("fsize_db",                        11421628490), # 11.42GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2v2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                      : [        99998, ],
    'CountWeighted'                                              : [        99972,        99976,        99970, ],
    'CountWeightedLHEWeightScale'                                : [       111338,        99972,        90326,       111338,        99972,        90326,       111338,        99972,        90326, ],
    'CountWeightedL1PrefireNom'                                  : [        95945,        95943,        95951, ],
    'CountWeightedL1Prefire'                                     : [        95945,        95031,        96851, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106828,        95945,        86704,       106828,        95945,        86704,       106828,        95945,        86704, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     924535248), # 924.54MB, avg file size 308.18MB
  ("fsize_db",                        5783738671), # 5.78GB, avg file size 826.25MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2v2t"),
  ("nof_files",                       10),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                      : [       394995, ],
    'CountWeighted'                                              : [       394971,       394966,       395009, ],
    'CountWeightedLHEWeightScale'                                : [       399836,       394971,       387334,       399836,       394971,       387334,       399836,       394971,       387334, ],
    'CountWeightedL1PrefireNom'                                  : [       387383,       387360,       387424, ],
    'CountWeightedL1Prefire'                                     : [       387383,       385415,       389260, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       392110,       387383,       379928,       392110,       387383,       379928,       392110,       387383,       379928, ],
  }),
  ("nof_tree_events",                 394995),
  ("nof_db_events",                   394995),
  ("fsize_local",                     2868430632), # 2.87GB, avg file size 286.84MB
  ("fsize_db",                        19490651554), # 19.49GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2v2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       395995, ],
    'CountWeighted'                                              : [       395947,       395970,       395947, ],
    'CountWeightedLHEWeightScale'                                : [       402177,       395943,       387243,       402177,       395943,       387243,       402177,       395943,       387243, ],
    'CountWeightedL1PrefireNom'                                  : [       388000,       387995,       388013, ],
    'CountWeightedL1Prefire'                                     : [       388000,       385956,       389953, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       394049,       387996,       379501,       394049,       387996,       379501,       394049,       387996,       379501, ],
  }),
  ("nof_tree_events",                 395995),
  ("nof_db_events",                   395995),
  ("fsize_local",                     2913771512), # 2.91GB, avg file size 364.22MB
  ("fsize_db",                        19808318644), # 19.81GB, avg file size 943.25MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2v2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       399996, ],
    'CountWeighted'                                              : [       399986,       399979,       399952, ],
    'CountWeightedLHEWeightScale'                                : [       407513,       399974,       390139,       407513,       399974,       390139,       407513,       399974,       390139, ],
    'CountWeightedL1PrefireNom'                                  : [       391644,       391643,       391610, ],
    'CountWeightedL1Prefire'                                     : [       391644,       389514,       393686, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       398967,       391634,       382047,       398967,       391634,       382047,       398967,       391634,       382047, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     2979875292), # 2.98GB, avg file size 372.48MB
  ("fsize_db",                        19945565524), # 19.95GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2v2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                      : [       394995, ],
    'CountWeighted'                                              : [       394983,       394997,       394983, ],
    'CountWeightedLHEWeightScale'                                : [       403606,       394983,       384334,       403606,       394983,       384334,       403606,       394983,       384334, ],
    'CountWeightedL1PrefireNom'                                  : [       386488,       386486,       386508, ],
    'CountWeightedL1Prefire'                                     : [       386488,       384332,       388559, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       394871,       386488,       376112,       394871,       386488,       376112,       394871,       386488,       376112, ],
  }),
  ("nof_tree_events",                 394995),
  ("nof_db_events",                   394995),
  ("fsize_local",                     2978389713), # 2.98GB, avg file size 330.93MB
  ("fsize_db",                        19924344376), # 19.92GB, avg file size 830.18MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2v2t"),
  ("nof_files",                       7),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       299995, ],
    'CountWeighted'                                              : [       299957,       299967,       299968, ],
    'CountWeightedLHEWeightScale'                                : [       308248,       299957,       290519,       308248,       299957,       290519,       308248,       299957,       290519, ],
    'CountWeightedL1PrefireNom'                                  : [       293022,       293004,       293044, ],
    'CountWeightedL1Prefire'                                     : [       293022,       291282,       294698, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301066,       293022,       283833,       301066,       293022,       283833,       301066,       293022,       283833, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     2315638119), # 2.32GB, avg file size 330.81MB
  ("fsize_db",                        15226334046), # 15.23GB, avg file size 761.32MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_2v2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       284992, ],
    'CountWeighted'                                              : [       284960,       284987,       284963, ],
    'CountWeightedLHEWeightScale'                                : [       294325,       284957,       274830,       294325,       284957,       274830,       294325,       284957,       274830, ],
    'CountWeightedL1PrefireNom'                                  : [       278056,       278065,       278068, ],
    'CountWeightedL1Prefire'                                     : [       278056,       276348,       279713, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       287139,       278053,       268205,       287139,       278053,       268205,       287139,       278053,       268205, ],
  }),
  ("nof_tree_events",                 284992),
  ("nof_db_events",                   284992),
  ("fsize_local",                     2239087026), # 2.24GB, avg file size 373.18MB
  ("fsize_db",                        14565597893), # 14.57GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2v2t"),
  ("nof_files",                       7),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       299995, ],
    'CountWeighted'                                              : [       299961,       299972,       299948, ],
    'CountWeightedLHEWeightScale'                                : [       311970,       299961,       287616,       311970,       299961,       287616,       311970,       299961,       287616, ],
    'CountWeightedL1PrefireNom'                                  : [       292238,       292233,       292240, ],
    'CountWeightedL1Prefire'                                     : [       292238,       290354,       294072, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       303877,       292238,       280257,       303877,       292238,       280257,       303877,       292238,       280257, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     2416905960), # 2.42GB, avg file size 345.27MB
  ("fsize_db",                        15709690748), # 15.71GB, avg file size 924.10MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2v2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       289998, ],
    'CountWeighted'                                              : [       289971,       289968,       289958, ],
    'CountWeightedLHEWeightScale'                                : [       304609,       289971,       275741,       304609,       289971,       275741,       304609,       289971,       275741, ],
    'CountWeightedL1PrefireNom'                                  : [       281921,       281917,       281923, ],
    'CountWeightedL1Prefire'                                     : [       281921,       279993,       283808, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       296092,       281921,       268139,       296092,       281921,       268139,       296092,       281921,       268139, ],
  }),
  ("nof_tree_events",                 289998),
  ("nof_db_events",                   289998),
  ("fsize_local",                     2412650729), # 2.41GB, avg file size 402.11MB
  ("fsize_db",                        15476703995), # 15.48GB, avg file size 1.11GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2v2t"),
  ("nof_files",                       7),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       279993, ],
    'CountWeighted'                                              : [       279990,       279993,       279923, ],
    'CountWeightedLHEWeightScale'                                : [       296564,       279990,       264339,       296564,       279990,       264339,       296564,       279990,       264339, ],
    'CountWeightedL1PrefireNom'                                  : [       271977,       271967,       271946, ],
    'CountWeightedL1Prefire'                                     : [       271977,       270079,       273836, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       288025,       271977,       256835,       288025,       271977,       256835,       288025,       271977,       256835, ],
  }),
  ("nof_tree_events",                 279993),
  ("nof_db_events",                   279993),
  ("fsize_local",                     2402395363), # 2.40GB, avg file size 343.20MB
  ("fsize_db",                        15200236312), # 15.20GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       199997, ],
    'CountWeighted'                                              : [       199979,       199973,       199993, ],
    'CountWeightedLHEWeightScale'                                : [       213389,       199979,       187653,       213389,       199979,       187653,       213389,       199979,       187653, ],
    'CountWeightedL1PrefireNom'                                  : [       194033,       194025,       194046, ],
    'CountWeightedL1Prefire'                                     : [       194033,       192643,       195401, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       206990,       194033,       182110,       206990,       194033,       182110,       206990,       194033,       182110, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1749842723), # 1.75GB, avg file size 437.46MB
  ("fsize_db",                        11038820268), # 11.04GB, avg file size 849.14MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       199995, ],
    'CountWeighted'                                              : [       199966,       199981,       199964, ],
    'CountWeightedLHEWeightScale'                                : [       214724,       199966,       186589,       214724,       199966,       186589,       214724,       199966,       186589, ],
    'CountWeightedL1PrefireNom'                                  : [       194016,       194013,       194031, ],
    'CountWeightedL1Prefire'                                     : [       194016,       192630,       195380, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       208283,       194016,       181073,       208283,       194016,       181073,       208283,       194016,       181073, ],
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     1778963347), # 1.78GB, avg file size 444.74MB
  ("fsize_db",                        11235761543), # 11.24GB, avg file size 802.55MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2v2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       199996, ],
    'CountWeighted'                                              : [       199978,       199978,       199971, ],
    'CountWeightedLHEWeightScale'                                : [       215943,       199978,       185661,       215943,       199978,       185661,       215943,       199978,       185661, ],
    'CountWeightedL1PrefireNom'                                  : [       193918,       193902,       193924, ],
    'CountWeightedL1Prefire'                                     : [       193918,       192514,       195301, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       209354,       193918,       180070,       209354,       193918,       180070,       209354,       193918,       180070, ],
  }),
  ("nof_tree_events",                 199996),
  ("nof_db_events",                   199996),
  ("fsize_local",                     1801353854), # 1.80GB, avg file size 360.27MB
  ("fsize_db",                        11265507117), # 11.27GB, avg file size 804.68MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       195999, ],
    'CountWeighted'                                              : [       195994,       195984,       195970, ],
    'CountWeightedLHEWeightScale'                                : [       212731,       195992,       181129,       212731,       195992,       181129,       212731,       195992,       181129, ],
    'CountWeightedL1PrefireNom'                                  : [       190127,       190109,       190123, ],
    'CountWeightedL1Prefire'                                     : [       190127,       188773,       191462, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       206317,       190125,       175746,       206317,       190125,       175746,       206317,       190125,       175746, ],
  }),
  ("nof_tree_events",                 195999),
  ("nof_db_events",                   195999),
  ("fsize_local",                     1779335697), # 1.78GB, avg file size 444.83MB
  ("fsize_db",                        11148852408), # 11.15GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2v2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       195997, ],
    'CountWeighted'                                              : [       195987,       195973,       195969, ],
    'CountWeightedLHEWeightScale'                                : [       213670,       195983,       180389,       213670,       195983,       180389,       213670,       195983,       180389, ],
    'CountWeightedL1PrefireNom'                                  : [       190108,       190089,       190101, ],
    'CountWeightedL1Prefire'                                     : [       190108,       188756,       191440, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       207225,       190105,       175013,       207225,       190105,       175013,       207225,       190105,       175013, ],
  }),
  ("nof_tree_events",                 195997),
  ("nof_db_events",                   195997),
  ("fsize_local",                     1793998453), # 1.79GB, avg file size 358.80MB
  ("fsize_db",                        11274075929), # 11.27GB, avg file size 626.34MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       199999, ],
    'CountWeighted'                                              : [       199968,       199966,       199982, ],
    'CountWeightedLHEWeightScale'                                : [       218965,       199968,       183384,       218965,       199968,       183384,       218965,       199968,       183384, ],
    'CountWeightedL1PrefireNom'                                  : [       194031,       194009,       194064, ],
    'CountWeightedL1Prefire'                                     : [       194031,       192667,       195377, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       212420,       194031,       177967,       212420,       194031,       177967,       212420,       194031,       177967, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1840619215), # 1.84GB, avg file size 460.15MB
  ("fsize_db",                        11369615851), # 11.37GB, avg file size 1.89GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       199998, ],
    'CountWeighted'                                              : [       199994,       199992,       199974, ],
    'CountWeightedLHEWeightScale'                                : [       219821,       199994,       182765,       219821,       199994,       182765,       219821,       199994,       182765, ],
    'CountWeightedL1PrefireNom'                                  : [       194097,       194079,       194096, ],
    'CountWeightedL1Prefire'                                     : [       194097,       192745,       195428, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       213301,       194096,       177407,       213301,       194096,       177407,       213301,       194096,       177407, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1846793637), # 1.85GB, avg file size 461.70MB
  ("fsize_db",                        11488159001), # 11.49GB, avg file size 1.15GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_2v2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       191995, ],
    'CountWeighted'                                              : [       191964,       191972,       191959, ],
    'CountWeightedL1PrefireNom'                                  : [       186280,       186283,       186282, ],
    'CountWeightedL1Prefire'                                     : [       186280,       184980,       187563, ],
  }),
  ("nof_tree_events",                 191995),
  ("nof_db_events",                   191995),
  ("fsize_local",                     1786876588), # 1.79GB, avg file size 357.38MB
  ("fsize_db",                        11613877178), # 11.61GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [        99999, ],
    'CountWeighted'                                              : [        99995,       100013,       100004, ],
    'CountWeightedLHEWeightScale'                                : [       110556,        99995,        90982,       110556,        99995,        90982,       110556,        99995,        90982, ],
    'CountWeightedL1PrefireNom'                                  : [        97162,        97167,        97178, ],
    'CountWeightedL1Prefire'                                     : [        97162,        96513,        97802, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107405,        97162,        88415,       107405,        97162,        88415,       107405,        97162,        88415, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     928548363), # 928.55MB, avg file size 464.27MB
  ("fsize_db",                        5984452524), # 5.98GB, avg file size 598.45MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [        99999, ],
    'CountWeighted'                                              : [        99977,        99972,        99983, ],
    'CountWeightedLHEWeightScale'                                : [       111346,        99977,        90339,       111346,        99977,        90339,       111346,        99977,        90339, ],
    'CountWeightedL1PrefireNom'                                  : [        97017,        96998,        97035, ],
    'CountWeightedL1Prefire'                                     : [        97017,        96343,        97682, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       108033,        97017,        87673,       108033,        97017,        87673,       108033,        97017,        87673, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     930995174), # 931.00MB, avg file size 465.50MB
  ("fsize_db",                        5974953438), # 5.97GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4v"),
  ("nof_files",                       8),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       399999, ],
    'CountWeighted'                                              : [       399977,       399951,       399913, ],
    'CountWeightedL1PrefireNom'                                  : [       393485,       393454,       393446, ],
    'CountWeightedL1Prefire'                                     : [       393485,       391755,       395102, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     2934224628), # 2.93GB, avg file size 366.78MB
  ("fsize_db",                        20459339723), # 20.46GB, avg file size 1.46GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_4v"),
  ("nof_files",                       8),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       399998, ],
    'CountWeighted'                                              : [       399976,       400013,       399997, ],
    'CountWeightedLHEWeightScale'                                : [       406234,       399976,       391167,       406234,       399976,       391167,       406234,       399976,       391167, ],
    'CountWeightedL1PrefireNom'                                  : [       393234,       393247,       393251, ],
    'CountWeightedL1Prefire'                                     : [       393234,       391448,       394911, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       399352,       393234,       384600,       399352,       393234,       384600,       399352,       393234,       384600, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     2970611814), # 2.97GB, avg file size 371.33MB
  ("fsize_db",                        19550516838), # 19.55GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_4v"),
  ("nof_files",                       8),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       386000, ],
    'CountWeighted'                                              : [       385960,       385982,       385980, ],
    'CountWeightedLHEWeightScale'                                : [       393236,       385959,       376481,       393236,       385959,       376481,       393236,       385959,       376481, ],
    'CountWeightedL1PrefireNom'                                  : [       379146,       379149,       379169, ],
    'CountWeightedL1Prefire'                                     : [       379146,       377353,       380838, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       386257,       379144,       369861,       386257,       379144,       369861,       386257,       379144,       369861, ],
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     2910293785), # 2.91GB, avg file size 363.79MB
  ("fsize_db",                        18992366194), # 18.99GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_4v"),
  ("nof_files",                       9),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                      : [       388998, ],
    'CountWeighted'                                              : [       388972,       388960,       388970, ],
    'CountWeightedL1PrefireNom'                                  : [       381850,       381831,       381862, ],
    'CountWeightedL1Prefire'                                     : [       381850,       379985,       383612, ],
  }),
  ("nof_tree_events",                 388998),
  ("nof_db_events",                   388998),
  ("fsize_local",                     2985937464), # 2.99GB, avg file size 331.77MB
  ("fsize_db",                        20249921988), # 20.25GB, avg file size 880.43MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_4v"),
  ("nof_files",                       6),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299982,       300005,       300021, ],
    'CountWeightedLHEWeightScale'                                : [       308284,       299980,       290523,       308284,       299980,       290523,       308284,       299980,       290523, ],
    'CountWeightedL1PrefireNom'                                  : [       293957,       293969,       293985, ],
    'CountWeightedL1Prefire'                                     : [       293957,       292402,       295435, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       302054,       293955,       284716,       302054,       293955,       284716,       302054,       293955,       284716, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2347378932), # 2.35GB, avg file size 391.23MB
  ("fsize_db",                        15102940723), # 15.10GB, avg file size 943.93MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_4v"),
  ("nof_files",                       6),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299954,       299964,       299974, ],
    'CountWeightedLHEWeightScale'                                : [       309814,       299954,       289282,       309814,       299954,       289282,       309814,       299954,       289282, ],
    'CountWeightedL1PrefireNom'                                  : [       293535,       293517,       293564, ],
    'CountWeightedL1Prefire'                                     : [       293535,       291896,       295099, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       303138,       293535,       283118,       303138,       293535,       283118,       303138,       293535,       283118, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     2397629576), # 2.40GB, avg file size 399.60MB
  ("fsize_db",                        15313788135), # 15.31GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_4v"),
  ("nof_files",                       6),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       291998, ],
    'CountWeighted'                                              : [       291985,       291964,       291988, ],
    'CountWeightedLHEWeightScale'                                : [       303644,       291985,       279961,       303644,       291985,       279961,       303644,       291985,       279961, ],
    'CountWeightedL1PrefireNom'                                  : [       285191,       285161,       285215, ],
    'CountWeightedL1Prefire'                                     : [       285191,       283484,       286831, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       296542,       285191,       273482,       296542,       285191,       273482,       296542,       285191,       273482, ],
  }),
  ("nof_tree_events",                 291998),
  ("nof_db_events",                   291998),
  ("fsize_local",                     2396044539), # 2.40GB, avg file size 399.34MB
  ("fsize_db",                        15117730207), # 15.12GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_4v"),
  ("nof_files",                       7),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299986,       299956,       299978, ],
    'CountWeightedLHEWeightScale'                                : [       315131,       299986,       285266,       315131,       299986,       285266,       315131,       299986,       285266, ],
    'CountWeightedL1PrefireNom'                                  : [       292132,       292099,       292147, ],
    'CountWeightedL1Prefire'                                     : [       292132,       290195,       294007, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       306832,       292132,       277841,       306832,       292132,       277841,       306832,       292132,       277841, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2555421574), # 2.56GB, avg file size 365.06MB
  ("fsize_db",                        15994431220), # 15.99GB, avg file size 799.72MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_4v"),
  ("nof_files",                       7),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       292000, ],
    'CountWeighted'                                              : [       291971,       291970,       291976, ],
    'CountWeightedLHEWeightScale'                                : [       309295,       291969,       275676,       309295,       291969,       275676,       309295,       291969,       275676, ],
    'CountWeightedL1PrefireNom'                                  : [       283680,       283659,       283702, ],
    'CountWeightedL1Prefire'                                     : [       283680,       281672,       285636, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       300457,       283678,       267896,       300457,       283678,       267896,       300457,       283678,       267896, ],
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     2550732905), # 2.55GB, avg file size 364.39MB
  ("fsize_db",                        15872838181), # 15.87GB, avg file size 755.85MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_4v"),
  ("nof_files",                       6),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       299958,       299968,       299989, ],
    'CountWeightedLHEWeightScale'                                : [       320065,       299958,       281478,       320065,       299958,       281478,       320065,       299958,       281478, ],
    'CountWeightedL1PrefireNom'                                  : [       290811,       290806,       290835, ],
    'CountWeightedL1Prefire'                                     : [       290811,       288620,       292950, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       310236,       290811,       272938,       310236,       290811,       272938,       310236,       290811,       272938, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     2674509502), # 2.67GB, avg file size 445.75MB
  ("fsize_db",                        16481520657), # 16.48GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_4v"),
  ("nof_files",                       6),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299957,       299949,       299962, ],
    'CountWeightedLHEWeightScale'                                : [       322093,       299957,       279887,       322093,       299957,       279887,       322093,       299957,       279887, ],
    'CountWeightedL1PrefireNom'                                  : [       290185,       290168,       290197, ],
    'CountWeightedL1Prefire'                                     : [       290185,       287871,       292453, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       311530,       290185,       270821,       311530,       290185,       270821,       311530,       290185,       270821, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     2726573826), # 2.73GB, avg file size 454.43MB
  ("fsize_db",                        16709110067), # 16.71GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       195999, ],
    'CountWeighted'                                              : [       195981,       195953,       195989, ],
    'CountWeightedLHEWeightScale'                                : [       211632,       195981,       181949,       211632,       195981,       181949,       211632,       195981,       181949, ],
    'CountWeightedL1PrefireNom'                                  : [       189364,       189351,       189368, ],
    'CountWeightedL1Prefire'                                     : [       189364,       187808,       190891, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       204443,       189364,       175841,       204443,       189364,       175841,       204443,       189364,       175841, ],
  }),
  ("nof_tree_events",                 195999),
  ("nof_db_events",                   195999),
  ("fsize_local",                     1801022476), # 1.80GB, avg file size 450.26MB
  ("fsize_db",                        11098413315), # 11.10GB, avg file size 1.11GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       199999, ],
    'CountWeighted'                                              : [       199973,       199972,       199981, ],
    'CountWeightedLHEWeightScale'                                : [       217043,       199973,       184820,       217043,       199973,       184820,       217043,       199973,       184820, ],
    'CountWeightedL1PrefireNom'                                  : [       192906,       192891,       192932, ],
    'CountWeightedL1Prefire'                                     : [       192906,       191259,       194526, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       209326,       192906,       178325,       209326,       192906,       178325,       209326,       192906,       178325, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1851868729), # 1.85GB, avg file size 462.97MB
  ("fsize_db",                        11471924888), # 11.47GB, avg file size 819.42MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199994,       199976,       199958, ],
    'CountWeightedLHEWeightScale'                                : [       218045,       199994,       184068,       218045,       199994,       184068,       218045,       199994,       184068, ],
    'CountWeightedL1PrefireNom'                                  : [       192910,       192893,       192889, ],
    'CountWeightedL1Prefire'                                     : [       192910,       191262,       194531, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       210281,       192910,       177589,       210281,       192910,       177589,       210281,       192910,       177589, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1860457487), # 1.86GB, avg file size 465.11MB
  ("fsize_db",                        11589915708), # 11.59GB, avg file size 772.66MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       192000, ],
    'CountWeighted'                                              : [       191991,       191987,       191986, ],
    'CountWeightedL1PrefireNom'                                  : [       184952,       184938,       184961, ],
    'CountWeightedL1Prefire'                                     : [       184952,       183324,       186557, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     1798561928), # 1.80GB, avg file size 449.64MB
  ("fsize_db",                        11585622017), # 11.59GB, avg file size 965.47MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                      : [       199997, ],
    'CountWeighted'                                              : [       199992,       199961,       199956, ],
    'CountWeightedL1PrefireNom'                                  : [       192562,       192522,       192558, ],
    'CountWeightedL1Prefire'                                     : [       192562,       190847,       194252, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1875012096), # 1.88GB, avg file size 468.75MB
  ("fsize_db",                        12059647437), # 12.06GB, avg file size 1.51GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_4v"),
  ("nof_files",                       5),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       199999, ],
    'CountWeighted'                                              : [       199961,       199983,       199979, ],
    'CountWeightedL1PrefireNom'                                  : [       192339,       192342,       192361, ],
    'CountWeightedL1Prefire'                                     : [       192339,       190590,       194066, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1874512267), # 1.87GB, avg file size 374.90MB
  ("fsize_db",                        12157898020), # 12.16GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199949,       199944,       199952, ],
    'CountWeightedLHEWeightScale'                                : [       221302,       199949,       181636,       221302,       199949,       181636,       221302,       199949,       181636, ],
    'CountWeightedL1PrefireNom'                                  : [       192258,       192238,       192283, ],
    'CountWeightedL1Prefire'                                     : [       192258,       190497,       194000, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       212740,       192258,       174681,       212740,       192258,       174681,       212740,       192258,       174681, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1866050455), # 1.87GB, avg file size 466.51MB
  ("fsize_db",                        11885543228), # 11.89GB, avg file size 742.85MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_4v"),
  ("nof_files",                       3),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [        99999, ],
    'CountWeighted'                                              : [        99977,        99982,        99976, ],
    'CountWeightedLHEWeightScale'                                : [       111340,        99974,        90328,       111340,        99974,        90328,       111340,        99974,        90328, ],
    'CountWeightedL1PrefireNom'                                  : [        95947,        95947,        95945, ],
    'CountWeightedL1Prefire'                                     : [        95947,        95033,        96851, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106827,        95945,        86704,       106827,        95945,        86704,       106827,        95945,        86704, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     929947052), # 929.95MB, avg file size 309.98MB
  ("fsize_db",                        5933581710), # 5.93GB, avg file size 988.93MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_4v"),
  ("nof_files",                       9),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       399996, ],
    'CountWeighted'                                              : [       399997,       399963,       399975, ],
    'CountWeightedLHEWeightScale'                                : [       404911,       399997,       392234,       404911,       399997,       392234,       404911,       399997,       392234, ],
    'CountWeightedL1PrefireNom'                                  : [       393154,       393106,       393165, ],
    'CountWeightedL1Prefire'                                     : [       393154,       391352,       394846, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       397954,       393154,       385554,       397954,       393154,       385554,       397954,       393154,       385554, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     2962372902), # 2.96GB, avg file size 329.15MB
  ("fsize_db",                        20066660592), # 20.07GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_4v"),
  ("nof_files",                       8),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       399997, ],
    'CountWeighted'                                              : [       399997,       400015,       399955, ],
    'CountWeightedLHEWeightScale'                                : [       406222,       399995,       391168,       406222,       399995,       391168,       406222,       399995,       391168, ],
    'CountWeightedL1PrefireNom'                                  : [       392829,       392824,       392822, ],
    'CountWeightedL1Prefire'                                     : [       392829,       390954,       394599, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       398916,       392827,       384195,       398916,       392827,       384195,       398916,       392827,       384195, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     3015266052), # 3.02GB, avg file size 376.91MB
  ("fsize_db",                        19879949428), # 19.88GB, avg file size 994.00MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_4v"),
  ("nof_files",                       8),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399986,       399990,       399997, ],
    'CountWeightedLHEWeightScale'                                : [       407516,       399986,       390157,       407516,       399986,       390157,       407516,       399986,       390157, ],
    'CountWeightedL1PrefireNom'                                  : [       392587,       392569,       392615, ],
    'CountWeightedL1Prefire'                                     : [       392587,       390658,       394409, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       399939,       392587,       382972,       399939,       392587,       382972,       399939,       392587,       382972, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     3065361427), # 3.07GB, avg file size 383.17MB
  ("fsize_db",                        20200851289), # 20.20GB, avg file size 961.95MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_4v"),
  ("nof_files",                       9),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       391999, ],
    'CountWeighted'                                              : [       391949,       391948,       391970, ],
    'CountWeightedLHEWeightScale'                                : [       400543,       391949,       381386,       400543,       391949,       381386,       400543,       391949,       381386, ],
    'CountWeightedL1PrefireNom'                                  : [       384308,       384295,       384321, ],
    'CountWeightedL1Prefire'                                     : [       384308,       382334,       386180, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       392684,       384308,       373980,       392684,       384308,       373980,       392684,       384308,       373980, ],
  }),
  ("nof_tree_events",                 391999),
  ("nof_db_events",                   391999),
  ("fsize_local",                     3048827165), # 3.05GB, avg file size 338.76MB
  ("fsize_db",                        19893233798), # 19.89GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_4v"),
  ("nof_files",                       8),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       383998, ],
    'CountWeighted'                                              : [       383976,       383954,       383986, ],
    'CountWeightedLHEWeightScale'                                : [       394542,       383976,       371873,       394542,       383976,       371873,       394542,       383976,       371873, ],
    'CountWeightedL1PrefireNom'                                  : [       375960,       375928,       375989, ],
    'CountWeightedL1Prefire'                                     : [       375960,       373916,       377909, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       386261,       375960,       364152,       386261,       375960,       364152,       386261,       375960,       364152, ],
  }),
  ("nof_tree_events",                 383998),
  ("nof_db_events",                   383998),
  ("fsize_local",                     3068007996), # 3.07GB, avg file size 383.50MB
  ("fsize_db",                        19708482041), # 19.71GB, avg file size 985.42MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_4v"),
  ("nof_files",                       6),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299978,       299973,       299961, ],
    'CountWeightedLHEWeightScale'                                : [       309817,       299978,       289292,       309817,       299978,       289292,       309817,       299978,       289292, ],
    'CountWeightedL1PrefireNom'                                  : [       293359,       293343,       293362, ],
    'CountWeightedL1Prefire'                                     : [       293359,       291690,       294959, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       302937,       293359,       282943,       302937,       293359,       282943,       302937,       293359,       282943, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2450357382), # 2.45GB, avg file size 408.39MB
  ("fsize_db",                        15656023835), # 15.66GB, avg file size 1.20GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_4v"),
  ("nof_files",                       7),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299941,       299994,       299978, ],
    'CountWeightedLHEWeightScale'                                : [       311994,       299941,       287634,       311994,       299941,       287634,       311994,       299941,       287634, ],
    'CountWeightedL1PrefireNom'                                  : [       292806,       292831,       292836, ],
    'CountWeightedL1Prefire'                                     : [       292806,       291032,       294519, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       304505,       292806,       280818,       304505,       292806,       280818,       304505,       292806,       280818, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     2528526168), # 2.53GB, avg file size 361.22MB
  ("fsize_db",                        16009029568), # 16.01GB, avg file size 1.33GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_4v"),
  ("nof_files",                       6),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299956,       299972,       299968, ],
    'CountWeightedLHEWeightScale'                                : [       315108,       299956,       285269,       315108,       299956,       285269,       315108,       299956,       285269, ],
    'CountWeightedL1PrefireNom'                                  : [       292122,       292119,       292137, ],
    'CountWeightedL1Prefire'                                     : [       292122,       290217,       293973, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       306812,       292122,       277860,       306812,       292122,       277860,       306812,       292122,       277860, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     2621283379), # 2.62GB, avg file size 436.88MB
  ("fsize_db",                        16480100060), # 16.48GB, avg file size 915.56MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_4v"),
  ("nof_files",                       6),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       287998, ],
    'CountWeighted'                                              : [       287940,       287977,       287936, ],
    'CountWeightedLHEWeightScale'                                : [       305053,       287940,       271900,       305053,       287940,       271900,       305053,       287940,       271900, ],
    'CountWeightedL1PrefireNom'                                  : [       279949,       279964,       279951, ],
    'CountWeightedL1Prefire'                                     : [       279949,       278041,       281817, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       296514,       279949,       264402,       296514,       279949,       264402,       296514,       279949,       264402, ],
  }),
  ("nof_tree_events",                 287998),
  ("nof_db_events",                   287998),
  ("fsize_local",                     2586580507), # 2.59GB, avg file size 431.10MB
  ("fsize_db",                        16214133807), # 16.21GB, avg file size 953.77MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_4v"),
  ("nof_files",                       6),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       299951,       299981,       299980, ],
    'CountWeightedLHEWeightScale'                                : [       320064,       299951,       281475,       320064,       299951,       281475,       320064,       299951,       281475, ],
    'CountWeightedL1PrefireNom'                                  : [       291318,       291325,       291363, ],
    'CountWeightedL1Prefire'                                     : [       291318,       289282,       293318, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       310776,       291318,       273422,       310776,       291318,       273422,       310776,       291318,       273422, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     2749299627), # 2.75GB, avg file size 458.22MB
  ("fsize_db",                        17053053622), # 17.05GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_4v"),
  ("nof_files",                       6),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299993,       299968,       299975, ],
    'CountWeightedLHEWeightScale'                                : [       322106,       299993,       279897,       322106,       299993,       279897,       322106,       299993,       279897, ],
    'CountWeightedL1PrefireNom'                                  : [       291155,       291121,       291155, ],
    'CountWeightedL1Prefire'                                     : [       291155,       289090,       293184, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       312549,       291155,       271713,       312549,       291155,       271713,       312549,       291155,       271713, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     2789556043), # 2.79GB, avg file size 464.93MB
  ("fsize_db",                        17210955077), # 17.21GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       191998, ],
    'CountWeighted'                                              : [       192001,       192005,       191986, ],
    'CountWeightedLHEWeightScale'                                : [       207318,       192001,       178241,       207318,       192001,       178241,       207318,       192001,       178241, ],
    'CountWeightedL1PrefireNom'                                  : [       186308,       186296,       186316, ],
    'CountWeightedL1Prefire'                                     : [       186308,       184986,       187609, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       201127,       186308,       172997,       201127,       186308,       172997,       201127,       186308,       172997, ],
  }),
  ("nof_tree_events",                 191998),
  ("nof_db_events",                   191998),
  ("fsize_local",                     1798888809), # 1.80GB, avg file size 449.72MB
  ("fsize_db",                        11180869047), # 11.18GB, avg file size 860.07MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199995,       200001,       199992, ],
    'CountWeightedLHEWeightScale'                                : [       217076,       199994,       184846,       217076,       199994,       184846,       217076,       199994,       184846, ],
    'CountWeightedL1PrefireNom'                                  : [       193961,       193957,       193959, ],
    'CountWeightedL1Prefire'                                     : [       193961,       192568,       195333, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       210475,       193960,       179305,       210475,       193960,       179305,       210475,       193960,       179305, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1882548439), # 1.88GB, avg file size 470.64MB
  ("fsize_db",                        11726047160), # 11.73GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_4v"),
  ("nof_files",                       5),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       191999, ],
    'CountWeighted'                                              : [       191978,       191998,       191994, ],
    'CountWeightedLHEWeightScale'                                : [       209346,       191977,       176728,       209346,       191977,       176728,       209346,       191977,       176728, ],
    'CountWeightedL1PrefireNom'                                  : [       186281,       186286,       186294, ],
    'CountWeightedL1Prefire'                                     : [       186281,       184967,       187577, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       203082,       186280,       171510,       203082,       186280,       171510,       203082,       186280,       171510, ],
  }),
  ("nof_tree_events",                 191999),
  ("nof_db_events",                   191999),
  ("fsize_local",                     1809530657), # 1.81GB, avg file size 361.91MB
  ("fsize_db",                        11310227020), # 11.31GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       199997, ],
    'CountWeighted'                                              : [       199972,       199979,       199975, ],
    'CountWeightedLHEWeightScale'                                : [       218944,       199972,       183367,       218944,       199972,       183367,       218944,       199972,       183367, ],
    'CountWeightedL1PrefireNom'                                  : [       193976,       193971,       193991, ],
    'CountWeightedL1Prefire'                                     : [       193976,       192599,       195332, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       212338,       193976,       177906,       212338,       193976,       177906,       212338,       193976,       177906, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1882779355), # 1.88GB, avg file size 470.69MB
  ("fsize_db",                        11817475227), # 11.82GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_4v"),
  ("nof_files",                       5),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       199998, ],
    'CountWeighted'                                              : [       199962,       199943,       199951, ],
    'CountWeightedLHEWeightScale'                                : [       219780,       199961,       182741,       219780,       199961,       182741,       219780,       199961,       182741, ],
    'CountWeightedL1PrefireNom'                                  : [       193989,       193963,       193991, ],
    'CountWeightedL1Prefire'                                     : [       193989,       192622,       195336, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       213176,       193988,       177311,       213176,       193988,       177311,       213176,       193988,       177311, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1879213168), # 1.88GB, avg file size 375.84MB
  ("fsize_db",                        11932391412), # 11.93GB, avg file size 701.91MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       199999, ],
    'CountWeighted'                                              : [       199967,       199968,       199980, ],
    'CountWeightedL1PrefireNom'                                  : [       194053,       194042,       194075, ],
    'CountWeightedL1Prefire'                                     : [       194053,       192699,       195386, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1879334021), # 1.88GB, avg file size 469.83MB
  ("fsize_db",                        12455825050), # 12.46GB, avg file size 958.14MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_4v"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                      : [        99998, ],
    'CountWeighted'                                              : [       100003,        99993,       100000, ],
    'CountWeightedLHEWeightScale'                                : [       110555,       100003,        90980,       110555,       100003,        90980,       110555,       100003,        90980, ],
    'CountWeightedL1PrefireNom'                                  : [        97135,        97129,        97134, ],
    'CountWeightedL1Prefire'                                     : [        97135,        96478,        97783, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107368,        97135,        88384,       107368,        97135,        88384,       107368,        97135,        88384, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     933798311), # 933.80MB, avg file size 466.90MB
  ("fsize_db",                        6157522996), # 6.16GB, avg file size 769.69MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_4v"),
  ("nof_files",                       3),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                      : [        99999, ],
    'CountWeighted'                                              : [        99979,        99980,        99979, ],
    'CountWeightedLHEWeightScale'                                : [       111345,        99979,        90329,       111345,        99979,        90329,       111345,        99979,        90329, ],
    'CountWeightedL1PrefireNom'                                  : [        97038,        97038,        97033, ],
    'CountWeightedL1Prefire'                                     : [        97038,        96368,        97698, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       108055,        97038,        87683,       108055,        97038,        87683,       108055,        97038,        87683, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     925325980), # 925.33MB, avg file size 308.44MB
  ("fsize_db",                        6189551070), # 6.19GB, avg file size 773.69MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_4v"),
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

samples_2017["/VBFHHTo4Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                      : [       384000, ],
    'CountWeighted'                                              : [       380250,       380282,       380239, ],
    'CountWeightedL1PrefireNom'                                  : [       354418,       354423,       354413, ],
    'CountWeightedL1Prefire'                                     : [       354418,       348447,       360355, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     3208310695), # 3.21GB, avg file size 401.04MB
  ("fsize_db",                        20516924301), # 20.52GB, avg file size 892.04MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_1_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399985,       399982,       399964, ],
    'CountWeightedLHEWeightScale'                                : [       511986,       483252,       456284,       423841,       399985,       377569,       356939,       336765,       317859, ],
    'CountWeightedL1PrefireNom'                                  : [       387197,       387161,       387217, ],
    'CountWeightedL1Prefire'                                     : [       387197,       384172,       390171, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       495492,       467831,       441846,       410168,       387197,       365605,       345411,       325992,       307776, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     3199121446), # 3.20GB, avg file size 399.89MB
  ("fsize_db",                        20766449398), # 20.77GB, avg file size 1.38GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       388000, ],
    'CountWeighted'                                              : [       387921,       387954,       387904, ],
    'CountWeightedLHEWeightScale'                                : [       504099,       464429,       429585,       421287,       387914,       358649,       357632,       329163,       304205, ],
    'CountWeightedL1PrefireNom'                                  : [       374145,       374139,       374157, ],
    'CountWeightedL1Prefire'                                     : [       374145,       370959,       377290, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       486034,       447973,       414515,       406152,       374140,       346037,       344761,       317449,       293485, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     3286401225), # 3.29GB, avg file size 410.80MB
  ("fsize_db",                        21137556590), # 21.14GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_4t"),
  ("nof_files",                       9),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399970,       399934,       399974, ],
    'CountWeightedLHEWeightScale'                                : [       512031,       483190,       456120,       423906,       399969,       377492,       357006,       336788,       317831, ],
    'CountWeightedL1PrefireNom'                                  : [       387093,       387046,       387108, ],
    'CountWeightedL1Prefire'                                     : [       387093,       384051,       390084, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       495416,       467653,       441568,       410135,       387091,       365436,       345398,       325937,       307671, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     3205550105), # 3.21GB, avg file size 356.17MB
  ("fsize_db",                        20758947388), # 20.76GB, avg file size 902.56MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       374000, ],
    'CountWeighted'                                              : [       374021,       373960,       373961, ],
    'CountWeightedLHEWeightScale'                                : [       476967,       452859,       429703,       393923,       374021,       354811,       331091,       314288,       298162, ],
    'CountWeightedL1PrefireNom'                                  : [       362305,       362237,       362299, ],
    'CountWeightedL1Prefire'                                     : [       362305,       359524,       365033, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       461933,       438705,       416370,       381498,       362305,       343793,       320640,       304451,       288897, ],
  }),
  ("nof_tree_events",                 374000),
  ("nof_db_events",                   374000),
  ("fsize_local",                     2943779304), # 2.94GB, avg file size 367.97MB
  ("fsize_db",                        19521414949), # 19.52GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_4t"),
  ("nof_files",                       9),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399958,       399954,       399940, ],
    'CountWeightedLHEWeightScale'                                : [       519455,       478870,       443032,       433967,       399958,       369927,       368248,       339305,       313771, ],
    'CountWeightedL1PrefireNom'                                  : [       385702,       385667,       385727, ],
    'CountWeightedL1Prefire'                                     : [       385702,       382409,       388956, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       500800,       461827,       427388,       418362,       385702,       356848,       354993,       327200,       302665, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     3397021150), # 3.40GB, avg file size 377.45MB
  ("fsize_db",                        21901746830), # 21.90GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       396000, ],
    'CountWeighted'                                              : [       395997,       395949,       395966, ],
    'CountWeightedLHEWeightScale'                                : [       504842,       479593,       455277,       416861,       395997,       375849,       350308,       332712,       315788, ],
    'CountWeightedL1PrefireNom'                                  : [       383687,       383640,       383691, ],
    'CountWeightedL1Prefire'                                     : [       383687,       380763,       386562, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       489048,       464712,       441255,       403809,       383687,       364264,       339332,       322375,       306047, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     3113045111), # 3.11GB, avg file size 389.13MB
  ("fsize_db",                        20180485758), # 20.18GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2v2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       399996, ],
    'CountWeighted'                                              : [       399944,       399993,       399994, ],
    'CountWeightedLHEWeightScale'                                : [       512033,       483269,       456282,       423883,       399942,       377570,       356978,       336780,       317863, ],
    'CountWeightedL1PrefireNom'                                  : [       387730,       387753,       387770, ],
    'CountWeightedL1Prefire'                                     : [       387730,       384815,       390584, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       496245,       468519,       442479,       410793,       387727,       366131,       345939,       326473,       308220, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     3355770571), # 3.36GB, avg file size 372.86MB
  ("fsize_db",                        21713327567), # 21.71GB, avg file size 1.45GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2v2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       369992, ],
    'CountWeighted'                                              : [       369950,       369953,       369898, ],
    'CountWeightedLHEWeightScale'                                : [       480695,       442942,       409765,       401696,       369950,       342076,       340984,       313890,       290128, ],
    'CountWeightedL1PrefireNom'                                  : [       357221,       357209,       357201, ],
    'CountWeightedL1Prefire'                                     : [       357221,       354264,       360131, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       463986,       427746,       395869,       387693,       357221,       330442,       329069,       303064,       280237, ],
  }),
  ("nof_tree_events",                 369992),
  ("nof_db_events",                   369992),
  ("fsize_local",                     3236993415), # 3.24GB, avg file size 404.62MB
  ("fsize_db",                        20666744125), # 20.67GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2v2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       392996, ],
    'CountWeighted'                                              : [       392968,       392952,       392983, ],
    'CountWeightedLHEWeightScale'                                : [       503068,       474746,       448161,       416479,       392968,       370899,       350747,       330893,       312276, ],
    'CountWeightedL1PrefireNom'                                  : [       380993,       380985,       381002, ],
    'CountWeightedL1Prefire'                                     : [       380993,       378135,       383790, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       487613,       460301,       434636,       403668,       380993,       359691,       339947,       320800,       302829, ],
  }),
  ("nof_tree_events",                 392996),
  ("nof_db_events",                   392996),
  ("fsize_local",                     3305891447), # 3.31GB, avg file size 413.24MB
  ("fsize_db",                        20864139002), # 20.86GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_4_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2v2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       375989, ],
    'CountWeighted'                                              : [       375962,       375959,       375933, ],
    'CountWeightedLHEWeightScale'                                : [       479433,       455310,       432111,       395942,       375962,       356760,       332773,       315942,       299778, ],
    'CountWeightedL1PrefireNom'                                  : [       365015,       364981,       365022, ],
    'CountWeightedL1Prefire'                                     : [       365015,       362378,       367587, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       465360,       442066,       419643,       384306,       365015,       346456,       322983,       306733,       291110, ],
  }),
  ("nof_tree_events",                 375989),
  ("nof_db_events",                   375989),
  ("fsize_local",                     3109564569), # 3.11GB, avg file size 345.51MB
  ("fsize_db",                        19916065120), # 19.92GB, avg file size 1.53GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_5_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2v2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       399994, ],
    'CountWeighted'                                              : [       399950,       399956,       399872, ],
    'CountWeightedLHEWeightScale'                                : [       512966,       482651,       454503,       425164,       399950,       376549,       358412,       337088,       317315, ],
    'CountWeightedL1PrefireNom'                                  : [       387551,       387529,       387525, ],
    'CountWeightedL1Prefire'                                     : [       387551,       384600,       390439, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       496928,       467711,       440554,       411850,       387551,       364975,       347174,       326624,       307550, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     3382830853), # 3.38GB, avg file size 422.85MB
  ("fsize_db",                        21844664310), # 21.84GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_6_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_2v2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       399992, ],
    'CountWeighted'                                              : [       399954,       399914,       399948, ],
    'CountWeightedLHEWeightScale'                                : [       510242,       484214,       459261,       421489,       399954,       379294,       354314,       336171,       318787, ],
    'CountWeightedL1PrefireNom'                                  : [       388279,       388229,       388297, ],
    'CountWeightedL1Prefire'                                     : [       388279,       385471,       391023, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       495239,       470099,       445974,       409084,       388279,       368310,       343877,       326354,       309548, ],
  }),
  ("nof_tree_events",                 399992),
  ("nof_db_events",                   399992),
  ("fsize_local",                     3314229145), # 3.31GB, avg file size 368.25MB
  ("fsize_db",                        21124650657), # 21.12GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2v2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       384992, ],
    'CountWeighted'                                              : [       384965,       384960,       384969, ],
    'CountWeightedLHEWeightScale'                                : [       490977,       466175,       442348,       405491,       384965,       365249,       340809,       323524,       306931, ],
    'CountWeightedL1PrefireNom'                                  : [       373717,       373681,       373749, ],
    'CountWeightedL1Prefire'                                     : [       373717,       371012,       376357, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       476522,       452568,       429531,       393542,       373717,       354656,       330758,       314063,       298023, ],
  }),
  ("nof_tree_events",                 384992),
  ("nof_db_events",                   384992),
  ("fsize_local",                     3185473486), # 3.19GB, avg file size 353.94MB
  ("fsize_db",                        20503345442), # 20.50GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_8_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2v2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       399997, ],
    'CountWeighted'                                              : [       399950,       399987,       399946, ],
    'CountWeightedLHEWeightScale'                                : [       509947,       484419,       459844,       421084,       399950,       379627,       353865,       336074,       318965, ],
    'CountWeightedL1PrefireNom'                                  : [       388366,       388391,       388358, ],
    'CountWeightedL1Prefire'                                     : [       388366,       385576,       391090, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       495059,       470400,       446637,       408777,       388366,       368713,       343514,       326329,       309787, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     3307125095), # 3.31GB, avg file size 367.46MB
  ("fsize_db",                        21039976306), # 21.04GB, avg file size 1.00GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2v2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       399991, ],
    'CountWeighted'                                              : [       399940,       399970,       399986, ],
    'CountWeightedLHEWeightScale'                                : [       519440,       478872,       443046,       433952,       399940,       369937,       368235,       339302,       313776, ],
    'CountWeightedL1PrefireNom'                                  : [       386001,       385993,       386051, ],
    'CountWeightedL1Prefire'                                     : [       386001,       382764,       389191, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       501184,       462201,       427751,       418678,       386001,       357147,       355259,       327459,       302915, ],
  }),
  ("nof_tree_events",                 399991),
  ("nof_db_events",                   399991),
  ("fsize_local",                     3543743584), # 3.54GB, avg file size 442.97MB
  ("fsize_db",                        22600644898), # 22.60GB, avg file size 1.88GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_10_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2v2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       399986, ],
    'CountWeighted'                                              : [       399979,       399960,       399955, ],
    'CountWeightedLHEWeightScale'                                : [       510083,       484311,       459551,       421277,       399979,       379459,       354083,       336117,       318873, ],
    'CountWeightedL1PrefireNom'                                  : [       388376,       388350,       388374, ],
    'CountWeightedL1Prefire'                                     : [       388376,       385587,       391103, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       495191,       470293,       446350,       408966,       388376,       368548,       343727,       326372,       309697, ],
  }),
  ("nof_tree_events",                 399986),
  ("nof_db_events",                   399986),
  ("fsize_local",                     3310768322), # 3.31GB, avg file size 367.86MB
  ("fsize_db",                        21181482185), # 21.18GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_11_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2v2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       395994, ],
    'CountWeighted'                                              : [       395958,       395945,       395950, ],
    'CountWeightedLHEWeightScale'                                : [       505348,       479279,       454341,       417548,       395956,       375322,       351068,       332888,       315510, ],
    'CountWeightedL1PrefireNom'                                  : [       384262,       384237,       384287, ],
    'CountWeightedL1Prefire'                                     : [       384262,       381454,       387007, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       490311,       465137,       441033,       405111,       384260,       364318,       340604,       323049,       306253, ],
  }),
  ("nof_tree_events",                 395994),
  ("nof_db_events",                   395994),
  ("fsize_local",                     3287087652), # 3.29GB, avg file size 410.89MB
  ("fsize_db",                        21005832838), # 21.01GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2v2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       399993, ],
    'CountWeighted'                                              : [       399956,       399940,       399958, ],
    'CountWeightedLHEWeightScale'                                : [       509960,       484403,       459809,       421100,       399956,       379602,       353882,       336073,       318948, ],
    'CountWeightedL1PrefireNom'                                  : [       388364,       388324,       388394, ],
    'CountWeightedL1Prefire'                                     : [       388364,       385570,       391090, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       495065,       470380,       446599,       408788,       388364,       368686,       343526,       326325,       309769, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     3306843995), # 3.31GB, avg file size 367.43MB
  ("fsize_db",                        21048263593), # 21.05GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_2v2t"),
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

samples_2017["/GluGluToHHTo4V_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_4v"),
  ("nof_files",                       9),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       379997, ],
    'CountWeighted'                                              : [       379953,       380002,       379976, ],
    'CountWeightedLHEWeightScale'                                : [       486416,       459084,       433446,       402677,       379951,       358675,       339121,       319930,       301957, ],
    'CountWeightedL1PrefireNom'                                  : [       368957,       368961,       369009, ],
    'CountWeightedL1Prefire'                                     : [       368957,       366306,       371539, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       472207,       445820,       421041,       390891,       368955,       348390,       329178,       310654,       293285, ],
  }),
  ("nof_tree_events",                 379997),
  ("nof_db_events",                   379997),
  ("fsize_local",                     3309694140), # 3.31GB, avg file size 367.74MB
  ("fsize_db",                        20701310914), # 20.70GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_4v"),
  ("nof_files",                       9),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       399999, ],
    'CountWeighted'                                              : [       399922,       399913,       399958, ],
    'CountWeightedLHEWeightScale'                                : [       519674,       478788,       442874,       434296,       399922,       369737,       368674,       339330,       313605, ],
    'CountWeightedL1PrefireNom'                                  : [       386434,       386429,       386457, ],
    'CountWeightedL1Prefire'                                     : [       386434,       383294,       389519, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       501963,       462702,       428179,       419443,       386434,       357426,       356030,       327857,       303133, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     3576228403), # 3.58GB, avg file size 397.36MB
  ("fsize_db",                        23052019817), # 23.05GB, avg file size 1.54GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_4v"),
  ("nof_files",                       8),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                      : [       382999, ],
    'CountWeighted'                                              : [       382970,       382971,       382963, ],
    'CountWeightedLHEWeightScale'                                : [       490278,       462662,       436737,       405895,       382970,       361449,       341840,       322481,       304325, ],
    'CountWeightedL1PrefireNom'                                  : [       371814,       371799,       371827, ],
    'CountWeightedL1Prefire'                                     : [       371814,       369128,       374430, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       475877,       449207,       424146,       393955,       371814,       351013,       331770,       313076,       295526, ],
  }),
  ("nof_tree_events",                 382999),
  ("nof_db_events",                   382999),
  ("fsize_local",                     3348252118), # 3.35GB, avg file size 418.53MB
  ("fsize_db",                        20935006290), # 20.94GB, avg file size 951.59MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_4_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_4v"),
  ("nof_files",                       8),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                      : [       391999, ],
    'CountWeighted'                                              : [       391979,       391969,       391950, ],
    'CountWeightedLHEWeightScale'                                : [       499829,       474723,       450576,       412768,       391979,       371997,       346909,       329394,       312571, ],
    'CountWeightedL1PrefireNom'                                  : [       381293,       381270,       381290, ],
    'CountWeightedL1Prefire'                                     : [       381293,       378688,       383818, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       486090,       461795,       438405,       401407,       381293,       361936,       337349,       320403,       304108, ],
  }),
  ("nof_tree_events",                 391999),
  ("nof_db_events",                   391999),
  ("fsize_local",                     3375723523), # 3.38GB, avg file size 421.97MB
  ("fsize_db",                        21344876204), # 21.34GB, avg file size 970.22MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_5_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_4v"),
  ("nof_files",                       9),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       399999, ],
    'CountWeighted'                                              : [       399948,       399911,       399994, ],
    'CountWeightedLHEWeightScale'                                : [       512973,       482650,       454497,       425173,       399948,       376548,       358426,       337101,       317319, ],
    'CountWeightedL1PrefireNom'                                  : [       388006,       387945,       388074, ],
    'CountWeightedL1Prefire'                                     : [       388006,       385139,       390797, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       497516,       468261,       441069,       412340,       388006,       365404,       347589,       327016,       307914, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     3509102163), # 3.51GB, avg file size 389.90MB
  ("fsize_db",                        22416145291), # 22.42GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_6_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_4v"),
  ("nof_files",                       10),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       396000, ],
    'CountWeighted'                                              : [       395991,       395995,       395980, ],
    'CountWeightedLHEWeightScale'                                : [       505187,       479416,       454703,       417313,       395982,       375531,       350803,       332839,       315623, ],
    'CountWeightedL1PrefireNom'                                  : [       385008,       385010,       385008, ],
    'CountWeightedL1Prefire'                                     : [       385008,       382339,       387600, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       491075,       466138,       442205,       405642,       385001,       365199,       340984,       323602,       306931, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     3426542113), # 3.43GB, avg file size 342.65MB
  ("fsize_db",                        21470016217), # 21.47GB, avg file size 1.34GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_4v"),
  ("nof_files",                       9),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399984,       399996,       399987, ],
    'CountWeightedLHEWeightScale'                                : [       510131,       484346,       459580,       421315,       399984,       379484,       354114,       336141,       318896, ],
    'CountWeightedL1PrefireNom'                                  : [       389021,       388998,       389046, ],
    'CountWeightedL1Prefire'                                     : [       389021,       386347,       391613, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       496044,       471088,       447095,       409668,       389021,       369164,       344315,       326923,       310216, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     3453155560), # 3.45GB, avg file size 383.68MB
  ("fsize_db",                        21847137342), # 21.85GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_8_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_4v"),
  ("nof_files",                       8),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       395995, ],
    'CountWeighted'                                              : [       395946,       395953,       395964, ],
    'CountWeightedLHEWeightScale'                                : [       504865,       479585,       455258,       416889,       395946,       375844,       350342,       332727,       315788, ],
    'CountWeightedL1PrefireNom'                                  : [       385200,       385187,       385227, ],
    'CountWeightedL1Prefire'                                     : [       385200,       382577,       387743, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       491040,       466576,       443005,       405461,       385200,       365717,       340729,       323680,       307270, ],
  }),
  ("nof_tree_events",                 395995),
  ("nof_db_events",                   395995),
  ("fsize_local",                     3412018718), # 3.41GB, avg file size 426.50MB
  ("fsize_db",                        21294763606), # 21.29GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_4v"),
  ("nof_files",                       9),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                      : [       399997, ],
    'CountWeighted'                                              : [       399912,       399927,       399886, ],
    'CountWeightedLHEWeightScale'                                : [       519406,       478833,       442999,       433934,       399912,       369904,       368225,       339285,       313754, ],
    'CountWeightedL1PrefireNom'                                  : [       386351,       386335,       386353, ],
    'CountWeightedL1Prefire'                                     : [       386351,       383183,       389462, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       501641,       462620,       428131,       419067,       386351,       357467,       355591,       327760,       303189, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     3647880856), # 3.65GB, avg file size 405.32MB
  ("fsize_db",                        23472759858), # 23.47GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_10_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_4v"),
  ("nof_files",                       10),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       391996, ],
    'CountWeighted'                                              : [       391961,       391942,       391973, ],
    'CountWeightedLHEWeightScale'                                : [       499936,       474647,       450353,       412904,       391954,       371868,       347049,       329418,       312501, ],
    'CountWeightedL1PrefireNom'                                  : [       381151,       381133,       381163, ],
    'CountWeightedL1Prefire'                                     : [       381151,       378522,       383703, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       486032,       461569,       438045,       401408,       381146,       361694,       337376,       320321,       303942, ],
  }),
  ("nof_tree_events",                 391996),
  ("nof_db_events",                   391996),
  ("fsize_local",                     3386605785), # 3.39GB, avg file size 338.66MB
  ("fsize_db",                        21244437020), # 21.24GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_11_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_4v"),
  ("nof_files",                       9),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       399997, ],
    'CountWeighted'                                              : [       399963,       399951,       399942, ],
    'CountWeightedLHEWeightScale'                                : [       510464,       484134,       458945,       421771,       399957,       379120,       354621,       336254,       318703, ],
    'CountWeightedL1PrefireNom'                                  : [       388899,       388873,       388899, ],
    'CountWeightedL1Prefire'                                     : [       388899,       386205,       391513, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       496229,       470751,       446355,       409997,       388894,       368711,       344711,       326941,       309944, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     3466891749), # 3.47GB, avg file size 385.21MB
  ("fsize_db",                        21689984880), # 21.69GB, avg file size 1.28GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_4v"),
  ("nof_files",                       9),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       394000, ],
    'CountWeighted'                                              : [       393955,       393953,       393947, ],
    'CountWeightedLHEWeightScale'                                : [       502315,       477180,       452976,       414774,       393955,       373951,       348557,       331042,       314192, ],
    'CountWeightedL1PrefireNom'                                  : [       383206,       383202,       383202, ],
    'CountWeightedL1Prefire'                                     : [       383206,       380579,       385751, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       488491,       464166,       440722,       403346,       383204,       363824,       338944,       321995,       305674, ],
  }),
  ("nof_tree_events",                 394000),
  ("nof_db_events",                   394000),
  ("fsize_local",                     3393871462), # 3.39GB, avg file size 377.10MB
  ("fsize_db",                        21086443719), # 21.09GB, avg file size 1.62GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Aug30_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4v"),
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

samples_2017["sum_events"] = [
  [ 'signal_ggf_nonresonant_node_sm_hh_4t',            'signal_ggf_nonresonant_node_2_hh_4t',             'signal_ggf_nonresonant_node_3_hh_4t',             'signal_ggf_nonresonant_node_7_hh_4t',             'signal_ggf_nonresonant_node_9_hh_4t',             'signal_ggf_nonresonant_node_12_hh_4t',             ],
  [ 'signal_ggf_nonresonant_node_sm_hh_4v',            'signal_ggf_nonresonant_node_2_hh_4v',             'signal_ggf_nonresonant_node_3_hh_4v',             'signal_ggf_nonresonant_node_4_hh_4v',             'signal_ggf_nonresonant_node_5_hh_4v',             'signal_ggf_nonresonant_node_6_hh_4v',             'signal_ggf_nonresonant_node_7_hh_4v',             'signal_ggf_nonresonant_node_8_hh_4v',             'signal_ggf_nonresonant_node_9_hh_4v',             'signal_ggf_nonresonant_node_10_hh_4v',            'signal_ggf_nonresonant_node_11_hh_4v',            'signal_ggf_nonresonant_node_12_hh_4v',             ],
  [ 'signal_ggf_nonresonant_node_sm_hh_2v2t',          'signal_ggf_nonresonant_node_2_hh_2v2t',           'signal_ggf_nonresonant_node_3_hh_2v2t',           'signal_ggf_nonresonant_node_4_hh_2v2t',           'signal_ggf_nonresonant_node_5_hh_2v2t',           'signal_ggf_nonresonant_node_6_hh_2v2t',           'signal_ggf_nonresonant_node_7_hh_2v2t',           'signal_ggf_nonresonant_node_8_hh_2v2t',           'signal_ggf_nonresonant_node_9_hh_2v2t',           'signal_ggf_nonresonant_node_10_hh_2v2t',          'signal_ggf_nonresonant_node_11_hh_2v2t',          'signal_ggf_nonresonant_node_12_hh_2v2t',           ],
]

