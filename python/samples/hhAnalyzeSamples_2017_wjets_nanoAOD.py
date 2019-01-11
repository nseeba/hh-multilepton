from collections import OrderedDict as OD

# file generated at 2018-12-22 16:54:44 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017_wjets.py -p /hdfs/local/karl/nanoProduction/WJets_split -Z zeroes.txt -z zombies.txt -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_wjets_nanoAOD.py -M

samples_2017 = OD()
samples_2017["/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM/part1"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "EWK"),
  ("process_name_specific",           "WJetsToLNu_part1"),
  ("nof_files",                       168),
  ("nof_db_files",                    514),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 8205539),
  ("nof_db_events",                   33073306),
  ("fsize_local",                     6840648011), # 6.84GB, avg file size 40.72MB
  ("fsize_db",                        1301026785288), # 1.30TB, avg file size 2.53GB
  ("use_it",                          False),
  ("xsection",                        61526.7),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_part1"),
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
  ("nof_files",                       225),
  ("nof_db_files",                    738),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 11157394),
  ("nof_db_events",                   44627200),
  ("fsize_local",                     9297437063), # 9.30GB, avg file size 41.32MB
  ("fsize_db",                        1756207826672), # 1.76TB, avg file size 2.38GB
  ("use_it",                          False),
  ("xsection",                        61526.7),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_ext_part1"),
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
  ("nof_files",                       273),
  ("nof_db_files",                    801),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 13521637),
  ("nof_db_events",                   54147812),
  ("fsize_local",                     12525135991), # 12.53GB, avg file size 45.88MB
  ("fsize_db",                        2175397601720), # 2.18TB, avg file size 2.72GB
  ("use_it",                          False),
  ("xsection",                        9418.44),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/W1JetsToLNu_part1"),
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
  ("nof_files",                       33),
  ("nof_db_files",                    157),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 1628331),
  ("nof_db_events",                   6577492),
  ("fsize_local",                     1775435941), # 1.78GB, avg file size 53.80MB
  ("fsize_db",                        283312015249), # 283.31GB, avg file size 1.80GB
  ("use_it",                          False),
  ("xsection",                        3244.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/W2JetsToLNu_part1"),
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
  ("nof_files",                       99),
  ("nof_db_files",                    250),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 4914826),
  ("nof_db_events",                   19700377),
  ("fsize_local",                     6254295303), # 6.25GB, avg file size 63.17MB
  ("fsize_db",                        868954430671), # 868.95GB, avg file size 3.48GB
  ("use_it",                          False),
  ("xsection",                        1153.02),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/W3JetsToLNu_part1"),
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
  ("nof_files",                       56),
  ("nof_db_files",                    186),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 2797023),
  ("nof_db_events",                   11333705),
  ("fsize_local",                     4429407668), # 4.43GB, avg file size 79.10MB
  ("fsize_db",                        544171543197), # 544.17GB, avg file size 2.93GB
  ("use_it",                          False),
  ("xsection",                        633.05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/W4JetsToLNu_part1"),
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
  ("nof_files",                       180),
  ("nof_db_files",                    735),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 8995404),
  ("nof_db_events",                   35862893),
  ("fsize_local",                     11257280900), # 11.26GB, avg file size 62.54MB
  ("fsize_db",                        1632440553612), # 1.63TB, avg file size 2.22GB
  ("use_it",                          False),
  ("xsection",                        1625.94),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT100To200_part1"),
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
  ("nof_files",                       108),
  ("nof_db_files",                    400),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 5297948),
  ("nof_db_events",                   21250517),
  ("fsize_local",                     8575653801), # 8.58GB, avg file size 79.40MB
  ("fsize_db",                        1058111782457), # 1.06TB, avg file size 2.65GB
  ("use_it",                          False),
  ("xsection",                        477.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT200To400_part1"),
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
  ("nof_files",                       71),
  ("nof_db_files",                    314),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 3525798),
  ("nof_db_events",                   14313274),
  ("fsize_local",                     7300928540), # 7.30GB, avg file size 102.83MB
  ("fsize_db",                        780224610750), # 780.22GB, avg file size 2.48GB
  ("use_it",                          False),
  ("xsection",                        67.51),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT400To600_part1"),
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
  ("nof_files",                       109),
  ("nof_db_files",                    488),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 5402228),
  ("nof_db_events",                   21709087),
  ("fsize_local",                     12341049480), # 12.34GB, avg file size 113.22MB
  ("fsize_db",                        1256446599197), # 1.26TB, avg file size 2.57GB
  ("use_it",                          False),
  ("xsection",                        15.09),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT600To800_part1"),
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
  ("nof_files",                       102),
  ("nof_db_files",                    487),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 5094340),
  ("nof_db_events",                   20432728),
  ("fsize_local",                     12325113489), # 12.33GB, avg file size 120.83MB
  ("fsize_db",                        1225597665572), # 1.23TB, avg file size 2.52GB
  ("use_it",                          False),
  ("xsection",                        6.297),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT800To1200_part1"),
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
  ("nof_files",                       101),
  ("nof_db_files",                    551),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 5044345),
  ("nof_db_events",                   20258624),
  ("fsize_local",                     12864498629), # 12.86GB, avg file size 127.37MB
  ("fsize_db",                        1289100671636), # 1.29TB, avg file size 2.34GB
  ("use_it",                          False),
  ("xsection",                        1.262),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT1200To2500_part1"),
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
  ("nof_files",                       107),
  ("nof_db_files",                    616),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 5319770),
  ("nof_db_events",                   21495421),
  ("fsize_local",                     14566575018), # 14.57GB, avg file size 136.14MB
  ("fsize_db",                        1489610697179), # 1.49TB, avg file size 2.42GB
  ("use_it",                          False),
  ("xsection",                        0.009446),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT2500ToInf_part1"),
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
  ("nof_files",                       507),
  ("nof_db_files",                    514),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 24867767),
  ("nof_db_events",                   33073306),
  ("fsize_local",                     20728027001), # 20.73GB, avg file size 40.88MB
  ("fsize_db",                        1301026785288), # 1.30TB, avg file size 2.53GB
  ("use_it",                          False),
  ("xsection",                        61526.7),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_part2"),
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
  ("nof_files",                       675),
  ("nof_db_files",                    738),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 33469806),
  ("nof_db_events",                   44627200),
  ("fsize_local",                     27893788975), # 27.89GB, avg file size 41.32MB
  ("fsize_db",                        1756207826672), # 1.76TB, avg file size 2.38GB
  ("use_it",                          False),
  ("xsection",                        61526.7),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_ext_part2"),
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
  ("nof_files",                       821),
  ("nof_db_files",                    801),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 40626175),
  ("nof_db_events",                   54147812),
  ("fsize_local",                     37633758092), # 37.63GB, avg file size 45.84MB
  ("fsize_db",                        2175397601720), # 2.18TB, avg file size 2.72GB
  ("use_it",                          False),
  ("xsection",                        9418.44),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/W1JetsToLNu_part2"),
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
  ("nof_files",                       101),
  ("nof_db_files",                    157),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 4949161),
  ("nof_db_events",                   6577492),
  ("fsize_local",                     5398687261), # 5.40GB, avg file size 53.45MB
  ("fsize_db",                        283312015249), # 283.31GB, avg file size 1.80GB
  ("use_it",                          False),
  ("xsection",                        3244.85),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/W2JetsToLNu_part2"),
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
  ("nof_files",                       298),
  ("nof_db_files",                    250),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 14785551),
  ("nof_db_events",                   19700377),
  ("fsize_local",                     18816301179), # 18.82GB, avg file size 63.14MB
  ("fsize_db",                        868954430671), # 868.95GB, avg file size 3.48GB
  ("use_it",                          False),
  ("xsection",                        1153.02),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/W3JetsToLNu_part2"),
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
  ("nof_files",                       171),
  ("nof_db_files",                    186),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 8536682),
  ("nof_db_events",                   11333705),
  ("fsize_local",                     13541296037), # 13.54GB, avg file size 79.19MB
  ("fsize_db",                        544171543197), # 544.17GB, avg file size 2.93GB
  ("use_it",                          False),
  ("xsection",                        633.05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/W4JetsToLNu_part2"),
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
  ("nof_files",                       540),
  ("nof_db_files",                    735),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 26867489),
  ("nof_db_events",                   35862893),
  ("fsize_local",                     33630526269), # 33.63GB, avg file size 62.28MB
  ("fsize_db",                        1632440553612), # 1.63TB, avg file size 2.22GB
  ("use_it",                          False),
  ("xsection",                        1625.94),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT100To200_part2"),
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
  ("nof_files",                       327),
  ("nof_db_files",                    400),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 15952569),
  ("nof_db_events",                   21250517),
  ("fsize_local",                     25829131223), # 25.83GB, avg file size 78.99MB
  ("fsize_db",                        1058111782457), # 1.06TB, avg file size 2.65GB
  ("use_it",                          False),
  ("xsection",                        477.52),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT200To400_part2"),
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
  ("nof_files",                       216),
  ("nof_db_files",                    314),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 10787476),
  ("nof_db_events",                   14313274),
  ("fsize_local",                     22333003503), # 22.33GB, avg file size 103.39MB
  ("fsize_db",                        780224610750), # 780.22GB, avg file size 2.48GB
  ("use_it",                          False),
  ("xsection",                        67.51),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT400To600_part2"),
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
  ("nof_files",                       327),
  ("nof_db_files",                    488),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 16306859),
  ("nof_db_events",                   21709087),
  ("fsize_local",                     37247884755), # 37.25GB, avg file size 113.91MB
  ("fsize_db",                        1256446599197), # 1.26TB, avg file size 2.57GB
  ("use_it",                          False),
  ("xsection",                        15.09),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT600To800_part2"),
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
  ("nof_files",                       309),
  ("nof_db_files",                    487),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 15372352),
  ("nof_db_events",                   20432728),
  ("fsize_local",                     37198464718), # 37.20GB, avg file size 120.38MB
  ("fsize_db",                        1225597665572), # 1.23TB, avg file size 2.52GB
  ("use_it",                          False),
  ("xsection",                        6.297),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT800To1200_part2"),
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
  ("nof_files",                       305),
  ("nof_db_files",                    551),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 15214279),
  ("nof_db_events",                   20258624),
  ("fsize_local",                     38803927300), # 38.80GB, avg file size 127.23MB
  ("fsize_db",                        1289100671636), # 1.29TB, avg file size 2.34GB
  ("use_it",                          False),
  ("xsection",                        1.262),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT1200To2500_part2"),
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
  ("nof_files",                       324),
  ("nof_db_files",                    616),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 16175651),
  ("nof_db_events",                   21495421),
  ("fsize_local",                     44291508854), # 44.29GB, avg file size 136.70MB
  ("fsize_db",                        1489610697179), # 1.49TB, avg file size 2.42GB
  ("use_it",                          False),
  ("xsection",                        0.009446),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/nanoProduction/WJets_split/WJetsToLNu_HT2500ToInf_part2"),
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

