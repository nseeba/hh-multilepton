from collections import OrderedDict as OD

# file generated at 2020-08-24 20:04:27 with the following command:
# create_dictionary.py -m python/samples/metaDict_2018_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples -N samples_2018 -E 2018 -o python/samples -g hhAnalyzeSamples_2018_hh.py -M

samples_2018 = OD()
samples_2018["/GluGluToRadionToHHTo4T_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99932141e+05, 3.99955969e+05, 3.99940297e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99932141e+05, 3.99932141e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.00013300e+06, 4.00013300e+06, 4.00013300e+06, 4.00013300e+06, 4.00013300e+06, 4.00013300e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99989156e+05, 4.00034125e+05, 5.48550156e+05, 3.99941062e+05, 3.99359656e+05, 2.67055266e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1395138204), # 1.40GB, avg file size 697.57MB
  ("fsize_db",                        21421829719), # 21.42GB, avg file size 1.65GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99962078e+05, 3.99953797e+05, 3.99886969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06182047e+05, 3.99957688e+05, 3.91129781e+05, 4.06182047e+05, 3.99957688e+05, 3.91129781e+05, 4.06182047e+05, 3.99957688e+05, 3.91129781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06182047e+05, 3.91129750e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99451844e+06, 1.99121856e+06, 2.63624662e+06, 1.99440050e+06, 1.89409562e+06, 1.33031719e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99976812e+05, 4.00051719e+05, 5.48900891e+05, 3.99960266e+05, 3.99330469e+05, 2.66779500e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1402407463), # 1.40GB, avg file size 701.20MB
  ("fsize_db",                        20670227545), # 20.67GB, avg file size 2.07GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99982219e+05, 3.99953875e+05, 3.99955516e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07483938e+05, 3.99976906e+05, 3.90118422e+05, 4.07483938e+05, 3.99976906e+05, 3.90118422e+05, 4.07483938e+05, 3.99976906e+05, 3.90118422e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07483938e+05, 3.90118422e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.48542294e+06, 1.48569344e+06, 2.00547838e+06, 1.48527456e+06, 1.44821081e+06, 9.88931906e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99981500e+05, 4.00143109e+05, 5.49373281e+05, 3.99954125e+05, 3.99231203e+05, 2.66296000e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1417832742), # 1.42GB, avg file size 708.92MB
  ("fsize_db",                        20783178743), # 20.78GB, avg file size 1.48GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 385000, ],
    'CountWeighted'                                                                  : [ 3.85005469e+05, 3.84971047e+05, 3.85005938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.85005469e+05, 3.85005469e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.22592797e+06, 1.22616525e+06, 1.66748325e+06, 1.22499169e+06, 1.20554550e+06, 8.14096219e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.85137344e+05, 3.85244484e+05, 5.30098547e+05, 3.84838641e+05, 3.84945609e+05, 2.55758625e+05, ],
  }),
  ("nof_tree_events",                 385000),
  ("nof_db_events",                   385000),
  ("fsize_local",                     1391850362), # 1.39GB, avg file size 695.93MB
  ("fsize_db",                        20779525724), # 20.78GB, avg file size 989.50MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_4t"),
  ("nof_files",                       3),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 294000, ],
    'CountWeighted'                                                                  : [ 2.93985035e+05, 2.93984283e+05, 2.93984400e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.02101472e+05, 2.93982359e+05, 2.84719862e+05, 3.02101472e+05, 2.93982359e+05, 2.84719862e+05, 3.02101472e+05, 2.93982359e+05, 2.84719862e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.02101472e+05, 2.84719862e+05, ],
    'CountWeightedPSWeight'                                                          : [ 7.92811289e+05, 7.93143752e+05, 1.08389322e+06, 7.93432559e+05, 7.84403213e+05, 5.26242336e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.93889152e+05, 2.94022961e+05, 4.04729285e+05, 2.94122253e+05, 2.93701461e+05, 1.95075958e+05, ],
  }),
  ("nof_tree_events",                 294000),
  ("nof_db_events",                   294000),
  ("fsize_local",                     1081364390), # 1.08GB, avg file size 360.45MB
  ("fsize_db",                        15512052325), # 15.51GB, avg file size 912.47MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 297000, ],
    'CountWeighted'                                                                  : [ 2.96976000e+05, 2.96992312e+05, 2.96982500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.06716438e+05, 2.96974594e+05, 2.86390172e+05, 3.06716438e+05, 2.96974594e+05, 2.86390172e+05, 3.06716438e+05, 2.96974594e+05, 2.86390172e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.06716438e+05, 2.86390172e+05, ],
    'CountWeightedPSWeight'                                                          : [ 7.32640406e+05, 7.32973156e+05, 1.00433962e+06, 7.32352062e+05, 7.25657625e+05, 4.84516766e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.97037938e+05, 2.97173656e+05, 4.09645969e+05, 2.96921828e+05, 2.96658406e+05, 1.96441008e+05, ],
  }),
  ("nof_tree_events",                 297000),
  ("nof_db_events",                   297000),
  ("fsize_local",                     1114414692), # 1.11GB, avg file size 557.21MB
  ("fsize_db",                        15790119701), # 15.79GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 297000, ],
    'CountWeighted'                                                                  : [ 2.96976816e+05, 2.96934723e+05, 2.96934316e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08838367e+05, 2.96970602e+05, 2.84720996e+05, 3.08838367e+05, 2.96970602e+05, 2.84720996e+05, 3.08838367e+05, 2.96970602e+05, 2.84720996e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08838367e+05, 2.84720996e+05, ],
    'CountWeightedPSWeight'                                                          : [ 6.79874461e+05, 6.79742805e+05, 9.35233188e+05, 6.80088656e+05, 6.75801422e+05, 4.48680445e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.96965602e+05, 2.96911586e+05, 4.10563484e+05, 2.97058246e+05, 2.97245148e+05, 1.95983164e+05, ],
  }),
  ("nof_tree_events",                 297000),
  ("nof_db_events",                   297000),
  ("fsize_local",                     1146796204), # 1.15GB, avg file size 573.40MB
  ("fsize_db",                        15967583373), # 15.97GB, avg file size 1.77GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99957543e+05, 2.99999375e+05, 2.99997676e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15125648e+05, 2.99957543e+05, 2.85268816e+05, 3.15125648e+05, 2.99957543e+05, 2.85268816e+05, 3.15125648e+05, 2.99957543e+05, 2.85268816e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15125648e+05, 2.85268816e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.65119188e+05, 8.64765469e+05, 1.18616491e+06, 8.65530484e+05, 8.53811719e+05, 5.68777625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99924328e+05, 2.99806641e+05, 4.15156586e+05, 3.00068414e+05, 2.99932008e+05, 1.97189449e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1207895856), # 1.21GB, avg file size 603.95MB
  ("fsize_db",                        15976195307), # 15.98GB, avg file size 887.57MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99949414e+05, 2.99959621e+05, 2.99983113e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17773633e+05, 2.99949414e+05, 2.83223914e+05, 3.17773633e+05, 2.99949414e+05, 2.83223914e+05, 3.17773633e+05, 2.99949414e+05, 2.83223914e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17773695e+05, 2.83223820e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.23579734e+05, 4.23637273e+05, 5.87534156e+05, 4.23884578e+05, 4.23283398e+05, 2.77246785e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99870758e+05, 2.99915203e+05, 4.16363695e+05, 3.00087848e+05, 3.00081160e+05, 1.96275445e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1255412691), # 1.26GB, avg file size 627.71MB
  ("fsize_db",                        17563676363), # 17.56GB, avg file size 2.93GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99931215e+05, 2.99912590e+05, 2.99885605e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20026773e+05, 2.99929859e+05, 2.81412234e+05, 3.20026773e+05, 2.99929859e+05, 2.81412234e+05, 3.20026773e+05, 2.99929859e+05, 2.81412234e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20026773e+05, 2.81412234e+05, ],
    'CountWeightedPSWeight'                                                          : [ 6.33581875e+05, 6.34380570e+05, 8.76463922e+05, 6.33930570e+05, 6.28092500e+05, 4.13081523e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99867848e+05, 3.00251695e+05, 4.16440016e+05, 3.00038688e+05, 2.98882336e+05, 1.95508246e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1295225942), # 1.30GB, avg file size 647.61MB
  ("fsize_db",                        16876391387), # 16.88GB, avg file size 3.38GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99977922e+05, 2.99983426e+05, 2.99991793e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22115086e+05, 2.99974316e+05, 2.79888039e+05, 3.22115086e+05, 2.99974316e+05, 2.79888039e+05, 3.22115086e+05, 2.99974316e+05, 2.79888039e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22115336e+05, 2.79887789e+05, ],
    'CountWeightedPSWeight'                                                          : [ 6.38660227e+05, 6.38670305e+05, 8.84896938e+05, 6.38648688e+05, 6.33957977e+05, 4.15189391e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99999016e+05, 3.00006898e+05, 4.17456000e+05, 2.99996871e+05, 2.99580309e+05, 1.95031033e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1330828200), # 1.33GB, avg file size 665.41MB
  ("fsize_db",                        17078741577), # 17.08GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 196000, ],
    'CountWeighted'                                                                  : [ 1.95957062e+05, 1.95963781e+05, 1.95938281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.11594328e+05, 1.95957062e+05, 1.81921312e+05, 2.11594328e+05, 1.95957062e+05, 1.81921312e+05, 2.11594328e+05, 1.95957062e+05, 1.81921312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.11594344e+05, 1.81921281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 5.64580000e+05, 5.65018812e+05, 7.79135750e+05, 5.64801875e+05, 5.55717625e+05, 3.65904438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.95921938e+05, 1.96079859e+05, 2.73058062e+05, 1.95997875e+05, 1.95522719e+05, 1.26978016e+05, ],
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     889934647), # 889.93MB, avg file size 889.93MB
  ("fsize_db",                        10929556578), # 10.93GB, avg file size 2.73GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99975469e+05, 1.99992703e+05, 1.99962156e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17052641e+05, 1.99975469e+05, 1.84828469e+05, 2.17052641e+05, 1.99975469e+05, 1.84828469e+05, 2.17052641e+05, 1.99975469e+05, 1.84828469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17052953e+05, 1.84828156e+05, ],
    'CountWeightedPSWeight'                                                          : [ 5.88217062e+05, 5.88409250e+05, 8.13476688e+05, 5.88536250e+05, 5.79568500e+05, 3.80040219e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99929656e+05, 2.00003109e+05, 2.79745312e+05, 2.00037266e+05, 2.00233625e+05, 1.29172062e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     928596417), # 928.60MB, avg file size 928.60MB
  ("fsize_db",                        11285007994), # 11.29GB, avg file size 940.42MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99952047e+05, 1.99930766e+05, 1.99963844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18030719e+05, 1.99951734e+05, 1.84042156e+05, 2.18030719e+05, 1.99951734e+05, 1.84042156e+05, 2.18030719e+05, 1.99951734e+05, 1.84042156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18030719e+05, 1.84042156e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.50883094e+05, 4.50670438e+05, 6.26308125e+05, 4.51029719e+05, 4.46758219e+05, 2.90875094e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99949156e+05, 1.99845453e+05, 2.79239406e+05, 2.00010422e+05, 1.99628234e+05, 1.28994227e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     949857620), # 949.86MB, avg file size 949.86MB
  ("fsize_db",                        11712322920), # 11.71GB, avg file size 2.34GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99964578e+05, 1.99957531e+05, 1.99962000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99964578e+05, 1.99964578e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.64238188e+05, 4.64072812e+05, 6.46144250e+05, 4.64221500e+05, 4.59936562e+05, 2.98490750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00006000e+05, 1.99934125e+05, 2.80026188e+05, 1.99992562e+05, 1.99802781e+05, 1.28596219e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     974769058), # 974.77MB, avg file size 974.77MB
  ("fsize_db",                        12140113240), # 12.14GB, avg file size 2.02GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 196000, ],
    'CountWeighted'                                                                  : [ 1.95940375e+05, 1.95942500e+05, 1.95932469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.95940375e+05, 1.95940375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 6.28360125e+05, 6.28373250e+05, 8.68662000e+05, 6.28359250e+05, 6.15721125e+05, 4.03147188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.95956203e+05, 1.95980984e+05, 2.74937938e+05, 1.95961328e+05, 1.96037656e+05, 1.25723828e+05, ],
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     969664077), # 969.66MB, avg file size 969.66MB
  ("fsize_db",                        11652048519), # 11.65GB, avg file size 2.33GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99940109e+05, 1.99971953e+05, 1.99937062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99940109e+05, 1.99940109e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.96039281e+05, 4.96394250e+05, 6.91085438e+05, 4.96423750e+05, 4.90059438e+05, 3.17366719e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99924500e+05, 2.00077953e+05, 2.80570344e+05, 2.00081781e+05, 1.99543625e+05, 1.27915031e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1003681358), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        12308761975), # 12.31GB, avg file size 2.46GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 190000, ],
    'CountWeighted'                                                                  : [ 1.89951812e+05, 1.89943812e+05, 1.89950719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.10240703e+05, 1.89951812e+05, 1.72537641e+05, 2.10240703e+05, 1.89951812e+05, 1.72537641e+05, 2.10240703e+05, 1.89951812e+05, 1.72537641e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.10242422e+05, 1.72535922e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.27215031e+05, 3.26766094e+05, 4.58272625e+05, 3.27133000e+05, 3.26309344e+05, 2.09361562e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.89996297e+05, 1.89741266e+05, 2.66734000e+05, 1.89949156e+05, 1.90105406e+05, 1.21566031e+05, ],
  }),
  ("nof_tree_events",                 190000),
  ("nof_db_events",                   190000),
  ("fsize_local",                     959314334), # 959.31MB, avg file size 959.31MB
  ("fsize_db",                        12135155388), # 12.14GB, avg file size 713.83MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99443906e+04, 9.99442188e+04, 9.99401250e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11296125e+05, 9.99443906e+04, 9.02919844e+04, 1.11296125e+05, 9.99443906e+04, 9.02919844e+04, 1.11296125e+05, 9.99443906e+04, 9.02919844e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11296125e+05, 9.02919844e+04, ],
    'CountWeightedPSWeight'                                                          : [ 1.86731547e+05, 1.86635109e+05, 2.61475562e+05, 1.86368188e+05, 1.85281234e+05, 1.18840875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00046578e+05, 9.99895938e+04, 1.40556156e+05, 9.98500781e+04, 9.97397188e+04, 6.36741797e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     517793650), # 517.79MB, avg file size 517.79MB
  ("fsize_db",                        6443692606), # 6.44GB, avg file size 2.15GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99358125e+04, 9.99474844e+04, 9.99359531e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99358125e+04, 9.99358125e+04, ],
    'CountWeightedPSWeight'                                                          : [ 2.33985797e+05, 2.34091922e+05, 3.28741625e+05, 2.34113781e+05, 2.31699328e+05, 1.47751281e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99529766e+04, 1.00002023e+05, 1.41503469e+05, 1.00008250e+05, 1.00049078e+05, 6.31185273e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     538351533), # 538.35MB, avg file size 538.35MB
  ("fsize_db",                        6712151176), # 6.71GB, avg file size 1.34GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_1250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99574375e+04, 9.99611250e+04, 9.99555781e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13896234e+05, 9.99569531e+04, 8.85251562e+04, 1.13896234e+05, 9.99569531e+04, 8.85251562e+04, 1.13896234e+05, 9.99569531e+04, 8.85251562e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13896234e+05, 8.85251562e+04, ],
    'CountWeightedPSWeight'                                                          : [ 4.49612375e+05, 4.48465344e+05, 6.11748562e+05, 4.49287562e+05, 4.25332000e+05, 2.83011188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00032445e+05, 9.99379531e+04, 1.41362734e+05, 9.99640234e+04, 9.97303828e+04, 6.29752734e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     533406339), # 533.41MB, avg file size 533.41MB
  ("fsize_db",                        6302147130), # 6.30GB, avg file size 630.21MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_1500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99186172e+04, 9.99264531e+04, 9.99196406e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99186172e+04, 9.99186172e+04, ],
    'CountWeightedPSWeight'                                                          : [ 3.95598219e+05, 3.94742188e+05, 5.46358000e+05, 3.95837938e+05, 3.81024062e+05, 2.47840531e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99645859e+04, 9.98205000e+04, 1.42255234e+05, 1.00021281e+05, 1.00407156e+05, 6.26279844e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     533901529), # 533.90MB, avg file size 533.90MB
  ("fsize_db",                        6821889709), # 6.82GB, avg file size 2.27GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_1750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 96000, ],
    'CountWeighted'                                                                  : [ 9.59204531e+04, 9.59172969e+04, 9.59237031e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11056359e+05, 9.59204531e+04, 8.37076094e+04, 1.11056359e+05, 9.59204531e+04, 8.37076094e+04, 1.11056359e+05, 9.59204531e+04, 8.37076094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11058375e+05, 8.37055938e+04, ],
    'CountWeightedPSWeight'                                                          : [ 5.05105688e+05, 5.03173875e+05, 6.77201250e+05, 5.05609500e+05, 4.65228156e+05, 3.15446250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.59528984e+04, 9.61193438e+04, 1.36347109e+05, 9.60562812e+04, 9.55497812e+04, 5.99301406e+04, ],
  }),
  ("nof_tree_events",                 96000),
  ("nof_db_events",                   96000),
  ("fsize_local",                     508500760), # 508.50MB, avg file size 508.50MB
  ("fsize_db",                        6494733234), # 6.49GB, avg file size 541.23MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_2000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98434219e+04, 9.98563516e+04, 9.98378438e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98434219e+04, 9.98434219e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.24221250e+05, 8.44690500e+05, 9.97067125e+05, 9.12087250e+05, 7.41660375e+05, 5.99463250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99881719e+04, 9.99917500e+04, 1.42251234e+05, 1.00001844e+05, 9.97735781e+04, 6.23104609e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     531322138), # 531.32MB, avg file size 531.32MB
  ("fsize_db",                        6926930812), # 6.93GB, avg file size 2.31GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_2500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo4T_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.97761875e+04, 9.97800312e+04, 9.97514219e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.97761875e+04, 9.97761875e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.97620125e+05, 9.83320625e+05, 9.97650500e+05, 9.97612875e+05, 9.31457000e+05, 9.17093500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99946250e+04, 1.00025242e+05, 1.42459578e+05, 9.99721406e+04, 9.97526562e+04, 6.20674531e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     531650889), # 531.65MB, avg file size 531.65MB
  ("fsize_db",                        6993185515), # 6.99GB, avg file size 2.33GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_3000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_250_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_250_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99932094e+05, 3.99939219e+05, 3.99926734e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99932094e+05, 3.99932094e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99967800e+06, 3.99967800e+06, 3.99967800e+06, 3.99967800e+06, 3.99967800e+06, 3.99967800e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00173516e+05, 3.99974328e+05, 5.93240406e+05, 3.99768656e+05, 3.99874672e+05, 2.29307312e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2076901668), # 2.08GB, avg file size 1.04GB
  ("fsize_db",                        25688213729), # 25.69GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_260_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_260_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    27),
  ("nof_events",                      {
    'Count'                                                                          : [ 392000, ],
    'CountWeighted'                                                                  : [ 3.91895531e+05, 3.91916375e+05, 3.91944031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.91895531e+05, 3.91895531e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.91895975e+06, 3.91895975e+06, 3.91895975e+06, 3.91895975e+06, 3.91895975e+06, 3.91895975e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.92122438e+05, 3.92239203e+05, 5.80867781e+05, 3.91760891e+05, 3.90501109e+05, 2.24233531e+05, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     2060003400), # 2.06GB, avg file size 1.03GB
  ("fsize_db",                        26459235708), # 26.46GB, avg file size 979.97MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_260_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_270_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_270_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 360000, ],
    'CountWeighted'                                                                  : [ 3.59952703e+05, 3.60002617e+05, 3.59921484e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.59952703e+05, 3.59952703e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.59945338e+06, 3.59945338e+06, 3.59945338e+06, 3.59945338e+06, 3.59945338e+06, 3.59945338e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.59920516e+05, 3.60140734e+05, 5.34010797e+05, 3.60060297e+05, 3.58388000e+05, 2.05237605e+05, ],
  }),
  ("nof_tree_events",                 360000),
  ("nof_db_events",                   360000),
  ("fsize_local",                     1916053514), # 1.92GB, avg file size 958.03MB
  ("fsize_db",                        22838217629), # 22.84GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_270_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_280_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_280_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 392000, ],
    'CountWeighted'                                                                  : [ 3.91939109e+05, 3.91948781e+05, 3.91962453e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.91939109e+05, 3.91939109e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.91951325e+06, 3.91951325e+06, 3.91951325e+06, 3.91951325e+06, 3.91951325e+06, 3.91951325e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.91993797e+05, 3.91183484e+05, 5.81890688e+05, 3.91981422e+05, 3.91687312e+05, 2.23566656e+05, ],
  }),
  ("nof_tree_events",                 392000),
  ("nof_db_events",                   392000),
  ("fsize_local",                     2109046228), # 2.11GB, avg file size 1.05GB
  ("fsize_db",                        24989693699), # 24.99GB, avg file size 1.92GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_280_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_300_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_300_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99962617e+05, 2.99952086e+05, 2.99961488e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99962617e+05, 2.99962617e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99972909e+06, 2.99972909e+06, 2.99972909e+06, 2.99972909e+06, 2.99972909e+06, 2.99972909e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99887434e+05, 2.99906754e+05, 4.46490453e+05, 3.00121711e+05, 2.99196137e+05, 1.70042826e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1647396656), # 1.65GB, avg file size 823.70MB
  ("fsize_db",                        19311475451), # 19.31GB, avg file size 3.22GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_300_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_320_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_320_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99961648e+05, 2.99910488e+05, 2.99922656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.90002223e+05, 3.58815016e+05, 3.31328770e+05, 3.26063156e+05, 2.99956211e+05, 2.76921059e+05, 2.76844062e+05, 2.54626742e+05, 2.35058082e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.90002223e+05, 2.35058082e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99939884e+06, 2.99939884e+06, 2.99939884e+06, 2.99939884e+06, 2.99939884e+06, 2.99939884e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99910379e+05, 2.99915297e+05, 4.47152484e+05, 3.00102012e+05, 2.98915215e+05, 1.69315967e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1656917359), # 1.66GB, avg file size 828.46MB
  ("fsize_db",                        19594757568), # 19.59GB, avg file size 783.79MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_320_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_350_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_350_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    31),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99917434e+05, 2.99928008e+05, 2.99905617e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99917434e+05, 2.99917434e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99886125e+06, 2.99886125e+06, 2.99886125e+06, 2.99886125e+06, 2.99886125e+06, 2.99886125e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99977707e+05, 3.00048781e+05, 4.48692328e+05, 3.00041953e+05, 2.99079277e+05, 1.68205668e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1722971410), # 1.72GB, avg file size 861.49MB
  ("fsize_db",                        21184916301), # 21.18GB, avg file size 683.38MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_350_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_400_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_400_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99912266e+05, 2.99914941e+05, 2.99876191e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99912266e+05, 2.99912266e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99896953e+06, 2.99897128e+06, 2.99897128e+06, 2.99896953e+06, 2.99897128e+06, 2.99896953e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00054953e+05, 2.99924355e+05, 4.50825547e+05, 2.99880410e+05, 2.99576297e+05, 1.66661805e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1785621116), # 1.79GB, avg file size 892.81MB
  ("fsize_db",                        21535525625), # 21.54GB, avg file size 2.39GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_400_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_450_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_450_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99925148e+05, 2.99921973e+05, 2.99893770e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99925148e+05, 2.99925148e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99934947e+06, 2.99934947e+06, 2.99934947e+06, 2.99934947e+06, 2.99934947e+06, 2.99934947e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99787457e+05, 2.99884598e+05, 4.51271617e+05, 3.00195309e+05, 2.98836191e+05, 1.65684492e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1840205127), # 1.84GB, avg file size 920.10MB
  ("fsize_db",                        21898598924), # 21.90GB, avg file size 2.43GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_450_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_500_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_500_hh_4t"),
  ("nof_files",                       3),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 296000, ],
    'CountWeighted'                                                                  : [ 2.95910227e+05, 2.95908680e+05, 2.95912730e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.95910227e+05, 2.95910227e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.95918038e+06, 2.95919462e+06, 2.95919462e+06, 2.95918050e+06, 2.95919462e+06, 2.95918038e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.95958539e+05, 2.95684371e+05, 4.47323992e+05, 2.95996844e+05, 2.95692215e+05, 1.62259262e+05, ],
  }),
  ("nof_tree_events",                 296000),
  ("nof_db_events",                   296000),
  ("fsize_local",                     1861137513), # 1.86GB, avg file size 620.38MB
  ("fsize_db",                        20445801040), # 20.45GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_550_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_550_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    27),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99932520e+05, 2.99890141e+05, 2.99902215e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99932520e+05, 2.99932520e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99891869e+06, 2.99891869e+06, 2.99891869e+06, 2.99891869e+06, 2.99891869e+06, 2.99891869e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99882148e+05, 3.00701707e+05, 4.53778594e+05, 3.00123410e+05, 2.97696625e+05, 1.63262295e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1928862447), # 1.93GB, avg file size 964.43MB
  ("fsize_db",                        21548412071), # 21.55GB, avg file size 798.09MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_550_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_600_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_600_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 2.00097875e+05, 2.00077281e+05, 2.00136406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.00097875e+05, 2.00097875e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.00136938e+06, 2.00136938e+06, 2.00136938e+06, 2.00136938e+06, 2.00136938e+06, 2.00136938e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00182594e+05, 2.00021906e+05, 3.03256656e+05, 2.00125016e+05, 1.99158297e+05, 1.08521656e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1310955777), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        15178299980), # 15.18GB, avg file size 2.53GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_600_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_650_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_650_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 196000, ],
    'CountWeighted'                                                                  : [ 1.95900516e+05, 1.95918969e+05, 1.95904047e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.95900516e+05, 1.95900516e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.95880412e+06, 1.95880950e+06, 1.95880950e+06, 1.95880738e+06, 1.95880950e+06, 1.95880412e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.95950125e+05, 1.96069859e+05, 2.97183500e+05, 1.95998078e+05, 1.94370375e+05, 1.05752766e+05, ],
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     1307489563), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        15016770852), # 15.02GB, avg file size 2.15GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_650_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_700_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_700_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99930031e+05, 1.99918219e+05, 1.99910281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99930031e+05, 1.99930031e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99906450e+06, 1.99906450e+06, 1.99906450e+06, 1.99906450e+06, 1.99906450e+06, 1.99906450e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00077641e+05, 2.00234844e+05, 3.04221562e+05, 1.99860406e+05, 1.98594031e+05, 1.07412531e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1354796370), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        15459043528), # 15.46GB, avg file size 3.09GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_700_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_750_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_750_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99900344e+05, 1.99889660e+05, 1.99887727e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99900344e+05, 1.99900344e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99894216e+06, 1.99894216e+06, 1.99894216e+06, 1.99894216e+06, 1.99894216e+06, 1.99894216e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00114496e+05, 2.00069738e+05, 3.04805344e+05, 1.99812320e+05, 1.98762602e+05, 1.06965865e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1374588243), # 1.37GB, avg file size 687.29MB
  ("fsize_db",                        15621663509), # 15.62GB, avg file size 918.92MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_800_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_800_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99866781e+05, 1.99887062e+05, 1.99856375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99866781e+05, 1.99866781e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99918825e+06, 1.99918825e+06, 1.99918825e+06, 1.99918825e+06, 1.99918825e+06, 1.99918825e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00012969e+05, 2.00371703e+05, 3.05309781e+05, 1.99925125e+05, 1.98438781e+05, 1.06573773e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1389814878), # 1.39GB, avg file size 1.39GB
  ("fsize_db",                        15721000671), # 15.72GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_800_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_850_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_850_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99865969e+05, 1.99896797e+05, 1.99918359e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99865969e+05, 1.99865969e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99897112e+06, 1.99897112e+06, 1.99897112e+06, 1.99897112e+06, 1.99897112e+06, 1.99897112e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00048844e+05, 1.99957844e+05, 3.06287688e+05, 1.99902719e+05, 1.99323062e+05, 1.06073156e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1402791553), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        15824798381), # 15.82GB, avg file size 1.98GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_850_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_900_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_900_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99884953e+05, 1.99897000e+05, 1.99881406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99884953e+05, 1.99884953e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99886300e+06, 1.99886150e+06, 1.99886150e+06, 1.99886300e+06, 1.99886150e+06, 1.99886300e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00064938e+05, 2.00231594e+05, 3.06511781e+05, 1.99898906e+05, 1.98862359e+05, 1.05766789e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1413983747), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        15947921131), # 15.95GB, avg file size 1.14GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_900_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1000_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_1000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99187188e+04, 9.99234375e+04, 9.99168594e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99187188e+04, 9.99187188e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99111500e+05, 9.99111500e+05, 9.99111500e+05, 9.99111500e+05, 9.99111500e+05, 9.99111500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99609922e+04, 9.99809219e+04, 1.53691875e+05, 1.00034406e+05, 9.96234219e+04, 5.25486641e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     719524145), # 719.52MB, avg file size 719.52MB
  ("fsize_db",                        8058532298), # 8.06GB, avg file size 1.15GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_1000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1250_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_1250_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98882188e+04, 9.98824531e+04, 9.98762578e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98882188e+04, 9.98882188e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.98855875e+05, 9.98860125e+05, 9.98860125e+05, 9.98855875e+05, 9.98860125e+05, 9.98855875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00001531e+05, 9.98137812e+04, 1.53595719e+05, 9.99816562e+04, 9.90831094e+04, 5.21567812e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     733638798), # 733.64MB, avg file size 733.64MB
  ("fsize_db",                        9385953952), # 9.39GB, avg file size 521.44MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_1250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1500_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_1500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98518203e+04, 9.98391250e+04, 9.98548203e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98518203e+04, 9.98518203e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.98365250e+05, 9.98357125e+05, 9.98357125e+05, 9.98365000e+05, 9.98357125e+05, 9.98365312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99542344e+04, 9.98711172e+04, 1.54486031e+05, 1.00017609e+05, 9.94050000e+04, 5.16458125e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     739247563), # 739.25MB, avg file size 739.25MB
  ("fsize_db",                        9486059274), # 9.49GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_1500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1750_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_1750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 98000, ],
    'CountWeighted'                                                                  : [ 9.77412969e+04, 9.77631250e+04, 9.77357344e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.77412969e+04, 9.77412969e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.77478500e+05, 9.77478500e+05, 9.77478500e+05, 9.77478500e+05, 9.77478500e+05, 9.77478500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.79749219e+04, 9.79483906e+04, 1.51914906e+05, 9.79292500e+04, 9.73941875e+04, 5.03091914e+04, ],
  }),
  ("nof_tree_events",                 98000),
  ("nof_db_events",                   98000),
  ("fsize_local",                     726329426), # 726.33MB, avg file size 726.33MB
  ("fsize_db",                        8276227918), # 8.28GB, avg file size 551.75MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_1750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_2000_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_2000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.96752812e+04, 9.96773047e+04, 9.96609844e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.96752812e+04, 9.96752812e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.96768125e+05, 9.96768125e+05, 9.96768125e+05, 9.96768125e+05, 9.96768125e+05, 9.96768125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99383594e+04, 1.00579258e+05, 1.54686578e+05, 1.00049531e+05, 9.80479453e+04, 5.09232695e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     741332795), # 741.33MB, avg file size 741.33MB
  ("fsize_db",                        9683084437), # 9.68GB, avg file size 569.59MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_2000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo4T_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_3000_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin0_3000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.88930859e+04, 9.89065000e+04, 9.88923906e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.88930859e+04, 9.88930859e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.89025500e+05, 9.89028750e+05, 9.89028750e+05, 9.89027625e+05, 9.89028750e+05, 9.89025500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99892578e+04, 9.99309219e+04, 1.55284938e+05, 9.99646562e+04, 9.90585625e+04, 5.07812812e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     739556552), # 739.56MB, avg file size 739.56MB
  ("fsize_db",                        9822846522), # 9.82GB, avg file size 545.71MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_3000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99959203e+05, 3.99975719e+05, 3.99968734e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.04867078e+05, 3.99953250e+05, 3.92217406e+05, 4.04867078e+05, 3.99953250e+05, 3.92217406e+05, 4.04867078e+05, 3.99953250e+05, 3.92217406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04867078e+05, 3.92217406e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.00001938e+06, 4.00001938e+06, 4.00001938e+06, 4.00001938e+06, 4.00001938e+06, 4.00001938e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99992266e+05, 3.99348219e+05, 5.50218531e+05, 3.99934750e+05, 4.00557188e+05, 2.66114078e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1410182611), # 1.41GB, avg file size 705.09MB
  ("fsize_db",                        20777026746), # 20.78GB, avg file size 2.60GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99985875e+05, 3.99958594e+05, 3.99928688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06202406e+05, 3.99975188e+05, 3.91150281e+05, 4.06202406e+05, 3.99975188e+05, 3.91150281e+05, 4.06202406e+05, 3.99975188e+05, 3.91150281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06202406e+05, 3.91150281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99904812e+06, 3.99904812e+06, 3.99904812e+06, 3.99904812e+06, 3.99904812e+06, 3.99904812e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99966203e+05, 3.99737344e+05, 5.50583844e+05, 3.99998984e+05, 4.00128891e+05, 2.65812828e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1431961153), # 1.43GB, avg file size 715.98MB
  ("fsize_db",                        20936620034), # 20.94GB, avg file size 2.62GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99952250e+05, 3.99985141e+05, 3.99911469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07491094e+05, 3.99952250e+05, 3.90120969e+05, 4.07491094e+05, 3.99952250e+05, 3.90120969e+05, 4.07491094e+05, 3.99952250e+05, 3.90120969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07491094e+05, 3.90120969e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99997588e+06, 3.99997588e+06, 3.99997588e+06, 3.99997588e+06, 3.99997588e+06, 3.99997588e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00005656e+05, 3.99898375e+05, 5.50470031e+05, 3.99947719e+05, 3.99579641e+05, 2.65529688e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1450906843), # 1.45GB, avg file size 725.45MB
  ("fsize_db",                        20729048194), # 20.73GB, avg file size 2.96GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99977359e+05, 3.99983703e+05, 3.99971297e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.08720797e+05, 3.99973938e+05, 3.89196266e+05, 4.08720797e+05, 3.99973938e+05, 3.89196266e+05, 4.08720797e+05, 3.99973938e+05, 3.89196266e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.08720797e+05, 3.89196266e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.00017212e+06, 4.00017212e+06, 4.00017212e+06, 4.00017212e+06, 4.00017212e+06, 4.00017212e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00071484e+05, 4.00354000e+05, 5.51201969e+05, 3.99874016e+05, 3.99345625e+05, 2.64975242e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1469785384), # 1.47GB, avg file size 734.89MB
  ("fsize_db",                        21136018972), # 21.14GB, avg file size 2.35GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 297000, ],
    'CountWeighted'                                                                  : [ 2.96994902e+05, 2.96966555e+05, 2.96959102e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.05120480e+05, 2.96991410e+05, 2.87608992e+05, 3.05120480e+05, 2.96991410e+05, 2.87608992e+05, 3.05120480e+05, 2.96991410e+05, 2.87608992e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.05120480e+05, 2.87608992e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.96941769e+06, 2.96941769e+06, 2.96941769e+06, 2.96941769e+06, 2.96941769e+06, 2.96941769e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.96979684e+05, 2.97243680e+05, 4.09542977e+05, 2.96969875e+05, 2.96425645e+05, 1.96405850e+05, ],
  }),
  ("nof_tree_events",                 297000),
  ("nof_db_events",                   297000),
  ("fsize_local",                     1120834431), # 1.12GB, avg file size 560.42MB
  ("fsize_db",                        15976487156), # 15.98GB, avg file size 1.78GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99915727e+05, 2.99978930e+05, 2.99953871e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09804426e+05, 2.99914723e+05, 2.89284398e+05, 3.09804426e+05, 2.99914723e+05, 2.89284398e+05, 3.09804426e+05, 2.99914723e+05, 2.89284398e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09804426e+05, 2.89284398e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99959988e+06, 2.99959988e+06, 2.99959988e+06, 2.99959988e+06, 2.99959988e+06, 2.99959988e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99953184e+05, 3.00097793e+05, 4.14365625e+05, 3.00009543e+05, 2.99755598e+05, 1.97915289e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1157481935), # 1.16GB, avg file size 578.74MB
  ("fsize_db",                        16324747735), # 16.32GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99991992e+05, 2.99942848e+05, 2.99942469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11975238e+05, 2.99991992e+05, 2.87627379e+05, 3.11975238e+05, 2.99991992e+05, 2.87627379e+05, 3.11975238e+05, 2.99991992e+05, 2.87627379e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11975473e+05, 2.87627160e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99948619e+06, 2.99949969e+06, 2.99949969e+06, 2.99948619e+06, 2.99949969e+06, 2.99948619e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99854754e+05, 3.00121039e+05, 4.15458906e+05, 3.00121570e+05, 3.00063395e+05, 1.97303039e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1195370701), # 1.20GB, avg file size 597.69MB
  ("fsize_db",                        17221121634), # 17.22GB, avg file size 2.87GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99995285e+05, 2.99942445e+05, 2.99998441e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15115168e+05, 2.99993801e+05, 2.85254922e+05, 3.15115168e+05, 2.99993801e+05, 2.85254922e+05, 3.15115168e+05, 2.99993801e+05, 2.85254922e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15115168e+05, 2.85254922e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99930369e+06, 2.99930369e+06, 2.99930369e+06, 2.99930369e+06, 2.99930369e+06, 2.99930369e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99848949e+05, 2.99565453e+05, 4.16281953e+05, 3.00205648e+05, 3.00570777e+05, 1.96627996e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1253114342), # 1.25GB, avg file size 626.56MB
  ("fsize_db",                        16917922951), # 16.92GB, avg file size 2.82GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 295000, ],
    'CountWeighted'                                                                  : [ 2.94962414e+05, 2.94981516e+05, 2.94964398e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.12482707e+05, 2.94962414e+05, 2.78510332e+05, 3.12482707e+05, 2.94962414e+05, 2.78510332e+05, 3.12482707e+05, 2.94962414e+05, 2.78510332e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.12482801e+05, 2.78510207e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.94967756e+06, 2.94967756e+06, 2.94967756e+06, 2.94967756e+06, 2.94967756e+06, 2.94967756e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.94924012e+05, 2.94791117e+05, 4.09737867e+05, 2.95098543e+05, 2.94920105e+05, 1.92585111e+05, ],
  }),
  ("nof_tree_events",                 295000),
  ("nof_db_events",                   295000),
  ("fsize_local",                     1280547229), # 1.28GB, avg file size 640.27MB
  ("fsize_db",                        16095046767), # 16.10GB, avg file size 1.79GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99946645e+05, 2.99942930e+05, 2.99956199e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20053426e+05, 2.99938461e+05, 2.81462238e+05, 3.20053426e+05, 2.99938461e+05, 2.81462238e+05, 3.20053426e+05, 2.99938461e+05, 2.81462238e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20053426e+05, 2.81462238e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99962253e+06, 2.99962703e+06, 2.99962703e+06, 2.99962303e+06, 2.99962703e+06, 2.99962253e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00000840e+05, 2.99939320e+05, 4.17203992e+05, 2.99974461e+05, 2.99559012e+05, 1.95258732e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1343634310), # 1.34GB, avg file size 671.82MB
  ("fsize_db",                        17370100767), # 17.37GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99959180e+05, 2.99926375e+05, 2.99936594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22098762e+05, 2.99959180e+05, 2.79880867e+05, 3.22098762e+05, 2.99959180e+05, 2.79880867e+05, 3.22098762e+05, 2.99959180e+05, 2.79880867e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22098762e+05, 2.79880867e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99969422e+06, 2.99969422e+06, 2.99969422e+06, 2.99969422e+06, 2.99969422e+06, 2.99969422e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99985660e+05, 2.99867863e+05, 4.18002367e+05, 2.99953031e+05, 2.99834426e+05, 1.94673230e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1382050553), # 1.38GB, avg file size 691.03MB
  ("fsize_db",                        18535631090), # 18.54GB, avg file size 2.32GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99961906e+05, 1.99991438e+05, 1.99946312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15947047e+05, 1.99961906e+05, 1.85651406e+05, 2.15947047e+05, 1.99961906e+05, 1.85651406e+05, 2.15947047e+05, 1.99961906e+05, 1.85651406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15947047e+05, 1.85651406e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99942475e+06, 1.99942475e+06, 1.99942475e+06, 1.99942475e+06, 1.99942475e+06, 1.99942475e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00072703e+05, 2.00148625e+05, 2.79051750e+05, 1.99858938e+05, 1.99611844e+05, 1.29389719e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     944631483), # 944.63MB, avg file size 944.63MB
  ("fsize_db",                        12464159691), # 12.46GB, avg file size 3.12GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99980281e+05, 1.99971078e+05, 1.99969125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17042516e+05, 1.99980281e+05, 1.84813594e+05, 2.17042516e+05, 1.99980281e+05, 1.84813594e+05, 2.17042516e+05, 1.99980281e+05, 1.84813594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17042531e+05, 1.84813594e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99960262e+06, 1.99960262e+06, 1.99960262e+06, 1.99960262e+06, 1.99960262e+06, 1.99960262e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99978312e+05, 1.99970875e+05, 2.79372406e+05, 1.99996672e+05, 1.99557344e+05, 1.28946703e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     967084696), # 967.08MB, avg file size 967.08MB
  ("fsize_db",                        12571955086), # 12.57GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99961750e+05, 1.99960969e+05, 1.99951031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18006875e+05, 1.99961750e+05, 1.84042266e+05, 2.18006875e+05, 1.99961750e+05, 1.84042266e+05, 2.18006875e+05, 1.99961750e+05, 1.84042266e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18006875e+05, 1.84042266e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99953662e+06, 1.99953662e+06, 1.99953662e+06, 1.99953662e+06, 1.99953662e+06, 1.99953662e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00093953e+05, 2.00162312e+05, 2.79560219e+05, 1.99867562e+05, 1.99242016e+05, 1.28696750e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     989218728), # 989.22MB, avg file size 989.22MB
  ("fsize_db",                        12721700410), # 12.72GB, avg file size 578.26MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 196000, ],
    'CountWeighted'                                                                  : [ 1.95930531e+05, 1.95962719e+05, 1.95948000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.14550672e+05, 1.95929328e+05, 1.79694203e+05, 2.14550672e+05, 1.95929328e+05, 1.79694203e+05, 2.14550672e+05, 1.95929328e+05, 1.79694203e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.14550672e+05, 1.79694203e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.95961650e+06, 1.95961650e+06, 1.95961650e+06, 1.95961650e+06, 1.95961650e+06, 1.95961650e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.96057656e+05, 1.95997344e+05, 2.74805406e+05, 1.95882641e+05, 1.95923359e+05, 1.25746898e+05, ],
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     986488724), # 986.49MB, avg file size 986.49MB
  ("fsize_db",                        11417510981), # 11.42GB, avg file size 1.90GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99873562e+05, 1.99888625e+05, 1.99902453e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19742156e+05, 1.99873562e+05, 1.82696797e+05, 2.19742156e+05, 1.99873562e+05, 1.82696797e+05, 2.19742156e+05, 1.99873562e+05, 1.82696797e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.19742188e+05, 1.82696781e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99919375e+06, 1.99919375e+06, 1.99919375e+06, 1.99919375e+06, 1.99919375e+06, 1.99919375e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99925359e+05, 1.99926656e+05, 2.81140844e+05, 2.00023500e+05, 2.00311688e+05, 1.28006203e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1022312147), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        12832750406), # 12.83GB, avg file size 2.14GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99967375e+05, 1.99953281e+05, 1.99945234e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99967375e+05, 1.99967375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99958625e+06, 1.99958625e+06, 1.99958625e+06, 1.99958625e+06, 1.99958625e+06, 1.99958625e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00103984e+05, 2.00169250e+05, 2.80519000e+05, 1.99825281e+05, 1.99292906e+05, 1.27885859e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1041991362), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        12511610477), # 12.51GB, avg file size 2.50GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99954500e+05, 1.99981094e+05, 1.99949078e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99954500e+05, 1.99954500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99940588e+06, 1.99940588e+06, 1.99940588e+06, 1.99940588e+06, 1.99940588e+06, 1.99940588e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99923750e+05, 1.99649719e+05, 2.81514844e+05, 2.00067844e+05, 2.00483719e+05, 1.27617570e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1054895360), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        13263531937), # 13.26GB, avg file size 780.21MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99709531e+04, 9.99874297e+04, 9.99696719e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11332141e+05, 9.99709531e+04, 9.03204531e+04, 1.11332141e+05, 9.99709531e+04, 9.03204531e+04, 1.11332141e+05, 9.99709531e+04, 9.03204531e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11332141e+05, 9.03204531e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99747625e+05, 9.99747625e+05, 9.99747625e+05, 9.99747625e+05, 9.99747625e+05, 9.99747625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00034812e+05, 9.98624219e+04, 1.41067219e+05, 9.99278984e+04, 1.00310914e+05, 6.36117969e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     534974381), # 534.97MB, avg file size 534.97MB
  ("fsize_db",                        6575758202), # 6.58GB, avg file size 657.58MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99634453e+04, 9.99574219e+04, 9.99561328e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99634453e+04, 9.99634453e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99529438e+05, 9.99529438e+05, 9.99529438e+05, 9.99529438e+05, 9.99529438e+05, 9.99529438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00058461e+05, 9.99188750e+04, 1.41628906e+05, 9.99129922e+04, 1.00310719e+05, 6.31611641e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     549578351), # 549.58MB, avg file size 549.58MB
  ("fsize_db",                        6795292081), # 6.80GB, avg file size 1.70GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_1250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99309062e+04, 9.99318438e+04, 9.99241719e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99309062e+04, 9.99309062e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99202562e+05, 9.99202562e+05, 9.99202562e+05, 9.99202562e+05, 9.99202562e+05, 9.99202562e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.98852656e+04, 9.98675000e+04, 1.41772594e+05, 1.00090047e+05, 1.00024734e+05, 6.27911016e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     537918734), # 537.92MB, avg file size 537.92MB
  ("fsize_db",                        6511569391), # 6.51GB, avg file size 1.63GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_1500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99379062e+04, 9.99342578e+04, 9.99358438e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99379062e+04, 9.99379062e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99378875e+05, 9.99378875e+05, 9.99378875e+05, 9.99378875e+05, 9.99378875e+05, 9.99378875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00001750e+05, 1.00264805e+05, 1.41740219e+05, 9.99613125e+04, 9.92967969e+04, 6.25101641e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     531227738), # 531.23MB, avg file size 531.23MB
  ("fsize_db",                        6883287799), # 6.88GB, avg file size 625.75MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_1750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99298203e+04, 9.99231172e+04, 9.99407031e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15697547e+05, 9.99295078e+04, 8.72056016e+04, 1.15697547e+05, 9.99295078e+04, 8.72056016e+04, 1.15697547e+05, 9.99295078e+04, 8.72056016e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15700406e+05, 8.72027266e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99256812e+05, 9.99273750e+05, 9.99273750e+05, 9.99258000e+05, 9.99273750e+05, 9.99256812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99767969e+04, 9.99303594e+04, 1.42089016e+05, 9.99709844e+04, 9.98412891e+04, 6.23779609e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     524466329), # 524.47MB, avg file size 524.47MB
  ("fsize_db",                        6432782988), # 6.43GB, avg file size 494.83MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_2000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98227578e+04, 9.98266641e+04, 9.98121641e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17109938e+05, 9.98227578e+04, 8.60675703e+04, 1.17109938e+05, 9.98227578e+04, 8.60675703e+04, 1.17109938e+05, 9.98227578e+04, 8.60675703e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.17110688e+05, 8.60668281e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.98255750e+05, 9.98255750e+05, 9.98255750e+05, 9.98255750e+05, 9.98255750e+05, 9.98255750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99823594e+04, 9.98004531e+04, 1.42252203e+05, 9.99546875e+04, 9.99707656e+04, 6.22774688e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     522430525), # 522.43MB, avg file size 522.43MB
  ("fsize_db",                        6860162901), # 6.86GB, avg file size 2.29GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_2500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo4T_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.97554688e+04, 9.97683125e+04, 9.97462969e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.18454180e+05, 9.97552266e+04, 8.50870781e+04, 1.18454180e+05, 9.97552266e+04, 8.50870781e+04, 1.18454180e+05, 9.97552266e+04, 8.50870781e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.18461188e+05, 8.50800156e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.97642500e+05, 9.97642500e+05, 9.97642500e+05, 9.97642500e+05, 9.97642500e+05, 9.97642500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00006102e+05, 9.99163594e+04, 1.42871516e+05, 9.99538750e+04, 1.00233617e+05, 6.20448008e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     523047209), # 523.05MB, avg file size 523.05MB
  ("fsize_db",                        6476075631), # 6.48GB, avg file size 1.62GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_3000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_250_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_250_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.94304078e+05, 3.94304844e+05, 3.94265094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.33449297e+05, 3.95686812e+05, 3.64247344e+05, 4.31904547e+05, 3.94302250e+05, 3.62997344e+05, 4.30698344e+05, 3.93221484e+05, 3.62022500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.35250422e+05, 3.60282906e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94309800e+06, 3.94309800e+06, 3.94309800e+06, 3.94309800e+06, 3.94309800e+06, 3.94309800e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99822797e+05, 3.99926578e+05, 5.57310562e+05, 3.99971078e+05, 3.99380234e+05, 2.56424109e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2153789971), # 2.15GB, avg file size 1.08GB
  ("fsize_db",                        25847161991), # 25.85GB, avg file size 1.85GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_260_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_260_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.96196438e+05, 3.96122234e+05, 3.96175875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.25574797e+05, 3.97487844e+05, 3.72974750e+05, 4.24158641e+05, 3.96196438e+05, 3.71790781e+05, 4.23062766e+05, 3.95197453e+05, 3.70875953e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.29844766e+05, 3.66699734e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96223950e+06, 3.96224350e+06, 3.96224350e+06, 3.96224000e+06, 3.96224350e+06, 3.96223925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99990531e+05, 3.99712578e+05, 5.48817062e+05, 3.99838125e+05, 4.00338766e+05, 2.64514297e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1942047904), # 1.94GB, avg file size 971.02MB
  ("fsize_db",                        25361450382), # 25.36GB, avg file size 3.62GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_260_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_270_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_270_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 382000, ],
    'CountWeighted'                                                                  : [ 3.78360289e+05, 3.78330641e+05, 3.78325172e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06671641e+05, 3.79569281e+05, 3.55947656e+05, 4.05339109e+05, 3.78355266e+05, 3.54835477e+05, 4.04307297e+05, 3.77415219e+05, 3.53975312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.10673156e+05, 3.50059070e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.78302625e+06, 3.78303175e+06, 3.78303175e+06, 3.78302725e+06, 3.78303175e+06, 3.78302625e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.81891984e+05, 3.81485547e+05, 5.24107344e+05, 3.81985344e+05, 3.82761391e+05, 2.52770719e+05, ],
  }),
  ("nof_tree_events",                 382000),
  ("nof_db_events",                   382000),
  ("fsize_local",                     1854982081), # 1.85GB, avg file size 927.49MB
  ("fsize_db",                        23019807000), # 23.02GB, avg file size 1.92GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_270_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_280_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_280_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 397000, ],
    'CountWeighted'                                                                  : [ 3.93459266e+05, 3.93333609e+05, 3.93451906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.23103406e+05, 3.94690109e+05, 3.69899391e+05, 4.21746203e+05, 3.93454141e+05, 3.68766953e+05, 4.20695250e+05, 3.92496672e+05, 3.67891172e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.27064031e+05, 3.64025781e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.93386862e+06, 3.93386338e+06, 3.93386338e+06, 3.93386862e+06, 3.93386338e+06, 3.93386825e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96944500e+05, 3.97291516e+05, 5.43622281e+05, 3.96922984e+05, 3.96296344e+05, 2.63068562e+05, ],
  }),
  ("nof_tree_events",                 397000),
  ("nof_db_events",                   397000),
  ("fsize_local",                     1925237314), # 1.93GB, avg file size 962.62MB
  ("fsize_db",                        24078569317), # 24.08GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_280_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_300_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_300_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 292000, ],
    'CountWeighted'                                                                  : [ 2.89353965e+05, 2.89370531e+05, 2.89358082e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11742938e+05, 2.90210410e+05, 2.71566090e+05, 3.10799852e+05, 2.89353965e+05, 2.70784453e+05, 3.10068277e+05, 2.88690562e+05, 2.70178605e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.14395746e+05, 2.67593754e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.89385803e+06, 2.89389078e+06, 2.89389078e+06, 2.89385828e+06, 2.89389078e+06, 2.89385803e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.91831336e+05, 2.92159250e+05, 3.99443086e+05, 2.92017695e+05, 2.91372047e+05, 1.93706324e+05, ],
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     1416036953), # 1.42GB, avg file size 708.02MB
  ("fsize_db",                        17208593955), # 17.21GB, avg file size 1.15GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_300_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_320_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_320_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.97159281e+05, 2.97154531e+05, 2.97165555e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20601105e+05, 2.97932250e+05, 2.78341074e+05, 3.19747855e+05, 2.97159281e+05, 2.77636949e+05, 3.19085250e+05, 2.96559730e+05, 2.77090598e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.23128438e+05, 2.74633875e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.97156931e+06, 2.97158634e+06, 2.97158634e+06, 2.97157047e+06, 2.97158634e+06, 2.97157041e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00025258e+05, 3.00030379e+05, 4.10461477e+05, 2.99846105e+05, 3.00064855e+05, 1.99405504e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1453002422), # 1.45GB, avg file size 726.50MB
  ("fsize_db",                        18909348383), # 18.91GB, avg file size 859.52MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_320_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_350_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_350_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.97150098e+05, 2.97110160e+05, 2.97153547e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.21577891e+05, 2.97857777e+05, 2.77447750e+05, 3.20793848e+05, 2.97150098e+05, 2.76804430e+05, 3.20184016e+05, 2.96599383e+05, 2.76304395e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.23807340e+05, 2.74143953e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.97107269e+06, 2.97107809e+06, 2.97107809e+06, 2.97107056e+06, 2.97107809e+06, 2.97107275e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99921648e+05, 2.99994219e+05, 4.09434148e+05, 2.99950930e+05, 2.99492895e+05, 1.99753207e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1452926338), # 1.45GB, avg file size 726.46MB
  ("fsize_db",                        18896343646), # 18.90GB, avg file size 899.83MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_350_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_400_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_400_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 297000, ],
    'CountWeighted'                                                                  : [ 2.94143785e+05, 2.94124941e+05, 2.94144578e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.19858234e+05, 2.94728824e+05, 2.73294316e+05, 3.19196223e+05, 2.94133672e+05, 2.72755738e+05, 3.18680145e+05, 2.93669766e+05, 2.72336176e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.21702129e+05, 2.70573629e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.94125597e+06, 2.94124172e+06, 2.94124172e+06, 2.94125147e+06, 2.94124172e+06, 2.94125497e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.96956113e+05, 2.97130195e+05, 4.05038195e+05, 2.96956176e+05, 2.96536180e+05, 1.98212270e+05, ],
  }),
  ("nof_tree_events",                 297000),
  ("nof_db_events",                   297000),
  ("fsize_local",                     1438687201), # 1.44GB, avg file size 719.34MB
  ("fsize_db",                        17699306957), # 17.70GB, avg file size 884.97MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_400_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_450_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_450_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 298000, ],
    'CountWeighted'                                                                  : [ 2.95158145e+05, 2.95116648e+05, 2.95143918e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22655609e+05, 2.95621539e+05, 2.72771094e+05, 3.22137211e+05, 2.95158145e+05, 2.72353586e+05, 3.21732016e+05, 2.94795633e+05, 2.72027320e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.24165730e+05, 2.70602078e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.95150309e+06, 2.95150559e+06, 2.95150559e+06, 2.95150181e+06, 2.95150559e+06, 2.95150331e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.97916590e+05, 2.97972051e+05, 4.05764016e+05, 2.98005617e+05, 2.97784648e+05, 1.99466461e+05, ],
  }),
  ("nof_tree_events",                 298000),
  ("nof_db_events",                   298000),
  ("fsize_local",                     1448183129), # 1.45GB, avg file size 724.09MB
  ("fsize_db",                        18708714887), # 18.71GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_450_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_500_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_500_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.96837117e+05, 2.96907480e+05, 2.96877090e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.26384891e+05, 2.97236258e+05, 2.72964879e+05, 3.25937715e+05, 2.96837117e+05, 2.72606594e+05, 3.25587660e+05, 2.96525465e+05, 2.72326180e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.27575688e+05, 2.71218766e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.96930212e+06, 2.96930612e+06, 2.96930612e+06, 2.96930538e+06, 2.96930612e+06, 2.96930212e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00004227e+05, 3.00003371e+05, 4.08463156e+05, 2.99890230e+05, 2.99968926e+05, 2.00933980e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1465250531), # 1.47GB, avg file size 732.63MB
  ("fsize_db",                        18801588414), # 18.80GB, avg file size 3.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_550_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_550_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.96723660e+05, 2.96743340e+05, 2.96708766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.96723660e+05, 2.96723660e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.96724775e+06, 2.96727878e+06, 2.96727878e+06, 2.96724622e+06, 2.96727878e+06, 2.96724622e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00067254e+05, 2.99664391e+05, 4.08059953e+05, 2.99822648e+05, 3.00513172e+05, 2.01451574e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1482314658), # 1.48GB, avg file size 741.16MB
  ("fsize_db",                        18305564047), # 18.31GB, avg file size 2.62GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_550_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_600_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_600_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.97644297e+05, 1.97631562e+05, 1.97668094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19641109e+05, 1.97829875e+05, 1.79926875e+05, 2.19431531e+05, 1.97644297e+05, 1.79761375e+05, 2.19266719e+05, 1.97498375e+05, 1.79631250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.20258453e+05, 1.79068688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.97658338e+06, 1.97660462e+06, 1.97660462e+06, 1.97658338e+06, 1.97660462e+06, 1.97658338e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99944438e+05, 2.00065156e+05, 2.71648500e+05, 1.99988734e+05, 1.99750031e+05, 1.34411828e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     986381808), # 986.38MB, avg file size 986.38MB
  ("fsize_db",                        12515645230), # 12.52GB, avg file size 2.50GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_600_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_650_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_650_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.97522516e+05, 1.97516938e+05, 1.97537000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.20594281e+05, 1.97690312e+05, 1.79053891e+05, 2.20403781e+05, 1.97522109e+05, 1.78903953e+05, 2.20253938e+05, 1.97389719e+05, 1.78786031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21153734e+05, 1.78285812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.97535712e+06, 1.97535712e+06, 1.97535712e+06, 1.97535712e+06, 1.97535712e+06, 1.97535712e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00010422e+05, 1.99987750e+05, 2.71173938e+05, 1.99879766e+05, 1.99582141e+05, 1.34540781e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     992247644), # 992.25MB, avg file size 992.25MB
  ("fsize_db",                        12072020917), # 12.07GB, avg file size 2.41GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_650_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_700_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_700_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 194000, ],
    'CountWeighted'                                                                  : [ 1.91288609e+05, 1.91300344e+05, 1.91336984e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.14676719e+05, 1.91429484e+05, 1.72649953e+05, 2.14516734e+05, 1.91288609e+05, 1.72524969e+05, 2.14390562e+05, 1.91177656e+05, 1.72426438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15167094e+05, 1.71995812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.91293875e+06, 1.91292800e+06, 1.91292800e+06, 1.91293900e+06, 1.91292800e+06, 1.91293900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.93939188e+05, 1.93895672e+05, 2.62966406e+05, 1.94009594e+05, 1.93715391e+05, 1.30672781e+05, ],
  }),
  ("nof_tree_events",                 194000),
  ("nof_db_events",                   194000),
  ("fsize_local",                     970391208), # 970.39MB, avg file size 970.39MB
  ("fsize_db",                        12224804271), # 12.22GB, avg file size 873.20MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_700_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_750_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 198000, ],
    'CountWeighted'                                                                  : [ 1.95205281e+05, 1.95190484e+05, 1.95176906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.20160859e+05, 1.95329656e+05, 1.75357594e+05, 2.20019219e+05, 1.95205281e+05, 1.75247281e+05, 2.19907438e+05, 1.95106969e+05, 1.75160266e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.20580219e+05, 1.74801844e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.95183175e+06, 1.95183175e+06, 1.95183175e+06, 1.95183175e+06, 1.95183175e+06, 1.95183175e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.97872094e+05, 1.97976281e+05, 2.68412562e+05, 1.98055281e+05, 1.97700109e+05, 1.33329906e+05, ],
  }),
  ("nof_tree_events",                 198000),
  ("nof_db_events",                   198000),
  ("fsize_local",                     996318348), # 996.32MB, avg file size 996.32MB
  ("fsize_db",                        12643257670), # 12.64GB, avg file size 574.69MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_800_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_800_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.97026000e+05, 1.97049125e+05, 1.97066625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.97026000e+05, 1.97026000e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.97048162e+06, 1.97049025e+06, 1.97049025e+06, 1.97048175e+06, 1.97049025e+06, 1.97048162e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99972141e+05, 1.99938406e+05, 2.71056312e+05, 1.99968625e+05, 1.99908297e+05, 1.34937062e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1018925628), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        12034640363), # 12.03GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_800_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_850_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_850_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.96774656e+05, 1.96748484e+05, 1.96749078e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.23997703e+05, 1.96863328e+05, 1.75346031e+05, 2.23895922e+05, 1.96774656e+05, 1.75267984e+05, 2.23815328e+05, 1.96704344e+05, 1.75206125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.24333812e+05, 1.74931391e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.96735025e+06, 1.96734275e+06, 1.96734275e+06, 1.96735075e+06, 1.96734275e+06, 1.96735075e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99894438e+05, 2.00028422e+05, 2.70667062e+05, 1.99973500e+05, 1.99576312e+05, 1.35057188e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1017102976), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        11719677487), # 11.72GB, avg file size 2.93GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_850_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_900_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_900_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.96776656e+05, 1.96755266e+05, 1.96785094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.24996062e+05, 1.96863281e+05, 1.74699953e+05, 2.24896062e+05, 1.96776141e+05, 1.74623203e+05, 2.24816859e+05, 1.96707016e+05, 1.74562469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.25319375e+05, 1.74302094e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.96758562e+06, 1.96759125e+06, 1.96759125e+06, 1.96758288e+06, 1.96759125e+06, 1.96758300e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99980719e+05, 1.99719859e+05, 2.71167469e+05, 1.99928000e+05, 2.00490781e+05, 1.35104641e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1023565705), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        11740308279), # 11.74GB, avg file size 2.35GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_900_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1000_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_1000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.81890938e+04, 9.81892031e+04, 9.81907656e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13229016e+05, 9.82232031e+04, 8.65375312e+04, 1.13188281e+05, 9.81878438e+04, 8.65065156e+04, 1.13155906e+05, 9.81597422e+04, 8.64819219e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13364977e+05, 8.63832344e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.81976625e+05, 9.81987750e+05, 9.81987750e+05, 9.81977812e+05, 9.81987750e+05, 9.81976250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99624219e+04, 1.00019547e+05, 1.35022031e+05, 9.99180938e+04, 9.96228203e+04, 6.76415625e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     516201256), # 516.20MB, avg file size 516.20MB
  ("fsize_db",                        6057895707), # 6.06GB, avg file size 1.51GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_1000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-1200_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1200_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_1200_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.77056719e+04, 9.77104609e+04, 9.77033281e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.14426531e+05, 9.77276875e+04, 8.49805156e+04, 1.14401016e+05, 9.77056719e+04, 8.49613672e+04, 1.14380641e+05, 9.76881641e+04, 8.49461016e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.14524172e+05, 8.48817734e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.77024688e+05, 9.77030375e+05, 9.77030375e+05, 9.77023812e+05, 9.77030375e+05, 9.77023812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99773984e+04, 9.99105234e+04, 1.35391281e+05, 9.99594766e+04, 1.00328164e+05, 6.77564141e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     521913805), # 521.91MB, avg file size 521.91MB
  ("fsize_db",                        6411531409), # 6.41GB, avg file size 712.39MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_1200_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1250_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_1250_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.73204609e+04, 9.73410547e+04, 9.72994375e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.73204609e+04, 9.73204609e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.73149125e+05, 9.73126625e+05, 9.73126625e+05, 9.73149375e+05, 9.73126625e+05, 9.73149375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99630156e+04, 9.98976953e+04, 1.34726438e+05, 9.99572812e+04, 9.98165859e+04, 6.79395312e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     525897964), # 525.90MB, avg file size 525.90MB
  ("fsize_db",                        6251695894), # 6.25GB, avg file size 1.56GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_1250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1500_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_1500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.68681562e+04, 9.68707344e+04, 9.68651328e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.68681562e+04, 9.68681562e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.68599688e+05, 9.68599688e+05, 9.68599688e+05, 9.68599688e+05, 9.68599688e+05, 9.68599688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99670000e+04, 9.98696094e+04, 1.35068562e+05, 9.99476172e+04, 1.00335531e+05, 6.80162969e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     520711601), # 520.71MB, avg file size 520.71MB
  ("fsize_db",                        6261842364), # 6.26GB, avg file size 2.09GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_1500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1750_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_1750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.61190156e+04, 9.61173906e+04, 9.61368047e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.16870742e+05, 9.61336094e+04, 8.09939062e+04, 1.16853562e+05, 9.61190156e+04, 8.09814062e+04, 1.16839797e+05, 9.61073594e+04, 8.09713750e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.16941203e+05, 8.09444531e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.61266375e+05, 9.61266375e+05, 9.61266375e+05, 9.61266375e+05, 9.61266375e+05, 9.61266375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99546562e+04, 9.99977109e+04, 1.34352125e+05, 9.99417109e+04, 9.97520000e+04, 6.82222969e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     514971543), # 514.97MB, avg file size 514.97MB
  ("fsize_db",                        6467004835), # 6.47GB, avg file size 2.16GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_1750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_2000_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_2000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.51585000e+04, 9.51809062e+04, 9.51447812e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17498922e+05, 9.51703125e+04, 7.91542734e+04, 1.17484875e+05, 9.51585000e+04, 7.91442109e+04, 1.17473578e+05, 9.51490000e+04, 7.91361250e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.17526438e+05, 7.91538750e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.51725688e+05, 9.51725688e+05, 9.51725688e+05, 9.51725688e+05, 9.51725688e+05, 9.51725688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99310078e+04, 1.00055641e+05, 1.34450969e+05, 9.99382656e+04, 1.00028266e+05, 6.84214297e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     513439851), # 513.44MB, avg file size 513.44MB
  ("fsize_db",                        6463629715), # 6.46GB, avg file size 1.62GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_2000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_2500_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_2500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.29645938e+04, 9.29718750e+04, 9.29682969e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.29645938e+04, 9.29645938e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.29606500e+05, 9.29606500e+05, 9.29606500e+05, 9.29606500e+05, 9.29606500e+05, 9.29606500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99713516e+04, 9.98727031e+04, 1.33649906e+05, 9.98488750e+04, 1.00208156e+05, 6.90916719e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     511593647), # 511.59MB, avg file size 511.59MB
  ("fsize_db",                        6303222189), # 6.30GB, avg file size 1.58GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_2500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo4T_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_3000_hh_tttt"),
  ("process_name_specific",           "signal_vbf_spin2_3000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 8.97061250e+04, 8.97327188e+04, 8.96927344e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 8.97061250e+04, 8.97061250e+04, ],
    'CountWeightedPSWeight'                                                          : [ 8.97066750e+05, 8.97066750e+05, 8.97066750e+05, 8.97066750e+05, 8.97066750e+05, 8.97066750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.98697031e+04, 1.00022625e+05, 1.32911500e+05, 9.99256406e+04, 9.98996406e+04, 6.96123906e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     504973083), # 504.97MB, avg file size 504.97MB
  ("fsize_db",                        6621087952), # 6.62GB, avg file size 472.93MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_3000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2v2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 3.99943938e+05, 3.99939953e+05, 3.99940414e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99943938e+05, 3.99943938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99937962e+06, 3.99938250e+06, 3.99938250e+06, 3.99938125e+06, 3.99938250e+06, 3.99937962e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99770969e+05, 4.00334117e+05, 5.63889781e+05, 4.00176172e+05, 3.98708000e+05, 2.53594641e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1418319724), # 1.42GB, avg file size 472.77MB
  ("fsize_db",                        21134388781), # 21.13GB, avg file size 960.65MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 4.00002547e+05, 3.99957234e+05, 3.99983000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06215781e+05, 3.99999766e+05, 3.91165328e+05, 4.06215781e+05, 3.99999766e+05, 3.91165328e+05, 4.06215781e+05, 3.99999766e+05, 3.91165328e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06216281e+05, 3.91164828e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.66301212e+06, 2.60966006e+06, 3.39396650e+06, 2.66243412e+06, 2.35244525e+06, 1.68982206e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99858969e+05, 3.99627422e+05, 5.63828250e+05, 4.00144500e+05, 3.99378266e+05, 2.53731141e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1427956472), # 1.43GB, avg file size 713.98MB
  ("fsize_db",                        20298425114), # 20.30GB, avg file size 2.03GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 393998, ],
    'CountWeighted'                                                                  : [ 3.93932547e+05, 3.93910484e+05, 3.93903797e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.01367953e+05, 3.93932547e+05, 3.84263047e+05, 4.01367953e+05, 3.93932547e+05, 3.84263047e+05, 4.01367953e+05, 3.93932547e+05, 3.84263047e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.01367953e+05, 3.84263047e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.77426000e+05, 9.77177031e+05, 1.37007800e+06, 9.76905688e+05, 9.66341906e+05, 6.18495969e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.94057516e+05, 3.93964141e+05, 5.56935078e+05, 3.93850109e+05, 3.94157328e+05, 2.49351664e+05, ],
  }),
  ("nof_tree_events",                 393998),
  ("nof_db_events",                   393998),
  ("fsize_local",                     1425958029), # 1.43GB, avg file size 712.98MB
  ("fsize_db",                        21723772822), # 21.72GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 3.99941734e+05, 3.99915984e+05, 3.99958344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99941734e+05, 3.99941734e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.27295025e+06, 1.27355938e+06, 1.77046988e+06, 1.27345991e+06, 1.24293722e+06, 8.04949500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99908594e+05, 4.00130094e+05, 5.65560156e+05, 4.00066109e+05, 3.99800375e+05, 2.52884156e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1483695351), # 1.48GB, avg file size 741.85MB
  ("fsize_db",                        21797314763), # 21.80GB, avg file size 1.98GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99953176e+05, 2.99940980e+05, 2.99933059e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08220852e+05, 2.99952344e+05, 2.90503301e+05, 3.08220852e+05, 2.99952344e+05, 2.90503301e+05, 3.08220852e+05, 2.99952344e+05, 2.90503301e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08220852e+05, 2.90503301e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.09225078e+05, 8.09348109e+05, 1.13227756e+06, 8.09213391e+05, 7.96071078e+05, 5.10764336e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99957695e+05, 3.00011137e+05, 4.24022039e+05, 2.99954219e+05, 2.99391129e+05, 1.89327355e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1136505315), # 1.14GB, avg file size 568.25MB
  ("fsize_db",                        16029048036), # 16.03GB, avg file size 1.00GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2v2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 293996, ],
    'CountWeighted'                                                                  : [ 2.93952531e+05, 2.93945414e+05, 2.93954227e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.03598109e+05, 2.93949797e+05, 2.83487984e+05, 3.03598109e+05, 2.93949797e+05, 2.83487984e+05, 3.03598109e+05, 2.93949797e+05, 2.83487984e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.03602656e+05, 2.83483438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 7.25411797e+05, 7.25402328e+05, 1.01897662e+06, 7.24749891e+05, 7.16156609e+05, 4.56283594e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.94109711e+05, 2.94112562e+05, 4.16648359e+05, 2.93848180e+05, 2.93869242e+05, 1.84997672e+05, ],
  }),
  ("nof_tree_events",                 293996),
  ("nof_db_events",                   293996),
  ("fsize_local",                     1145574548), # 1.15GB, avg file size 381.86MB
  ("fsize_db",                        15888556444), # 15.89GB, avg file size 836.24MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 299993, ],
    'CountWeighted'                                                                  : [ 2.99934090e+05, 2.99941762e+05, 2.99955785e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11936160e+05, 2.99934090e+05, 2.87578500e+05, 3.11936160e+05, 2.99934090e+05, 2.87578500e+05, 3.11936160e+05, 2.99934090e+05, 2.87578500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11936160e+05, 2.87578500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.15922422e+05, 9.16411625e+05, 1.27894948e+06, 9.15090688e+05, 8.94332375e+05, 5.74579852e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00061473e+05, 3.00239266e+05, 4.25402773e+05, 2.99788805e+05, 2.99380859e+05, 1.88236875e+05, ],
  }),
  ("nof_tree_events",                 299993),
  ("nof_db_events",                   299993),
  ("fsize_local",                     1208572936), # 1.21GB, avg file size 604.29MB
  ("fsize_db",                        15974763144), # 15.97GB, avg file size 3.19GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 278994, ],
    'CountWeighted'                                                                  : [ 2.78925312e+05, 2.78926479e+05, 2.78936922e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.93031883e+05, 2.78922641e+05, 2.65260188e+05, 2.93031883e+05, 2.78922641e+05, 2.65260188e+05, 2.93031883e+05, 2.78922641e+05, 2.65260188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.93032873e+05, 2.65260100e+05, ],
    'CountWeightedPSWeight'                                                          : [ 6.03493422e+05, 6.03549902e+05, 8.54910469e+05, 6.03568414e+05, 5.99574816e+05, 3.76702441e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.78970137e+05, 2.78999912e+05, 3.97753215e+05, 2.79005754e+05, 2.79721957e+05, 1.74135664e+05, ],
  }),
  ("nof_tree_events",                 278994),
  ("nof_db_events",                   278994),
  ("fsize_local",                     1184909571), # 1.18GB, avg file size 592.45MB
  ("fsize_db",                        15658111382), # 15.66GB, avg file size 921.07MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 293997, ],
    'CountWeighted'                                                                  : [ 2.93965055e+05, 2.94010488e+05, 2.94022645e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11430219e+05, 2.93965055e+05, 2.77569312e+05, 3.11430219e+05, 2.93965055e+05, 2.77569312e+05, 3.11430219e+05, 2.93965055e+05, 2.77569312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11430219e+05, 2.77569312e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.15201551e+05, 4.15575773e+05, 5.89846656e+05, 4.15328996e+05, 4.12988480e+05, 2.58570277e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.93951371e+05, 2.94214766e+05, 4.18136648e+05, 2.94040453e+05, 2.92925812e+05, 1.83060850e+05, ],
  }),
  ("nof_tree_events",                 293997),
  ("nof_db_events",                   293997),
  ("fsize_local",                     1301871050), # 1.30GB, avg file size 650.94MB
  ("fsize_db",                        17725740224), # 17.73GB, avg file size 770.68MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99941324e+05, 2.99958465e+05, 2.99974012e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20084996e+05, 2.99941324e+05, 2.81456832e+05, 3.20084996e+05, 2.99941324e+05, 2.81456832e+05, 3.20084996e+05, 2.99941324e+05, 2.81456832e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20084996e+05, 2.81456832e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.22570820e+05, 4.22350148e+05, 6.01840141e+05, 4.22375922e+05, 4.21430555e+05, 2.62189555e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00042449e+05, 2.99885277e+05, 4.27985812e+05, 2.99903695e+05, 2.99890859e+05, 1.86166477e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1374558772), # 1.37GB, avg file size 687.28MB
  ("fsize_db",                        18359036586), # 18.36GB, avg file size 3.06GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 295998, ],
    'CountWeighted'                                                                  : [ 2.95947141e+05, 2.95996324e+05, 2.96002250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17817684e+05, 2.95947141e+05, 2.76173672e+05, 3.17817684e+05, 2.95947141e+05, 2.76173672e+05, 3.17817684e+05, 2.95947141e+05, 2.76173672e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17818590e+05, 2.76172766e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.40368250e+05, 8.40280070e+05, 1.18261903e+06, 8.40159078e+05, 8.21652234e+05, 5.20119875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.96032746e+05, 2.96011305e+05, 4.22086691e+05, 2.95960059e+05, 2.94923137e+05, 1.83221732e+05, ],
  }),
  ("nof_tree_events",                 295998),
  ("nof_db_events",                   295998),
  ("fsize_local",                     1396016305), # 1.40GB, avg file size 698.01MB
  ("fsize_db",                        16949359291), # 16.95GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99932766e+05, 1.99932969e+05, 1.99910125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15907312e+05, 1.99931156e+05, 1.85634516e+05, 2.15907312e+05, 1.99931156e+05, 1.85634516e+05, 2.15907312e+05, 1.99931156e+05, 1.85634516e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15907312e+05, 1.85634516e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.30638125e+05, 4.30404375e+05, 6.12195625e+05, 4.30728750e+05, 4.26685062e+05, 2.65798062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99958750e+05, 1.99851031e+05, 2.86081062e+05, 1.99999750e+05, 1.99943250e+05, 1.23418609e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     964972212), # 964.97MB, avg file size 964.97MB
  ("fsize_db",                        11943067602), # 11.94GB, avg file size 853.08MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 199995, ],
    'CountWeighted'                                                                  : [ 1.99922172e+05, 1.99930797e+05, 1.99893484e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.16963844e+05, 1.99922172e+05, 1.84762250e+05, 2.16963844e+05, 1.99922172e+05, 1.84762250e+05, 2.16963844e+05, 1.99922172e+05, 1.84762250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.16963844e+05, 1.84762250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 5.88199750e+05, 5.87623625e+05, 8.29203500e+05, 5.88237625e+05, 5.75056312e+05, 3.62147062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99944172e+05, 1.99758422e+05, 2.86112875e+05, 1.99958562e+05, 1.99713016e+05, 1.23103805e+05, ],
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     982978192), # 982.98MB, avg file size 982.98MB
  ("fsize_db",                        11686132211), # 11.69GB, avg file size 2.34GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 199995, ],
    'CountWeighted'                                                                  : [ 1.99954562e+05, 1.99955781e+05, 1.99960953e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18018047e+05, 1.99954562e+05, 1.84043766e+05, 2.18018047e+05, 1.99954562e+05, 1.84043766e+05, 2.18018047e+05, 1.99954562e+05, 1.84043766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18018047e+05, 1.84043766e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.01691438e+05, 3.02005812e+05, 4.32051719e+05, 3.01689375e+05, 3.00304375e+05, 1.85027375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99988438e+05, 2.00196844e+05, 2.86991750e+05, 1.99983688e+05, 1.99663250e+05, 1.22655328e+05, ],
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     999546626), # 999.55MB, avg file size 999.55MB
  ("fsize_db",                        12840929781), # 12.84GB, avg file size 3.21GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 196000, ],
    'CountWeighted'                                                                  : [ 1.95955719e+05, 1.95938375e+05, 1.95945484e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.95955719e+05, 1.95955719e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.04158906e+05, 3.04242781e+05, 4.35728719e+05, 3.04423625e+05, 3.02640062e+05, 1.86196500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.95906016e+05, 1.95957500e+05, 2.81288781e+05, 1.96078297e+05, 1.95572359e+05, 1.19930219e+05, ],
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     997966569), # 997.97MB, avg file size 997.97MB
  ("fsize_db",                        12970290914), # 12.97GB, avg file size 864.69MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2v2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99930180e+05, 1.99939352e+05, 1.99932836e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99930180e+05, 1.99930180e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.20556727e+05, 3.20700945e+05, 4.59212203e+05, 3.20648227e+05, 3.18495977e+05, 1.95914711e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99942406e+05, 2.00031281e+05, 2.87218117e+05, 1.99996344e+05, 1.99452781e+05, 1.22201617e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1032526327), # 1.03GB, avg file size 344.18MB
  ("fsize_db",                        13346223144), # 13.35GB, avg file size 741.46MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 193998, ],
    'CountWeighted'                                                                  : [ 1.93927031e+05, 1.93939094e+05, 1.93927500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.93927031e+05, 1.93927031e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.21847906e+05, 3.21487375e+05, 4.61132250e+05, 3.21979000e+05, 3.20049156e+05, 1.96466703e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.93921812e+05, 1.93707234e+05, 2.78673219e+05, 1.94005734e+05, 1.93666969e+05, 1.18379562e+05, ],
  }),
  ("nof_tree_events",                 193998),
  ("nof_db_events",                   193998),
  ("fsize_local",                     1007320483), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        13004188270), # 13.00GB, avg file size 1.63GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99968109e+05, 1.99935203e+05, 1.99950500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.21311625e+05, 1.99968109e+05, 1.81621047e+05, 2.21311625e+05, 1.99968109e+05, 1.81621047e+05, 2.21311625e+05, 1.99968109e+05, 1.81621047e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21307688e+05, 1.81622734e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.44271469e+05, 3.44536562e+05, 4.94023500e+05, 3.44731438e+05, 3.41998062e+05, 2.09715625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99878594e+05, 2.00033094e+05, 2.87821438e+05, 2.00146797e+05, 1.99560531e+05, 1.21759773e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1040034177), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        13219528779), # 13.22GB, avg file size 2.20GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99883516e+04, 9.99769688e+04, 9.99728750e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11344047e+05, 9.99883516e+04, 9.03308906e+04, 1.11344047e+05, 9.99883516e+04, 9.03308906e+04, 1.11344047e+05, 9.99883516e+04, 9.03308906e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11344047e+05, 9.03308906e+04, ],
    'CountWeightedPSWeight'                                                          : [ 1.86725609e+05, 1.86550656e+05, 2.68227688e+05, 1.86502969e+05, 1.85662219e+05, 1.13327203e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00048609e+05, 9.99540781e+04, 1.44363781e+05, 9.99262891e+04, 1.00124398e+05, 6.07203711e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     528210132), # 528.21MB, avg file size 528.21MB
  ("fsize_db",                        6685081658), # 6.69GB, avg file size 1.67GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 96999, ],
    'CountWeighted'                                                                  : [ 9.69516719e+04, 9.69660625e+04, 9.69536406e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.69516719e+04, 9.69516719e+04, ],
    'CountWeightedPSWeight'                                                          : [ 3.38319188e+05, 3.37963281e+05, 4.76864000e+05, 3.38293812e+05, 3.25955188e+05, 2.04099656e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.69758906e+04, 9.69343047e+04, 1.40344641e+05, 9.69780312e+04, 9.70258594e+04, 5.85068906e+04, ],
  }),
  ("nof_tree_events",                 96999),
  ("nof_db_events",                   96999),
  ("fsize_local",                     523571794), # 523.57MB, avg file size 523.57MB
  ("fsize_db",                        6424419348), # 6.42GB, avg file size 713.82MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_1250_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99466016e+04, 9.99407188e+04, 9.99500469e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13883695e+05, 9.99418750e+04, 8.85087656e+04, 1.13883695e+05, 9.99418750e+04, 8.85087656e+04, 1.13883695e+05, 9.99418750e+04, 8.85087656e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13884062e+05, 8.85084062e+04, ],
    'CountWeightedPSWeight'                                                          : [ 4.49403875e+05, 4.48113125e+05, 6.21193625e+05, 4.49613125e+05, 4.19336562e+05, 2.69495438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99611406e+04, 9.99715000e+04, 1.45111344e+05, 1.00011141e+05, 9.99157812e+04, 5.99442109e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     533323284), # 533.32MB, avg file size 533.32MB
  ("fsize_db",                        6512314789), # 6.51GB, avg file size 1.30GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_1500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99136406e+04, 9.99122969e+04, 9.99170156e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99136406e+04, 9.99136406e+04, ],
    'CountWeightedPSWeight'                                                          : [ 3.96020625e+05, 3.95526438e+05, 5.53940125e+05, 3.95047562e+05, 3.74352219e+05, 2.36447375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00092500e+05, 1.00107344e+05, 1.44838344e+05, 9.98493359e+04, 9.93102188e+04, 5.97593047e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     533995999), # 534.00MB, avg file size 534.00MB
  ("fsize_db",                        7078717091), # 7.08GB, avg file size 505.62MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_1750_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99107500e+04, 9.99147188e+04, 9.99256250e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15679914e+05, 9.99107500e+04, 8.71990312e+04, 1.15679914e+05, 9.99107500e+04, 8.71990312e+04, 1.15679914e+05, 9.99107500e+04, 8.71990312e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15679984e+05, 8.71989531e+04, ],
    'CountWeightedPSWeight'                                                          : [ 5.26274375e+05, 5.22109875e+05, 7.13801125e+05, 5.26193250e+05, 4.77324125e+05, 3.13247250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00000570e+05, 1.00044766e+05, 1.45857500e+05, 9.99876719e+04, 1.00089859e+05, 5.95252070e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     530414115), # 530.41MB, avg file size 530.41MB
  ("fsize_db",                        6969030499), # 6.97GB, avg file size 1.74GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_2000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 99997, ],
    'CountWeighted'                                                                  : [ 9.98848750e+04, 9.98716016e+04, 9.98738047e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98848750e+04, 9.98848750e+04, ],
    'CountWeightedPSWeight'                                                          : [ 4.81235000e+05, 4.78696062e+05, 6.61419062e+05, 4.81306688e+05, 4.43150281e+05, 2.85725938e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99826875e+04, 9.98961562e+04, 1.45496391e+05, 1.00001477e+05, 9.97129062e+04, 5.93688828e+04, ],
  }),
  ("nof_tree_events",                 99997),
  ("nof_db_events",                   99997),
  ("fsize_local",                     531697268), # 531.70MB, avg file size 531.70MB
  ("fsize_db",                        8227083083), # 8.23GB, avg file size 1.65GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_2500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToRadionToHHTo2V2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.97929688e+04, 9.97965625e+04, 9.98025547e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.97929688e+04, 9.97929688e+04, ],
    'CountWeightedPSWeight'                                                          : [ 8.92425000e+05, 8.09040125e+05, 9.91319250e+05, 8.84281500e+05, 6.99882500e+05, 5.41782375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.98852188e+04, 9.98956562e+04, 1.45666625e+05, 1.00129656e+05, 9.96981875e+04, 5.92357969e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     533300092), # 533.30MB, avg file size 533.30MB
  ("fsize_db",                        8326148543), # 8.33GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin0_3000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_250_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_250_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 383996, ],
    'CountWeighted'                                                                  : [ 3.83906531e+05, 3.83933641e+05, 3.83912828e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.83906531e+05, 3.83906531e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.83939688e+06, 3.83939688e+06, 3.83939688e+06, 3.83939688e+06, 3.83939688e+06, 3.83939688e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.83965250e+05, 3.84004594e+05, 5.79626375e+05, 3.84001094e+05, 3.82808984e+05, 2.10783531e+05, ],
  }),
  ("nof_tree_events",                 383996),
  ("nof_db_events",                   383996),
  ("fsize_local",                     2025893521), # 2.03GB, avg file size 1.01GB
  ("fsize_db",                        24278727790), # 24.28GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_250_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_260_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_260_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 389991, ],
    'CountWeighted'                                                                  : [ 3.89853594e+05, 3.89874516e+05, 3.89895438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.89853594e+05, 3.89853594e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.89848300e+06, 3.89848300e+06, 3.89848300e+06, 3.89848300e+06, 3.89848300e+06, 3.89848300e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.89909219e+05, 3.90024438e+05, 5.88715031e+05, 3.89897766e+05, 3.88211141e+05, 2.13580172e+05, ],
  }),
  ("nof_tree_events",                 389991),
  ("nof_db_events",                   389991),
  ("fsize_local",                     2086728960), # 2.09GB, avg file size 1.04GB
  ("fsize_db",                        26571434322), # 26.57GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_260_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_270_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_270_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.99912938e+05, 3.99905000e+05, 3.99901062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99912938e+05, 3.99912938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99869550e+06, 3.99869550e+06, 3.99869550e+06, 3.99869550e+06, 3.99869550e+06, 3.99869550e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99858672e+05, 3.99712969e+05, 6.04283844e+05, 4.00128812e+05, 3.98379875e+05, 2.18730062e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     2171028094), # 2.17GB, avg file size 1.09GB
  ("fsize_db",                        27386438209), # 27.39GB, avg file size 2.74GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_270_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_280_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_280_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99958922e+05, 3.99982047e+05, 3.99889297e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99958922e+05, 3.99958922e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99947888e+06, 3.99948438e+06, 3.99948438e+06, 3.99947888e+06, 3.99948438e+06, 3.99947888e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00116500e+05, 3.99771000e+05, 6.05003891e+05, 3.99830844e+05, 3.98526266e+05, 2.18212359e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     2197092250), # 2.20GB, avg file size 1.10GB
  ("fsize_db",                        27556511297), # 27.56GB, avg file size 2.51GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_280_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_300_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_300_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    30),
  ("nof_events",                      {
    'Count'                                                                          : [ 293996, ],
    'CountWeighted'                                                                  : [ 2.93953156e+05, 2.93951780e+05, 2.93942589e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.93953156e+05, 2.93953156e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.93938709e+06, 2.93939884e+06, 2.93939884e+06, 2.93938709e+06, 2.93939884e+06, 2.93938709e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.93976391e+05, 2.94143008e+05, 4.45829377e+05, 2.94020659e+05, 2.92732559e+05, 1.59562579e+05, ],
  }),
  ("nof_tree_events",                 293996),
  ("nof_db_events",                   293996),
  ("fsize_local",                     1656638230), # 1.66GB, avg file size 414.16MB
  ("fsize_db",                        20555029971), # 20.56GB, avg file size 685.17MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_300_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_320_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_320_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99926570e+05, 2.99922039e+05, 2.99919824e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.89973727e+05, 3.58801746e+05, 3.31326961e+05, 3.26033297e+05, 2.99926570e+05, 2.76913852e+05, 2.76814316e+05, 2.54608484e+05, 2.35048844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.89973758e+05, 2.35048844e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99934406e+06, 2.99934406e+06, 2.99934406e+06, 2.99934406e+06, 2.99934406e+06, 2.99934406e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99943852e+05, 3.00135051e+05, 4.55201188e+05, 2.99978203e+05, 2.98341023e+05, 1.62195393e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1701676342), # 1.70GB, avg file size 850.84MB
  ("fsize_db",                        20860701519), # 20.86GB, avg file size 2.61GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_320_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_350_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_350_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 3.00038227e+05, 2.99987824e+05, 3.00025289e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.00038227e+05, 3.00038227e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.00053612e+06, 3.00055062e+06, 3.00055062e+06, 3.00053612e+06, 3.00055062e+06, 3.00053612e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00110922e+05, 3.00548621e+05, 4.56491766e+05, 3.00076578e+05, 2.97945770e+05, 1.61297992e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1772100574), # 1.77GB, avg file size 886.05MB
  ("fsize_db",                        21462869404), # 21.46GB, avg file size 3.58GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_350_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_400_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_400_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 299992, ],
    'CountWeighted'                                                                  : [ 2.99929176e+05, 2.99933281e+05, 2.99916148e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99929176e+05, 2.99929176e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99918797e+06, 2.99918797e+06, 2.99918797e+06, 2.99918797e+06, 2.99918797e+06, 2.99918797e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00023168e+05, 2.99622543e+05, 4.58529438e+05, 2.99893391e+05, 2.99385047e+05, 1.59886395e+05, ],
  }),
  ("nof_tree_events",                 299992),
  ("nof_db_events",                   299992),
  ("fsize_local",                     1839563618), # 1.84GB, avg file size 919.78MB
  ("fsize_db",                        21940279980), # 21.94GB, avg file size 2.44GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_400_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_450_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_450_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 299993, ],
    'CountWeighted'                                                                  : [ 2.99917422e+05, 2.99952289e+05, 2.99897848e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99917422e+05, 2.99917422e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99935925e+06, 2.99935925e+06, 2.99935925e+06, 2.99935925e+06, 2.99935925e+06, 2.99935925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00007773e+05, 2.99947344e+05, 4.58561320e+05, 2.99915855e+05, 2.97709605e+05, 1.58771215e+05, ],
  }),
  ("nof_tree_events",                 299993),
  ("nof_db_events",                   299993),
  ("fsize_local",                     1894715683), # 1.89GB, avg file size 947.36MB
  ("fsize_db",                        22350188940), # 22.35GB, avg file size 3.19GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_450_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_500_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_500_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 299992, ],
    'CountWeighted'                                                                  : [ 2.99897191e+05, 2.99882043e+05, 2.99897527e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99897191e+05, 2.99897191e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99878919e+06, 2.99879697e+06, 2.99879697e+06, 2.99878844e+06, 2.99879697e+06, 2.99878844e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99964906e+05, 3.00052598e+05, 4.61124016e+05, 3.00011414e+05, 2.98729277e+05, 1.57614594e+05, ],
  }),
  ("nof_tree_events",                 299992),
  ("nof_db_events",                   299992),
  ("fsize_local",                     1942856061), # 1.94GB, avg file size 971.43MB
  ("fsize_db",                        21732849779), # 21.73GB, avg file size 3.10GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_550_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_550_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 299994, ],
    'CountWeighted'                                                                  : [ 2.99884922e+05, 2.99922168e+05, 2.99909832e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.99884922e+05, 2.99884922e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99913103e+06, 2.99914153e+06, 2.99914153e+06, 2.99913178e+06, 2.99914153e+06, 2.99913103e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99829109e+05, 2.99667363e+05, 4.61527188e+05, 3.00140582e+05, 2.98497016e+05, 1.56824309e+05, ],
  }),
  ("nof_tree_events",                 299994),
  ("nof_db_events",                   299994),
  ("fsize_local",                     1984932715), # 1.98GB, avg file size 992.47MB
  ("fsize_db",                        22027024008), # 22.03GB, avg file size 2.75GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_550_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_600_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_600_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 199993, ],
    'CountWeighted'                                                                  : [ 1.99927359e+05, 1.99943359e+05, 1.99917156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99927359e+05, 1.99927359e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99924238e+06, 1.99925338e+06, 1.99925338e+06, 1.99924238e+06, 1.99925338e+06, 1.99924238e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99891938e+05, 1.99977750e+05, 3.09144875e+05, 2.00087906e+05, 1.99587906e+05, 1.03857289e+05, ],
  }),
  ("nof_tree_events",                 199993),
  ("nof_db_events",                   199993),
  ("fsize_local",                     1344733197), # 1.34GB, avg file size 1.34GB
  ("fsize_db",                        15551759262), # 15.55GB, avg file size 2.59GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_600_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_650_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_650_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99986047e+05, 1.99965844e+05, 1.99992750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99986047e+05, 1.99986047e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99977075e+06, 1.99977075e+06, 1.99977075e+06, 1.99977075e+06, 1.99977075e+06, 1.99977075e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00027328e+05, 2.00189234e+05, 3.08952625e+05, 2.00077094e+05, 1.98629031e+05, 1.03571188e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1365424330), # 1.37GB, avg file size 1.37GB
  ("fsize_db",                        13853892609), # 13.85GB, avg file size 1.54GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_650_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_700_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_700_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99915188e+05, 1.99899594e+05, 1.99911859e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99915188e+05, 1.99915188e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99919900e+06, 1.99920975e+06, 1.99920975e+06, 1.99919900e+06, 1.99920975e+06, 1.99919900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00028016e+05, 2.00039844e+05, 3.09769469e+05, 1.99913438e+05, 1.99086469e+05, 1.02951547e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1382540578), # 1.38GB, avg file size 1.38GB
  ("fsize_db",                        14045165712), # 14.05GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_700_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_750_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_750_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99885672e+05, 1.99898172e+05, 1.99881203e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99885672e+05, 1.99885672e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99883112e+06, 1.99883112e+06, 1.99883112e+06, 1.99883112e+06, 1.99883112e+06, 1.99883112e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99961375e+05, 2.00381219e+05, 3.09964188e+05, 2.00013344e+05, 1.98347719e+05, 1.02606336e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1397055427), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        14174590935), # 14.17GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_750_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_800_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_800_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 191996, ],
    'CountWeighted'                                                                  : [ 1.91918812e+05, 1.91908641e+05, 1.91920484e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91918812e+05, 1.91918812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.91906838e+06, 1.91906838e+06, 1.91906838e+06, 1.91906838e+06, 1.91906838e+06, 1.91906838e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.92082156e+05, 1.92029312e+05, 2.98527000e+05, 1.91852641e+05, 1.91254188e+05, 9.80654922e+04, ],
  }),
  ("nof_tree_events",                 191996),
  ("nof_db_events",                   191996),
  ("fsize_local",                     1353570972), # 1.35GB, avg file size 1.35GB
  ("fsize_db",                        13643630164), # 13.64GB, avg file size 1.24GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_800_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_850_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_850_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 199993, ],
    'CountWeighted'                                                                  : [ 2.00026156e+05, 1.99957266e+05, 2.00104641e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.00026156e+05, 2.00026156e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99996900e+06, 1.99996900e+06, 1.99996900e+06, 1.99996900e+06, 1.99996900e+06, 1.99996900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00176953e+05, 2.00322609e+05, 3.10973750e+05, 2.00070953e+05, 1.98504125e+05, 1.01892688e+05, ],
  }),
  ("nof_tree_events",                 199993),
  ("nof_db_events",                   199993),
  ("fsize_local",                     1421046826), # 1.42GB, avg file size 1.42GB
  ("fsize_db",                        14301131301), # 14.30GB, avg file size 1.30GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_850_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_900_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_900_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99867789e+05, 1.99857836e+05, 1.99853539e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99867789e+05, 1.99867789e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99856181e+06, 1.99856181e+06, 1.99856181e+06, 1.99856181e+06, 1.99856181e+06, 1.99856181e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00053102e+05, 1.99668844e+05, 3.10283859e+05, 1.99934492e+05, 1.98216695e+05, 1.01811773e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1431255226), # 1.43GB, avg file size 715.63MB
  ("fsize_db",                        14436186956), # 14.44GB, avg file size 1.11GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_900_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1000_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_1000_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99139297e+04, 9.99210000e+04, 9.99101016e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99139297e+04, 9.99139297e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99117062e+05, 9.99117062e+05, 9.99117062e+05, 9.99117062e+05, 9.99117062e+05, 9.99117062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00015656e+05, 9.99157656e+04, 1.55601750e+05, 9.99401719e+04, 9.91438438e+04, 5.06068398e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     723195055), # 723.20MB, avg file size 723.20MB
  ("fsize_db",                        7357026530), # 7.36GB, avg file size 817.45MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_1000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1250_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_1250_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 99997, ],
    'CountWeighted'                                                                  : [ 9.98889609e+04, 9.99063281e+04, 9.98976406e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98889609e+04, 9.98889609e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99007625e+05, 9.99007625e+05, 9.99007625e+05, 9.99007625e+05, 9.99007625e+05, 9.99007625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00019203e+05, 9.97667500e+04, 1.56234906e+05, 9.99438984e+04, 9.92517891e+04, 5.00673672e+04, ],
  }),
  ("nof_tree_events",                 99997),
  ("nof_db_events",                   99997),
  ("fsize_local",                     733527541), # 733.53MB, avg file size 733.53MB
  ("fsize_db",                        7500010088), # 7.50GB, avg file size 937.50MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_1250_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1500_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_1500_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.98113984e+04, 9.98245547e+04, 9.98368906e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98113984e+04, 9.98113984e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.98203062e+05, 9.98215250e+05, 9.98215250e+05, 9.98203312e+05, 9.98215250e+05, 9.98203062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99274766e+04, 9.96833047e+04, 1.56938203e+05, 1.00039055e+05, 9.94361328e+04, 4.96257656e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     738115268), # 738.12MB, avg file size 738.12MB
  ("fsize_db",                        7713759404), # 7.71GB, avg file size 593.37MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_1500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_1750_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_1750_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 98998, ],
    'CountWeighted'                                                                  : [ 9.87571094e+04, 9.87660898e+04, 9.87522930e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.87571094e+04, 9.87571094e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.87597719e+05, 9.87597719e+05, 9.87597719e+05, 9.87597719e+05, 9.87597719e+05, 9.87597719e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.89600820e+04, 9.91678516e+04, 1.55772133e+05, 9.90423633e+04, 9.79143711e+04, 4.87014297e+04, ],
  }),
  ("nof_tree_events",                 98998),
  ("nof_db_events",                   98998),
  ("fsize_local",                     732610561), # 732.61MB, avg file size 366.31MB
  ("fsize_db",                        7662155139), # 7.66GB, avg file size 696.56MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_1750_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_2000_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_2000_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.96503750e+04, 9.96506016e+04, 9.96543203e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.96503750e+04, 9.96503750e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.96504812e+05, 9.96513812e+05, 9.96513812e+05, 9.96504438e+05, 9.96513812e+05, 9.96504438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99783125e+04, 1.00281047e+05, 1.57953828e+05, 9.99771797e+04, 9.91391172e+04, 4.88432812e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     738187644), # 738.19MB, avg file size 738.19MB
  ("fsize_db",                        7724622965), # 7.72GB, avg file size 965.58MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_2000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToRadionToHHTo2V2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin0_3000_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin0_3000_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 99996, ],
    'CountWeighted'                                                                  : [ 9.87934531e+04, 9.88020938e+04, 9.87905859e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.87934531e+04, 9.87934531e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.87904438e+05, 9.87904438e+05, 9.87904438e+05, 9.87904438e+05, 9.87904438e+05, 9.87904438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00000148e+05, 1.00202344e+05, 1.58097219e+05, 9.99143516e+04, 9.90531406e+04, 4.86877266e+04, ],
  }),
  ("nof_tree_events",                 99996),
  ("nof_db_events",                   99996),
  ("fsize_local",                     738524679), # 738.52MB, avg file size 738.52MB
  ("fsize_db",                        7943067646), # 7.94GB, avg file size 794.31MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin0_3000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 391996, ],
    'CountWeighted'                                                                  : [ 3.91977031e+05, 3.91937875e+05, 3.91946453e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.96769469e+05, 3.91974625e+05, 3.84377766e+05, 3.96769469e+05, 3.91974625e+05, 3.84377766e+05, 3.96769469e+05, 3.91974625e+05, 3.84377766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96769469e+05, 3.84377766e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.91922725e+06, 3.91922725e+06, 3.91922725e+06, 3.91922725e+06, 3.91922725e+06, 3.91922725e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.92125438e+05, 3.92124312e+05, 5.53354531e+05, 3.91770109e+05, 3.90900516e+05, 2.47809750e+05, ],
  }),
  ("nof_tree_events",                 391996),
  ("nof_db_events",                   391996),
  ("fsize_local",                     1404243336), # 1.40GB, avg file size 702.12MB
  ("fsize_db",                        20055994832), # 20.06GB, avg file size 1.11GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399991, ],
    'CountWeighted'                                                                  : [ 3.99953406e+05, 3.99919359e+05, 3.99922359e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06199984e+05, 3.99952250e+05, 3.91133359e+05, 4.06199984e+05, 3.99952250e+05, 3.91133359e+05, 4.06199984e+05, 3.99952250e+05, 3.91133359e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06199984e+05, 3.91133359e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99980400e+06, 3.99980400e+06, 3.99980400e+06, 3.99980400e+06, 3.99980400e+06, 3.99980400e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99829203e+05, 4.00304078e+05, 5.65784484e+05, 4.00121500e+05, 3.99264766e+05, 2.52494070e+05, ],
  }),
  ("nof_tree_events",                 399991),
  ("nof_db_events",                   399991),
  ("fsize_local",                     1458747911), # 1.46GB, avg file size 729.37MB
  ("fsize_db",                        20560214076), # 20.56GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 397996, ],
    'CountWeighted'                                                                  : [ 3.98009391e+05, 3.97950359e+05, 3.98018938e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.05479391e+05, 3.98009391e+05, 3.88180047e+05, 4.05479391e+05, 3.98009391e+05, 3.88180047e+05, 4.05479391e+05, 3.98009391e+05, 3.88180047e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.05479391e+05, 3.88180047e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97976288e+06, 3.97976288e+06, 3.97976288e+06, 3.97976288e+06, 3.97976288e+06, 3.97976288e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.97982562e+05, 3.97958469e+05, 5.62450984e+05, 3.97980281e+05, 3.97069438e+05, 2.51103039e+05, ],
  }),
  ("nof_tree_events",                 397996),
  ("nof_db_events",                   397996),
  ("fsize_local",                     1477464838), # 1.48GB, avg file size 738.73MB
  ("fsize_db",                        22172374707), # 22.17GB, avg file size 2.22GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399992, ],
    'CountWeighted'                                                                  : [ 3.99955641e+05, 3.99954453e+05, 3.99940547e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.08722359e+05, 3.99952625e+05, 3.89167453e+05, 4.08722359e+05, 3.99952625e+05, 3.89167453e+05, 4.08722359e+05, 3.99952625e+05, 3.89167453e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.08722438e+05, 3.89167359e+05, ],
    'CountWeightedPSWeight'                                                          : [ 4.00017038e+06, 4.00018075e+06, 4.00018075e+06, 4.00017038e+06, 4.00018075e+06, 4.00017038e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00001078e+05, 4.00372672e+05, 5.66645688e+05, 3.99947812e+05, 3.99338719e+05, 2.51744031e+05, ],
  }),
  ("nof_tree_events",                 399992),
  ("nof_db_events",                   399992),
  ("fsize_local",                     1511306211), # 1.51GB, avg file size 755.65MB
  ("fsize_db",                        20820001722), # 20.82GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 297998, ],
    'CountWeighted'                                                                  : [ 2.97980609e+05, 2.97959973e+05, 2.97979516e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.06200086e+05, 2.97980609e+05, 2.88592172e+05, 3.06200086e+05, 2.97980609e+05, 2.88592172e+05, 3.06200086e+05, 2.97980609e+05, 2.88592172e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.06200086e+05, 2.88592172e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.98000262e+06, 2.97999162e+06, 2.97999162e+06, 2.98000262e+06, 2.97999162e+06, 2.98000262e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98021949e+05, 2.97973512e+05, 4.22181188e+05, 2.97962250e+05, 2.97634785e+05, 1.87415188e+05, ],
  }),
  ("nof_tree_events",                 297998),
  ("nof_db_events",                   297998),
  ("fsize_local",                     1163726958), # 1.16GB, avg file size 581.86MB
  ("fsize_db",                        17126493878), # 17.13GB, avg file size 856.32MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 299995, ],
    'CountWeighted'                                                                  : [ 2.99972484e+05, 2.99981879e+05, 2.99971668e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09798859e+05, 2.99972484e+05, 2.89279633e+05, 3.09798859e+05, 2.99972484e+05, 2.89279633e+05, 3.09798859e+05, 2.99972484e+05, 2.89279633e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09798859e+05, 2.89279633e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99957259e+06, 2.99957259e+06, 2.99957259e+06, 2.99957259e+06, 2.99957259e+06, 2.99957259e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99993879e+05, 3.00248492e+05, 4.24943195e+05, 2.99969098e+05, 2.98861000e+05, 1.88344180e+05, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1206507724), # 1.21GB, avg file size 603.25MB
  ("fsize_db",                        16154095425), # 16.15GB, avg file size 2.69GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 295998, ],
    'CountWeighted'                                                                  : [ 2.95947805e+05, 2.95962480e+05, 2.95967949e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.07787363e+05, 2.95947805e+05, 2.83782934e+05, 3.07787363e+05, 2.95947805e+05, 2.83782934e+05, 3.07787363e+05, 2.95947805e+05, 2.83782934e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.07787363e+05, 2.83782934e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.95966288e+06, 2.95967388e+06, 2.95967388e+06, 2.95966288e+06, 2.95967388e+06, 2.95966288e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.96134117e+05, 2.96014652e+05, 4.20678102e+05, 2.95796395e+05, 2.95863582e+05, 1.85190887e+05, ],
  }),
  ("nof_tree_events",                 295998),
  ("nof_db_events",                   295998),
  ("fsize_local",                     1237720073), # 1.24GB, avg file size 618.86MB
  ("fsize_db",                        16258445329), # 16.26GB, avg file size 1.81GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 297995, ],
    'CountWeighted'                                                                  : [ 2.97965082e+05, 2.97947738e+05, 2.97938031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.12995336e+05, 2.97965082e+05, 2.83338641e+05, 3.12995336e+05, 2.97965082e+05, 2.83338641e+05, 3.12995336e+05, 2.97965082e+05, 2.83338641e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.12995336e+05, 2.83338641e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.97950272e+06, 2.97950272e+06, 2.97950272e+06, 2.97950272e+06, 2.97950272e+06, 2.97950272e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.98028625e+05, 2.98165035e+05, 4.24403086e+05, 2.97885293e+05, 2.97878707e+05, 1.85662051e+05, ],
  }),
  ("nof_tree_events",                 297995),
  ("nof_db_events",                   297995),
  ("fsize_local",                     1315720077), # 1.32GB, avg file size 657.86MB
  ("fsize_db",                        17915945878), # 17.92GB, avg file size 942.94MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 284994, ],
    'CountWeighted'                                                                  : [ 2.84960660e+05, 2.84954480e+05, 2.84987832e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.01911422e+05, 2.84958125e+05, 2.69077094e+05, 3.01911422e+05, 2.84958125e+05, 2.69077094e+05, 3.01911422e+05, 2.84958125e+05, 2.69077094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.01911422e+05, 2.69077094e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.85007638e+06, 2.85008462e+06, 2.85008462e+06, 2.85007638e+06, 2.85008462e+06, 2.85007638e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.84951121e+05, 2.84953027e+05, 4.05986637e+05, 2.85051492e+05, 2.84433852e+05, 1.77118797e+05, ],
  }),
  ("nof_tree_events",                 284994),
  ("nof_db_events",                   284994),
  ("fsize_local",                     1314738576), # 1.31GB, avg file size 657.37MB
  ("fsize_db",                        16848799352), # 16.85GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2v2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99951875e+05, 2.99970197e+05, 2.99962201e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20061346e+05, 2.99951875e+05, 2.81466164e+05, 3.20061346e+05, 2.99951875e+05, 2.81466164e+05, 3.20061346e+05, 2.99951875e+05, 2.81466164e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20061346e+05, 2.81466164e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99971231e+06, 2.99971231e+06, 2.99971231e+06, 2.99971231e+06, 2.99971231e+06, 2.99971231e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99947381e+05, 2.99760281e+05, 4.28710137e+05, 3.00015820e+05, 3.00201717e+05, 1.85705208e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1434783574), # 1.43GB, avg file size 478.26MB
  ("fsize_db",                        17493740155), # 17.49GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99955016e+05, 2.99972410e+05, 2.99957430e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22076020e+05, 2.99955016e+05, 2.79868023e+05, 3.22076020e+05, 2.99955016e+05, 2.79868023e+05, 3.22076020e+05, 2.99955016e+05, 2.79868023e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22076020e+05, 2.79868023e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.99973797e+06, 2.99973797e+06, 2.99973797e+06, 2.99973797e+06, 2.99973797e+06, 2.99973797e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00106004e+05, 3.00035004e+05, 4.29136156e+05, 2.99827984e+05, 2.99751988e+05, 1.85160359e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1474945780), # 1.47GB, avg file size 737.47MB
  ("fsize_db",                        17710981794), # 17.71GB, avg file size 885.55MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99977562e+05, 1.99965312e+05, 1.99971453e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15934125e+05, 1.99977562e+05, 1.85668688e+05, 2.15934125e+05, 1.99977562e+05, 1.85668688e+05, 2.15934125e+05, 1.99977562e+05, 1.85668688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15934875e+05, 1.85667922e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99966262e+06, 1.99967812e+06, 1.99967812e+06, 1.99966612e+06, 1.99967812e+06, 1.99966262e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00000812e+05, 1.99983875e+05, 2.85660750e+05, 1.99942969e+05, 1.99139594e+05, 1.23221164e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1003710955), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        11919833002), # 11.92GB, avg file size 744.99MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99934203e+05, 1.99962219e+05, 1.99973094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17039672e+05, 1.99933688e+05, 1.84804281e+05, 2.17039672e+05, 1.99933688e+05, 1.84804281e+05, 2.17039672e+05, 1.99933688e+05, 1.84804281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17039672e+05, 1.84804281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99959275e+06, 1.99959275e+06, 1.99959275e+06, 1.99959275e+06, 1.99959275e+06, 1.99959275e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00087625e+05, 1.99886844e+05, 2.86774031e+05, 1.99837781e+05, 1.99968406e+05, 1.22901039e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1019597560), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        11994685720), # 11.99GB, avg file size 1.33GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99967922e+05, 1.99997938e+05, 1.99996484e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18053562e+05, 1.99967484e+05, 1.84066281e+05, 2.18053562e+05, 1.99967484e+05, 1.84066281e+05, 2.18053562e+05, 1.99967484e+05, 1.84066281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18053719e+05, 1.84066156e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99951238e+06, 1.99951238e+06, 1.99951238e+06, 1.99951238e+06, 1.99951238e+06, 1.99951238e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99921672e+05, 2.00184953e+05, 2.86624031e+05, 2.00064125e+05, 1.99027672e+05, 1.22463477e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1033995184), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        12072988172), # 12.07GB, avg file size 2.01GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2v2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 197997, ],
    'CountWeighted'                                                                  : [ 1.97956692e+05, 1.97961749e+05, 1.97947249e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.16748092e+05, 1.97956692e+05, 1.81534261e+05, 2.16748092e+05, 1.97956692e+05, 1.81534261e+05, 2.16748092e+05, 1.97956692e+05, 1.81534261e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.16748092e+05, 1.81534261e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.97953722e+06, 1.97953722e+06, 1.97953722e+06, 1.97953722e+06, 1.97953722e+06, 1.97953722e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.97953145e+05, 1.97883290e+05, 2.84660810e+05, 1.98013842e+05, 1.98018060e+05, 1.21092731e+05, ],
  }),
  ("nof_tree_events",                 197997),
  ("nof_db_events",                   197997),
  ("fsize_local",                     1037344699), # 1.04GB, avg file size 345.78MB
  ("fsize_db",                        13158550685), # 13.16GB, avg file size 657.93MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 199995, ],
    'CountWeighted'                                                                  : [ 1.99937875e+05, 1.99959609e+05, 1.99929188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19730453e+05, 1.99936375e+05, 1.82728938e+05, 2.19730453e+05, 1.99936375e+05, 1.82728938e+05, 2.19730453e+05, 1.99936375e+05, 1.82728938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.19732953e+05, 1.82726438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99915200e+06, 1.99915275e+06, 1.99915275e+06, 1.99915200e+06, 1.99915275e+06, 1.99915200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99891594e+05, 2.00256188e+05, 2.87329406e+05, 2.00073297e+05, 1.99063812e+05, 1.21958344e+05, ],
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     1054191419), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        12213814696), # 12.21GB, avg file size 939.52MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99930875e+05, 1.99937500e+05, 1.99922219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99930875e+05, 1.99930875e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.99928850e+06, 1.99928850e+06, 1.99928850e+06, 1.99928850e+06, 1.99928850e+06, 1.99928850e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99914812e+05, 1.99837719e+05, 2.87616469e+05, 2.00009250e+05, 1.99639984e+05, 1.21808156e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1068135756), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        12732436951), # 12.73GB, avg file size 748.97MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 195995, ],
    'CountWeighted'                                                                  : [ 1.95957531e+05, 1.95920922e+05, 1.95922359e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.95957531e+05, 1.95957531e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.95935550e+06, 1.95936650e+06, 1.95936650e+06, 1.95935550e+06, 1.95936650e+06, 1.95935550e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.96006719e+05, 1.95874672e+05, 2.82527781e+05, 1.95967625e+05, 1.95986094e+05, 1.19135930e+05, ],
  }),
  ("nof_tree_events",                 195995),
  ("nof_db_events",                   195995),
  ("fsize_local",                     1051908909), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        13482710118), # 13.48GB, avg file size 749.04MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99700781e+04, 9.99751875e+04, 9.99688281e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11332289e+05, 9.99700781e+04, 9.03242656e+04, 1.11332289e+05, 9.99700781e+04, 9.03242656e+04, 1.11332289e+05, 9.99700781e+04, 9.03242656e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11332312e+05, 9.03242578e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99800312e+05, 9.99800312e+05, 9.99800312e+05, 9.99800312e+05, 9.99800312e+05, 9.99800312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00028125e+05, 1.00007039e+05, 1.44671047e+05, 9.99153438e+04, 1.00150031e+05, 6.05316484e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     539008130), # 539.01MB, avg file size 539.01MB
  ("fsize_db",                        6814333152), # 6.81GB, avg file size 851.79MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99732344e+04, 9.99667266e+04, 9.99586250e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99732344e+04, 9.99732344e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99660250e+05, 9.99660250e+05, 9.99660250e+05, 9.99660250e+05, 9.99660250e+05, 9.99660250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99787656e+04, 1.00032859e+05, 1.44717797e+05, 9.99700000e+04, 9.98093750e+04, 6.02125078e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     544730735), # 544.73MB, avg file size 544.73MB
  ("fsize_db",                        6700622854), # 6.70GB, avg file size 957.23MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_1250_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99285000e+04, 9.99409844e+04, 9.99302969e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99285000e+04, 9.99285000e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99234312e+05, 9.99234312e+05, 9.99234312e+05, 9.99234312e+05, 9.99234312e+05, 9.99234312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99827266e+04, 1.00073414e+05, 1.45112312e+05, 9.99565000e+04, 9.97134688e+04, 5.98383281e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     534390386), # 534.39MB, avg file size 534.39MB
  ("fsize_db",                        6724912073), # 6.72GB, avg file size 1.68GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_1500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99343750e+04, 9.99385312e+04, 9.99201328e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99343750e+04, 9.99343750e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99379938e+05, 9.99379938e+05, 9.99379938e+05, 9.99379938e+05, 9.99379938e+05, 9.99379938e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99488750e+04, 9.97628516e+04, 1.45395031e+05, 1.00003125e+05, 1.00192945e+05, 5.97486406e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     529065361), # 529.07MB, avg file size 529.07MB
  ("fsize_db",                        6757238050), # 6.76GB, avg file size 1.69GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_1750_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99024609e+04, 9.98992031e+04, 9.98932500e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15647562e+05, 9.99024609e+04, 8.71867422e+04, 1.15647562e+05, 9.99024609e+04, 8.71867422e+04, 1.15647562e+05, 9.99024609e+04, 8.71867422e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15649422e+05, 8.71848906e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.98974188e+05, 9.98974188e+05, 9.98974188e+05, 9.98974188e+05, 9.98974188e+05, 9.98974188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99476328e+04, 1.00074812e+05, 1.45182469e+05, 1.00053062e+05, 9.93188672e+04, 5.94460156e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     524071253), # 524.07MB, avg file size 524.07MB
  ("fsize_db",                        7030476859), # 7.03GB, avg file size 1.76GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_2000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 99996, ],
    'CountWeighted'                                                                  : [ 9.98571875e+04, 9.98535625e+04, 9.98411562e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17149578e+05, 9.98571875e+04, 8.60884062e+04, 1.17149578e+05, 9.98571875e+04, 8.60884062e+04, 1.17149578e+05, 9.98571875e+04, 8.60884062e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.17152719e+05, 8.60852812e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.98447125e+05, 9.98447125e+05, 9.98447125e+05, 9.98447125e+05, 9.98447125e+05, 9.98447125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99686250e+04, 9.99389844e+04, 1.45778000e+05, 1.00014203e+05, 9.98101094e+04, 5.93125078e+04, ],
  }),
  ("nof_tree_events",                 99996),
  ("nof_db_events",                   99996),
  ("fsize_local",                     522921498), # 522.92MB, avg file size 522.92MB
  ("fsize_db",                        7124837516), # 7.12GB, avg file size 1.78GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_2500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToBulkGravitonToHHTo2V2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 99997, ],
    'CountWeighted'                                                                  : [ 9.97810938e+04, 9.97774375e+04, 9.97742031e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.18478453e+05, 9.97805000e+04, 8.51036562e+04, 1.18478453e+05, 9.97805000e+04, 8.51036562e+04, 1.18478453e+05, 9.97805000e+04, 8.51036562e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.18485125e+05, 8.50971094e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.97806062e+05, 9.97806062e+05, 9.97806062e+05, 9.97806062e+05, 9.97806062e+05, 9.97806062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99929844e+04, 9.99577734e+04, 1.45886938e+05, 9.99216562e+04, 9.98499844e+04, 5.92564531e+04, ],
  }),
  ("nof_tree_events",                 99997),
  ("nof_db_events",                   99997),
  ("fsize_local",                     524216199), # 524.22MB, avg file size 524.22MB
  ("fsize_db",                        6801982100), # 6.80GB, avg file size 453.47MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_spin2_3000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_250_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_250_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 3.94246859e+05, 3.94253906e+05, 3.94274531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.33392250e+05, 3.95621906e+05, 3.64233234e+05, 4.31855281e+05, 3.94243641e+05, 3.62988672e+05, 4.30655312e+05, 3.93169188e+05, 3.62018375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.35148094e+05, 3.60319453e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94273212e+06, 3.94273212e+06, 3.94273212e+06, 3.94273212e+06, 3.94273212e+06, 3.94273212e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99933859e+05, 4.00096984e+05, 5.71630688e+05, 3.99843172e+05, 3.99359312e+05, 2.43898336e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     2178472058), # 2.18GB, avg file size 1.09GB
  ("fsize_db",                        24054774128), # 24.05GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_250_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_260_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_260_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399988, ],
    'CountWeighted'                                                                  : [ 3.96256016e+05, 3.96257250e+05, 3.96265109e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.25567109e+05, 3.97569922e+05, 3.73136875e+05, 4.24126406e+05, 3.96255469e+05, 3.71931016e+05, 4.23012047e+05, 3.95238594e+05, 3.70999328e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.29857047e+05, 3.66796516e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96221925e+06, 3.96222575e+06, 3.96222575e+06, 3.96221900e+06, 3.96222575e+06, 3.96221900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99912484e+05, 3.99789656e+05, 5.63587656e+05, 3.99936797e+05, 3.99889062e+05, 2.51189906e+05, ],
  }),
  ("nof_tree_events",                 399988),
  ("nof_db_events",                   399988),
  ("fsize_local",                     1970717026), # 1.97GB, avg file size 985.36MB
  ("fsize_db",                        22637330314), # 22.64GB, avg file size 1.33GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_260_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_270_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_270_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.96409938e+05, 3.96311938e+05, 3.96385391e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.26148000e+05, 3.97690156e+05, 3.72868031e+05, 4.24742906e+05, 3.96409938e+05, 3.71694141e+05, 4.23655344e+05, 3.95418344e+05, 3.70786781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.30279938e+05, 3.66745984e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96419875e+06, 3.96420725e+06, 3.96420725e+06, 3.96419850e+06, 3.96420725e+06, 3.96419825e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99872078e+05, 3.99930281e+05, 5.63593234e+05, 4.00024109e+05, 3.99957406e+05, 2.51286844e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1972929429), # 1.97GB, avg file size 986.46MB
  ("fsize_db",                        22515385410), # 22.52GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_270_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_280_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_280_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 387993, ],
    'CountWeighted'                                                                  : [ 3.84137578e+05, 3.84130000e+05, 3.84139812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.13150266e+05, 3.85315672e+05, 3.61125781e+05, 4.11848328e+05, 3.84131656e+05, 3.60042984e+05, 4.10839359e+05, 3.83214734e+05, 3.59204773e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.17024750e+05, 3.55415906e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.84122575e+06, 3.84123688e+06, 3.84123688e+06, 3.84122550e+06, 3.84123688e+06, 3.84122500e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.87927281e+05, 3.87846000e+05, 5.45768828e+05, 3.87959016e+05, 3.87563453e+05, 2.44222609e+05, ],
  }),
  ("nof_tree_events",                 387993),
  ("nof_db_events",                   387993),
  ("fsize_local",                     1915440346), # 1.92GB, avg file size 957.72MB
  ("fsize_db",                        21745034723), # 21.75GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_280_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_300_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_300_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.97240793e+05, 2.97220258e+05, 2.97239688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20203531e+05, 2.98108051e+05, 2.78906137e+05, 3.19248500e+05, 2.97240793e+05, 2.78114133e+05, 3.18507574e+05, 2.96568070e+05, 2.77500332e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22945148e+05, 2.74833125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.97241388e+06, 2.97240534e+06, 2.97240534e+06, 2.97241559e+06, 2.97240534e+06, 2.97241388e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99976215e+05, 2.99702586e+05, 4.21153172e+05, 2.99874824e+05, 2.99442250e+05, 1.89182932e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1484715102), # 1.48GB, avg file size 742.36MB
  ("fsize_db",                        16963251239), # 16.96GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_300_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_320_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_320_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 299992, ],
    'CountWeighted'                                                                  : [ 2.97242191e+05, 2.97247113e+05, 2.97218445e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20745121e+05, 2.98051504e+05, 2.78415918e+05, 3.19851309e+05, 2.97242191e+05, 2.77678598e+05, 3.19157066e+05, 2.96613652e+05, 2.77106629e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.23296125e+05, 2.74630613e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.97234297e+06, 2.97236772e+06, 2.97236772e+06, 2.97234272e+06, 2.97236772e+06, 2.97234272e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99929594e+05, 3.00203051e+05, 4.20947758e+05, 2.99968809e+05, 2.98807922e+05, 1.89257514e+05, ],
  }),
  ("nof_tree_events",                 299992),
  ("nof_db_events",                   299992),
  ("fsize_local",                     1486437750), # 1.49GB, avg file size 743.22MB
  ("fsize_db",                        16652379052), # 16.65GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_320_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_350_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_350_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 284992, ],
    'CountWeighted'                                                                  : [ 2.82327934e+05, 2.82347207e+05, 2.82313363e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.05440129e+05, 2.83020094e+05, 2.63729863e+05, 3.04674895e+05, 2.82327934e+05, 2.63100172e+05, 3.04080090e+05, 2.81790633e+05, 2.62611156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.07598098e+05, 2.60526314e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.82353044e+06, 2.82353044e+06, 2.82353044e+06, 2.82353044e+06, 2.82353044e+06, 2.82353044e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.84853023e+05, 2.84699770e+05, 4.00657695e+05, 2.85077051e+05, 2.85433953e+05, 1.80071436e+05, ],
  }),
  ("nof_tree_events",                 284992),
  ("nof_db_events",                   284992),
  ("fsize_local",                     1418014054), # 1.42GB, avg file size 709.01MB
  ("fsize_db",                        15762362705), # 15.76GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_350_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_400_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_400_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 296996, ],
    'CountWeighted'                                                                  : [ 2.94092562e+05, 2.94100500e+05, 2.94094031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.19758062e+05, 2.94702250e+05, 2.73326141e+05, 3.19077938e+05, 2.94090766e+05, 2.72772906e+05, 3.18547562e+05, 2.93614234e+05, 2.72341844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.21603344e+05, 2.70579047e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.94088288e+06, 2.94088738e+06, 2.94088738e+06, 2.94088288e+06, 2.94088738e+06, 2.94088288e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.97045125e+05, 2.97225172e+05, 4.16264328e+05, 2.96858531e+05, 2.96360625e+05, 1.88101883e+05, ],
  }),
  ("nof_tree_events",                 296996),
  ("nof_db_events",                   296996),
  ("fsize_local",                     1486227288), # 1.49GB, avg file size 743.11MB
  ("fsize_db",                        16521281646), # 16.52GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_400_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_450_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_450_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.96886871e+05, 2.96956047e+05, 2.96861879e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.24708211e+05, 2.97419949e+05, 2.74434250e+05, 3.24112641e+05, 2.96886871e+05, 2.73954113e+05, 3.23647168e+05, 2.96470836e+05, 2.73579062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.26215129e+05, 2.72150652e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.96906375e+06, 2.96906375e+06, 2.96906375e+06, 2.96906375e+06, 2.96906375e+06, 2.96906375e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.00013855e+05, 3.00447852e+05, 4.20004461e+05, 2.99911926e+05, 2.99040719e+05, 1.90270699e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1512393567), # 1.51GB, avg file size 756.20MB
  ("fsize_db",                        16625335022), # 16.63GB, avg file size 977.96MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_450_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_500_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_500_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 2.96821691e+05, 2.96848645e+05, 2.96848051e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.26335914e+05, 2.97227836e+05, 2.72917512e+05, 3.25880668e+05, 2.96821691e+05, 2.72552355e+05, 3.25524301e+05, 2.96503844e+05, 2.72266816e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.27636379e+05, 2.71043922e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.96816103e+06, 2.96815650e+06, 2.96815650e+06, 2.96815603e+06, 2.96815650e+06, 2.96815603e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99998113e+05, 3.00118309e+05, 4.19286117e+05, 2.99871988e+05, 2.99168484e+05, 1.90733588e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1523885417), # 1.52GB, avg file size 761.94MB
  ("fsize_db",                        16847345601), # 16.85GB, avg file size 842.37MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_550_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_550_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 299993, ],
    'CountWeighted'                                                                  : [ 2.96395621e+05, 2.96425711e+05, 2.96357750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.96395621e+05, 2.96395621e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.96405347e+06, 2.96407997e+06, 2.96407997e+06, 2.96405297e+06, 2.96407997e+06, 2.96405297e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.99984453e+05, 2.99918410e+05, 4.18995266e+05, 2.99790020e+05, 2.99454012e+05, 1.91010396e+05, ],
  }),
  ("nof_tree_events",                 299993),
  ("nof_db_events",                   299993),
  ("fsize_local",                     1545753830), # 1.55GB, avg file size 772.88MB
  ("fsize_db",                        17390260115), # 17.39GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_550_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_600_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_600_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.97584969e+05, 1.97581547e+05, 1.97597656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19523078e+05, 1.97787328e+05, 1.79933578e+05, 2.19294625e+05, 1.97584969e+05, 1.79753031e+05, 2.19115078e+05, 1.97426125e+05, 1.79611172e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.20167969e+05, 1.79029297e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.97589525e+06, 1.97588350e+06, 1.97588350e+06, 1.97589525e+06, 1.97588350e+06, 1.97589525e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99990125e+05, 2.00037719e+05, 2.79417719e+05, 1.99880172e+05, 1.99664734e+05, 1.27395281e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1029977765), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        11461789019), # 11.46GB, avg file size 818.70MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_600_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_650_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_650_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.97558734e+05, 1.97546203e+05, 1.97559266e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.20595406e+05, 1.97718609e+05, 1.79074297e+05, 2.20414500e+05, 1.97558734e+05, 1.78931969e+05, 2.20271969e+05, 1.97432891e+05, 1.78819859e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21173688e+05, 1.78299578e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.97553812e+06, 1.97552238e+06, 1.97552238e+06, 1.97553775e+06, 1.97552238e+06, 1.97553775e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99999500e+05, 2.00107594e+05, 2.79153406e+05, 1.99937188e+05, 1.99535641e+05, 1.27595859e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1035468851), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11185859826), # 11.19GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_650_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_700_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_700_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 199996, ],
    'CountWeighted'                                                                  : [ 1.97355375e+05, 1.97358891e+05, 1.97387344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.21421219e+05, 1.97490125e+05, 1.78139469e+05, 2.21267734e+05, 1.97355109e+05, 1.78019688e+05, 2.21146641e+05, 1.97248734e+05, 1.77925266e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21950891e+05, 1.77455656e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.97351700e+06, 1.97351788e+06, 1.97351788e+06, 1.97351700e+06, 1.97351788e+06, 1.97351700e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.00007594e+05, 1.99770250e+05, 2.79340594e+05, 1.99879047e+05, 2.00294906e+05, 1.27657109e+05, ],
  }),
  ("nof_tree_events",                 199996),
  ("nof_db_events",                   199996),
  ("fsize_local",                     1040963064), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11512583657), # 11.51GB, avg file size 822.33MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_700_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_750_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_750_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 199994, ],
    'CountWeighted'                                                                  : [ 1.97099672e+05, 1.97129141e+05, 1.97085047e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.22292234e+05, 1.97231359e+05, 1.77112641e+05, 2.22142062e+05, 1.97099672e+05, 1.76996125e+05, 2.22023500e+05, 1.96995719e+05, 1.76904062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.22739328e+05, 1.76517141e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.97097512e+06, 1.97099850e+06, 1.97099850e+06, 1.97097550e+06, 1.97099850e+06, 1.97097500e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99894125e+05, 1.99896922e+05, 2.78684406e+05, 2.00038109e+05, 1.99509109e+05, 1.27760094e+05, ],
  }),
  ("nof_tree_events",                 199994),
  ("nof_db_events",                   199994),
  ("fsize_local",                     1046908360), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        11559274596), # 11.56GB, avg file size 825.66MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_750_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_800_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_800_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.96994078e+05, 1.96997938e+05, 1.96994375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.96994078e+05, 1.96994078e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.96994100e+06, 1.96994100e+06, 1.96994100e+06, 1.96994100e+06, 1.96994100e+06, 1.96994100e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99923688e+05, 1.99831641e+05, 2.78971750e+05, 1.99967656e+05, 1.99944688e+05, 1.27799141e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1059094733), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        11741664635), # 11.74GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_800_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_850_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_850_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.96785031e+05, 1.96761609e+05, 1.96752016e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.23968188e+05, 1.96877344e+05, 1.75390641e+05, 2.23862375e+05, 1.96785031e+05, 1.75309125e+05, 2.23778688e+05, 1.96711812e+05, 1.75244703e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.24309406e+05, 1.74966078e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.96745400e+06, 1.96745412e+06, 1.96745412e+06, 1.96745138e+06, 1.96745412e+06, 1.96745138e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99978500e+05, 2.00106109e+05, 2.78891344e+05, 1.99940953e+05, 1.99707109e+05, 1.27877773e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1054228051), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        11434850687), # 11.43GB, avg file size 816.78MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_850_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_900_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_900_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.96481844e+05, 1.96462312e+05, 1.96513438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.24630766e+05, 1.96567844e+05, 1.74470672e+05, 2.24531625e+05, 1.96481484e+05, 1.74394750e+05, 2.24453031e+05, 1.96413094e+05, 1.74334594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.24989188e+05, 1.74040094e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.96488088e+06, 1.96487812e+06, 1.96487812e+06, 1.96488012e+06, 1.96487812e+06, 1.96488025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.99998594e+05, 2.00091453e+05, 2.78731312e+05, 1.99831250e+05, 1.99658156e+05, 1.27891562e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1057469002), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        11404514844), # 11.40GB, avg file size 950.38MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_900_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1000_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_1000_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.80200938e+04, 9.80116562e+04, 9.80352812e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13021531e+05, 9.80577656e+04, 8.64087188e+04, 1.12977672e+05, 9.80196953e+04, 8.63753594e+04, 1.12942828e+05, 9.79894375e+04, 8.63488750e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13151883e+05, 8.62532500e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.80165250e+05, 9.80184250e+05, 9.80184250e+05, 9.80165000e+05, 9.80184250e+05, 9.80164500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99950781e+04, 9.99322500e+04, 1.38763656e+05, 9.99550625e+04, 9.95436875e+04, 6.41431602e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     530825694), # 530.83MB, avg file size 530.83MB
  ("fsize_db",                        5759188056), # 5.76GB, avg file size 719.90MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_1000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-1200_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1200_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_1200_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.77753516e+04, 9.77744531e+04, 9.77498750e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.14437789e+05, 9.78014453e+04, 8.50705625e+04, 1.14406297e+05, 9.77743594e+04, 8.50469844e+04, 1.14381234e+05, 9.77527734e+04, 8.50282422e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.14560688e+05, 8.49442188e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.77762000e+05, 9.77762000e+05, 9.77762000e+05, 9.77762000e+05, 9.77762000e+05, 9.77762000e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99738750e+04, 9.99403594e+04, 1.39251953e+05, 9.99552656e+04, 1.00113016e+05, 6.41784336e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     532877487), # 532.88MB, avg file size 532.88MB
  ("fsize_db",                        5800432824), # 5.80GB, avg file size 828.63MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_1200_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1250_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_1250_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.75930078e+04, 9.75978438e+04, 9.75712891e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.75930078e+04, 9.75930078e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.75870875e+05, 9.75873375e+05, 9.75873375e+05, 9.75870750e+05, 9.75873375e+05, 9.75870750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99719453e+04, 1.00070758e+05, 1.38639484e+05, 9.99284219e+04, 9.95297578e+04, 6.43334297e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     535945035), # 535.95MB, avg file size 535.95MB
  ("fsize_db",                        6064296650), # 6.06GB, avg file size 551.30MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_1250_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1500_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_1500_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.68053359e+04, 9.68235781e+04, 9.67847422e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.68053359e+04, 9.68053359e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.68012375e+05, 9.68012375e+05, 9.68012375e+05, 9.68012375e+05, 9.68012375e+05, 9.68012375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99052656e+04, 9.98930000e+04, 1.38813469e+05, 9.99907812e+04, 1.00025023e+05, 6.44062188e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     530549496), # 530.55MB, avg file size 530.55MB
  ("fsize_db",                        6002045697), # 6.00GB, avg file size 857.44MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_1500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_1750_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_1750_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 95997, ],
    'CountWeighted'                                                                  : [ 9.24688672e+04, 9.24770156e+04, 9.24789766e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.12472047e+05, 9.24785312e+04, 7.79125078e+04, 1.12460508e+05, 9.24687109e+04, 7.79040781e+04, 1.12451281e+05, 9.24608672e+04, 7.78973125e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.12515844e+05, 7.78893906e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.24835125e+05, 9.24835125e+05, 9.24835125e+05, 9.24835125e+05, 9.24835125e+05, 9.24835125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.59490938e+04, 9.59147500e+04, 1.32956203e+05, 9.58935312e+04, 9.60215625e+04, 6.20855000e+04, ],
  }),
  ("nof_tree_events",                 95997),
  ("nof_db_events",                   95997),
  ("fsize_local",                     502029353), # 502.03MB, avg file size 502.03MB
  ("fsize_db",                        5595401383), # 5.60GB, avg file size 699.43MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_1750_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_2000_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_2000_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.53136973e+04, 9.53010732e+04, 9.53295918e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17714559e+05, 9.53216738e+04, 7.92466768e+04, 1.17705102e+05, 9.53136973e+04, 7.92398682e+04, 1.17697502e+05, 9.53072891e+04, 7.92343945e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.17766314e+05, 7.92283896e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.53139281e+05, 9.53130781e+05, 9.53130781e+05, 9.53139344e+05, 9.53130781e+05, 9.53139344e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99052559e+04, 9.99684473e+04, 1.38242041e+05, 1.00010207e+05, 9.99239883e+04, 6.48555830e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     521025266), # 521.03MB, avg file size 260.51MB
  ("fsize_db",                        5933132461), # 5.93GB, avg file size 494.43MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_2000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_2500_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_2500_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 99997, ],
    'CountWeighted'                                                                  : [ 9.27171094e+04, 9.26894844e+04, 9.27399141e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.27171094e+04, 9.27171094e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.27199875e+05, 9.27199875e+05, 9.27199875e+05, 9.27199875e+05, 9.27199875e+05, 9.27199875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99246875e+04, 1.00052883e+05, 1.37766219e+05, 9.99313438e+04, 9.98744844e+04, 6.52774414e+04, ],
  }),
  ("nof_tree_events",                 99997),
  ("nof_db_events",                   99997),
  ("fsize_local",                     516310665), # 516.31MB, avg file size 516.31MB
  ("fsize_db",                        6048578056), # 6.05GB, avg file size 864.08MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_2500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFToBulkGravitonToHHTo2V2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_spin2_3000_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_spin2_3000_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 8.97024219e+04, 8.97261250e+04, 8.96838125e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 8.97024219e+04, 8.97024219e+04, ],
    'CountWeightedPSWeight'                                                          : [ 8.96982375e+05, 8.96982375e+05, 8.96982375e+05, 8.96982375e+05, 8.96982375e+05, 8.96982375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.98737656e+04, 1.00218805e+05, 1.36786734e+05, 9.99179375e+04, 9.93963906e+04, 6.57991484e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     509179165), # 509.18MB, avg file size 509.18MB
  ("fsize_db",                        6043078205), # 6.04GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_spin2_3000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFHHTo4T_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.96211328e+05, 3.96179500e+05, 3.96184891e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96211328e+05, 3.96211328e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96175325e+06, 3.96174525e+06, 3.96174525e+06, 3.96175300e+06, 3.96174525e+06, 3.96175325e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99847406e+05, 4.00052266e+05, 5.38201812e+05, 4.00038219e+05, 4.00249984e+05, 2.73774906e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1704614637), # 1.70GB, avg file size 852.31MB
  ("fsize_db",                        22348961141), # 22.35GB, avg file size 3.19GB
  ("use_it",                          True),
  ("xsection",                        6.785e-06),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_1_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFHHTo4T_CV_1_C2V_1_C3_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 397000, ],
    'CountWeighted'                                                                  : [ 3.93158422e+05, 3.93171438e+05, 3.93167359e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.93158422e+05, 3.93158422e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.93159500e+06, 3.93157425e+06, 3.93157425e+06, 3.93159475e+06, 3.93157425e+06, 3.93159500e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96942938e+05, 3.96801734e+05, 5.37365531e+05, 3.96791812e+05, 3.96706016e+05, 2.68354961e+05, ],
  }),
  ("nof_tree_events",                 397000),
  ("nof_db_events",                   397000),
  ("fsize_local",                     1805302270), # 1.81GB, avg file size 902.65MB
  ("fsize_db",                        23455713216), # 23.46GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        5.5932e-06),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_2_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFHHTo4T_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.92797141e+05, 3.92719984e+05, 3.92819453e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.92797141e+05, 3.92797141e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.92776675e+06, 3.92777425e+06, 3.92777425e+06, 3.92776700e+06, 3.92777425e+06, 3.92776675e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99898469e+05, 4.00083719e+05, 5.39265562e+05, 4.00028047e+05, 3.99311625e+05, 2.72015656e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     2048793829), # 2.05GB, avg file size 1.02GB
  ("fsize_db",                        24644254146), # 24.64GB, avg file size 2.74GB
  ("use_it",                          True),
  ("xsection",                        5.5891e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_2_1_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFHHTo4T_CV_1_C2V_1_C3_0_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 396000, ],
    'CountWeighted'                                                                  : [ 3.92641969e+05, 3.92632734e+05, 3.92607250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.92641969e+05, 3.92641969e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.92646475e+06, 3.92647725e+06, 3.92647725e+06, 3.92646800e+06, 3.92647725e+06, 3.92646450e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95944047e+05, 3.95716312e+05, 5.32034078e+05, 3.95973922e+05, 3.96583859e+05, 2.71884156e+05, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1684303728), # 1.68GB, avg file size 842.15MB
  ("fsize_db",                        22116713711), # 22.12GB, avg file size 1.11GB
  ("use_it",                          True),
  ("xsection",                        1.81178e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_0_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFHHTo4T_CV_0_5_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.94069156e+05, 3.94050547e+05, 3.94027359e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.94069156e+05, 3.94069156e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94093638e+06, 3.94095788e+06, 3.94095788e+06, 3.94093588e+06, 3.94095788e+06, 3.94093588e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00002359e+05, 3.99835031e+05, 5.39405625e+05, 3.99810781e+05, 4.00280141e+05, 2.72447656e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1989520757), # 1.99GB, avg file size 994.76MB
  ("fsize_db",                        25461655211), # 25.46GB, avg file size 2.83GB
  ("use_it",                          True),
  ("xsection",                        4.25487e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFHHTo4T_CV_1_5_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_4t"),
  ("nof_files",                       3),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.94749887e+05, 3.94781975e+05, 3.94818254e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.94749887e+05, 3.94749887e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94788644e+06, 3.94790603e+06, 3.94790603e+06, 3.94788903e+06, 3.94790603e+06, 3.94788641e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99987416e+05, 3.99900697e+05, 5.38066102e+05, 3.99898586e+05, 4.00149104e+05, 2.73657967e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1859624550), # 1.86GB, avg file size 619.87MB
  ("fsize_db",                        23099322943), # 23.10GB, avg file size 1.36GB
  ("use_it",                          True),
  ("xsection",                        0.0002595228),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFHHTo2V2Tau_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.96110750e+05, 3.96124781e+05, 3.96139578e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96110750e+05, 3.96110750e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96116625e+06, 3.96116625e+06, 3.96116625e+06, 3.96116625e+06, 3.96116625e+06, 3.96116625e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99909469e+05, 3.99595094e+05, 5.53532594e+05, 3.99946953e+05, 4.00054359e+05, 2.59584711e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1762082938), # 1.76GB, avg file size 881.04MB
  ("fsize_db",                        23234072342), # 23.23GB, avg file size 2.58GB
  ("use_it",                          True),
  ("xsection",                        5.19e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_1_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFHHTo2V2Tau_CV_1_C2V_1_C3_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 395994, ],
    'CountWeighted'                                                                  : [ 3.92264094e+05, 3.92251938e+05, 3.92213875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.92264094e+05, 3.92264094e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.92278500e+06, 3.92277350e+06, 3.92277350e+06, 3.92278400e+06, 3.92277350e+06, 3.92278500e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96054516e+05, 3.96094844e+05, 5.52331594e+05, 3.95852719e+05, 3.95873406e+05, 2.53433453e+05, ],
  }),
  ("nof_tree_events",                 395994),
  ("nof_db_events",                   395994),
  ("fsize_local",                     1857078656), # 1.86GB, avg file size 928.54MB
  ("fsize_db",                        23202328259), # 23.20GB, avg file size 2.32GB
  ("use_it",                          True),
  ("xsection",                        4.27833e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_2_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFHHTo2V2Tau_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.92892875e+05, 3.92971625e+05, 3.92912031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.92892875e+05, 3.92892875e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.92954175e+06, 3.92954175e+06, 3.92954175e+06, 3.92954175e+06, 3.92954175e+06, 3.92954175e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99992484e+05, 3.99959719e+05, 5.56167797e+05, 3.99900344e+05, 4.00337297e+05, 2.57657016e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     2113258434), # 2.11GB, avg file size 1.06GB
  ("fsize_db",                        26711769527), # 26.71GB, avg file size 2.97GB
  ("use_it",                          True),
  ("xsection",                        0.0004275219),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_2_1_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFHHTo2V2Tau_CV_1_C2V_1_C3_0_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 399994, ],
    'CountWeighted'                                                                  : [ 3.96569016e+05, 3.96567625e+05, 3.96509750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96569016e+05, 3.96569016e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96469800e+06, 3.96470912e+06, 3.96470912e+06, 3.96470338e+06, 3.96470912e+06, 3.96469800e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99910750e+05, 3.99829219e+05, 5.53567328e+05, 3.99970344e+05, 4.00378109e+05, 2.60061328e+05, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     1759051684), # 1.76GB, avg file size 879.53MB
  ("fsize_db",                        23217249445), # 23.22GB, avg file size 1.93GB
  ("use_it",                          True),
  ("xsection",                        0.0001385868),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_0_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFHHTo2V2Tau_CV_0_5_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 399991, ],
    'CountWeighted'                                                                  : [ 3.93915109e+05, 3.93927797e+05, 3.93913219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.93915109e+05, 3.93915109e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.93906875e+06, 3.93909400e+06, 3.93909400e+06, 3.93906912e+06, 3.93909400e+06, 3.93906850e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99830000e+05, 4.00052828e+05, 5.54676828e+05, 3.99885703e+05, 3.99443750e+05, 2.58319836e+05, ],
  }),
  ("nof_tree_events",                 399991),
  ("nof_db_events",                   399991),
  ("fsize_local",                     2057500697), # 2.06GB, avg file size 1.03GB
  ("fsize_db",                        26237196263), # 26.24GB, avg file size 2.92GB
  ("use_it",                          True),
  ("xsection",                        0.0003254642),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/VBFHHTo2V2Tau_CV_1_5_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 399990, ],
    'CountWeighted'                                                                  : [ 3.94928453e+05, 3.94921656e+05, 3.94900266e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.94928453e+05, 3.94928453e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.94895450e+06, 3.94894400e+06, 3.94894400e+06, 3.94895450e+06, 3.94894400e+06, 3.94895450e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99952094e+05, 4.00122156e+05, 5.53985109e+05, 3.99898062e+05, 3.99505391e+05, 2.59114438e+05, ],
  }),
  ("nof_tree_events",                 399990),
  ("nof_db_events",                   399990),
  ("fsize_local",                     1926948973), # 1.93GB, avg file size 963.47MB
  ("fsize_db",                        23679254925), # 23.68GB, avg file size 2.96GB
  ("use_it",                          True),
  ("xsection",                        0.001985145),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4T_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99937422e+05, 3.99938469e+05, 3.99988281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.11999219e+05, 4.83245734e+05, 4.56267062e+05, 4.23860359e+05, 3.99934188e+05, 3.77562578e+05, 3.56961734e+05, 3.36773164e+05, 3.17860156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.11999266e+05, 3.17860016e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99954175e+06, 3.99954450e+06, 3.99954450e+06, 3.99954175e+06, 3.99954450e+06, 3.99954175e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99847750e+05, 4.00171844e+05, 5.55970297e+05, 4.00162938e+05, 3.99450609e+05, 2.60736266e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1711834420), # 1.71GB, avg file size 855.92MB
  ("fsize_db",                        22565271440), # 22.57GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4T_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 396000, ],
    'CountWeighted'                                                                  : [ 3.95919375e+05, 3.95933875e+05, 3.95891500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.14408500e+05, 4.74001031e+05, 4.38495141e+05, 4.29876234e+05, 3.95919375e+05, 3.66066047e+05, 3.64907578e+05, 3.35911031e+05, 3.10480602e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.14408562e+05, 3.10480586e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95881062e+06, 3.95881062e+06, 3.95881062e+06, 3.95881062e+06, 3.95881062e+06, 3.95881062e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95940172e+05, 3.95872844e+05, 5.54050859e+05, 3.96015031e+05, 3.95988906e+05, 2.55148156e+05, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1859552289), # 1.86GB, avg file size 929.78MB
  ("fsize_db",                        22812356401), # 22.81GB, avg file size 950.51MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4T_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99997984e+05, 3.99891672e+05, 3.99960672e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.11961797e+05, 4.83164438e+05, 4.56117750e+05, 4.23840250e+05, 3.99991375e+05, 3.77483109e+05, 3.56946047e+05, 3.36756500e+05, 3.17817336e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.11961797e+05, 3.17817320e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99890325e+06, 3.99890325e+06, 3.99890325e+06, 3.99890325e+06, 3.99890325e+06, 3.99890325e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00029469e+05, 3.99887031e+05, 5.56268406e+05, 3.99854844e+05, 4.00164375e+05, 2.60853109e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1714585470), # 1.71GB, avg file size 857.29MB
  ("fsize_db",                        22577919040), # 22.58GB, avg file size 2.82GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4T_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    28),
  ("nof_events",                      {
    'Count'                                                                          : [ 394000, ],
    'CountWeighted'                                                                  : [ 3.93946078e+05, 3.93924062e+05, 3.93936219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.02339406e+05, 4.77098406e+05, 4.52818344e+05, 4.14844016e+05, 3.93946078e+05, 3.73848375e+05, 3.48650734e+05, 3.31043961e+05, 3.14127820e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.02340688e+05, 3.14127820e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.93914175e+06, 3.93915612e+06, 3.93915612e+06, 3.93914175e+06, 3.93911325e+06, 3.93909900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.93993219e+05, 3.94109969e+05, 5.46733031e+05, 3.93926547e+05, 3.93575250e+05, 2.57643914e+05, ],
  }),
  ("nof_tree_events",                 394000),
  ("nof_db_events",                   394000),
  ("fsize_local",                     1644346965), # 1.64GB, avg file size 822.17MB
  ("fsize_db",                        23345042125), # 23.35GB, avg file size 833.75MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4T_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99961391e+05, 3.99920719e+05, 3.99957750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12943938e+05, 4.82628281e+05, 4.54475531e+05, 4.25153281e+05, 3.99952188e+05, 3.76531984e+05, 3.58407844e+05, 3.37081773e+05, 3.17305391e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12943938e+05, 3.17305594e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99965325e+06, 3.99965600e+06, 3.99965600e+06, 3.99965400e+06, 3.99965600e+06, 3.99965325e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00062625e+05, 4.00057953e+05, 5.56239406e+05, 3.99920516e+05, 3.99443297e+05, 2.60434633e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1731138454), # 1.73GB, avg file size 865.57MB
  ("fsize_db",                        22616576770), # 22.62GB, avg file size 2.26GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4T_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99980797e+05, 3.99961656e+05, 3.99893906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10234406e+05, 4.84202281e+05, 4.59238828e+05, 4.21487422e+05, 3.99975047e+05, 3.79279234e+05, 3.54315188e+05, 3.36165297e+05, 3.18776578e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10234500e+05, 3.18776734e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99976025e+06, 3.99976025e+06, 3.99976025e+06, 3.99976025e+06, 3.99976025e+06, 3.99976025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00010312e+05, 3.99944297e+05, 5.54598188e+05, 3.99895922e+05, 3.99367141e+05, 2.61691945e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1672471589), # 1.67GB, avg file size 836.24MB
  ("fsize_db",                        22434110190), # 22.43GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4T_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 397000, ],
    'CountWeighted'                                                                  : [ 3.96939219e+05, 3.96978109e+05, 3.96947266e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.06274688e+05, 4.80704406e+05, 4.56135109e+05, 4.18132312e+05, 3.96937250e+05, 3.76638438e+05, 3.51436516e+05, 3.33614266e+05, 3.16505031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.06275141e+05, 3.16504625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96940112e+06, 3.96940112e+06, 3.96940112e+06, 3.96940112e+06, 3.96934900e+06, 3.96934900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.97011938e+05, 3.97192672e+05, 5.50584406e+05, 3.96953625e+05, 3.96369375e+05, 2.59722305e+05, ],
  }),
  ("nof_tree_events",                 397000),
  ("nof_db_events",                   397000),
  ("fsize_local",                     1656639834), # 1.66GB, avg file size 828.32MB
  ("fsize_db",                        22349849698), # 22.35GB, avg file size 2.48GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4T_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 388000, ],
    'CountWeighted'                                                                  : [ 3.87913578e+05, 3.87928750e+05, 3.87909406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.94608812e+05, 4.69838344e+05, 4.45992328e+05, 4.08426531e+05, 3.87910328e+05, 3.68198078e+05, 3.43231219e+05, 3.25969031e+05, 3.09366641e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.94608812e+05, 3.09366641e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.44744688e+05, 8.45358500e+05, 1.16667488e+06, 8.45087469e+05, 8.38447594e+05, 5.52985906e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.87868125e+05, 3.88155531e+05, 5.38023797e+05, 3.88032266e+05, 3.87306719e+05, 2.53902961e+05, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     1616535288), # 1.62GB, avg file size 808.27MB
  ("fsize_db",                        21577784792), # 21.58GB, avg file size 899.07MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4T_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99880594e+05, 3.99891906e+05, 3.99907750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19392250e+05, 4.78823031e+05, 4.43000344e+05, 4.33913500e+05, 3.99880031e+05, 3.69901203e+05, 3.68203406e+05, 3.39269984e+05, 3.13748805e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19392500e+05, 3.13748867e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99895875e+06, 3.99895875e+06, 3.99895875e+06, 3.99895875e+06, 3.99895875e+06, 3.99895875e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00082359e+05, 4.00089000e+05, 5.59522859e+05, 3.99864359e+05, 3.99633906e+05, 2.57723594e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1882787773), # 1.88GB, avg file size 941.39MB
  ("fsize_db",                        23501535916), # 23.50GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4T_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 397000, ],
    'CountWeighted'                                                                  : [ 3.96945859e+05, 3.96930828e+05, 3.96952875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.06282781e+05, 4.80689031e+05, 4.56101047e+05, 4.18147703e+05, 3.96934969e+05, 3.76617703e+05, 3.51456930e+05, 3.33615359e+05, 3.16490953e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.06282781e+05, 3.16490953e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.89344075e+06, 3.62798450e+06, 3.96479962e+06, 3.85847888e+06, 3.26065975e+06, 2.89009825e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96867516e+05, 3.97293984e+05, 5.51035625e+05, 3.97135812e+05, 3.96508203e+05, 2.59512992e+05, ],
  }),
  ("nof_tree_events",                 397000),
  ("nof_db_events",                   397000),
  ("fsize_local",                     1658736826), # 1.66GB, avg file size 829.37MB
  ("fsize_db",                        22257366649), # 22.26GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4T_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                                          : [ 398000, ],
    'CountWeighted'                                                                  : [ 3.97932906e+05, 3.97934828e+05, 3.97935875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.07893609e+05, 4.81679250e+05, 4.56607516e+05, 4.19650484e+05, 3.97932906e+05, 3.77193484e+05, 3.52837297e+05, 3.34555141e+05, 3.17083078e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.07893609e+05, 3.17083078e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97951688e+06, 3.97951688e+06, 3.97951688e+06, 3.97951688e+06, 3.97951688e+06, 3.97951688e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.98092047e+05, 3.98217766e+05, 5.52679375e+05, 3.97824000e+05, 3.97746359e+05, 2.60139914e+05, ],
  }),
  ("nof_tree_events",                 398000),
  ("nof_db_events",                   398000),
  ("fsize_local",                     1668621039), # 1.67GB, avg file size 834.31MB
  ("fsize_db",                        23587120978), # 23.59GB, avg file size 907.20MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4T_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99981078e+05, 3.99942484e+05, 3.99965219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09922391e+05, 4.84409922e+05, 4.59845891e+05, 4.21062000e+05, 3.99979312e+05, 3.79626812e+05, 3.53842375e+05, 3.36065516e+05, 3.18962727e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09922391e+05, 3.18962727e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.88032938e+05, 8.87995188e+05, 1.22524038e+06, 8.88944062e+05, 8.81399062e+05, 5.81877688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99789266e+05, 3.99756266e+05, 5.53974250e+05, 4.00189609e+05, 3.99202469e+05, 2.61963492e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1665803232), # 1.67GB, avg file size 832.90MB
  ("fsize_db",                        22176978836), # 22.18GB, avg file size 2.77GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    29),
  ("nof_events",                      {
    'Count'                                                                          : [ 979100, ],
    'CountWeighted'                                                                  : [ 9.21271953e+05, 9.21215156e+05, 9.21090062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.06555089e+06, 1.04699806e+06, 1.03395817e+06, 9.42103000e+05, 9.21271891e+05, 9.04402500e+05, 8.35438422e+05, 8.13912688e+05, 7.95551656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.10339658e+06, 7.76986469e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.21274625e+05, 9.21229266e+05, 1.27021662e+06, 9.21102219e+05, 9.20586094e+05, 6.06667594e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 6.27460811e+04, 6.27462197e+04, 8.65466602e+04, 6.27405029e+04, 6.27392686e+04, 4.13286797e+04, ],
  }),
  ("nof_tree_events",                 979100),
  ("nof_db_events",                   979100),
  ("fsize_local",                     3874648971), # 3.87GB, avg file size 968.66MB
  ("fsize_db",                        46583707050), # 46.58GB, avg file size 1.61GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH0_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_4t"),
  ("nof_files",                       8),
  ("nof_db_files",                    56),
  ("nof_events",                      {
    'Count'                                                                          : [ 963000, ],
    'CountWeighted'                                                                  : [ 8.63579232e+05, 8.63624552e+05, 8.63522581e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.83480383e+05, 9.67728533e+05, 9.57328772e+05, 8.83510320e+05, 8.63537039e+05, 8.47909303e+05, 7.92824631e+05, 7.71162119e+05, 7.53010630e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.02540120e+06, 7.30352777e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.63613612e+05, 8.63599510e+05, 1.19233571e+06, 8.63523099e+05, 8.62878791e+05, 5.67316963e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.88192916e+04, 2.88186381e+04, 3.97907529e+04, 2.88153379e+04, 2.88169450e+04, 1.89495127e+04, ],
  }),
  ("nof_tree_events",                 963000),
  ("nof_db_events",                   963000),
  ("fsize_local",                     3919951598), # 3.92GB, avg file size 489.99MB
  ("fsize_db",                        46586377730), # 46.59GB, avg file size 831.90MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH1_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    33),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 8.62968969e+05, 8.62801672e+05, 8.63068344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.84292203e+05, 9.70635266e+05, 9.61920000e+05, 8.80611672e+05, 8.62957062e+05, 8.49140031e+05, 7.88155844e+05, 7.68726422e+05, 7.52383266e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03651197e+06, 7.20532984e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.63042016e+05, 8.63521172e+05, 1.19373578e+06, 8.62829094e+05, 8.61801422e+05, 5.64896406e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.31325801e+04, 1.31416882e+04, 1.81761177e+04, 1.31311782e+04, 1.31252925e+04, 8.59790942e+03, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4098976287), # 4.10GB, avg file size 1.02GB
  ("fsize_db",                        48200072580), # 48.20GB, avg file size 1.46GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    37),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.84279438e+05, 9.84263016e+05, 9.84334344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17908144e+06, 1.15698941e+06, 1.13999362e+06, 1.00380811e+06, 9.84224109e+05, 9.67769281e+05, 8.64291453e+05, 8.47023469e+05, 8.31396109e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.21492525e+06, 8.14662781e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.84194062e+05, 9.84286875e+05, 1.35605581e+06, 9.84479469e+05, 9.83649328e+05, 6.49155625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 8.02207266e+04, 8.02267383e+04, 1.10583080e+05, 8.02383457e+04, 8.02274277e+04, 5.29085645e+04, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     3757699427), # 3.76GB, avg file size 939.42MB
  ("fsize_db",                        46823526474), # 46.82GB, avg file size 1.27GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH5_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 393993, ],
    'CountWeighted'                                                                  : [ 3.93924453e+05, 3.93953656e+05, 3.93941812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.04268531e+05, 4.76010203e+05, 4.49485922e+05, 4.17438234e+05, 3.93924453e+05, 3.71932594e+05, 3.51537477e+05, 3.31699992e+05, 3.13107531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.04268531e+05, 3.13107531e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.93973725e+06, 3.93973725e+06, 3.93973725e+06, 3.93973725e+06, 3.93973725e+06, 3.93973725e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.93943141e+05, 3.94276250e+05, 5.61720297e+05, 3.94033328e+05, 3.93069844e+05, 2.44554766e+05, ],
  }),
  ("nof_tree_events",                 393993),
  ("nof_db_events",                   393993),
  ("fsize_local",                     1762168198), # 1.76GB, avg file size 881.08MB
  ("fsize_db",                        24027472831), # 24.03GB, avg file size 1.33GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 399994, ],
    'CountWeighted'                                                                  : [ 3.99878156e+05, 3.99872516e+05, 3.99889891e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19595719e+05, 4.78780672e+05, 4.42911875e+05, 4.34208156e+05, 3.99878156e+05, 3.69749562e+05, 3.68583469e+05, 3.39293094e+05, 3.13603914e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19597969e+05, 3.13603219e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99875275e+06, 3.99875275e+06, 3.99875275e+06, 3.99875275e+06, 3.99875275e+06, 3.99875275e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99934594e+05, 3.99882938e+05, 5.73533406e+05, 4.00029203e+05, 3.99612016e+05, 2.45592477e+05, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     1935793652), # 1.94GB, avg file size 967.90MB
  ("fsize_db",                        25778291187), # 25.78GB, avg file size 1.72GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 395996, ],
    'CountWeighted'                                                                  : [ 3.95951172e+05, 3.95998281e+05, 3.95921484e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.06883531e+05, 4.78348906e+05, 4.51555359e+05, 4.19640141e+05, 3.95951172e+05, 3.73711281e+05, 3.53410922e+05, 3.33406516e+05, 3.14643734e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.06883531e+05, 3.14643734e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95913425e+06, 3.95913425e+06, 3.95913425e+06, 3.95913425e+06, 3.95913425e+06, 3.95913425e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95860562e+05, 3.95951266e+05, 5.64715859e+05, 3.96133906e+05, 3.95511328e+05, 2.45797750e+05, ],
  }),
  ("nof_tree_events",                 395996),
  ("nof_db_events",                   395996),
  ("fsize_local",                     1780925490), # 1.78GB, avg file size 890.46MB
  ("fsize_db",                        24237765625), # 24.24GB, avg file size 969.51MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 3.99956609e+05, 3.99976000e+05, 3.99948625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10054750e+05, 4.84376281e+05, 4.59693109e+05, 4.21228781e+05, 3.99956609e+05, 3.79534875e+05, 3.54025719e+05, 3.36113086e+05, 3.18913297e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10054750e+05, 3.18913297e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99954425e+06, 3.99954525e+06, 3.99954525e+06, 3.99954425e+06, 3.99944012e+06, 3.99943925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00019828e+05, 4.00359344e+05, 5.69443812e+05, 3.99966750e+05, 3.98938266e+05, 2.49016828e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1748624484), # 1.75GB, avg file size 874.31MB
  ("fsize_db",                        24245036817), # 24.25GB, avg file size 1.28GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2v2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 397992, ],
    'CountWeighted'                                                                  : [ 3.97902641e+05, 3.97912758e+05, 3.97922281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10330141e+05, 4.80192047e+05, 4.52199203e+05, 4.22979695e+05, 3.97902641e+05, 3.74640430e+05, 3.56569742e+05, 3.35370992e+05, 3.15707781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10330625e+05, 3.15707328e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97931788e+06, 3.97934138e+06, 3.97934138e+06, 3.97931800e+06, 3.97934138e+06, 3.97931788e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.98032352e+05, 3.98312781e+05, 5.67845203e+05, 3.97833078e+05, 3.96959945e+05, 2.46658164e+05, ],
  }),
  ("nof_tree_events",                 397992),
  ("nof_db_events",                   397992),
  ("fsize_local",                     1805180238), # 1.81GB, avg file size 601.73MB
  ("fsize_db",                        24407491284), # 24.41GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_2v2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 393990, ],
    'CountWeighted'                                                                  : [ 3.93961570e+05, 3.93967219e+05, 3.93941008e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.02596125e+05, 4.76950781e+05, 4.52360320e+05, 4.15179297e+05, 3.93961570e+05, 3.73600172e+05, 3.49013664e+05, 3.31133125e+05, 3.14004000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.02596125e+05, 3.14003977e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.93957938e+06, 3.93957938e+06, 3.93957938e+06, 3.93957938e+06, 3.93957938e+06, 3.93957938e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.93952859e+05, 3.93961375e+05, 5.61419312e+05, 3.93975828e+05, 3.93794094e+05, 2.45142648e+05, ],
  }),
  ("nof_tree_events",                 393990),
  ("nof_db_events",                   393990),
  ("fsize_local",                     1731545748), # 1.73GB, avg file size 577.18MB
  ("fsize_db",                        23907169624), # 23.91GB, avg file size 956.29MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 395994, ],
    'CountWeighted'                                                                  : [ 3.95937141e+05, 3.95941438e+05, 3.95991250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.04982859e+05, 4.79468781e+05, 4.54951156e+05, 4.17065734e+05, 3.95937141e+05, 3.75661297e+05, 3.50540477e+05, 3.32756281e+05, 3.15682352e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.04982859e+05, 3.15682352e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95963662e+06, 3.95964738e+06, 3.95964738e+06, 3.95963662e+06, 3.95942662e+06, 3.95941588e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95969438e+05, 3.95712594e+05, 5.63975438e+05, 3.95977688e+05, 3.95890922e+05, 2.46577703e+05, ],
  }),
  ("nof_tree_events",                 395994),
  ("nof_db_events",                   395994),
  ("fsize_local",                     1734076022), # 1.73GB, avg file size 867.04MB
  ("fsize_db",                        24013488664), # 24.01GB, avg file size 1.14GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 3.99937812e+05, 3.99959656e+05, 3.99950391e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09927109e+05, 4.84390219e+05, 4.59805094e+05, 4.21077156e+05, 3.99936234e+05, 3.79603203e+05, 3.53861312e+05, 3.36064961e+05, 3.18949398e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09927109e+05, 3.18949352e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.70739094e+05, 8.70245406e+05, 1.23300181e+06, 8.71303031e+05, 8.63554250e+05, 5.42516703e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99865453e+05, 3.99645906e+05, 5.69894375e+05, 4.00126688e+05, 4.00223078e+05, 2.49135320e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1748774616), # 1.75GB, avg file size 874.39MB
  ("fsize_db",                        22774541667), # 22.77GB, avg file size 1.42GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 399993, ],
    'CountWeighted'                                                                  : [ 3.99888203e+05, 3.99884359e+05, 3.99940766e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19339797e+05, 4.78836016e+05, 4.43057344e+05, 4.33850844e+05, 3.99888203e+05, 3.69929531e+05, 3.68134953e+05, 3.39249867e+05, 3.13760438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19339797e+05, 3.13760406e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99931600e+06, 3.99931600e+06, 3.99931600e+06, 3.99931600e+06, 3.99931600e+06, 3.99931600e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99960750e+05, 3.99502125e+05, 5.73669891e+05, 3.99945000e+05, 4.00302703e+05, 2.45703891e+05, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     1960028095), # 1.96GB, avg file size 980.01MB
  ("fsize_db",                        25563876624), # 25.56GB, avg file size 2.84GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.99933750e+05, 3.99937375e+05, 3.99939016e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10070047e+05, 4.84286469e+05, 4.59520219e+05, 4.21270844e+05, 3.99933750e+05, 3.79436875e+05, 3.54078297e+05, 3.36104984e+05, 3.18855812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10070047e+05, 3.18855812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.97862625e+06, 2.85694375e+06, 3.66346525e+06, 2.96616362e+06, 2.52741162e+06, 1.85464800e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00047344e+05, 3.99793547e+05, 5.69260594e+05, 3.99864719e+05, 3.99477641e+05, 2.49057656e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1751549091), # 1.75GB, avg file size 875.77MB
  ("fsize_db",                        23894007583), # 23.89GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 399991, ],
    'CountWeighted'                                                                  : [ 3.99919750e+05, 3.99947141e+05, 3.99937297e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10422391e+05, 4.84095922e+05, 4.58915000e+05, 4.21736156e+05, 3.99916422e+05, 3.79097516e+05, 3.54590219e+05, 3.36230453e+05, 3.18681711e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10422391e+05, 3.18681633e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99933400e+06, 3.99933400e+06, 3.99933400e+06, 3.99933400e+06, 3.99933400e+06, 3.99933400e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99981906e+05, 3.99786500e+05, 5.70192047e+05, 3.99949844e+05, 4.00188078e+05, 2.48851227e+05, ],
  }),
  ("nof_tree_events",                 399991),
  ("nof_db_events",                   399991),
  ("fsize_local",                     1760537754), # 1.76GB, avg file size 880.27MB
  ("fsize_db",                        22984187913), # 22.98GB, avg file size 2.87GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    27),
  ("nof_events",                      {
    'Count'                                                                          : [ 399994, ],
    'CountWeighted'                                                                  : [ 3.99922219e+05, 3.99963922e+05, 3.99965891e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09911562e+05, 4.84389016e+05, 4.59817906e+05, 4.21055016e+05, 3.99922219e+05, 3.79605922e+05, 3.53838078e+05, 3.36053719e+05, 3.18947234e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09912375e+05, 3.18946531e+05, ],
    'CountWeightedPSWeight'                                                          : [ 5.93424406e+05, 5.93694688e+05, 8.43131781e+05, 5.93203188e+05, 5.90407281e+05, 3.69322531e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00035656e+05, 4.00217156e+05, 5.69356359e+05, 3.99883719e+05, 3.98994766e+05, 2.48966562e+05, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     1747195951), # 1.75GB, avg file size 873.60MB
  ("fsize_db",                        23989311263), # 23.99GB, avg file size 888.49MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_2v2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 399991, ],
    'CountWeighted'                                                                  : [ 3.76426088e+05, 3.76407980e+05, 3.76464635e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.35676506e+05, 4.27969742e+05, 4.22526559e+05, 3.85065347e+05, 3.76426083e+05, 3.69473533e+05, 3.41338102e+05, 3.32476638e+05, 3.24915298e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.50993093e+05, 3.17442427e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.76493525e+05, 3.76854948e+05, 5.32991949e+05, 3.76319385e+05, 3.75468892e+05, 2.35385635e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.56276059e+04, 2.56509933e+04, 3.63095428e+04, 2.56210900e+04, 2.55900510e+04, 1.60247566e+04, ],
  }),
  ("nof_tree_events",                 399991),
  ("nof_db_events",                   399991),
  ("fsize_local",                     1676271545), # 1.68GB, avg file size 335.25MB
  ("fsize_db",                        19678248548), # 19.68GB, avg file size 855.58MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH0_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 396992, ],
    'CountWeighted'                                                                  : [ 3.55412250e+05, 3.55410531e+05, 3.55488625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.04819812e+05, 3.98332203e+05, 3.94054719e+05, 3.63634750e+05, 3.55403250e+05, 3.49001797e+05, 3.26310531e+05, 3.17402781e+05, 3.09938344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.22055219e+05, 3.00641391e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.55421703e+05, 3.55401703e+05, 5.04488938e+05, 3.55429562e+05, 3.55703375e+05, 2.21857391e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.18788892e+04, 1.18760293e+04, 1.68777231e+04, 1.18800034e+04, 1.19152354e+04, 7.42161938e+03, ],
  }),
  ("nof_tree_events",                 396992),
  ("nof_db_events",                   396992),
  ("fsize_local",                     1708431622), # 1.71GB, avg file size 854.22MB
  ("fsize_db",                        19734784964), # 19.73GB, avg file size 1.10GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH1_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 383094, ],
    'CountWeighted'                                                                  : [ 3.29737453e+05, 3.29802117e+05, 3.29662312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.76047234e+05, 3.70846625e+05, 3.67536406e+05, 3.36477734e+05, 3.29708773e+05, 3.24487781e+05, 3.01172164e+05, 2.93770086e+05, 2.87542969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95972766e+05, 2.75400203e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.29785930e+05, 3.30061273e+05, 4.68089094e+05, 3.29679914e+05, 3.29018266e+05, 2.05303570e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.03153369e+03, 5.03408777e+03, 7.14946582e+03, 5.03076843e+03, 5.02948120e+03, 3.13244470e+03, ],
  }),
  ("nof_tree_events",                 383094),
  ("nof_db_events",                   383094),
  ("fsize_local",                     1648798884), # 1.65GB, avg file size 824.40MB
  ("fsize_db",                        19131899752), # 19.13GB, avg file size 797.16MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo2V2Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 386288, ],
    'CountWeighted'                                                                  : [ 3.80062156e+05, 3.79986203e+05, 3.80098594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.55293031e+05, 4.46722609e+05, 4.40108875e+05, 3.87605078e+05, 3.80056500e+05, 3.73632344e+05, 3.33729531e+05, 3.27040609e+05, 3.20980359e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.69144078e+05, 3.14496172e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.79938266e+05, 3.80013922e+05, 5.37718969e+05, 3.80189578e+05, 3.79694609e+05, 2.38125633e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.10034355e+04, 3.10088906e+04, 4.38966299e+04, 3.10243154e+04, 3.10121387e+04, 1.94415127e+04, ],
  }),
  ("nof_tree_events",                 386288),
  ("nof_db_events",                   386288),
  ("fsize_local",                     1505678728), # 1.51GB, avg file size 752.84MB
  ("fsize_db",                        18478360608), # 18.48GB, avg file size 879.92MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH5_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4V_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    30),
  ("nof_events",                      {
    'Count'                                                                          : [ 985392, ],
    'CountWeighted'                                                                  : [ 9.28005938e+05, 9.28055672e+05, 9.27767453e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.07353639e+06, 1.05482153e+06, 1.04168672e+06, 9.49022516e+05, 9.28005906e+05, 9.11077641e+05, 8.41480000e+05, 8.19806406e+05, 8.01316516e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11184825e+06, 7.82382297e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.27992953e+05, 9.27675641e+05, 1.34371028e+06, 9.27967250e+05, 9.25926281e+05, 5.53525406e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 6.31022549e+04, 6.31028184e+04, 9.15087891e+04, 6.31074844e+04, 6.30681934e+04, 3.76313037e+04, ],
  }),
  ("nof_tree_events",                 985392),
  ("nof_db_events",                   985392),
  ("fsize_local",                     4231909299), # 4.23GB, avg file size 1.06GB
  ("fsize_db",                        49340466342), # 49.34GB, avg file size 1.64GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH0_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4V_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    59),
  ("nof_events",                      {
    'Count'                                                                          : [ 932996, ],
    'CountWeighted'                                                                  : [ 8.35131141e+05, 8.35149078e+05, 8.35173875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.50669344e+05, 9.35633688e+05, 9.25741578e+05, 8.54261281e+05, 8.35122391e+05, 8.20145125e+05, 7.66755812e+05, 7.45910484e+05, 7.28442281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.91422562e+05, 7.06361562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.35267875e+05, 8.35419375e+05, 1.21122436e+06, 8.35005266e+05, 8.33099578e+05, 4.96999773e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.79137002e+04, 2.79266934e+04, 4.05158613e+04, 2.79011011e+04, 2.78762119e+04, 1.66093245e+04, ],
  }),
  ("nof_tree_events",                 932996),
  ("nof_db_events",                   932996),
  ("fsize_local",                     4133649091), # 4.13GB, avg file size 1.03GB
  ("fsize_db",                        47734342494), # 47.73GB, avg file size 809.06MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH1_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4V_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    39),
  ("nof_events",                      {
    'Count'                                                                          : [ 999995, ],
    'CountWeighted'                                                                  : [ 8.61716609e+05, 8.61742609e+05, 8.61753438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.82429828e+05, 9.68718391e+05, 9.59966812e+05, 8.79371641e+05, 8.61690078e+05, 8.47889781e+05, 7.87363234e+05, 7.67926594e+05, 7.51567438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03456333e+06, 7.19753359e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.61502969e+05, 8.61146422e+05, 1.25265550e+06, 8.62023438e+05, 8.61409031e+05, 5.11277109e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.31534910e+04, 1.31472415e+04, 1.91301602e+04, 1.31568535e+04, 1.31685728e+04, 7.81580530e+03, ],
  }),
  ("nof_tree_events",                 999995),
  ("nof_db_events",                   999995),
  ("fsize_local",                     4402542008), # 4.40GB, avg file size 1.10GB
  ("fsize_db",                        50832748643), # 50.83GB, avg file size 1.30GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["/GluGluToHHTo4V_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    66),
  ("nof_events",                      {
    'Count'                                                                          : [ 999792, ],
    'CountWeighted'                                                                  : [ 9.84031188e+05, 9.84025422e+05, 9.84040641e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17852791e+06, 1.15638297e+06, 1.13934978e+06, 1.00355550e+06, 9.84026703e+05, 9.67447156e+05, 8.64207562e+05, 8.46908062e+05, 8.31249734e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.21454181e+06, 8.14338156e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.84127219e+05, 9.83688422e+05, 1.42505412e+06, 9.83849438e+05, 9.83073703e+05, 5.87623266e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 8.02310898e+04, 8.01885859e+04, 1.16346102e+05, 8.02100859e+04, 8.03235957e+04, 4.79101406e+04, ],
  }),
  ("nof_tree_events",                 999792),
  ("nof_db_events",                   999792),
  ("fsize_local",                     3945260615), # 3.95GB, avg file size 986.32MB
  ("fsize_db",                        48774118094), # 48.77GB, avg file size 739.00MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2018/2020Jul15_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH5_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [
    "HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg",
    "HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg",
    "HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1",
    "HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1",
  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2018["sum_events"] = [
  [ 'signal_ggf_nonresonant_node_sm_hh_2v2t',          'signal_ggf_nonresonant_node_2_hh_2v2t',           'signal_ggf_nonresonant_node_3_hh_2v2t',           'signal_ggf_nonresonant_node_4_hh_2v2t',           'signal_ggf_nonresonant_node_5_hh_2v2t',           'signal_ggf_nonresonant_node_6_hh_2v2t',           'signal_ggf_nonresonant_node_7_hh_2v2t',           'signal_ggf_nonresonant_node_8_hh_2v2t',           'signal_ggf_nonresonant_node_9_hh_2v2t',           'signal_ggf_nonresonant_node_10_hh_2v2t',          'signal_ggf_nonresonant_node_11_hh_2v2t',          'signal_ggf_nonresonant_node_12_hh_2v2t',           ],
  [ 'signal_ggf_nonresonant_node_sm_hh_4t',            'signal_ggf_nonresonant_node_2_hh_4t',             'signal_ggf_nonresonant_node_3_hh_4t',             'signal_ggf_nonresonant_node_4_hh_4t',             'signal_ggf_nonresonant_node_5_hh_4t',             'signal_ggf_nonresonant_node_6_hh_4t',             'signal_ggf_nonresonant_node_7_hh_4t',             'signal_ggf_nonresonant_node_8_hh_4t',             'signal_ggf_nonresonant_node_9_hh_4t',             'signal_ggf_nonresonant_node_10_hh_4t',            'signal_ggf_nonresonant_node_11_hh_4t',            'signal_ggf_nonresonant_node_12_hh_4t',             ],
]

