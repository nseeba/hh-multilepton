import FWCore.ParameterSet.Config as cms

from hhAnalysis.multilepton.configs.makePlots_cfi import process

process.makePlots.distributions.extend([
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mTauTauVis'),
        xAxisTitle = cms.string('m_{#tau#tau}^{vis} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{#tau#tau}^{vis} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadHadTau/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading #tau_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadHadTau/$PROCESS/eta'),
        xAxisTitle = cms.string('leading #tau_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadHadTau/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('subleading #tau_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadHadTau/$PROCESS/eta'),
        xAxisTitle = cms.string('subleading #tau_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/leptonPairCharge'),
        xAxisTitle = cms.string('lepton charge sum'),
        yAxisTitle = cms.string('N')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/hadTauPairCharge'),
        xAxisTitle = cms.string('#tau_{h} charge sum'),
        yAxisTitle = cms.string('N')
    ),
    cms.PSet(
        histogramName = cms.string('sel/svFit4tau_wMassConstraint/$PROCESS/dihiggsVisMass1'), ## set to dihiggsVisMass1 from dihiggsVisMass
        xAxisTitle = cms.string('m_{HH}^{Vis1} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH}^{vis} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/numBJets_loose"),
        xAxisTitle = cms.string("loose b-jet Multiplicity"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/numBJets_medium"),
        xAxisTitle = cms.string("medium b-jet Multiplicity"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dihiggsMass'),
        xAxisTitle = cms.string('m_{HH} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dihiggsVisMass'),
        xAxisTitle = cms.string('m_{HH}^{Vis} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/svFit4tau_wMassConstraint/$PROCESS/dihiggsVisMass2'),
        xAxisTitle = cms.string('m_{HH}^{Vis2} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH}^{vis} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/svFit4tau_wMassConstraint/$PROCESS/dihiggsMass1'),
        xAxisTitle = cms.string('m_{HH}^({1)} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
#    cms.PSet(
#        histogramName = cms.string('sel/svFit4tau_woMassConstraint/$PROCESS/ditau1Mass1'),
#        xAxisTitle = cms.string('m_{H}^{(1)} [GeV]'),
#        yAxisTitle = cms.string('dN/dm_{H}^{(1)} [1/GeV]')
#    ),
#    cms.PSet(
#        histogramName = cms.string('sel/svFit4tau_woMassConstraint/$PROCESS/ditau1Mass2'),
#        xAxisTitle = cms.string('m_{H}^{(1)} [GeV]'),
#        yAxisTitle = cms.string('dN/dm_{H}^{(1)} [1/GeV]')
#    ),
    cms.PSet(
        histogramName = cms.string('sel/svFit4tau_wMassConstraint/$PROCESS/dihiggsMass2'),
        xAxisTitle = cms.string('m_{HH} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
#    cms.PSet(
#        histogramName = cms.string('sel/svFit4tau_woMassConstraint/$PROCESS/ditau2Mass1'),
#        xAxisTitle = cms.string('m_{H}^{(2)} [GeV]'),
#        yAxisTitle = cms.string('dN/dm_{H}^{(2)} [1/GeV]')
#    ),
#    cms.PSet(
#        histogramName = cms.string('sel/svFit4tau_woMassConstraint/$PROCESS/ditau2Mass2'),
#        xAxisTitle = cms.string('m_{H}^{(2)} [GeV]'),
#        yAxisTitle = cms.string('dN/dm_{H}^{(2)} [1/GeV]')
#    ),
    cms.PSet(
        histogramName = cms.string('sel/met/$PROCESS/met_LD'),
        xAxisTitle = cms.string('MET_LD [GeV]'),
        yAxisTitle = cms.string('dN/dMET_LD [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/met/$PROCESS/met_pt'),
        xAxisTitle = cms.string('MET [GeV]'),
        yAxisTitle = cms.string('dN/dMET [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/met/$PROCESS/mht_pt'),
        xAxisTitle = cms.string('MHT [GeV]'),
        yAxisTitle = cms.string('dN/dMHT [1/GeV]')
    ),
#    cms.PSet(
#        histogramName = cms.string('sel/met/$PROCESS/mht_phi'),
#        xAxisTitle = cms.string('#phi_{MHT} [rad]'),
#        yAxisTitle = cms.string('dN/d#phi_{MHT} [1/rad]')
#    ),
#    cms.PSet(
#        histogramName = cms.string('sel/met/$PROCESS/met_phi'),
#        xAxisTitle = cms.string('#phi_{MET} [rad]'),
#        yAxisTitle = cms.string('dN/d#phi_{MET} [1/rad]')
#    ),
])
