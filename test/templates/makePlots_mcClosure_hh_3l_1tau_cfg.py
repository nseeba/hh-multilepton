import FWCore.ParameterSet.Config as cms

from hhAnalysis.multilepton.makePlots_mcClosure_cfg import process

process.makePlots.distributions.extend([
    cms.PSet(
        histogramName = cms.string('sel/hadTaus/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('#tau_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/hadTaus/$PROCESS/eta'),
        xAxisTitle = cms.string('#tau_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
])
