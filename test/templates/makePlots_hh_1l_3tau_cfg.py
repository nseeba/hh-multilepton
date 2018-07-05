import FWCore.ParameterSet.Config as cms

import numpy as np

import os

from tthAnalysis.HiggsToTauTau.configs.makePlots_cfi import process

process.makePlots.pluginType = cms.string("Plotter_HH")

process.makePlots.processesBackground = cms.vstring(
    "ZZ",
    "WZ",
    "WW",    
    "fakes_data",
    "TT",
    "TTW",
    "TTWW",
    "TTZ",
    "conversions",
    "Other",
    "VH",
    "TTH",
    "TH"
)
process.makePlots.processSignal = cms.string("signal_nonresonant")
process.makePlots.scaleSignal = cms.double(50.)
process.makePlots.legendEntrySignal = cms.string("50x SM HH#rightarrow WWWW,WW#tau#tau,#tau#tau#tau#tau")

process.makePlots.categories = cms.VPSet(
    cms.PSet(
        name = cms.string("hh_1l_3tau_OS_Tight"),
        label = cms.string("1l+3#tau_{h}")
    )
)

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
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/m4Vis'),
        xAxisTitle = cms.string('m_{HH}^{vis} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH}^{vis} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/m4'),
        xAxisTitle = cms.string('m_{HH} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    )
])

process.makePlots.nuisanceParameters.normalization.ZZ    = cms.string("1.0 +/- 0.20")
process.makePlots.nuisanceParameters.normalization.WZ    = cms.string("1.0 +/- 0.20")
process.makePlots.nuisanceParameters.normalization.WW    = cms.string("1.0 +/- 0.20")
process.makePlots.nuisanceParameters.normalization.Other = cms.string("1.0 +/- 0.20")
process.makePlots.nuisanceParameters.normalization.VH    = cms.string("1.0 +/- 0.20")
process.makePlots.nuisanceParameters.normalization.TTH   = cms.string("1.0 +/- 0.20")
process.makePlots.nuisanceParameters.normalization.TH    = cms.string("1.0 +/- 0.20")
