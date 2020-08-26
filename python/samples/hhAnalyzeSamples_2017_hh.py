from collections import OrderedDict as OD

# file generated at 2020-08-24 20:02:31 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_hh.py -p python/samples/sampleLocations_2017_hh_multilepton.txt -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_hh.py -M

samples_2017 = OD()
samples_2017["/GluGluToRadionToHHTo4Tau_M-250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99957031e+05, 3.99953688e+05, 3.99928375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99957031e+05, 3.99957031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91753375e+05, 3.91738375e+05, 3.91746656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91753375e+05, 3.89637000e+05, 3.93799188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.91753375e+05, 3.91753375e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1429499835), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        20114964479), # 20.11GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99961438e+05, 3.99946344e+05, 3.99950031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06226969e+05, 3.99961438e+05, 3.91154312e+05, 4.06226969e+05, 3.99961438e+05, 3.91154312e+05, 4.06226969e+05, 3.99961438e+05, 3.91154312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06227031e+05, 3.91154188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91466938e+05, 3.91443594e+05, 3.91480688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91466938e+05, 3.89297375e+05, 3.93563812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.97544938e+05, 3.91466938e+05, 3.82896062e+05, 3.97544938e+05, 3.91466938e+05, 3.82896062e+05, 3.97544938e+05, 3.91466938e+05, 3.82896062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.97545000e+05, 3.82895938e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1437293231), # 1.44GB, avg file size 1.44GB
  ("fsize_db",                        19104985604), # 19.10GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 385000, ],
    'CountWeighted'                                                                  : [ 3.84993750e+05, 3.85057594e+05, 3.84965562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.92263188e+05, 3.84993750e+05, 3.75530156e+05, 3.92263188e+05, 3.84993750e+05, 3.75530156e+05, 3.92263188e+05, 3.84993750e+05, 3.75530156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.92263188e+05, 3.75530156e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.76402062e+05, 3.76428656e+05, 3.76390625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.76402062e+05, 3.74220438e+05, 3.78504656e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.83448656e+05, 3.76402062e+05, 3.67198688e+05, 3.83448656e+05, 3.76402062e+05, 3.67198688e+05, 3.83448656e+05, 3.76402062e+05, 3.67198688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.83448656e+05, 3.67198688e+05, ],
  }),
  ("nof_tree_events",                 385000),
  ("nof_db_events",                   385000),
  ("fsize_local",                     1402099938), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        18511645006), # 18.51GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00002250e+05, 3.99926938e+05, 3.99922531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00002250e+05, 4.00002250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.90729938e+05, 3.90657969e+05, 3.90687344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.90729938e+05, 3.88399594e+05, 3.92989812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.90729938e+05, 3.90729938e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1485019968), # 1.49GB, avg file size 1.49GB
  ("fsize_db",                        20219319064), # 20.22GB, avg file size 962.82MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00057781e+05, 2.99966938e+05, 3.00015094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08244250e+05, 3.00057781e+05, 2.90542875e+05, 3.08244250e+05, 3.00057781e+05, 2.90542875e+05, 3.08244250e+05, 3.00057781e+05, 2.90542875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08244250e+05, 2.90542875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92679156e+05, 2.92604406e+05, 2.92668125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92679156e+05, 2.90846750e+05, 2.94457625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.00635875e+05, 2.92679156e+05, 2.83460219e+05, 3.00635875e+05, 2.92679156e+05, 2.83460219e+05, 3.00635875e+05, 2.92679156e+05, 2.83460219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.00635875e+05, 2.83460219e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1131312058), # 1.13GB, avg file size 1.13GB
  ("fsize_db",                        14610494649), # 14.61GB, avg file size 859.44MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 284000, ],
    'CountWeighted'                                                                  : [ 2.83970438e+05, 2.83959250e+05, 2.83963875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.95331719e+05, 2.83970438e+05, 2.72299188e+05, 2.95331719e+05, 2.83970438e+05, 2.72299188e+05, 2.95331719e+05, 2.83970438e+05, 2.72299188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.95331719e+05, 2.72299188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.76080312e+05, 2.76070188e+05, 2.76078031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.76080312e+05, 2.74166875e+05, 2.77949250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.87068875e+05, 2.76080312e+05, 2.64774062e+05, 2.87068875e+05, 2.76080312e+05, 2.64774062e+05, 2.87068875e+05, 2.76080312e+05, 2.64774062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.87068875e+05, 2.64774062e+05, ],
  }),
  ("nof_tree_events",                 284000),
  ("nof_db_events",                   284000),
  ("fsize_local",                     1123577013), # 1.12GB, avg file size 1.12GB
  ("fsize_db",                        14267271177), # 14.27GB, avg file size 713.36MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99956062e+05, 3.00033688e+05, 2.99897688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15120312e+05, 2.99931344e+05, 2.85260031e+05, 3.15120312e+05, 2.99931344e+05, 2.85260031e+05, 3.15120312e+05, 2.99931344e+05, 2.85260031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15120312e+05, 2.85260031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91050375e+05, 2.91096750e+05, 2.91005719e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91050375e+05, 2.88914062e+05, 2.93143812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.05691750e+05, 2.91032938e+05, 2.76833500e+05, 3.05691750e+05, 2.91032938e+05, 2.76833500e+05, 3.05691750e+05, 2.91032938e+05, 2.76833500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.05691750e+05, 2.76833500e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1237729003), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        15112224162), # 15.11GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99869188e+05, 2.99990656e+05, 2.99933562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17756500e+05, 2.99869188e+05, 2.83230938e+05, 3.17756500e+05, 2.99869188e+05, 2.83230938e+05, 3.17756500e+05, 2.99869188e+05, 2.83230938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17756500e+05, 2.83230938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90399625e+05, 2.90460875e+05, 2.90451469e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90399625e+05, 2.88156688e+05, 2.92608094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.07626625e+05, 2.90399625e+05, 2.74311250e+05, 3.07626625e+05, 2.90399625e+05, 2.74311250e+05, 3.07626625e+05, 2.90399625e+05, 2.74311250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.07626625e+05, 2.74311250e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1282107768), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        15314286391), # 15.31GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99976188e+05, 1.99985062e+05, 1.99951828e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.13411406e+05, 1.99975797e+05, 1.87663062e+05, 2.13411406e+05, 1.99975797e+05, 1.87663062e+05, 2.13411406e+05, 1.99975797e+05, 1.87663062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.13411406e+05, 1.87662984e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93292469e+05, 1.93282797e+05, 1.93288906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93292469e+05, 1.91721219e+05, 1.94837500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.06223859e+05, 1.93291688e+05, 1.81419188e+05, 2.06223859e+05, 1.93291688e+05, 1.81419188e+05, 2.06223859e+05, 1.93291688e+05, 1.81419188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.06223875e+05, 1.81419125e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     881123312), # 881.12MB, avg file size 881.12MB
  ("fsize_db",                        10307241524), # 10.31GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 2.00003844e+05, 1.99925719e+05, 1.99958438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.14706484e+05, 2.00003375e+05, 1.86563125e+05, 2.14706484e+05, 2.00003375e+05, 1.86563125e+05, 2.14706484e+05, 2.00003375e+05, 1.86563125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.14706484e+05, 1.86563125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93005594e+05, 1.92956750e+05, 1.92971266e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93005594e+05, 1.91376734e+05, 1.94608969e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.07165891e+05, 1.93004234e+05, 1.80086281e+05, 2.07165891e+05, 1.93004234e+05, 1.80086281e+05, 2.07165891e+05, 1.93004234e+05, 1.80086281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.07165891e+05, 1.80086281e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     906855322), # 906.86MB, avg file size 906.86MB
  ("fsize_db",                        10435371711), # 10.44GB, avg file size 948.67MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99988156e+05, 1.99935125e+05, 2.00006656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15949203e+05, 1.99988156e+05, 1.85660000e+05, 2.15949203e+05, 1.99988156e+05, 1.85660000e+05, 2.15949203e+05, 1.99988156e+05, 1.85660000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15949203e+05, 1.85660000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92779031e+05, 1.92745266e+05, 1.92800969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92779031e+05, 1.91110969e+05, 1.94433688e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.08126688e+05, 1.92779031e+05, 1.79011344e+05, 2.08126688e+05, 1.92779031e+05, 1.79011344e+05, 2.08126688e+05, 1.92779031e+05, 1.79011344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.08126688e+05, 1.79011344e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     928090478), # 928.09MB, avg file size 928.09MB
  ("fsize_db",                        10556003606), # 10.56GB, avg file size 812.00MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99969578e+05, 1.99942344e+05, 1.99977375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17051531e+05, 1.99969578e+05, 1.84812906e+05, 2.17051531e+05, 1.99969578e+05, 1.84812906e+05, 2.17051531e+05, 1.99969578e+05, 1.84812906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17051531e+05, 1.84812906e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92693047e+05, 1.92676250e+05, 1.92697156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92693047e+05, 1.91008438e+05, 1.94356531e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09105688e+05, 1.92693047e+05, 1.78123000e+05, 2.09105688e+05, 1.92693047e+05, 1.78123000e+05, 2.09105688e+05, 1.92693047e+05, 1.78123000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09105688e+05, 1.78123000e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     947767551), # 947.77MB, avg file size 947.77MB
  ("fsize_db",                        10638007613), # 10.64GB, avg file size 709.20MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99992250e+05, 1.99943938e+05, 1.99941984e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18037719e+05, 1.99992250e+05, 1.84049938e+05, 2.18037719e+05, 1.99992250e+05, 1.84049938e+05, 2.18037719e+05, 1.99992250e+05, 1.84049938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18037734e+05, 1.84049922e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92485031e+05, 1.92428969e+05, 1.92478656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92485031e+05, 1.90761438e+05, 1.94192500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09814281e+05, 1.92485031e+05, 1.77188094e+05, 2.09814281e+05, 1.92485031e+05, 1.77188094e+05, 2.09814281e+05, 1.92485031e+05, 1.77188094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09814312e+05, 1.77188094e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     967715015), # 967.72MB, avg file size 967.72MB
  ("fsize_db",                        10705047349), # 10.71GB, avg file size 823.47MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99970875e+05, 1.99962328e+05, 1.99938578e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99970875e+05, 1.99970875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92279688e+05, 1.92263469e+05, 1.92259812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92279688e+05, 1.90512500e+05, 1.94022906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92279688e+05, 1.92279688e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     992480121), # 992.48MB, avg file size 992.48MB
  ("fsize_db",                        11200569052), # 11.20GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99963828e+05, 1.99952047e+05, 1.99986594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99963828e+05, 1.99963828e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92240906e+05, 1.92226234e+05, 1.92261062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92240906e+05, 1.90470438e+05, 1.93990406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92240906e+05, 1.92240906e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1008140850), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11266991203), # 11.27GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 192000, ],
    'CountWeighted'                                                                  : [ 1.91955125e+05, 1.91988688e+05, 1.91948766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91955125e+05, 1.91955125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.84439766e+05, 1.84463156e+05, 1.84428703e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.84439766e+05, 1.82721688e+05, 1.86140719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.84439766e+05, 1.84439766e+05, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     981459235), # 981.46MB, avg file size 981.46MB
  ("fsize_db",                        10933218336), # 10.93GB, avg file size 993.93MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99836094e+04, 9.99947656e+04, 1.00000039e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.10686578e+05, 9.99836094e+04, 9.08187266e+04, 1.10686578e+05, 9.99836094e+04, 9.08187266e+04, 1.10686578e+05, 9.99836094e+04, 9.08187266e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.10686578e+05, 9.08187266e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.60522109e+04, 9.60615703e+04, 9.60546406e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.60522109e+04, 9.51564141e+04, 9.69388203e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06304250e+05, 9.60522109e+04, 8.72628516e+04, 1.06304250e+05, 9.60522109e+04, 8.72628516e+04, 1.06304250e+05, 9.60522109e+04, 8.72628516e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06304250e+05, 8.72628516e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     514409988), # 514.41MB, avg file size 514.41MB
  ("fsize_db",                        5507575850), # 5.51GB, avg file size 917.93MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99722188e+04, 9.99884297e+04, 9.99862969e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11340117e+05, 9.99722188e+04, 9.03435859e+04, 1.11340117e+05, 9.99722188e+04, 9.03435859e+04, 1.11340117e+05, 9.99722188e+04, 9.03435859e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11340117e+05, 9.03435859e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.59610938e+04, 9.59567109e+04, 9.59825078e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.59610938e+04, 9.50512031e+04, 9.68641797e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06847047e+05, 9.59610938e+04, 8.67302969e+04, 1.06847047e+05, 9.59610938e+04, 8.67302969e+04, 1.06847047e+05, 9.59610938e+04, 8.67302969e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06847047e+05, 8.67302969e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     525161359), # 525.16MB, avg file size 525.16MB
  ("fsize_db",                        5537065038), # 5.54GB, avg file size 1.38GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 391000, ],
    'CountWeighted'                                                                  : [ 3.90962844e+05, 3.90985875e+05, 3.90868188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.95791062e+05, 3.90955656e+05, 3.83420562e+05, 3.95791062e+05, 3.90955656e+05, 3.83420562e+05, 3.95791062e+05, 3.90955656e+05, 3.83420562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95791062e+05, 3.83420562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.82617938e+05, 3.82603312e+05, 3.82577281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.82617938e+05, 3.80477281e+05, 3.84679375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.87281688e+05, 3.82611812e+05, 3.75274312e+05, 3.87281688e+05, 3.82611812e+05, 3.75274312e+05, 3.87281688e+05, 3.82611812e+05, 3.75274312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.87281688e+05, 3.75274312e+05, ],
  }),
  ("nof_tree_events",                 391000),
  ("nof_db_events",                   391000),
  ("fsize_local",                     1413132508), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        18879671024), # 18.88GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 386000, ],
    'CountWeighted'                                                                  : [ 3.85979688e+05, 3.85964312e+05, 3.86005156e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.92027375e+05, 3.85979688e+05, 3.77493000e+05, 3.92027375e+05, 3.85979688e+05, 3.77493000e+05, 3.92027375e+05, 3.85979688e+05, 3.77493000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.92027844e+05, 3.77492562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.77354938e+05, 3.77331312e+05, 3.77384375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.77354938e+05, 3.75171625e+05, 3.79469188e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.83207094e+05, 3.77354938e+05, 3.69099625e+05, 3.83207094e+05, 3.77354938e+05, 3.69099625e+05, 3.83207094e+05, 3.77354938e+05, 3.69099625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.83207562e+05, 3.69099156e+05, ],
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     1416664492), # 1.42GB, avg file size 1.42GB
  ("fsize_db",                        18925798715), # 18.93GB, avg file size 727.92MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 380000, ],
    'CountWeighted'                                                                  : [ 3.80032312e+05, 3.79991875e+05, 3.79941312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.87117250e+05, 3.80029219e+05, 3.70624625e+05, 3.87117250e+05, 3.80029219e+05, 3.70624625e+05, 3.87117250e+05, 3.80029219e+05, 3.70624625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.87117250e+05, 3.70624625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.71255500e+05, 3.71228688e+05, 3.71192062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.71255500e+05, 3.69052250e+05, 3.73386250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.78137344e+05, 3.71252312e+05, 3.62136312e+05, 3.78137344e+05, 3.71252312e+05, 3.62136312e+05, 3.78137344e+05, 3.71252312e+05, 3.62136312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.78137344e+05, 3.62136312e+05, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     1415233363), # 1.42GB, avg file size 1.42GB
  ("fsize_db",                        18931125504), # 18.93GB, avg file size 728.12MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99976000e+05, 4.00033406e+05, 3.99957875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.08711906e+05, 3.99973000e+05, 3.89181219e+05, 4.08711906e+05, 3.99973000e+05, 3.89181219e+05, 4.08711906e+05, 3.99973000e+05, 3.89181219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.08711969e+05, 3.89181125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.90461938e+05, 3.90496875e+05, 3.90445125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.90461938e+05, 3.88090969e+05, 3.92764562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98921719e+05, 3.90458500e+05, 3.79977844e+05, 3.98921719e+05, 3.90458500e+05, 3.79977844e+05, 3.98921719e+05, 3.90458500e+05, 3.79977844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.98921812e+05, 3.79977719e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1509110216), # 1.51GB, avg file size 1.51GB
  ("fsize_db",                        19706361148), # 19.71GB, avg file size 656.88MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00043125e+05, 4.00001656e+05, 3.99972938e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.11015062e+05, 4.00043125e+05, 3.87374500e+05, 4.11015062e+05, 4.00043125e+05, 3.87374500e+05, 4.11015062e+05, 4.00043125e+05, 3.87374500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.11016094e+05, 3.87373469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.89929875e+05, 3.89874906e+05, 3.89912438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.89929875e+05, 3.87440875e+05, 3.92349188e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.00569844e+05, 3.89929875e+05, 3.77663438e+05, 4.00569844e+05, 3.89929875e+05, 3.77663438e+05, 4.00569844e+05, 3.89929875e+05, 3.77663438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.00570875e+05, 3.77662406e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1546833892), # 1.55GB, avg file size 1.55GB
  ("fsize_db",                        20098276225), # 20.10GB, avg file size 773.01MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 298000, ],
    'CountWeighted'                                                                  : [ 2.97932844e+05, 2.97997906e+05, 2.97964906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.07751938e+05, 2.97932844e+05, 2.87342375e+05, 3.07751938e+05, 2.97932844e+05, 2.87342375e+05, 3.07751938e+05, 2.97932844e+05, 2.87342375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.07751938e+05, 2.87342375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90134812e+05, 2.90169125e+05, 2.90157781e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90134812e+05, 2.88238688e+05, 2.91996562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.99628375e+05, 2.90134812e+05, 2.79863344e+05, 2.99628375e+05, 2.90134812e+05, 2.79863344e+05, 2.99628375e+05, 2.90134812e+05, 2.79863344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.99628375e+05, 2.79863344e+05, ],
  }),
  ("nof_tree_events",                 298000),
  ("nof_db_events",                   298000),
  ("fsize_local",                     1179252726), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        15176832017), # 15.18GB, avg file size 758.84MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 384000, ],
    'CountWeighted'                                                                  : [ 3.83888188e+05, 3.83949375e+05, 3.84001312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.99338875e+05, 3.83888188e+05, 3.68141875e+05, 3.99338875e+05, 3.83888188e+05, 3.68141875e+05, 3.99338875e+05, 3.83888188e+05, 3.68141875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99338875e+05, 3.68141844e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.73339656e+05, 3.73356938e+05, 3.73423969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.73339656e+05, 3.70801906e+05, 3.75828125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.88250031e+05, 3.73339656e+05, 3.58073906e+05, 3.88250031e+05, 3.73339656e+05, 3.58073906e+05, 3.88250031e+05, 3.73339656e+05, 3.58073906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.88250031e+05, 3.58073844e+05, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1564940896), # 1.56GB, avg file size 1.56GB
  ("fsize_db",                        19349982170), # 19.35GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00007938e+05, 2.99973219e+05, 2.99999406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15125375e+05, 3.00007938e+05, 2.85252188e+05, 3.15125375e+05, 3.00007938e+05, 2.85252188e+05, 3.15125375e+05, 3.00007938e+05, 2.85252188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15125375e+05, 2.85252188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91273688e+05, 2.91249000e+05, 2.91265625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91273688e+05, 2.89207594e+05, 2.93306312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.05892906e+05, 2.91273688e+05, 2.77018156e+05, 3.05892906e+05, 2.91273688e+05, 2.77018156e+05, 3.05892906e+05, 2.91273688e+05, 2.77018156e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.05892906e+05, 2.77018156e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1278939126), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        15427844934), # 15.43GB, avg file size 857.10MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 280000, ],
    'CountWeighted'                                                                  : [ 2.79984938e+05, 2.80001312e+05, 2.79960344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.96615812e+05, 2.79984938e+05, 2.64337938e+05, 2.96615812e+05, 2.79984938e+05, 2.64337938e+05, 2.96615812e+05, 2.79984938e+05, 2.64337938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.96617344e+05, 2.64336375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.71534688e+05, 2.71532688e+05, 2.71524812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.71534688e+05, 2.69562219e+05, 2.73478000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.87593438e+05, 2.71534688e+05, 2.56420531e+05, 2.87593438e+05, 2.71534688e+05, 2.56420531e+05, 2.87593438e+05, 2.71534688e+05, 2.56420531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.87594938e+05, 2.56419062e+05, ],
  }),
  ("nof_tree_events",                 280000),
  ("nof_db_events",                   280000),
  ("fsize_local",                     1240222140), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        14667839164), # 14.67GB, avg file size 637.73MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 284000, ],
    'CountWeighted'                                                                  : [ 2.83953625e+05, 2.84019562e+05, 2.83902875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.03009719e+05, 2.83953625e+05, 2.66463125e+05, 3.03009719e+05, 2.83953625e+05, 2.66463125e+05, 3.03009719e+05, 2.83953625e+05, 2.66463125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.03009719e+05, 2.66463125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.75433000e+05, 2.75464875e+05, 2.75403969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.75433000e+05, 2.73447375e+05, 2.77393562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.93835656e+05, 2.75433000e+05, 2.58513000e+05, 2.93835656e+05, 2.75433000e+05, 2.58513000e+05, 2.93835656e+05, 2.75433000e+05, 2.58513000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.93835656e+05, 2.58513000e+05, ],
  }),
  ("nof_tree_events",                 284000),
  ("nof_db_events",                   284000),
  ("fsize_local",                     1298058672), # 1.30GB, avg file size 1.30GB
  ("fsize_db",                        15248320207), # 15.25GB, avg file size 693.11MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99979047e+05, 1.99978828e+05, 1.99969109e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.14731594e+05, 1.99978719e+05, 1.86604188e+05, 2.14731594e+05, 1.99978719e+05, 1.86604188e+05, 2.14731594e+05, 1.99978719e+05, 1.86604188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.14731594e+05, 1.86604188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93924625e+05, 1.93923156e+05, 1.93925719e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93924625e+05, 1.92525125e+05, 1.95308031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.08183812e+05, 1.93923656e+05, 1.80992781e+05, 2.08183812e+05, 1.93923656e+05, 1.80992781e+05, 2.08183812e+05, 1.93923656e+05, 1.80992781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.08183812e+05, 1.80992781e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     940503856), # 940.50MB, avg file size 940.50MB
  ("fsize_db",                        10729026481), # 10.73GB, avg file size 536.45MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 198000, ],
    'CountWeighted'                                                                  : [ 1.97981609e+05, 1.97967172e+05, 1.97985359e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.13791688e+05, 1.97981609e+05, 1.83808391e+05, 2.13791688e+05, 1.97981609e+05, 1.83808391e+05, 2.13791688e+05, 1.97981609e+05, 1.83808391e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.13792000e+05, 1.83808094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.91926359e+05, 1.91909062e+05, 1.91940438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.91926359e+05, 1.90530609e+05, 1.93304031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.07208406e+05, 1.91926359e+05, 1.78222672e+05, 2.07208406e+05, 1.91926359e+05, 1.78222672e+05, 2.07208406e+05, 1.91926359e+05, 1.78222672e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.07208516e+05, 1.78222547e+05, ],
  }),
  ("nof_tree_events",                 198000),
  ("nof_db_events",                   198000),
  ("fsize_local",                     953765545), # 953.77MB, avg file size 953.77MB
  ("fsize_db",                        10881260447), # 10.88GB, avg file size 604.51MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99964719e+05, 1.99944688e+05, 1.99943500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17056844e+05, 1.99961594e+05, 1.84835844e+05, 2.17056844e+05, 1.99961594e+05, 1.84835844e+05, 2.17056844e+05, 1.99961594e+05, 1.84835844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17056844e+05, 1.84835844e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93894078e+05, 1.93868078e+05, 1.93892562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93894078e+05, 1.92494125e+05, 1.95275938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.10416156e+05, 1.93891484e+05, 1.79252781e+05, 2.10416156e+05, 1.93891484e+05, 1.79252781e+05, 2.10416156e+05, 1.93891484e+05, 1.79252781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.10416156e+05, 1.79252781e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     985593348), # 985.59MB, avg file size 985.59MB
  ("fsize_db",                        10995288880), # 11.00GB, avg file size 610.85MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 189000, ],
    'CountWeighted'                                                                  : [ 1.88975141e+05, 1.88986000e+05, 1.88967688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.06028094e+05, 1.88975141e+05, 1.73935875e+05, 2.06028094e+05, 1.88975141e+05, 1.73935875e+05, 2.06028094e+05, 1.88975141e+05, 1.73935875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.06028094e+05, 1.73935875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.83333484e+05, 1.83320125e+05, 1.83348750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.83333484e+05, 1.82034422e+05, 1.84612875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.99843250e+05, 1.83333484e+05, 1.68773859e+05, 1.99843250e+05, 1.83333484e+05, 1.68773859e+05, 1.99843250e+05, 1.83333484e+05, 1.68773859e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.99843250e+05, 1.68773859e+05, ],
  }),
  ("nof_tree_events",                 189000),
  ("nof_db_events",                   189000),
  ("fsize_local",                     951669407), # 951.67MB, avg file size 951.67MB
  ("fsize_db",                        10562893577), # 10.56GB, avg file size 528.14MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 196000, ],
    'CountWeighted'                                                                  : [ 1.95958031e+05, 1.95984500e+05, 1.96001188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.14575156e+05, 1.95958031e+05, 1.79692328e+05, 2.14575156e+05, 1.95958031e+05, 1.79692328e+05, 2.14575156e+05, 1.95958031e+05, 1.79692328e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.14575172e+05, 1.79692328e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.90102266e+05, 1.90107516e+05, 1.90150438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.90102266e+05, 1.88758375e+05, 1.91429156e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.08116938e+05, 1.90102266e+05, 1.74353406e+05, 2.08116938e+05, 1.90102266e+05, 1.74353406e+05, 2.08116938e+05, 1.90102266e+05, 1.74353406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.08116938e+05, 1.74353406e+05, ],
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     1004924679), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        11128480225), # 11.13GB, avg file size 428.02MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99965719e+05, 1.99928156e+05, 1.99990375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19780531e+05, 1.99965719e+05, 1.82751938e+05, 2.19780531e+05, 1.99965719e+05, 1.82751938e+05, 2.19780531e+05, 1.99965719e+05, 1.82751938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.19780531e+05, 1.82751938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94027812e+05, 1.93987719e+05, 1.94056266e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94027812e+05, 1.92666906e+05, 1.95372234e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.13219281e+05, 1.94027812e+05, 1.77350969e+05, 2.13219281e+05, 1.94027812e+05, 1.77350969e+05, 2.13219281e+05, 1.94027812e+05, 1.77350969e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.13219281e+05, 1.77350969e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1039059094), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11297900227), # 11.30GB, avg file size 470.75MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 194000, ],
    'CountWeighted'                                                                  : [ 1.93918844e+05, 1.93958672e+05, 1.93975812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.93918844e+05, 1.93918844e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.88167094e+05, 1.88178250e+05, 1.88226422e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.88167094e+05, 1.86847312e+05, 1.89469266e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.88167094e+05, 1.88167094e+05, ],
  }),
  ("nof_tree_events",                 194000),
  ("nof_db_events",                   194000),
  ("fsize_local",                     1027807435), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        11268378526), # 11.27GB, avg file size 704.27MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99836953e+04, 9.99772734e+04, 1.00000344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.10544883e+05, 9.99836953e+04, 9.09752734e+04, 1.10544883e+05, 9.99836953e+04, 9.09752734e+04, 1.10544883e+05, 9.99836953e+04, 9.09752734e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.10544883e+05, 9.09752734e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71493984e+04, 9.71368906e+04, 9.71694922e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71493984e+04, 9.64993984e+04, 9.77905547e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.07391797e+05, 9.71493984e+04, 8.84047344e+04, 1.07391797e+05, 9.71493984e+04, 8.84047344e+04, 1.07391797e+05, 9.71493984e+04, 8.84047344e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.07391797e+05, 8.84047344e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     534192407), # 534.19MB, avg file size 534.19MB
  ("fsize_db",                        5743750248), # 5.74GB, avg file size 441.83MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99550312e+04, 9.99787344e+04, 9.99576953e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11321031e+05, 9.99550312e+04, 9.03187578e+04, 1.11321031e+05, 9.99550312e+04, 9.03187578e+04, 1.11321031e+05, 9.99550312e+04, 9.03187578e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11321031e+05, 9.03187578e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70344531e+04, 9.70459062e+04, 9.70435703e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70344531e+04, 9.63676641e+04, 9.76921953e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.08055273e+05, 9.70344531e+04, 8.76862812e+04, 1.08055273e+05, 9.70344531e+04, 8.76862812e+04, 1.08055273e+05, 9.70344531e+04, 8.76862812e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.08055273e+05, 8.76862812e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     543620853), # 543.62MB, avg file size 543.62MB
  ("fsize_db",                        5923175401), # 5.92GB, avg file size 311.75MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99912000e+05, 3.99995125e+05, 4.00008938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99912000e+05, 3.99912000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92663000e+05, 3.92701000e+05, 3.92743938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92663000e+05, 3.90757625e+05, 3.94479562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.92663000e+05, 3.92663000e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1451360323), # 1.45GB, avg file size 1.45GB
  ("fsize_db",                        20344351713), # 20.34GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399993, ],
    'CountWeighted'                                                                  : [ 3.99926344e+05, 3.99979688e+05, 4.00061688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06243688e+05, 3.99925500e+05, 3.91187094e+05, 4.06243688e+05, 3.99925500e+05, 3.91187094e+05, 4.06243688e+05, 3.99925500e+05, 3.91187094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06243688e+05, 3.91187094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92304844e+05, 3.92323250e+05, 3.92408219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92304844e+05, 3.90314562e+05, 3.94197062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98436688e+05, 3.92302938e+05, 3.83746125e+05, 3.98436688e+05, 3.92302938e+05, 3.83746125e+05, 3.98436688e+05, 3.92302938e+05, 3.83746125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.98436688e+05, 3.83746125e+05, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     1463903886), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        19527920598), # 19.53GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 4.00039531e+05, 3.99917531e+05, 3.99979219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07500875e+05, 4.00039531e+05, 3.90165938e+05, 4.07500875e+05, 4.00039531e+05, 3.90165938e+05, 4.07500875e+05, 4.00039531e+05, 3.90165938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07500875e+05, 3.90165938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92092938e+05, 3.91998062e+05, 3.92056219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92092938e+05, 3.90041312e+05, 3.94043969e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.99373406e+05, 3.92092938e+05, 3.82468688e+05, 3.99373406e+05, 3.92092938e+05, 3.82468688e+05, 3.99373406e+05, 3.92092938e+05, 3.82468688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.99373406e+05, 3.82468688e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1483238971), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        19473148919), # 19.47GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 379996, ],
    'CountWeighted'                                                                  : [ 3.80026812e+05, 3.79978250e+05, 3.80015938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.80026812e+05, 3.80026812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.72179250e+05, 3.72139312e+05, 3.72174375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.72179250e+05, 3.70166906e+05, 3.74100531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.72179250e+05, 3.72179250e+05, ],
  }),
  ("nof_tree_events",                 379996),
  ("nof_db_events",                   379996),
  ("fsize_local",                     1443317478), # 1.44GB, avg file size 1.44GB
  ("fsize_db",                        19590423166), # 19.59GB, avg file size 725.57MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299994, ],
    'CountWeighted'                                                                  : [ 2.99947469e+05, 2.99958469e+05, 2.99956000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08253906e+05, 2.99947062e+05, 2.90539812e+05, 3.08253906e+05, 2.99947062e+05, 2.90539812e+05, 3.08253906e+05, 2.99947062e+05, 2.90539812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08253906e+05, 2.90539812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93250594e+05, 2.93245312e+05, 2.93265250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93250594e+05, 2.91556188e+05, 2.94881250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.01313750e+05, 2.93249312e+05, 2.84074375e+05, 3.01313750e+05, 2.93249312e+05, 2.84074375e+05, 3.01313750e+05, 2.93249312e+05, 2.84074375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.01313750e+05, 2.84074375e+05, ],
  }),
  ("nof_tree_events",                 299994),
  ("nof_db_events",                   299994),
  ("fsize_local",                     1164639721), # 1.16GB, avg file size 1.16GB
  ("fsize_db",                        14916149163), # 14.92GB, avg file size 828.67MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99972750e+05, 2.99989969e+05, 3.00038531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09807000e+05, 2.99972625e+05, 2.89291938e+05, 3.09807000e+05, 2.99972625e+05, 2.89291938e+05, 3.09807000e+05, 2.99972625e+05, 2.89291938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09807000e+05, 2.89291938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92946594e+05, 2.92944781e+05, 2.93008688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92946594e+05, 2.91185625e+05, 2.94643500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.02505469e+05, 2.92945250e+05, 2.82553375e+05, 3.02505469e+05, 2.92945250e+05, 2.82553375e+05, 3.02505469e+05, 2.92945250e+05, 2.82553375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.02505469e+05, 2.82553375e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1192106413), # 1.19GB, avg file size 1.19GB
  ("fsize_db",                        14997791200), # 15.00GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299990, ],
    'CountWeighted'                                                                  : [ 3.00014938e+05, 2.99997125e+05, 3.00031344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11942438e+05, 3.00013188e+05, 2.87615531e+05, 3.11942438e+05, 3.00013188e+05, 2.87615531e+05, 3.11942438e+05, 3.00013188e+05, 2.87615531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11942438e+05, 2.87615531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92395750e+05, 2.92362625e+05, 2.92428344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92395750e+05, 2.90515312e+05, 2.94218844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.03991562e+05, 2.92392938e+05, 2.80368094e+05, 3.03991562e+05, 2.92392938e+05, 2.80368094e+05, 3.03991562e+05, 2.92392938e+05, 2.80368094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.03991562e+05, 2.80368094e+05, ],
  }),
  ("nof_tree_events",                 299990),
  ("nof_db_events",                   299990),
  ("fsize_local",                     1236136314), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        15235183188), # 15.24GB, avg file size 952.20MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 286992, ],
    'CountWeighted'                                                                  : [ 2.86998156e+05, 2.87037562e+05, 2.86973531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.01485281e+05, 2.86998156e+05, 2.72878688e+05, 3.01485281e+05, 2.86998156e+05, 2.72878688e+05, 3.01485281e+05, 2.86998156e+05, 2.72878688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.01485281e+05, 2.72878688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.78904375e+05, 2.78920094e+05, 2.78890250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.78904375e+05, 2.76940250e+05, 2.80814938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.92930938e+05, 2.78904375e+05, 2.65235906e+05, 2.92930938e+05, 2.78904375e+05, 2.65235906e+05, 2.92930938e+05, 2.78904375e+05, 2.65235906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.92930938e+05, 2.65235906e+05, ],
  }),
  ("nof_tree_events",                 286992),
  ("nof_db_events",                   286992),
  ("fsize_local",                     1242967949), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        14884438376), # 14.88GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 291993, ],
    'CountWeighted'                                                                  : [ 2.91964250e+05, 2.91937750e+05, 2.91926844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09261969e+05, 2.91964250e+05, 2.75698125e+05, 3.09261969e+05, 2.91964250e+05, 2.75698125e+05, 3.09261969e+05, 2.91964250e+05, 2.75698125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09261969e+05, 2.75698125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.83177281e+05, 2.83150188e+05, 2.83158156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.83177281e+05, 2.81068875e+05, 2.85234469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.99898094e+05, 2.83177281e+05, 2.67443781e+05, 2.99898094e+05, 2.83177281e+05, 2.67443781e+05, 2.99898094e+05, 2.83177281e+05, 2.67443781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.99898094e+05, 2.67443781e+05, ],
  }),
  ("nof_tree_events",                 291993),
  ("nof_db_events",                   291993),
  ("fsize_local",                     1317996151), # 1.32GB, avg file size 1.32GB
  ("fsize_db",                        15416817462), # 15.42GB, avg file size 906.87MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 269995, ],
    'CountWeighted'                                                                  : [ 2.69945250e+05, 2.69994406e+05, 2.69968594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.88081438e+05, 2.69945250e+05, 2.53320172e+05, 2.88081438e+05, 2.69945250e+05, 2.53320172e+05, 2.88081438e+05, 2.69945250e+05, 2.53320172e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.88081438e+05, 2.53320172e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.61382625e+05, 2.61398500e+05, 2.61410719e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.61382625e+05, 2.59349578e+05, 2.63379375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.78870125e+05, 2.61382625e+05, 2.45321594e+05, 2.78870125e+05, 2.61382625e+05, 2.45321594e+05, 2.78870125e+05, 2.61382625e+05, 2.45321594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.78870125e+05, 2.45321594e+05, ],
  }),
  ("nof_tree_events",                 269995),
  ("nof_db_events",                   269995),
  ("fsize_local",                     1261881216), # 1.26GB, avg file size 1.26GB
  ("fsize_db",                        14437624405), # 14.44GB, avg file size 802.09MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99951094e+05, 2.99985406e+05, 2.99982531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22112562e+05, 2.99951094e+05, 2.79890469e+05, 3.22112562e+05, 2.99951094e+05, 2.79890469e+05, 3.22112562e+05, 2.99951094e+05, 2.79890469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22112562e+05, 2.79890469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.89898500e+05, 2.89907812e+05, 2.89935312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.89898500e+05, 2.87535312e+05, 2.92224406e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.11241312e+05, 2.89898500e+05, 2.70556188e+05, 3.11241312e+05, 2.89898500e+05, 2.70556188e+05, 3.11241312e+05, 2.89898500e+05, 2.70556188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.11241312e+05, 2.70556188e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1441159698), # 1.44GB, avg file size 1.44GB
  ("fsize_db",                        16219407866), # 16.22GB, avg file size 954.08MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 195995, ],
    'CountWeighted'                                                                  : [ 1.95994000e+05, 1.95979547e+05, 1.95931578e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.11660203e+05, 1.95994000e+05, 1.81972750e+05, 2.11660203e+05, 1.95994000e+05, 1.81972750e+05, 2.11660203e+05, 1.95994000e+05, 1.81972750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.11660219e+05, 1.81972750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.89210656e+05, 1.89191031e+05, 1.89175781e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.89210656e+05, 1.87627969e+05, 1.90768297e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.04286344e+05, 1.89210656e+05, 1.75706109e+05, 2.04286344e+05, 1.89210656e+05, 1.75706109e+05, 2.04286344e+05, 1.89210656e+05, 1.75706109e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.04286344e+05, 1.75706109e+05, ],
  }),
  ("nof_tree_events",                 195995),
  ("nof_db_events",                   195995),
  ("fsize_local",                     963879095), # 963.88MB, avg file size 963.88MB
  ("fsize_db",                        10725957373), # 10.73GB, avg file size 893.83MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199995, ],
    'CountWeighted'                                                                  : [ 1.99976344e+05, 2.00016688e+05, 1.99985531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17031484e+05, 1.99976344e+05, 1.84826344e+05, 2.17031484e+05, 1.99976344e+05, 1.84826344e+05, 2.17031484e+05, 1.99976344e+05, 1.84826344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17031719e+05, 1.84826125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92824484e+05, 1.92849969e+05, 1.92825672e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92824484e+05, 1.91161750e+05, 1.94464984e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09228344e+05, 1.92824484e+05, 1.78251812e+05, 2.09228344e+05, 1.92824484e+05, 1.78251812e+05, 2.09228344e+05, 1.92824484e+05, 1.78251812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09228562e+05, 1.78251594e+05, ],
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     1002437920), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        11039880992), # 11.04GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 191997, ],
    'CountWeighted'                                                                  : [ 1.91969297e+05, 1.91984438e+05, 1.92001656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.09335125e+05, 1.91969297e+05, 1.76706250e+05, 2.09335125e+05, 1.91969297e+05, 1.76706250e+05, 2.09335125e+05, 1.91969297e+05, 1.76706250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.09335125e+05, 1.76706250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.84877406e+05, 1.84869562e+05, 1.84914859e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.84877406e+05, 1.83239000e+05, 1.86497469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.01547703e+05, 1.84877406e+05, 1.70209656e+05, 2.01547703e+05, 1.84877406e+05, 1.70209656e+05, 2.01547703e+05, 1.84877406e+05, 1.70209656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.01547703e+05, 1.70209656e+05, ],
  }),
  ("nof_tree_events",                 191997),
  ("nof_db_events",                   191997),
  ("fsize_local",                     977587834), # 977.59MB, avg file size 977.59MB
  ("fsize_db",                        10772500407), # 10.77GB, avg file size 769.46MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99936969e+05, 1.99943109e+05, 1.99980734e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99936969e+05, 1.99936969e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92514000e+05, 1.92494266e+05, 1.92559656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92514000e+05, 1.90802734e+05, 1.94206000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92514000e+05, 1.92514000e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1036377761), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11660934047), # 11.66GB, avg file size 832.92MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 2.00007594e+05, 1.99962828e+05, 1.99958219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.00007594e+05, 2.00007594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92410812e+05, 1.92369406e+05, 1.92385047e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92410812e+05, 1.90669219e+05, 1.94133172e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92410812e+05, 1.92410812e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1047112930), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        11774979133), # 11.77GB, avg file size 692.65MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 191996, ],
    'CountWeighted'                                                                  : [ 1.91963000e+05, 1.91965609e+05, 1.91969500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91963000e+05, 1.91963000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.84557125e+05, 1.84544500e+05, 1.84574828e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.84557125e+05, 1.82858828e+05, 1.86236328e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.84557125e+05, 1.84557125e+05, ],
  }),
  ("nof_tree_events",                 191996),
  ("nof_db_events",                   191996),
  ("fsize_local",                     1014986486), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11335819766), # 11.34GB, avg file size 944.65MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99948734e+05, 1.99993344e+05, 1.99967297e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.21318812e+05, 1.99948734e+05, 1.81636281e+05, 2.21318812e+05, 1.99948734e+05, 1.81636281e+05, 2.21318812e+05, 1.99948734e+05, 1.81636281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21318906e+05, 1.81636219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92072969e+05, 1.92093453e+05, 1.92098969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92072969e+05, 1.90277375e+05, 1.93851703e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.12549969e+05, 1.92072969e+05, 1.74511219e+05, 2.12549969e+05, 1.92072969e+05, 1.74511219e+05, 2.12549969e+05, 1.92072969e+05, 1.74511219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.12550031e+05, 1.74511125e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1057921703), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        11421628490), # 11.42GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99807578e+04, 9.99730234e+04, 9.99710078e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11335477e+05, 9.99807578e+04, 9.03286953e+04, 1.11335477e+05, 9.99807578e+04, 9.03286953e+04, 1.11335477e+05, 9.99807578e+04, 9.03286953e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11335477e+05, 9.03286953e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.59499062e+04, 9.59401328e+04, 9.59501406e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.59499062e+04, 9.50349609e+04, 9.68552734e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06826461e+05, 9.59499062e+04, 8.67055312e+04, 1.06826461e+05, 9.59499062e+04, 8.67055312e+04, 1.06826461e+05, 9.59499062e+04, 8.67055312e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06826461e+05, 8.67055312e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     536584086), # 536.58MB, avg file size 536.58MB
  ("fsize_db",                        5783738671), # 5.78GB, avg file size 826.25MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 394995, ],
    'CountWeighted'                                                                  : [ 3.94970543e+05, 3.94982699e+05, 3.94986055e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.99821884e+05, 3.94970543e+05, 3.87347695e+05, 3.99821884e+05, 3.94970543e+05, 3.87347695e+05, 3.99821884e+05, 3.94970543e+05, 3.87347695e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99821884e+05, 3.87347695e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87384950e+05, 3.87371970e+05, 3.87405163e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87384950e+05, 3.85410941e+05, 3.89256848e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.92098971e+05, 3.87384950e+05, 3.79939293e+05, 3.92098971e+05, 3.87384950e+05, 3.79939293e+05, 3.92098971e+05, 3.87384950e+05, 3.79939293e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.92098971e+05, 3.79939293e+05, ],
  }),
  ("nof_tree_events",                 394995),
  ("nof_db_events",                   394995),
  ("fsize_local",                     1449930522), # 1.45GB, avg file size 724.97MB
  ("fsize_db",                        19490651554), # 19.49GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 395995, ],
    'CountWeighted'                                                                  : [ 3.96046062e+05, 3.95973562e+05, 3.95918531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.02169000e+05, 3.96042031e+05, 3.87238812e+05, 4.02169000e+05, 3.96042031e+05, 3.87238812e+05, 4.02169000e+05, 3.96042031e+05, 3.87238812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.02169000e+05, 3.87238812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88066938e+05, 3.87999938e+05, 3.87991094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88066938e+05, 3.86014719e+05, 3.90016812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.94042500e+05, 3.88062688e+05, 3.79496562e+05, 3.94042500e+05, 3.88062688e+05, 3.79496562e+05, 3.94042500e+05, 3.88062688e+05, 3.79496562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.94042500e+05, 3.79496562e+05, ],
  }),
  ("nof_tree_events",                 395995),
  ("nof_db_events",                   395995),
  ("fsize_local",                     1478302719), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        19808318644), # 19.81GB, avg file size 943.25MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.99985469e+05, 4.00019625e+05, 3.99915250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07519344e+05, 3.99978031e+05, 3.90123625e+05, 4.07519344e+05, 3.99978031e+05, 3.90123625e+05, 4.07519344e+05, 3.99978031e+05, 3.90123625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07519344e+05, 3.90123625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91644625e+05, 3.91668969e+05, 3.91579312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91644625e+05, 3.89514500e+05, 3.93681938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98969906e+05, 3.91637938e+05, 3.82033969e+05, 3.98969906e+05, 3.91637938e+05, 3.82033969e+05, 3.98969906e+05, 3.91637938e+05, 3.82033969e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.98969906e+05, 3.82033969e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1522310632), # 1.52GB, avg file size 1.52GB
  ("fsize_db",                        19945565524), # 19.95GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 394995, ],
    'CountWeighted'                                                                  : [ 3.94911812e+05, 3.94998844e+05, 3.94962500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.03595000e+05, 3.94911812e+05, 3.84344531e+05, 4.03595000e+05, 3.94911812e+05, 3.84344531e+05, 4.03595000e+05, 3.94911812e+05, 3.84344531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.03595000e+05, 3.84344531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.86437094e+05, 3.86489719e+05, 3.86490938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.86437094e+05, 3.84286750e+05, 3.88510500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.94863812e+05, 3.86437094e+05, 3.76119000e+05, 3.94863812e+05, 3.86437094e+05, 3.76119000e+05, 3.94863812e+05, 3.86437094e+05, 3.76119000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.94863812e+05, 3.76119000e+05, ],
  }),
  ("nof_tree_events",                 394995),
  ("nof_db_events",                   394995),
  ("fsize_local",                     1527631171), # 1.53GB, avg file size 1.53GB
  ("fsize_db",                        19924344376), # 19.92GB, avg file size 830.18MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299995, ],
    'CountWeighted'                                                                  : [ 2.99902094e+05, 2.99974719e+05, 2.99951500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08265688e+05, 2.99902094e+05, 2.90533625e+05, 3.08265688e+05, 2.99902094e+05, 2.90533625e+05, 3.08265688e+05, 2.99902094e+05, 2.90533625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08265688e+05, 2.90533625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92983938e+05, 2.93012500e+05, 2.93032219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92983938e+05, 2.91248000e+05, 2.94661438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.01080750e+05, 2.92983938e+05, 2.83845406e+05, 3.01080750e+05, 2.92983938e+05, 2.83845406e+05, 3.01080750e+05, 2.92983938e+05, 2.83845406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.01080750e+05, 2.83845406e+05, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1196794744), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        15226334046), # 15.23GB, avg file size 761.32MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 284992, ],
    'CountWeighted'                                                                  : [ 2.85007656e+05, 2.85000000e+05, 2.84948562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.94338250e+05, 2.85006250e+05, 2.74835156e+05, 2.94338250e+05, 2.85006250e+05, 2.74835156e+05, 2.94338250e+05, 2.85006250e+05, 2.74835156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.94338250e+05, 2.74835125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.78087031e+05, 2.78071469e+05, 2.78056656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.78087031e+05, 2.76376188e+05, 2.79742781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.87148500e+05, 2.78084938e+05, 2.68209688e+05, 2.87148500e+05, 2.78084938e+05, 2.68209688e+05, 2.87148500e+05, 2.78084938e+05, 2.68209688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.87148500e+05, 2.68209656e+05, ],
  }),
  ("nof_tree_events",                 284992),
  ("nof_db_events",                   284992),
  ("fsize_local",                     1169663491), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        14565597893), # 14.57GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299995, ],
    'CountWeighted'                                                                  : [ 2.99937562e+05, 2.99881344e+05, 3.00032750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11973625e+05, 2.99937562e+05, 2.87601406e+05, 3.11973625e+05, 2.99937562e+05, 2.87601406e+05, 3.11973625e+05, 2.99937562e+05, 2.87601406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11973625e+05, 2.87601406e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92221125e+05, 2.92175062e+05, 2.92293812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92221125e+05, 2.90340656e+05, 2.94059312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.03879875e+05, 2.92221125e+05, 2.80244750e+05, 3.03879875e+05, 2.92221125e+05, 2.80244750e+05, 3.03879875e+05, 2.92221125e+05, 2.80244750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.03879875e+05, 2.80244750e+05, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1281596561), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        15709690748), # 15.71GB, avg file size 924.10MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 289998, ],
    'CountWeighted'                                                                  : [ 2.89995812e+05, 2.89956625e+05, 2.89965594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.04610969e+05, 2.89995812e+05, 2.75747344e+05, 3.04610969e+05, 2.89995812e+05, 2.75747344e+05, 3.04610969e+05, 2.89995812e+05, 2.75747344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.04610969e+05, 2.75747344e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.81938625e+05, 2.81907938e+05, 2.81924312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.81938625e+05, 2.80012000e+05, 2.83823875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.96093188e+05, 2.81938625e+05, 2.68143875e+05, 2.96093188e+05, 2.81938625e+05, 2.68143875e+05, 2.96093188e+05, 2.81938625e+05, 2.68143875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.96093188e+05, 2.68143875e+05, ],
  }),
  ("nof_tree_events",                 289998),
  ("nof_db_events",                   289998),
  ("fsize_local",                     1306300429), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        15476703995), # 15.48GB, avg file size 1.11GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 279993, ],
    'CountWeighted'                                                                  : [ 2.79968375e+05, 2.79990500e+05, 2.79973250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.96578844e+05, 2.79968375e+05, 2.64335062e+05, 2.96578844e+05, 2.79968375e+05, 2.64335062e+05, 2.96578844e+05, 2.79968375e+05, 2.64335062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.96578844e+05, 2.64335062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.71965062e+05, 2.71968562e+05, 2.71975375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.71965062e+05, 2.70068438e+05, 2.73824281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.88036625e+05, 2.71965062e+05, 2.56832578e+05, 2.88036625e+05, 2.71965062e+05, 2.56832578e+05, 2.88036625e+05, 2.71965062e+05, 2.56832578e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.88036625e+05, 2.56832578e+05, ],
  }),
  ("nof_tree_events",                 279993),
  ("nof_db_events",                   279993),
  ("fsize_local",                     1316582992), # 1.32GB, avg file size 1.32GB
  ("fsize_db",                        15200236312), # 15.20GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99961703e+05, 1.99953672e+05, 2.00027188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.13367812e+05, 1.99961703e+05, 1.87663609e+05, 2.13367812e+05, 1.99961703e+05, 1.87663609e+05, 2.13367812e+05, 1.99961703e+05, 1.87663609e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.13367922e+05, 1.87663484e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94020547e+05, 1.94013953e+05, 1.94066562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94020547e+05, 1.92631078e+05, 1.95388906e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.06975312e+05, 1.94020547e+05, 1.82118406e+05, 2.06975312e+05, 1.94020547e+05, 1.82118406e+05, 2.06975312e+05, 1.94020547e+05, 1.82118406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.06975406e+05, 1.82118312e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     972975743), # 972.98MB, avg file size 972.98MB
  ("fsize_db",                        11038820268), # 11.04GB, avg file size 849.14MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199995, ],
    'CountWeighted'                                                                  : [ 1.99967062e+05, 1.99962750e+05, 1.99991656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.14710312e+05, 1.99967062e+05, 1.86601250e+05, 2.14710312e+05, 1.99967062e+05, 1.86601250e+05, 2.14710312e+05, 1.99967062e+05, 1.86601250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.14710312e+05, 1.86601250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94015984e+05, 1.94001906e+05, 1.94045938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94015984e+05, 1.92630688e+05, 1.95380250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.08272656e+05, 1.94015984e+05, 1.81080562e+05, 2.08272656e+05, 1.94015984e+05, 1.81080562e+05, 2.08272656e+05, 1.94015984e+05, 1.81080562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.08272656e+05, 1.81080562e+05, ],
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     1001949655), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        11235761543), # 11.24GB, avg file size 802.55MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199996, ],
    'CountWeighted'                                                                  : [ 1.99984594e+05, 1.99986406e+05, 1.99962500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15957328e+05, 1.99984594e+05, 1.85674125e+05, 2.15957328e+05, 1.99984594e+05, 1.85674125e+05, 2.15957328e+05, 1.99984594e+05, 1.85674125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15957328e+05, 1.85674125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93922438e+05, 1.93909594e+05, 1.93918688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93922438e+05, 1.92518328e+05, 1.95304984e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09364312e+05, 1.93922438e+05, 1.80080094e+05, 2.09364312e+05, 1.93922438e+05, 1.80080094e+05, 2.09364312e+05, 1.93922438e+05, 1.80080094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09364312e+05, 1.80080094e+05, ],
  }),
  ("nof_tree_events",                 199996),
  ("nof_db_events",                   199996),
  ("fsize_local",                     1023250041), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        11265507117), # 11.27GB, avg file size 804.68MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 195999, ],
    'CountWeighted'                                                                  : [ 1.95966469e+05, 1.96011125e+05, 1.96008750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.12742938e+05, 1.95965562e+05, 1.81136844e+05, 2.12742938e+05, 1.95965562e+05, 1.81136844e+05, 2.12742938e+05, 1.95965562e+05, 1.81136844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.12743125e+05, 1.81136656e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.90109469e+05, 1.90128344e+05, 1.90147375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.90109469e+05, 1.88756938e+05, 1.91444844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.06325391e+05, 1.90108375e+05, 1.75750000e+05, 2.06325391e+05, 1.90108375e+05, 1.75750000e+05, 2.06325391e+05, 1.90108375e+05, 1.75750000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.06325531e+05, 1.75749875e+05, ],
  }),
  ("nof_tree_events",                 195999),
  ("nof_db_events",                   195999),
  ("fsize_local",                     1017963396), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        11148852408), # 11.15GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 195997, ],
    'CountWeighted'                                                                  : [ 1.95964781e+05, 1.95970406e+05, 1.95941297e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.13670062e+05, 1.95963109e+05, 1.80385625e+05, 2.13670062e+05, 1.95963109e+05, 1.80385625e+05, 2.13670062e+05, 1.95963109e+05, 1.80385625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.13671188e+05, 1.80384469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.90094875e+05, 1.90087094e+05, 1.90083016e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.90094875e+05, 1.88743125e+05, 1.91426062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.07223688e+05, 1.90093438e+05, 1.75009812e+05, 2.07223688e+05, 1.90093438e+05, 1.75009812e+05, 2.07223688e+05, 1.90093438e+05, 1.75009812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.07224234e+05, 1.75009281e+05, ],
  }),
  ("nof_tree_events",                 195997),
  ("nof_db_events",                   195997),
  ("fsize_local",                     1031456296), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        11274075929), # 11.27GB, avg file size 626.34MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99946891e+05, 1.99974656e+05, 1.99953719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18950312e+05, 1.99946891e+05, 1.83382469e+05, 2.18950312e+05, 1.99946891e+05, 1.83382469e+05, 2.18950312e+05, 1.99946891e+05, 1.83382469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18950984e+05, 1.83381781e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94016281e+05, 1.94014031e+05, 1.94044609e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94016281e+05, 1.92652641e+05, 1.95362500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.12409188e+05, 1.94016281e+05, 1.77967219e+05, 2.12409188e+05, 1.94016281e+05, 1.77967219e+05, 2.12409188e+05, 1.94016281e+05, 1.77967219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.12409453e+05, 1.77966938e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1064198907), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        11369615851), # 11.37GB, avg file size 1.89GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99960438e+05, 1.99995516e+05, 1.99960500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19821969e+05, 1.99960438e+05, 1.82751422e+05, 2.19821969e+05, 1.99960438e+05, 1.82751422e+05, 2.19821969e+05, 1.99960438e+05, 1.82751422e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.19821969e+05, 1.82751422e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94074781e+05, 1.94082031e+05, 1.94085125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94074781e+05, 1.92725031e+05, 1.95407844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.13300062e+05, 1.94074219e+05, 1.77397844e+05, 2.13300062e+05, 1.94074219e+05, 1.77397844e+05, 2.13300062e+05, 1.94074219e+05, 1.77397844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.13300062e+05, 1.77397844e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1071714772), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        11488159001), # 11.49GB, avg file size 1.15GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 191995, ],
    'CountWeighted'                                                                  : [ 1.91991703e+05, 1.91940906e+05, 1.91948703e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91991703e+05, 1.91991703e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.86298844e+05, 1.86261094e+05, 1.86273938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.86298844e+05, 1.84995875e+05, 1.87579594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.86298844e+05, 1.86298844e+05, ],
  }),
  ("nof_tree_events",                 191995),
  ("nof_db_events",                   191995),
  ("fsize_local",                     1042160135), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11613877178), # 11.61GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 1.00007969e+05, 1.00003773e+05, 9.99957656e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.10551680e+05, 1.00007969e+05, 9.09851875e+04, 1.10551680e+05, 1.00007969e+05, 9.09851875e+04, 1.10551680e+05, 1.00007969e+05, 9.09851875e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.10551680e+05, 9.09851875e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71716094e+04, 9.71614219e+04, 9.71713438e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71716094e+04, 9.65215000e+04, 9.78114062e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.07401406e+05, 9.71716094e+04, 8.84177422e+04, 1.07401406e+05, 9.71716094e+04, 8.84177422e+04, 1.07401406e+05, 9.71716094e+04, 8.84177422e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.07401406e+05, 8.84177422e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     543864763), # 543.86MB, avg file size 543.86MB
  ("fsize_db",                        5984452524), # 5.98GB, avg file size 598.45MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99832344e+04, 9.99760469e+04, 9.99992344e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11340320e+05, 9.99832344e+04, 9.03368828e+04, 1.11340320e+05, 9.99832344e+04, 9.03368828e+04, 1.11340320e+05, 9.99832344e+04, 9.03368828e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11340320e+05, 9.03368828e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70214922e+04, 9.70016094e+04, 9.70454688e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70214922e+04, 9.63482578e+04, 9.76866016e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.08028406e+05, 9.70214922e+04, 8.76718203e+04, 1.08028406e+05, 9.70214922e+04, 8.76718203e+04, 1.08028406e+05, 9.70214922e+04, 8.76718203e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.08028406e+05, 8.76718203e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     547829762), # 547.83MB, avg file size 547.83MB
  ("fsize_db",                        5974953438), # 5.97GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99938000e+05, 3.99982188e+05, 4.00000906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99938000e+05, 3.99938000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.93456625e+05, 3.93478250e+05, 3.93505812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.93456625e+05, 3.91730969e+05, 3.95078875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.93456625e+05, 3.93456625e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1442897499), # 1.44GB, avg file size 1.44GB
  ("fsize_db",                        20459339723), # 20.46GB, avg file size 1.46GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99967750e+05, 3.99970219e+05, 3.99949594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06231594e+05, 3.99967750e+05, 3.91162438e+05, 4.06231594e+05, 3.99967750e+05, 3.91162438e+05, 4.06231594e+05, 3.99967750e+05, 3.91162438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06231594e+05, 3.91162438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.93223344e+05, 3.93218438e+05, 3.93217375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.93223344e+05, 3.91440438e+05, 3.94904750e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.99350000e+05, 3.93223344e+05, 3.84596875e+05, 3.99350000e+05, 3.93223344e+05, 3.84596875e+05, 3.99350000e+05, 3.93223344e+05, 3.84596875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.99350000e+05, 3.84596875e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1457206746), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        19550516838), # 19.55GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 386000, ],
    'CountWeighted'                                                                  : [ 3.85978656e+05, 3.86073594e+05, 3.85895281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.93216938e+05, 3.85978281e+05, 3.76476375e+05, 3.93216938e+05, 3.85978281e+05, 3.76476375e+05, 3.93216938e+05, 3.85978281e+05, 3.76476375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.93216938e+05, 3.76476375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.79159000e+05, 3.79213062e+05, 3.79109000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.79159000e+05, 3.77367250e+05, 3.80851000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.86241438e+05, 3.79158000e+05, 3.69855562e+05, 3.86241438e+05, 3.79158000e+05, 3.69855562e+05, 3.86241438e+05, 3.79158000e+05, 3.69855562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.86241438e+05, 3.69855562e+05, ],
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     1430045185), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        18992366194), # 18.99GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 388998, ],
    'CountWeighted'                                                                  : [ 3.88993312e+05, 3.89050188e+05, 3.89025094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.88993312e+05, 3.88993312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81861250e+05, 3.81889219e+05, 3.81896219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81861250e+05, 3.79997344e+05, 3.83628531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81861250e+05, 3.81861250e+05, ],
  }),
  ("nof_tree_events",                 388998),
  ("nof_db_events",                   388998),
  ("fsize_local",                     1478108345), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        20249921988), # 20.25GB, avg file size 880.43MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99994156e+05, 2.99953906e+05, 2.99988125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08273938e+05, 2.99993250e+05, 2.90511031e+05, 3.08273938e+05, 2.99993250e+05, 2.90511031e+05, 3.08273938e+05, 2.99993250e+05, 2.90511031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08273938e+05, 2.90511031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93966938e+05, 2.93936812e+05, 2.93963000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93966938e+05, 2.92413625e+05, 2.95445812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.02047688e+05, 2.93965438e+05, 2.84706750e+05, 3.02047688e+05, 2.93965438e+05, 2.84706750e+05, 3.02047688e+05, 2.93965438e+05, 2.84706750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.02047688e+05, 2.84706750e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1170732826), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        15102940723), # 15.10GB, avg file size 943.93MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99958625e+05, 2.99975531e+05, 3.00022219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09824000e+05, 2.99958625e+05, 2.89276062e+05, 3.09824000e+05, 2.99958625e+05, 2.89276062e+05, 3.09824000e+05, 2.99958625e+05, 2.89276062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09824000e+05, 2.89276062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93538344e+05, 2.93526406e+05, 2.93594469e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93538344e+05, 2.91899406e+05, 2.95100844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.03146562e+05, 2.93538344e+05, 2.83112625e+05, 3.03146562e+05, 2.93538344e+05, 2.83112625e+05, 3.03146562e+05, 2.93538344e+05, 2.83112625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.03146562e+05, 2.83112625e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1208652503), # 1.21GB, avg file size 1.21GB
  ("fsize_db",                        15313788135), # 15.31GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 291998, ],
    'CountWeighted'                                                                  : [ 2.92021500e+05, 2.91952531e+05, 2.91962125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.03639531e+05, 2.92021500e+05, 2.79966875e+05, 3.03639531e+05, 2.92021500e+05, 2.79966875e+05, 3.03639531e+05, 2.92021500e+05, 2.79966875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.03639531e+05, 2.79966875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.85216219e+05, 2.85151375e+05, 2.85194188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.85216219e+05, 2.83505281e+05, 2.86853375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.96541375e+05, 2.85216219e+05, 2.73488188e+05, 2.96541375e+05, 2.85216219e+05, 2.73488188e+05, 2.96541375e+05, 2.85216219e+05, 2.73488188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.96541375e+05, 2.73488188e+05, ],
  }),
  ("nof_tree_events",                 291998),
  ("nof_db_events",                   291998),
  ("fsize_local",                     1224632436), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        15117730207), # 15.12GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00046125e+05, 2.99928000e+05, 3.00051719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15116438e+05, 3.00046125e+05, 2.85271875e+05, 3.15116438e+05, 3.00046125e+05, 2.85271875e+05, 3.15116438e+05, 3.00046125e+05, 2.85271875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15116438e+05, 2.85271812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92168969e+05, 2.92079094e+05, 2.92191406e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92168969e+05, 2.90230188e+05, 2.94043594e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.06820875e+05, 2.92168969e+05, 2.77846438e+05, 3.06820875e+05, 2.92168969e+05, 2.77846438e+05, 3.06820875e+05, 2.92168969e+05, 2.77846438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.06820906e+05, 2.77846375e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1334794810), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        15994431220), # 15.99GB, avg file size 799.72MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 292000, ],
    'CountWeighted'                                                                  : [ 2.91998500e+05, 2.91991281e+05, 2.91964469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09297375e+05, 2.91989812e+05, 2.75677750e+05, 3.09297375e+05, 2.91989812e+05, 2.75677750e+05, 3.09297375e+05, 2.91989812e+05, 2.75677750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09297375e+05, 2.75677750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.83698875e+05, 2.83672594e+05, 2.83689531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.83698875e+05, 2.81684625e+05, 2.85652719e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.00458812e+05, 2.83692688e+05, 2.67895562e+05, 3.00458812e+05, 2.83692688e+05, 2.67895562e+05, 3.00458812e+05, 2.83692688e+05, 2.67895562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.00458812e+05, 2.67895562e+05, ],
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     1357081034), # 1.36GB, avg file size 1.36GB
  ("fsize_db",                        15872838181), # 15.87GB, avg file size 755.85MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 2.99981688e+05, 2.99979688e+05, 2.99981281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20091656e+05, 2.99981688e+05, 2.81474156e+05, 3.20091656e+05, 2.99981688e+05, 2.81474156e+05, 3.20091656e+05, 2.99981688e+05, 2.81474156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20092000e+05, 2.81473781e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90825125e+05, 2.90814625e+05, 2.90830375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90825125e+05, 2.88629844e+05, 2.92964000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.10255438e+05, 2.90825125e+05, 2.72934688e+05, 3.10255438e+05, 2.90825125e+05, 2.72934688e+05, 3.10255438e+05, 2.90825125e+05, 2.72934688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.10255781e+05, 2.72934375e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1449096531), # 1.45GB, avg file size 1.45GB
  ("fsize_db",                        16481520657), # 16.48GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99980938e+05, 2.99981469e+05, 2.99912719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22090156e+05, 2.99980938e+05, 2.79884125e+05, 3.22090156e+05, 2.99980938e+05, 2.79884125e+05, 3.22090156e+05, 2.99980938e+05, 2.79884125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22091531e+05, 2.79882750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90197406e+05, 2.90189656e+05, 2.90164938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90197406e+05, 2.87885312e+05, 2.92465656e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.11529031e+05, 2.90197406e+05, 2.70817750e+05, 3.11529031e+05, 2.90197406e+05, 2.70817750e+05, 3.11529031e+05, 2.90197406e+05, 2.70817750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.11530406e+05, 2.70816375e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1493973020), # 1.49GB, avg file size 1.49GB
  ("fsize_db",                        16709110067), # 16.71GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 195999, ],
    'CountWeighted'                                                                  : [ 1.95990094e+05, 1.95993875e+05, 1.95981484e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.11611094e+05, 1.95990094e+05, 1.81952625e+05, 2.11611094e+05, 1.95990094e+05, 1.81952625e+05, 2.11611094e+05, 1.95990094e+05, 1.81952625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.11611156e+05, 1.81952562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.89369656e+05, 1.89375797e+05, 1.89364000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.89369656e+05, 1.87813781e+05, 1.90896875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.04428172e+05, 1.89369656e+05, 1.75843094e+05, 2.04428172e+05, 1.89369656e+05, 1.75843094e+05, 2.04428172e+05, 1.89369656e+05, 1.75843094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.04428188e+05, 1.75843062e+05, ],
  }),
  ("nof_tree_events",                 195999),
  ("nof_db_events",                   195999),
  ("fsize_local",                     995854465), # 995.85MB, avg file size 995.85MB
  ("fsize_db",                        11098413315), # 11.10GB, avg file size 1.11GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99958188e+05, 1.99957578e+05, 1.99938219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17067875e+05, 1.99958188e+05, 1.84802188e+05, 2.17067875e+05, 1.99958188e+05, 1.84802188e+05, 2.17067875e+05, 1.99958188e+05, 1.84802188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17067875e+05, 1.84802188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92896375e+05, 1.92884250e+05, 1.92905578e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92896375e+05, 1.91250812e+05, 1.94515234e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09343047e+05, 1.92896375e+05, 1.78312672e+05, 2.09343047e+05, 1.92896375e+05, 1.78312672e+05, 2.09343047e+05, 1.92896375e+05, 1.78312672e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09343047e+05, 1.78312672e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1029555319), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        11471924888), # 11.47GB, avg file size 819.42MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99997719e+05, 2.00008844e+05, 1.99966625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18036312e+05, 1.99997719e+05, 1.84073594e+05, 2.18036312e+05, 1.99997719e+05, 1.84073594e+05, 2.18036312e+05, 1.99997719e+05, 1.84073594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18036312e+05, 1.84073594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92911391e+05, 1.92910062e+05, 1.92893953e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92911391e+05, 1.91265094e+05, 1.94534281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.10273531e+05, 1.92911391e+05, 1.77594406e+05, 2.10273531e+05, 1.92911391e+05, 1.77594406e+05, 2.10273531e+05, 1.92911391e+05, 1.77594406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.10273531e+05, 1.77594406e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1040975952), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11589915708), # 11.59GB, avg file size 772.66MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 192000, ],
    'CountWeighted'                                                                  : [ 1.91986516e+05, 1.91985594e+05, 1.91977766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91986516e+05, 1.91986516e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.84948156e+05, 1.84936078e+05, 1.84956094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.84948156e+05, 1.83321250e+05, 1.86553875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.84948156e+05, 1.84948156e+05, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     1013702990), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11585622017), # 11.59GB, avg file size 965.47MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99951688e+05, 1.99955688e+05, 1.99958094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99951688e+05, 1.99951688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92537938e+05, 1.92520031e+05, 1.92556734e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92537938e+05, 1.90827125e+05, 1.94228641e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92537938e+05, 1.92537938e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1061350128), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        12059647437), # 12.06GB, avg file size 1.51GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99966375e+05, 1.99933156e+05, 1.99983953e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99966375e+05, 1.99966375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92344031e+05, 1.92313078e+05, 1.92363000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92344031e+05, 1.90594156e+05, 1.94068781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92344031e+05, 1.92344031e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1065055830), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        12157898020), # 12.16GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99981891e+05, 1.99987156e+05, 1.99977812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.21313812e+05, 1.99981891e+05, 1.81619125e+05, 2.21313812e+05, 1.99981891e+05, 1.81619125e+05, 2.21313812e+05, 1.99981891e+05, 1.81619125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21313812e+05, 1.81619125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92276281e+05, 1.92265625e+05, 1.92294969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92276281e+05, 1.90514750e+05, 1.94018812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.12747781e+05, 1.92276281e+05, 1.74669781e+05, 2.12747781e+05, 1.92276281e+05, 1.74669781e+05, 2.12747781e+05, 1.92276281e+05, 1.74669781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.12747781e+05, 1.74669781e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1061996640), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        11885543228), # 11.89GB, avg file size 742.85MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99630078e+04, 9.99682422e+04, 9.99854766e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11351805e+05, 9.99623359e+04, 9.03295391e+04, 1.11351805e+05, 9.99623359e+04, 9.03295391e+04, 1.11351805e+05, 9.99623359e+04, 9.03295391e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11351805e+05, 9.03295391e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.59384297e+04, 9.59389688e+04, 9.59525703e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.59384297e+04, 9.50253203e+04, 9.68423750e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06835023e+05, 9.59375859e+04, 8.67047969e+04, 1.06835023e+05, 9.59375859e+04, 8.67047969e+04, 1.06835023e+05, 9.59375859e+04, 8.67047969e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06835023e+05, 8.67047969e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     533493168), # 533.49MB, avg file size 533.49MB
  ("fsize_db",                        5933581710), # 5.93GB, avg file size 988.93MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 4.00014625e+05, 3.99954781e+05, 3.99984094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.04907469e+05, 4.00014625e+05, 3.92226062e+05, 4.04907469e+05, 4.00014625e+05, 3.92226062e+05, 4.04907469e+05, 4.00014625e+05, 3.92226062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04907469e+05, 3.92226062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.93165219e+05, 3.93103156e+05, 3.93168531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.93165219e+05, 3.91363656e+05, 3.94859375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.97950156e+05, 3.93165219e+05, 3.85549219e+05, 3.97950156e+05, 3.93165219e+05, 3.85549219e+05, 3.97950156e+05, 3.93165219e+05, 3.85549219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.97950156e+05, 3.85549219e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1459244189), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        20066660592), # 20.07GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 4.00006438e+05, 3.99970344e+05, 3.99987906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06233875e+05, 4.00005500e+05, 3.91158344e+05, 4.06233875e+05, 4.00005500e+05, 3.91158344e+05, 4.06233875e+05, 4.00005500e+05, 3.91158344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06233875e+05, 3.91158344e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92837625e+05, 3.92796688e+05, 3.92843031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92837625e+05, 3.90962969e+05, 3.94602562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98924375e+05, 3.92836125e+05, 3.84187125e+05, 3.98924375e+05, 3.92836125e+05, 3.84187125e+05, 3.98924375e+05, 3.92836125e+05, 3.84187125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.98924375e+05, 3.84187125e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1490854087), # 1.49GB, avg file size 1.49GB
  ("fsize_db",                        19879949428), # 19.88GB, avg file size 994.00MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99952156e+05, 3.99938344e+05, 3.99997500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07518438e+05, 3.99952156e+05, 3.90144750e+05, 4.07518438e+05, 3.99952156e+05, 3.90144750e+05, 4.07518438e+05, 3.99952156e+05, 3.90144750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07518438e+05, 3.90144750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92566125e+05, 3.92534719e+05, 3.92615562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92566125e+05, 3.90637156e+05, 3.94387000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.99940750e+05, 3.92566125e+05, 3.82962438e+05, 3.99940750e+05, 3.92566125e+05, 3.82962438e+05, 3.99940750e+05, 3.92566125e+05, 3.82962438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.99940750e+05, 3.82962438e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1519704538), # 1.52GB, avg file size 1.52GB
  ("fsize_db",                        20200851289), # 20.20GB, avg file size 961.95MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 391999, ],
    'CountWeighted'                                                                  : [ 3.91963062e+05, 3.91926906e+05, 3.91970312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.00557281e+05, 3.91963062e+05, 3.81389656e+05, 4.00557281e+05, 3.91963062e+05, 3.81389656e+05, 4.00557281e+05, 3.91963062e+05, 3.81389656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00557281e+05, 3.81389656e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.84316719e+05, 3.84280938e+05, 3.84320000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.84316719e+05, 3.82339969e+05, 3.86186375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.92695656e+05, 3.84316719e+05, 3.73982000e+05, 3.92695656e+05, 3.84316719e+05, 3.73982000e+05, 3.92695656e+05, 3.84316719e+05, 3.73982000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.92695656e+05, 3.73982000e+05, ],
  }),
  ("nof_tree_events",                 391999),
  ("nof_db_events",                   391999),
  ("fsize_local",                     1519834815), # 1.52GB, avg file size 1.52GB
  ("fsize_db",                        19893233798), # 19.89GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 383998, ],
    'CountWeighted'                                                                  : [ 3.83900281e+05, 3.83940625e+05, 3.84001719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.94554625e+05, 3.83900281e+05, 3.71885875e+05, 3.94554625e+05, 3.83900281e+05, 3.71885875e+05, 3.94554625e+05, 3.83900281e+05, 3.71885875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.94554625e+05, 3.71885875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.75910031e+05, 3.75918844e+05, 3.75995656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.75910031e+05, 3.73868812e+05, 3.77855938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.86271000e+05, 3.75910031e+05, 3.64161812e+05, 3.86271000e+05, 3.75910031e+05, 3.64161812e+05, 3.86271000e+05, 3.75910031e+05, 3.64161812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.86271000e+05, 3.64161812e+05, ],
  }),
  ("nof_tree_events",                 383998),
  ("nof_db_events",                   383998),
  ("fsize_local",                     1549484304), # 1.55GB, avg file size 1.55GB
  ("fsize_db",                        19708482041), # 19.71GB, avg file size 985.42MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99983594e+05, 2.99945938e+05, 3.00008094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09819125e+05, 2.99983594e+05, 2.89293062e+05, 3.09819125e+05, 2.99983594e+05, 2.89293062e+05, 3.09819125e+05, 2.99983594e+05, 2.89293062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09819594e+05, 2.89292594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93359250e+05, 2.93323125e+05, 2.93388125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93359250e+05, 2.91690000e+05, 2.94957625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.02939781e+05, 2.93359250e+05, 2.82944000e+05, 3.02939781e+05, 2.93359250e+05, 2.82944000e+05, 3.02939781e+05, 2.93359250e+05, 2.82944000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.02940125e+05, 2.82943688e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1251335063), # 1.25GB, avg file size 1.25GB
  ("fsize_db",                        15656023835), # 15.66GB, avg file size 1.20GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99948625e+05, 3.00021938e+05, 2.99978375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11994344e+05, 2.99948625e+05, 2.87634438e+05, 3.11994344e+05, 2.99948625e+05, 2.87634438e+05, 3.11994344e+05, 2.99948625e+05, 2.87634438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11994344e+05, 2.87634438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92808438e+05, 2.92851250e+05, 2.92834375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92808438e+05, 2.91034344e+05, 2.94520000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.04505719e+05, 2.92808438e+05, 2.80817625e+05, 3.04505719e+05, 2.92808438e+05, 2.80817625e+05, 3.04505719e+05, 2.92808438e+05, 2.80817625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.04505719e+05, 2.80817625e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1313117405), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        16009029568), # 16.01GB, avg file size 1.33GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99961219e+05, 2.99948719e+05, 2.99978406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15114281e+05, 2.99961219e+05, 2.85299188e+05, 3.15114281e+05, 2.99961219e+05, 2.85299188e+05, 3.15114281e+05, 2.99961219e+05, 2.85299188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15114281e+05, 2.85299188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92122781e+05, 2.92107906e+05, 2.92141812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92122781e+05, 2.90216375e+05, 2.93975562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.06817125e+05, 2.92122781e+05, 2.77884125e+05, 3.06817125e+05, 2.92122781e+05, 2.77884125e+05, 3.06817125e+05, 2.92122781e+05, 2.77884125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.06817125e+05, 2.77884125e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1393235442), # 1.39GB, avg file size 1.39GB
  ("fsize_db",                        16480100060), # 16.48GB, avg file size 915.56MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 287998, ],
    'CountWeighted'                                                                  : [ 2.87999781e+05, 2.87963281e+05, 2.87965562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.05060562e+05, 2.87999781e+05, 2.71898625e+05, 3.05060562e+05, 2.87999781e+05, 2.71898625e+05, 3.05060562e+05, 2.87999781e+05, 2.71898625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.05060562e+05, 2.71898625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.79988062e+05, 2.79956062e+05, 2.79967750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.79988062e+05, 2.78074188e+05, 2.81857656e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.96519500e+05, 2.79988062e+05, 2.64399094e+05, 2.96519500e+05, 2.79988062e+05, 2.64399094e+05, 2.96519500e+05, 2.79988062e+05, 2.64399094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.96519500e+05, 2.64399094e+05, ],
  }),
  ("nof_tree_events",                 287998),
  ("nof_db_events",                   287998),
  ("fsize_local",                     1401638942), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        16214133807), # 16.21GB, avg file size 953.77MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 2.99986281e+05, 2.99985125e+05, 2.99932500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20048000e+05, 2.99986281e+05, 2.81478594e+05, 3.20048000e+05, 2.99986281e+05, 2.81478594e+05, 3.20048000e+05, 2.99986281e+05, 2.81478594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20048000e+05, 2.81478594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91339906e+05, 2.91327219e+05, 2.91328062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91339906e+05, 2.89304062e+05, 2.93339250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.10762688e+05, 2.91339906e+05, 2.73424625e+05, 3.10762688e+05, 2.91339906e+05, 2.73424625e+05, 3.10762688e+05, 2.91339906e+05, 2.73424625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.10762688e+05, 2.73424625e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1515692238), # 1.52GB, avg file size 1.52GB
  ("fsize_db",                        17053053622), # 17.05GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 3.00039062e+05, 3.00037688e+05, 2.99930750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22091188e+05, 3.00039062e+05, 2.79875125e+05, 3.22091188e+05, 3.00039062e+05, 2.79875125e+05, 3.22091188e+05, 3.00039062e+05, 2.79875125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22091562e+05, 2.79874750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91187562e+05, 2.91169281e+05, 2.91124875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91187562e+05, 2.89119188e+05, 2.93212938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.12536031e+05, 2.91187562e+05, 2.71696500e+05, 3.12536031e+05, 2.91187562e+05, 2.71696500e+05, 3.12536031e+05, 2.91187562e+05, 2.71696500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.12536281e+05, 2.71696250e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1554471753), # 1.55GB, avg file size 1.55GB
  ("fsize_db",                        17210955077), # 17.21GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 191998, ],
    'CountWeighted'                                                                  : [ 1.92007266e+05, 1.92023906e+05, 1.91961812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.07321891e+05, 1.92007266e+05, 1.78227969e+05, 2.07321891e+05, 1.92007266e+05, 1.78227969e+05, 2.07321891e+05, 1.92007266e+05, 1.78227969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.07321891e+05, 1.78227969e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.86311219e+05, 1.86306953e+05, 1.86297500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.86311219e+05, 1.84989688e+05, 1.87612281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.01130391e+05, 1.86311219e+05, 1.72985906e+05, 2.01130391e+05, 1.86311219e+05, 1.72985906e+05, 2.01130391e+05, 1.86311219e+05, 1.72985906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.01130391e+05, 1.72985906e+05, ],
  }),
  ("nof_tree_events",                 191998),
  ("nof_db_events",                   191998),
  ("fsize_local",                     1011551932), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11180869047), # 11.18GB, avg file size 860.07MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99957688e+05, 2.00016219e+05, 1.99953344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17069391e+05, 1.99957234e+05, 1.84853797e+05, 2.17069391e+05, 1.99957234e+05, 1.84853797e+05, 2.17069391e+05, 1.99957234e+05, 1.84853797e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17069391e+05, 1.84853797e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93935734e+05, 1.93967609e+05, 1.93933891e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93935734e+05, 1.92544422e+05, 1.95309219e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.10468844e+05, 1.93934953e+05, 1.79311625e+05, 2.10468844e+05, 1.93934953e+05, 1.79311625e+05, 2.10468844e+05, 1.93934953e+05, 1.79311625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.10468844e+05, 1.79311625e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1064750918), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        11726047160), # 11.73GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 191999, ],
    'CountWeighted'                                                                  : [ 1.91987531e+05, 1.91988969e+05, 1.92020781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.09349641e+05, 1.91986688e+05, 1.76704547e+05, 2.09349641e+05, 1.91986688e+05, 1.76704547e+05, 2.09349641e+05, 1.91986688e+05, 1.76704547e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.09349641e+05, 1.76704547e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.86285281e+05, 1.86281625e+05, 1.86311812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.86285281e+05, 1.84972703e+05, 1.87581031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.03084453e+05, 1.86284281e+05, 1.71493812e+05, 2.03084453e+05, 1.86284281e+05, 1.71493812e+05, 2.03084453e+05, 1.86284281e+05, 1.71493812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.03084453e+05, 1.71493812e+05, ],
  }),
  ("nof_tree_events",                 191999),
  ("nof_db_events",                   191999),
  ("fsize_local",                     1027815199), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        11310227020), # 11.31GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99977562e+05, 1.99959281e+05, 1.99965031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18966062e+05, 1.99977562e+05, 1.83370641e+05, 2.18966062e+05, 1.99977562e+05, 1.83370641e+05, 2.18966062e+05, 1.99977562e+05, 1.83370641e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18966062e+05, 1.83370641e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93981750e+05, 1.93957703e+05, 1.93983000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93981750e+05, 1.92604812e+05, 1.95336625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.12353438e+05, 1.93981750e+05, 1.77907219e+05, 2.12353438e+05, 1.93981750e+05, 1.77907219e+05, 2.12353438e+05, 1.93981750e+05, 1.77907219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.12353438e+05, 1.77907219e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1074773837), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        11817475227), # 11.82GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99978594e+05, 1.99932406e+05, 1.99967594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19772969e+05, 1.99977625e+05, 1.82732344e+05, 2.19772969e+05, 1.99977625e+05, 1.82732344e+05, 2.19772969e+05, 1.99977625e+05, 1.82732344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.19773203e+05, 1.82732094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94000766e+05, 1.93956328e+05, 1.93999406e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94000766e+05, 1.92633641e+05, 1.95347969e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.13169188e+05, 1.93999875e+05, 1.77306062e+05, 2.13169188e+05, 1.93999875e+05, 1.77306062e+05, 2.13169188e+05, 1.93999875e+05, 1.77306062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.13169250e+05, 1.77306016e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1076482557), # 1.08GB, avg file size 1.08GB
  ("fsize_db",                        11932391412), # 11.93GB, avg file size 701.91MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99950469e+05, 1.99956031e+05, 1.99983531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99950469e+05, 1.99950469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94040750e+05, 1.94034234e+05, 1.94073031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94040750e+05, 1.92688094e+05, 1.95373531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.94040750e+05, 1.94040750e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1083724599), # 1.08GB, avg file size 1.08GB
  ("fsize_db",                        12455825050), # 12.46GB, avg file size 958.14MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99866562e+04, 9.99833516e+04, 9.99901641e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.10549570e+05, 9.99866562e+04, 9.09819844e+04, 1.10549570e+05, 9.99866562e+04, 9.09819844e+04, 1.10549570e+05, 9.99866562e+04, 9.09819844e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.10549570e+05, 9.09819844e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71242656e+04, 9.71228984e+04, 9.71265547e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71242656e+04, 9.64678984e+04, 9.77721953e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.07363617e+05, 9.71242656e+04, 8.83851016e+04, 1.07363617e+05, 9.71242656e+04, 8.83851016e+04, 1.07363617e+05, 9.71242656e+04, 8.83851016e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.07363617e+05, 8.83851016e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     540678583), # 540.68MB, avg file size 540.68MB
  ("fsize_db",                        6157522996), # 6.16GB, avg file size 769.69MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99917344e+04, 9.99856641e+04, 9.99733359e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11347883e+05, 9.99917344e+04, 9.03333828e+04, 1.11347883e+05, 9.99917344e+04, 9.03333828e+04, 1.11347883e+05, 9.99917344e+04, 9.03333828e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11347883e+05, 9.03333828e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70476406e+04, 9.70427578e+04, 9.70298906e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70476406e+04, 9.63770469e+04, 9.77081562e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.08057453e+05, 9.70476406e+04, 8.76858516e+04, 1.08057453e+05, 9.70476406e+04, 8.76858516e+04, 1.08057453e+05, 9.70476406e+04, 8.76858516e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.08057453e+05, 8.76858516e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     538964916), # 538.96MB, avg file size 538.96MB
  ("fsize_db",                        6189551070), # 6.19GB, avg file size 773.69MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 384000, ],
    'CountWeighted'                                                                  : [ 3.80254812e+05, 3.80320062e+05, 3.80244594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.80254812e+05, 3.80254812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.54415406e+05, 3.54445188e+05, 3.54416250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.54415406e+05, 3.48441062e+05, 3.60354062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.54415406e+05, 3.54415406e+05, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1673849673), # 1.67GB, avg file size 1.67GB
  ("fsize_db",                        20516924301), # 20.52GB, avg file size 892.04MB
  ("use_it",                          True),
  ("xsection",                        6.785e-06),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_1_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99941812e+05, 3.99958688e+05, 3.99992844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.11981406e+05, 4.83258344e+05, 4.56283688e+05, 4.23837688e+05, 3.99941812e+05, 3.77566188e+05, 3.56937688e+05, 3.36759188e+05, 3.17858750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.11984281e+05, 3.17857781e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87170656e+05, 3.87149500e+05, 3.87232875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87170656e+05, 3.84148438e+05, 3.90140250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.95490531e+05, 4.67837125e+05, 4.41844250e+05, 4.10164625e+05, 3.87170656e+05, 3.65603062e+05, 3.45410312e+05, 3.25988594e+05, 3.07776125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.95493406e+05, 3.07775125e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1749281207), # 1.75GB, avg file size 1.75GB
  ("fsize_db",                        20766449398), # 20.77GB, avg file size 1.38GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 388000, ],
    'CountWeighted'                                                                  : [ 3.87882969e+05, 3.87857188e+05, 3.87846219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.04101125e+05, 4.64442469e+05, 4.29581625e+05, 4.21280312e+05, 3.87869500e+05, 3.58650562e+05, 3.57634000e+05, 3.29170281e+05, 3.04204312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.04101188e+05, 3.04204281e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.74120469e+05, 3.74085500e+05, 3.74118125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.74120469e+05, 3.70938531e+05, 3.77262938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.86036000e+05, 4.47982500e+05, 4.14512469e+05, 4.06147812e+05, 3.74110719e+05, 3.46038125e+05, 3.44761250e+05, 3.17452312e+05, 2.93484875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.86036062e+05, 2.93484844e+05, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     1859963491), # 1.86GB, avg file size 1.86GB
  ("fsize_db",                        21137556590), # 21.14GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99962562e+05, 3.99949688e+05, 3.99932906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12031844e+05, 4.83198531e+05, 4.56119500e+05, 4.23902000e+05, 3.99962000e+05, 3.77489094e+05, 3.57007188e+05, 3.36786750e+05, 3.17831500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12031844e+05, 3.17831500e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87087312e+05, 3.87056438e+05, 3.87079438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87087312e+05, 3.84047875e+05, 3.90076938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.95416531e+05, 4.67658781e+05, 4.41567688e+05, 4.10131938e+05, 3.87085688e+05, 3.65432844e+05, 3.45398625e+05, 3.25936344e+05, 3.07671688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.95416531e+05, 3.07671688e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1752141428), # 1.75GB, avg file size 1.75GB
  ("fsize_db",                        20758947388), # 20.76GB, avg file size 902.56MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 374000, ],
    'CountWeighted'                                                                  : [ 3.73979250e+05, 3.73896469e+05, 3.73970219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.76968062e+05, 4.52875438e+05, 4.29698125e+05, 3.93920750e+05, 3.73979250e+05, 3.54812625e+05, 3.31091500e+05, 3.14286750e+05, 2.98159000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.76968062e+05, 2.98159000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.62279875e+05, 3.62196156e+05, 3.62301969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.62279875e+05, 3.59507500e+05, 3.65008625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.61933781e+05, 4.38716812e+05, 4.16365938e+05, 3.81496000e+05, 3.62279875e+05, 3.43794812e+05, 3.20639906e+05, 3.04449812e+05, 2.88896875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.61933781e+05, 2.88896875e+05, ],
  }),
  ("nof_tree_events",                 374000),
  ("nof_db_events",                   374000),
  ("fsize_local",                     1596650076), # 1.60GB, avg file size 1.60GB
  ("fsize_db",                        19521414949), # 19.52GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99932875e+05, 3.99996688e+05, 3.99998250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19447031e+05, 4.78878406e+05, 4.43029219e+05, 4.33960125e+05, 3.99932875e+05, 3.69929781e+05, 3.68249062e+05, 3.39303750e+05, 3.13772812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19447062e+05, 3.13772812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.85684031e+05, 3.85692125e+05, 3.85761219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.85684031e+05, 3.82396188e+05, 3.88944000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.00794500e+05, 4.61833094e+05, 4.27386406e+05, 4.18356750e+05, 3.85684031e+05, 3.56848281e+05, 3.54993875e+05, 3.27199000e+05, 3.02666938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.00794500e+05, 3.02666938e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1918950365), # 1.92GB, avg file size 1.92GB
  ("fsize_db",                        21901746830), # 21.90GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 396000, ],
    'CountWeighted'                                                                  : [ 3.95942031e+05, 3.96003594e+05, 3.95945906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.04830000e+05, 4.79599375e+05, 4.55277188e+05, 4.16854062e+05, 3.95942031e+05, 3.75852438e+05, 3.50307812e+05, 3.32711406e+05, 3.15790000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.04830000e+05, 3.15790000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.83655844e+05, 3.83677438e+05, 3.83673781e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.83655844e+05, 3.80736188e+05, 3.86530875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.89039031e+05, 4.64719188e+05, 4.41253375e+05, 4.03803375e+05, 3.83655844e+05, 3.64266625e+05, 3.39332344e+05, 3.22372406e+05, 3.06048875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.89039031e+05, 3.06048875e+05, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1687383825), # 1.69GB, avg file size 1.69GB
  ("fsize_db",                        20180485758), # 20.18GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo4Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    55),
  ("nof_events",                      {
    'Count'                                                                          : [ 993800, ],
    'CountWeighted'                                                                  : [ 9.35851250e+05, 9.35668766e+05, 9.35816516e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.08269056e+06, 1.06366330e+06, 1.05026102e+06, 9.57200469e+05, 9.35851234e+05, 9.18644641e+05, 8.48701406e+05, 8.26740828e+05, 8.08004172e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.12098859e+06, 7.89224516e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.35767547e+05, 9.35778156e+05, 1.29037906e+06, 9.35887875e+05, 9.35258172e+05, 6.16218094e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 6.36766475e+04, 6.36860898e+04, 8.78388066e+04, 6.36956982e+04, 6.36783564e+04, 4.19431953e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.11437250e+05, 9.11260547e+05, 9.11449828e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.11437250e+05, 9.05448344e+05, 9.17280266e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.05409314e+06, 1.03579808e+06, 1.02295031e+06, 9.32018859e+05, 9.11437203e+05, 8.94870141e+05, 8.26436625e+05, 8.05249000e+05, 7.87166875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.09140834e+06, 7.68878969e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.11472609e+05, 9.11224797e+05, 1.25646722e+06, 9.11342438e+05, 9.11089625e+05, 6.00413938e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 6.20071543e+04, 6.19986631e+04, 8.55085352e+04, 6.20089951e+04, 6.20159863e+04, 4.08559092e+04, ],
  }),
  ("nof_tree_events",                 993800),
  ("nof_db_events",                   993800),
  ("fsize_local",                     4055293270), # 4.06GB, avg file size 1.01GB
  ("fsize_db",                        48437908822), # 48.44GB, avg file size 880.69MB
  ("use_it",                          True),
  ("xsection",                        0.00026349),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH0_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo4Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    55),
  ("nof_events",                      {
    'Count'                                                                          : [ 973200, ],
    'CountWeighted'                                                                  : [ 8.72135797e+05, 8.72118000e+05, 8.72067078e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.92976781e+05, 9.77088797e+05, 9.66615578e+05, 8.92237359e+05, 8.72084469e+05, 8.56363141e+05, 8.00844656e+05, 7.78974422e+05, 7.60652766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03559289e+06, 7.37506391e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.72235516e+05, 8.72399375e+05, 1.20490481e+06, 8.72057906e+05, 8.71816469e+05, 5.72707438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.91179463e+04, 2.91169233e+04, 4.02133398e+04, 2.91169180e+04, 2.91232778e+04, 1.91421523e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.48528594e+05, 8.48505750e+05, 8.48480297e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.48528594e+05, 8.42776422e+05, 8.54143578e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.65739109e+05, 9.50499047e+05, 9.40503000e+05, 8.67879125e+05, 8.48485406e+05, 8.33351688e+05, 7.79048812e+05, 7.57959859e+05, 7.40292875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00722794e+06, 7.17762453e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.48728375e+05, 8.48622578e+05, 1.17204866e+06, 8.48309141e+05, 8.48461844e+05, 5.57449680e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.83298462e+04, 2.83202446e+04, 3.91115645e+04, 2.83199644e+04, 2.83388486e+04, 1.86300747e+04, ],
  }),
  ("nof_tree_events",                 973200),
  ("nof_db_events",                   973200),
  ("fsize_local",                     4066476593), # 4.07GB, avg file size 1.02GB
  ("fsize_db",                        47737447211), # 47.74GB, avg file size 867.95MB
  ("use_it",                          True),
  ("xsection",                        0.00011734),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH1_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo4Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    62),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 8.62699391e+05, 8.62784453e+05, 8.62588484e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.84110781e+05, 9.70390672e+05, 9.61615875e+05, 8.80358906e+05, 8.62660312e+05, 8.48880953e+05, 7.87947781e+05, 7.68524625e+05, 7.52163375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03623509e+06, 7.20361641e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.62675047e+05, 8.62634391e+05, 1.19285556e+06, 8.62719047e+05, 8.62023172e+05, 5.65253828e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.31737903e+04, 1.31703269e+04, 1.82129136e+04, 1.31760439e+04, 1.31758391e+04, 8.64209082e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.39325891e+05, 8.39327734e+05, 8.39302594e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.39325891e+05, 8.33632328e+05, 8.44890562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.57019891e+05, 9.43929438e+05, 9.35617750e+05, 8.56272234e+05, 8.39291547e+05, 8.26080609e+05, 7.66477734e+05, 7.47796078e+05, 7.32056375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00776438e+06, 7.01107016e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.39433953e+05, 8.39076719e+05, 1.16020112e+06, 8.39178984e+05, 8.38910562e+05, 5.50263891e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.28172744e+04, 1.28091853e+04, 1.77126514e+04, 1.28148801e+04, 1.28212061e+04, 8.41160327e+03, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4210889018), # 4.21GB, avg file size 1.05GB
  ("fsize_db",                        49299783371), # 49.30GB, avg file size 795.16MB
  ("use_it",                          True),
  ("xsection",                        4.97e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo4Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    58),
  ("nof_events",                      {
    'Count'                                                                          : [ 991200, ],
    'CountWeighted'                                                                  : [ 9.75626250e+05, 9.75693250e+05, 9.75702094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.16860781e+06, 1.14658962e+06, 1.12963400e+06, 9.95071703e+05, 9.75590094e+05, 9.59165234e+05, 8.56874094e+05, 8.39680328e+05, 8.24117297e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.20429662e+06, 8.07343391e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.75826812e+05, 9.76011125e+05, 1.34362962e+06, 9.75431281e+05, 9.74448453e+05, 6.43645422e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 7.95415391e+04, 7.95522422e+04, 1.09577090e+05, 7.95029785e+04, 7.94826836e+04, 5.24578037e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.52048281e+05, 9.52063859e+05, 9.52126453e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.52048281e+05, 9.46138234e+05, 9.57784312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.13982188e+06, 1.11864509e+06, 1.10235869e+06, 9.70753047e+05, 9.52013172e+05, 9.36188531e+05, 8.36058141e+05, 8.19501156e+05, 8.04495391e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.17471109e+06, 7.88093641e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.52386750e+05, 9.52222281e+05, 1.31075509e+06, 9.51652766e+05, 9.51155781e+05, 6.28464375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 7.76214062e+04, 7.76035039e+04, 1.06883943e+05, 7.75551133e+04, 7.75744180e+04, 5.12141641e+04, ],
  }),
  ("nof_tree_events",                 991200),
  ("nof_db_events",                   991200),
  ("fsize_local",                     3840770806), # 3.84GB, avg file size 960.19MB
  ("fsize_db",                        47501791315), # 47.50GB, avg file size 819.00MB
  ("use_it",                          True),
  ("xsection",                        0.00034666),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH5_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.99957375e+05, 3.99958188e+05, 3.99988938e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12035625e+05, 4.83279000e+05, 4.56279500e+05, 4.23879594e+05, 3.99956406e+05, 3.77572719e+05, 3.56977094e+05, 3.36780875e+05, 3.17864094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12035969e+05, 3.17863594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87740219e+05, 3.87731656e+05, 3.87761219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87740219e+05, 3.84821438e+05, 3.90593469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.96246438e+05, 4.68526719e+05, 4.42477406e+05, 4.10789500e+05, 3.87738188e+05, 3.66133062e+05, 3.45939469e+05, 3.26472562e+05, 3.08222344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.96246781e+05, 3.08221875e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1828350814), # 1.83GB, avg file size 1.83GB
  ("fsize_db",                        21713327567), # 21.71GB, avg file size 1.45GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 369992, ],
    'CountWeighted'                                                                  : [ 3.69968406e+05, 3.69942844e+05, 3.69992906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.80692500e+05, 4.42947688e+05, 4.09764188e+05, 4.01694375e+05, 3.69968406e+05, 3.42076125e+05, 3.40983594e+05, 3.13889406e+05, 2.90126969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.80695375e+05, 2.90124438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.57228656e+05, 3.57207156e+05, 3.57255688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.57228656e+05, 3.54270938e+05, 3.60142625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.63984094e+05, 4.27750906e+05, 3.95869156e+05, 3.87692562e+05, 3.57228656e+05, 3.30440688e+05, 3.29069125e+05, 3.03063375e+05, 2.80236156e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.63986656e+05, 2.80233875e+05, ],
  }),
  ("nof_tree_events",                 369992),
  ("nof_db_events",                   369992),
  ("fsize_local",                     1824685750), # 1.82GB, avg file size 1.82GB
  ("fsize_db",                        20666744125), # 20.67GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 392996, ],
    'CountWeighted'                                                                  : [ 3.92980156e+05, 3.93009969e+05, 3.92944188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.03066812e+05, 4.74755438e+05, 4.48161250e+05, 4.16473062e+05, 3.92980156e+05, 3.70900344e+05, 3.50746812e+05, 3.30894625e+05, 3.12278125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.03066812e+05, 3.12278125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81002250e+05, 3.81017312e+05, 3.80973938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81002250e+05, 3.78142281e+05, 3.83795000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.87612438e+05, 4.60307688e+05, 4.34635688e+05, 4.03664312e+05, 3.81002250e+05, 3.59692594e+05, 3.39945750e+05, 3.20801781e+05, 3.02830250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.87612438e+05, 3.02830250e+05, ],
  }),
  ("nof_tree_events",                 392996),
  ("nof_db_events",                   392996),
  ("fsize_local",                     1803196101), # 1.80GB, avg file size 1.80GB
  ("fsize_db",                        20864139002), # 20.86GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 375989, ],
    'CountWeighted'                                                                  : [ 3.75942344e+05, 3.75900812e+05, 3.75909062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.79431188e+05, 4.55317156e+05, 4.32108094e+05, 3.95940062e+05, 3.75942344e+05, 3.56764375e+05, 3.32774406e+05, 3.15938500e+05, 2.99778344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.79431188e+05, 2.99778344e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.65001562e+05, 3.64947062e+05, 3.65006031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.65001562e+05, 3.62364562e+05, 3.67574438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.65357875e+05, 4.42073094e+05, 4.19641562e+05, 3.84304156e+05, 3.65001562e+05, 3.46456844e+05, 3.22984469e+05, 3.06730469e+05, 2.91110750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.65357875e+05, 2.91110750e+05, ],
  }),
  ("nof_tree_events",                 375989),
  ("nof_db_events",                   375989),
  ("fsize_local",                     1680309348), # 1.68GB, avg file size 1.68GB
  ("fsize_db",                        19916065120), # 19.92GB, avg file size 1.53GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399994, ],
    'CountWeighted'                                                                  : [ 3.99928188e+05, 3.99937562e+05, 3.99889344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12958344e+05, 4.82659688e+05, 4.54506500e+05, 4.25159156e+05, 3.99928188e+05, 3.76550125e+05, 3.58412375e+05, 3.37086562e+05, 3.17317062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12958562e+05, 3.17317000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87536562e+05, 3.87521656e+05, 3.87534906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87536562e+05, 3.84586688e+05, 3.90422031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.96920688e+05, 4.67718812e+05, 4.40557000e+05, 4.11848125e+05, 3.87536562e+05, 3.64973188e+05, 3.47173312e+05, 3.26622062e+05, 3.07552438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.96920844e+05, 3.07552406e+05, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     1849347478), # 1.85GB, avg file size 1.85GB
  ("fsize_db",                        21844664310), # 21.84GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399992, ],
    'CountWeighted'                                                                  : [ 4.00012500e+05, 3.99947625e+05, 3.99905281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10237156e+05, 4.84218438e+05, 4.59263812e+05, 4.21483125e+05, 4.00012500e+05, 3.79293250e+05, 3.54315375e+05, 3.36162844e+05, 3.18785406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10239812e+05, 3.18783188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88315719e+05, 3.88247625e+05, 3.88271438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88315719e+05, 3.85505125e+05, 3.91060875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.95235375e+05, 4.70102125e+05, 4.45975844e+05, 4.09079250e+05, 3.88315719e+05, 3.68309562e+05, 3.43877969e+05, 3.26349219e+05, 3.09547062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.95238031e+05, 3.09544812e+05, ],
  }),
  ("nof_tree_events",                 399992),
  ("nof_db_events",                   399992),
  ("fsize_local",                     1792433729), # 1.79GB, avg file size 1.79GB
  ("fsize_db",                        21124650657), # 21.12GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 384992, ],
    'CountWeighted'                                                                  : [ 3.84885938e+05, 3.84939656e+05, 3.85031531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.90972156e+05, 4.66187594e+05, 4.42348594e+05, 4.05486719e+05, 3.84885938e+05, 3.65247812e+05, 3.40809750e+05, 3.23515938e+05, 3.06930188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.90972156e+05, 3.06930188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.73665938e+05, 3.73671344e+05, 3.73780938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.73665938e+05, 3.70967812e+05, 3.76305156e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.76520688e+05, 4.52576500e+05, 4.29532281e+05, 3.93539188e+05, 3.73665938e+05, 3.54655281e+05, 3.30757406e+05, 3.14059000e+05, 2.98023062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.76520688e+05, 2.98023062e+05, ],
  }),
  ("nof_tree_events",                 384992),
  ("nof_db_events",                   384992),
  ("fsize_local",                     1721373758), # 1.72GB, avg file size 1.72GB
  ("fsize_db",                        20503345442), # 20.50GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99973625e+05, 3.99962781e+05, 3.99921344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09944719e+05, 4.84427062e+05, 4.59848875e+05, 4.21075500e+05, 3.99973625e+05, 3.79626938e+05, 3.53863188e+05, 3.36076312e+05, 3.18965219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09944719e+05, 3.18965219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88379125e+05, 3.88372719e+05, 3.88339750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88379125e+05, 3.85588812e+05, 3.91099625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.95057500e+05, 4.70406375e+05, 4.46639125e+05, 4.08771719e+05, 3.88379125e+05, 3.68712688e+05, 3.43514000e+05, 3.26329688e+05, 3.09787188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.95057500e+05, 3.09787188e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1786275996), # 1.79GB, avg file size 1.79GB
  ("fsize_db",                        21039976306), # 21.04GB, avg file size 1.00GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399991, ],
    'CountWeighted'                                                                  : [ 3.99960906e+05, 3.99951125e+05, 3.99946969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19447438e+05, 4.78882281e+05, 4.43042156e+05, 4.33948844e+05, 3.99960906e+05, 3.69935688e+05, 3.68235062e+05, 3.39303500e+05, 3.13770812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19447438e+05, 3.13770812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.86012531e+05, 3.85984531e+05, 3.86022656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.86012531e+05, 3.82775000e+05, 3.89207062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.01188312e+05, 4.62207281e+05, 4.27747938e+05, 4.18674688e+05, 3.86012531e+05, 3.57146250e+05, 3.55258438e+05, 3.27458812e+05, 3.02911375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.01188312e+05, 3.02911375e+05, ],
  }),
  ("nof_tree_events",                 399991),
  ("nof_db_events",                   399991),
  ("fsize_local",                     1997726780), # 2.00GB, avg file size 2.00GB
  ("fsize_db",                        22600644898), # 22.60GB, avg file size 1.88GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399986, ],
    'CountWeighted'                                                                  : [ 3.99978375e+05, 3.99962344e+05, 3.99916188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10079625e+05, 4.84326469e+05, 4.59553156e+05, 4.21272125e+05, 3.99978375e+05, 3.79460938e+05, 3.54086125e+05, 3.36115031e+05, 3.18870844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10079625e+05, 3.18870844e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88381531e+05, 3.88353625e+05, 3.88347812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88381531e+05, 3.85588656e+05, 3.91105562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.95186812e+05, 4.70303125e+05, 4.46350562e+05, 4.08962719e+05, 3.88381531e+05, 3.68549406e+05, 3.43729500e+05, 3.26369531e+05, 3.09695031e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.95186812e+05, 3.09695031e+05, ],
  }),
  ("nof_tree_events",                 399986),
  ("nof_db_events",                   399986),
  ("fsize_local",                     1788637296), # 1.79GB, avg file size 1.79GB
  ("fsize_db",                        21181482185), # 21.18GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 395994, ],
    'CountWeighted'                                                                  : [ 3.95966562e+05, 3.95890562e+05, 3.95945000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.05350531e+05, 4.79294000e+05, 4.54333375e+05, 4.17546469e+05, 3.95965594e+05, 3.75321156e+05, 3.51069250e+05, 3.32890031e+05, 3.15505688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.05350531e+05, 3.15505688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.84266594e+05, 3.84202625e+05, 3.84279000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.84266594e+05, 3.81460562e+05, 3.87011781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.90313000e+05, 4.65147156e+05, 4.41026375e+05, 4.05110375e+05, 3.84265219e+05, 3.64316469e+05, 3.40604812e+05, 3.23049375e+05, 3.06249688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.90313000e+05, 3.06249688e+05, ],
  }),
  ("nof_tree_events",                 395994),
  ("nof_db_events",                   395994),
  ("fsize_local",                     1779952009), # 1.78GB, avg file size 1.78GB
  ("fsize_db",                        21005832838), # 21.01GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399993, ],
    'CountWeighted'                                                                  : [ 3.99941562e+05, 3.99938312e+05, 3.99955219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09953219e+05, 4.84407750e+05, 4.59807344e+05, 4.21095000e+05, 3.99941562e+05, 3.79602812e+05, 3.53883125e+05, 3.36069094e+05, 3.18948000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09953219e+05, 3.18948000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88355938e+05, 3.88323000e+05, 3.88388562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88355938e+05, 3.85563656e+05, 3.91081531e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.95060594e+05, 4.70384188e+05, 4.46597312e+05, 4.08785281e+05, 3.88355938e+05, 3.68686500e+05, 3.43526469e+05, 3.26322438e+05, 3.09770062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.95060594e+05, 3.09770062e+05, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     1786126379), # 1.79GB, avg file size 1.79GB
  ("fsize_db",                        21048263593), # 21.05GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2V2Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    38),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 3.76452031e+05, 3.76409000e+05, 3.76504016e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.35350672e+05, 4.27786891e+05, 4.22483766e+05, 3.84984438e+05, 3.76452031e+05, 3.69622891e+05, 3.41435375e+05, 3.32648555e+05, 3.25150898e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.50942844e+05, 3.17427094e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.76489656e+05, 3.76553828e+05, 5.32995172e+05, 3.76405156e+05, 3.75921500e+05, 2.35506062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.56186133e+04, 2.56147207e+04, 3.63070391e+04, 2.56117451e+04, 2.56266953e+04, 1.60245610e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.67376344e+05, 3.67314594e+05, 3.67446328e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.67376344e+05, 3.65109000e+05, 3.69571016e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.24694344e+05, 4.17409234e+05, 4.12317125e+05, 3.75608844e+05, 3.67376344e+05, 3.60780750e+05, 3.33151734e+05, 3.24656297e+05, 3.17405750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.39929219e+05, 3.09859180e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.67444172e+05, 3.67375609e+05, 5.20025156e+05, 3.67278828e+05, 3.66961391e+05, 2.29930242e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.49970254e+04, 2.49845947e+04, 3.54143516e+04, 2.49843408e+04, 2.50084678e+04, 1.56409512e+04, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1715031176), # 1.72GB, avg file size 857.52MB
  ("fsize_db",                        20212438535), # 20.21GB, avg file size 531.91MB
  ("use_it",                          True),
  ("xsection",                        0.0020155),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH0_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2V2Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.58664578e+05, 3.58694969e+05, 3.58736641e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.08532531e+05, 4.01965062e+05, 3.97629891e+05, 3.66975422e+05, 3.58660812e+05, 3.52198469e+05, 3.29315375e+05, 3.20315781e+05, 3.12769844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.26078359e+05, 3.03235570e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.58745594e+05, 3.58714531e+05, 5.08267297e+05, 3.58657422e+05, 3.58134469e+05, 2.23910938e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.19841426e+04, 1.19900483e+04, 1.69669697e+04, 1.19844717e+04, 1.19608647e+04, 7.49689673e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.49603875e+05, 3.49602938e+05, 3.49669852e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.49603875e+05, 3.47365516e+05, 3.51781703e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98048891e+05, 3.91743422e+05, 3.87601297e+05, 3.57606578e+05, 3.49597906e+05, 3.43364781e+05, 3.20937078e+05, 3.12245148e+05, 3.04957078e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.15173766e+05, 2.95649828e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.49712562e+05, 3.49545172e+05, 4.95339125e+05, 3.49534555e+05, 3.49208812e+05, 2.18341438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.16773921e+04, 1.16789351e+04, 1.65288525e+04, 1.16743755e+04, 1.16569575e+04, 7.30632324e+03, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1764957465), # 1.76GB, avg file size 882.48MB
  ("fsize_db",                        20236176844), # 20.24GB, avg file size 919.83MB
  ("use_it",                          True),
  ("xsection",                        0.00089753),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH1_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2V2Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    38),
  ("nof_events",                      {
    'Count'                                                                          : [ 390697, ],
    'CountWeighted'                                                                  : [ 3.37054062e+05, 3.37106891e+05, 3.36997984e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.84407469e+05, 3.79149406e+05, 3.75816016e+05, 3.43880484e+05, 3.37047172e+05, 3.31703438e+05, 3.07742516e+05, 3.00217359e+05, 2.93880406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04933266e+05, 2.81345641e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.37108391e+05, 3.36894891e+05, 4.79287891e+05, 3.36975844e+05, 3.37462484e+05, 2.09568719e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.13176123e+03, 5.12825903e+03, 7.30025220e+03, 5.12955151e+03, 5.14287427e+03, 3.19185767e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.28434828e+05, 3.28474641e+05, 3.28398984e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.28434828e+05, 3.26310016e+05, 3.30497891e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.74403859e+05, 3.69380016e+05, 3.66219250e+05, 3.34996516e+05, 3.28427109e+05, 3.23300766e+05, 2.99830938e+05, 2.92581875e+05, 2.86477250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.94433859e+05, 2.74242484e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.28543016e+05, 3.28238906e+05, 4.66890922e+05, 3.28290344e+05, 3.28875422e+05, 2.04317570e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 5.00058740e+03, 4.99575952e+03, 7.11058545e+03, 4.99666846e+03, 5.01133716e+03, 3.11135181e+03, ],
  }),
  ("nof_tree_events",                 390697),
  ("nof_db_events",                   390697),
  ("fsize_local",                     1727376597), # 1.73GB, avg file size 863.69MB
  ("fsize_db",                        20005894046), # 20.01GB, avg file size 526.47MB
  ("use_it",                          True),
  ("xsection",                        0.00038015),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo2V2Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 395591, ],
    'CountWeighted'                                                                  : [ 3.89418438e+05, 3.89419125e+05, 3.89478219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.66548969e+05, 4.57673703e+05, 4.50840391e+05, 3.97226266e+05, 3.89406594e+05, 3.82784281e+05, 3.42052453e+05, 3.35138969e+05, 3.28888523e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.80703844e+05, 3.22267430e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.89342609e+05, 3.89360219e+05, 5.50976969e+05, 3.89531906e+05, 3.89032734e+05, 2.43976734e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.17307168e+04, 3.17359844e+04, 4.49310332e+04, 3.17464883e+04, 3.17277637e+04, 1.98820684e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.80892109e+05, 3.80871141e+05, 3.80964703e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.80892109e+05, 3.78712109e+05, 3.82985781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.56127219e+05, 4.47568500e+05, 4.40985422e+05, 3.88431609e+05, 3.80881172e+05, 3.74489375e+05, 3.34529906e+05, 3.27852156e+05, 3.21807844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.70001391e+05, 3.15316508e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.80879609e+05, 3.80751062e+05, 5.38840531e+05, 3.80931203e+05, 3.80687219e+05, 2.38754305e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.10366426e+04, 3.10300273e+04, 4.39339668e+04, 3.10415928e+04, 3.10417051e+04, 1.94541187e+04, ],
  }),
  ("nof_tree_events",                 395591),
  ("nof_db_events",                   395591),
  ("fsize_local",                     1584294346), # 1.58GB, avg file size 792.15MB
  ("fsize_db",                        19318646300), # 19.32GB, avg file size 804.94MB
  ("use_it",                          True),
  ("xsection",                        0.00265166),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH5_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 379997, ],
    'CountWeighted'                                                                  : [ 3.79965875e+05, 3.79896062e+05, 3.79950438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.86418750e+05, 4.59095594e+05, 4.33443688e+05, 4.02671125e+05, 3.79964438e+05, 3.58676875e+05, 3.39120812e+05, 3.19925250e+05, 3.01956125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.86418750e+05, 3.01956125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.68965188e+05, 3.68896094e+05, 3.68987688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.68965188e+05, 3.66313375e+05, 3.71547281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.72210125e+05, 4.45827906e+05, 4.21037000e+05, 3.90886156e+05, 3.68963375e+05, 3.48391875e+05, 3.29178969e+05, 3.10650531e+05, 2.93284438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.72210125e+05, 2.93284438e+05, ],
  }),
  ("nof_tree_events",                 379997),
  ("nof_db_events",                   379997),
  ("fsize_local",                     1772266263), # 1.77GB, avg file size 1.77GB
  ("fsize_db",                        20701310914), # 20.70GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99956500e+05, 3.99890062e+05, 3.99849375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19677375e+05, 4.78803281e+05, 4.42871625e+05, 4.34290438e+05, 3.99956500e+05, 3.69738844e+05, 3.68675250e+05, 3.39330938e+05, 3.13603031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19677438e+05, 3.13602938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.86454688e+05, 3.86414562e+05, 3.86391906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.86454688e+05, 3.83314875e+05, 3.89539812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.01965125e+05, 4.62712062e+05, 4.28177188e+05, 4.19440812e+05, 3.86454688e+05, 3.57426219e+05, 3.56030469e+05, 3.27856438e+05, 3.03131312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.01965219e+05, 3.03131250e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1986460975), # 1.99GB, avg file size 1.99GB
  ("fsize_db",                        23052019817), # 23.05GB, avg file size 1.54GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 382999, ],
    'CountWeighted'                                                                  : [ 3.82919406e+05, 3.83001250e+05, 3.82988594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.90277438e+05, 4.62670438e+05, 4.36736062e+05, 4.05892938e+05, 3.82919406e+05, 3.61453125e+05, 3.41837688e+05, 3.22477000e+05, 3.04324156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.90277438e+05, 3.04324156e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.71783188e+05, 3.71816312e+05, 3.71840812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.71783188e+05, 3.69098750e+05, 3.74398531e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.75876312e+05, 4.49214031e+05, 4.24144938e+05, 3.93951656e+05, 3.71783188e+05, 3.51014656e+05, 3.31768719e+05, 3.13072812e+05, 2.95525375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.75876312e+05, 2.95525375e+05, ],
  }),
  ("nof_tree_events",                 382999),
  ("nof_db_events",                   382999),
  ("fsize_local",                     1797409170), # 1.80GB, avg file size 1.80GB
  ("fsize_db",                        20935006290), # 20.94GB, avg file size 951.59MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 391999, ],
    'CountWeighted'                                                                  : [ 3.92007438e+05, 3.92043531e+05, 3.91910344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.99819625e+05, 4.74721438e+05, 4.50576125e+05, 4.12762062e+05, 3.92007438e+05, 3.72001781e+05, 3.46906500e+05, 3.29397062e+05, 3.12567688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.99819625e+05, 3.12567688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81311156e+05, 3.81321906e+05, 3.81263281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81311156e+05, 3.78704281e+05, 3.83836250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.86083094e+05, 4.61796344e+05, 4.38404719e+05, 4.01403469e+05, 3.81311156e+05, 3.61939062e+05, 3.37348188e+05, 3.20404469e+05, 3.04106562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.86083094e+05, 3.04106562e+05, ],
  }),
  ("nof_tree_events",                 391999),
  ("nof_db_events",                   391999),
  ("fsize_local",                     1788057498), # 1.79GB, avg file size 1.79GB
  ("fsize_db",                        21344876204), # 21.34GB, avg file size 970.22MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99899000e+05, 3.99932625e+05, 3.99929875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12975031e+05, 4.82669938e+05, 4.54490562e+05, 4.25171094e+05, 3.99899000e+05, 3.76546469e+05, 3.58426125e+05, 3.37101812e+05, 3.17319656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12975344e+05, 3.17319375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87974750e+05, 3.87963750e+05, 3.88025875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87974750e+05, 3.85110562e+05, 3.90771125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.97518562e+05, 4.68274375e+05, 4.41064094e+05, 4.12337938e+05, 3.87974750e+05, 3.65403219e+05, 3.47591719e+05, 3.27016812e+05, 3.07913562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.97518844e+05, 3.07913312e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1890750332), # 1.89GB, avg file size 1.89GB
  ("fsize_db",                        22416145291), # 22.42GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 396000, ],
    'CountWeighted'                                                                  : [ 3.96038625e+05, 3.95940750e+05, 3.95938750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.05183812e+05, 4.79426000e+05, 4.54701750e+05, 4.17308281e+05, 3.96032125e+05, 3.75533750e+05, 3.50806062e+05, 3.32836250e+05, 3.15618531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.05183812e+05, 3.15618531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.85039500e+05, 3.84974250e+05, 3.84980781e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.85039500e+05, 3.82364906e+05, 3.87629062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.91073125e+05, 4.66147969e+05, 4.42203344e+05, 4.05637781e+05, 3.85033906e+05, 3.65199375e+05, 3.40985750e+05, 3.23600188e+05, 3.06928625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.91073125e+05, 3.06928625e+05, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1814756331), # 1.81GB, avg file size 1.81GB
  ("fsize_db",                        21470016217), # 21.47GB, avg file size 1.34GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99895844e+05, 3.99970688e+05, 4.00048000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10129688e+05, 4.84349062e+05, 4.59582969e+05, 4.21310719e+05, 3.99895844e+05, 3.79486125e+05, 3.54112688e+05, 3.36147031e+05, 3.18893312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10129688e+05, 3.18893312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88968625e+05, 3.88986688e+05, 3.89082812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88968625e+05, 3.86297938e+05, 3.91559031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.96042688e+05, 4.71092750e+05, 4.47095562e+05, 4.09665250e+05, 3.88968625e+05, 3.69165500e+05, 3.44316094e+05, 3.26925438e+05, 3.10213844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.96042688e+05, 3.10213844e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1828878568), # 1.83GB, avg file size 1.83GB
  ("fsize_db",                        21847137342), # 21.85GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 395995, ],
    'CountWeighted'                                                                  : [ 3.96045906e+05, 3.95933656e+05, 3.95999188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.04858656e+05, 4.79596750e+05, 4.55260438e+05, 4.16883562e+05, 3.96045906e+05, 3.75841719e+05, 3.50342125e+05, 3.32726938e+05, 3.15789469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.04858656e+05, 3.15789469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.85262688e+05, 3.85175062e+05, 3.85244531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.85262688e+05, 3.82633281e+05, 3.87808906e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.91035688e+05, 4.66583500e+05, 4.43006062e+05, 4.05457938e+05, 3.85262688e+05, 3.65714469e+05, 3.40728812e+05, 3.23680188e+05, 3.07271219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.91035688e+05, 3.07271219e+05, ],
  }),
  ("nof_tree_events",                 395995),
  ("nof_db_events",                   395995),
  ("fsize_local",                     1806742986), # 1.81GB, avg file size 1.81GB
  ("fsize_db",                        21294763606), # 21.29GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99939688e+05, 3.99878250e+05, 3.99909312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19409375e+05, 4.78830938e+05, 4.42995188e+05, 4.33928562e+05, 3.99939688e+05, 3.69907062e+05, 3.68228656e+05, 3.39285312e+05, 3.13755312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19409375e+05, 3.13755312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.86364875e+05, 3.86311938e+05, 3.86365125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.86364875e+05, 3.83196188e+05, 3.89477125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.01643875e+05, 4.62618688e+05, 4.28127312e+05, 4.19061062e+05, 3.86364875e+05, 3.57469062e+05, 3.55594031e+05, 3.27759438e+05, 3.03191469e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.01643875e+05, 3.03191469e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     2029419511), # 2.03GB, avg file size 2.03GB
  ("fsize_db",                        23472759858), # 23.47GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 391996, ],
    'CountWeighted'                                                                  : [ 3.91944812e+05, 3.92051688e+05, 3.91874250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.99933438e+05, 4.74655875e+05, 4.50354312e+05, 4.12904938e+05, 3.91934219e+05, 3.71872719e+05, 3.47049906e+05, 3.29414625e+05, 3.12498125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.99933500e+05, 3.12498062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81137188e+05, 3.81204000e+05, 3.81099875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81137188e+05, 3.78513906e+05, 3.83691688e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.86030469e+05, 4.61576750e+05, 4.38046438e+05, 4.01406562e+05, 3.81128875e+05, 3.61697375e+05, 3.37377125e+05, 3.20319469e+05, 3.03938625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.86030531e+05, 3.03938562e+05, ],
  }),
  ("nof_tree_events",                 391996),
  ("nof_db_events",                   391996),
  ("fsize_local",                     1792867546), # 1.79GB, avg file size 1.79GB
  ("fsize_db",                        21244437020), # 21.24GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 4.00010656e+05, 4.00003875e+05, 3.99939062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10460438e+05, 4.84147688e+05, 4.58939656e+05, 4.21770750e+05, 4.00003094e+05, 3.79123031e+05, 3.54620875e+05, 3.36252500e+05, 3.18700500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10460438e+05, 3.18700438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88927562e+05, 3.88908844e+05, 3.88892250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88927562e+05, 3.86229469e+05, 3.91539719e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.96225781e+05, 4.70762000e+05, 4.46351000e+05, 4.09997094e+05, 3.88921562e+05, 3.68713031e+05, 3.44711531e+05, 3.26939438e+05, 3.09941438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.96225781e+05, 3.09941375e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1838375868), # 1.84GB, avg file size 1.84GB
  ("fsize_db",                        21689984880), # 21.69GB, avg file size 1.28GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 394000, ],
    'CountWeighted'                                                                  : [ 3.93914000e+05, 3.93999125e+05, 3.93941625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.02311688e+05, 4.77199875e+05, 4.52976438e+05, 4.14771188e+05, 3.93913781e+05, 3.73949656e+05, 3.48555938e+05, 3.31031625e+05, 3.14192531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.02311688e+05, 3.14192500e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.83178438e+05, 3.83230594e+05, 3.83198281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.83178438e+05, 3.80554438e+05, 3.85723469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.88490469e+05, 4.64181812e+05, 4.40721219e+05, 4.03344688e+05, 3.83177500e+05, 3.63822062e+05, 3.38941844e+05, 3.21988000e+05, 3.05674562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.88490469e+05, 3.05674562e+05, ],
  }),
  ("nof_tree_events",                 394000),
  ("nof_db_events",                   394000),
  ("fsize_local",                     1796731124), # 1.80GB, avg file size 1.80GB
  ("fsize_db",                        21086443719), # 21.09GB, avg file size 1.62GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo4V_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    74),
  ("nof_events",                      {
    'Count'                                                                          : [ 999992, ],
    'CountWeighted'                                                                  : [ 9.41119406e+05, 9.41134438e+05, 9.41174672e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.08848938e+06, 1.06943397e+06, 1.05603791e+06, 9.62564438e+05, 9.41119406e+05, 9.23902156e+05, 8.53666297e+05, 8.31616297e+05, 8.12804453e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.12731481e+06, 7.93624109e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.41173578e+05, 9.40441203e+05, 1.36379288e+06, 9.41065375e+05, 9.40416656e+05, 5.61377844e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 6.40770859e+04, 6.40472568e+04, 9.29430566e+04, 6.40752812e+04, 6.40893955e+04, 3.82120332e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.20508469e+05, 9.20495797e+05, 9.20556891e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.20508469e+05, 9.15248594e+05, 9.25547594e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06430072e+06, 1.04588623e+06, 1.03297352e+06, 9.41276875e+05, 9.20508469e+05, 9.03837562e+05, 8.34847781e+05, 8.13468203e+05, 7.95223312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.10231338e+06, 7.76451312e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.20656547e+05, 9.19604219e+05, 1.33380159e+06, 9.20329859e+05, 9.20236375e+05, 5.49321312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 6.26621465e+04, 6.26096533e+04, 9.08732656e+04, 6.26446582e+04, 6.26964883e+04, 3.73802373e+04, ],
  }),
  ("nof_tree_events",                 999992),
  ("nof_db_events",                   999992),
  ("fsize_local",                     4401470243), # 4.40GB, avg file size 1.10GB
  ("fsize_db",                        51563406070), # 51.56GB, avg file size 696.80MB
  ("use_it",                          True),
  ("xsection",                        0.00385439),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH0_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo4V_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    53),
  ("nof_events",                      {
    'Count'                                                                          : [ 963693, ],
    'CountWeighted'                                                                  : [ 8.63450016e+05, 8.63367266e+05, 8.63424750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.82849672e+05, 9.67203906e+05, 9.56899797e+05, 8.83250281e+05, 8.63397766e+05, 8.47807328e+05, 7.92834906e+05, 7.71213641e+05, 7.53099594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.02526606e+06, 7.29957922e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.63095891e+05, 8.63102750e+05, 1.25243769e+06, 8.63811203e+05, 8.62238203e+05, 5.13989227e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.87884595e+04, 2.87794463e+04, 4.18346475e+04, 2.88078604e+04, 2.88346841e+04, 1.71462507e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.43204516e+05, 8.43106953e+05, 8.43250016e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.43204516e+05, 8.38113344e+05, 8.48108016e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.59494344e+05, 9.44426438e+05, 9.34551547e+05, 8.62364719e+05, 8.43161188e+05, 8.28120047e+05, 7.74151203e+05, 7.53219656e+05, 7.35683984e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00095155e+06, 7.13069219e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.42988812e+05, 8.42615781e+05, 1.22296388e+06, 8.43443625e+05, 8.42471328e+05, 5.02190227e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.81098574e+04, 2.80885757e+04, 4.08382002e+04, 2.81204941e+04, 2.81652051e+04, 1.67481890e+04, ],
  }),
  ("nof_tree_events",                 963693),
  ("nof_db_events",                   963693),
  ("fsize_local",                     4378289511), # 4.38GB, avg file size 1.09GB
  ("fsize_db",                        50159794192), # 50.16GB, avg file size 946.41MB
  ("use_it",                          True),
  ("xsection",                        0.00171641),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH1_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo4V_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    63),
  ("nof_events",                      {
    'Count'                                                                          : [ 999996, ],
    'CountWeighted'                                                                  : [ 8.61863875e+05, 8.61982250e+05, 8.61825766e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.82960656e+05, 9.69436703e+05, 9.60813750e+05, 8.79381031e+05, 8.61859562e+05, 8.48131438e+05, 7.87038484e+05, 7.67738531e+05, 7.51484406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03520162e+06, 7.19598891e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.61759328e+05, 8.61961891e+05, 1.25138638e+06, 8.62003328e+05, 8.59598266e+05, 5.11507648e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.31346560e+04, 1.31395608e+04, 1.90839604e+04, 1.31356467e+04, 1.31121006e+04, 7.79717847e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.41422500e+05, 8.41514828e+05, 8.41412672e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.41422500e+05, 8.36309672e+05, 8.46344562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.59272156e+05, 9.46309797e+05, 9.38103672e+05, 8.58303922e+05, 8.41411438e+05, 8.28213453e+05, 7.68245375e+05, 7.49613031e+05, 7.33916844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.01033717e+06, 7.02750000e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.41472859e+05, 8.41378281e+05, 1.22141400e+06, 8.41381922e+05, 8.39388172e+05, 4.99638648e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.28201785e+04, 1.28202644e+04, 1.86203154e+04, 1.28161887e+04, 1.27997498e+04, 7.61287659e+03, ],
  }),
  ("nof_tree_events",                 999996),
  ("nof_db_events",                   999996),
  ("fsize_local",                     4512892780), # 4.51GB, avg file size 1.13GB
  ("fsize_db",                        52111900186), # 52.11GB, avg file size 827.17MB
  ("use_it",                          True),
  ("xsection",                        0.00072699),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2017["/GluGluToHHTo4V_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    42),
  ("nof_events",                      {
    'Count'                                                                          : [ 999995, ],
    'CountWeighted'                                                                  : [ 9.84275656e+05, 9.84303500e+05, 9.84293141e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17920944e+06, 1.15681609e+06, 1.13958131e+06, 1.00401247e+06, 9.84226984e+05, 9.67553484e+05, 8.64512688e+05, 8.47067938e+05, 8.31296969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.21512141e+06, 8.14476547e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.84252172e+05, 9.84553141e+05, 1.42333678e+06, 9.84319641e+05, 9.80600391e+05, 5.87952312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 8.02275254e+04, 8.02429199e+04, 1.16176324e+05, 8.02310312e+04, 8.00910312e+04, 4.79213594e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.64972891e+05, 9.64956109e+05, 9.65030250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.64972891e+05, 9.59940953e+05, 9.69747781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.15552272e+06, 1.13387078e+06, 1.11722822e+06, 9.84076406e+05, 9.64932625e+05, 9.48785594e+05, 8.47497375e+05, 8.30600688e+05, 8.15308875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.19081250e+06, 7.98778875e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.65100312e+05, 9.65005422e+05, 1.39513622e+06, 9.64824391e+05, 9.61752469e+05, 5.76758875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 7.86593789e+04, 7.86422383e+04, 1.13863523e+05, 7.86346445e+04, 7.85438438e+04, 4.70043604e+04, ],
  }),
  ("nof_tree_events",                 999995),
  ("nof_db_events",                   999995),
  ("fsize_local",                     4052868482), # 4.05GB, avg file size 1.01GB
  ("fsize_db",                        49489862385), # 49.49GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.00507095),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH5_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

