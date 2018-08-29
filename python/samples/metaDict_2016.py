from hhAnalysis.tttt.samples.metaDict_2016_hh import meta_dictionary as meta_dictionary_hh
#from tthAnalysis.HiggsToTauTau.samples.metaDict_2016 import meta_dictionary as meta_dictionary_2016
#from tthAnalysis.HiggsToTauTau.samples.metaDict_2016 import sum_events

sum_events = set()

import itertools, collections

meta_dictionary = collections.OrderedDict(itertools.chain(
  meta_dictionary_hh.items(),# meta_dictionary_2016.items()
))
