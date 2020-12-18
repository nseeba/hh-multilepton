import collections
import itertools
import copy
import re

HH_DECAYMODES = [ 'wwww', 'wwtt', 'tttt', 'bbtt', 'bbvv_sl', 'bbvv' ]
HH_DECAYMODES_SUFFIX = [ '_{}'.format(hh_dm) for hh_dm in HH_DECAYMODES ]
HH_DECAYMODES_RE = re.compile('_({}$)'.format('|'.join(HH_DECAYMODES)))

from tthAnalysis.HiggsToTauTau.analysisSettings import systematics

def reclassifySamples(samples_era_hh, samples_era_bkg, samples_era_ttbar = None, separate_th = True):

  sum_events_hh  = copy.deepcopy(samples_era_hh['sum_events'])
  sum_events_bkg = copy.deepcopy(samples_era_bkg['sum_events'])
  sum_events_ttbar = []

  del samples_era_hh['sum_events']
  del samples_era_bkg['sum_events']
  if samples_era_ttbar:
    sum_events_ttbar = copy.deepcopy(samples_era_ttbar['sum_events'])
    del samples_era_ttbar['sum_events']

  if samples_era_ttbar:
    samples = collections.OrderedDict(itertools.chain(
      samples_era_bkg.items(), samples_era_hh.items(), samples_era_ttbar.items()
    ))
  else:
    samples = collections.OrderedDict(itertools.chain(samples_era_bkg.items(), samples_era_hh.items()))

  samples['sum_events'] = sum_events_hh + sum_events_bkg + sum_events_ttbar

  from collections import OrderedDict as OD

  for sample_name, sample_info in samples.items():

    if not isinstance(sample_info, OD):
      continue

    if 'CountWeightedLHEWeightScale' in sample_info["nof_events"] and \
        sample_info["nof_events"]['CountWeightedLHEWeightScale'] == [ 0 ]:
      sample_info["has_LHE"] = False

    if sample_info["process_name_specific"].startswith('signal') and 'hh' in sample_info["process_name_specific"]:
      sample_info["use_it"] = 'vbf_spin' not in sample_info["process_name_specific"]
      sample_info["sample_category_hh"] = copy.deepcopy(sample_info["sample_category"])
      if 'dipoleRecoilOn' not in sample_info["sample_category"]:
        assert(sample_info["sample_category"].endswith(tuple(HH_DECAYMODES_SUFFIX)))
      sample_info["sample_category"] = HH_DECAYMODES_RE.sub("", sample_info["sample_category_hh"])
      assert(sample_info["sample_category"] != sample_info["sample_category_hh"])

    if sample_info["sample_category"] == "Rares":
      sample_info["sample_category"] = "Other"
    elif sample_name.startswith('/ZZTo'):
      sample_info["sample_category"] = "qqZZ"
    elif sample_name.startswith('/GluGluToContinToZZTo'):
      sample_info["sample_category"] = "ggZZ"
    elif sample_name.startswith('/WZTo'):
      sample_info["sample_category"] = "WZ"
    elif sample_name.startswith('/WWTo'):
      sample_info["sample_category"] = "WW"
    elif sample_name.startswith('/DY'):
      sample_info["sample_category"] = "DY"
    elif sample_name.startswith('/W') and sample_name.find('JetsToLNu') != -1 and sample_name.find('JetsToLNu') < 10:
      sample_info["sample_category"] = "W"
    elif sample_name.startswith('/ttH'):
      sample_info["sample_category"] = "TTH"
    elif sample_info["sample_category"] in [ "tHq", "tHW" ]:
      if not separate_th:
        sample_info["sample_category"] = "TH"
    elif sample_name.startswith('/TTTo'):
      if sample_info["sample_category"].replace("TT_", "") not in systematics.ttbar:
        sample_info["sample_category"] = "TT"
      sample_info["use_it"] = True
    elif sample_name.startswith('/TTJets'):
      sample_info["sample_category"] = "TT"
      sample_info["use_it"] = False
    elif sample_name.startswith(('/TTZTo', '/ttZJets')):
      sample_info["sample_category"] = "TTZ"
    elif sample_name.startswith('/TTWW'):
      sample_info["sample_category"] = "TTWW"
    elif sample_name.startswith(('/TTWJets', '/ttWJets')):
      sample_info["sample_category"] = "TTW"
    elif sample_name.startswith(("/TTZH", "/TTWH")):
      sample_info["use_it"] = False

    # disable Tau PD by default -- to avoid double-counting the data events in all analysis channels but 0l+4tau and 1l+3tau
    # where the PD is the only one enabled
    elif sample_name.startswith('/Tau/'):
      sample_info["use_it"] = False

    if samples_era_ttbar and sample_name in samples_era_ttbar:
      sample_info["use_it"] = False

    if sample_name.startswith(('/TGJets', '/TTGJets', '/WGTo', '/ZGTo')):
      sample_info["sample_category"] = "XGamma"

    if sample_info["sample_category"] == "VH":
      if sample_name.startswith("/WH"):
        sample_info["sample_category"] = "WH"
      elif sample_name.startswith("/ZH"):
        sample_info["sample_category"] = "ZH"
      else:
        assert(sample_name.startswith("/VH"))
        sample_info["use_it"] = False

      #TODO remove after we've skimmed them
      if sample_name.startswith(("/WHToNonbb", "/ZHToNonbb")):
        sample_info["use_it"] = False

  return samples
