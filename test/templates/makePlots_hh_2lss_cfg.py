import FWCore.ParameterSet.Config as cms

from hhAnalysis.multilepton.configs.makePlots_cfi import process

process.makePlots.distributions = cms.VPSet(
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/numJets"),
        xAxisTitle = cms.string("jet Multiplicity"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/numJetsPtGt40"),
        xAxisTitle = cms.string("jet w/ pT > 40 GeV Multiplicity"),
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
        histogramName = cms.string('sel/evt/$PROCESS/dihiggsVisMass'),
        xAxisTitle = cms.string('m_{HH} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/electrons/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading e_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/electrons/$PROCESS/eta'),
        xAxisTitle = cms.string('leading e_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadElectron/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading e_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadElectron/$PROCESS/eta'),
        xAxisTitle = cms.string('leading e_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadElectron/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('subleading e_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadElectron/$PROCESS/eta'),
        xAxisTitle = cms.string('subleading e_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/muons/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading #mu_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/muons/$PROCESS/eta'),
        xAxisTitle = cms.string('leading #mu_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadMuon/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading #mu_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadMuon/$PROCESS/eta'),
        xAxisTitle = cms.string('leading #mu_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadMuon/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('subleading #mu_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadMuon/$PROCESS/eta'),
        xAxisTitle = cms.string('subleading #mu_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/jets/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading jet_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/jets/$PROCESS/eta'),
        xAxisTitle = cms.string('leading jet_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadJet/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading jet_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadJet/$PROCESS/eta'),
        xAxisTitle = cms.string('leading jet_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadJet/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('subleading jet_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadJet/$PROCESS/eta'),
        xAxisTitle = cms.string('subleading jet_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/leptonPairCharge'),
        xAxisTitle = cms.string('lepton charge sum'),
        yAxisTitle = cms.string('N')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dihiggsMass_wMet'),
        xAxisTitle = cms.string('m_{HH} with Met [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/jetMass'),
        xAxisTitle = cms.string('m_{jjjj} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{jjjj} [1/GeV]')
    ),
)
