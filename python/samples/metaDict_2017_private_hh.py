from collections import OrderedDict as OD

# file generated at 2018-08-04 19:19:15 with the following command:
# find_samples.py -V -i /home/karl/CMSSW_9_4_6_patch1/src/tthAnalysis/NanoAOD/test/datasets_private_hh_2017.txt -m python/samples/metaDict_2017_private_hh.py -c /hdfs/cms/store/user/kaehatah/NanoProduction_v2_2018Aug03 -v 9_4_0

meta_dictionary = OD()


### event sums

sum_events = {
}


meta_dictionary["/HHTo4T_madgraph_pythia8_CP5_M400/private/USER"] =  OD([
  ("crab_string",           "NanoProduction_v2_2018Aug03_HHTo4T_madgraph_pythia8_CP5_M400__private"),
  ("sample_category",       "signal_radion_400"),
  ("process_name_specific", "signal_hh_4t_400"),
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
  ("sample_category",       "signal_radion_700"),
  ("process_name_specific", "signal_hh_4t_700"),
  ("nof_db_events",         311998),
  ("nof_db_files",          160),
  ("fsize_db",              19502577906),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.50GB; nevents: 312.00k; release: 9_4_0; last modified: 2018-08-02 19:45:36"),
])

meta_dictionary["/HHTo2T2V_madgraph_pythia8_CP5_M400/private/USER"] =  OD([
  ("crab_string",           "NanoProduction_v2_2018Aug03_HHTo2T2V_madgraph_pythia8_CP5_M400__private"),
  ("sample_category",       "signal_radion_400"),
  ("process_name_specific", "signal_hh_2t2v_400"),
  ("nof_db_events",         257207),
  ("nof_db_files",          130),
  ("fsize_db",              15401525854),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.40GB; nevents: 257.21k; release: 9_4_0; last modified: 2018-08-04 14:40:28"),
])

meta_dictionary["/HHTo2T2V_madgraph_pythia8_CP5_M700/private/USER"] =  OD([
  ("crab_string",           "NanoProduction_v2_2018Aug03_HHTo2T2V_madgraph_pythia8_CP5_M700__private"),
  ("sample_category",       "signal_radion_700"),
  ("process_name_specific", "signal_hh_2t2v_700"),
  ("nof_db_events",         301884),
  ("nof_db_files",          152),
  ("fsize_db",              19508012725),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 19.51GB; nevents: 301.88k; release: 9_4_0; last modified: 2018-08-04 17:11:50"),
])

meta_dictionary["/HHTo4V_madgraph_pythia8_CP5_M400/private/USER"] =  OD([
  ("crab_string",           "NanoProduction_v2_2018Aug03_HHTo4V_madgraph_pythia8_CP5_M400__private"),
  ("sample_category",       "signal_radion_400"),
  ("process_name_specific", "signal_hh_4v_400"),
  ("nof_db_events",         262996),
  ("nof_db_files",          133),
  ("fsize_db",              16090082982),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 16.09GB; nevents: 263.00k; release: 9_4_0; last modified: 2018-08-04 17:22:25"),
])

meta_dictionary["/HHTo4V_madgraph_pythia8_CP5_M700/private/USER"] =  OD([
  ("crab_string",           "NanoProduction_v2_2018Aug03_HHTo4V_madgraph_pythia8_CP5_M700__private"),
  ("sample_category",       "signal_radion_700"),
  ("process_name_specific", "signal_hh_4v_700"),
  ("nof_db_events",         230116),
  ("nof_db_files",          118),
  ("fsize_db",              15395786053),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 15.40GB; nevents: 230.12k; release: 9_4_0; last modified: 2018-08-04 17:20:53"),
])


# event statistics by sample category:
# signal: 1.75M

