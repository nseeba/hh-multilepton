from collections import OrderedDict as OD

# file generated at 2018-12-23 23:31:16 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_wjets.py -p /hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples -Z zeroes.txt -z zombies.txt -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_wjets.py -M

samples_2017 = OD()
samples_2017["/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_part1"),
  ("nof_files",                       17),
  ("nof_db_files",                    514),
  ("nof_events",                      {
    'Count'                                  : [      8205539, ],
    'CountFullWeighted'                      : [      8197569,      8197774,      8197515, ],
    'CountWeighted'                          : [      8197569,      8197774,      8197515, ],
    'CountFullWeightedNoPU'                  : [      8198363, ],
    'CountWeightedNoPU'                      : [      8198363, ],
    'CountWeightedLHEWeightScale'            : [      7214961,      8235125,      9149243,      7178883,      8197569,      9110745,      7149457,      8166921,      9079335, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      7215797,      8235943,      9150272,      7179700,      8198363,      9111749,      7150259,      8167706,      9080318, ],
    'CountFullWeightedLHEWeightScale'        : [      7214961,      8235125,      9149243,      7178883,      8197569,      9110745,      7149457,      8166921,      9079335, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      7215797,      8235943,      9150272,      7179700,      8198363,      9111749,      7150259,      8167706,      9080318, ],
  }),
  ("nof_tree_events",                 8205539),
  ("nof_db_events",                   33073306),
  ("fsize_local",                     8986194948), # 8.99GB, avg file size 528.60MB
  ("fsize_db",                        1301026785288), # 1.30TB, avg file size 2.53GB
  ("use_it",                          False),
  ("xsection",                        61526.7),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_part1"),
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

samples_2017["/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_ext_part1"),
  ("nof_files",                       23),
  ("nof_db_files",                    738),
  ("nof_events",                      {
    'Count'                                  : [     11157394, ],
    'CountFullWeighted'                      : [     11146982,     11147958,     11145816, ],
    'CountWeighted'                          : [     11146982,     11147958,     11145816, ],
    'CountFullWeightedNoPU'                  : [     11147320, ],
    'CountWeightedNoPU'                      : [     11147320, ],
    'CountWeightedLHEWeightScale'            : [      9810409,     11197747,     12441660,      9761661,     11146982,     12389617,      9721907,     11105588,     12347157, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      9810433,     11198064,     12441784,      9761701,     11147320,     12389759,      9721957,     11105927,     12347313, ],
    'CountFullWeightedLHEWeightScale'        : [      9810409,     11197747,     12441660,      9761661,     11146982,     12389617,      9721907,     11105588,     12347157, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      9810433,     11198064,     12441784,      9761701,     11147320,     12389759,      9721957,     11105927,     12347313, ],
  }),
  ("nof_tree_events",                 11157394),
  ("nof_db_events",                   44627200),
  ("fsize_local",                     12214253259), # 12.21GB, avg file size 531.05MB
  ("fsize_db",                        1756207826672), # 1.76TB, avg file size 2.38GB
  ("use_it",                          False),
  ("xsection",                        61526.7),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_ext_part1"),
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

samples_2017["/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "W1JetsToLNu_part1"),
  ("nof_files",                       28),
  ("nof_db_files",                    801),
  ("nof_events",                      {
    'Count'                                  : [     13521637, ],
    'CountFullWeighted'                      : [     13510772,     13510180,     13510921, ],
    'CountWeighted'                          : [     13510772,     13510180,     13510921, ],
    'CountFullWeightedNoPU'                  : [     13511179, ],
    'CountWeightedNoPU'                      : [     13511179, ],
    'CountWeightedLHEWeightScale'            : [     11794481,     13644278,     15201130,     11669417,     13510772,     15060955,     11566901,     13401315,     14946107, ],
    'CountWeightedLHEWeightScaleNoPU'        : [     11795231,     13644669,     15201697,     11670196,     13511179,     15061557,     11567703,     13401786,     14946741, ],
    'CountFullWeightedLHEWeightScale'        : [     11794481,     13644278,     15201130,     11669417,     13510772,     15060955,     11566901,     13401315,     14946107, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [     11795231,     13644669,     15201697,     11670196,     13511179,     15061557,     11567703,     13401786,     14946741, ],
  }),
  ("nof_tree_events",                 13521637),
  ("nof_db_events",                   54147812),
  ("fsize_local",                     16492788821), # 16.49GB, avg file size 589.03MB
  ("fsize_db",                        2175397601720), # 2.18TB, avg file size 2.72GB
  ("use_it",                          False),
  ("xsection",                        9418.44),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/W1JetsToLNu_part1"),
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

samples_2017["/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "W2JetsToLNu_part1"),
  ("nof_files",                       4),
  ("nof_db_files",                    157),
  ("nof_events",                      {
    'Count'                                  : [      1628331, ],
    'CountFullWeighted'                      : [      1626791,      1626707,      1626990, ],
    'CountWeighted'                          : [      1626791,      1626707,      1626990, ],
    'CountFullWeightedNoPU'                  : [      1626569, ],
    'CountWeightedNoPU'                      : [      1626569, ],
    'CountWeightedLHEWeightScale'            : [      1537282,      1677975,      1778883,      1489573,      1626791,      1725321,      1450572,      1584985,      1681544, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      1536922,      1677712,      1778630,      1489238,      1626569,      1725096,      1450256,      1584764,      1681341, ],
    'CountFullWeightedLHEWeightScale'        : [      1537282,      1677975,      1778883,      1489573,      1626791,      1725321,      1450572,      1584985,      1681544, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      1536922,      1677712,      1778630,      1489238,      1626569,      1725096,      1450256,      1584764,      1681341, ],
  }),
  ("nof_tree_events",                 1628331),
  ("nof_db_events",                   6577492),
  ("fsize_local",                     2303116664), # 2.30GB, avg file size 575.78MB
  ("fsize_db",                        283312015249), # 283.31GB, avg file size 1.80GB
  ("use_it",                          False),
  ("xsection",                        3244.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/W2JetsToLNu_part1"),
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

samples_2017["/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "W3JetsToLNu_part1"),
  ("nof_files",                       10),
  ("nof_db_files",                    250),
  ("nof_events",                      {
    'Count'                                  : [      4914826, ],
    'CountFullWeighted'                      : [      4902903,      4901968,      4903529, ],
    'CountWeighted'                          : [      4902903,      4901968,      4903529, ],
    'CountFullWeightedNoPU'                  : [      4907218, ],
    'CountWeightedNoPU'                      : [      4907218, ],
    'CountWeightedLHEWeightScale'            : [      4992942,      5130909,      5178221,      4768563,      4902903,      4949917,      4585897,      4717186,      4764005, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      4997520,      5135478,      5182838,      4772911,      4907218,      4954303,      4590050,      4721362,      4768204, ],
    'CountFullWeightedLHEWeightScale'        : [      4992942,      5130909,      5178221,      4768563,      4902903,      4949917,      4585897,      4717186,      4764005, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      4997520,      5135478,      5182838,      4772911,      4907218,      4954303,      4590050,      4721362,      4768204, ],
  }),
  ("nof_tree_events",                 4914826),
  ("nof_db_events",                   19700377),
  ("fsize_local",                     7955870235), # 7.96GB, avg file size 795.59MB
  ("fsize_db",                        868954430671), # 868.95GB, avg file size 3.48GB
  ("use_it",                          False),
  ("xsection",                        1153.02),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/W3JetsToLNu_part1"),
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

samples_2017["/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "W4JetsToLNu_part1"),
  ("nof_files",                       6),
  ("nof_db_files",                    186),
  ("nof_events",                      {
    'Count'                                  : [      2797023, ],
    'CountFullWeighted'                      : [      2769673,      2767457,      2772808, ],
    'CountWeighted'                          : [      2769673,      2767457,      2772808, ],
    'CountFullWeightedNoPU'                  : [      2789505, ],
    'CountWeightedNoPU'                      : [      2789505, ],
    'CountWeightedLHEWeightScale'            : [      3055181,      2942347,      2818873,      2874139,      2769662,      2654661,      2728825,      2631018,      2522774, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      3077081,      2963417,      2839050,      2894724,      2789505,      2673646,      2748358,      2649870,      2540807, ],
    'CountFullWeightedLHEWeightScale'        : [      3055181,      2942347,      2818873,      2874139,      2769662,      2654661,      2728825,      2631018,      2522774, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      3077081,      2963417,      2839050,      2894724,      2789505,      2673646,      2748358,      2649870,      2540807, ],
  }),
  ("nof_tree_events",                 2797023),
  ("nof_db_events",                   11333705),
  ("fsize_local",                     5559505691), # 5.56GB, avg file size 926.58MB
  ("fsize_db",                        544171543197), # 544.17GB, avg file size 2.93GB
  ("use_it",                          False),
  ("xsection",                        633.05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/W4JetsToLNu_part1"),
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

samples_2017["/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT100To200_part1"),
  ("nof_files",                       18),
  ("nof_db_files",                    735),
  ("nof_events",                      {
    'Count'                                  : [      8995404, ],
    'CountFullWeighted'                      : [      8980267,      8982218,      8980720, ],
    'CountWeighted'                          : [      8980267,      8982218,      8980720, ],
    'CountFullWeightedNoPU'                  : [      8980800, ],
    'CountWeightedNoPU'                      : [      8980800, ],
    'CountWeightedLHEWeightScale'            : [      9166373,      9336814,      9375015,      8814586,      8980239,      9018812,      8525778,      8688080,      8726385, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      9165981,      9337084,      9374797,      8814200,      8980799,      9018605,      8525387,      8688294,      8726171, ],
    'CountFullWeightedLHEWeightScale'        : [      9166373,      9336814,      9375015,      8814586,      8980239,      9018812,      8525778,      8688080,      8726385, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      9165981,      9337084,      9374797,      8814200,      8980799,      9018605,      8525387,      8688294,      8726171, ],
  }),
  ("nof_tree_events",                 8995404),
  ("nof_db_events",                   35862893),
  ("fsize_local",                     14486987197), # 14.49GB, avg file size 804.83MB
  ("fsize_db",                        1632440553612), # 1.63TB, avg file size 2.22GB
  ("use_it",                          False),
  ("xsection",                        1625.94),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT100To200_part1"),
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

samples_2017["/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT200To400_part1"),
  ("nof_files",                       11),
  ("nof_db_files",                    400),
  ("nof_events",                      {
    'Count'                                  : [      5297948, ],
    'CountFullWeighted'                      : [      5282593,      5283305,      5281561, ],
    'CountWeighted'                          : [      5282593,      5283305,      5281561, ],
    'CountFullWeightedNoPU'                  : [      5283300, ],
    'CountWeightedNoPU'                      : [      5283300, ],
    'CountWeightedLHEWeightScale'            : [      5866373,      5650966,      5422055,      5484316,      5282593,      5068267,      5178432,      4987826,      4785077, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      5866964,      5651604,      5422638,      5484896,      5283300,      5068845,      5178994,      4988434,      4785636, ],
    'CountFullWeightedLHEWeightScale'        : [      5866373,      5650966,      5422055,      5484316,      5282593,      5068267,      5178432,      4987826,      4785077, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      5866964,      5651604,      5422638,      5484896,      5283300,      5068845,      5178994,      4988434,      4785636, ],
  }),
  ("nof_tree_events",                 5297948),
  ("nof_db_events",                   21250517),
  ("fsize_local",                     10983808460), # 10.98GB, avg file size 998.53MB
  ("fsize_db",                        1058111782457), # 1.06TB, avg file size 2.65GB
  ("use_it",                          False),
  ("xsection",                        477.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT200To400_part1"),
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

samples_2017["/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT400To600_part1"),
  ("nof_files",                       8),
  ("nof_db_files",                    314),
  ("nof_events",                      {
    'Count'                                  : [      3525798, ],
    'CountFullWeighted'                      : [      3511076,      3510846,      3511370, ],
    'CountWeighted'                          : [      3511076,      3510846,      3511370, ],
    'CountFullWeightedNoPU'                  : [      3510274, ],
    'CountWeightedNoPU'                      : [      3510274, ],
    'CountWeightedLHEWeightScale'            : [      4204474,      3889028,      3608938,      3797146,      3511032,      3257272,      3474753,      3211999,      2978974, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      4203531,      3888202,      3608177,      3796210,      3510274,      3256517,      3473837,      3211186,      2978228, ],
    'CountFullWeightedLHEWeightScale'        : [      4204474,      3889028,      3608938,      3797146,      3511032,      3257272,      3474753,      3211999,      2978974, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      4203531,      3888202,      3608177,      3796210,      3510274,      3256517,      3473837,      3211186,      2978228, ],
  }),
  ("nof_tree_events",                 3525798),
  ("nof_db_events",                   14313274),
  ("fsize_local",                     9443058998), # 9.44GB, avg file size 1.18GB
  ("fsize_db",                        780224610750), # 780.22GB, avg file size 2.48GB
  ("use_it",                          False),
  ("xsection",                        67.51),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT400To600_part1"),
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

samples_2017["/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT600To800_part1"),
  ("nof_files",                       11),
  ("nof_db_files",                    488),
  ("nof_events",                      {
    'Count'                                  : [      5402228, ],
    'CountFullWeighted'                      : [      5370812,      5371089,      5369952, ],
    'CountWeighted'                          : [      5370812,      5371089,      5369952, ],
    'CountFullWeightedNoPU'                  : [      5370862, ],
    'CountWeightedNoPU'                      : [      5370862, ],
    'CountWeightedLHEWeightScale'            : [      6621507,      6001128,      5474746,      5927743,      5370780,      4898495,      5376085,      4869649,      4440326, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      6621510,      6001198,      5474794,      5927765,      5370862,      4898546,      5376123,      4869672,      4440382, ],
    'CountFullWeightedLHEWeightScale'        : [      6621507,      6001128,      5474746,      5927743,      5370780,      4898495,      5376085,      4869649,      4440326, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      6621510,      6001198,      5474794,      5927765,      5370862,      4898546,      5376123,      4869672,      4440382, ],
  }),
  ("nof_tree_events",                 5402228),
  ("nof_db_events",                   21709087),
  ("fsize_local",                     15851126632), # 15.85GB, avg file size 1.44GB
  ("fsize_db",                        1256446599197), # 1.26TB, avg file size 2.57GB
  ("use_it",                          False),
  ("xsection",                        15.09),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT600To800_part1"),
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

samples_2017["/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT800To1200_part1"),
  ("nof_files",                       11),
  ("nof_db_files",                    487),
  ("nof_events",                      {
    'Count'                                  : [      5094340, ],
    'CountFullWeighted'                      : [      5055512,      5055355,      5055672, ],
    'CountWeighted'                          : [      5055512,      5055355,      5055672, ],
    'CountFullWeightedNoPU'                  : [      5054718, ],
    'CountWeightedNoPU'                      : [      5054718, ],
    'CountWeightedLHEWeightScale'            : [      6354861,      5660569,      5088855,      5676788,      5055512,      4544059,      5134325,      4571426,      4108275, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      6353937,      5659750,      5088116,      5675955,      5054718,      4543396,      5133584,      4570785,      4107690, ],
    'CountFullWeightedLHEWeightScale'        : [      6354861,      5660569,      5088855,      5676788,      5055512,      4544059,      5134325,      4571426,      4108275, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      6353937,      5659750,      5088116,      5675955,      5054718,      4543396,      5133584,      4570785,      4107690, ],
  }),
  ("nof_tree_events",                 5094340),
  ("nof_db_events",                   20432728),
  ("fsize_local",                     15669209102), # 15.67GB, avg file size 1.42GB
  ("fsize_db",                        1225597665572), # 1.23TB, avg file size 2.52GB
  ("use_it",                          False),
  ("xsection",                        6.297),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT800To1200_part1"),
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

samples_2017["/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT1200To2500_part1"),
  ("nof_files",                       11),
  ("nof_db_files",                    551),
  ("nof_events",                      {
    'Count'                                  : [      5044345, ],
    'CountFullWeighted'                      : [      4977989,      4978082,      4978328, ],
    'CountWeighted'                          : [      4977989,      4978082,      4978328, ],
    'CountFullWeightedNoPU'                  : [      4978477, ],
    'CountWeightedNoPU'                      : [      4978477, ],
    'CountWeightedLHEWeightScale'            : [      6376434,      5555646,      4900631,      5714454,      4977989,      4390688,      5178237,      4510376,      3977701, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      6376855,      5556089,      4900975,      5714829,      4978477,      4390985,      5178581,      4510674,      3977979, ],
    'CountFullWeightedLHEWeightScale'        : [      6376434,      5555646,      4900631,      5714454,      4977989,      4390688,      5178237,      4510376,      3977701, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      6376855,      5556089,      4900975,      5714829,      4978477,      4390985,      5178581,      4510674,      3977979, ],
  }),
  ("nof_tree_events",                 5044345),
  ("nof_db_events",                   20258624),
  ("fsize_local",                     16156961194), # 16.16GB, avg file size 1.47GB
  ("fsize_db",                        1289100671636), # 1.29TB, avg file size 2.34GB
  ("use_it",                          False),
  ("xsection",                        1.262),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT1200To2500_part1"),
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

samples_2017["/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT2500ToInf_part1"),
  ("nof_files",                       11),
  ("nof_db_files",                    616),
  ("nof_events",                      {
    'Count'                                  : [      5319770, ],
    'CountFullWeighted'                      : [      5106378,      5106195,      5105900, ],
    'CountWeighted'                          : [      5106378,      5106195,      5105900, ],
    'CountFullWeightedNoPU'                  : [      5105822, ],
    'CountWeightedNoPU'                      : [      5105822, ],
    'CountWeightedLHEWeightScale'            : [      6675434,      5618495,      4805274,      6066558,      5106362,      4367162,      5559508,      4679314,      4002252, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      6674994,      5618112,      4805072,      6066174,      5105822,      4366981,      5559164,      4679326,      4002101, ],
    'CountFullWeightedLHEWeightScale'        : [      6675434,      5618495,      4805274,      6066558,      5106362,      4367162,      5559508,      4679314,      4002252, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      6674994,      5618112,      4805072,      6066174,      5105822,      4366981,      5559164,      4679326,      4002101, ],
  }),
  ("nof_tree_events",                 5319770),
  ("nof_db_events",                   21495421),
  ("fsize_local",                     17851101150), # 17.85GB, avg file size 1.62GB
  ("fsize_db",                        1489610697179), # 1.49TB, avg file size 2.42GB
  ("use_it",                          False),
  ("xsection",                        0.009446),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT2500ToInf_part1"),
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

samples_2017["/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM/part2"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_part2"),
  ("nof_files",                       51),
  ("nof_db_files",                    514),
  ("nof_events",                      {
    'Count'                                  : [     24867767, ],
    'CountFullWeighted'                      : [     24846835,     24846323,     24846855, ],
    'CountWeighted'                          : [     24846835,     24846323,     24846855, ],
    'CountFullWeightedNoPU'                  : [     24845369, ],
    'CountWeightedNoPU'                      : [     24845369, ],
    'CountWeightedLHEWeightScale'            : [     21867935,     24960501,     27731572,     21758776,     24846835,     27615030,     21669748,     24754082,     27519944, ],
    'CountWeightedLHEWeightScaleNoPU'        : [     21866976,     24959041,     27730358,     21757811,     24845369,     27613814,     21668777,     24752641,     27518720, ],
    'CountFullWeightedLHEWeightScale'        : [     21867935,     24960501,     27731572,     21758776,     24846835,     27615030,     21669748,     24754082,     27519944, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [     21866976,     24959041,     27730358,     21757811,     24845369,     27613814,     21668777,     24752641,     27518720, ],
  }),
  ("nof_tree_events",                 24867767),
  ("nof_db_events",                   33073306),
  ("fsize_local",                     27231335994), # 27.23GB, avg file size 533.95MB
  ("fsize_db",                        1301026785288), # 1.30TB, avg file size 2.53GB
  ("use_it",                          False),
  ("xsection",                        61526.7),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_part2"),
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

samples_2017["/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM/part2"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_ext_part2"),
  ("nof_files",                       68),
  ("nof_db_files",                    738),
  ("nof_events",                      {
    'Count'                                  : [     33469806, ],
    'CountFullWeighted'                      : [     33439627,     33441763,     33436040, ],
    'CountWeighted'                          : [     33439627,     33441763,     33436040, ],
    'CountFullWeightedNoPU'                  : [     33440128, ],
    'CountWeightedNoPU'                      : [     33440128, ],
    'CountWeightedLHEWeightScale'            : [     29429816,     33591795,     37323613,     29283675,     33439627,     37167626,     29164488,     33315538,     37040352, ],
    'CountWeightedLHEWeightScaleNoPU'        : [     29430035,     33592435,     37323296,     29283744,     33440128,     37167159,     29164441,     33315888,     37039764, ],
    'CountFullWeightedLHEWeightScale'        : [     29429816,     33591795,     37323613,     29283675,     33439627,     37167626,     29164488,     33315538,     37040352, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [     29430035,     33592435,     37323296,     29283744,     33440128,     37167159,     29164441,     33315888,     37039764, ],
  }),
  ("nof_tree_events",                 33469806),
  ("nof_db_events",                   44627200),
  ("fsize_local",                     36644516958), # 36.64GB, avg file size 538.89MB
  ("fsize_db",                        1756207826672), # 1.76TB, avg file size 2.38GB
  ("use_it",                          False),
  ("xsection",                        61526.7),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_ext_part2"),
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

samples_2017["/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM/part2"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "W1JetsToLNu_part2"),
  ("nof_files",                       83),
  ("nof_db_files",                    801),
  ("nof_events",                      {
    'Count'                                  : [     40626175, ],
    'CountFullWeighted'                      : [     40597128,     40597941,     40594268, ],
    'CountWeighted'                          : [     40597128,     40597941,     40594268, ],
    'CountFullWeightedNoPU'                  : [     40595747, ],
    'CountWeightedNoPU'                      : [     40595747, ],
    'CountWeightedLHEWeightScale'            : [     35440590,     40998049,     45675372,     35065022,     40597128,     45254414,     34757177,     40268432,     44909517, ],
    'CountWeightedLHEWeightScaleNoPU'        : [     35440118,     40996692,     45674818,     35064576,     40595747,     45253885,     34756745,     40267180,     44909026, ],
    'CountFullWeightedLHEWeightScale'        : [     35440590,     40998049,     45675372,     35065022,     40597128,     45254414,     34757177,     40268432,     44909517, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [     35440118,     40996692,     45674818,     35064576,     40595747,     45253885,     34756745,     40267180,     44909026, ],
  }),
  ("nof_tree_events",                 40626175),
  ("nof_db_events",                   54147812),
  ("fsize_local",                     49549232504), # 49.55GB, avg file size 596.98MB
  ("fsize_db",                        2175397601720), # 2.18TB, avg file size 2.72GB
  ("use_it",                          False),
  ("xsection",                        9418.44),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/W1JetsToLNu_part2"),
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

samples_2017["/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4/MINIAODSIM/part2"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "W2JetsToLNu_part2"),
  ("nof_files",                       11),
  ("nof_db_files",                    157),
  ("nof_events",                      {
    'Count'                                  : [      4949161, ],
    'CountFullWeighted'                      : [      4943423,      4943614,      4943670, ],
    'CountWeighted'                          : [      4943423,      4943614,      4943670, ],
    'CountFullWeightedNoPU'                  : [      4943873, ],
    'CountWeightedNoPU'                      : [      4943873, ],
    'CountWeightedLHEWeightScale'            : [      4670996,      5098655,      5405411,      4526305,      4943423,      5242975,      4408024,      4816642,      5110220, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      4671206,      5099077,      5405760,      4526495,      4943873,      5243311,      4408193,      4817014,      5110535, ],
    'CountFullWeightedLHEWeightScale'        : [      4670996,      5098655,      5405411,      4526305,      4943423,      5242975,      4408024,      4816642,      5110220, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      4671206,      5099077,      5405760,      4526495,      4943873,      5243311,      4408193,      4817014,      5110535, ],
  }),
  ("nof_tree_events",                 4949161),
  ("nof_db_events",                   6577492),
  ("fsize_local",                     6996828700), # 7.00GB, avg file size 636.08MB
  ("fsize_db",                        283312015249), # 283.31GB, avg file size 1.80GB
  ("use_it",                          False),
  ("xsection",                        3244.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/W2JetsToLNu_part2"),
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

samples_2017["/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "W3JetsToLNu_part2"),
  ("nof_files",                       30),
  ("nof_db_files",                    250),
  ("nof_events",                      {
    'Count'                                  : [     14785551, ],
    'CountFullWeighted'                      : [     14766893,     14767551,     14766068, ],
    'CountWeighted'                          : [     14766893,     14767551,     14766068, ],
    'CountFullWeightedNoPU'                  : [     14762475, ],
    'CountWeightedNoPU'                      : [     14762475, ],
    'CountWeightedLHEWeightScale'            : [     15039996,     15454511,     15596188,     14363288,     14766893,     14907684,     13812410,     14206849,     14347047, ],
    'CountWeightedLHEWeightScaleNoPU'        : [     15035370,     15449728,     15591636,     14359099,     14762475,     14903563,     13808568,     14202929,     14343282, ],
    'CountFullWeightedLHEWeightScale'        : [     15039996,     15454511,     15596188,     14363288,     14766893,     14907684,     13812410,     14206849,     14347047, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [     15035370,     15449728,     15591636,     14359099,     14762475,     14903563,     13808568,     14202929,     14343282, ],
  }),
  ("nof_tree_events",                 14785551),
  ("nof_db_events",                   19700377),
  ("fsize_local",                     23940787851), # 23.94GB, avg file size 798.03MB
  ("fsize_db",                        868954430671), # 868.95GB, avg file size 3.48GB
  ("use_it",                          False),
  ("xsection",                        1153.02),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/W3JetsToLNu_part2"),
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

samples_2017["/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "W4JetsToLNu_part2"),
  ("nof_files",                       18),
  ("nof_db_files",                    186),
  ("nof_events",                      {
    'Count'                                  : [      8536682, ],
    'CountFullWeighted'                      : [      8533646,      8536591,      8530342, ],
    'CountWeighted'                          : [      8533646,      8536591,      8530342, ],
    'CountFullWeightedNoPU'                  : [      8513920, ],
    'CountWeightedNoPU'                      : [      8513920, ],
    'CountWeightedLHEWeightScale'            : [      9414675,      9066238,      8685214,      8856246,      8533611,      8178744,      8408056,      8106022,      7772007, ],
    'CountWeightedLHEWeightScaleNoPU'        : [      9393026,      9045380,      8665280,      8835721,      8513919,      8159845,      8388463,      8087249,      7753951, ],
    'CountFullWeightedLHEWeightScale'        : [      9414675,      9066238,      8685214,      8856246,      8533611,      8178744,      8408056,      8106022,      7772007, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [      9393026,      9045380,      8665280,      8835721,      8513919,      8159845,      8388463,      8087249,      7753951, ],
  }),
  ("nof_tree_events",                 8536682),
  ("nof_db_events",                   11333705),
  ("fsize_local",                     16982283435), # 16.98GB, avg file size 943.46MB
  ("fsize_db",                        544171543197), # 544.17GB, avg file size 2.93GB
  ("use_it",                          False),
  ("xsection",                        633.05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/W4JetsToLNu_part2"),
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

samples_2017["/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM/part2"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT100To200_part2"),
  ("nof_files",                       54),
  ("nof_db_files",                    735),
  ("nof_events",                      {
    'Count'                                  : [     26867489, ],
    'CountFullWeighted'                      : [     26821020,     26826327,     26822918, ],
    'CountWeighted'                          : [     26821020,     26826327,     26822918, ],
    'CountFullWeightedNoPU'                  : [     26823823, ],
    'CountWeightedNoPU'                      : [     26823823, ],
    'CountWeightedLHEWeightScale'            : [     27376497,     27886252,     28000899,     26325535,     26820935,     26936645,     25462716,     25948063,     26062925, ],
    'CountWeightedLHEWeightScaleNoPU'        : [     27376729,     27888268,     28001313,     26325791,     26823820,     26937102,     25462962,     25949920,     26063379, ],
    'CountFullWeightedLHEWeightScale'        : [     27376497,     27886252,     28000899,     26325535,     26820935,     26936645,     25462716,     25948063,     26062925, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [     27376729,     27888268,     28001313,     26325791,     26823820,     26937102,     25462962,     25949920,     26063379, ],
  }),
  ("nof_tree_events",                 26867489),
  ("nof_db_events",                   35862893),
  ("fsize_local",                     43276410952), # 43.28GB, avg file size 801.42MB
  ("fsize_db",                        1632440553612), # 1.63TB, avg file size 2.22GB
  ("use_it",                          False),
  ("xsection",                        1625.94),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT100To200_part2"),
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

samples_2017["/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT200To400_part2"),
  ("nof_files",                       33),
  ("nof_db_files",                    400),
  ("nof_events",                      {
    'Count'                                  : [     15952569, ],
    'CountFullWeighted'                      : [     15908875,     15908272,     15908260, ],
    'CountWeighted'                          : [     15908875,     15908272,     15908260, ],
    'CountFullWeightedNoPU'                  : [     15908911, ],
    'CountWeightedNoPU'                      : [     15908911, ],
    'CountWeightedLHEWeightScale'            : [     17666952,     17018558,     16329387,     16516124,     15908875,     15263602,     15594662,     15020857,     14410415, ],
    'CountWeightedLHEWeightScaleNoPU'        : [     17666542,     17018265,     16328916,     16515816,     15908911,     15263224,     15594419,     15020705,     14410077, ],
    'CountFullWeightedLHEWeightScale'        : [     17666952,     17018558,     16329387,     16516124,     15908875,     15263602,     15594662,     15020857,     14410415, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [     17666542,     17018265,     16328916,     16515816,     15908911,     15263224,     15594419,     15020705,     14410077, ],
  }),
  ("nof_tree_events",                 15952569),
  ("nof_db_events",                   21250517),
  ("fsize_local",                     33068128164), # 33.07GB, avg file size 1.00GB
  ("fsize_db",                        1058111782457), # 1.06TB, avg file size 2.65GB
  ("use_it",                          False),
  ("xsection",                        477.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT200To400_part2"),
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

samples_2017["/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT400To600_part2"),
  ("nof_files",                       22),
  ("nof_db_files",                    314),
  ("nof_events",                      {
    'Count'                                  : [     10787476, ],
    'CountFullWeighted'                      : [     10738911,     10739209,     10738379, ],
    'CountWeighted'                          : [     10738911,     10739209,     10738379, ],
    'CountFullWeightedNoPU'                  : [     10739840, ],
    'CountWeightedNoPU'                      : [     10739840, ],
    'CountWeightedLHEWeightScale'            : [     12860357,     11895464,     11038772,     11613889,     10738777,      9962682,     10627390,      9823780,      9111147, ],
    'CountWeightedLHEWeightScaleNoPU'        : [     12861306,     11896541,     11039847,     11614618,     10739839,      9963551,     10627961,      9824480,      9111853, ],
    'CountFullWeightedLHEWeightScale'        : [     12860357,     11895464,     11038772,     11613889,     10738777,      9962682,     10627390,      9823780,      9111147, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [     12861306,     11896541,     11039847,     11614618,     10739839,      9963551,     10627961,      9824480,      9111853, ],
  }),
  ("nof_tree_events",                 10787476),
  ("nof_db_events",                   14313274),
  ("fsize_local",                     28886840965), # 28.89GB, avg file size 1.31GB
  ("fsize_db",                        780224610750), # 780.22GB, avg file size 2.48GB
  ("use_it",                          False),
  ("xsection",                        67.51),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT400To600_part2"),
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

samples_2017["/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT600To800_part2"),
  ("nof_files",                       33),
  ("nof_db_files",                    488),
  ("nof_events",                      {
    'Count'                                  : [     16306859, ],
    'CountFullWeighted'                      : [     16211502,     16211313,     16210383, ],
    'CountWeighted'                          : [     16211502,     16211313,     16210383, ],
    'CountFullWeightedNoPU'                  : [     16211447, ],
    'CountWeightedNoPU'                      : [     16211447, ],
    'CountWeightedLHEWeightScale'            : [     19986813,     18113885,     16524806,     17892945,     16211396,     14785577,     16228005,     14698941,     13402778, ],
    'CountWeightedLHEWeightScaleNoPU'        : [     19986798,     18113940,     16524730,     17892927,     16211446,     14785477,     16227982,     14698786,     13402693, ],
    'CountFullWeightedLHEWeightScale'        : [     19986813,     18113885,     16524806,     17892945,     16211396,     14785577,     16228005,     14698941,     13402778, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [     19986798,     18113940,     16524730,     17892927,     16211446,     14785477,     16227982,     14698786,     13402693, ],
  }),
  ("nof_tree_events",                 16306859),
  ("nof_db_events",                   21709087),
  ("fsize_local",                     47846637970), # 47.85GB, avg file size 1.45GB
  ("fsize_db",                        1256446599197), # 1.26TB, avg file size 2.57GB
  ("use_it",                          False),
  ("xsection",                        15.09),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT600To800_part2"),
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

samples_2017["/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT800To1200_part2"),
  ("nof_files",                       31),
  ("nof_db_files",                    487),
  ("nof_events",                      {
    'Count'                                  : [     15372352, ],
    'CountFullWeighted'                      : [     15251663,     15252367,     15251090, ],
    'CountWeighted'                          : [     15251663,     15252367,     15251090, ],
    'CountFullWeightedNoPU'                  : [     15251960, ],
    'CountWeightedNoPU'                      : [     15251960, ],
    'CountWeightedLHEWeightScale'            : [     19171779,     17076510,     15351350,     17126615,     15251663,     13708268,     15490410,     13791595,     12393928, ],
    'CountWeightedLHEWeightScaleNoPU'        : [     19172195,     17076966,     15351779,     17127075,     15251960,     13708722,     15490930,     13792140,     12394422, ],
    'CountFullWeightedLHEWeightScale'        : [     19171779,     17076510,     15351350,     17126615,     15251663,     13708268,     15490410,     13791595,     12393928, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [     19172195,     17076966,     15351779,     17127075,     15251960,     13708722,     15490930,     13792140,     12394422, ],
  }),
  ("nof_tree_events",                 15372352),
  ("nof_db_events",                   20432728),
  ("fsize_local",                     47277853856), # 47.28GB, avg file size 1.53GB
  ("fsize_db",                        1225597665572), # 1.23TB, avg file size 2.52GB
  ("use_it",                          False),
  ("xsection",                        6.297),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT800To1200_part2"),
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

samples_2017["/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT1200To2500_part2"),
  ("nof_files",                       31),
  ("nof_db_files",                    551),
  ("nof_events",                      {
    'Count'                                  : [     15214279, ],
    'CountFullWeighted'                      : [     15013601,     15013667,     15014124, ],
    'CountWeighted'                          : [     15013601,     15013667,     15014124, ],
    'CountFullWeightedNoPU'                  : [     15013415, ],
    'CountWeightedNoPU'                      : [     15013415, ],
    'CountWeightedLHEWeightScale'            : [     19230058,     16755307,     14780222,     17234212,     15013601,     13242612,     15617454,     13603646,     11997293, ],
    'CountWeightedLHEWeightScaleNoPU'        : [     19229373,     16754831,     14779590,     17233558,     15013415,     13241975,     15616858,     13602988,     11996722, ],
    'CountFullWeightedLHEWeightScale'        : [     19230058,     16755307,     14780222,     17234212,     15013601,     13242612,     15617454,     13603646,     11997293, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [     19229373,     16754831,     14779590,     17233558,     15013415,     13241975,     15616858,     13602988,     11996722, ],
  }),
  ("nof_tree_events",                 15214279),
  ("nof_db_events",                   20258624),
  ("fsize_local",                     48729796459), # 48.73GB, avg file size 1.57GB
  ("fsize_db",                        1289100671636), # 1.29TB, avg file size 2.34GB
  ("use_it",                          False),
  ("xsection",                        1.262),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT1200To2500_part2"),
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

samples_2017["/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM/part2"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_HT2500ToInf_part2"),
  ("nof_files",                       33),
  ("nof_db_files",                    616),
  ("nof_events",                      {
    'Count'                                  : [     16175651, ],
    'CountFullWeighted'                      : [     15524625,     15523976,     15522990, ],
    'CountWeighted'                          : [     15524625,     15523976,     15522990, ],
    'CountFullWeightedNoPU'                  : [     15523763, ],
    'CountWeightedNoPU'                      : [     15523763, ],
    'CountWeightedLHEWeightScale'            : [     20295374,     17081570,     14608854,     18444249,     15524580,     13276936,     16902668,     14226242,     12167537, ],
    'CountWeightedLHEWeightScaleNoPU'        : [     20295325,     17081337,     14608851,     18444245,     15523763,     13276935,     16902699,     14227038,     12167590, ],
    'CountFullWeightedLHEWeightScale'        : [     20295374,     17081570,     14608854,     18444249,     15524580,     13276936,     16902668,     14226242,     12167537, ],
    'CountFullWeightedLHEWeightScaleNoPU'    : [     20295325,     17081337,     14608851,     18444245,     15523763,     13276935,     16902699,     14227038,     12167590, ],
  }),
  ("nof_tree_events",                 16175651),
  ("nof_db_events",                   21495421),
  ("fsize_local",                     54281856047), # 54.28GB, avg file size 1.64GB
  ("fsize_db",                        1489610697179), # 1.49TB, avg file size 2.42GB
  ("use_it",                          False),
  ("xsection",                        0.009446),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2018Dec22_woPresel_nom_hh_wjets/ntuples/WJetsToLNu_HT2500ToInf_part2"),
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
  [ 'WJetsToLNu_part2',                                'WJetsToLNu_ext_part2',                             ],
  [ 'WJetsToLNu_part1',                                'WJetsToLNu_ext_part1',                             ],
]

