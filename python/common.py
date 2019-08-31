import re

NONRESONANT_RE    = re.compile(r'signal_ggf_nonresonant_\w+')
NONRESONANT_SM_RE = re.compile(r'signal_ggf_nonresonant_node_sm_hh_\w+')

def is_nonresonant(sample_category, require_sm = False):
  if require_sm:
    return bool(NONRESONANT_SM_RE.match(sample_category))
  else:
    return bool(NONRESONANT_RE.match(sample_category))
