import FWCore.ParameterSet.Config as cms
import os

from tthAnalysis.HiggsToTauTau.configs.recommendedMEtFilters_cfi import *
from tthAnalysis.HiggsToTauTau.configs.EvtYieldHistManager_cfi import *
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

process.analyze_conversions = cms.PSet(
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
    leptonChargeSelection = cms.string(''),

    hadTauChargeSelection = cms.string(''),
    hadTauGenMatch = cms.string('all'),
    hadTauSelection = cms.string(''),
    apply_hadTauGenMatching = cms.bool(False),

    chargeSumSelection = cms.string(''),

    applyFakeRateWeights = cms.string(""),
    leptonFakeRateWeight = cms.PSet(
        inputFileName = cms.string(""),
        histogramName_e = cms.string(""),
        histogramName_mu = cms.string(""),
        era = cms.string(""),
        applyNonClosureCorrection = cms.bool(False),
    ),

    isMC = cms.bool(True),
    isControlRegion = cms.bool(False),
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
    #branchName_jets = cms.string('Jet'),
    branchName_jets_ak4 = cms.string('Jet'),
    branchName_jets_ak8_Wjj = cms.string('FatJetAK8LSLoose'),
    branchName_subjets_ak8_Wjj = cms.string('SubJetAK8LSLoose'),
    #branchName_jets_ak8_Wjj = cms.string('FatJet'),
    #branchName_subjets_ak8_Wjj = cms.string('SubJet'),
    branchName_met = cms.string('MET'),
    branchName_vertex = cms.string('PV'),

    branchName_muonGenMatch = cms.string('MuonGenMatch'),
    branchName_electronGenMatch = cms.string('ElectronGenMatch'),
    branchName_hadTauGenMatch = cms.string('TauGenMatch'),
    branchName_jetGenMatch = cms.string('JetGenMatch'),

    branchName_genLeptons = cms.string('GenLep'),
    branchName_genHadTaus = cms.string('GenVisTau'),
    branchName_genPhotons = cms.string('GenPhoton'),
    branchName_genJets = cms.string('GenJet'),
    branchName_genHiggses = cms.string('GenHiggs'),

    redoGenMatching = cms.bool(False),
    genMatchingByIndex = cms.bool(True),
    jetCleaningByIndex = cms.bool(True),

    branchName_genWBosons = cms.string('GenVbosons'),
    branchName_genWJets = cms.string('GenWZQuark'),
    branchName_genNeutrinos = cms.string('GenNu'),
    
    selEventsFileName_input = cms.string(''),
    selEventsFileName_output = cms.string(''),

    useNonNominal = cms.bool(False),
    isDEBUG = cms.bool(False),
    hasLHE = cms.bool(True),
    hasPS = cms.bool(False),
    apply_LHE_nom = cms.bool(False),
    useObjectMultiplicity = cms.bool(False),


    # 20201201: 9 variable BDT, used for pre-pre-approval 
    gen_mHH = cms.vdouble(), ## Set the signal mass range used in the BDT .pkl/.xml/.pb files
    ## -------- USE THIS FOR TMVAInterface (after changing it in the .cc file) -----------------##
    mvaInfo_res = cms.PSet( 
        BDT_xml_FileName_spin0_even = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/3l_0tau_spin0_oddTrainModel.xml'),
        BDT_xml_FileName_spin0_odd = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/3l_0tau_spin0_evenTrainModel.xml'),
        fitFunctionFileName_spin0 = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/3l_0tau_spin0_fitFuncs.root'), 
        inputVars_spin0 = cms.vstring('m3l', 'diHiggsVisMass', 'mSFOS2l_closestToZ', 'dr_LeptonIdx3_AK4jNear_Approach2', 'dr_LeptonIdx3_2j_inclusive1j_Approach2', 'dr_los_min', 'dr_los_max', 'nSFOS_3l', 'met_LD', 'gen_mHH'),
        BDT_xml_FileName_spin2_even = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/3l_0tau_spin2_oddTrainModel.xml'),
        BDT_xml_FileName_spin2_odd = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/3l_0tau_spin2_evenTrainModel.xml'),
        fitFunctionFileName_spin2 = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/3l_0tau_spin2_fitFuncs.root'), 
        inputVars_spin2 = cms.vstring('m3l', 'diHiggsVisMass', 'mSFOS2l_closestToZ', 'dr_LeptonIdx3_AK4jNear_Approach2', 'dr_LeptonIdx3_2j_inclusive1j_Approach2', 'dr_los_min', 'dr_los_max', 'nSFOS_3l', 'met_LD', 'gen_mHH'),
    ),
    nonRes_BMs = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    mvaInfo_nonRes = cms.PSet( ## [Tweaked hyper-para.s used]
        BDT_xml_FileName_nonRes_even = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/3l_0tau_nonRes_default_oddTrainModel.xml'),
        BDT_xml_FileName_nonRes_odd = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/3l_0tau_nonRes_default_evenTrainModel.xml'),
        inputVars_nonRes = cms.vstring('m3l', 'diHiggsVisMass', 'mSFOS2l_closestToZ', 'dr_LeptonIdx3_AK4jNear_Approach2', 'dr_LeptonIdx3_2j_inclusive1j_Approach2', 'dr_los_min', 'dr_los_max', 'nSFOS_3l', 'met_LD',
                                       'SM', 'BM1', 'BM2', 'BM3', 'BM4', 'BM5', 'BM6', 'BM7', 'BM8', 'BM9', 'BM10', 'BM11', 'BM12'),
    ),


    # 20210109: 23 variable BDT 
    #gen_mHH = cms.vdouble(250,260,270,280,300, 320,350,400,450,500,550,600,650,700,750,800,850,900,1000), ## Set the signal mass range used in the BDT .pkl/.xml/.pb files
    ## -------- USE THIS FOR TMVAInterface (after changing it in the .cc file) -----------------##
    #mvaInfo_res = cms.PSet( 
    #    BDT_xml_FileName_spin0_even = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/spin0_v4_combineBest23vars_pso_kappa0p3_wBestHyperparameters/3l_0tau_odd_half_model_spin0.xml'),
    #    BDT_xml_FileName_spin0_odd  = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/spin0_v4_combineBest23vars_pso_kappa0p3_wBestHyperparameters/3l_0tau_even_half_model_spin0.xml'),
    #    fitFunctionFileName_spin0 = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/3l_0tau_spin0_fitFuncs.root'), 
    #    inputVars_spin0 = cms.vstring(
    #        "nSFOS_3l", "m3l", "diHiggsVisMass", "diHiggsVisMass_inclusive1j", "met",
    #        "mht", "met_LD", "mT_MEtLep1", "mT_LeptonIdx3_Met_Approach2", "dr_lss",
    #        "dr_los_min", "dr_los_max", "mSFOS2l_closestToZ", "m_LeptonIdx1_LeptonIdx2_Approach0", "m_LeptonIdx1_LeptonIdx3_Approach0",
    #        "m_LeptonIdx1_LeptonIdx2_Approach2", "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2", "dPhi_LeptonIdx1_LeptonIdx3_Approach0", "m_LeptonIdx3_Jet1_Approach0", "m_LeptonIdx3_JetNear_Approach0",
    #        "mindr_lep1_jet", "dr_LeptonIdx3_AK4jNear_Approach2", "dr_LeptonIdx3_2j_inclusive1j_Approach2",
    #        "gen_mHH"),
    #    BDT_xml_FileName_spin2_even = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/spin2_v4_combineBest23vars_pso_kappa0p3_wBestHyperparameters/3l_0tau_odd_half_model_spin2.xml'),
    #    BDT_xml_FileName_spin2_odd  = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/spin2_v4_combineBest23vars_pso_kappa0p3_wBestHyperparameters/3l_0tau_even_half_model_spin2.xml'),
    #    fitFunctionFileName_spin2 = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/3l_0tau_spin2_fitFuncs.root'), 
    #    inputVars_spin2 = cms.vstring(
    #        "nSFOS_3l", "m3l", "diHiggsVisMass", "diHiggsVisMass_inclusive1j", "met",
    #        "mht", "met_LD", "mT_MEtLep1", "mT_LeptonIdx3_Met_Approach2", "dr_lss",
    #        "dr_los_min", "dr_los_max", "mSFOS2l_closestToZ", "m_LeptonIdx1_LeptonIdx2_Approach0", "m_LeptonIdx1_LeptonIdx3_Approach0",
    #        "m_LeptonIdx1_LeptonIdx2_Approach2", "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2", "dPhi_LeptonIdx1_LeptonIdx3_Approach0", "m_LeptonIdx3_Jet1_Approach0", "m_LeptonIdx3_JetNear_Approach0",
    #        "mindr_lep1_jet", "dr_LeptonIdx3_AK4jNear_Approach2", "dr_LeptonIdx3_2j_inclusive1j_Approach2",
    #        "gen_mHH"),
    #),
    #nonRes_BMs = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    #mvaInfo_nonRes = cms.PSet( ## [Tweaked hyper-para.s used]
    #    BDT_xml_FileName_nonRes_even = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/nonres_v4_combineBest23vars_pso_kappa0p3_wBestHyperparameters/3l_0tau_odd_half_model_nonres.xml'),
    #    BDT_xml_FileName_nonRes_odd  = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/nonres_v4_combineBest23vars_pso_kappa0p3_wBestHyperparameters/3l_0tau_even_half_model_nonres.xml'),
    #    inputVars_nonRes = cms.vstring(
    #        "nSFOS_3l", "m3l", "diHiggsVisMass", "diHiggsVisMass_inclusive1j", "met",
    #        "mht", "met_LD", "mT_MEtLep1", "mT_LeptonIdx3_Met_Approach2", "dr_lss",
    #        "dr_los_min", "dr_los_max", "mSFOS2l_closestToZ", "m_LeptonIdx1_LeptonIdx2_Approach0", "m_LeptonIdx1_LeptonIdx3_Approach0",
    #        "m_LeptonIdx1_LeptonIdx2_Approach2", "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2", "dPhi_LeptonIdx1_LeptonIdx3_Approach0", "m_LeptonIdx3_Jet1_Approach0", "m_LeptonIdx3_JetNear_Approach0",
    #        "mindr_lep1_jet", "dr_LeptonIdx3_AK4jNear_Approach2", "dr_LeptonIdx3_2j_inclusive1j_Approach2",
    #        "SM", "BM1", "BM2", "BM3", "BM4", "BM5", "BM6", "BM7", "BM8", "BM9", "BM10", "BM11", "BM12"),
    #),

    
    # 20210109: 18 variable BDT 
    #gen_mHH = cms.vdouble(250,260,270,280,300, 320,350,400,450,500,550,600,650,700,750,800,850,900,1000), ## Set the signal mass range used in the BDT .pkl/.xml/.pb files
    ## -------- USE THIS FOR TMVAInterface (after changing it in the .cc file) -----------------##
    #mvaInfo_res = cms.PSet( 
    #    BDT_xml_FileName_spin0_even = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/spin0_v4_combineBest23vars_pso_kappa0p3_wBestHyperparameters_remove5vars/3l_0tau_odd_half_model_spin0.xml'),
    #    BDT_xml_FileName_spin0_odd  = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/spin0_v4_combineBest23vars_pso_kappa0p3_wBestHyperparameters_remove5vars/3l_0tau_even_half_model_spin0.xml'),
    #    fitFunctionFileName_spin0 = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/3l_0tau_spin0_fitFuncs.root'), 
    #    inputVars_spin0 = cms.vstring(
    #        "nSFOS_3l", "m3l", "diHiggsVisMass_inclusive1j", 
    #        "met_LD", "mT_MEtLep1", "mT_LeptonIdx3_Met_Approach2", "dr_lss",
    #        "dr_los_min", "dr_los_max", "mSFOS2l_closestToZ", "m_LeptonIdx1_LeptonIdx2_Approach0", 
    #        "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2", "dPhi_LeptonIdx1_LeptonIdx3_Approach0", "m_LeptonIdx3_Jet1_Approach0", "m_LeptonIdx3_JetNear_Approach0",
    #        "mindr_lep1_jet", "dr_LeptonIdx3_AK4jNear_Approach2", "dr_LeptonIdx3_2j_inclusive1j_Approach2",
    #        "gen_mHH"),
    #    BDT_xml_FileName_spin2_even = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/spin2_v4_combineBest23vars_pso_kappa0p3_wBestHyperparameters_remove5vars/3l_0tau_odd_half_model_spin2.xml'),
    #    BDT_xml_FileName_spin2_odd  = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/spin2_v4_combineBest23vars_pso_kappa0p3_wBestHyperparameters_remove5vars/3l_0tau_even_half_model_spin2.xml'),
    #    fitFunctionFileName_spin2 = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/3l_0tau_spin2_fitFuncs.root'), 
    #    inputVars_spin2 = cms.vstring(
    #        "nSFOS_3l", "m3l", "diHiggsVisMass_inclusive1j", 
    #        "met_LD", "mT_MEtLep1", "mT_LeptonIdx3_Met_Approach2", "dr_lss",
    #        "dr_los_min", "dr_los_max", "mSFOS2l_closestToZ", "m_LeptonIdx1_LeptonIdx2_Approach0", 
    #        "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2", "dPhi_LeptonIdx1_LeptonIdx3_Approach0", "m_LeptonIdx3_Jet1_Approach0", "m_LeptonIdx3_JetNear_Approach0",
    #        "mindr_lep1_jet", "dr_LeptonIdx3_AK4jNear_Approach2", "dr_LeptonIdx3_2j_inclusive1j_Approach2",
    #        "gen_mHH"),
    #),
    #nonRes_BMs = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    #mvaInfo_nonRes = cms.PSet( ## [Tweaked hyper-para.s used]
    #    BDT_xml_FileName_nonRes_even = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/nonres_v4_combineBest23vars_pso_kappa0p3_wBestHyperparameters_remove5vars/3l_0tau_odd_half_model_nonres.xml'),
    #    BDT_xml_FileName_nonRes_odd  = cms.string('hhAnalysis/multilepton/data/BDT_3l_0tau/nonres_v4_combineBest23vars_pso_kappa0p3_wBestHyperparameters_remove5vars/3l_0tau_even_half_model_nonres.xml'),
    #    inputVars_nonRes = cms.vstring(
    #        "nSFOS_3l", "m3l", "diHiggsVisMass_inclusive1j", 
    #        "met_LD", "mT_MEtLep1", "mT_LeptonIdx3_Met_Approach2", "dr_lss",
    #        "dr_los_min", "dr_los_max", "mSFOS2l_closestToZ", "m_LeptonIdx1_LeptonIdx2_Approach2", 
    #        "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2", "dPhi_LeptonIdx1_LeptonIdx3_Approach0", "m_LeptonIdx3_Jet1_Approach0", "m_LeptonIdx3_JetNear_Approach0",
    #        "mindr_lep1_jet", "dr_LeptonIdx3_AK4jNear_Approach2", "dr_LeptonIdx3_2j_inclusive1j_Approach2",
    #        "SM", "BM1", "BM2", "BM3", "BM4", "BM5", "BM6", "BM7", "BM8", "BM9", "BM10", "BM11", "BM12"),
    #),

    
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
)
