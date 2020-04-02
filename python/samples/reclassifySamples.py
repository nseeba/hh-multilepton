import collections
import itertools
import copy

def reclassifySamples(samples_era_hh, samples_era_bkg, samples_era_ttbar = None):

  sum_events_hh  = copy.deepcopy(samples_era_hh['sum_events'])
  sum_events_bkg = copy.deepcopy(samples_era_bkg['sum_events'])

  del samples_era_hh['sum_events']
  del samples_era_bkg['sum_events']
  if samples_era_ttbar:
    del samples_era_ttbar['sum_events']

  if samples_era_ttbar:
    samples = collections.OrderedDict(itertools.chain(
      samples_era_bkg.items(), samples_era_hh.items(), samples_era_ttbar.items()
    ))
  else:
    samples = collections.OrderedDict(itertools.chain(samples_era_bkg.items(), samples_era_hh.items()))

  samples['sum_events'] = sum_events_hh + sum_events_bkg

  from collections import OrderedDict as OD

  for sample_name, sample_info in samples.items():

    if not isinstance(sample_info, OD):
      continue

    if 'CountWeightedLHEWeightScale' in sample_info["nof_events"] and \
        sample_info["nof_events"]['CountWeightedLHEWeightScale'] == [ 0 ]:
      sample_info["has_LHE"] = False

    if sample_info["process_name_specific"].startswith('signal') and 'hh' in sample_info["process_name_specific"]:
      ##sample_info["use_it"] = 'nonresonant' not in sample_info["process_name_specific"] # temp: enable resonant samples only
      sample_info["use_it"] = True # CV: enable non-resonant samples (needed for HH->bbWW analysis !!)
      sample_info["sample_category_hh"] = sample_info["sample_category"]

    if sample_info["sample_category"] == "Rares":
      sample_info["sample_category"] = "Other"
    elif sample_name.startswith('/ZZTo'):
      sample_info["sample_category"] = "ZZ"
    elif sample_name.startswith('/WZTo'):
      sample_info["sample_category"] = "WZ"
    elif sample_name.startswith('/WWTo'):
      sample_info["sample_category"] = "WW"
    elif sample_name.startswith('/DY') and sample_name.find('JetsToLL') != -1 and sample_name.find('JetsToLL') < 10:
      sample_info["sample_category"] = "DY"
    elif sample_name.startswith('/W') and sample_name.find('JetsToLNu') != -1 and sample_name.find('JetsToLNu') < 10:
      sample_info["sample_category"] = "W"
    elif sample_name.startswith('/ttH'):
      sample_info["sample_category"] = "TTH"
    elif sample_info["sample_category"] in [ "tHq", "tHW" ]:
      sample_info["sample_category"] = "TH"
    elif sample_name.startswith('/TTTo'):
      sample_info["sample_category"] = "TT"
      sample_info["use_it"] = True
    elif sample_name.startswith('/TTJets'):
      sample_info["sample_category"] = "TT"
      sample_info["use_it"] = False
    elif sample_name.startswith(('/VH', '/ZH')):
      sample_info["sample_category"] = "VH"
    elif sample_name.startswith(('/TTZTo', '/ttZJets')):
      sample_info["sample_category"] = "TTZ"
    elif sample_name.startswith('/TTWW'):
      sample_info["sample_category"] = "TTWW"
    elif sample_name.startswith(('/TTWJets', '/ttWJets')):
      sample_info["sample_category"] = "TTW"

    # disable Tau PD by default -- to avoid double-counting the data events in all analysis channels but 0l+4tau and 1l+3tau
    # where the PD is the only one enabled
    elif sample_name.startswith('/Tau/'):
      sample_info["use_it"] = False

    if samples_era_ttbar and sample_name in samples_era_ttbar:
      sample_info["use_it"] = False

    if sample_name.startswith(('/TGJets', '/TTGJets', '/WGTo', '/ZGTo')):
      sample_info["sample_category"] = "XGamma"

  return samples
