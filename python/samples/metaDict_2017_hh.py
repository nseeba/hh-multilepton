from collections import OrderedDict as OD

# file generated at 2019-07-09 20:41:31 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_hh_multilepton_mc_2017_RunIIFall17MiniAODv2.txt -m python/samples/metaDict_2017_hh.py -s ../../tthAnalysis/NanoAOD/test/datasets/txt/sum_datasets_hh_multilepton_2017_RunIIFall17MiniAODv2.txt -c python/samples/sampleLocations_2017_nanoAOD_hh_multilepton.txt

meta_dictionary = OD()


### event sums

sum_events = { 
  ("signal_ggf_nonresonant_node_sm_hh_4v", "signal_ggf_nonresonant_node_2_hh_4v", "signal_ggf_nonresonant_node_3_hh_4v", "signal_ggf_nonresonant_node_4_hh_4v", "signal_ggf_nonresonant_node_5_hh_4v", "signal_ggf_nonresonant_node_6_hh_4v", "signal_ggf_nonresonant_node_7_hh_4v", "signal_ggf_nonresonant_node_8_hh_4v", "signal_ggf_nonresonant_node_9_hh_4v", "signal_ggf_nonresonant_node_10_hh_4v", "signal_ggf_nonresonant_node_11_hh_4v", "signal_ggf_nonresonant_node_12_hh_4v"),
  ("signal_ggf_nonresonant_node_sm_hh_2v2t", "signal_ggf_nonresonant_node_2_hh_2v2t", "signal_ggf_nonresonant_node_3_hh_2v2t", "signal_ggf_nonresonant_node_4_hh_2v2t", "signal_ggf_nonresonant_node_5_hh_2v2t", "signal_ggf_nonresonant_node_6_hh_2v2t", "signal_ggf_nonresonant_node_7_hh_2v2t", "signal_ggf_nonresonant_node_8_hh_2v2t", "signal_ggf_nonresonant_node_9_hh_2v2t", "signal_ggf_nonresonant_node_10_hh_2v2t", "signal_ggf_nonresonant_node_11_hh_2v2t", "signal_ggf_nonresonant_node_12_hh_2v2t"),
  ("signal_ggf_nonresonant_node_sm_hh_4t", "signal_ggf_nonresonant_node_2_hh_4t", "signal_ggf_nonresonant_node_3_hh_4t", "signal_ggf_nonresonant_node_7_hh_4t", "signal_ggf_nonresonant_node_9_hh_4t", "signal_ggf_nonresonant_node_12_hh_4t"),
}


meta_dictionary["/GluGluToRadionToHHTo4Tau_M-250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-250_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_250_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_250_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          17),
  ("fsize_db",              20114964479),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.11GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-07 00:33:14"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-260_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-260_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_260_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          16),
  ("fsize_db",              19104985604),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.10GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-04 12:15:56"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-270_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-270_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_270_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_4t"),
  ("nof_db_events",         385000),
  ("nof_db_files",          16),
  ("fsize_db",              18511645006),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 18.51GB; nevents: 385.00k; release: 9_4_7; last modified: 2018-10-07 19:38:27"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-280_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-280_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_280_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_280_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          21),
  ("fsize_db",              20219319064),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.22GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-15 04:28:04"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-300_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_300_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          17),
  ("fsize_db",              14610494649),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.61GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-04 16:58:26"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-350_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_350_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_4t"),
  ("nof_db_events",         284000),
  ("nof_db_files",          20),
  ("fsize_db",              14267271177),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.27GB; nevents: 284.00k; release: 9_4_7; last modified: 2018-10-05 15:58:40"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-400_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_400_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          15),
  ("fsize_db",              15112224162),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.11GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-08 08:46:46"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-450_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-450_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_450_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          13),
  ("fsize_db",              15314286391),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.31GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-06 15:09:59"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-500_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_500_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          10),
  ("fsize_db",              10307241524),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.31GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-15 04:27:17"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-550_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-550_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_550_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              10435371711),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.44GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-15 04:42:35"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-600_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-600_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_600_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          13),
  ("fsize_db",              10556003606),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.56GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-07 08:59:45"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-650_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-650_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_650_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          15),
  ("fsize_db",              10638007613),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.64GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-07 10:46:20"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-700_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-700_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_700_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_700_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          13),
  ("fsize_db",              10705047349),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.71GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-04 12:15:36"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-750_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_750_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              11200569052),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.20GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-05 06:36:12"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-800_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-800_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_800_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          10),
  ("fsize_db",              11266991203),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.27GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-05 16:04:52"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-850_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-850_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_850_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_850_hh_4t"),
  ("nof_db_events",         192000),
  ("nof_db_files",          11),
  ("fsize_db",              10933218336),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.93GB; nevents: 192.00k; release: 9_4_7; last modified: 2018-10-06 03:12:10"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-900_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-900_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_900_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          6),
  ("fsize_db",              5507575850),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.51GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-07 00:27:04"),
])

meta_dictionary["/GluGluToRadionToHHTo4Tau_M-1000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4Tau_M-1000_narrow_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          4),
  ("fsize_db",              5537065038),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.54GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-07 00:32:36"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4Tau_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_250_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_250_hh_4t"),
  ("nof_db_events",         391000),
  ("nof_db_files",          18),
  ("fsize_db",              18879671024),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 18.88GB; nevents: 391.00k; release: 9_4_7; last modified: 2018-09-21 02:54:58"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4Tau_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_260_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_4t"),
  ("nof_db_events",         386000),
  ("nof_db_files",          26),
  ("fsize_db",              18925798715),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 18.93GB; nevents: 386.00k; release: 9_4_7; last modified: 2018-10-13 05:53:43"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo4Tau_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_270_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_4t"),
  ("nof_db_events",         380000),
  ("nof_db_files",          26),
  ("fsize_db",              18931125504),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 18.93GB; nevents: 380.00k; release: 9_4_7; last modified: 2018-10-17 12:32:44"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4Tau_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_280_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_280_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          30),
  ("fsize_db",              19706361148),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.71GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-18 02:53:32"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo4Tau_M-300_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_300_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          26),
  ("fsize_db",              20098276225),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.10GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-15 04:45:03"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo4Tau_M-320_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_320_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_320_hh_4t"),
  ("nof_db_events",         298000),
  ("nof_db_files",          20),
  ("fsize_db",              15176832017),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.18GB; nevents: 298.00k; release: 9_4_7; last modified: 2019-03-31 18:01:21"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo4Tau_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_350_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_4t"),
  ("nof_db_events",         384000),
  ("nof_db_files",          18),
  ("fsize_db",              19349982170),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.35GB; nevents: 384.00k; release: 9_4_7; last modified: 2018-10-07 19:35:30"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4Tau_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_400_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          18),
  ("fsize_db",              15427844934),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.43GB; nevents: 300.00k; release: 9_4_7; last modified: 2018-10-15 07:06:03"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4Tau_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_450_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_4t"),
  ("nof_db_events",         280000),
  ("nof_db_files",          23),
  ("fsize_db",              14667839164),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.67GB; nevents: 280.00k; release: 9_4_7; last modified: 2018-10-17 12:25:47"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4Tau_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_500_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_4t"),
  ("nof_db_events",         284000),
  ("nof_db_files",          22),
  ("fsize_db",              15248320207),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.25GB; nevents: 284.00k; release: 9_4_7; last modified: 2019-02-21 02:43:27"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4Tau_M-550_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_550_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          20),
  ("fsize_db",              10729026481),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.73GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-17 12:59:28"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4Tau_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_600_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_4t"),
  ("nof_db_events",         198000),
  ("nof_db_files",          18),
  ("fsize_db",              10881260447),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.88GB; nevents: 198.00k; release: 9_4_7; last modified: 2018-10-13 06:01:27"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo4Tau_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_650_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          18),
  ("fsize_db",              10995288880),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.00GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-15 04:58:31"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4Tau_M-700_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_700_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_700_hh_4t"),
  ("nof_db_events",         189000),
  ("nof_db_files",          20),
  ("fsize_db",              10562893577),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.56GB; nevents: 189.00k; release: 9_4_7; last modified: 2018-10-17 12:38:36"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo4Tau_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_750_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_750_hh_4t"),
  ("nof_db_events",         196000),
  ("nof_db_files",          26),
  ("fsize_db",              11128480225),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.13GB; nevents: 196.00k; release: 9_4_7; last modified: 2018-10-13 06:13:15"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo4Tau_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_800_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          24),
  ("fsize_db",              11297900227),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.30GB; nevents: 200.00k; release: 9_4_7; last modified: 2018-10-17 12:14:08"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4Tau_M-850_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_850_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_850_hh_4t"),
  ("nof_db_events",         194000),
  ("nof_db_files",          16),
  ("fsize_db",              11268378526),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.27GB; nevents: 194.00k; release: 9_4_7; last modified: 2019-04-07 02:09:25"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo4Tau_M-900_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-"),
  ("sample_category",       "signal_ggf_spin2_900_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_900_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          13),
  ("fsize_db",              5743750248),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.74GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-18 02:19:56"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo4Tau_M-1000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14"),
  ("sample_category",       "signal_ggf_spin2_1000_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_1000_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          19),
  ("fsize_db",              5923175401),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.92GB; nevents: 100.00k; release: 9_4_7; last modified: 2018-10-15 05:35:32"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToRadionToHHTo2V2Tau_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_250_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_250_hh_2v2t"),
  ("nof_db_events",         399997),
  ("nof_db_files",          19),
  ("fsize_db",              20344351713),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.34GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-23 17:13:36"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToRadionToHHTo2V2Tau_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_260_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_2v2t"),
  ("nof_db_events",         399993),
  ("nof_db_files",          16),
  ("fsize_db",              19527920598),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.53GB; nevents: 399.99k; release: 9_4_7; last modified: 2019-03-16 09:59:03"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToRadionToHHTo2V2Tau_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_270_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_2v2t"),
  ("nof_db_events",         399995),
  ("nof_db_files",          18),
  ("fsize_db",              19473148919),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.47GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-16 17:37:41"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToRadionToHHTo2V2Tau_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_280_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_280_hh_2v2t"),
  ("nof_db_events",         379996),
  ("nof_db_files",          27),
  ("fsize_db",              19590423166),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.59GB; nevents: 380.00k; release: 9_4_7; last modified: 2019-03-16 22:22:46"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToRadionToHHTo2V2Tau_M-300_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_300_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_2v2t"),
  ("nof_db_events",         299994),
  ("nof_db_files",          18),
  ("fsize_db",              14916149163),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.92GB; nevents: 299.99k; release: 9_4_7; last modified: 2019-03-04 08:52:20"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToRadionToHHTo2V2Tau_M-320_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_320_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_320_hh_2v2t"),
  ("nof_db_events",         299998),
  ("nof_db_files",          14),
  ("fsize_db",              14997791200),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.00GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-03-13 17:04:54"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToRadionToHHTo2V2Tau_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_350_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_2v2t"),
  ("nof_db_events",         299990),
  ("nof_db_files",          16),
  ("fsize_db",              15235183188),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.24GB; nevents: 299.99k; release: 9_4_7; last modified: 2019-03-11 10:06:19"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToRadionToHHTo2V2Tau_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_400_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_2v2t"),
  ("nof_db_events",         286992),
  ("nof_db_files",          14),
  ("fsize_db",              14884438376),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.88GB; nevents: 286.99k; release: 9_4_7; last modified: 2019-03-16 09:50:17"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToRadionToHHTo2V2Tau_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_450_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_2v2t"),
  ("nof_db_events",         291993),
  ("nof_db_files",          17),
  ("fsize_db",              15416817462),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.42GB; nevents: 291.99k; release: 9_4_7; last modified: 2019-03-12 20:44:40"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToRadionToHHTo2V2Tau_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_500_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_2v2t"),
  ("nof_db_events",         269995),
  ("nof_db_files",          18),
  ("fsize_db",              14437624405),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.44GB; nevents: 270.00k; release: 9_4_7; last modified: 2019-03-18 20:00:55"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo2V2Tau_M-550_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_550_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_2v2t"),
  ("nof_db_events",         299996),
  ("nof_db_files",          17),
  ("fsize_db",              16219407866),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.22GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-03-20 23:51:08"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToRadionToHHTo2V2Tau_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "signal_ggf_spin0_600_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_2v2t"),
  ("nof_db_events",         195995),
  ("nof_db_files",          12),
  ("fsize_db",              10725957373),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.73GB; nevents: 196.00k; release: 9_4_7; last modified: 2019-04-01 07:39:54"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToRadionToHHTo2V2Tau_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_650_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_2v2t"),
  ("nof_db_events",         199995),
  ("nof_db_files",          10),
  ("fsize_db",              11039880992),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.04GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-11 15:01:30"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun26_GluGluToRadionToHHTo2V2Tau_M-700_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_700_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_700_hh_2v2t"),
  ("nof_db_events",         191997),
  ("nof_db_files",          14),
  ("fsize_db",              10772500407),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 10.77GB; nevents: 192.00k; release: 9_4_7; last modified: 2019-03-16 13:37:30"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun26_GluGluToRadionToHHTo2V2Tau_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_750_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_2v2t"),
  ("nof_db_events",         199998),
  ("nof_db_files",          14),
  ("fsize_db",              11660934047),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.66GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-11 16:47:10"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo2V2Tau_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_800_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_2v2t"),
  ("nof_db_events",         199999),
  ("nof_db_files",          17),
  ("fsize_db",              11774979133),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.77GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-11 15:02:00"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "signal_ggf_spin0_850_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_850_hh_2v2t"),
  ("nof_db_events",         191996),
  ("nof_db_files",          12),
  ("fsize_db",              11335819766),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.34GB; nevents: 192.00k; release: 9_4_7; last modified: 2019-03-10 20:18:51"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo2V2Tau_M-900_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_900_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_2v2t"),
  ("nof_db_events",         199997),
  ("nof_db_files",          9),
  ("fsize_db",              11421628490),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.42GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-08 09:27:21"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToRadionToHHTo2V2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_2v2t"),
  ("nof_db_events",         99998),
  ("nof_db_files",          7),
  ("fsize_db",              5783738671),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.78GB; nevents: 100.00k; release: 9_4_7; last modified: 2019-03-07 02:52:45"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo2V2Tau_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_250_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_250_hh_2v2t"),
  ("nof_db_events",         394995),
  ("nof_db_files",          9),
  ("fsize_db",              19490651554),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.49GB; nevents: 395.00k; release: 9_4_7; last modified: 2019-05-03 23:36:31"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo2V2Tau_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_260_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_2v2t"),
  ("nof_db_events",         395995),
  ("nof_db_files",          21),
  ("fsize_db",              19808318644),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.81GB; nevents: 396.00k; release: 9_4_7; last modified: 2019-03-15 02:06:50"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "signal_ggf_spin2_270_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_2v2t"),
  ("nof_db_events",         399996),
  ("nof_db_files",          19),
  ("fsize_db",              19945565524),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.95GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-04 10:35:16"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo2V2Tau_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_280_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_280_hh_2v2t"),
  ("nof_db_events",         394995),
  ("nof_db_files",          24),
  ("fsize_db",              19924344376),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.92GB; nevents: 395.00k; release: 9_4_7; last modified: 2019-03-12 20:46:16"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo2V2Tau_M-300_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_300_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_2v2t"),
  ("nof_db_events",         299995),
  ("nof_db_files",          20),
  ("fsize_db",              15226334046),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.23GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-03-14 08:08:47"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo2V2Tau_M-320_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_320_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_320_hh_2v2t"),
  ("nof_db_events",         284992),
  ("nof_db_files",          12),
  ("fsize_db",              14565597893),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 14.57GB; nevents: 284.99k; release: 9_4_7; last modified: 2019-03-15 08:55:22"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo2V2Tau_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_350_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_2v2t"),
  ("nof_db_events",         299995),
  ("nof_db_files",          17),
  ("fsize_db",              15709690748),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.71GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-03-15 02:11:19"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo2V2Tau_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_400_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_2v2t"),
  ("nof_db_events",         289998),
  ("nof_db_files",          14),
  ("fsize_db",              15476703995),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.48GB; nevents: 290.00k; release: 9_4_7; last modified: 2019-03-13 20:40:21"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo2V2Tau_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_450_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_2v2t"),
  ("nof_db_events",         279993),
  ("nof_db_files",          14),
  ("fsize_db",              15200236312),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.20GB; nevents: 279.99k; release: 9_4_7; last modified: 2019-03-18 20:02:05"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo2V2Tau_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_500_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_2v2t"),
  ("nof_db_events",         199997),
  ("nof_db_files",          13),
  ("fsize_db",              11038820268),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.04GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-12 20:46:07"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo2V2Tau_M-550_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_550_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_2v2t"),
  ("nof_db_events",         199995),
  ("nof_db_files",          14),
  ("fsize_db",              11235761543),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.24GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-11 04:57:17"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo2V2Tau_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_600_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_2v2t"),
  ("nof_db_events",         199996),
  ("nof_db_files",          14),
  ("fsize_db",              11265507117),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.27GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-12 20:36:49"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo2V2Tau_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_650_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_2v2t"),
  ("nof_db_events",         195999),
  ("nof_db_files",          11),
  ("fsize_db",              11148852408),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.15GB; nevents: 196.00k; release: 9_4_7; last modified: 2019-03-11 06:53:08"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo2V2Tau_M-700_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_700_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_700_hh_2v2t"),
  ("nof_db_events",         195997),
  ("nof_db_files",          18),
  ("fsize_db",              11274075929),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.27GB; nevents: 196.00k; release: 9_4_7; last modified: 2019-03-14 16:55:24"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo2V2Tau_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_750_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_750_hh_2v2t"),
  ("nof_db_events",         199999),
  ("nof_db_files",          6),
  ("fsize_db",              11369615851),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.37GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-07 05:54:49"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo2V2Tau_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_800_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_2v2t"),
  ("nof_db_events",         199998),
  ("nof_db_files",          10),
  ("fsize_db",              11488159001),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.49GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-14 14:03:02"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jul07_GluGluToBulkGravitonToHHTo2V2Tau_M-850_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_850_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_850_hh_2v2t"),
  ("nof_db_events",         191995),
  ("nof_db_files",          11),
  ("fsize_db",              11613877178),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.61GB; nevents: 192.00k; release: 9_4_7; last modified: 2019-03-22 09:58:47"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo2V2Tau_M-900_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v1"),
  ("sample_category",       "signal_ggf_spin2_900_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_900_hh_2v2t"),
  ("nof_db_events",         99999),
  ("nof_db_files",          10),
  ("fsize_db",              5984452524),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.98GB; nevents: 100.00k; release: 9_4_7; last modified: 2019-03-11 21:40:18"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo2V2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_1000_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_1000_hh_2v2t"),
  ("nof_db_events",         99999),
  ("nof_db_files",          5),
  ("fsize_db",              5974953438),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.97GB; nevents: 100.00k; release: 9_4_7; last modified: 2019-03-11 03:38:15"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_250_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_250_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          14),
  ("fsize_db",              20459339723),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.46GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-14 09:52:36"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_260_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_4v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          18),
  ("fsize_db",              19550516838),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.55GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-13 02:59:43"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_270_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_4v"),
  ("nof_db_events",         386000),
  ("nof_db_files",          16),
  ("fsize_db",              18992366194),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 18.99GB; nevents: 386.00k; release: 9_4_7; last modified: 2019-03-13 20:44:46"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_280_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_280_hh_4v"),
  ("nof_db_events",         388998),
  ("nof_db_files",          23),
  ("fsize_db",              20249921988),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.25GB; nevents: 389.00k; release: 9_4_7; last modified: 2019-03-11 10:04:54"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-300_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_300_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_4v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          16),
  ("fsize_db",              15102940723),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.10GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-03-13 02:58:52"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-320_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_320_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_320_hh_4v"),
  ("nof_db_events",         299998),
  ("nof_db_files",          14),
  ("fsize_db",              15313788135),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.31GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-03-11 06:49:53"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_350_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_4v"),
  ("nof_db_events",         291998),
  ("nof_db_files",          13),
  ("fsize_db",              15117730207),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.12GB; nevents: 292.00k; release: 9_4_7; last modified: 2019-03-14 20:21:35"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_400_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_4v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          20),
  ("fsize_db",              15994431220),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.99GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-03-13 20:39:39"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_450_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_4v"),
  ("nof_db_events",         292000),
  ("nof_db_files",          21),
  ("fsize_db",              15872838181),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.87GB; nevents: 292.00k; release: 9_4_7; last modified: 2019-03-16 05:47:35"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_500_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_4v"),
  ("nof_db_events",         299997),
  ("nof_db_files",          14),
  ("fsize_db",              16481520657),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.48GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-03-13 04:47:53"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-550_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_550_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_4v"),
  ("nof_db_events",         299998),
  ("nof_db_files",          14),
  ("fsize_db",              16709110067),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.71GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-03-10 20:18:40"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_600_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_4v"),
  ("nof_db_events",         195999),
  ("nof_db_files",          10),
  ("fsize_db",              11098413315),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.10GB; nevents: 196.00k; release: 9_4_7; last modified: 2019-03-12 21:44:13"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_650_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_4v"),
  ("nof_db_events",         199999),
  ("nof_db_files",          14),
  ("fsize_db",              11471924888),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.47GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-27 00:26:57"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-700_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_700_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_700_hh_4v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          15),
  ("fsize_db",              11589915708),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.59GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-14 16:59:07"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_750_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_4v"),
  ("nof_db_events",         192000),
  ("nof_db_files",          12),
  ("fsize_db",              11585622017),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.59GB; nevents: 192.00k; release: 9_4_7; last modified: 2019-03-11 03:38:48"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_800_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_4v"),
  ("nof_db_events",         199997),
  ("nof_db_files",          8),
  ("fsize_db",              12059647437),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 12.06GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-08 17:40:59"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-850_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_850_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_850_hh_4v"),
  ("nof_db_events",         199999),
  ("nof_db_files",          10),
  ("fsize_db",              12157898020),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 12.16GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-10 21:32:56"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-900_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin0_900_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_4v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          16),
  ("fsize_db",              11885543228),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.89GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-11 03:38:58"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToRadionToHHTo4V_M-1000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_4v"),
  ("nof_db_events",         99999),
  ("nof_db_files",          6),
  ("fsize_db",              5933581710),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 5.93GB; nevents: 100.00k; release: 9_4_7; last modified: 2019-05-09 08:59:43"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-250_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_250_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_250_hh_4v"),
  ("nof_db_events",         399996),
  ("nof_db_files",          17),
  ("fsize_db",              20066660592),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.07GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-05-10 23:05:41"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-260_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_260_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_4v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          20),
  ("fsize_db",              19879949428),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.88GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-14 13:55:46"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-270_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_270_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_4v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          21),
  ("fsize_db",              20200851289),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.20GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-12 20:46:36"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-280_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_280_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_280_hh_4v"),
  ("nof_db_events",         391999),
  ("nof_db_files",          17),
  ("fsize_db",              19893233798),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.89GB; nevents: 392.00k; release: 9_4_7; last modified: 2019-05-17 07:27:19"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-300_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_300_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_4v"),
  ("nof_db_events",         383998),
  ("nof_db_files",          20),
  ("fsize_db",              19708482041),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.71GB; nevents: 384.00k; release: 9_4_7; last modified: 2019-05-15 22:27:34"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-320_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_320_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_320_hh_4v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          13),
  ("fsize_db",              15656023835),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.66GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-05-19 00:22:01"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-350_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_350_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_4v"),
  ("nof_db_events",         299999),
  ("nof_db_files",          12),
  ("fsize_db",              16009029568),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.01GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-05-17 12:41:42"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo4V_M-400_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_400_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_4v"),
  ("nof_db_events",         300000),
  ("nof_db_files",          18),
  ("fsize_db",              16480100060),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.48GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-05-19 11:17:41"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-450_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_450_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_4v"),
  ("nof_db_events",         287998),
  ("nof_db_files",          17),
  ("fsize_db",              16214133807),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.21GB; nevents: 288.00k; release: 9_4_7; last modified: 2019-03-15 08:47:13"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-500_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_500_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_4v"),
  ("nof_db_events",         299997),
  ("nof_db_files",          14),
  ("fsize_db",              17053053622),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 17.05GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-05-21 18:09:10"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-550_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_550_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_4v"),
  ("nof_db_events",         299998),
  ("nof_db_files",          12),
  ("fsize_db",              17210955077),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 17.21GB; nevents: 300.00k; release: 9_4_7; last modified: 2019-05-12 13:31:18"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo4V_M-600_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_600_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_4v"),
  ("nof_db_events",         191998),
  ("nof_db_files",          13),
  ("fsize_db",              11180869047),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.18GB; nevents: 192.00k; release: 9_4_7; last modified: 2019-05-23 14:27:10"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-650_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_650_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_4v"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              11726047160),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.73GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-05-11 00:11:58"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-700_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_700_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_700_hh_4v"),
  ("nof_db_events",         191999),
  ("nof_db_files",          11),
  ("fsize_db",              11310227020),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.31GB; nevents: 192.00k; release: 9_4_7; last modified: 2019-03-13 17:02:18"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo4V_M-750_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_750_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_750_hh_4v"),
  ("nof_db_events",         199997),
  ("nof_db_files",          11),
  ("fsize_db",              11817475227),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.82GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-14 16:49:49"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-800_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_800_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_4v"),
  ("nof_db_events",         199998),
  ("nof_db_files",          17),
  ("fsize_db",              11932391412),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 11.93GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-13 20:45:26"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToBulkGravitonToHHTo4V_M-850_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_spin2_850_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_850_hh_4v"),
  ("nof_db_events",         199999),
  ("nof_db_files",          13),
  ("fsize_db",              12455825050),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 12.46GB; nevents: 200.00k; release: 9_4_7; last modified: 2019-03-14 01:46:21"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jul07_GluGluToBulkGravitonToHHTo4V_M-900_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v"),
  ("sample_category",       "signal_ggf_spin2_900_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_900_hh_4v"),
  ("nof_db_events",         99998),
  ("nof_db_files",          8),
  ("fsize_db",              6157522996),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.16GB; nevents: 100.00k; release: 9_4_7; last modified: 2019-03-14 22:53:43"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToBulkGravitonToHHTo4V_M-1000_narrow_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v"),
  ("sample_category",       "signal_ggf_spin2_1000_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_1000_hh_4v"),
  ("nof_db_events",         99999),
  ("nof_db_files",          8),
  ("fsize_db",              6189551070),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 6.19GB; nevents: 100.00k; release: 9_4_7; last modified: 2019-03-11 06:49:27"),
])

meta_dictionary["/VBFHHTo4Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_VBFHHTo4Tau_CV_1_C2V_1_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_tttt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_4t"),
  ("nof_db_events",         384000),
  ("nof_db_files",          23),
  ("fsize_db",              20516924301),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.52GB; nevents: 384.00k; release: 9_4_7; last modified: 2018-08-14 13:42:37"),
])

meta_dictionary["/GluGluToHHTo4Tau_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4Tau_node_SM_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          15),
  ("fsize_db",              20766449398),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.77GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-07 00:29:46"),
])

meta_dictionary["/GluGluToHHTo4Tau_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4Tau_node_2_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_4t"),
  ("nof_db_events",         388000),
  ("nof_db_files",          21),
  ("fsize_db",              21137556590),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.14GB; nevents: 388.00k; release: 9_4_7; last modified: 2018-10-04 12:13:06"),
])

meta_dictionary["/GluGluToHHTo4Tau_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4Tau_node_3_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          23),
  ("fsize_db",              20758947388),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.76GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-10-05 15:59:05"),
])

meta_dictionary["/GluGluToHHTo4Tau_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4Tau_node_7_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_4t"),
  ("nof_db_events",         374000),
  ("nof_db_files",          16),
  ("fsize_db",              19521414949),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.52GB; nevents: 374.00k; release: 9_4_7; last modified: 2018-10-05 15:45:55"),
])

meta_dictionary["/GluGluToHHTo4Tau_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4Tau_node_9_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          20),
  ("fsize_db",              21901746830),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.90GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-09-19 08:27:56"),
])

meta_dictionary["/GluGluToHHTo4Tau_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4Tau_node_12_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_4t"),
  ("nof_db_events",         396000),
  ("nof_db_files",          16),
  ("fsize_db",              20180485758),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.18GB; nevents: 396.00k; release: 9_4_7; last modified: 2018-10-05 06:34:17"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo2V2Tau_node_SM_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_2v2t"),
  ("nof_db_events",         399996),
  ("nof_db_files",          15),
  ("fsize_db",              21713327567),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.71GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-12 20:31:29"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToHHTo2V2Tau_node_2_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_2v2t"),
  ("nof_db_events",         369992),
  ("nof_db_files",          19),
  ("fsize_db",              20666744125),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.67GB; nevents: 369.99k; release: 9_4_7; last modified: 2019-03-18 19:59:40"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo2V2Tau_node_3_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_2v2t"),
  ("nof_db_events",         392996),
  ("nof_db_files",          14),
  ("fsize_db",              20864139002),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.86GB; nevents: 393.00k; release: 9_4_7; last modified: 2019-03-13 01:12:35"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_4_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToHHTo2V2Tau_node_4_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_4_hh_2v2t"),
  ("nof_db_events",         375989),
  ("nof_db_files",          13),
  ("fsize_db",              19916065120),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.92GB; nevents: 375.99k; release: 9_4_7; last modified: 2019-03-13 18:44:19"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_5_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToHHTo2V2Tau_node_5_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_5_hh_2v2t"),
  ("nof_db_events",         399994),
  ("nof_db_files",          20),
  ("fsize_db",              21844664310),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.84GB; nevents: 399.99k; release: 9_4_7; last modified: 2019-03-20 22:16:15"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_6_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToHHTo2V2Tau_node_6_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_6_hh_2v2t"),
  ("nof_db_events",         399992),
  ("nof_db_files",          18),
  ("fsize_db",              21124650657),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.12GB; nevents: 399.99k; release: 9_4_7; last modified: 2019-03-14 14:02:38"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToHHTo2V2Tau_node_7_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_2v2t"),
  ("nof_db_events",         384992),
  ("nof_db_files",          20),
  ("fsize_db",              20503345442),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.50GB; nevents: 384.99k; release: 9_4_7; last modified: 2019-03-13 18:51:06"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_8_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToHHTo2V2Tau_node_8_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_8_hh_2v2t"),
  ("nof_db_events",         399997),
  ("nof_db_files",          21),
  ("fsize_db",              21039976306),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.04GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-10 21:33:53"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToHHTo2V2Tau_node_9_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_2v2t"),
  ("nof_db_events",         399991),
  ("nof_db_files",          12),
  ("fsize_db",              22600644898),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 22.60GB; nevents: 399.99k; release: 9_4_7; last modified: 2019-03-08 20:38:53"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_10_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo2V2Tau_node_10_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_10_hh_2v2t"),
  ("nof_db_events",         399986),
  ("nof_db_files",          18),
  ("fsize_db",              21181482185),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.18GB; nevents: 399.99k; release: 9_4_7; last modified: 2019-03-11 08:41:47"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_11_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_11_hh_2v2t"),
  ("nof_db_events",         395994),
  ("nof_db_files",          20),
  ("fsize_db",              21005832838),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.01GB; nevents: 395.99k; release: 9_4_7; last modified: 2019-03-12 20:40:51"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo2V2Tau_node_12_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_2v2t"),
  ("nof_db_events",         399993),
  ("nof_db_files",          20),
  ("fsize_db",              21048263593),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.05GB; nevents: 399.99k; release: 9_4_7; last modified: 2019-03-16 11:40:55"),
])

meta_dictionary["/GluGluToHHTo4V_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4V_node_SM_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_4v"),
  ("nof_db_events",         379997),
  ("nof_db_files",          17),
  ("fsize_db",              20701310914),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.70GB; nevents: 380.00k; release: 9_4_7; last modified: 2019-03-12 20:29:20"),
])

meta_dictionary["/GluGluToHHTo4V_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4V_node_2_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          15),
  ("fsize_db",              23052019817),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 23.05GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-11 06:49:43"),
])

meta_dictionary["/GluGluToHHTo4V_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4V_node_3_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_4v"),
  ("nof_db_events",         382999),
  ("nof_db_files",          22),
  ("fsize_db",              20935006290),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.94GB; nevents: 383.00k; release: 9_4_7; last modified: 2019-03-23 09:29:26"),
])

meta_dictionary["/GluGluToHHTo4V_node_4_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4V_node_4_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_4_hh_4v"),
  ("nof_db_events",         391999),
  ("nof_db_files",          22),
  ("fsize_db",              21344876204),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.34GB; nevents: 392.00k; release: 9_4_7; last modified: 2019-03-14 14:02:05"),
])

meta_dictionary["/GluGluToHHTo4V_node_5_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToHHTo4V_node_5_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_5_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          21),
  ("fsize_db",              22416145291),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 22.42GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-11 03:38:26"),
])

meta_dictionary["/GluGluToHHTo4V_node_6_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4V_node_6_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_6_hh_4v"),
  ("nof_db_events",         396000),
  ("nof_db_files",          16),
  ("fsize_db",              21470016217),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.47GB; nevents: 396.00k; release: 9_4_7; last modified: 2019-03-15 02:11:57"),
])

meta_dictionary["/GluGluToHHTo4V_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4V_node_7_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_4v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          21),
  ("fsize_db",              21847137342),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.85GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-15 02:07:04"),
])

meta_dictionary["/GluGluToHHTo4V_node_8_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4V_node_8_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_8_hh_4v"),
  ("nof_db_events",         395995),
  ("nof_db_files",          17),
  ("fsize_db",              21294763606),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.29GB; nevents: 396.00k; release: 9_4_7; last modified: 2019-03-16 08:10:56"),
])

meta_dictionary["/GluGluToHHTo4V_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4V_node_9_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_4v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          23),
  ("fsize_db",              23472759858),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 23.47GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-14 20:29:02"),
])

meta_dictionary["/GluGluToHHTo4V_node_10_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4V_node_10_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_10_hh_4v"),
  ("nof_db_events",         391996),
  ("nof_db_files",          18),
  ("fsize_db",              21244437020),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.24GB; nevents: 392.00k; release: 9_4_7; last modified: 2019-03-12 20:39:09"),
])

meta_dictionary["/GluGluToHHTo4V_node_11_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun17_GluGluToHHTo4V_node_11_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_11_hh_4v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          17),
  ("fsize_db",              21689984880),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.69GB; nevents: 400.00k; release: 9_4_7; last modified: 2019-03-13 13:57:22"),
])

meta_dictionary["/GluGluToHHTo4V_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2017v2_2019Jun18_GluGluToHHTo4V_node_12_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_4v"),
  ("nof_db_events",         394000),
  ("nof_db_files",          13),
  ("fsize_db",              21086443719),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.09GB; nevents: 394.00k; release: 9_4_7; last modified: 2019-03-12 21:44:20"),
])


# event statistics by sample category:
# signal_ggf_spin0_250_hh_tttt:         400.00k
# signal_ggf_spin0_260_hh_tttt:         400.00k
# signal_ggf_spin0_270_hh_tttt:         385.00k
# signal_ggf_spin0_280_hh_tttt:         400.00k
# signal_ggf_spin0_300_hh_tttt:         300.00k
# signal_ggf_spin0_350_hh_tttt:         284.00k
# signal_ggf_spin0_400_hh_tttt:         300.00k
# signal_ggf_spin0_450_hh_tttt:         300.00k
# signal_ggf_spin0_500_hh_tttt:         200.00k
# signal_ggf_spin0_550_hh_tttt:         200.00k
# signal_ggf_spin0_600_hh_tttt:         200.00k
# signal_ggf_spin0_650_hh_tttt:         200.00k
# signal_ggf_spin0_700_hh_tttt:         200.00k
# signal_ggf_spin0_750_hh_tttt:         200.00k
# signal_ggf_spin0_800_hh_tttt:         200.00k
# signal_ggf_spin0_850_hh_tttt:         192.00k
# signal_ggf_spin0_900_hh_tttt:         100.00k
# signal_ggf_spin0_1000_hh_tttt:        100.00k
# signal_ggf_spin2_250_hh_tttt:         391.00k
# signal_ggf_spin2_260_hh_tttt:         386.00k
# signal_ggf_spin2_270_hh_tttt:         380.00k
# signal_ggf_spin2_280_hh_tttt:         400.00k
# signal_ggf_spin2_300_hh_tttt:         400.00k
# signal_ggf_spin2_320_hh_tttt:         298.00k
# signal_ggf_spin2_350_hh_tttt:         384.00k
# signal_ggf_spin2_400_hh_tttt:         300.00k
# signal_ggf_spin2_450_hh_tttt:         280.00k
# signal_ggf_spin2_500_hh_tttt:         284.00k
# signal_ggf_spin2_550_hh_tttt:         200.00k
# signal_ggf_spin2_600_hh_tttt:         198.00k
# signal_ggf_spin2_650_hh_tttt:         200.00k
# signal_ggf_spin2_700_hh_tttt:         189.00k
# signal_ggf_spin2_750_hh_tttt:         196.00k
# signal_ggf_spin2_800_hh_tttt:         200.00k
# signal_ggf_spin2_850_hh_tttt:         194.00k
# signal_ggf_spin2_900_hh_tttt:         100.00k
# signal_ggf_spin2_1000_hh_tttt:        100.00k
# signal_ggf_spin0_250_hh_wwtt:         400.00k
# signal_ggf_spin0_260_hh_wwtt:         399.99k
# signal_ggf_spin0_270_hh_wwtt:         400.00k
# signal_ggf_spin0_280_hh_wwtt:         380.00k
# signal_ggf_spin0_300_hh_wwtt:         299.99k
# signal_ggf_spin0_320_hh_wwtt:         300.00k
# signal_ggf_spin0_350_hh_wwtt:         299.99k
# signal_ggf_spin0_400_hh_wwtt:         286.99k
# signal_ggf_spin0_450_hh_wwtt:         291.99k
# signal_ggf_spin0_500_hh_wwtt:         270.00k
# signal_ggf_spin0_550_hh_wwtt:         300.00k
# signal_ggf_spin0_600_hh_wwtt:         196.00k
# signal_ggf_spin0_650_hh_wwtt:         200.00k
# signal_ggf_spin0_700_hh_wwtt:         192.00k
# signal_ggf_spin0_750_hh_wwtt:         200.00k
# signal_ggf_spin0_800_hh_wwtt:         200.00k
# signal_ggf_spin0_850_hh_wwtt:         192.00k
# signal_ggf_spin0_900_hh_wwtt:         200.00k
# signal_ggf_spin0_1000_hh_wwtt:        100.00k
# signal_ggf_spin2_250_hh_wwtt:         395.00k
# signal_ggf_spin2_260_hh_wwtt:         396.00k
# signal_ggf_spin2_270_hh_wwtt:         400.00k
# signal_ggf_spin2_280_hh_wwtt:         395.00k
# signal_ggf_spin2_300_hh_wwtt:         300.00k
# signal_ggf_spin2_320_hh_wwtt:         284.99k
# signal_ggf_spin2_350_hh_wwtt:         300.00k
# signal_ggf_spin2_400_hh_wwtt:         290.00k
# signal_ggf_spin2_450_hh_wwtt:         279.99k
# signal_ggf_spin2_500_hh_wwtt:         200.00k
# signal_ggf_spin2_550_hh_wwtt:         200.00k
# signal_ggf_spin2_600_hh_wwtt:         200.00k
# signal_ggf_spin2_650_hh_wwtt:         196.00k
# signal_ggf_spin2_700_hh_wwtt:         196.00k
# signal_ggf_spin2_750_hh_wwtt:         200.00k
# signal_ggf_spin2_800_hh_wwtt:         200.00k
# signal_ggf_spin2_850_hh_wwtt:         192.00k
# signal_ggf_spin2_900_hh_wwtt:         100.00k
# signal_ggf_spin2_1000_hh_wwtt:        100.00k
# signal_ggf_spin0_250_hh_wwww:         400.00k
# signal_ggf_spin0_260_hh_wwww:         400.00k
# signal_ggf_spin0_270_hh_wwww:         386.00k
# signal_ggf_spin0_280_hh_wwww:         389.00k
# signal_ggf_spin0_300_hh_wwww:         300.00k
# signal_ggf_spin0_320_hh_wwww:         300.00k
# signal_ggf_spin0_350_hh_wwww:         292.00k
# signal_ggf_spin0_400_hh_wwww:         300.00k
# signal_ggf_spin0_450_hh_wwww:         292.00k
# signal_ggf_spin0_500_hh_wwww:         300.00k
# signal_ggf_spin0_550_hh_wwww:         300.00k
# signal_ggf_spin0_600_hh_wwww:         196.00k
# signal_ggf_spin0_650_hh_wwww:         200.00k
# signal_ggf_spin0_700_hh_wwww:         200.00k
# signal_ggf_spin0_750_hh_wwww:         192.00k
# signal_ggf_spin0_800_hh_wwww:         200.00k
# signal_ggf_spin0_850_hh_wwww:         200.00k
# signal_ggf_spin0_900_hh_wwww:         200.00k
# signal_ggf_spin0_1000_hh_wwww:        100.00k
# signal_ggf_spin2_250_hh_wwww:         400.00k
# signal_ggf_spin2_260_hh_wwww:         400.00k
# signal_ggf_spin2_270_hh_wwww:         400.00k
# signal_ggf_spin2_280_hh_wwww:         392.00k
# signal_ggf_spin2_300_hh_wwww:         384.00k
# signal_ggf_spin2_320_hh_wwww:         300.00k
# signal_ggf_spin2_350_hh_wwww:         300.00k
# signal_ggf_spin2_400_hh_wwww:         300.00k
# signal_ggf_spin2_450_hh_wwww:         288.00k
# signal_ggf_spin2_500_hh_wwww:         300.00k
# signal_ggf_spin2_550_hh_wwww:         300.00k
# signal_ggf_spin2_600_hh_wwww:         192.00k
# signal_ggf_spin2_650_hh_wwww:         200.00k
# signal_ggf_spin2_700_hh_wwww:         192.00k
# signal_ggf_spin2_750_hh_wwww:         200.00k
# signal_ggf_spin2_800_hh_wwww:         200.00k
# signal_ggf_spin2_850_hh_wwww:         200.00k
# signal_ggf_spin2_900_hh_wwww:         100.00k
# signal_ggf_spin2_1000_hh_wwww:        100.00k
# signal_vbf_nonresonant_1_1_1_hh_tttt: 384.00k
# signal_ggf_nonresonant_hh_tttt:       2.36M
# signal_ggf_nonresonant_hh_wwtt:       4.72M
# signal_ggf_nonresonant_hh_wwww:       4.73M

