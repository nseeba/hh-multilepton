from collections import OrderedDict as OD

# file generated at 2018-10-12 13:13:50 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets_hh_2017.txt -m python/samples/metaDict_2017_hh.py -c /hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Sep26

meta_dictionary = OD()


### event sums

sum_events = { 
}


meta_dictionary["/GluGluToHHTo4Tau_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "NanoProduction_v2_2018Sep26_GluGluToHHTo4Tau_node_9_13TeV-madgraph_correctedcfg__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_ggf_nonresonant_node_9_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          20),
  ("fsize_db",              21901746830),
  ("xsection",              1.0),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 21.90GB; nevents: 400.00k; release: 9_4_7; last modified: 2018-09-19 08:27:56"),
])

meta_dictionary["/VBFHHTo4Tau_CV_1_C2V_1_C3_1_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "NanoProduction_v2_2018Sep26_VBFHHTo4Tau_CV_1_C2V_1_C3_1_13TeV-madgraph__RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_tttt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_4t"),
  ("nof_db_events",         384000),
  ("nof_db_files",          23),
  ("fsize_db",              20516924301),
  ("xsection",              1.0),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 20.52GB; nevents: 384.00k; release: 9_4_7; last modified: 2018-08-14 13:42:37"),
])


# event statistics by sample category:
# signal_ggf_nonresonant_node_9_hh_tttt: 400.00k
# signal_vbf_nonresonant_1_1_1_hh_tttt:  384.00k

