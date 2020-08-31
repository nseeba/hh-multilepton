import FWCore.ParameterSet.Config as cms

from hhAnalysis.multilepton.configs.makePlots_cfi import process

process.makePlots.distributions.extend([
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
        histogramName = cms.string('sel/thirdHadTau/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('third #tau_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/thirdHadTau/$PROCESS/eta'),
        xAxisTitle = cms.string('third #tau_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    # CV: additional plots specific to 1e+3tau category
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/1e3tau_numTightLeptons"),
        xAxisTitle = cms.string("Multiplicity of tight leptons"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/1e3tau_numFakeableTaus_passingElecVeto"),
        xAxisTitle = cms.string("Multiplicity of fakeable taus passing anti-e veto"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/1e3tau_numTightTaus"),
        xAxisTitle = cms.string("Multiplicity of tight taus"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/1e3tau_numTightTaus_passingElecVeto"),
        xAxisTitle = cms.string("Multiplicity of tight taus passing anti-e veto"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/1e3tau_numTightLeptons_and_Taus"),
        xAxisTitle = cms.string("Multiplicity of tight leptons + taus"),
        yAxisTitle = cms.string("Events")
    ),
    # CV: additional plots specific to 1mu+3tau category
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/1mu3tau_numTightLeptons"),
        xAxisTitle = cms.string("Multiplicity of tight leptons"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/1mu3tau_numFakeableTaus_passingElecVeto"),
        xAxisTitle = cms.string("Multiplicity of fakeable taus passing anti-e veto"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/1mu3tau_numTightTaus"),
        xAxisTitle = cms.string("Multiplicity of tight taus"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/1mu3tau_numTightTaus_passingElecVeto"),
        xAxisTitle = cms.string("Multiplicity of tight taus passing anti-e veto"),
        yAxisTitle = cms.string("Events")
    ),
    cms.PSet(
        histogramName = cms.string("sel/evt/$PROCESS/1mu3tau_numTightLeptons_and_Taus"),
        xAxisTitle = cms.string("Multiplicity of tight leptons + taus"),
        yAxisTitle = cms.string("Events")
    )
])
