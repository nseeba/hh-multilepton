import FWCore.ParameterSet.Config as cms
import os

from tthAnalysis.HiggsToTauTau.configs.recommendedMEtFilters_cfi import *
from tthAnalysis.HiggsToTauTau.configs.EvtYieldHistManager_cfi import *
from tthAnalysis.HiggsToTauTau.configs.hhWeight_cfi import hhWeight
from tthAnalysis.HiggsToTauTau.analysisSettings import *

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(100000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('')
)

process.analyze_hh_0l_4tau = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string(''),
    histogramDir = cms.string(''),
    era = cms.string(''),

    triggers_2tau = cms.vstring(),
    use_triggers_2tau = cms.bool(False),

    hadTauSelection = cms.string(''),
    hadTauChargeSelection = cms.string(''),
    apply_hadTauGenMatching = cms.bool(False),

    applyFakeRateWeights = cms.string(""),
    hadTauFakeRateWeight = cms.PSet(
        inputFileName = cms.string(""),
        lead = cms.PSet(
            absEtaBins = cms.vdouble(-1., 1.479, 9.9),
            graphName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/jetToTauFakeRate_mc_hadTaus_pt"),
            applyGraph = cms.bool(True),
            fitFunctionName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/fitFunction_data_div_mc_hadTaus_pt"),
            applyFitFunction = cms.bool(True),
        ),
        sublead = cms.PSet(
            absEtaBins = cms.vdouble(-1., 1.479, 9.9),
            graphName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/jetToTauFakeRate_mc_hadTaus_pt"),
            applyGraph = cms.bool(True),
            fitFunctionName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/fitFunction_data_div_mc_hadTaus_pt"),
            applyFitFunction = cms.bool(True),
        ),
        third = cms.PSet(
            absEtaBins = cms.vdouble(-1., 1.479, 9.9),
            graphName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/jetToTauFakeRate_mc_hadTaus_pt"),
            applyGraph = cms.bool(True),
            fitFunctionName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/fitFunction_data_div_mc_hadTaus_pt"),
            applyFitFunction = cms.bool(True),
        ),
        fourth = cms.PSet(
            absEtaBins = cms.vdouble(-1., 1.479, 9.9),
            graphName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/jetToTauFakeRate_mc_hadTaus_pt"),
            applyGraph = cms.bool(True),
            fitFunctionName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/fitFunction_data_div_mc_hadTaus_pt"),
            applyFitFunction = cms.bool(True),
        )
    ),

    isMC = cms.bool(False),
    central_or_shift = cms.string(''),
    lumiScale = cms.VPSet(),
    ref_genWeight = cms.double(0.),
    apply_genWeight = cms.bool(True),
    apply_DYMCReweighting = cms.bool(False),
    apply_DYMCNormScaleFactors = cms.bool(False),
    apply_topPtReweighting = cms.string(''),
    apply_l1PreFireWeight = cms.bool(True),
    apply_hlt_filter = cms.bool(False),
    apply_met_filters = cms.bool(True),
    cfgMEtFilter = cms.PSet(),
    triggerWhiteList = cms.PSet(),
    apply_hadTauFakeRateSF = cms.bool(False),
    apply_genPhotonFilter = cms.string("disabled"),

    fillGenEvtHistograms = cms.bool(False),
    cfgEvtYieldHistManager = cms.PSet(),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_hadTaus = cms.string('Tau'),
    branchName_jets = cms.string('Jet'),
    branchName_met = cms.string('MET'),
    branchName_vertex = cms.string('PV'),
    branchName_trigObjs = cms.string('TrigObj'),

    branchName_muonGenMatch = cms.string('MuonGenMatch'),
    branchName_electronGenMatch = cms.string('ElectronGenMatch'),
    branchName_hadTauGenMatch = cms.string('TauGenMatch'),
    branchName_jetGenMatch = cms.string('JetGenMatch'),

    branchName_genLeptons = cms.string('GenLep'),
    branchName_genHadTaus = cms.string('GenVisTau'),
    branchName_genPhotons = cms.string('GenPhoton'),
    branchName_genProxyPhotons = cms.string('GenPhotonCandidate'),
    branchName_genFromHardProcess = cms.string('GenIsHardProcess'),
    branchName_genJets = cms.string('GenJet'),
    branchName_genWBosons = cms.string('GenVbosons'),

    redoGenMatching = cms.bool(False),
    genMatchingByIndex = cms.bool(True),
    jetCleaningByIndex = cms.bool(True),

    selEventsFileName_input = cms.string(''),
    selEventsFileName_output = cms.string(''),

    isDEBUG = cms.bool(False),
    hasLHE = cms.bool(True),
    hasPS = cms.bool(False),
    apply_LHE_nom = cms.bool(False),
    useObjectMultiplicity = cms.bool(False),

    selectBDT = cms.bool(False), ## Set it to true for making BDT training Ntuples

    gen_mHH = cms.vdouble(), ## Set the signal mass range used in the BDT .pkl/.xml/.pb files
    mvaInfo_res = cms.PSet(
        BDT_xml_FileName_even_spin2 = cms.string('hhAnalysis/multilepton/data/0l_4tau_odd_half_model_spin2.xml'), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
        BDT_xml_FileName_odd_spin2 = cms.string('hhAnalysis/multilepton/data/0l_4tau_even_half_model_spin2.xml'), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
        fitFunctionFileName_spin2 = cms.string('hhAnalysis/multilepton/data/0l_4tau_TProfile_signal_fit_func_spin2.root'),  ## File contaning the fitted TF1s
        inputVars_spin2 = cms.vstring(
            'tau1_pt', 'tau1_phi', 'diHiggsMass', 'met_phi', 'dr_tau1_tau3',
            'dr_tau2_tau4', 'pt_bestTauHPair_m', 'dr_bestTauHPair_m',
            'dr_bestTauHPair_dr', 'gen_mHH'
        ),
        BDT_xml_FileName_even_spin0 = cms.string('hhAnalysis/multilepton/data/0l_4tau_odd_half_model_spin0.xml'),
        BDT_xml_FileName_odd_spin0 = cms.string('hhAnalysis/multilepton/data/0l_4tau_even_half_model_spin0.xml'),
        fitFunctionFileName_spin0 = cms.string('hhAnalysis/multilepton/data/0l_4tau_TProfile_signal_fit_func_spin0.root'),
        inputVars_spin0 = cms.vstring(
            'tau1_phi', 'tau4_phi', 'diHiggsVisMass', 'diHiggsMass', 'met_LD',
            'deltaEta_tau2_tau3', 'dr_tau2_tau4', 'dr_bestTauHPair_m',
            'dr_secondTauHPair_m', 'gen_mHH'
        ),
    ),
    nonRes_BMs = cms.vstring(),
    mvaInfo_nonres = cms.PSet(
        BDT_xml_FileName_even_nonres = cms.string('hhAnalysis/multilepton/data/0l_4tau_odd_half_model_nonres.xml'),
        BDT_xml_FileName_odd_nonres = cms.string('hhAnalysis/multilepton/data/0l_4tau_even_half_model_nonres.xml'),
        inputVars_nonres = cms.vstring(
            'tau1_pt', 'tau1_eta', 'tau1_phi', 'tau4_pt', 'diHiggsMass', 'mTauTau',
            'STMET', 'met_LD', 'met_phi', 'm_tau2_tau3', 'Zee_bestTauHPair_m',
            'dr_bestTauHPair_m', 'dr_bestTauHPair_dr', 'Zee_secondTauHPair_m',
            'dr_secondTauHPair_dr', 'SM', 'BM1', 'BM2', 'BM3', 'BM4', 'BM5',
            'BM6', 'BM7', 'BM8', 'BM9', 'BM10', 'BM11', 'BM12'
        ),
    ),

    evtWeight = cms.PSet(
        apply = cms.bool(False),
        histogramFile = cms.string(''),
        histogramName = cms.string(''),
        branchNameXaxis = cms.string(''),
        branchNameYaxis = cms.string(''),
        branchTypeXaxis = cms.string(''),
        branchTypeYaxis = cms.string(''),
    ),
    tHweights = cms.VPSet(),
    hhWeight_cfg = hhWeight,
    blacklist = cms.PSet(
        inputFileNames = cms.vstring(),
        sampleName = cms.string(''),
    ),
)
