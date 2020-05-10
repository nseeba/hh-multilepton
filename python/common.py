import re

NONRESONANT_RE = re.compile(r'signal_ggf_nonresonant_\w+')

def is_nonresonant(sample_category, allow_nlo = False):
  if not allow_nlo and 'cHHH' in sample_category:
    return False
  return bool(NONRESONANT_RE.match(sample_category))
