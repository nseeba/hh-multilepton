from hhAnalysis.multilepton.samples.hhAnalyzeSamples_2017_nanoAOD_hh_private import samples_2017 as samples_2017_hh_private
from hhAnalysis.multilepton.samples.hhAnalyzeSamples_2017_nanoAOD_hh import samples_2017 as samples_2017_hh

import collections
import itertools

del samples_2017_hh_private['sum_events']
del samples_2017_hh['sum_events']
samples_2017 = collections.OrderedDict(itertools.chain(
  samples_2017_hh_private.items(), samples_2017_hh.items()
))
