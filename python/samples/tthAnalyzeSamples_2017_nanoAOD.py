from collections import OrderedDict as OD

# file generated at 2018-04-04 10:09:51 with the following command:
# create_dictionary.py -v -m python/samples/metaDict_2017.py -p python/samples/sampleLocations_2017.txt -Z zeroes.txt -z zombies.txt -N samples_2017 -E 2017 -o python/samples -g tthAnalyzeSamples_2017_nanoAOD.py

samples_2017 = OD()

samples_2017["/GluGluToRadionToHHTo4Tau_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "x_to_hh_260"),
  ("nof_files",                       5),
  ("nof_db_files",                    283),
  ("nof_events",                      0),
  ("nof_tree_events",                 10000),
  ("nof_db_events",                   10000),
  ("fsize_local",                     25360848528), # 25.36GB, avg file size 130.06MB
  ("fsize_db",                        603282930374), # 603.28GB, avg file size 2.13GB
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/acaan/HH_4tau_nanoAOD/GluGluToRadionToHHTo4Tau_M-260_narrow_13TeV-madgraph/nanoaod_m260"),
        ("selection", "*"),
        ("blacklist", [3]),
      ]),
    ]
  ),
])

samples_2017["/GluGluToRadionToHHTo4Tau_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "x_to_hh_300"),
  ("nof_files",                       6),
  ("nof_db_files",                    283),
  ("nof_events",                      0),
  ("nof_tree_events",                 10000),
  ("nof_db_events",                   10000),
  ("fsize_local",                     25360848528), # 25.36GB, avg file size 130.06MB
  ("fsize_db",                        603282930374), # 603.28GB, avg file size 2.13GB
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/acaan/HH_4tau_nanoAOD/GluGluToRadionToHHTo4Tau_M-300_narrow_13TeV-madgraph/nanoaod_m300"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2017["/GluGluToRadionToHHTo4Tau_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "x_to_hh_400"),
  ("nof_files",                       5),
  ("nof_db_files",                    283),
  ("nof_events",                      0),
  ("nof_tree_events",                 10000),
  ("nof_db_events",                   10000),
  ("fsize_local",                     25360848528), # 25.36GB, avg file size 130.06MB
  ("fsize_db",                        603282930374), # 603.28GB, avg file size 2.13GB
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/acaan/HH_4tau_nanoAOD/GluGluToRadionToHHTo4Tau_M-400_narrow_13TeV-madgraph/nanoaod_m400"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])

samples_2017["/GluGluToRadionToHHTo4Tau_M-700_narrow_13TeV-madgraph/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal"),
  ("process_name_specific",           "x_to_hh_700"),
  ("nof_files",                       3),
  ("nof_db_files",                    283),
  ("nof_events",                      0),
  ("nof_tree_events",                 10000),
  ("nof_db_events",                   10000),
  ("fsize_local",                     25360848528), # 25.36GB, avg file size 130.06MB
  ("fsize_db",                        603282930374), # 603.28GB, avg file size 2.13GB
  ("use_HIP_mitigation_bTag",         False),
  ("use_HIP_mitigation_mediumMuonId", False),
  ("use_it",                          True),
  ("xsection",                        1.0),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("reHLT",                           True),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/acaan/HH_4tau_nanoAOD/GluGluToRadionToHHTo4Tau_M-700_narrow_13TeV-madgraph/nanoaod_m700"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
])
