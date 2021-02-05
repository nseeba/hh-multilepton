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

process.analyze_hh_4l = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string(''),
    histogramDir = cms.string(''),
    era = cms.string(''),

    triggers_1e = cms.vstring(),
    use_triggers_1e = cms.bool(True),
    triggers_1mu = cms.vstring(),
    use_triggers_1mu = cms.bool(True),

    triggers_2e = cms.vstring(),
    use_triggers_2e = cms.bool(True),
    triggers_1e1mu = cms.vstring(),
    use_triggers_1e1mu = cms.bool(True),
    triggers_2mu = cms.vstring(),
    use_triggers_2mu = cms.bool(True),

    triggers_3e = cms.vstring(),
    use_triggers_3e = cms.bool(False),
    triggers_2e1mu = cms.vstring(),
    use_triggers_2e1mu = cms.bool(False),
    triggers_1e2mu = cms.vstring(),
    use_triggers_1e2mu = cms.bool(False),
    triggers_3mu = cms.vstring(),
    use_triggers_3mu = cms.bool(False),

    apply_offline_e_trigger_cuts_1e = cms.bool(True),
    apply_offline_e_trigger_cuts_1mu = cms.bool(True),
    apply_offline_e_trigger_cuts_2e = cms.bool(True),
    apply_offline_e_trigger_cuts_1e1mu = cms.bool(True),
    apply_offline_e_trigger_cuts_2mu = cms.bool(True),
    apply_offline_e_trigger_cuts_3e = cms.bool(True),
    apply_offline_e_trigger_cuts_2e1mu = cms.bool(True),
    apply_offline_e_trigger_cuts_1e2mu = cms.bool(True),
    apply_offline_e_trigger_cuts_3mu = cms.bool(True),

    electronSelection = cms.string(''),
    muonSelection = cms.string(''),
    apply_leptonGenMatching = cms.bool(True),
    hadTauSelection = cms.string(''),

    leptonChargeSelection = cms.string(''),

    applyFakeRateWeights = cms.string(""),
    leptonFakeRateWeight = cms.PSet(
        inputFileName = cms.string(""),
        histogramName_e = cms.string(""),
        histogramName_mu = cms.string(""),
        era = cms.string(""),
        applyNonClosureCorrection = cms.bool(False),
    ),

    isMC = cms.bool(True),
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
    invert_ZbosonMassVeto = cms.bool(False),
    cfgMEtFilter = cms.PSet(),
    triggerWhiteList = cms.PSet(),

    fillGenEvtHistograms = cms.bool(False),
    cfgEvtYieldHistManager = cms.PSet(),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_hadTaus = cms.string('Tau'),
    branchName_jets = cms.string('Jet'),
    branchName_met = cms.string('MET'),
    branchName_vertex = cms.string('PV'),
    branchName_memOutput = cms.string(''),

    branchName_muonGenMatch = cms.string('MuonGenMatch'),
    branchName_electronGenMatch = cms.string('ElectronGenMatch'),
    branchName_hadTauGenMatch = cms.string('TauGenMatch'),
    branchName_jetGenMatch = cms.string('JetGenMatch'),

    branchName_genLeptons = cms.string('GenLep'),
    branchName_genHadTaus = cms.string('GenVisTau'),
    branchName_genPhotons = cms.string('GenPhoton'),
    branchName_genJets = cms.string('GenJet'),
    branchName_genWBosons = cms.string('GenVbosons'),

    redoGenMatching = cms.bool(False),
    genMatchingByIndex = cms.bool(True),
    jetCleaningByIndex = cms.bool(True),

    selEventsFileName_input = cms.string(''),
    selEventsFileName_output = cms.string(''),

    useNonNominal = cms.bool(False),
    isDEBUG = cms.bool(False),
    hasLHE = cms.bool(True),
    hasPS = cms.bool(False),
    apply_LHE_nom = cms.bool(False),
    useObjectMultiplicity = cms.bool(False),

    selectBDT = cms.bool(False),
    gen_mHH = cms.vdouble(), ## Set the signal mass range used in the BDT .pkl/.xml/.pb files
        ## -------- USE THIS FOR TMVAInterface (after changing it in the .cc file) -----------------##
    mvaInfo_res = cms.PSet( 
        BDT_xml_FileName_spin0_even = cms.string('hhAnalysis/multilepton/data/BDT_4l/4l_even_half_model_spin0.xml'),
        BDT_xml_FileName_spin0_odd = cms.string('hhAnalysis/multilepton/data/BDT_4l/4l_odd_half_model_spin0.xml'),
        fitFunctionFileName_spin0 = cms.string('hhAnalysis/multilepton/data/BDT_4l/4l_TProfile_signal_fit_func_spin0.root'), 
        inputVars_spin0 = cms.vstring('dihiggsVisMass_sel', 'maxPtSum_pair1_m', 'maxPtSum_pair2_deltaEtaLep1', 'maxPtSum_pair2_deltaEta', 'maxPtSum_pair2_deltaPhi', 'maxPtSum_pair2_m', 'MET', 'METDeltaPhiLep1', 'HTmiss', 'gen_mHH'),
        BDT_xml_FileName_spin2_even = cms.string('hhAnalysis/multilepton/data/BDT_4l/4l_even_half_model_spin2.xml'),
        BDT_xml_FileName_spin2_odd = cms.string('hhAnalysis/multilepton/data/BDT_4l/4l_odd_half_model_spin2.xml'),
        fitFunctionFileName_spin2 = cms.string('hhAnalysis/multilepton/data/BDT_4l/4l_TProfile_signal_fit_func_spin2.root'), 
        inputVars_spin2 = cms.vstring('dihiggsVisMass_sel', 'maxPtSum_pair1_m', 'maxPtSum_pair2_deltaEtaLep1', 'maxPtSum_pair2_deltaEta', 'maxPtSum_pair2_deltaPhi', 'maxPtSum_pair2_m', 'MET', 'METDeltaPhiLep1', 'HTmiss', 'gen_mHH'),
    ),
    nonRes_BMs = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    mvaInfo_nonRes = cms.PSet( ## [Tweaked hyper-para.s used]
        BDT_xml_FileName_nonRes_even = cms.string('hhAnalysis/multilepton/data/BDT_4l/4l_even_half_model_nonres_default.xml'),
        BDT_xml_FileName_nonRes_odd = cms.string('hhAnalysis/multilepton/data/BDT_4l/4l_odd_half_model_nonres_default.xml'),
        inputVars_nonRes = cms.vstring('dihiggsVisMass_sel', 'HT', 'maxPtSum_pair1_deltaPhi', 'maxPtSum_pair1_m', 'maxPtSum_pair2_deltaPhiLep1', 'maxPtSum_pair2_m', 'MET', 'METDeltaPhiLep1', 'HTmiss', 'SM', 'BM1', 'BM2', 'BM3', 'BM4', 'BM5', 'BM6', 'BM7', 'BM8', 'BM9', 'BM10', 'BM11', 'BM12'),
    ),

    mvaInfo_nonRes_base = cms.PSet( ## [Tweaked hyper-para.s used]                                                                                                                                
        BDT_xml_FileName_nonRes_base_even = cms.string('hhAnalysis/multilepton/data/BDT_4l/4l_even_half_model_nonres_base.xml'),
        BDT_xml_FileName_nonRes_base_odd = cms.string('hhAnalysis/multilepton/data/BDT_4l/4l_odd_half_model_nonres_base.xml'),
        inputVars_nonRes_base = cms.vstring('dihiggsVisMass_sel', 'HT', 'maxPtSum_pair1_deltaPhi', 'maxPtSum_pair1_m', 'maxPtSum_pair2_deltaPhiLep1', 'maxPtSum_pair2_m', 'MET', 'METDeltaPhiLep1', 'HTmiss'),
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
)
