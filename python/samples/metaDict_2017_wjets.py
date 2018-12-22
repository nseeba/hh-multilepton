from collections import OrderedDict as OD

# file generated at 2018-12-22 16:23:51 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets_wjets_2017.txt -m python/samples/metaDict_2017_wjets.py -s ../../tthAnalysis/NanoAOD/test/datasets_sum_2017_wjets.txt -c /hdfs/local/karl/nanoProduction/WJets_split

meta_dictionary = OD()


### event sums

sum_events = { 
  ("WJetsToLNu_part1", "WJetsToLNu_ext_part1"),
  ("WJetsToLNu_part2", "WJetsToLNu_ext_part2"),
}


meta_dictionary["/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM/part1"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_part1"),
  ("nof_db_events",         33073306),
  ("nof_db_files",          514),
  ("fsize_db",              1301026785288),
  ("xsection",              61526.7),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.30TB; nevents: 33.07M; release: 9_4_6_patch1; last modified: 2018-08-17 01:17:04"),
])

meta_dictionary["/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM/part1"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_ext_part1"),
  ("nof_db_events",         44627200),
  ("nof_db_files",          738),
  ("fsize_db",              1756207826672),
  ("xsection",              61526.7),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.76TB; nevents: 44.63M; release: 9_4_6_patch1; last modified: 2018-07-26 02:31:57"),
])

meta_dictionary["/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM/part1"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "W1JetsToLNu_part1"),
  ("nof_db_events",         54147812),
  ("nof_db_files",          801),
  ("fsize_db",              2175397601720),
  ("xsection",              9418.44),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 2.18TB; nevents: 54.15M; release: 9_4_6_patch1; last modified: 2018-08-24 10:17:33"),
])

meta_dictionary["/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4/MINIAODSIM/part1"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "W2JetsToLNu_part1"),
  ("nof_db_events",         6577492),
  ("nof_db_files",          157),
  ("fsize_db",              283312015249),
  ("xsection",              3244.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 283.31GB; nevents: 6.58M; release: 9_4_6_patch1; last modified: 2018-08-05 18:44:31"),
])

meta_dictionary["/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "W3JetsToLNu_part1"),
  ("nof_db_events",         19700377),
  ("nof_db_files",          250),
  ("fsize_db",              868954430671),
  ("xsection",              1153.02),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 868.95GB; nevents: 19.70M; release: 9_4_6_patch1; last modified: 2018-04-20 18:55:18"),
])

meta_dictionary["/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "W4JetsToLNu_part1"),
  ("nof_db_events",         11333705),
  ("nof_db_files",          186),
  ("fsize_db",              544171543197),
  ("xsection",              633.05),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 544.17GB; nevents: 11.33M; release: 9_4_6_patch1; last modified: 2018-04-21 04:46:56"),
])

meta_dictionary["/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM/part1"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT100To200_part1"),
  ("nof_db_events",         35862893),
  ("nof_db_files",          735),
  ("fsize_db",              1632440553612),
  ("xsection",              1625.94),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.63TB; nevents: 35.86M; release: 9_4_6_patch1; last modified: 2018-07-16 22:47:23"),
])

meta_dictionary["/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT200To400_part1"),
  ("nof_db_events",         21250517),
  ("nof_db_files",          400),
  ("fsize_db",              1058111782457),
  ("xsection",              477.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.06TB; nevents: 21.25M; release: 9_4_6_patch1; last modified: 2018-06-11 22:53:32"),
])

meta_dictionary["/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT400To600_part1"),
  ("nof_db_events",         14313274),
  ("nof_db_files",          314),
  ("fsize_db",              780224610750),
  ("xsection",              67.51),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 780.22GB; nevents: 14.31M; release: 9_4_6_patch1; last modified: 2018-05-28 05:52:21"),
])

meta_dictionary["/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT600To800_part1"),
  ("nof_db_events",         21709087),
  ("nof_db_files",          488),
  ("fsize_db",              1256446599197),
  ("xsection",              15.09),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.26TB; nevents: 21.71M; release: 9_4_6_patch1; last modified: 2018-06-17 00:32:54"),
])

meta_dictionary["/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT800To1200_part1"),
  ("nof_db_events",         20432728),
  ("nof_db_files",          487),
  ("fsize_db",              1225597665572),
  ("xsection",              6.297),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.23TB; nevents: 20.43M; release: 9_4_6_patch1; last modified: 2018-06-26 12:59:36"),
])

meta_dictionary["/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part1"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT1200To2500_part1"),
  ("nof_db_events",         20258624),
  ("nof_db_files",          551),
  ("fsize_db",              1289100671636),
  ("xsection",              1.262),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.29TB; nevents: 20.26M; release: 9_4_6_patch1; last modified: 2018-06-25 05:52:24"),
])

meta_dictionary["/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM/part1"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT2500ToInf_part1"),
  ("nof_db_events",         21495421),
  ("nof_db_files",          616),
  ("fsize_db",              1489610697179),
  ("xsection",              0.009446),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.49TB; nevents: 21.50M; release: 9_4_6_patch1; last modified: 2018-07-06 12:31:23"),
])

meta_dictionary["/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM/part2"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_part2"),
  ("nof_db_events",         33073306),
  ("nof_db_files",          514),
  ("fsize_db",              1301026785288),
  ("xsection",              61526.7),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.30TB; nevents: 33.07M; release: 9_4_6_patch1; last modified: 2018-08-17 01:17:04"),
])

meta_dictionary["/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14_ext1-v2/MINIAODSIM/part2"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_ext_part2"),
  ("nof_db_events",         44627200),
  ("nof_db_files",          738),
  ("fsize_db",              1756207826672),
  ("xsection",              61526.7),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.76TB; nevents: 44.63M; release: 9_4_6_patch1; last modified: 2018-07-26 02:31:57"),
])

meta_dictionary["/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM/part2"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "W1JetsToLNu_part2"),
  ("nof_db_events",         54147812),
  ("nof_db_files",          801),
  ("fsize_db",              2175397601720),
  ("xsection",              9418.44),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 2.18TB; nevents: 54.15M; release: 9_4_6_patch1; last modified: 2018-08-24 10:17:33"),
])

meta_dictionary["/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4/MINIAODSIM/part2"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "W2JetsToLNu_part2"),
  ("nof_db_events",         6577492),
  ("nof_db_files",          157),
  ("fsize_db",              283312015249),
  ("xsection",              3244.85),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 283.31GB; nevents: 6.58M; release: 9_4_6_patch1; last modified: 2018-08-05 18:44:31"),
])

meta_dictionary["/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "W3JetsToLNu_part2"),
  ("nof_db_events",         19700377),
  ("nof_db_files",          250),
  ("fsize_db",              868954430671),
  ("xsection",              1153.02),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 868.95GB; nevents: 19.70M; release: 9_4_6_patch1; last modified: 2018-04-20 18:55:18"),
])

meta_dictionary["/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "W4JetsToLNu_part2"),
  ("nof_db_events",         11333705),
  ("nof_db_files",          186),
  ("fsize_db",              544171543197),
  ("xsection",              633.05),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 544.17GB; nevents: 11.33M; release: 9_4_6_patch1; last modified: 2018-04-21 04:46:56"),
])

meta_dictionary["/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM/part2"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT100To200_part2"),
  ("nof_db_events",         35862893),
  ("nof_db_files",          735),
  ("fsize_db",              1632440553612),
  ("xsection",              1625.94),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.63TB; nevents: 35.86M; release: 9_4_6_patch1; last modified: 2018-07-16 22:47:23"),
])

meta_dictionary["/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT200To400_part2"),
  ("nof_db_events",         21250517),
  ("nof_db_files",          400),
  ("fsize_db",              1058111782457),
  ("xsection",              477.52),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.06TB; nevents: 21.25M; release: 9_4_6_patch1; last modified: 2018-06-11 22:53:32"),
])

meta_dictionary["/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT400To600_part2"),
  ("nof_db_events",         14313274),
  ("nof_db_files",          314),
  ("fsize_db",              780224610750),
  ("xsection",              67.51),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 780.22GB; nevents: 14.31M; release: 9_4_6_patch1; last modified: 2018-05-28 05:52:21"),
])

meta_dictionary["/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT600To800_part2"),
  ("nof_db_events",         21709087),
  ("nof_db_files",          488),
  ("fsize_db",              1256446599197),
  ("xsection",              15.09),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.26TB; nevents: 21.71M; release: 9_4_6_patch1; last modified: 2018-06-17 00:32:54"),
])

meta_dictionary["/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT800To1200_part2"),
  ("nof_db_events",         20432728),
  ("nof_db_files",          487),
  ("fsize_db",              1225597665572),
  ("xsection",              6.297),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.23TB; nevents: 20.43M; release: 9_4_6_patch1; last modified: 2018-06-26 12:59:36"),
])

meta_dictionary["/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM/part2"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT1200To2500_part2"),
  ("nof_db_events",         20258624),
  ("nof_db_files",          551),
  ("fsize_db",              1289100671636),
  ("xsection",              1.262),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.29TB; nevents: 20.26M; release: 9_4_6_patch1; last modified: 2018-06-25 05:52:24"),
])

meta_dictionary["/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/MINIAODSIM/part2"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "EWK"),
  ("process_name_specific", "WJetsToLNu_HT2500ToInf_part2"),
  ("nof_db_events",         21495421),
  ("nof_db_files",          616),
  ("fsize_db",              1489610697179),
  ("xsection",              0.009446),
  ("use_it",                False),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 1.49TB; nevents: 21.50M; release: 9_4_6_patch1; last modified: 2018-07-06 12:31:23"),
])


# event statistics by sample category:
# EWK: 649.56M

