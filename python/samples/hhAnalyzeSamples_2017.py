from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2017 import samples_2017

from collections import OrderedDict as OD

for sample_name, sample_info in samples_2017.items():

  if not isinstance(sample_info, OD):
    continue

  if sample_name.find('HHTo4Tau') != -1:
    sample_info["use_it"] = True

  if sample_name.startswith('/ZZ'):
    sample_info["sample_category"] = "ZZ"
  elif sample_name.startswith('/WZ'):
    sample_info["sample_category"] = "WZ"
  elif sample_name.startswith('/WW'):
    sample_info["sample_category"] = "WW"
  elif sample_name.startswith('/DY') and sample_name.find('JetsToLL') < 10:
    sample_info["sample_category"] = "DY"
  elif sample_name.startswith('/W') and sample_name.find('JetsToLNu') < 10:
    sample_info["sample_category"] = "W"
  elif sample_name.startswith('/ttH'):
    sample_info["sample_category"] = "TTH"

  if sample_info["sample_category"] == "Rares":
    sample_info["sample_category"] = "Other"
  if sample_info["sample_category"] in [ "tHq", "tHW" ]:
    sample_info["sample_category"] = "TH"
