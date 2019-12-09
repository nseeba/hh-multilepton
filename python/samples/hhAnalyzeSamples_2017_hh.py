from collections import OrderedDict as OD

# file generated at 2019-12-09 14:05:49 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_hh.py -M

samples_2017 = OD()
samples_2017["/GluGluToRadionToHHTo4Tau_M-250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399957,       399954,       399928, ],
    'CountWeightedL1PrefireNom'                                  : [       391753,       391738,       391747, ],
    'CountWeightedL1Prefire'                                     : [       391753,       389637,       393799, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1256781690), # 1.26GB, avg file size 1.26GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399961,       399946,       399950, ],
    'CountWeightedLHEWeightScale'                                : [       406227,       399961,       391154,       406227,       399961,       391154,       406227,       399961,       391154, ],
    'CountWeightedL1PrefireNom'                                  : [       391467,       391444,       391481, ],
    'CountWeightedL1Prefire'                                     : [       391467,       389297,       393564, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       397545,       391467,       382896,       397545,       391467,       382896,       397545,       391467,       382896, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1256677472), # 1.26GB, avg file size 1.26GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       385000, ],
    'CountWeighted'                                              : [       384994,       385058,       384966, ],
    'CountWeightedLHEWeightScale'                                : [       392263,       384994,       375530,       392263,       384994,       375530,       392263,       384994,       375530, ],
    'CountWeightedL1PrefireNom'                                  : [       376402,       376429,       376391, ],
    'CountWeightedL1Prefire'                                     : [       376402,       374220,       378505, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       383449,       376402,       367199,       383449,       376402,       367199,       383449,       376402,       367199, ],
  }),
  ("nof_tree_events",                 385000),
  ("nof_db_events",                   385000),
  ("fsize_local",                     1221575051), # 1.22GB, avg file size 1.22GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       400002,       399927,       399923, ],
    'CountWeightedL1PrefireNom'                                  : [       390730,       390658,       390687, ],
    'CountWeightedL1Prefire'                                     : [       390730,       388400,       392990, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1291926340), # 1.29GB, avg file size 1.29GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300058,       299967,       300015, ],
    'CountWeightedLHEWeightScale'                                : [       308244,       300058,       290543,       308244,       300058,       290543,       308244,       300058,       290543, ],
    'CountWeightedL1PrefireNom'                                  : [       292679,       292604,       292668, ],
    'CountWeightedL1Prefire'                                     : [       292679,       290847,       294458, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       300636,       292679,       283460,       300636,       292679,       283460,       300636,       292679,       283460, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     977403005), # 977.40MB, avg file size 977.40MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       284000, ],
    'CountWeighted'                                              : [       283970,       283959,       283964, ],
    'CountWeightedLHEWeightScale'                                : [       295332,       283970,       272299,       295332,       283970,       272299,       295332,       283970,       272299, ],
    'CountWeightedL1PrefireNom'                                  : [       276080,       276070,       276078, ],
    'CountWeightedL1Prefire'                                     : [       276080,       274167,       277949, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       287069,       276080,       264774,       287069,       276080,       264774,       287069,       276080,       264774, ],
  }),
  ("nof_tree_events",                 284000),
  ("nof_db_events",                   284000),
  ("fsize_local",                     962710968), # 962.71MB, avg file size 962.71MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299956,       300034,       299898, ],
    'CountWeightedLHEWeightScale'                                : [       315120,       299931,       285260,       315120,       299931,       285260,       315120,       299931,       285260, ],
    'CountWeightedL1PrefireNom'                                  : [       291050,       291097,       291006, ],
    'CountWeightedL1Prefire'                                     : [       291050,       288914,       293144, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       305692,       291033,       276834,       305692,       291033,       276834,       305692,       291033,       276834, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1052838415), # 1.05GB, avg file size 1.05GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299869,       299991,       299934, ],
    'CountWeightedLHEWeightScale'                                : [       317757,       299869,       283231,       317757,       299869,       283231,       317757,       299869,       283231, ],
    'CountWeightedL1PrefireNom'                                  : [       290400,       290461,       290451, ],
    'CountWeightedL1Prefire'                                     : [       290400,       288157,       292608, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       307627,       290400,       274311,       307627,       290400,       274311,       307627,       290400,       274311, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1084562576), # 1.08GB, avg file size 1.08GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199976,       199985,       199952, ],
    'CountWeightedLHEWeightScale'                                : [       213411,       199976,       187663,       213411,       199976,       187663,       213411,       199976,       187663, ],
    'CountWeightedL1PrefireNom'                                  : [       193292,       193283,       193289, ],
    'CountWeightedL1Prefire'                                     : [       193292,       191721,       194838, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       206224,       193292,       181419,       206224,       193292,       181419,       206224,       193292,       181419, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     741890213), # 741.89MB, avg file size 741.89MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       200004,       199926,       199958, ],
    'CountWeightedLHEWeightScale'                                : [       214706,       200003,       186563,       214706,       200003,       186563,       214706,       200003,       186563, ],
    'CountWeightedL1PrefireNom'                                  : [       193006,       192957,       192971, ],
    'CountWeightedL1Prefire'                                     : [       193006,       191377,       194609, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       207166,       193004,       180086,       207166,       193004,       180086,       207166,       193004,       180086, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     759870531), # 759.87MB, avg file size 759.87MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199988,       199935,       200007, ],
    'CountWeightedLHEWeightScale'                                : [       215949,       199988,       185660,       215949,       199988,       185660,       215949,       199988,       185660, ],
    'CountWeightedL1PrefireNom'                                  : [       192779,       192745,       192801, ],
    'CountWeightedL1Prefire'                                     : [       192779,       191111,       194434, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       208127,       192779,       179011,       208127,       192779,       179011,       208127,       192779,       179011, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     775657846), # 775.66MB, avg file size 775.66MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199970,       199942,       199977, ],
    'CountWeightedLHEWeightScale'                                : [       217052,       199970,       184813,       217052,       199970,       184813,       217052,       199970,       184813, ],
    'CountWeightedL1PrefireNom'                                  : [       192693,       192676,       192697, ],
    'CountWeightedL1Prefire'                                     : [       192693,       191008,       194357, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       209106,       192693,       178123,       209106,       192693,       178123,       209106,       192693,       178123, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     790698518), # 790.70MB, avg file size 790.70MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199992,       199944,       199942, ],
    'CountWeightedLHEWeightScale'                                : [       218038,       199992,       184050,       218038,       199992,       184050,       218038,       199992,       184050, ],
    'CountWeightedL1PrefireNom'                                  : [       192485,       192429,       192479, ],
    'CountWeightedL1Prefire'                                     : [       192485,       190761,       194193, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       209814,       192485,       177188,       209814,       192485,       177188,       209814,       192485,       177188, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     805314239), # 805.31MB, avg file size 805.31MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199971,       199962,       199939, ],
    'CountWeightedL1PrefireNom'                                  : [       192280,       192263,       192260, ],
    'CountWeightedL1Prefire'                                     : [       192280,       190513,       194023, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     825535238), # 825.54MB, avg file size 825.54MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199964,       199952,       199987, ],
    'CountWeightedL1PrefireNom'                                  : [       192241,       192226,       192261, ],
    'CountWeightedL1Prefire'                                     : [       192241,       190470,       193990, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     836360662), # 836.36MB, avg file size 836.36MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       192000, ],
    'CountWeighted'                                              : [       191955,       191989,       191949, ],
    'CountWeightedL1PrefireNom'                                  : [       184440,       184463,       184429, ],
    'CountWeightedL1Prefire'                                     : [       184440,       182722,       186141, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     812721251), # 812.72MB, avg file size 812.72MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99984,        99995,       100000, ],
    'CountWeightedLHEWeightScale'                                : [       110687,        99984,        90819,       110687,        99984,        90819,       110687,        99984,        90819, ],
    'CountWeightedL1PrefireNom'                                  : [        96052,        96062,        96055, ],
    'CountWeightedL1Prefire'                                     : [        96052,        95156,        96939, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106304,        96052,        87263,       106304,        96052,        87263,       106304,        96052,        87263, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     424747621), # 424.75MB, avg file size 424.75MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99972,        99988,        99986, ],
    'CountWeightedLHEWeightScale'                                : [       111340,        99972,        90344,       111340,        99972,        90344,       111340,        99972,        90344, ],
    'CountWeightedL1PrefireNom'                                  : [        95961,        95957,        95983, ],
    'CountWeightedL1Prefire'                                     : [        95961,        95051,        96864, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106847,        95961,        86730,       106847,        95961,        86730,       106847,        95961,        86730, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     432943853), # 432.94MB, avg file size 432.94MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       391000, ],
    'CountWeighted'                                              : [       390963,       390986,       390868, ],
    'CountWeightedLHEWeightScale'                                : [       395791,       390956,       383421,       395791,       390956,       383421,       395791,       390956,       383421, ],
    'CountWeightedL1PrefireNom'                                  : [       382618,       382603,       382577, ],
    'CountWeightedL1Prefire'                                     : [       382618,       380477,       384679, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       387282,       382612,       375274,       387282,       382612,       375274,       387282,       382612,       375274, ],
  }),
  ("nof_tree_events",                 391000),
  ("nof_db_events",                   391000),
  ("fsize_local",                     1234366463), # 1.23GB, avg file size 1.23GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                      : [       386000, ],
    'CountWeighted'                                              : [       385980,       385964,       386005, ],
    'CountWeightedLHEWeightScale'                                : [       392027,       385980,       377493,       392027,       385980,       377493,       392027,       385980,       377493, ],
    'CountWeightedL1PrefireNom'                                  : [       377355,       377331,       377384, ],
    'CountWeightedL1Prefire'                                     : [       377355,       375172,       379469, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       383207,       377355,       369100,       383207,       377355,       369100,       383207,       377355,       369100, ],
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     1232186602), # 1.23GB, avg file size 1.23GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                      : [       380000, ],
    'CountWeighted'                                              : [       380032,       379992,       379941, ],
    'CountWeightedLHEWeightScale'                                : [       387117,       380029,       370625,       387117,       380029,       370625,       387117,       380029,       370625, ],
    'CountWeightedL1PrefireNom'                                  : [       371256,       371229,       371192, ],
    'CountWeightedL1Prefire'                                     : [       371256,       369052,       373386, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       378137,       371252,       362136,       378137,       371252,       362136,       378137,       371252,       362136, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     1225235609), # 1.23GB, avg file size 1.23GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    30),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399976,       400033,       399958, ],
    'CountWeightedLHEWeightScale'                                : [       408712,       399973,       389181,       408712,       399973,       389181,       408712,       399973,       389181, ],
    'CountWeightedL1PrefireNom'                                  : [       390462,       390497,       390445, ],
    'CountWeightedL1Prefire'                                     : [       390462,       388091,       392765, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       398922,       390459,       379978,       398922,       390459,       379978,       398922,       390459,       379978, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1302729413), # 1.30GB, avg file size 1.30GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       400043,       400002,       399973, ],
    'CountWeightedLHEWeightScale'                                : [       411015,       400043,       387375,       411015,       400043,       387375,       411015,       400043,       387375, ],
    'CountWeightedL1PrefireNom'                                  : [       389930,       389875,       389912, ],
    'CountWeightedL1Prefire'                                     : [       389930,       387441,       392349, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       400570,       389930,       377663,       400570,       389930,       377663,       400570,       389930,       377663, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1330060089), # 1.33GB, avg file size 1.33GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       298000, ],
    'CountWeighted'                                              : [       297933,       297998,       297965, ],
    'CountWeightedLHEWeightScale'                                : [       307752,       297933,       287342,       307752,       297933,       287342,       307752,       297933,       287342, ],
    'CountWeightedL1PrefireNom'                                  : [       290135,       290169,       290158, ],
    'CountWeightedL1Prefire'                                     : [       290135,       288239,       291997, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       299628,       290135,       279863,       299628,       290135,       279863,       299628,       290135,       279863, ],
  }),
  ("nof_tree_events",                 298000),
  ("nof_db_events",                   298000),
  ("fsize_local",                     1009682552), # 1.01GB, avg file size 1.01GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       384000, ],
    'CountWeighted'                                              : [       383888,       383949,       384001, ],
    'CountWeightedLHEWeightScale'                                : [       399339,       383888,       368142,       399339,       383888,       368142,       399339,       383888,       368142, ],
    'CountWeightedL1PrefireNom'                                  : [       373340,       373357,       373424, ],
    'CountWeightedL1Prefire'                                     : [       373340,       370802,       375828, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       388250,       373340,       358074,       388250,       373340,       358074,       388250,       373340,       358074, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1333074693), # 1.33GB, avg file size 1.33GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       300008,       299973,       299999, ],
    'CountWeightedLHEWeightScale'                                : [       315125,       300008,       285252,       315125,       300008,       285252,       315125,       300008,       285252, ],
    'CountWeightedL1PrefireNom'                                  : [       291274,       291249,       291266, ],
    'CountWeightedL1Prefire'                                     : [       291274,       289208,       293306, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       305893,       291274,       277018,       305893,       291274,       277018,       305893,       291274,       277018, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1080941729), # 1.08GB, avg file size 1.08GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                      : [       280000, ],
    'CountWeighted'                                              : [       279985,       280001,       279960, ],
    'CountWeightedLHEWeightScale'                                : [       296616,       279985,       264338,       296616,       279985,       264338,       296616,       279985,       264338, ],
    'CountWeightedL1PrefireNom'                                  : [       271535,       271533,       271525, ],
    'CountWeightedL1Prefire'                                     : [       271535,       269562,       273478, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       287593,       271535,       256421,       287593,       271535,       256421,       287593,       271535,       256421, ],
  }),
  ("nof_tree_events",                 280000),
  ("nof_db_events",                   280000),
  ("fsize_local",                     1042298114), # 1.04GB, avg file size 1.04GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                      : [       284000, ],
    'CountWeighted'                                              : [       283954,       284020,       283903, ],
    'CountWeightedLHEWeightScale'                                : [       303010,       283954,       266463,       303010,       283954,       266463,       303010,       283954,       266463, ],
    'CountWeightedL1PrefireNom'                                  : [       275433,       275465,       275404, ],
    'CountWeightedL1Prefire'                                     : [       275433,       273447,       277394, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       293836,       275433,       258513,       293836,       275433,       258513,       293836,       275433,       258513, ],
  }),
  ("nof_tree_events",                 284000),
  ("nof_db_events",                   284000),
  ("fsize_local",                     1085285449), # 1.09GB, avg file size 1.09GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199979,       199979,       199969, ],
    'CountWeightedLHEWeightScale'                                : [       214732,       199979,       186604,       214732,       199979,       186604,       214732,       199979,       186604, ],
    'CountWeightedL1PrefireNom'                                  : [       193925,       193923,       193926, ],
    'CountWeightedL1Prefire'                                     : [       193925,       192525,       195308, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       208184,       193924,       180993,       208184,       193924,       180993,       208184,       193924,       180993, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     784698600), # 784.70MB, avg file size 784.70MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       198000, ],
    'CountWeighted'                                              : [       197982,       197967,       197985, ],
    'CountWeightedLHEWeightScale'                                : [       213792,       197982,       183808,       213792,       197982,       183808,       213792,       197982,       183808, ],
    'CountWeightedL1PrefireNom'                                  : [       191926,       191909,       191940, ],
    'CountWeightedL1Prefire'                                     : [       191926,       190531,       193304, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       207208,       191926,       178223,       207208,       191926,       178223,       207208,       191926,       178223, ],
  }),
  ("nof_tree_events",                 198000),
  ("nof_db_events",                   198000),
  ("fsize_local",                     793133088), # 793.13MB, avg file size 793.13MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199965,       199945,       199944, ],
    'CountWeightedLHEWeightScale'                                : [       217057,       199962,       184836,       217057,       199962,       184836,       217057,       199962,       184836, ],
    'CountWeightedL1PrefireNom'                                  : [       193894,       193868,       193893, ],
    'CountWeightedL1Prefire'                                     : [       193894,       192494,       195276, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       210416,       193891,       179253,       210416,       193891,       179253,       210416,       193891,       179253, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     816906917), # 816.91MB, avg file size 816.91MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       189000, ],
    'CountWeighted'                                              : [       188975,       188986,       188968, ],
    'CountWeightedLHEWeightScale'                                : [       206028,       188975,       173936,       206028,       188975,       173936,       206028,       188975,       173936, ],
    'CountWeightedL1PrefireNom'                                  : [       183333,       183320,       183349, ],
    'CountWeightedL1Prefire'                                     : [       183333,       182034,       184613, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       199843,       183333,       168774,       199843,       183333,       168774,       199843,       183333,       168774, ],
  }),
  ("nof_tree_events",                 189000),
  ("nof_db_events",                   189000),
  ("fsize_local",                     785984210), # 785.98MB, avg file size 785.98MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                      : [       196000, ],
    'CountWeighted'                                              : [       195958,       195985,       196001, ],
    'CountWeightedLHEWeightScale'                                : [       214575,       195958,       179692,       214575,       195958,       179692,       214575,       195958,       179692, ],
    'CountWeightedL1PrefireNom'                                  : [       190102,       190108,       190150, ],
    'CountWeightedL1Prefire'                                     : [       190102,       188758,       191429, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       208117,       190102,       174353,       208117,       190102,       174353,       208117,       190102,       174353, ],
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     828500202), # 828.50MB, avg file size 828.50MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199966,       199928,       199990, ],
    'CountWeightedLHEWeightScale'                                : [       219781,       199966,       182752,       219781,       199966,       182752,       219781,       199966,       182752, ],
    'CountWeightedL1PrefireNom'                                  : [       194028,       193988,       194056, ],
    'CountWeightedL1Prefire'                                     : [       194028,       192667,       195372, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       213219,       194028,       177351,       213219,       194028,       177351,       213219,       194028,       177351, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     855917899), # 855.92MB, avg file size 855.92MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       194000, ],
    'CountWeighted'                                              : [       193919,       193959,       193976, ],
    'CountWeightedL1PrefireNom'                                  : [       188167,       188178,       188226, ],
    'CountWeightedL1Prefire'                                     : [       188167,       186847,       189469, ],
  }),
  ("nof_tree_events",                 194000),
  ("nof_db_events",                   194000),
  ("fsize_local",                     847264363), # 847.26MB, avg file size 847.26MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99984,        99977,       100000, ],
    'CountWeightedLHEWeightScale'                                : [       110545,        99984,        90975,       110545,        99984,        90975,       110545,        99984,        90975, ],
    'CountWeightedL1PrefireNom'                                  : [        97149,        97137,        97169, ],
    'CountWeightedL1Prefire'                                     : [        97149,        96499,        97791, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107392,        97149,        88405,       107392,        97149,        88405,       107392,        97149,        88405, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     439042112), # 439.04MB, avg file size 439.04MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       100000, ],
    'CountWeighted'                                              : [        99955,        99979,        99958, ],
    'CountWeightedLHEWeightScale'                                : [       111321,        99955,        90319,       111321,        99955,        90319,       111321,        99955,        90319, ],
    'CountWeightedL1PrefireNom'                                  : [        97034,        97046,        97044, ],
    'CountWeightedL1Prefire'                                     : [        97034,        96368,        97692, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       108055,        97034,        87686,       108055,        97034,        87686,       108055,        97034,        87686, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     445429630), # 445.43MB, avg file size 445.43MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       399997, ],
    'CountWeighted'                                              : [       399912,       399995,       400009, ],
    'CountWeightedL1PrefireNom'                                  : [       392663,       392701,       392744, ],
    'CountWeightedL1Prefire'                                     : [       392663,       390758,       394480, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1266548543), # 1.27GB, avg file size 1.27GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       399993, ],
    'CountWeighted'                                              : [       399926,       399980,       400062, ],
    'CountWeightedLHEWeightScale'                                : [       406244,       399926,       391187,       406244,       399926,       391187,       406244,       399926,       391187, ],
    'CountWeightedL1PrefireNom'                                  : [       392305,       392323,       392408, ],
    'CountWeightedL1Prefire'                                     : [       392305,       390315,       394197, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       398437,       392303,       383746,       398437,       392303,       383746,       398437,       392303,       383746, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     1271244004), # 1.27GB, avg file size 1.27GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       399995, ],
    'CountWeighted'                                              : [       400040,       399918,       399979, ],
    'CountWeightedLHEWeightScale'                                : [       407501,       400040,       390166,       407501,       400040,       390166,       407501,       400040,       390166, ],
    'CountWeightedL1PrefireNom'                                  : [       392093,       391998,       392056, ],
    'CountWeightedL1Prefire'                                     : [       392093,       390041,       394044, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       399373,       392093,       382469,       399373,       392093,       382469,       399373,       392093,       382469, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1285590694), # 1.29GB, avg file size 1.29GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    27),
  ("nof_events",                      {
    'Count'                                                      : [       379996, ],
    'CountWeighted'                                              : [       380027,       379978,       380016, ],
    'CountWeightedL1PrefireNom'                                  : [       372179,       372139,       372174, ],
    'CountWeightedL1Prefire'                                     : [       372179,       370167,       374101, ],
  }),
  ("nof_tree_events",                 379996),
  ("nof_db_events",                   379996),
  ("fsize_local",                     1248069769), # 1.25GB, avg file size 1.25GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       299994, ],
    'CountWeighted'                                              : [       299947,       299958,       299956, ],
    'CountWeightedLHEWeightScale'                                : [       308254,       299947,       290540,       308254,       299947,       290540,       308254,       299947,       290540, ],
    'CountWeightedL1PrefireNom'                                  : [       293251,       293245,       293265, ],
    'CountWeightedL1Prefire'                                     : [       293251,       291556,       294881, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301314,       293249,       284074,       301314,       293249,       284074,       301314,       293249,       284074, ],
  }),
  ("nof_tree_events",                 299994),
  ("nof_db_events",                   299994),
  ("fsize_local",                     998883769), # 998.88MB, avg file size 998.88MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299973,       299990,       300039, ],
    'CountWeightedLHEWeightScale'                                : [       309807,       299973,       289292,       309807,       299973,       289292,       309807,       299973,       289292, ],
    'CountWeightedL1PrefireNom'                                  : [       292947,       292945,       293009, ],
    'CountWeightedL1Prefire'                                     : [       292947,       291186,       294644, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       302505,       292945,       282553,       302505,       292945,       282553,       302505,       292945,       282553, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1018863786), # 1.02GB, avg file size 1.02GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       299990, ],
    'CountWeighted'                                              : [       300015,       299997,       300031, ],
    'CountWeightedLHEWeightScale'                                : [       311942,       300013,       287616,       311942,       300013,       287616,       311942,       300013,       287616, ],
    'CountWeightedL1PrefireNom'                                  : [       292396,       292363,       292428, ],
    'CountWeightedL1Prefire'                                     : [       292396,       290515,       294219, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       303992,       292393,       280368,       303992,       292393,       280368,       303992,       292393,       280368, ],
  }),
  ("nof_tree_events",                 299990),
  ("nof_db_events",                   299990),
  ("fsize_local",                     1050791736), # 1.05GB, avg file size 1.05GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       286992, ],
    'CountWeighted'                                              : [       286998,       287038,       286974, ],
    'CountWeightedLHEWeightScale'                                : [       301485,       286998,       272879,       301485,       286998,       272879,       301485,       286998,       272879, ],
    'CountWeightedL1PrefireNom'                                  : [       278904,       278920,       278890, ],
    'CountWeightedL1Prefire'                                     : [       278904,       276940,       280815, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       292931,       278904,       265236,       292931,       278904,       265236,       292931,       278904,       265236, ],
  }),
  ("nof_tree_events",                 286992),
  ("nof_db_events",                   286992),
  ("fsize_local",                     1046294413), # 1.05GB, avg file size 1.05GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       291993, ],
    'CountWeighted'                                              : [       291964,       291938,       291927, ],
    'CountWeightedLHEWeightScale'                                : [       309262,       291964,       275698,       309262,       291964,       275698,       309262,       291964,       275698, ],
    'CountWeightedL1PrefireNom'                                  : [       283177,       283150,       283158, ],
    'CountWeightedL1Prefire'                                     : [       283177,       281069,       285234, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       299898,       283177,       267444,       299898,       283177,       267444,       299898,       283177,       267444, ],
  }),
  ("nof_tree_events",                 291993),
  ("nof_db_events",                   291993),
  ("fsize_local",                     1102329679), # 1.10GB, avg file size 1.10GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       269995, ],
    'CountWeighted'                                              : [       269945,       269994,       269969, ],
    'CountWeightedLHEWeightScale'                                : [       288081,       269945,       253320,       288081,       269945,       253320,       288081,       269945,       253320, ],
    'CountWeightedL1PrefireNom'                                  : [       261383,       261399,       261411, ],
    'CountWeightedL1Prefire'                                     : [       261383,       259350,       263379, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       278870,       261383,       245322,       278870,       261383,       245322,       278870,       261383,       245322, ],
  }),
  ("nof_tree_events",                 269995),
  ("nof_db_events",                   269995),
  ("fsize_local",                     1048177823), # 1.05GB, avg file size 1.05GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       299996, ],
    'CountWeighted'                                              : [       299951,       299985,       299983, ],
    'CountWeightedLHEWeightScale'                                : [       322113,       299951,       279890,       322113,       299951,       279890,       322113,       299951,       279890, ],
    'CountWeightedL1PrefireNom'                                  : [       289899,       289908,       289935, ],
    'CountWeightedL1Prefire'                                     : [       289899,       287535,       292224, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       311241,       289899,       270556,       311241,       289899,       270556,       311241,       289899,       270556, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1193001506), # 1.19GB, avg file size 1.19GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       195995, ],
    'CountWeighted'                                              : [       195994,       195980,       195932, ],
    'CountWeightedLHEWeightScale'                                : [       211660,       195994,       181973,       211660,       195994,       181973,       211660,       195994,       181973, ],
    'CountWeightedL1PrefireNom'                                  : [       189211,       189191,       189176, ],
    'CountWeightedL1Prefire'                                     : [       189211,       187628,       190768, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       204286,       189211,       175706,       204286,       189211,       175706,       204286,       189211,       175706, ],
  }),
  ("nof_tree_events",                 195995),
  ("nof_db_events",                   195995),
  ("fsize_local",                     795340127), # 795.34MB, avg file size 795.34MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       199995, ],
    'CountWeighted'                                              : [       199976,       200017,       199986, ],
    'CountWeightedLHEWeightScale'                                : [       217031,       199976,       184826,       217031,       199976,       184826,       217031,       199976,       184826, ],
    'CountWeightedL1PrefireNom'                                  : [       192824,       192850,       192826, ],
    'CountWeightedL1Prefire'                                     : [       192824,       191162,       194465, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       209228,       192824,       178252,       209228,       192824,       178252,       209228,       192824,       178252, ],
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     824676138), # 824.68MB, avg file size 824.68MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       191997, ],
    'CountWeighted'                                              : [       191969,       191984,       192002, ],
    'CountWeightedLHEWeightScale'                                : [       209335,       191969,       176706,       209335,       191969,       176706,       209335,       191969,       176706, ],
    'CountWeightedL1PrefireNom'                                  : [       184877,       184870,       184915, ],
    'CountWeightedL1Prefire'                                     : [       184877,       183239,       186497, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       201548,       184877,       170210,       201548,       184877,       170210,       201548,       184877,       170210, ],
  }),
  ("nof_tree_events",                 191997),
  ("nof_db_events",                   191997),
  ("fsize_local",                     802363786), # 802.36MB, avg file size 802.36MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       199998, ],
    'CountWeighted'                                              : [       199937,       199943,       199981, ],
    'CountWeightedL1PrefireNom'                                  : [       192514,       192494,       192560, ],
    'CountWeightedL1Prefire'                                     : [       192514,       190803,       194206, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     851115809), # 851.12MB, avg file size 851.12MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       199999, ],
    'CountWeighted'                                              : [       200008,       199963,       199958, ],
    'CountWeightedL1PrefireNom'                                  : [       192411,       192369,       192385, ],
    'CountWeightedL1Prefire'                                     : [       192411,       190669,       194133, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     858716784), # 858.72MB, avg file size 858.72MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       191996, ],
    'CountWeighted'                                              : [       191963,       191966,       191970, ],
    'CountWeightedL1PrefireNom'                                  : [       184557,       184545,       184575, ],
    'CountWeightedL1Prefire'                                     : [       184557,       182859,       186236, ],
  }),
  ("nof_tree_events",                 191996),
  ("nof_db_events",                   191996),
  ("fsize_local",                     831081990), # 831.08MB, avg file size 831.08MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                      : [       199997, ],
    'CountWeighted'                                              : [       199949,       199993,       199967, ],
    'CountWeightedLHEWeightScale'                                : [       221319,       199949,       181636,       221319,       199949,       181636,       221319,       199949,       181636, ],
    'CountWeightedL1PrefireNom'                                  : [       192073,       192093,       192099, ],
    'CountWeightedL1Prefire'                                     : [       192073,       190277,       193852, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       212550,       192073,       174511,       212550,       192073,       174511,       212550,       192073,       174511, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     863558874), # 863.56MB, avg file size 863.56MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                      : [        99998, ],
    'CountWeighted'                                              : [        99981,        99973,        99971, ],
    'CountWeightedLHEWeightScale'                                : [       111335,        99981,        90329,       111335,        99981,        90329,       111335,        99981,        90329, ],
    'CountWeightedL1PrefireNom'                                  : [        95950,        95940,        95950, ],
    'CountWeightedL1Prefire'                                     : [        95950,        95035,        96855, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106826,        95950,        86706,       106826,        95950,        86706,       106826,        95950,        86706, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     437316626), # 437.32MB, avg file size 437.32MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_2v2t"),
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
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                      : [       394995, ],
    'CountWeighted'                                              : [       394971,       394983,       394986, ],
    'CountWeightedLHEWeightScale'                                : [       399822,       394971,       387348,       399822,       394971,       387348,       399822,       394971,       387348, ],
    'CountWeightedL1PrefireNom'                                  : [       387385,       387372,       387405, ],
    'CountWeightedL1Prefire'                                     : [       387385,       385411,       389257, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       392099,       387385,       379939,       392099,       387385,       379939,       392099,       387385,       379939, ],
  }),
  ("nof_tree_events",                 394995),
  ("nof_db_events",                   394995),
  ("fsize_local",                     1257257282), # 1.26GB, avg file size 628.63MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       395995, ],
    'CountWeighted'                                              : [       396046,       395974,       395919, ],
    'CountWeightedLHEWeightScale'                                : [       402169,       396042,       387239,       402169,       396042,       387239,       402169,       396042,       387239, ],
    'CountWeightedL1PrefireNom'                                  : [       388067,       388000,       387991, ],
    'CountWeightedL1Prefire'                                     : [       388067,       386015,       390017, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       394043,       388063,       379497,       394043,       388063,       379497,       394043,       388063,       379497, ],
  }),
  ("nof_tree_events",                 395995),
  ("nof_db_events",                   395995),
  ("fsize_local",                     1278856550), # 1.28GB, avg file size 1.28GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       399996, ],
    'CountWeighted'                                              : [       399985,       400020,       399915, ],
    'CountWeightedLHEWeightScale'                                : [       407519,       399978,       390124,       407519,       399978,       390124,       407519,       399978,       390124, ],
    'CountWeightedL1PrefireNom'                                  : [       391645,       391669,       391579, ],
    'CountWeightedL1Prefire'                                     : [       391645,       389515,       393682, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       398970,       391638,       382034,       398970,       391638,       382034,       398970,       391638,       382034, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1309906886), # 1.31GB, avg file size 1.31GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                      : [       394995, ],
    'CountWeighted'                                              : [       394912,       394999,       394963, ],
    'CountWeightedLHEWeightScale'                                : [       403595,       394912,       384345,       403595,       394912,       384345,       403595,       394912,       384345, ],
    'CountWeightedL1PrefireNom'                                  : [       386437,       386490,       386491, ],
    'CountWeightedL1Prefire'                                     : [       386437,       384287,       388511, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       394864,       386437,       376119,       394864,       386437,       376119,       394864,       386437,       376119, ],
  }),
  ("nof_tree_events",                 394995),
  ("nof_db_events",                   394995),
  ("fsize_local",                     1310139085), # 1.31GB, avg file size 1.31GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       299995, ],
    'CountWeighted'                                              : [       299902,       299975,       299952, ],
    'CountWeightedLHEWeightScale'                                : [       308266,       299902,       290534,       308266,       299902,       290534,       308266,       299902,       290534, ],
    'CountWeightedL1PrefireNom'                                  : [       292984,       293013,       293032, ],
    'CountWeightedL1Prefire'                                     : [       292984,       291248,       294661, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       301081,       292984,       283845,       301081,       292984,       283845,       301081,       292984,       283845, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1021721713), # 1.02GB, avg file size 1.02GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       284992, ],
    'CountWeighted'                                              : [       285008,       285000,       284949, ],
    'CountWeightedLHEWeightScale'                                : [       294338,       285006,       274835,       294338,       285006,       274835,       294338,       285006,       274835, ],
    'CountWeightedL1PrefireNom'                                  : [       278087,       278071,       278057, ],
    'CountWeightedL1Prefire'                                     : [       278087,       276376,       279743, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       287149,       278085,       268210,       287149,       278085,       268210,       287149,       278085,       268210, ],
  }),
  ("nof_tree_events",                 284992),
  ("nof_db_events",                   284992),
  ("fsize_local",                     994274803), # 994.27MB, avg file size 994.27MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       299995, ],
    'CountWeighted'                                              : [       299938,       299881,       300033, ],
    'CountWeightedLHEWeightScale'                                : [       311974,       299938,       287601,       311974,       299938,       287601,       311974,       299938,       287601, ],
    'CountWeightedL1PrefireNom'                                  : [       292221,       292175,       292294, ],
    'CountWeightedL1Prefire'                                     : [       292221,       290341,       294059, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       303880,       292221,       280245,       303880,       292221,       280245,       303880,       292221,       280245, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1080854642), # 1.08GB, avg file size 1.08GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       289998, ],
    'CountWeighted'                                              : [       289996,       289957,       289966, ],
    'CountWeightedLHEWeightScale'                                : [       304611,       289996,       275747,       304611,       289996,       275747,       304611,       289996,       275747, ],
    'CountWeightedL1PrefireNom'                                  : [       281939,       281908,       281924, ],
    'CountWeightedL1Prefire'                                     : [       281939,       280012,       283824, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       296093,       281939,       268144,       296093,       281939,       268144,       296093,       281939,       268144, ],
  }),
  ("nof_tree_events",                 289998),
  ("nof_db_events",                   289998),
  ("fsize_local",                     1091340446), # 1.09GB, avg file size 1.09GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       279993, ],
    'CountWeighted'                                              : [       279968,       279991,       279973, ],
    'CountWeightedLHEWeightScale'                                : [       296579,       279968,       264335,       296579,       279968,       264335,       296579,       279968,       264335, ],
    'CountWeightedL1PrefireNom'                                  : [       271965,       271969,       271975, ],
    'CountWeightedL1Prefire'                                     : [       271965,       270068,       273824, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       288037,       271965,       256833,       288037,       271965,       256833,       288037,       271965,       256833, ],
  }),
  ("nof_tree_events",                 279993),
  ("nof_db_events",                   279993),
  ("fsize_local",                     1091627104), # 1.09GB, avg file size 1.09GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       199997, ],
    'CountWeighted'                                              : [       199962,       199954,       200027, ],
    'CountWeightedLHEWeightScale'                                : [       213368,       199962,       187664,       213368,       199962,       187664,       213368,       199962,       187664, ],
    'CountWeightedL1PrefireNom'                                  : [       194021,       194014,       194067, ],
    'CountWeightedL1Prefire'                                     : [       194021,       192631,       195389, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       206975,       194021,       182118,       206975,       194021,       182118,       206975,       194021,       182118, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     803177861), # 803.18MB, avg file size 803.18MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       199995, ],
    'CountWeighted'                                              : [       199967,       199963,       199992, ],
    'CountWeightedLHEWeightScale'                                : [       214710,       199967,       186601,       214710,       199967,       186601,       214710,       199967,       186601, ],
    'CountWeightedL1PrefireNom'                                  : [       194016,       194002,       194046, ],
    'CountWeightedL1Prefire'                                     : [       194016,       192631,       195380, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       208273,       194016,       181081,       208273,       194016,       181081,       208273,       194016,       181081, ],
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     823493229), # 823.49MB, avg file size 823.49MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       199996, ],
    'CountWeighted'                                              : [       199985,       199986,       199963, ],
    'CountWeightedLHEWeightScale'                                : [       215957,       199985,       185674,       215957,       199985,       185674,       215957,       199985,       185674, ],
    'CountWeightedL1PrefireNom'                                  : [       193922,       193910,       193919, ],
    'CountWeightedL1Prefire'                                     : [       193922,       192518,       195305, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       209364,       193922,       180080,       209364,       193922,       180080,       209364,       193922,       180080, ],
  }),
  ("nof_tree_events",                 199996),
  ("nof_db_events",                   199996),
  ("fsize_local",                     837739788), # 837.74MB, avg file size 837.74MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       195999, ],
    'CountWeighted'                                              : [       195966,       196011,       196009, ],
    'CountWeightedLHEWeightScale'                                : [       212743,       195966,       181137,       212743,       195966,       181137,       212743,       195966,       181137, ],
    'CountWeightedL1PrefireNom'                                  : [       190109,       190128,       190147, ],
    'CountWeightedL1Prefire'                                     : [       190109,       188757,       191445, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       206325,       190108,       175750,       206325,       190108,       175750,       206325,       190108,       175750, ],
  }),
  ("nof_tree_events",                 195999),
  ("nof_db_events",                   195999),
  ("fsize_local",                     832184886), # 832.18MB, avg file size 832.18MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       195997, ],
    'CountWeighted'                                              : [       195965,       195970,       195941, ],
    'CountWeightedLHEWeightScale'                                : [       213670,       195963,       180386,       213670,       195963,       180386,       213670,       195963,       180386, ],
    'CountWeightedL1PrefireNom'                                  : [       190095,       190087,       190083, ],
    'CountWeightedL1Prefire'                                     : [       190095,       188743,       191426, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       207224,       190093,       175010,       207224,       190093,       175010,       207224,       190093,       175010, ],
  }),
  ("nof_tree_events",                 195997),
  ("nof_db_events",                   195997),
  ("fsize_local",                     841701982), # 841.70MB, avg file size 841.70MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [       199999, ],
    'CountWeighted'                                              : [       199947,       199975,       199954, ],
    'CountWeightedLHEWeightScale'                                : [       218950,       199947,       183382,       218950,       199947,       183382,       218950,       199947,       183382, ],
    'CountWeightedL1PrefireNom'                                  : [       194016,       194014,       194045, ],
    'CountWeightedL1Prefire'                                     : [       194016,       192653,       195363, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       212409,       194016,       177967,       212409,       194016,       177967,       212409,       194016,       177967, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     867524755), # 867.52MB, avg file size 867.52MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       199998, ],
    'CountWeighted'                                              : [       199960,       199996,       199961, ],
    'CountWeightedLHEWeightScale'                                : [       219822,       199960,       182751,       219822,       199960,       182751,       219822,       199960,       182751, ],
    'CountWeightedL1PrefireNom'                                  : [       194075,       194082,       194085, ],
    'CountWeightedL1Prefire'                                     : [       194075,       192725,       195408, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       213300,       194074,       177398,       213300,       194074,       177398,       213300,       194074,       177398, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     872836532), # 872.84MB, avg file size 872.84MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       191995, ],
    'CountWeighted'                                              : [       191992,       191941,       191949, ],
    'CountWeightedL1PrefireNom'                                  : [       186299,       186261,       186274, ],
    'CountWeightedL1Prefire'                                     : [       186299,       184996,       187580, ],
  }),
  ("nof_tree_events",                 191995),
  ("nof_db_events",                   191995),
  ("fsize_local",                     849458657), # 849.46MB, avg file size 849.46MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [        99999, ],
    'CountWeighted'                                              : [       100008,       100004,        99996, ],
    'CountWeightedLHEWeightScale'                                : [       110552,       100008,        90985,       110552,       100008,        90985,       110552,       100008,        90985, ],
    'CountWeightedL1PrefireNom'                                  : [        97172,        97161,        97171, ],
    'CountWeightedL1Prefire'                                     : [        97172,        96522,        97811, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107401,        97172,        88418,       107401,        97172,        88418,       107401,        97172,        88418, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     442298164), # 442.30MB, avg file size 442.30MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                      : [        99999, ],
    'CountWeighted'                                              : [        99983,        99976,        99999, ],
    'CountWeightedLHEWeightScale'                                : [       111340,        99983,        90337,       111340,        99983,        90337,       111340,        99983,        90337, ],
    'CountWeightedL1PrefireNom'                                  : [        97021,        97002,        97045, ],
    'CountWeightedL1Prefire'                                     : [        97021,        96348,        97687, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       108028,        97021,        87672,       108028,        97021,        87672,       108028,        97021,        87672, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     444957061), # 444.96MB, avg file size 444.96MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       399999, ],
    'CountWeighted'                                              : [       399938,       399982,       400001, ],
    'CountWeightedL1PrefireNom'                                  : [       393457,       393478,       393506, ],
    'CountWeightedL1Prefire'                                     : [       393457,       391731,       395079, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1248189553), # 1.25GB, avg file size 1.25GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       399998, ],
    'CountWeighted'                                              : [       399968,       399970,       399950, ],
    'CountWeightedLHEWeightScale'                                : [       406232,       399968,       391162,       406232,       399968,       391162,       406232,       399968,       391162, ],
    'CountWeightedL1PrefireNom'                                  : [       393223,       393218,       393217, ],
    'CountWeightedL1Prefire'                                     : [       393223,       391440,       394905, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       399350,       393223,       384597,       399350,       393223,       384597,       399350,       393223,       384597, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1256393814), # 1.26GB, avg file size 1.26GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       386000, ],
    'CountWeighted'                                              : [       385979,       386074,       385895, ],
    'CountWeightedLHEWeightScale'                                : [       393217,       385978,       376476,       393217,       385978,       376476,       393217,       385978,       376476, ],
    'CountWeightedL1PrefireNom'                                  : [       379159,       379213,       379109, ],
    'CountWeightedL1Prefire'                                     : [       379159,       377367,       380851, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       386241,       379158,       369856,       386241,       379158,       369856,       386241,       379158,       369856, ],
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     1231260285), # 1.23GB, avg file size 1.23GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                      : [       388998, ],
    'CountWeighted'                                              : [       388993,       389050,       389025, ],
    'CountWeightedL1PrefireNom'                                  : [       381861,       381889,       381896, ],
    'CountWeightedL1Prefire'                                     : [       381861,       379997,       383629, ],
  }),
  ("nof_tree_events",                 388998),
  ("nof_db_events",                   388998),
  ("fsize_local",                     1271132054), # 1.27GB, avg file size 1.27GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299994,       299954,       299988, ],
    'CountWeightedLHEWeightScale'                                : [       308274,       299993,       290511,       308274,       299993,       290511,       308274,       299993,       290511, ],
    'CountWeightedL1PrefireNom'                                  : [       293967,       293937,       293963, ],
    'CountWeightedL1Prefire'                                     : [       293967,       292414,       295446, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       302048,       293965,       284707,       302048,       293965,       284707,       302048,       293965,       284707, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     998370671), # 998.37MB, avg file size 998.37MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299959,       299976,       300022, ],
    'CountWeightedLHEWeightScale'                                : [       309824,       299959,       289276,       309824,       299959,       289276,       309824,       299959,       289276, ],
    'CountWeightedL1PrefireNom'                                  : [       293538,       293526,       293594, ],
    'CountWeightedL1Prefire'                                     : [       293538,       291899,       295101, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       303147,       293538,       283113,       303147,       293538,       283113,       303147,       293538,       283113, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1023767694), # 1.02GB, avg file size 1.02GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       291998, ],
    'CountWeighted'                                              : [       292022,       291953,       291962, ],
    'CountWeightedLHEWeightScale'                                : [       303640,       292022,       279967,       303640,       292022,       279967,       303640,       292022,       279967, ],
    'CountWeightedL1PrefireNom'                                  : [       285216,       285151,       285194, ],
    'CountWeightedL1Prefire'                                     : [       285216,       283505,       286853, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       296541,       285216,       273488,       296541,       285216,       273488,       296541,       285216,       273488, ],
  }),
  ("nof_tree_events",                 291998),
  ("nof_db_events",                   291998),
  ("fsize_local",                     1029713389), # 1.03GB, avg file size 1.03GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       300046,       299928,       300052, ],
    'CountWeightedLHEWeightScale'                                : [       315116,       300046,       285272,       315116,       300046,       285272,       315116,       300046,       285272, ],
    'CountWeightedL1PrefireNom'                                  : [       292169,       292079,       292191, ],
    'CountWeightedL1Prefire'                                     : [       292169,       290230,       294044, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       306821,       292169,       277846,       306821,       292169,       277846,       306821,       292169,       277846, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1108305830), # 1.11GB, avg file size 1.11GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       292000, ],
    'CountWeighted'                                              : [       291999,       291991,       291964, ],
    'CountWeightedLHEWeightScale'                                : [       309297,       291990,       275678,       309297,       291990,       275678,       309297,       291990,       275678, ],
    'CountWeightedL1PrefireNom'                                  : [       283699,       283673,       283690, ],
    'CountWeightedL1Prefire'                                     : [       283699,       281685,       285653, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       300459,       283693,       267896,       300459,       283693,       267896,       300459,       283693,       267896, ],
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     1119399685), # 1.12GB, avg file size 1.12GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       299982,       299980,       299981, ],
    'CountWeightedLHEWeightScale'                                : [       320092,       299982,       281474,       320092,       299982,       281474,       320092,       299982,       281474, ],
    'CountWeightedL1PrefireNom'                                  : [       290825,       290815,       290830, ],
    'CountWeightedL1Prefire'                                     : [       290825,       288630,       292964, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       310255,       290825,       272935,       310255,       290825,       272935,       310255,       290825,       272935, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1186979724), # 1.19GB, avg file size 1.19GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       299981,       299981,       299913, ],
    'CountWeightedLHEWeightScale'                                : [       322090,       299981,       279884,       322090,       299981,       279884,       322090,       299981,       279884, ],
    'CountWeightedL1PrefireNom'                                  : [       290197,       290190,       290165, ],
    'CountWeightedL1Prefire'                                     : [       290197,       287885,       292466, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       311529,       290197,       270818,       311529,       290197,       270818,       311529,       290197,       270818, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1216504097), # 1.22GB, avg file size 1.22GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       195999, ],
    'CountWeighted'                                              : [       195990,       195994,       195981, ],
    'CountWeightedLHEWeightScale'                                : [       211611,       195990,       181953,       211611,       195990,       181953,       211611,       195990,       181953, ],
    'CountWeightedL1PrefireNom'                                  : [       189370,       189376,       189364, ],
    'CountWeightedL1Prefire'                                     : [       189370,       187814,       190897, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       204428,       189370,       175843,       204428,       189370,       175843,       204428,       189370,       175843, ],
  }),
  ("nof_tree_events",                 195999),
  ("nof_db_events",                   195999),
  ("fsize_local",                     808714972), # 808.71MB, avg file size 808.71MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       199999, ],
    'CountWeighted'                                              : [       199958,       199958,       199938, ],
    'CountWeightedLHEWeightScale'                                : [       217068,       199958,       184802,       217068,       199958,       184802,       217068,       199958,       184802, ],
    'CountWeightedL1PrefireNom'                                  : [       192896,       192884,       192906, ],
    'CountWeightedL1Prefire'                                     : [       192896,       191251,       194515, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       209343,       192896,       178313,       209343,       192896,       178313,       209343,       192896,       178313, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     835211719), # 835.21MB, avg file size 835.21MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199998,       200009,       199967, ],
    'CountWeightedLHEWeightScale'                                : [       218036,       199998,       184074,       218036,       199998,       184074,       218036,       199998,       184074, ],
    'CountWeightedL1PrefireNom'                                  : [       192911,       192910,       192894, ],
    'CountWeightedL1Prefire'                                     : [       192911,       191265,       194534, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       210274,       192911,       177594,       210274,       192911,       177594,       210274,       192911,       177594, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     842788244), # 842.79MB, avg file size 842.79MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       192000, ],
    'CountWeighted'                                              : [       191987,       191986,       191978, ],
    'CountWeightedL1PrefireNom'                                  : [       184948,       184936,       184956, ],
    'CountWeightedL1Prefire'                                     : [       184948,       183321,       186554, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     821186953), # 821.19MB, avg file size 821.19MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                      : [       199997, ],
    'CountWeighted'                                              : [       199952,       199956,       199958, ],
    'CountWeightedL1PrefireNom'                                  : [       192538,       192520,       192557, ],
    'CountWeightedL1Prefire'                                     : [       192538,       190827,       194229, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     858849072), # 858.85MB, avg file size 858.85MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                      : [       199999, ],
    'CountWeighted'                                              : [       199966,       199933,       199984, ],
    'CountWeightedL1PrefireNom'                                  : [       192344,       192313,       192363, ],
    'CountWeightedL1Prefire'                                     : [       192344,       190594,       194069, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     861014505), # 861.01MB, avg file size 861.01MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199982,       199987,       199978, ],
    'CountWeightedLHEWeightScale'                                : [       221314,       199982,       181619,       221314,       199982,       181619,       221314,       199982,       181619, ],
    'CountWeightedL1PrefireNom'                                  : [       192276,       192266,       192295, ],
    'CountWeightedL1Prefire'                                     : [       192276,       190515,       194019, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       212748,       192276,       174670,       212748,       192276,       174670,       212748,       192276,       174670, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     856161697), # 856.16MB, avg file size 856.16MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                      : [        99999, ],
    'CountWeighted'                                              : [        99963,        99968,        99985, ],
    'CountWeightedLHEWeightScale'                                : [       111352,        99962,        90330,       111352,        99962,        90330,       111352,        99962,        90330, ],
    'CountWeightedL1PrefireNom'                                  : [        95938,        95939,        95953, ],
    'CountWeightedL1Prefire'                                     : [        95938,        95025,        96842, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       106835,        95938,        86705,       106835,        95938,        86705,       106835,        95938,        86705, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     429619666), # 429.62MB, avg file size 429.62MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       399996, ],
    'CountWeighted'                                              : [       400015,       399955,       399984, ],
    'CountWeightedLHEWeightScale'                                : [       404907,       400015,       392226,       404907,       400015,       392226,       404907,       400015,       392226, ],
    'CountWeightedL1PrefireNom'                                  : [       393165,       393103,       393169, ],
    'CountWeightedL1Prefire'                                     : [       393165,       391364,       394859, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       397950,       393165,       385549,       397950,       393165,       385549,       397950,       393165,       385549, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1255599161), # 1.26GB, avg file size 1.26GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       399997, ],
    'CountWeighted'                                              : [       400006,       399970,       399988, ],
    'CountWeightedLHEWeightScale'                                : [       406234,       400006,       391158,       406234,       400006,       391158,       406234,       400006,       391158, ],
    'CountWeightedL1PrefireNom'                                  : [       392838,       392797,       392843, ],
    'CountWeightedL1Prefire'                                     : [       392838,       390963,       394603, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       398924,       392836,       384187,       398924,       392836,       384187,       398924,       392836,       384187, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1279537755), # 1.28GB, avg file size 1.28GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399952,       399938,       399998, ],
    'CountWeightedLHEWeightScale'                                : [       407518,       399952,       390145,       407518,       399952,       390145,       407518,       399952,       390145, ],
    'CountWeightedL1PrefireNom'                                  : [       392566,       392535,       392616, ],
    'CountWeightedL1Prefire'                                     : [       392566,       390637,       394387, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       399941,       392566,       382962,       399941,       392566,       382962,       399941,       392566,       382962, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1301469346), # 1.30GB, avg file size 1.30GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       391999, ],
    'CountWeighted'                                              : [       391963,       391927,       391970, ],
    'CountWeightedLHEWeightScale'                                : [       400557,       391963,       381390,       400557,       391963,       381390,       400557,       391963,       381390, ],
    'CountWeightedL1PrefireNom'                                  : [       384317,       384281,       384320, ],
    'CountWeightedL1Prefire'                                     : [       384317,       382340,       386186, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       392696,       384317,       373982,       392696,       384317,       373982,       392696,       384317,       373982, ],
  }),
  ("nof_tree_events",                 391999),
  ("nof_db_events",                   391999),
  ("fsize_local",                     1296062891), # 1.30GB, avg file size 1.30GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       383998, ],
    'CountWeighted'                                              : [       383900,       383941,       384002, ],
    'CountWeightedLHEWeightScale'                                : [       394555,       383900,       371886,       394555,       383900,       371886,       394555,       383900,       371886, ],
    'CountWeightedL1PrefireNom'                                  : [       375910,       375919,       375996, ],
    'CountWeightedL1Prefire'                                     : [       375910,       373869,       377856, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       386271,       375910,       364162,       386271,       375910,       364162,       386271,       375910,       364162, ],
  }),
  ("nof_tree_events",                 383998),
  ("nof_db_events",                   383998),
  ("fsize_local",                     1310764333), # 1.31GB, avg file size 1.31GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299984,       299946,       300008, ],
    'CountWeightedLHEWeightScale'                                : [       309819,       299984,       289293,       309819,       299984,       289293,       309819,       299984,       289293, ],
    'CountWeightedL1PrefireNom'                                  : [       293359,       293323,       293388, ],
    'CountWeightedL1Prefire'                                     : [       293359,       291690,       294958, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       302940,       293359,       282944,       302940,       293359,       282944,       302940,       293359,       282944, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1052913734), # 1.05GB, avg file size 1.05GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       299999, ],
    'CountWeighted'                                              : [       299949,       300022,       299978, ],
    'CountWeightedLHEWeightScale'                                : [       311994,       299949,       287634,       311994,       299949,       287634,       311994,       299949,       287634, ],
    'CountWeightedL1PrefireNom'                                  : [       292808,       292851,       292834, ],
    'CountWeightedL1Prefire'                                     : [       292808,       291034,       294520, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       304506,       292808,       280818,       304506,       292808,       280818,       304506,       292808,       280818, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1092696505), # 1.09GB, avg file size 1.09GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       300000, ],
    'CountWeighted'                                              : [       299961,       299949,       299978, ],
    'CountWeightedLHEWeightScale'                                : [       315114,       299961,       285299,       315114,       299961,       285299,       315114,       299961,       285299, ],
    'CountWeightedL1PrefireNom'                                  : [       292123,       292108,       292142, ],
    'CountWeightedL1Prefire'                                     : [       292123,       290216,       293976, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       306817,       292123,       277884,       306817,       292123,       277884,       306817,       292123,       277884, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1148859708), # 1.15GB, avg file size 1.15GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       287998, ],
    'CountWeighted'                                              : [       288000,       287963,       287966, ],
    'CountWeightedLHEWeightScale'                                : [       305061,       288000,       271899,       305061,       288000,       271899,       305061,       288000,       271899, ],
    'CountWeightedL1PrefireNom'                                  : [       279988,       279956,       279968, ],
    'CountWeightedL1Prefire'                                     : [       279988,       278074,       281858, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       296520,       279988,       264399,       296520,       279988,       264399,       296520,       279988,       264399, ],
  }),
  ("nof_tree_events",                 287998),
  ("nof_db_events",                   287998),
  ("fsize_local",                     1145777943), # 1.15GB, avg file size 1.15GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       299997, ],
    'CountWeighted'                                              : [       299986,       299985,       299933, ],
    'CountWeightedLHEWeightScale'                                : [       320048,       299986,       281479,       320048,       299986,       281479,       320048,       299986,       281479, ],
    'CountWeightedL1PrefireNom'                                  : [       291340,       291327,       291328, ],
    'CountWeightedL1Prefire'                                     : [       291340,       289304,       293339, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       310763,       291340,       273425,       310763,       291340,       273425,       310763,       291340,       273425, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1230339683), # 1.23GB, avg file size 1.23GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       299998, ],
    'CountWeighted'                                              : [       300039,       300038,       299931, ],
    'CountWeightedLHEWeightScale'                                : [       322091,       300039,       279875,       322091,       300039,       279875,       322091,       300039,       279875, ],
    'CountWeightedL1PrefireNom'                                  : [       291188,       291169,       291125, ],
    'CountWeightedL1Prefire'                                     : [       291188,       289119,       293213, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       312536,       291188,       271697,       312536,       291188,       271697,       312536,       291188,       271697, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1257134914), # 1.26GB, avg file size 1.26GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       191998, ],
    'CountWeighted'                                              : [       192007,       192024,       191962, ],
    'CountWeightedLHEWeightScale'                                : [       207322,       192007,       178228,       207322,       192007,       178228,       207322,       192007,       178228, ],
    'CountWeightedL1PrefireNom'                                  : [       186311,       186307,       186298, ],
    'CountWeightedL1Prefire'                                     : [       186311,       184990,       187612, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       201130,       186311,       172986,       201130,       186311,       172986,       201130,       186311,       172986, ],
  }),
  ("nof_tree_events",                 191998),
  ("nof_db_events",                   191998),
  ("fsize_local",                     816337930), # 816.34MB, avg file size 816.34MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       200000, ],
    'CountWeighted'                                              : [       199958,       200016,       199953, ],
    'CountWeightedLHEWeightScale'                                : [       217069,       199957,       184854,       217069,       199957,       184854,       217069,       199957,       184854, ],
    'CountWeightedL1PrefireNom'                                  : [       193936,       193968,       193934, ],
    'CountWeightedL1Prefire'                                     : [       193936,       192544,       195309, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       210469,       193935,       179312,       210469,       193935,       179312,       210469,       193935,       179312, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     858547442), # 858.55MB, avg file size 858.55MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       191999, ],
    'CountWeighted'                                              : [       191988,       191989,       192021, ],
    'CountWeightedLHEWeightScale'                                : [       209350,       191987,       176705,       209350,       191987,       176705,       209350,       191987,       176705, ],
    'CountWeightedL1PrefireNom'                                  : [       186285,       186282,       186312, ],
    'CountWeightedL1Prefire'                                     : [       186285,       184973,       187581, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       203084,       186284,       171494,       203084,       186284,       171494,       203084,       186284,       171494, ],
  }),
  ("nof_tree_events",                 191999),
  ("nof_db_events",                   191999),
  ("fsize_local",                     828295503), # 828.30MB, avg file size 828.30MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                      : [       199997, ],
    'CountWeighted'                                              : [       199978,       199959,       199965, ],
    'CountWeightedLHEWeightScale'                                : [       218966,       199978,       183371,       218966,       199978,       183371,       218966,       199978,       183371, ],
    'CountWeightedL1PrefireNom'                                  : [       193982,       193958,       193983, ],
    'CountWeightedL1Prefire'                                     : [       193982,       192605,       195337, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       212353,       193982,       177907,       212353,       193982,       177907,       212353,       193982,       177907, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     865543360), # 865.54MB, avg file size 865.54MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       199998, ],
    'CountWeighted'                                              : [       199979,       199932,       199968, ],
    'CountWeightedLHEWeightScale'                                : [       219773,       199978,       182732,       219773,       199978,       182732,       219773,       199978,       182732, ],
    'CountWeightedL1PrefireNom'                                  : [       194001,       193956,       193999, ],
    'CountWeightedL1Prefire'                                     : [       194001,       192634,       195348, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       213169,       194000,       177306,       213169,       194000,       177306,       213169,       194000,       177306, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     866115010), # 866.12MB, avg file size 866.12MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       199999, ],
    'CountWeighted'                                              : [       199950,       199956,       199984, ],
    'CountWeightedL1PrefireNom'                                  : [       194041,       194034,       194073, ],
    'CountWeightedL1Prefire'                                     : [       194041,       192688,       195374, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     872269146), # 872.27MB, avg file size 872.27MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                      : [        99998, ],
    'CountWeighted'                                              : [        99987,        99983,        99990, ],
    'CountWeightedLHEWeightScale'                                : [       110550,        99987,        90982,       110550,        99987,        90982,       110550,        99987,        90982, ],
    'CountWeightedL1PrefireNom'                                  : [        97124,        97123,        97127, ],
    'CountWeightedL1Prefire'                                     : [        97124,        96468,        97772, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       107364,        97124,        88385,       107364,        97124,        88385,       107364,        97124,        88385, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     434210862), # 434.21MB, avg file size 434.21MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                      : [        99999, ],
    'CountWeighted'                                              : [        99992,        99986,        99973, ],
    'CountWeightedLHEWeightScale'                                : [       111348,        99992,        90333,       111348,        99992,        90333,       111348,        99992,        90333, ],
    'CountWeightedL1PrefireNom'                                  : [        97048,        97043,        97030, ],
    'CountWeightedL1Prefire'                                     : [        97048,        96377,        97708, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       108057,        97048,        87686,       108057,        97048,        87686,       108057,        97048,        87686, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     431815013), # 431.82MB, avg file size 431.82MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                      : [       384000, ],
    'CountWeighted'                                              : [       380255,       380320,       380245, ],
    'CountWeightedL1PrefireNom'                                  : [       354415,       354445,       354416, ],
    'CountWeightedL1Prefire'                                     : [       354415,       348441,       360354, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1447725805), # 1.45GB, avg file size 1.45GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_1_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399942,       399959,       399993, ],
    'CountWeightedLHEWeightScale'                                : [       511981,       483258,       456284,       423838,       399942,       377566,       356938,       336759,       317859, ],
    'CountWeightedL1PrefireNom'                                  : [       387171,       387150,       387233, ],
    'CountWeightedL1Prefire'                                     : [       387171,       384148,       390140, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       495491,       467837,       441844,       410165,       387171,       365603,       345410,       325989,       307776, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1479030797), # 1.48GB, avg file size 1.48GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       388000, ],
    'CountWeighted'                                              : [       387883,       387857,       387846, ],
    'CountWeightedLHEWeightScale'                                : [       504101,       464442,       429582,       421280,       387870,       358651,       357634,       329170,       304204, ],
    'CountWeightedL1PrefireNom'                                  : [       374120,       374086,       374118, ],
    'CountWeightedL1Prefire'                                     : [       374120,       370939,       377263, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       486036,       447983,       414512,       406148,       374111,       346038,       344761,       317452,       293485, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     1553834528), # 1.55GB, avg file size 1.55GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399963,       399950,       399933, ],
    'CountWeightedLHEWeightScale'                                : [       512032,       483199,       456120,       423902,       399962,       377489,       357007,       336787,       317832, ],
    'CountWeightedL1PrefireNom'                                  : [       387087,       387056,       387079, ],
    'CountWeightedL1Prefire'                                     : [       387087,       384048,       390077, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       495417,       467659,       441568,       410132,       387086,       365433,       345399,       325936,       307672, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1481291517), # 1.48GB, avg file size 1.48GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       374000, ],
    'CountWeighted'                                              : [       373979,       373896,       373970, ],
    'CountWeightedLHEWeightScale'                                : [       476968,       452875,       429698,       393921,       373979,       354813,       331092,       314287,       298159, ],
    'CountWeightedL1PrefireNom'                                  : [       362280,       362196,       362302, ],
    'CountWeightedL1Prefire'                                     : [       362280,       359508,       365009, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       461934,       438717,       416366,       381496,       362280,       343795,       320640,       304450,       288897, ],
  }),
  ("nof_tree_events",                 374000),
  ("nof_db_events",                   374000),
  ("fsize_local",                     1354847794), # 1.35GB, avg file size 1.35GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399933,       399997,       399998, ],
    'CountWeightedLHEWeightScale'                                : [       519447,       478878,       443029,       433960,       399933,       369930,       368249,       339304,       313773, ],
    'CountWeightedL1PrefireNom'                                  : [       385684,       385692,       385761, ],
    'CountWeightedL1Prefire'                                     : [       385684,       382396,       388944, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       500795,       461833,       427386,       418357,       385684,       356848,       354994,       327199,       302667, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1602108344), # 1.60GB, avg file size 1.60GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       396000, ],
    'CountWeighted'                                              : [       395942,       396004,       395946, ],
    'CountWeightedLHEWeightScale'                                : [       504830,       479599,       455277,       416854,       395942,       375852,       350308,       332711,       315790, ],
    'CountWeightedL1PrefireNom'                                  : [       383656,       383677,       383674, ],
    'CountWeightedL1Prefire'                                     : [       383656,       380736,       386531, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       489039,       464719,       441253,       403803,       383656,       364267,       339332,       322372,       306049, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1432250067), # 1.43GB, avg file size 1.43GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       399996, ],
    'CountWeighted'                                              : [       399957,       399958,       399989, ],
    'CountWeightedLHEWeightScale'                                : [       512036,       483279,       456280,       423880,       399956,       377573,       356977,       336781,       317864, ],
    'CountWeightedL1PrefireNom'                                  : [       387740,       387732,       387761, ],
    'CountWeightedL1Prefire'                                     : [       387740,       384821,       390593, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       496246,       468527,       442477,       410790,       387738,       366133,       345939,       326473,       308222, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1528938021), # 1.53GB, avg file size 1.53GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                      : [       369992, ],
    'CountWeighted'                                              : [       369968,       369943,       369993, ],
    'CountWeightedLHEWeightScale'                                : [       480693,       442948,       409764,       401694,       369968,       342076,       340984,       313889,       290127, ],
    'CountWeightedL1PrefireNom'                                  : [       357229,       357207,       357256, ],
    'CountWeightedL1Prefire'                                     : [       357229,       354271,       360143, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       463984,       427751,       395869,       387693,       357229,       330441,       329069,       303063,       280236, ],
  }),
  ("nof_tree_events",                 369992),
  ("nof_db_events",                   369992),
  ("fsize_local",                     1506801170), # 1.51GB, avg file size 1.51GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                      : [       392996, ],
    'CountWeighted'                                              : [       392980,       393010,       392944, ],
    'CountWeightedLHEWeightScale'                                : [       503067,       474755,       448161,       416473,       392980,       370900,       350747,       330895,       312278, ],
    'CountWeightedL1PrefireNom'                                  : [       381002,       381017,       380974, ],
    'CountWeightedL1Prefire'                                     : [       381002,       378142,       383795, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       487612,       460308,       434636,       403664,       381002,       359693,       339946,       320802,       302830, ],
  }),
  ("nof_tree_events",                 392996),
  ("nof_db_events",                   392996),
  ("fsize_local",                     1506959706), # 1.51GB, avg file size 1.51GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       375989, ],
    'CountWeighted'                                              : [       375942,       375901,       375909, ],
    'CountWeightedLHEWeightScale'                                : [       479431,       455317,       432108,       395940,       375942,       356764,       332774,       315939,       299778, ],
    'CountWeightedL1PrefireNom'                                  : [       365002,       364947,       365006, ],
    'CountWeightedL1Prefire'                                     : [       365002,       362365,       367574, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       465358,       442073,       419642,       384304,       365002,       346457,       322984,       306730,       291111, ],
  }),
  ("nof_tree_events",                 375989),
  ("nof_db_events",                   375989),
  ("fsize_local",                     1411025733), # 1.41GB, avg file size 1.41GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       399994, ],
    'CountWeighted'                                              : [       399928,       399938,       399889, ],
    'CountWeightedLHEWeightScale'                                : [       512958,       482660,       454507,       425159,       399928,       376550,       358412,       337087,       317317, ],
    'CountWeightedL1PrefireNom'                                  : [       387537,       387522,       387535, ],
    'CountWeightedL1Prefire'                                     : [       387537,       384587,       390422, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       496921,       467719,       440557,       411848,       387537,       364973,       347173,       326622,       307552, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     1544270914), # 1.54GB, avg file size 1.54GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       399992, ],
    'CountWeighted'                                              : [       400013,       399948,       399905, ],
    'CountWeightedLHEWeightScale'                                : [       510237,       484218,       459264,       421483,       400013,       379293,       354315,       336163,       318785, ],
    'CountWeightedL1PrefireNom'                                  : [       388316,       388248,       388271, ],
    'CountWeightedL1Prefire'                                     : [       388316,       385505,       391061, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       495235,       470102,       445976,       409079,       388316,       368310,       343878,       326349,       309547, ],
  }),
  ("nof_tree_events",                 399992),
  ("nof_db_events",                   399992),
  ("fsize_local",                     1504311921), # 1.50GB, avg file size 1.50GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       384992, ],
    'CountWeighted'                                              : [       384886,       384940,       385032, ],
    'CountWeightedLHEWeightScale'                                : [       490972,       466188,       442349,       405487,       384886,       365248,       340810,       323516,       306930, ],
    'CountWeightedL1PrefireNom'                                  : [       373666,       373671,       373781, ],
    'CountWeightedL1Prefire'                                     : [       373666,       370968,       376305, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       476521,       452577,       429532,       393539,       373666,       354655,       330757,       314059,       298023, ],
  }),
  ("nof_tree_events",                 384992),
  ("nof_db_events",                   384992),
  ("fsize_local",                     1445359652), # 1.45GB, avg file size 1.45GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       399997, ],
    'CountWeighted'                                              : [       399974,       399963,       399921, ],
    'CountWeightedLHEWeightScale'                                : [       509945,       484427,       459849,       421076,       399974,       379627,       353863,       336076,       318965, ],
    'CountWeightedL1PrefireNom'                                  : [       388379,       388373,       388340, ],
    'CountWeightedL1Prefire'                                     : [       388379,       385589,       391100, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       495058,       470406,       446639,       408772,       388379,       368713,       343514,       326330,       309787, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1500310109), # 1.50GB, avg file size 1.50GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                      : [       399991, ],
    'CountWeighted'                                              : [       399961,       399951,       399947, ],
    'CountWeightedLHEWeightScale'                                : [       519447,       478882,       443042,       433949,       399961,       369936,       368235,       339304,       313771, ],
    'CountWeightedL1PrefireNom'                                  : [       386013,       385985,       386023, ],
    'CountWeightedL1Prefire'                                     : [       386013,       382775,       389207, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       501188,       462207,       427748,       418675,       386013,       357146,       355258,       327459,       302911, ],
  }),
  ("nof_tree_events",                 399991),
  ("nof_db_events",                   399991),
  ("fsize_local",                     1647373821), # 1.65GB, avg file size 1.65GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       399986, ],
    'CountWeighted'                                              : [       399978,       399962,       399916, ],
    'CountWeightedLHEWeightScale'                                : [       510080,       484326,       459553,       421272,       399978,       379461,       354086,       336115,       318871, ],
    'CountWeightedL1PrefireNom'                                  : [       388382,       388354,       388348, ],
    'CountWeightedL1Prefire'                                     : [       388382,       385589,       391106, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       495187,       470303,       446351,       408963,       388382,       368549,       343730,       326370,       309695, ],
  }),
  ("nof_tree_events",                 399986),
  ("nof_db_events",                   399986),
  ("fsize_local",                     1502106098), # 1.50GB, avg file size 1.50GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       395994, ],
    'CountWeighted'                                              : [       395967,       395891,       395945, ],
    'CountWeightedLHEWeightScale'                                : [       505351,       479294,       454333,       417546,       395966,       375321,       351069,       332890,       315506, ],
    'CountWeightedL1PrefireNom'                                  : [       384267,       384203,       384279, ],
    'CountWeightedL1Prefire'                                     : [       384267,       381461,       387012, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       490313,       465147,       441026,       405110,       384265,       364316,       340605,       323049,       306250, ],
  }),
  ("nof_tree_events",                 395994),
  ("nof_db_events",                   395994),
  ("fsize_local",                     1493274368), # 1.49GB, avg file size 1.49GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                      : [       399993, ],
    'CountWeighted'                                              : [       399942,       399938,       399955, ],
    'CountWeightedLHEWeightScale'                                : [       509953,       484408,       459807,       421095,       399942,       379603,       353883,       336069,       318948, ],
    'CountWeightedL1PrefireNom'                                  : [       388356,       388323,       388389, ],
    'CountWeightedL1Prefire'                                     : [       388356,       385564,       391082, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       495061,       470384,       446597,       408785,       388356,       368687,       343526,       326322,       309770, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     1500129362), # 1.50GB, avg file size 1.50GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_2v2t"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       379997, ],
    'CountWeighted'                                              : [       379966,       379896,       379950, ],
    'CountWeightedLHEWeightScale'                                : [       486419,       459096,       433444,       402671,       379964,       358677,       339121,       319925,       301956, ],
    'CountWeightedL1PrefireNom'                                  : [       368965,       368896,       368988, ],
    'CountWeightedL1Prefire'                                     : [       368965,       366313,       371547, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       472210,       445828,       421037,       390886,       368963,       348392,       329179,       310651,       293284, ],
  }),
  ("nof_tree_events",                 379997),
  ("nof_db_events",                   379997),
  ("fsize_local",                     1466377245), # 1.47GB, avg file size 1.47GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                      : [       399999, ],
    'CountWeighted'                                              : [       399957,       399890,       399849, ],
    'CountWeightedLHEWeightScale'                                : [       519677,       478803,       442872,       434290,       399957,       369739,       368675,       339331,       313603, ],
    'CountWeightedL1PrefireNom'                                  : [       386455,       386415,       386392, ],
    'CountWeightedL1Prefire'                                     : [       386455,       383315,       389540, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       501965,       462712,       428177,       419441,       386455,       357426,       356030,       327856,       303131, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1620843340), # 1.62GB, avg file size 1.62GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                      : [       382999, ],
    'CountWeighted'                                              : [       382919,       383001,       382989, ],
    'CountWeightedLHEWeightScale'                                : [       490277,       462670,       436736,       405893,       382919,       361453,       341838,       322477,       304324, ],
    'CountWeightedL1PrefireNom'                                  : [       371783,       371816,       371841, ],
    'CountWeightedL1Prefire'                                     : [       371783,       369099,       374399, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       475876,       449214,       424145,       393952,       371783,       351015,       331769,       313073,       295525, ],
  }),
  ("nof_tree_events",                 382999),
  ("nof_db_events",                   382999),
  ("fsize_local",                     1485918415), # 1.49GB, avg file size 1.49GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                      : [       391999, ],
    'CountWeighted'                                              : [       392007,       392044,       391910, ],
    'CountWeightedLHEWeightScale'                                : [       499820,       474721,       450576,       412762,       392007,       372002,       346907,       329397,       312568, ],
    'CountWeightedL1PrefireNom'                                  : [       381311,       381322,       381263, ],
    'CountWeightedL1Prefire'                                     : [       381311,       378704,       383836, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       486083,       461796,       438405,       401403,       381311,       361939,       337348,       320404,       304107, ],
  }),
  ("nof_tree_events",                 391999),
  ("nof_db_events",                   391999),
  ("fsize_local",                     1483114236), # 1.48GB, avg file size 1.48GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       399999, ],
    'CountWeighted'                                              : [       399899,       399933,       399930, ],
    'CountWeightedLHEWeightScale'                                : [       512975,       482670,       454491,       425171,       399899,       376546,       358426,       337102,       317320, ],
    'CountWeightedL1PrefireNom'                                  : [       387975,       387964,       388026, ],
    'CountWeightedL1Prefire'                                     : [       387975,       385111,       390771, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       497519,       468274,       441064,       412338,       387975,       365403,       347592,       327017,       307914, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1561627447), # 1.56GB, avg file size 1.56GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                      : [       396000, ],
    'CountWeighted'                                              : [       396039,       395941,       395939, ],
    'CountWeightedLHEWeightScale'                                : [       505184,       479426,       454702,       417308,       396032,       375534,       350806,       332836,       315619, ],
    'CountWeightedL1PrefireNom'                                  : [       385040,       384974,       384981, ],
    'CountWeightedL1Prefire'                                     : [       385040,       382365,       387629, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       491073,       466148,       442203,       405638,       385034,       365199,       340986,       323600,       306929, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1504531622), # 1.50GB, avg file size 1.50GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                      : [       400000, ],
    'CountWeighted'                                              : [       399896,       399971,       400048, ],
    'CountWeightedLHEWeightScale'                                : [       510130,       484349,       459583,       421311,       399896,       379486,       354113,       336147,       318893, ],
    'CountWeightedL1PrefireNom'                                  : [       388969,       388987,       389083, ],
    'CountWeightedL1Prefire'                                     : [       388969,       386298,       391559, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       496043,       471093,       447096,       409665,       388969,       369166,       344316,       326925,       310214, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1516484493), # 1.52GB, avg file size 1.52GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       395995, ],
    'CountWeighted'                                              : [       396046,       395934,       395999, ],
    'CountWeightedLHEWeightScale'                                : [       504859,       479597,       455260,       416884,       396046,       375842,       350342,       332727,       315789, ],
    'CountWeightedL1PrefireNom'                                  : [       385263,       385175,       385245, ],
    'CountWeightedL1Prefire'                                     : [       385263,       382633,       387809, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       491036,       466584,       443006,       405458,       385263,       365714,       340729,       323680,       307271, ],
  }),
  ("nof_tree_events",                 395995),
  ("nof_db_events",                   395995),
  ("fsize_local",                     1498751435), # 1.50GB, avg file size 1.50GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                      : [       399997, ],
    'CountWeighted'                                              : [       399940,       399878,       399909, ],
    'CountWeightedLHEWeightScale'                                : [       519409,       478831,       442995,       433929,       399940,       369907,       368229,       339285,       313755, ],
    'CountWeightedL1PrefireNom'                                  : [       386365,       386312,       386365, ],
    'CountWeightedL1Prefire'                                     : [       386365,       383196,       389477, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       501644,       462619,       428127,       419061,       386365,       357469,       355594,       327759,       303191, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1650062592), # 1.65GB, avg file size 1.65GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                      : [       391996, ],
    'CountWeighted'                                              : [       391945,       392052,       391874, ],
    'CountWeightedLHEWeightScale'                                : [       499933,       474656,       450354,       412905,       391934,       371873,       347050,       329415,       312498, ],
    'CountWeightedL1PrefireNom'                                  : [       381137,       381204,       381100, ],
    'CountWeightedL1Prefire'                                     : [       381137,       378514,       383692, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       486030,       461577,       438046,       401407,       381129,       361697,       337377,       320319,       303939, ],
  }),
  ("nof_tree_events",                 391996),
  ("nof_db_events",                   391996),
  ("fsize_local",                     1486700862), # 1.49GB, avg file size 1.49GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                      : [       399997, ],
    'CountWeighted'                                              : [       400011,       400004,       399939, ],
    'CountWeightedLHEWeightScale'                                : [       510460,       484148,       458940,       421771,       400003,       379123,       354621,       336253,       318701, ],
    'CountWeightedL1PrefireNom'                                  : [       388928,       388909,       388892, ],
    'CountWeightedL1Prefire'                                     : [       388928,       386229,       391540, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       496226,       470762,       446351,       409997,       388922,       368713,       344712,       326939,       309941, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1523170070), # 1.52GB, avg file size 1.52GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_4v"),
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
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                      : [       394000, ],
    'CountWeighted'                                              : [       393914,       393999,       393942, ],
    'CountWeightedLHEWeightScale'                                : [       502312,       477200,       452976,       414771,       393914,       373950,       348556,       331032,       314193, ],
    'CountWeightedL1PrefireNom'                                  : [       383178,       383231,       383198, ],
    'CountWeightedL1Prefire'                                     : [       383178,       380554,       385723, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                    : [       488490,       464182,       440721,       403345,       383178,       363822,       338942,       321988,       305675, ],
  }),
  ("nof_tree_events",                 394000),
  ("nof_db_events",                   394000),
  ("fsize_local",                     1490134520), # 1.49GB, avg file size 1.49GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2019Dec08_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4v"),
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

