import re
import collections

NONRESONANT_RE = re.compile(r'signal_ggf_nonresonant_\w+')
MASSPOINTS = [ 250., 260., 270., 280., 300., 320., 350., 400., 450., 500., 550., 600., 650., 700., 750., 800., 850., 900., 1000. ]

def is_nonresonant(sample_category, allow_nlo = False):
  if not allow_nlo and 'cHHH' in sample_category:
    return False
  return bool(NONRESONANT_RE.match(sample_category))

def get_histograms_to_fit(*custom_histograms):
  histograms_to_fit = collections.OrderedDict()
  if custom_histograms:
    for histogram_name in custom_histograms:
      histograms_to_fit[histogram_name] = {}
  #for histogram_name in [ "EventCounter", "dihiggsMass", "MVAOutput_SM" ]:
  for histogram_name in [ "EventCounter", "MVAOutput_SM" ]:
    if histogram_name not in histograms_to_fit:
      histograms_to_fit[histogram_name] = {}

  for masspoint in MASSPOINTS:
    histograms_to_fit["MVAOutput_%0.0f_spin0" % masspoint] = {}
    histograms_to_fit["MVAOutput_%0.0f_spin2" % masspoint] = {}
  bmNames = [ "BM1", "BM2", "BM3", "BM4", "BM5", "BM6", "BM7", "BM8", "BM9", "BM10", "BM11", "BM12" ]
  for bmName in bmNames:
    histograms_to_fit["MVAOutput_%s" % bmName] = {}
  return histograms_to_fit
