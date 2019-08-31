import re

NONRESONANT_RE = re.compile(r'signal_ggf_nonresonant_\w+')

def is_nonresonant(sample_category, require_sm = False):
  return bool(NONRESONANT_RE.match(sample_category))
