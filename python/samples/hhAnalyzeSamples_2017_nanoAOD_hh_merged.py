from hhAnalysis.multilepton.samples.hhAnalyzeSamples_2017_nanoAOD_hh_private import samples_2017 as samples_2017_hh_private

import collections
import itertools

del samples_2017_hh_private['sum_events']
samples_2017 = collections.OrderedDict(itertools.chain(
  samples_2017_hh_private.items()
))
