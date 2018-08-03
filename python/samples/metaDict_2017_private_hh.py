from collections import OrderedDict as OD

# file generated at 2018-08-03 20:11:51 with the following command:
# find_samples.py -V -i /home/karl/CMSSW_9_4_6_patch1/src/tthAnalysis/NanoAOD/test/datasets_private_hh_2017.txt -m python/samples/metaDict_2017_private_hh.py -c /hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Aug03 -v 9_4_0

meta_dictionary = OD()


### event sums

sum_events = { 
}


meta_dictionary["/HHTo4T_madgraph_pythia8_CP5_M400/private/USER"] =  OD([
  ("crab_string",           "NanoProduction_v2_2018Aug03_HHTo4T_madgraph_pythia8_CP5_M400__private"),
  ("sample_category",       "signal"),
  ("process_name_specific", "hh_4t_400"),
  ("nof_db_events",         384000),
  ("nof_db_files",          193),
  ("fsize_db",              22408025117),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 22.41GB; nevents: 384.00k; release: 9_4_0; last modified: 2018-08-02 20:38:17"),
])

meta_dictionary["/HHTo4T_madgraph_pythia8_CP5_M700/private/USER"] =  OD([
  ("crab_string",           "NanoProduction_v2_2018Aug03_HHTo4T_madgraph_pythia8_CP5_M700__private"),
  ("sample_category",       "signal"),
  ("process_name_specific", "hh_4t_700"),
  ("nof_db_events",         311998),
  ("nof_db_files",          160),
  ("fsize_db",              19502577906),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.50GB; nevents: 312.00k; release: 9_4_0; last modified: 2018-08-02 19:45:36"),
])


# event statistics by sample category:
# signal: 696.00k

