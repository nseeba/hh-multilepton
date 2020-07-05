from hhAnalysis.multilepton.samples.hhAnalyzeSamples_2016 import samples_2016
from tthAnalysis.HiggsToTauTau.common import load_samples_stitched

samples_2016 = load_samples_stitched(samples_2016, '2016', ['dy_lo', 'wjets']) # load LO DY and W+jets

for sample_name, sample_info in samples_2016.items():
  if sample_name == 'sum_events':
    continue
  process_name = sample_info["process_name_specific"]
  if process_name.startswith('WZTo3LNu'):
    # or maybe even use samples binned by jet multiplicity
    sample_info["use_it"] = 'powheg' in process_name
  elif process_name.lower().startswith('ttz'):
    sample_info["use_it"] = 'TTZJets_LO' in process_name
  elif process_name.lower().startswith('ttw'):
    sample_info["use_it"] = 'TTWJets_LO' in process_name
