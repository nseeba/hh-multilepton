from collections import OrderedDict as OD

# file generated at 2018-10-04 11:31:00 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_private_hh.py -p /hdfs/local/karl/ttHNtupleProduction/2017/2018Oct03_woPresel_nom_hh/ntuples -Z zeroes.txt -z zombies.txt -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_hh_private.py -M

samples_2017 = OD()
samples_2017["/HHTo4T_madgraph_pythia8_CP5_M400/private/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    193),
  ("nof_events",                      {
    'Count'                                  : [       384000, ],
    'CountFullWeighted'                      : [       383982,       383980,       383981, ],
    'CountWeighted'                          : [       383982,       383980,       383981, ],
    'CountFullWeightedNoPU'                  : [       383980, ],
    'CountWeightedNoPU'                      : [       383980, ],
    'CountWeightedLHEWeightScale'            : [       403362,       383982,       365152,       403362,       383982,       365152,       403362,       383982,       365152, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       403363,       383980,       365149,       403363,       383980,       365149,       403363,       383980,       365149, ],
    'CountFullWeightedLHEWeightScale'        : [       403362,       383982,       365152,       403362,       383982,       365152,       403362,       383982,       365152, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       403363,       383980,       365149,       403363,       383980,       365149,       403363,       383980,       365149, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     999441783), # 999.44MB, avg file size 999.44MB
  ("fsize_db",                        22408025117), # 22.41GB, avg file size 116.10MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct03_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4t"),
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
  ("sample_category",                 "signal_ggf_spin0_700_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    160),
  ("nof_events",                      {
    'Count'                                  : [       311998, ],
    'CountFullWeighted'                      : [       311956,       311958,       311958, ],
    'CountWeighted'                          : [       311956,       311958,       311958, ],
    'CountFullWeightedNoPU'                  : [       311962, ],
    'CountWeightedNoPU'                      : [       311962, ],
    'CountWeightedLHEWeightScale'            : [       340143,       311956,       287146,       340143,       311956,       287146,       340143,       311956,       287146, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       340146,       311962,       287152,       340146,       311962,       287152,       340146,       311962,       287152, ],
    'CountFullWeightedLHEWeightScale'        : [       340143,       311956,       287146,       340143,       311956,       287146,       340143,       311956,       287146, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       340146,       311962,       287152,       340146,       311962,       287152,       340146,       311962,       287152, ],
  }),
  ("nof_tree_events",                 311998),
  ("nof_db_events",                   311998),
  ("fsize_local",                     958829344), # 958.83MB, avg file size 958.83MB
  ("fsize_db",                        19502577906), # 19.50GB, avg file size 121.89MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct03_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4t"),
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

samples_2017["/HHTo2T2V_madgraph_pythia8_CP5_M400/private/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    130),
  ("nof_events",                      {
    'Count'                                  : [       257207, ],
    'CountFullWeighted'                      : [       257191,       257191,       257193, ],
    'CountWeighted'                          : [       257191,       257191,       257193, ],
    'CountFullWeightedNoPU'                  : [       257191, ],
    'CountWeightedNoPU'                      : [       257191, ],
    'CountWeightedLHEWeightScale'            : [       270167,       257191,       244583,       270167,       257191,       244583,       270167,       257191,       244583, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       270170,       257191,       244581,       270170,       257191,       244581,       270170,       257191,       244581, ],
    'CountFullWeightedLHEWeightScale'        : [       270167,       257191,       244583,       270167,       257191,       244583,       270167,       257191,       244583, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       270170,       257191,       244581,       270170,       257191,       244581,       270170,       257191,       244581, ],
  }),
  ("nof_tree_events",                 257207),
  ("nof_db_events",                   257207),
  ("fsize_local",                     684946015), # 684.95MB, avg file size 684.95MB
  ("fsize_db",                        15401525854), # 15.40GB, avg file size 118.47MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct03_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_2v2t"),
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

samples_2017["/HHTo2T2V_madgraph_pythia8_CP5_M700/private/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    152),
  ("nof_events",                      {
    'Count'                                  : [       301884, ],
    'CountFullWeighted'                      : [       301845,       301848,       301844, ],
    'CountWeighted'                          : [       301845,       301848,       301844, ],
    'CountFullWeightedNoPU'                  : [       301846, ],
    'CountWeightedNoPU'                      : [       301846, ],
    'CountWeightedLHEWeightScale'            : [       329111,       301845,       277844,       329111,       301845,       277844,       329111,       301845,       277844, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       329112,       301846,       277843,       329112,       301846,       277843,       329112,       301846,       277843, ],
    'CountFullWeightedLHEWeightScale'        : [       329111,       301845,       277844,       329111,       301845,       277844,       329111,       301845,       277844, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       329112,       301846,       277843,       329112,       301846,       277843,       329112,       301846,       277843, ],
  }),
  ("nof_tree_events",                 301884),
  ("nof_db_events",                   301884),
  ("fsize_local",                     957121976), # 957.12MB, avg file size 957.12MB
  ("fsize_db",                        19508012725), # 19.51GB, avg file size 128.34MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct03_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_2v2t"),
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

samples_2017["/HHTo4V_madgraph_pythia8_CP5_M400/private/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    133),
  ("nof_events",                      {
    'Count'                                  : [       262996, ],
    'CountFullWeighted'                      : [       262977,       262977,       262979, ],
    'CountWeighted'                          : [       262977,       262977,       262979, ],
    'CountFullWeightedNoPU'                  : [       262978, ],
    'CountWeightedNoPU'                      : [       262978, ],
    'CountWeightedLHEWeightScale'            : [       276256,       262977,       250077,       276256,       262977,       250077,       276256,       262977,       250077, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       276259,       262978,       250076,       276259,       262978,       250076,       276259,       262978,       250076, ],
    'CountFullWeightedLHEWeightScale'        : [       276256,       262977,       250077,       276256,       262977,       250077,       276256,       262977,       250077, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       276259,       262978,       250076,       276259,       262978,       250076,       276259,       262978,       250076, ],
  }),
  ("nof_tree_events",                 262996),
  ("nof_db_events",                   262996),
  ("fsize_local",                     680505339), # 680.51MB, avg file size 680.51MB
  ("fsize_db",                        16090082982), # 16.09GB, avg file size 120.98MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct03_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4v"),
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

samples_2017["/HHTo4V_madgraph_pythia8_CP5_M700/private/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    118),
  ("nof_events",                      {
    'Count'                                  : [       230116, ],
    'CountFullWeighted'                      : [       230099,       230100,       230098, ],
    'CountWeighted'                          : [       230099,       230100,       230098, ],
    'CountFullWeightedNoPU'                  : [       230102, ],
    'CountWeightedNoPU'                      : [       230102, ],
    'CountWeightedLHEWeightScale'            : [       250899,       230099,       211794,       250899,       230099,       211794,       250899,       230099,       211794, ],
    'CountWeightedLHEWeightScaleNoPU'        : [       250901,       230102,       211795,       250901,       230102,       211795,       250901,       230102,       211795, ],
    'CountFullWeightedLHEWeightScale'        : [       250899,       230099,       211794,       250899,       230099,       211794,       250899,       230099,       211794, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [       250901,       230102,       211795,       250901,       230102,       211795,       250901,       230102,       211795, ],
  }),
  ("nof_tree_events",                 230116),
  ("nof_db_events",                   230116),
  ("fsize_local",                     716174119), # 716.17MB, avg file size 716.17MB
  ("fsize_db",                        15395786053), # 15.40GB, avg file size 130.47MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Oct03_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4v"),
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

