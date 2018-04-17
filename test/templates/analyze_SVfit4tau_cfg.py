import FWCore.ParameterSet.Config as cms

import os

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring('/home/karl/test_nanoAOD_tools/GluGluToRadionToHHTo4Tau_M-400_narrow_13TeV-madgraph_nanoAOD_1_i.root'),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(100000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('analyze_SVfit4tau.root')
)

process.analyze_SVfit4tau = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string('HH'),

    histogramDir = cms.string('SVfit4tau'),

    era = cms.string('2017'),

    mode = cms.string("rec"), # CV: 'rec', 'gen', or 'gen_smeared'

    leptonSelection = cms.string('Tight'),

    hadTauSelection = cms.string('Tight|dR03mvaMedium'),

    SVfit4tau = cms.PSet(
        logM_wMassConstraint = cms.double(0.),
        logM_woMassConstraint = cms.double(0.)
    ),

    use_HIP_mitigation_mediumMuonId = cms.bool(False),

    isMC = cms.bool(True),
    central_or_shift = cms.string('central'),
    lumiScale = cms.double(1.),
    apply_genWeight = cms.bool(True),

    fillGenEvtHistograms = cms.bool(False),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_hadTaus = cms.string('Tau'),
    branchName_jets = cms.string('Jet'),
    branchName_met = cms.string('MET'),
    branchName_memOutput = cms.string(''),

    branchName_genLeptons1 = cms.string('GenLep'),
    branchName_genLeptons2 = cms.string(''),
    branchName_genHadTaus = cms.string('GenVisTau'),
    branchName_genJets = cms.string('GenJet'),
    redoGenMatching = cms.bool(True),
    
    branchName_genTaus = cms.string('GenTau'),
    branchName_genHiggsBosons = cms.string('GenHiggsBosons'), # CV: use 'GenHiggsBoson' in CMSSW_8_0_x, 'GenHiggs' in  CMSSW_9_4_x

    genHadTauSmearing = cms.PSet(
        inputFileName = cms.string("hhAnalysis/tttt/data/hadTauSmearingCDF_toyMC.root"),
        graphName = cms.string("rCDF")
    ),
    genMEtSmearing = cms.PSet(
        sigmaX = cms.double(10.),
        sigmaY = cms.double(10.)
    ),

    selEventsFileName_input = cms.string(''),
)
