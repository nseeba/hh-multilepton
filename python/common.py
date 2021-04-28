import re
import collections
import functools

from tthAnalysis.HiggsToTauTau.hhSettings import NONRESONANT_KEYS, NONRESONANT_POINTS

NONRESONANT_RE = re.compile(r'signal_ggf_nonresonant_\w+')
MASSPOINTS = [ 250., 260., 270., 280., 300., 320., 350., 400., 450., 500., 550., 600., 650., 700., 750., 800., 850., 900., 1000. ]

def is_nonresonant(sample_category, allow_nlo = False):
  if not allow_nlo and 'cHHH' in sample_category:
    return False
  return bool(NONRESONANT_RE.match(sample_category))

# credit to: https://stackoverflow.com/a/50107777
def default_kwargs(**defaultKwargs):
  def actual_decorator(fn):
    @functools.wraps(fn)
    def g(*args, **kwargs):
      defaultKwargs.update(kwargs)
      return fn(*args, **defaultKwargs)
    return g
  return actual_decorator

# example usages:
# get_histograms_to_fit('dihiggsVisMass')
# get_histograms_to_fit('dihiggsVisMass', 'm3l')
# get_histograms_to_fit('dihiggsVisMass', nonresPoints = [ 'extra' ])
@default_kwargs(nonresPoints = NONRESONANT_KEYS)
def get_histograms_to_fit(*custom_histograms, **kwargs):
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

  assert('nonresPoints' in kwargs)
  nonresPoints = kwargs['nonresPoints']
  assert(all(nonresPoint in NONRESONANT_POINTS for nonresPoint in nonresPoints))
  for nonresPoint in nonresPoints:
    for bmName in NONRESONANT_POINTS[nonresPoint]:
      mvaOutputName = "MVAOutput_{}{}".format(nonresPoint, bmName)
      if mvaOutputName in histograms_to_fit:
        raise ValueError("Encountered duplicate histogram name: %s" % mvaOutputName)
      histograms_to_fit[mvaOutputName] = {}
  return histograms_to_fit
