from hhAnalysis.multilepton.samples.hhAnalyzeSamples_2018 import samples_2018
from tthAnalysis.HiggsToTauTau.common import load_samples_stitched

samples_2018 = load_samples_stitched(samples_2018, '2018', ['dy_lo', 'wjets']) # load LO DY and W+jets

for sample_name, sample_info in samples_2018.items():
  if sample_name == 'sum_events':
    continue
  process_name = sample_info["process_name_specific"]
  if process_name.startswith('WZTo3LNu'):
    sample_info["use_it"] = process_name.startswith(('WZTo3LNu_powheg', 'WZTo3LNu_mllmin01'))
  elif process_name.lower().startswith('ttz'):
    sample_info["use_it"] = 'TTZJets_LO' in process_name
  elif process_name.lower().startswith('ttw'):
    sample_info["use_it"] = 'TTWJets_LO' in process_name

