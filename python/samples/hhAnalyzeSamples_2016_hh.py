from collections import OrderedDict as OD

# file generated at 2020-08-24 20:01:00 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_hh.py -M

samples_2016 = OD()
samples_2016["/GluGluToRadionToHHTo4Tau_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99842109e+04, 1.00002930e+05, 9.99984844e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.01618172e+05, 9.99840156e+04, 9.78144062e+04, 1.01618172e+05, 9.99840156e+04, 9.78144062e+04, 1.01618172e+05, 9.99840156e+04, 9.78144062e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.01618172e+05, 9.78144062e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.85401094e+04, 9.85487656e+04, 9.85527188e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.85401094e+04, 9.81517344e+04, 9.89247891e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.00132750e+05, 9.85395547e+04, 9.64066016e+04, 1.00132750e+05, 9.85395547e+04, 9.64066016e+04, 1.00132750e+05, 9.85395547e+04, 9.64066016e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00132750e+05, 9.64066016e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     355692868), # 355.69MB, avg file size 355.69MB
  ("fsize_db",                        3874786969), # 3.87GB, avg file size 1.94GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99204, ],
    'CountWeighted'                                                                  : [ 9.91955312e+04, 9.92114531e+04, 9.92246172e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.01102273e+05, 9.91952969e+04, 9.68024609e+04, 1.01102273e+05, 9.91952969e+04, 9.68024609e+04, 1.01102273e+05, 9.91952969e+04, 9.68024609e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.01102273e+05, 9.68024609e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.77267891e+04, 9.77302031e+04, 9.77503359e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.77267891e+04, 9.73338594e+04, 9.81162344e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.95891406e+04, 9.77262578e+04, 9.53754844e+04, 9.95891406e+04, 9.77262578e+04, 9.53754844e+04, 9.95891406e+04, 9.77262578e+04, 9.53754844e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.95891406e+04, 9.53754844e+04, ],
  }),
  ("nof_tree_events",                 99204),
  ("nof_db_events",                   99204),
  ("fsize_local",                     357798293), # 357.80MB, avg file size 357.80MB
  ("fsize_db",                        3865138450), # 3.87GB, avg file size 3.87GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99987734e+04, 9.99978594e+04, 9.99978047e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.02214961e+05, 9.99930156e+04, 9.73355391e+04, 1.02214961e+05, 9.99930156e+04, 9.73355391e+04, 1.02214961e+05, 9.99930156e+04, 9.73355391e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.02214961e+05, 9.73355391e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.84414219e+04, 9.84372734e+04, 9.84447969e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.84414219e+04, 9.80287812e+04, 9.88503906e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.00609664e+05, 9.84375234e+04, 9.58300859e+04, 1.00609664e+05, 9.84375234e+04, 9.58300859e+04, 1.00609664e+05, 9.84375234e+04, 9.58300859e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00609664e+05, 9.58300859e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     365837331), # 365.84MB, avg file size 365.84MB
  ("fsize_db",                        3829876445), # 3.83GB, avg file size 1.91GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 98567, ],
    'CountWeighted'                                                                  : [ 9.85633828e+04, 9.85756641e+04, 9.85579297e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.01012320e+05, 9.85627578e+04, 9.57350859e+04, 1.01012320e+05, 9.85627578e+04, 9.57350859e+04, 1.01012320e+05, 9.85627578e+04, 9.57350859e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.01012320e+05, 9.57350859e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70055234e+04, 9.70116016e+04, 9.70074062e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70055234e+04, 9.65955547e+04, 9.74155703e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.94010469e+04, 9.70044922e+04, 9.42323359e+04, 9.94010469e+04, 9.70044922e+04, 9.42323359e+04, 9.94010469e+04, 9.70044922e+04, 9.42323359e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.94010469e+04, 9.42323359e+04, ],
  }),
  ("nof_tree_events",                 98567),
  ("nof_db_events",                   98567),
  ("fsize_local",                     364621676), # 364.62MB, avg file size 364.62MB
  ("fsize_db",                        3900002340), # 3.90GB, avg file size 1.95GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 94730, ],
    'CountWeighted'                                                                  : [ 9.47288359e+04, 9.47177969e+04, 9.47170781e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.75562266e+04, 9.47266562e+04, 9.16262812e+04, 9.75562266e+04, 9.47266562e+04, 9.16262812e+04, 9.75562266e+04, 9.47266562e+04, 9.16262812e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.75562266e+04, 9.16262812e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.31726953e+04, 9.31647812e+04, 9.31670234e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.31726953e+04, 9.27647656e+04, 9.35785938e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.59384844e+04, 9.31710391e+04, 9.01307578e+04, 9.59384844e+04, 9.31710391e+04, 9.01307578e+04, 9.59384844e+04, 9.31710391e+04, 9.01307578e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.59384844e+04, 9.01307578e+04, ],
  }),
  ("nof_tree_events",                 94730),
  ("nof_db_events",                   94730),
  ("fsize_local",                     358324529), # 358.32MB, avg file size 358.32MB
  ("fsize_db",                        3783167238), # 3.78GB, avg file size 1.89GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99934297e+04, 1.00014250e+05, 1.00013695e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.03476656e+05, 9.99930234e+04, 9.63385703e+04, 1.03476656e+05, 9.99930234e+04, 9.63385703e+04, 1.03476656e+05, 9.99930234e+04, 9.63385703e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03476656e+05, 9.63385703e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.82577969e+04, 9.82666641e+04, 9.82750781e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.82577969e+04, 9.78076094e+04, 9.87077656e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.01661367e+05, 9.82570469e+04, 9.46760703e+04, 1.01661367e+05, 9.82570469e+04, 9.46760703e+04, 1.01661367e+05, 9.82570469e+04, 9.46760703e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.01661367e+05, 9.46760703e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     386362402), # 386.36MB, avg file size 386.36MB
  ("fsize_db",                        3916703835), # 3.92GB, avg file size 1.96GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99849453e+04, 1.00031766e+05, 1.00019320e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.03907734e+05, 9.99847422e+04, 9.59960859e+04, 1.03907734e+05, 9.99847422e+04, 9.59960859e+04, 1.03907734e+05, 9.99847422e+04, 9.59960859e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03907734e+05, 9.59960859e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.81691406e+04, 9.81915078e+04, 9.81936562e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.81691406e+04, 9.76990469e+04, 9.86361875e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.01998117e+05, 9.81685156e+04, 9.42578750e+04, 1.01998117e+05, 9.81685156e+04, 9.42578750e+04, 1.01998117e+05, 9.81685156e+04, 9.42578750e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.01998117e+05, 9.42578750e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     393923436), # 393.92MB, avg file size 393.92MB
  ("fsize_db",                        3984955042), # 3.98GB, avg file size 1.99GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_340_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 98356, ],
    'CountWeighted'                                                                  : [ 9.83407422e+04, 9.83567734e+04, 9.83692422e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.02414094e+05, 9.83398359e+04, 9.42459766e+04, 1.02414094e+05, 9.83398359e+04, 9.42459766e+04, 1.02414094e+05, 9.83398359e+04, 9.42459766e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.02414094e+05, 9.42459766e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.65584922e+04, 9.65690234e+04, 9.65753516e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.65584922e+04, 9.60983359e+04, 9.70179531e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.00536383e+05, 9.65573672e+04, 9.25453516e+04, 1.00536383e+05, 9.65573672e+04, 9.25453516e+04, 1.00536383e+05, 9.65573672e+04, 9.25453516e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00536383e+05, 9.25453516e+04, ],
  }),
  ("nof_tree_events",                 98356),
  ("nof_db_events",                   98356),
  ("fsize_local",                     391368218), # 391.37MB, avg file size 391.37MB
  ("fsize_db",                        4031403477), # 4.03GB, avg file size 2.02GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 97614, ],
    'CountWeighted'                                                                  : [ 9.76113828e+04, 9.76283438e+04, 9.76203828e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.02562062e+05, 9.76090938e+04, 9.28191953e+04, 1.02562062e+05, 9.76090938e+04, 9.28191953e+04, 1.02562062e+05, 9.76090938e+04, 9.28191953e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.02562062e+05, 9.28191953e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.56989688e+04, 9.57043438e+04, 9.57090938e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.56989688e+04, 9.52133359e+04, 9.61841016e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.00535953e+05, 9.56970781e+04, 9.10121953e+04, 1.00535953e+05, 9.56970781e+04, 9.10121953e+04, 1.00535953e+05, 9.56970781e+04, 9.10121953e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00535953e+05, 9.10121953e+04, ],
  }),
  ("nof_tree_events",                 97614),
  ("nof_db_events",                   97614),
  ("fsize_local",                     405986995), # 405.99MB, avg file size 405.99MB
  ("fsize_db",                        4056144350), # 4.06GB, avg file size 2.03GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 1.00035867e+05, 1.00015391e+05, 9.99826250e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.05910008e+05, 1.00035578e+05, 9.44479609e+04, 1.05910008e+05, 1.00035578e+05, 9.44479609e+04, 1.05910008e+05, 1.00035578e+05, 9.44479609e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.05910008e+05, 9.44479609e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.79573750e+04, 9.79413672e+04, 9.79311250e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.79573750e+04, 9.74378750e+04, 9.84761094e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.03705617e+05, 9.79567031e+04, 9.25123906e+04, 1.03705617e+05, 9.79567031e+04, 9.25123906e+04, 1.03705617e+05, 9.79567031e+04, 9.25123906e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.03705617e+05, 9.25123906e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     431019652), # 431.02MB, avg file size 431.02MB
  ("fsize_db",                        4254873375), # 4.25GB, avg file size 2.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 4.99993633e+04, 5.00020742e+04, 5.00045898e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.33123047e+04, 4.99975469e+04, 4.69473125e+04, 5.33123047e+04, 4.99975469e+04, 4.69473125e+04, 5.33123047e+04, 4.99975469e+04, 4.69473125e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.33123047e+04, 4.69473125e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.89386328e+04, 4.89377109e+04, 4.89437266e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.89386328e+04, 4.86724609e+04, 4.92044219e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.21725273e+04, 4.89373359e+04, 4.59574375e+04, 5.21725273e+04, 4.89373359e+04, 4.59574375e+04, 5.21725273e+04, 4.89373359e+04, 4.59574375e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.21725273e+04, 4.59574375e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     223459823), # 223.46MB, avg file size 223.46MB
  ("fsize_db",                        2208888272), # 2.21GB, avg file size 2.21GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 5.00012344e+04, 5.00026680e+04, 5.00037773e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.36450273e+04, 5.00006914e+04, 4.66945898e+04, 5.36450273e+04, 5.00006914e+04, 4.66945898e+04, 5.36450273e+04, 5.00006914e+04, 4.66945898e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.36450273e+04, 4.66945898e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.88942031e+04, 4.88929609e+04, 4.88974531e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.88942031e+04, 4.86178555e+04, 4.91702109e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.24481406e+04, 4.88935820e+04, 4.56682266e+04, 5.24481406e+04, 4.88935820e+04, 4.56682266e+04, 5.24481406e+04, 4.88935820e+04, 4.56682266e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.24481406e+04, 4.56682266e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     229509166), # 229.51MB, avg file size 229.51MB
  ("fsize_db",                        2111067830), # 2.11GB, avg file size 2.11GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 5.00010703e+04, 5.00024961e+04, 4.99999727e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.39346641e+04, 4.99986680e+04, 4.64752266e+04, 5.39346641e+04, 4.99986680e+04, 4.64752266e+04, 5.39346641e+04, 4.99986680e+04, 4.64752266e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.39346641e+04, 4.64752266e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.88572734e+04, 4.88549375e+04, 4.88595000e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.88572734e+04, 4.85741211e+04, 4.91399414e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.26927109e+04, 4.88555469e+04, 4.54194375e+04, 5.26927109e+04, 4.88555469e+04, 4.54194375e+04, 5.26927109e+04, 4.88555469e+04, 4.54194375e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.26927109e+04, 4.54194375e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     235117280), # 235.12MB, avg file size 235.12MB
  ("fsize_db",                        2253668540), # 2.25GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 48463, ],
    'CountWeighted'                                                                  : [ 4.84710234e+04, 4.84620898e+04, 4.84675156e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.25383906e+04, 4.84708867e+04, 4.48554297e+04, 5.25383906e+04, 4.84708867e+04, 4.48554297e+04, 5.25383906e+04, 4.84708867e+04, 4.48554297e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.25383906e+04, 4.48554297e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.73220742e+04, 4.73175234e+04, 4.73188555e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.73220742e+04, 4.70398008e+04, 4.76045391e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.12880977e+04, 4.73217500e+04, 4.38010938e+04, 5.12880977e+04, 4.73217500e+04, 4.38010938e+04, 5.12880977e+04, 4.73217500e+04, 4.38010938e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.12880977e+04, 4.38010938e+04, ],
  }),
  ("nof_tree_events",                 48463),
  ("nof_db_events",                   48463),
  ("fsize_local",                     233309684), # 233.31MB, avg file size 233.31MB
  ("fsize_db",                        2355229431), # 2.36GB, avg file size 2.36GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 4.99983438e+04, 4.99976133e+04, 4.99958203e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.44534023e+04, 4.99964609e+04, 4.60924219e+04, 5.44534023e+04, 4.99964609e+04, 4.60924219e+04, 5.44534023e+04, 4.99964609e+04, 4.60924219e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.44534023e+04, 4.60924219e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.88012812e+04, 4.87967852e+04, 4.88044492e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.88012812e+04, 4.85079844e+04, 4.90947461e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.31405000e+04, 4.87997461e+04, 4.49947305e+04, 5.31405000e+04, 4.87997461e+04, 4.49947305e+04, 5.31405000e+04, 4.87997461e+04, 4.49947305e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.31405000e+04, 4.49947305e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     245720862), # 245.72MB, avg file size 245.72MB
  ("fsize_db",                        2263100514), # 2.26GB, avg file size 2.26GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 4.99963359e+04, 5.00077305e+04, 5.00008984e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.46793828e+04, 4.99962188e+04, 4.59256602e+04, 5.46793828e+04, 4.99962188e+04, 4.59256602e+04, 5.46793828e+04, 4.99962188e+04, 4.59256602e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.46793828e+04, 4.59256602e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.87883867e+04, 4.87970117e+04, 4.87883477e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.87883867e+04, 4.84915586e+04, 4.90851992e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.33488398e+04, 4.87881289e+04, 4.48208242e+04, 5.33488398e+04, 4.87881289e+04, 4.48208242e+04, 5.33488398e+04, 4.87881289e+04, 4.48208242e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.33488398e+04, 4.48208242e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     250003966), # 250.00MB, avg file size 250.00MB
  ("fsize_db",                        2299577348), # 2.30GB, avg file size 1.15GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 5.00072578e+04, 5.00015000e+04, 4.99983867e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.48947188e+04, 5.00070703e+04, 4.57681445e+04, 5.48947188e+04, 5.00070703e+04, 4.57681445e+04, 5.48947188e+04, 5.00070703e+04, 4.57681445e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.48947188e+04, 4.57681445e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.87867891e+04, 4.87850547e+04, 4.87802422e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.87867891e+04, 4.84882539e+04, 4.90856250e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.35503555e+04, 4.87864062e+04, 4.46594883e+04, 5.35503555e+04, 4.87864062e+04, 4.46594883e+04, 5.35503555e+04, 4.87864062e+04, 4.46594883e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.35503555e+04, 4.46594883e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     254168863), # 254.17MB, avg file size 254.17MB
  ("fsize_db",                        2263981849), # 2.26GB, avg file size 2.26GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 5.00022500e+04, 5.00020312e+04, 4.99943047e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.52771016e+04, 5.00020977e+04, 4.54891875e+04, 5.52771016e+04, 5.00020977e+04, 4.54891875e+04, 5.52771016e+04, 5.00020977e+04, 4.54891875e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.52771016e+04, 4.54891875e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.87492070e+04, 4.87474023e+04, 4.87464102e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.87492070e+04, 4.84447305e+04, 4.90543750e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.38860430e+04, 4.87488789e+04, 4.43558750e+04, 5.38860430e+04, 4.87488789e+04, 4.43558750e+04, 5.38860430e+04, 4.87488789e+04, 4.43558750e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.38860430e+04, 4.43558750e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     261024278), # 261.02MB, avg file size 261.02MB
  ("fsize_db",                        2478591891), # 2.48GB, avg file size 2.48GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99430, ],
    'CountWeighted'                                                                  : [ 9.94342500e+04, 9.94362734e+04, 9.94290859e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.01035336e+05, 9.94341016e+04, 9.72616250e+04, 1.01035336e+05, 9.94341016e+04, 9.72616250e+04, 1.01035336e+05, 9.94341016e+04, 9.72616250e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.01035336e+05, 9.72616250e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.79381562e+04, 9.79368672e+04, 9.79418516e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.79381562e+04, 9.75418203e+04, 9.83335391e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.95055078e+04, 9.79375078e+04, 9.58099531e+04, 9.95055078e+04, 9.79375078e+04, 9.58099531e+04, 9.95055078e+04, 9.79375078e+04, 9.58099531e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.95055078e+04, 9.58099531e+04, ],
  }),
  ("nof_tree_events",                 99430),
  ("nof_db_events",                   99430),
  ("fsize_local",                     360960250), # 360.96MB, avg file size 360.96MB
  ("fsize_db",                        3877049177), # 3.88GB, avg file size 1.94GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 97772, ],
    'CountWeighted'                                                                  : [ 9.77424297e+04, 9.77740391e+04, 9.77618672e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.96510547e+04, 9.77421875e+04, 9.53926094e+04, 9.96510547e+04, 9.77421875e+04, 9.53926094e+04, 9.96510547e+04, 9.77421875e+04, 9.53926094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.96510547e+04, 9.53926094e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.62463281e+04, 9.62587109e+04, 9.62616484e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.62463281e+04, 9.58450625e+04, 9.66430312e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.81007734e+04, 9.62456172e+04, 9.39322109e+04, 9.81007734e+04, 9.62456172e+04, 9.39322109e+04, 9.81007734e+04, 9.62456172e+04, 9.39322109e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.81007734e+04, 9.39322109e+04, ],
  }),
  ("nof_tree_events",                 97772),
  ("nof_db_events",                   97772),
  ("fsize_local",                     360160348), # 360.16MB, avg file size 360.16MB
  ("fsize_db",                        3871755682), # 3.87GB, avg file size 1.94GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 1.00004250e+05, 9.99859766e+04, 9.99754141e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.02211461e+05, 1.00001602e+05, 9.73391797e+04, 1.02211461e+05, 1.00001602e+05, 9.73391797e+04, 1.02211461e+05, 1.00001602e+05, 9.73391797e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.02211461e+05, 9.73391797e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.84047812e+04, 9.83916328e+04, 9.83893516e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.84047812e+04, 9.79841641e+04, 9.88233906e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.00564562e+05, 9.84026641e+04, 9.57945078e+04, 1.00564562e+05, 9.84026641e+04, 9.57945078e+04, 1.00564562e+05, 9.84026641e+04, 9.57945078e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00564562e+05, 9.57945078e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     373788092), # 373.79MB, avg file size 373.79MB
  ("fsize_db",                        3873301459), # 3.87GB, avg file size 1.94GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 98688, ],
    'CountWeighted'                                                                  : [ 9.86865703e+04, 9.86775703e+04, 9.86805391e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.01137242e+05, 9.86820781e+04, 9.58455938e+04, 1.01137242e+05, 9.86820781e+04, 9.58455938e+04, 1.01137242e+05, 9.86820781e+04, 9.58455938e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.01137242e+05, 9.58455938e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70517422e+04, 9.70404453e+04, 9.70527891e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70517422e+04, 9.66234297e+04, 9.74767344e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.94463281e+04, 9.70481094e+04, 9.42688828e+04, 9.94463281e+04, 9.70481094e+04, 9.42688828e+04, 9.94463281e+04, 9.70481094e+04, 9.42688828e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.94463281e+04, 9.42688828e+04, ],
  }),
  ("nof_tree_events",                 98688),
  ("nof_db_events",                   98688),
  ("fsize_local",                     373896636), # 373.90MB, avg file size 373.90MB
  ("fsize_db",                        4085852491), # 4.09GB, avg file size 2.04GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99502, ],
    'CountWeighted'                                                                  : [ 9.95110781e+04, 9.95142109e+04, 9.94857500e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.02482258e+05, 9.95102266e+04, 9.62261172e+04, 1.02482258e+05, 9.95102266e+04, 9.62261172e+04, 1.02482258e+05, 9.95102266e+04, 9.62261172e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.02482258e+05, 9.62261172e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.77931875e+04, 9.77936562e+04, 9.77796406e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.77931875e+04, 9.73483359e+04, 9.82362344e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.00702344e+05, 9.77921250e+04, 9.45814688e+04, 1.00702344e+05, 9.77921250e+04, 9.45814688e+04, 1.00702344e+05, 9.77921250e+04, 9.45814688e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00702344e+05, 9.45814688e+04, ],
  }),
  ("nof_tree_events",                 99502),
  ("nof_db_events",                   99502),
  ("fsize_local",                     387402781), # 387.40MB, avg file size 387.40MB
  ("fsize_db",                        3937638636), # 3.94GB, avg file size 1.97GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 97676, ],
    'CountWeighted'                                                                  : [ 9.76805000e+04, 9.76709062e+04, 9.76727578e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.01064328e+05, 9.76790234e+04, 9.41049219e+04, 1.01064328e+05, 9.76790234e+04, 9.41049219e+04, 1.01064328e+05, 9.76790234e+04, 9.41049219e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.01064328e+05, 9.41049219e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.59358125e+04, 9.59292656e+04, 9.59366484e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.59358125e+04, 9.54875078e+04, 9.63841719e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.92441797e+04, 9.59343047e+04, 9.24398984e+04, 9.92441797e+04, 9.59343047e+04, 9.24398984e+04, 9.92441797e+04, 9.59343047e+04, 9.24398984e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.92441797e+04, 9.24398984e+04, ],
  }),
  ("nof_tree_events",                 97676),
  ("nof_db_events",                   97676),
  ("fsize_local",                     388479698), # 388.48MB, avg file size 388.48MB
  ("fsize_db",                        3947093624), # 3.95GB, avg file size 3.95GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99226, ],
    'CountWeighted'                                                                  : [ 9.92229375e+04, 9.92352422e+04, 9.92217578e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.03124562e+05, 9.92225938e+04, 9.52363594e+04, 1.03124562e+05, 9.92225938e+04, 9.52363594e+04, 1.03124562e+05, 9.92225938e+04, 9.52363594e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03124562e+05, 9.52363594e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.74127656e+04, 9.74175469e+04, 9.74129453e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.74127656e+04, 9.69475547e+04, 9.78756406e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.01222945e+05, 9.74121016e+04, 9.35110625e+04, 1.01222945e+05, 9.74121016e+04, 9.35110625e+04, 1.01222945e+05, 9.74121016e+04, 9.35110625e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.01222945e+05, 9.35110625e+04, ],
  }),
  ("nof_tree_events",                 99226),
  ("nof_db_events",                   99226),
  ("fsize_local",                     403209905), # 403.21MB, avg file size 403.21MB
  ("fsize_db",                        4027035901), # 4.03GB, avg file size 2.01GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_340_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 98212, ],
    'CountWeighted'                                                                  : [ 9.82239453e+04, 9.82141016e+04, 9.81968594e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.02261648e+05, 9.82162266e+04, 9.41107266e+04, 1.02261648e+05, 9.82162266e+04, 9.41107266e+04, 1.02261648e+05, 9.82162266e+04, 9.41107266e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.02261648e+05, 9.41107266e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.63912812e+04, 9.63836562e+04, 9.63790625e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.63912812e+04, 9.59262344e+04, 9.68572812e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.00341289e+05, 9.63858594e+04, 9.23741953e+04, 1.00341289e+05, 9.63858594e+04, 9.23741953e+04, 1.00341289e+05, 9.63858594e+04, 9.23741953e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00341289e+05, 9.23741953e+04, ],
  }),
  ("nof_tree_events",                 98212),
  ("nof_db_events",                   98212),
  ("fsize_local",                     403461559), # 403.46MB, avg file size 403.46MB
  ("fsize_db",                        4125701387), # 4.13GB, avg file size 2.06GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 98789, ],
    'CountWeighted'                                                                  : [ 9.87823047e+04, 9.87825234e+04, 9.88054609e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.03797344e+05, 9.87818516e+04, 9.39310781e+04, 1.03797344e+05, 9.87818516e+04, 9.39310781e+04, 1.03797344e+05, 9.87818516e+04, 9.39310781e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03797344e+05, 9.39310781e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.68846328e+04, 9.68803203e+04, 9.69023438e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.68846328e+04, 9.64062031e+04, 9.73642891e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.01781117e+05, 9.68840312e+04, 9.21395781e+04, 1.01781117e+05, 9.68840312e+04, 9.21395781e+04, 1.01781117e+05, 9.68840312e+04, 9.21395781e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.01781117e+05, 9.21395781e+04, ],
  }),
  ("nof_tree_events",                 98789),
  ("nof_db_events",                   98789),
  ("fsize_local",                     424663258), # 424.66MB, avg file size 424.66MB
  ("fsize_db",                        4251757973), # 4.25GB, avg file size 2.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 1.00008430e+05, 1.00015242e+05, 1.00004484e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.05911102e+05, 1.00008008e+05, 9.44406484e+04, 1.05911102e+05, 1.00008008e+05, 9.44406484e+04, 1.05911102e+05, 1.00008008e+05, 9.44406484e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.05911102e+05, 9.44406484e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.80546016e+04, 9.80533047e+04, 9.80578281e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.80546016e+04, 9.75648281e+04, 9.85442109e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.03824367e+05, 9.80538984e+04, 9.26133281e+04, 1.03824367e+05, 9.80538984e+04, 9.26133281e+04, 1.03824367e+05, 9.80538984e+04, 9.26133281e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.03824367e+05, 9.26133281e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     446475948), # 446.48MB, avg file size 446.48MB
  ("fsize_db",                        4221394903), # 4.22GB, avg file size 2.11GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 49535, ],
    'CountWeighted'                                                                  : [ 4.95344336e+04, 4.95371953e+04, 4.95290117e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.28274531e+04, 4.95343164e+04, 4.65026289e+04, 5.28274531e+04, 4.95343164e+04, 4.65026289e+04, 5.28274531e+04, 4.95343164e+04, 4.65026289e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.28274531e+04, 4.65026289e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.85554609e+04, 4.85556562e+04, 4.85539453e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.85554609e+04, 4.83123438e+04, 4.87990312e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.17739766e+04, 4.85551484e+04, 4.55903867e+04, 5.17739766e+04, 4.85551484e+04, 4.55903867e+04, 5.17739766e+04, 4.85551484e+04, 4.55903867e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.17739766e+04, 4.55903867e+04, ],
  }),
  ("nof_tree_events",                 49535),
  ("nof_db_events",                   49535),
  ("fsize_local",                     228813373), # 228.81MB, avg file size 228.81MB
  ("fsize_db",                        2291615192), # 2.29GB, avg file size 763.87MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 5.00024375e+04, 4.99954727e+04, 5.00018281e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.36443320e+04, 5.00008086e+04, 4.66948672e+04, 5.36443320e+04, 5.00008086e+04, 4.66948672e+04, 5.36443320e+04, 5.00008086e+04, 4.66948672e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.36443320e+04, 4.66948672e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.90083320e+04, 4.90027188e+04, 4.90090781e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.90083320e+04, 4.87628711e+04, 4.92545898e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.25702305e+04, 4.90071094e+04, 4.57746328e+04, 5.25702305e+04, 4.90071094e+04, 4.57746328e+04, 5.25702305e+04, 4.90071094e+04, 4.57746328e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.25702305e+04, 4.57746328e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     237944185), # 237.94MB, avg file size 237.94MB
  ("fsize_db",                        2274028392), # 2.27GB, avg file size 2.27GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 49175, ],
    'CountWeighted'                                                                  : [ 4.91740547e+04, 4.91768164e+04, 4.91759492e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.30438828e+04, 4.91729219e+04, 4.57085586e+04, 5.30438828e+04, 4.91729219e+04, 4.57085586e+04, 5.30438828e+04, 4.91729219e+04, 4.57085586e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.30438828e+04, 4.57085586e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.82097344e+04, 4.82092852e+04, 4.82124414e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.82097344e+04, 4.79714141e+04, 4.84479258e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.19956602e+04, 4.82087930e+04, 4.48177305e+04, 5.19956602e+04, 4.82087930e+04, 4.48177305e+04, 5.19956602e+04, 4.82087930e+04, 4.48177305e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.19956602e+04, 4.48177305e+04, ],
  }),
  ("nof_tree_events",                 49175),
  ("nof_db_events",                   49175),
  ("fsize_local",                     240281544), # 240.28MB, avg file size 240.28MB
  ("fsize_db",                        2305398213), # 2.31GB, avg file size 2.31GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 5.00021445e+04, 4.99929492e+04, 4.99989922e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.42103750e+04, 5.00011758e+04, 4.62737070e+04, 5.42103750e+04, 5.00011758e+04, 4.62737070e+04, 5.42103750e+04, 5.00011758e+04, 4.62737070e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.42103750e+04, 4.62737070e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.90223750e+04, 4.90146602e+04, 4.90222969e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.90223750e+04, 4.87809453e+04, 4.92634102e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.31413359e+04, 4.90214531e+04, 4.53729180e+04, 5.31413359e+04, 4.90214531e+04, 4.53729180e+04, 5.31413359e+04, 4.90214531e+04, 4.53729180e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.31413359e+04, 4.53729180e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     249737670), # 249.74MB, avg file size 249.74MB
  ("fsize_db",                        2270214311), # 2.27GB, avg file size 2.27GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 49080, ],
    'CountWeighted'                                                                  : [ 4.90772461e+04, 4.90815820e+04, 4.90817148e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.34517812e+04, 4.90771289e+04, 4.52431641e+04, 5.34517812e+04, 4.90771289e+04, 4.52431641e+04, 5.34517812e+04, 4.90771289e+04, 4.52431641e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.34517812e+04, 4.52431641e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.81073633e+04, 4.81080273e+04, 4.81121719e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.81073633e+04, 4.78696133e+04, 4.83450625e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.23879141e+04, 4.81070156e+04, 4.43528945e+04, 5.23879141e+04, 4.81070156e+04, 4.43528945e+04, 5.23879141e+04, 4.81070156e+04, 4.43528945e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.23879141e+04, 4.43528945e+04, ],
  }),
  ("nof_tree_events",                 49080),
  ("nof_db_events",                   49080),
  ("fsize_local",                     250154267), # 250.15MB, avg file size 250.15MB
  ("fsize_db",                        2393147016), # 2.39GB, avg file size 2.39GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 50000, ],
    'CountWeighted'                                                                  : [ 5.00045508e+04, 4.99971172e+04, 5.00013750e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.46792305e+04, 5.00044727e+04, 4.59271016e+04, 5.46792305e+04, 5.00044727e+04, 4.59271016e+04, 5.46792305e+04, 5.00044727e+04, 4.59271016e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.46792305e+04, 4.59271016e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.90284414e+04, 4.90221602e+04, 4.90276289e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.90284414e+04, 4.87891484e+04, 4.92672109e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.36064570e+04, 4.90281484e+04, 4.50360625e+04, 5.36064570e+04, 4.90281484e+04, 4.50360625e+04, 5.36064570e+04, 4.90281484e+04, 4.50360625e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.36064570e+04, 4.50360625e+04, ],
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     259894988), # 259.89MB, avg file size 259.89MB
  ("fsize_db",                        2439402593), # 2.44GB, avg file size 2.44GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 49178, ],
    'CountWeighted'                                                                  : [ 4.91676914e+04, 4.91695898e+04, 4.91726836e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.39821523e+04, 4.91673008e+04, 4.50106875e+04, 5.39821523e+04, 4.91673008e+04, 4.50106875e+04, 5.39821523e+04, 4.91673008e+04, 4.50106875e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.39821523e+04, 4.50106875e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.82078047e+04, 4.82086016e+04, 4.82115312e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.82078047e+04, 4.79730508e+04, 4.84426172e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.29215977e+04, 4.82073828e+04, 4.41352109e+04, 5.29215977e+04, 4.82073828e+04, 4.41352109e+04, 5.29215977e+04, 4.82073828e+04, 4.41352109e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.29215977e+04, 4.41352109e+04, ],
  }),
  ("nof_tree_events",                 49178),
  ("nof_db_events",                   49178),
  ("fsize_local",                     259722934), # 259.72MB, avg file size 259.72MB
  ("fsize_db",                        2401512581), # 2.40GB, avg file size 2.40GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 49283, ],
    'CountWeighted'                                                                  : [ 4.92889180e+04, 4.92831016e+04, 4.92821367e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.44834180e+04, 4.92877148e+04, 4.48388320e+04, 5.44834180e+04, 4.92877148e+04, 4.48388320e+04, 5.44834180e+04, 4.92877148e+04, 4.48388320e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.44834180e+04, 4.48388320e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 4.83232773e+04, 4.83171406e+04, 4.83210977e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 4.83232773e+04, 4.80887812e+04, 4.85570586e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.34140195e+04, 4.83221914e+04, 4.39653398e+04, 5.34140195e+04, 4.83221914e+04, 4.39653398e+04, 5.34140195e+04, 4.83221914e+04, 4.39653398e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.34140195e+04, 4.39653398e+04, ],
  }),
  ("nof_tree_events",                 49283),
  ("nof_db_events",                   49283),
  ("fsize_local",                     265894017), # 265.89MB, avg file size 265.89MB
  ("fsize_db",                        2506744879), # 2.51GB, avg file size 2.51GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99916250e+04, 9.99930938e+04, 9.99960781e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.28102977e+05, 1.20944641e+05, 1.14228867e+05, 1.05931281e+05, 9.99911875e+04, 9.44376562e+04, 8.90565078e+04, 8.40632656e+04, 7.93810547e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.28102977e+05, 7.93810547e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.78769609e+04, 9.78753672e+04, 9.78817891e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.78769609e+04, 9.73462891e+04, 9.84066406e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.25368148e+05, 1.18384992e+05, 1.11827852e+05, 1.03668234e+05, 9.78761641e+04, 9.24516953e+04, 8.71523984e+04, 8.22813047e+04, 7.77112578e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.25368148e+05, 7.77112578e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     440764613), # 440.76MB, avg file size 440.76MB
  ("fsize_db",                        4335254200), # 4.34GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99984453e+04, 9.99988125e+04, 1.00021328e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27639461e+05, 1.21244227e+05, 1.15116211e+05, 1.05285844e+05, 9.99978047e+04, 9.49353750e+04, 8.83338828e+04, 8.38884453e+04, 7.96352578e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27639461e+05, 7.96352578e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.79698984e+04, 9.79633047e+04, 9.79888203e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.79698984e+04, 9.74566250e+04, 9.84802734e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.25023703e+05, 1.18784266e+05, 1.12798195e+05, 1.03128281e+05, 9.79689922e+04, 9.30225938e+04, 8.65227734e+04, 8.21853750e+04, 7.80302344e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.25023703e+05, 7.80302344e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     429868021), # 429.87MB, avg file size 429.87MB
  ("fsize_db",                        4343698408), # 4.34GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_box_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 95878, ],
    'CountWeighted'                                                                  : [ 9.58760312e+04, 9.58648438e+04, 9.58850312e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.25439117e+05, 1.14511781e+05, 1.05094531e+05, 1.05068227e+05, 9.58756875e+04, 8.79636250e+04, 8.92985703e+04, 8.14604375e+04, 7.47155547e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.25439117e+05, 7.47155547e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.36608594e+04, 9.36569688e+04, 9.36634297e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.36608594e+04, 9.31186562e+04, 9.42035234e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.22518844e+05, 1.11869656e+05, 1.02687586e+05, 1.02618711e+05, 9.36600625e+04, 8.59458594e+04, 8.72146328e+04, 7.95755156e+04, 7.30000391e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.22518844e+05, 7.30000391e+04, ],
  }),
  ("nof_tree_events",                 95878),
  ("nof_db_events",                   95878),
  ("fsize_local",                     483232693), # 483.23MB, avg file size 483.23MB
  ("fsize_db",                        4587536778), # 4.59GB, avg file size 2.29GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99000, ],
    'CountWeighted'                                                                  : [ 9.90121797e+04, 9.90159766e+04, 9.89906484e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27158867e+05, 1.19550844e+05, 1.12522172e+05, 1.05319688e+05, 9.90120469e+04, 9.31636250e+04, 8.86640625e+04, 8.33323672e+04, 7.84078516e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27158867e+05, 7.84078516e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.68606406e+04, 9.68582031e+04, 9.68520000e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.68606406e+04, 9.63221250e+04, 9.73964766e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.24376133e+05, 1.16960453e+05, 1.10103539e+05, 1.03012945e+05, 9.68599766e+04, 9.11597656e+04, 8.67217734e+04, 8.15228984e+04, 7.67195938e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.24376133e+05, 7.67195938e+04, ],
  }),
  ("nof_tree_events",                 99000),
  ("nof_db_events",                   99000),
  ("fsize_local",                     444715734), # 444.72MB, avg file size 444.72MB
  ("fsize_db",                        4402287226), # 4.40GB, avg file size 1.47GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 97777, ],
    'CountWeighted'                                                                  : [ 9.77622266e+04, 9.77759922e+04, 9.77704219e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.24975969e+05, 1.18448336e+05, 1.12251383e+05, 1.03183836e+05, 9.77621094e+04, 9.26491797e+04, 8.66363828e+04, 8.20858125e+04, 7.77703594e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.24975969e+05, 7.77703594e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.57650234e+04, 9.57724766e+04, 9.57722344e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.57650234e+04, 9.52607812e+04, 9.62685312e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.22392523e+05, 1.16024500e+05, 1.09974164e+05, 1.01047359e+05, 9.57645000e+04, 9.07679141e+04, 8.48411797e+04, 8.04029609e+04, 7.61905312e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.22392523e+05, 7.61905312e+04, ],
  }),
  ("nof_tree_events",                 97777),
  ("nof_db_events",                   97777),
  ("fsize_local",                     425118741), # 425.12MB, avg file size 425.12MB
  ("fsize_db",                        4296631601), # 4.30GB, avg file size 2.15GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 98210, ],
    'CountWeighted'                                                                  : [ 9.82007656e+04, 9.82072188e+04, 9.82124766e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27342656e+05, 1.17934828e+05, 1.09591367e+05, 1.06082383e+05, 9.82005312e+04, 9.12358828e+04, 8.97459844e+04, 8.30619375e+04, 7.71449375e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27342656e+05, 7.71449375e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.59907578e+04, 9.59901719e+04, 9.60041953e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.59907578e+04, 9.54422031e+04, 9.65391094e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.24448648e+05, 1.15281883e+05, 1.07146719e+05, 1.03668398e+05, 9.59900000e+04, 8.91979297e+04, 8.77023906e+04, 8.11883672e+04, 7.54195625e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.24448648e+05, 7.54195625e+04, ],
  }),
  ("nof_tree_events",                 98210),
  ("nof_db_events",                   98210),
  ("fsize_local",                     468688223), # 468.69MB, avg file size 468.69MB
  ("fsize_db",                        4483694248), # 4.48GB, avg file size 2.24GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99178, ],
    'CountWeighted'                                                                  : [ 9.91787266e+04, 9.91885391e+04, 9.92018125e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.26566555e+05, 1.20296164e+05, 1.14307461e+05, 1.04380289e+05, 9.91785391e+04, 9.42137188e+04, 8.75657188e+04, 8.31798438e+04, 7.89988750e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.26566555e+05, 7.89988750e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.72118516e+04, 9.72128203e+04, 9.72313594e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.72118516e+04, 9.67156250e+04, 9.77092344e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.24031320e+05, 1.17916141e+05, 1.12068633e+05, 1.02285148e+05, 9.72110938e+04, 9.23659453e+04, 8.58052344e+04, 8.15288203e+04, 7.74475469e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.24031320e+05, 7.74475469e+04, ],
  }),
  ("nof_tree_events",                 99178),
  ("nof_db_events",                   99178),
  ("fsize_local",                     428058854), # 428.06MB, avg file size 428.06MB
  ("fsize_db",                        4255863331), # 4.26GB, avg file size 2.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 97801, ],
    'CountWeighted'                                                                  : [ 9.77855938e+04, 9.78010938e+04, 9.78120469e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.23604383e+05, 1.19364234e+05, 1.14932227e+05, 1.01287305e+05, 9.77852422e+04, 9.41616484e+04, 8.45132578e+04, 8.15953281e+04, 7.85533359e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.23604383e+05, 7.85533359e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.60400391e+04, 9.60470000e+04, 9.60600703e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.60400391e+04, 9.55872031e+04, 9.64903672e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.21369914e+05, 1.17227711e+05, 1.12893211e+05, 9.94540547e+04, 9.60391797e+04, 9.24887422e+04, 8.29826719e+04, 8.01342812e+04, 7.71576562e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.21369914e+05, 7.71576562e+04, ],
  }),
  ("nof_tree_events",                 97801),
  ("nof_db_events",                   97801),
  ("fsize_local",                     391148357), # 391.15MB, avg file size 391.15MB
  ("fsize_db",                        3951072091), # 3.95GB, avg file size 1.98GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99301, ],
    'CountWeighted'                                                                  : [ 9.93059766e+04, 9.92896094e+04, 9.92818125e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27634586e+05, 1.19886750e+05, 1.12766477e+05, 1.05751797e+05, 9.93056172e+04, 9.33780625e+04, 8.90617578e+04, 8.36064922e+04, 7.86033359e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27634586e+05, 7.86033359e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71913438e+04, 9.71802109e+04, 9.71800625e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71913438e+04, 9.66638516e+04, 9.77185234e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.24895883e+05, 1.17341367e+05, 1.10394039e+05, 1.03478898e+05, 9.71906562e+04, 9.14106016e+04, 8.71450781e+04, 8.18265625e+04, 7.69448359e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.24895883e+05, 7.69448359e+04, ],
  }),
  ("nof_tree_events",                 99301),
  ("nof_db_events",                   99301),
  ("fsize_local",                     448717747), # 448.72MB, avg file size 448.72MB
  ("fsize_db",                        4354193987), # 4.35GB, avg file size 1.45GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 98588, ],
    'CountWeighted'                                                                  : [ 9.86246719e+04, 9.85919219e+04, 9.85850938e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27434664e+05, 1.18590125e+05, 1.10647914e+05, 1.05967523e+05, 9.86126172e+04, 9.19639141e+04, 8.95112188e+04, 8.32585469e+04, 7.76513203e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27434664e+05, 7.76513203e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.64108984e+04, 9.63858750e+04, 9.63922891e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.64108984e+04, 9.58652656e+04, 9.69570312e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.24568891e+05, 1.15947875e+05, 1.08201953e+05, 1.03581391e+05, 9.64031953e+04, 8.99293750e+04, 8.74943359e+04, 8.13997969e+04, 7.59318594e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.24568891e+05, 7.59318594e+04, ],
  }),
  ("nof_tree_events",                 98588),
  ("nof_db_events",                   98588),
  ("fsize_local",                     462657938), # 462.66MB, avg file size 462.66MB
  ("fsize_db",                        4491891214), # 4.49GB, avg file size 2.25GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 98724, ],
    'CountWeighted'                                                                  : [ 9.87262969e+04, 9.87180547e+04, 9.87379062e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.25017203e+05, 1.20347859e+05, 1.15596258e+05, 1.02575242e+05, 9.87227969e+04, 9.48026641e+04, 8.56843125e+04, 8.24471641e+04, 7.91609688e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.25017203e+05, 7.91609688e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.69217578e+04, 9.69163750e+04, 9.69293203e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.69217578e+04, 9.64585781e+04, 9.73833516e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.22711648e+05, 1.18154227e+05, 1.13507633e+05, 1.00681297e+05, 9.69191328e+04, 9.30876094e+04, 8.40993672e+04, 8.09395938e+04, 7.77272812e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.22711648e+05, 7.77272812e+04, ],
  }),
  ("nof_tree_events",                 98724),
  ("nof_db_events",                   98724),
  ("fsize_local",                     401802191), # 401.80MB, avg file size 401.80MB
  ("fsize_db",                        4130096263), # 4.13GB, avg file size 2.07GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99807500e+04, 9.99728750e+04, 9.99901641e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27627969e+05, 1.21294133e+05, 1.15254547e+05, 1.05259359e+05, 9.99804688e+04, 9.49906016e+04, 8.83081484e+04, 8.38703125e+04, 7.96487656e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27627969e+05, 7.96487656e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.80136719e+04, 9.80111328e+04, 9.80162812e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.80136719e+04, 9.75129922e+04, 9.85127578e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.25081625e+05, 1.18903398e+05, 1.13003695e+05, 1.03155109e+05, 9.80129688e+04, 9.31328438e+04, 8.65394453e+04, 8.22110312e+04, 7.80886953e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.25081625e+05, 7.80886953e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     430758092), # 430.76MB, avg file size 430.76MB
  ("fsize_db",                        4262962926), # 4.26GB, avg file size 2.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
    'Count'                                                                          : [ 99190, ],
    'CountWeighted'                                                                  : [ 9.91963828e+04, 9.91832812e+04, 9.91874766e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.25927312e+05, 1.20694922e+05, 1.15472391e+05, 1.03505578e+05, 9.91962266e+04, 9.48897734e+04, 8.65805859e+04, 8.29622812e+04, 7.93592734e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.25927312e+05, 7.93592734e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.73081797e+04, 9.72978125e+04, 9.73094922e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.73081797e+04, 9.68276328e+04, 9.77886641e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23514070e+05, 1.18404523e+05, 1.13299188e+05, 1.01519898e+05, 9.73075625e+04, 9.31019688e+04, 8.49192031e+04, 8.13861406e+04, 7.78629375e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23514070e+05, 7.78629375e+04, ],
  }),
  ("nof_tree_events",                 99190),
  ("nof_db_events",                   99190),
  ("fsize_local",                     410008628), # 410.01MB, avg file size 410.01MB
  ("fsize_db",                        4123293762), # 4.12GB, avg file size 2.06GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2016/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

