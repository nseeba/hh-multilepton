import FWCore.ParameterSet.Config as cms

import os

from tthAnalysis.HiggsToTauTau.makePlots_mcClosure_cfg import process

process.makePlots.pluginType = cms.string("Plotter_mcClosure")

process.makePlots.processesBackground = cms.vstring(
    "ZZ",
    "WZ",
    "WW",    
    "fakes_data",
    "TT",
    "TTW",
    "TTWW",
    "TTZ",
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
        name = cms.string("3l_1tau_OS_lepFakeable_mcClosure_wFakeRateWeights_tauTight"),
        label = cms.string("3l+1#tau_{h}")
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
        histogramName = cms.string('sel/evt/$PROCESS/mTauTauVis'),
        xAxisTitle = cms.string('m_{#tau#tau}^{vis} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{#tau#tau}^{vis} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/HT'),
        xAxisTitle = cms.string('H_{T} [GeV]'),
        yAxisTitle = cms.string('dN/d}H_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/STMET'),
        xAxisTitle = cms.string('S_{T}^{MET} [GeV]'),
        yAxisTitle = cms.string('dN/dS_{T}^{MET} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/svFit4tau_wMassConstraint/$PROCESS/dihiggsVisMass'),
        xAxisTitle = cms.string('m_{HH}^{vis} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH}^{vis} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/svFit4tau_wMassConstraint/$PROCESS/dihiggsMass1'),
        xAxisTitle = cms.string('m_{HH} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/svFit4tau_woMassConstraint/$PROCESS/ditau1Mass1'),
        xAxisTitle = cms.string('m_{H}^{(1)} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{H}^{(1)} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/svFit4tau_woMassConstraint/$PROCESS/ditau1Mass2'),
        xAxisTitle = cms.string('m_{H}^{(1)} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{H}^{(1)} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/svFit4tau_wMassConstraint/$PROCESS/dihiggsMass2'),
        xAxisTitle = cms.string('m_{HH} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/svFit4tau_woMassConstraint/$PROCESS/ditau2Mass1'),
        xAxisTitle = cms.string('m_{H}^{(2)} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{H}^{(2)} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/svFit4tau_woMassConstraint/$PROCESS/ditau2Mass2'),
        xAxisTitle = cms.string('m_{H}^{(2)} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{H}^{(2)} [1/GeV]')
    )
])

process.makePlots.nuisanceParameters.normalization.ZZ                 = cms.string("1.0 +/- 0.20")
process.makePlots.nuisanceParameters.normalization.WZ                 = cms.string("1.0 +/- 0.20")
process.makePlots.nuisanceParameters.normalization.WW                 = cms.string("1.0 +/- 0.20")
process.makePlots.nuisanceParameters.normalization.Other              = cms.string("1.0 +/- 0.20")
process.makePlots.nuisanceParameters.normalization.VH                 = cms.string("1.0 +/- 0.20")
process.makePlots.nuisanceParameters.normalization.TTH                = cms.string("1.0 +/- 0.20")
process.makePlots.nuisanceParameters.normalization.TH                 = cms.string("1.0 +/- 0.20")
process.makePlots.nuisanceParameters.normalization.signal_nonresonant = cms.string("1.0 +/- 0.20")
