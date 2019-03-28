from hhAnalysis.multilepton.samples.hhAnalyzeSamples_2017 import samples_2017

import re

for sample_name, sample_info in samples_2017.items():
  if sample_name == 'sum_events':
    continue
  if sample_info["process_name_specific"] in [
        "ttHJetToNonbb_M125_amcatnlo",
        "ttHToNonbb_M125_powheg",
        "ttHToNonbb_M125_powheg_ext1",
        "TTZJets_LO",
        "TTZJets_LO_ext1",
        "TTWJets_LO",
        "TTWJets_LO_ext1",
        "TTTo2L2Nu",
        "TTTo2L2Nu_PSweights",
        "TTToSemiLeptonic",
        "TTToSemiLeptonic_PSweights",
        "TTToHadronic",
        "TTToHadronic_PSweights",
        "GluGluHToZZTo4L",
        "GluGluHToZZTo4L_ext1",
        "ZZTo4L",
        "ZZTo4L_ext1",
        "ZZTo2L2Q",
        "ZZTo2L2Nu",
        "WZZ",
        "ZZZ",
        "DYJetsToLL_M-50_LO",
        "DYJetsToLL_M-50_LO_ext1",
        "DY1JetsToLL_M-50",
        "DY1JetsToLL_M-50_ext1",
        "DY2JetsToLL_M-50",
        "DY2JetsToLL_M-50_ext1",
        "DY3JetsToLL_M-50",
        "DY3JetsToLL_M-50_ext1",
        "DY4JetsToLL_M-50",
        "VHToNonbb_M125",
        "VHToNonbb_M125_v14-v2",
        "TTWW",
        "WZTo3LNu",
        "WWTo2L2Nu",
        "WWTo2L2Nu_PSweights",
        "WWToLNuQQ",
        "WWToLNuQQ_ext1",
        "WWToLNuQQ_PSweights",
        "WWTo1L1Nu2Q",
        "WWTo4Q",
        "WWTo4Q_PSweights",
        "WWW_4F",
        "WWZ_4F",
        "WWTo2L2Nu_DoubleScattering",
        "WpWpJJ_EWK_QCD",
        "WpWpJJ_EWK_QCD_v14-v1",
        "DYJetsToLL_M-4to50_HT-100to200",
        "DYJetsToLL_M-4to50_HT-100to200_ext1",
        "DYJetsToLL_M-4to50_HT-200to400",
        "DYJetsToLL_M-4to50_HT-200to400_ext1",
        "DYJetsToLL_M-4to50_HT-400to600",
        "DYJetsToLL_M-4to50_HT-400to600_ext1",
        "DYJetsToLL_M-4to50_HT-600toInf",
        "DYJetsToLL_M50_HT100to200",
        "DYJetsToLL_M50_HT100to200_ext1",
        "DYJetsToLL_M50_HT200to400",
        "DYJetsToLL_M50_HT200to400_ext1",
        "DYJetsToLL_M50_HT400to600",
        "DYJetsToLL_M50_HT400to600_ext1",
        "DYJetsToLL_M50_HT600to800",
        "DYJetsToLL_M50_HT800to1200",
        "DYJetsToLL_M50_HT1200to2500",
        "DYJetsToLL_M50_HT2500toInf"
      ]:
    sample_info["use_it"] = True
  elif sample_info["process_name_specific"].startswith("signal") and 'hh' in sample_info["process_name_specific"]:
    sample_info["use_it"] = 'nonresonant' not in sample_info["process_name_specific"] # temp: enable resonant samples only
  elif re.match("WZTo3LNu_(0|1|2|3)Jets.*", sample_info["process_name_specific"]):
    sample_info["use_it"] = True
  else:
    sample_info["use_it"] = False
