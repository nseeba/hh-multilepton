from hhAnalysis.multilepton.samples.metaDict_2017_hh import meta_dictionary as meta_dictionary_general
from hhAnalysis.multilepton.samples.metaDict_2017_hh import sum_events as sum_events_general
from hhAnalysis.multilepton.samples.metaDict_2017_private_hh import meta_dictionary as meta_dictionary_private
from hhAnalysis.multilepton.samples.metaDict_2017_private_hh import sum_events as sum_events_private

import collections
import itertools

meta_dictionary = collections.OrderedDict(itertools.chain(
  meta_dictionary_general.items(), meta_dictionary_private.items()
))
sum_events = set(sum_events_general) | set(sum_events_private)
