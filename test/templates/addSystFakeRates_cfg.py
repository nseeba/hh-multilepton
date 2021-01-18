import FWCore.ParameterSet.Config as cms

import os

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring('prepareDatacards.root')
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('addSystFakeRates.root')
)

process.addSystFakeRates = cms.PSet(

    process = cms.string("data_fakes"),

    histogramToFit = cms.string("mvaOutput_final"),
    xAxisTitle = cms.string("MVA Discriminant"),
    yAxisTitle = cms.string("dN/dMVA"),

    addSyst = cms.VPSet(),

    outputFileName = cms.string("plots/addSystFakeRates.png")
)
