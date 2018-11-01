import FWCore.ParameterSet.Config as cms

from hhAnalysis.multilepton.configs.makePlots_cfi import process

process.makePlots.processesBackground = cms.vstring(["WW", "WZ", "ZZ", "TT", "TTZ", "TTW", "TTWW", "VH", "TH", "TTH", "DY", "W", "Other", "conversions", "fakes_data"])

process.makePlots.distributions.extend([
  cms.PSet(
    histogramName = cms.string("sel/evt/$PROCESS/numJets"),
    xAxisTitle = cms.string("jet Multiplicity"),
    yAxisTitle = cms.string("Events")
  ),
  cms.PSet(
    histogramName = cms.string("sel/evt/$PROCESS/numJetsPtGt40"),
    xAxisTitle = cms.string("jet (>40 GeV) Multiplicity"),
    yAxisTitle = cms.string("Events")
  ),
  cms.PSet(
    histogramName = cms.string("sel/evt/$PROCESS/numBJets_loose"),
    xAxisTitle = cms.string("B-jet loose Multiplicity"),
    yAxisTitle = cms.string("Events")
  ),
  cms.PSet(
    histogramName = cms.string("sel/evt/$PROCESS/numBJets_medium"),
    xAxisTitle = cms.string("B-jet medium Multiplicity"),
    yAxisTitle = cms.string("Events")
  ),
  cms.PSet(
    histogramName = cms.string("sel/evt/$PROCESS/numElectrons"),
    xAxisTitle = cms.string("electron Multiplicity"),
    yAxisTitle = cms.string("Events")
  ),
  cms.PSet(
    histogramName = cms.string("sel/evt/$PROCESS/numMuons"),
    xAxisTitle = cms.string("muon Multiplicity"),
    yAxisTitle = cms.string("Events")
  ),
  cms.PSet(
    histogramName = cms.string("sel/evt/$PROCESS/EventCounter"),
    xAxisTitle = cms.string(""),
    yAxisTitle = cms.string("Events")
  ),
  cms.PSet(
    histogramName = cms.string("sel/evtYield/$PROCESS/evtYield"),
    xAxisTitle = cms.string("Run Period"),
    yAxisTitle = cms.string("Events / 1 fb^{-1}")
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/HT'),
    xAxisTitle = cms.string('H_{T} [GeV]'),
    yAxisTitle = cms.string('dN/dH_{T} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/STMET'),
    xAxisTitle = cms.string('S_{T}^{MET} [GeV]'),
    yAxisTitle = cms.string('dN/dS_{T}^{MET} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dihiggsMass'),
    xAxisTitle = cms.string('m_{HH} [GeV]'),
    yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dihiggsVisMass'),
    xAxisTitle = cms.string('m_{HH} visible [GeV]'),
    yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/WTojjMass'),
    xAxisTitle = cms.string('m_{jj} [GeV]'),
    yAxisTitle = cms.string('dN/dm_{jj} [1/GeV]'),
  ),
  cms.PSet(
    histogramName = cms.string('sel/electrons/$PROCESS/pt'),
    xAxisTitle = cms.string('p_{T} (e) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/muons/$PROCESS/pt'),
    xAxisTitle = cms.string('p_{T} (#mu) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/jets/$PROCESS/pt'),
    xAxisTitle = cms.string('p_{T} (jet) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/met/$PROCESS/met_pt'),
    xAxisTitle = cms.string('p_{T} (MET) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/hadTaus/$PROCESS/pt'),
    xAxisTitle = cms.string('p_{T} (#tau_{h}) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/chargedSum3l'),
    xAxisTitle = cms.string('Total charge of 3l'),
    yAxisTitle = cms.string('dN')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/numSFOS2l'),
    xAxisTitle = cms.string('Same flavor opposite sign lepton pairs'),
    yAxisTitle = cms.string('dN')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mTMetLepton1'),
    xAxisTitle = cms.string('m_{T} (MET + Lepton1) [GeV]'),
    yAxisTitle = cms.string('dN/dm_{T} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mTMetLepton2'),
    xAxisTitle = cms.string('m_{T} (MET + Lepton2) [GeV]'),
    yAxisTitle = cms.string('dN/dm_{T} [1/GeV]')
  ),
])
