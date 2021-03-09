#include "hhAnalysis/multilepton/interface/EvtHistManager_conversions.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), getLogWeight()
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include <TMath.h>

const int analysisRunLevel = 0; // 0: only nEvent histo, 1: all category histo, 2: all histo

EvtHistManager_conversions::EvtHistManager_conversions(const edm::ParameterSet & cfg, bool isControlRegion)
  : HistManagerBase(cfg)
{
  isControlRegion_ = isControlRegion;
  
  const std::vector<std::string> sysOpts_central = {
    "numElectrons",
    "numMuons",
    "nJetAK4",
    "nBJetLoose",
    "nJetAK8_wSelectorAK8_Wjj",
    //
    "sumLeptonCharge_3l",
    "numSameFlavor_OS_Full",
    "numSameFlavor_OS_3l",
    //
    "lep1_pt",
    "lep1_conePt",
    "lep1_eta",
    "mindr_lep1_jet",
    "mT_MEtLep1",
    //
    "lep2_pt",
    "lep2_conePt",
    "lep2_eta",
    "mindr_lep2_jet",
    "mT_MEtLep2",
    //
    "lep3_pt",
    "lep3_conePt",
    "lep3_eta",
    "mindr_lep3_jet",
    "mT_MEtLep3",
    //
    "jet1_pt",
    "jet1_eta",
    "jet2_pt",
    "jet2_eta",
    "jet1plus2_pt",
    "jet1plus2_eta",
    "jet1_m",
    "jet2_m",
    //
    "met",
    "mht",
    "met_LD",
    "HT",
    "STMET",
    //
    "mSFOS2l_closestToZ",
    "m3l",
    "WTojjMass",
    "dihiggsVisMass_sel",
    "dihiggsVisMass_sel_inclusive1j",
    "dihiggsMass",
    "dihiggsMass_inclusive1j",
    //
    "mTMetLepton1_chargeEqualSumCharge3l",
    "mTMetLepton2_chargeEqualSumCharge3l",
    //
    "dr_l12",
    "dr_l23",
    "dr_l13",
    "dr_lss",
    "dr_los_min",
    "dr_los_max",
    //		   //
    "avg_dr_jet",
    "dr_Wjj",
    //
    "dPhi_3l_2j",
    "dPhi_3l_2j_inclusive1j",
    "dEta_3l_2j",
    "dEta_3l_2j_inclusive1j",
    "dR_3l_2j",
    "dR_3l_2j_inclusive1j",
    //
    "dEta_3l_avg2j",
    "dEta_3l_avg2j_inclusive1j",
    //
    "bTag_jet1",
    "bTag_jet2",
    "bTag_sum_jet1And2",
    "bTag_max_jet1or2",
    "bTag_max_AK4",
    "bTag_sum_AK4",
    //
    "pt_lastAK4",
    //
    "m_AK8",
    //
    //
    "mT_LeptonIdx1_Met_Approach0",
    "mT_LeptonIdx2_Met_Approach0",
    "mT_LeptonIdx3_Met_Approach0",
    //
    "m_LeptonIdx1_LeptonIdx2_Approach0",
    "m_LeptonIdx2_LeptonIdx3_Approach0",
    "m_LeptonIdx1_LeptonIdx3_Approach0",
    //
    "dPhi_LeptonIdx1_LeptonIdx2_Approach0",
    "dPhi_LeptonIdx2_LeptonIdx3_Approach0",
    "dPhi_LeptonIdx1_LeptonIdx3_Approach0",
    //
    "dEta_LeptonIdx1_LeptonIdx2_Approach0",
    "dEta_LeptonIdx2_LeptonIdx3_Approach0",
    "dEta_LeptonIdx1_LeptonIdx3_Approach0",
    //
    "dr_LeptonIdx1_LeptonIdx2_Approach0",
    "dr_LeptonIdx2_LeptonIdx3_Approach0",
    "dr_LeptonIdx1_LeptonIdx3_Approach0",
    //
    "m_LeptonIdx3_Jet1_Approach0",
    "dr_LeptonIdx3_Jet1_Approach0",
    //
    "m_LeptonIdx3_JetNear_Approach0",
    "dr_LeptonIdx3_JetNear_Approach0",
    //
    "dr_LeptonIdx3_2j_Approach0",
    "dr_LeptonIdx3_2j_inclusive1j_Approach0",
    //
    "dr_LeptonIdx3_AK4jNear_Approach0",
    "dr_LeptonIdx3_2AK4jNear_Approach0",
    "dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach0",
    "m_LeptonIdx3_2AK4jNear_Approach0",
    "m_LeptonIdx3_2AK4jNear_inclusive1j_Approach0",
    "dr_2AK4J_NearestToLeptonIdx3_Approach0",
    //
    "dr_LeptonIdx3_AK8_Approach0",
    "m_LeptonIdx3_AK8_Approach0",
    //
    "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0",
    //
    "dPhi_LeptonIdx3_Met_Approach0",
    //
    //
    "mT_LeptonIdx1_Met_Approach2",
    "mT_LeptonIdx2_Met_Approach2",
    "mT_LeptonIdx3_Met_Approach2",
    //
    "m_LeptonIdx1_LeptonIdx2_Approach2",
    "m_LeptonIdx2_LeptonIdx3_Approach2",
    "m_LeptonIdx1_LeptonIdx3_Approach2",
    //
    "dPhi_LeptonIdx1_LeptonIdx2_Approach2",
    "dPhi_LeptonIdx2_LeptonIdx3_Approach2",
    "dPhi_LeptonIdx1_LeptonIdx3_Approach2",
    //
    "dEta_LeptonIdx1_LeptonIdx2_Approach2",
    "dEta_LeptonIdx2_LeptonIdx3_Approach2",
    "dEta_LeptonIdx1_LeptonIdx3_Approach2",
    //
    "dr_LeptonIdx1_LeptonIdx2_Approach2",
    "dr_LeptonIdx2_LeptonIdx3_Approach2",
    "dr_LeptonIdx1_LeptonIdx3_Approach2",
    //
    "m_LeptonIdx3_Jet1_Approach2",
    "dr_LeptonIdx3_Jet1_Approach2",
    //
    "m_LeptonIdx3_JetNear_Approach2",
    "dr_LeptonIdx3_JetNear_Approach2",
    //
    "dr_LeptonIdx3_2j_Approach2",
    "dr_LeptonIdx3_2j_inclusive1j_Approach2",
    //
    "dr_LeptonIdx3_AK4jNear_Approach2",
    "dr_LeptonIdx3_2AK4jNear_Approach2",
    "dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach2",
    "m_LeptonIdx3_2AK4jNear_Approach2",
    "m_LeptonIdx3_2AK4jNear_inclusive1j_Approach2",
    "dr_2AK4J_NearestToLeptonIdx3_Approach2",
    //
    "dr_LeptonIdx3_AK8_Approach2",
    "m_LeptonIdx3_AK8_Approach2",
    //
    "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2",
    //
    "dPhi_LeptonIdx3_Met_Approach2",
    //
    //
    "mT_LeptonIdx1_Met_Approach3",
    "mT_LeptonIdx2_Met_Approach3",
    "mT_LeptonIdx3_Met_Approach3",
    //
    "m_LeptonIdx1_LeptonIdx2_Approach3",
    "m_LeptonIdx2_LeptonIdx3_Approach3",
    "m_LeptonIdx1_LeptonIdx3_Approach3",
    //
    "dPhi_LeptonIdx1_LeptonIdx2_Approach3",
    "dPhi_LeptonIdx2_LeptonIdx3_Approach3",
    "dPhi_LeptonIdx1_LeptonIdx3_Approach3",
    //
    "dEta_LeptonIdx1_LeptonIdx2_Approach3",
    "dEta_LeptonIdx2_LeptonIdx3_Approach3",
    "dEta_LeptonIdx1_LeptonIdx3_Approach3",
    //
    "dr_LeptonIdx1_LeptonIdx2_Approach3",
    "dr_LeptonIdx2_LeptonIdx3_Approach3",
    "dr_LeptonIdx1_LeptonIdx3_Approach3",
    //
    "m_LeptonIdx3_Jet1_Approach3",
    "dr_LeptonIdx3_Jet1_Approach3",
    //
    "m_LeptonIdx3_JetNear_Approach3",
    "dr_LeptonIdx3_JetNear_Approach3",
    //
    "dr_LeptonIdx3_2j_Approach3",
    "dr_LeptonIdx3_2j_inclusive1j_Approach3",
    //
    "dr_LeptonIdx3_AK4jNear_Approach3",
    "dr_LeptonIdx3_2AK4jNear_Approach3",
    "dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach3",
    "m_LeptonIdx3_2AK4jNear_Approach3",
    "m_LeptonIdx3_2AK4jNear_inclusive1j_Approach3",
    "dr_2AK4J_NearestToLeptonIdx3_Approach3",
    //
    "dr_LeptonIdx3_AK8_Approach3",
    "m_LeptonIdx3_AK8_Approach3",
    //
    "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3",
    //
    "dPhi_LeptonIdx3_Met_Approach3",
    //
    //
    //
    "dPhi_2lSFOS_one2lSFOSEvt",
    "dR_2lSFOS_one2lSFOSEvt",
    "m_2lSFOS_one2lSFOSEvt",
    "mT_LeptonNonSFOS_Met_one2lSFOSEvt",
    "dPhi_LeptonNonSFOS_Met_one2lSFOSEvt",
    //
    //
    "eventCategory",
    //
    //
    //
    // WZctrl
    // WZctrl 2lss
    "jetMass_sel_WZctrl_2lss",
    "leptonPairMass_sel_WZctrl_2lss",
    "mindr_lep1_jet_WZctrl_2lss",
    "mT_lep1_WZctrl_2lss",
    "mindr_lep2_jet_WZctrl_2lss",
    "mT_lep2_WZctrl_2lss",
    "dR_ll_WZctrl_2lss",
    "max_lep_eta_WZctrl_2lss",
    //
    "nLostHits_selElectron",
    "passesConversionVeto_selElectron",
    "ntightLeptonsFull"
  };
  const std::vector<std::string> sysOpts_all = {
    //"mvaOutput_xgb_conversions_SUMBk_HH",
    "EventCounter",
    // WZctrl
    "mT_WZctrl_leptonW_MET",
  };
  
  for(const std::string & sysOpt: sysOpts_central)
  {
    central_or_shiftOptions_[sysOpt] = { "central" };
  }
  for(const std::string & sysOpt: sysOpts_all)
  {
    central_or_shiftOptions_[sysOpt] = { "*" };
  } 
}

const TH1 *
EvtHistManager_conversions::getHistogram_EventCounter() const
{
  return hEventCounter_;
}

void
EvtHistManager_conversions::bookHistograms(TFileDirectory & dir)
{
  hEventCounter_                                       = book1D(dir, "EventCounter", "EventCounter",                              1, -0.5, +0.5);

  hm3l_                                                = book1D(dir, "m3l",                                               "m3l",                                              200, 0,  600);
  hdihiggsVisMass_sel_                                 = book1D(dir, "dihiggsVisMass_sel",                                "dihiggsVisMass_sel",                               200, 0, 1500);
  hmSFOS2l_closestToZ_                                 = book1D(dir, "mSFOS2l_closestToZ",                                "mSFOS2l_closestToZ",                                40, 0,  320);
  hdr_LeptonIdx3_AK4jNear_Approach2_                   = book1D(dir, "dr_LeptonIdx3_AK4jNear_Approach2",                  "dr_LeptonIdx3_AK4jNear_Approach2",                 100, 0,   7);
  hdr_LeptonIdx3_2j_inclusive1j_Approach2_             = book1D(dir, "dr_LeptonIdx3_2j_inclusive1j_Approach2",            "dr_LeptonIdx3_2j_inclusive1j_Approach2",           100, 0,   7);
  hdr_los_min_                                         = book1D(dir, "dr_los_min",                                        "dr_los_min",                                       100, 0, 7); 
  hdr_los_max_                                         = book1D(dir, "dr_los_max",                                        "dr_los_max",                                       100, 0, 7);
  hnumSameFlavor_OS_3l_                                = book1D(dir, "numSameFlavor_OS_3l",                               "numSameFlavor_OS_3l",                               9, -0.5,  +8.5);  
  hmet_LD_                                             = book1D(dir, "met_LD",                                            "met_LD",                                           200, 0,500);


  hnumElectrons_                                       = book1D(dir, "numElectrons",                                      "numElectrons",                                      5, -0.5,  +4.5); 
  hnumMuons_                                           = book1D(dir, "numMuons",                                          "numMuons",                                          5, -0.5,  +4.5);
  hnJetAK4_                                            = book1D(dir, "nJetAK4",                                           "nJetAK4",                                          20, -0.5, +19.5);
  hnJetAK8_wSelectorAK8_Wjj_                           = book1D(dir, "nJetAK8_wSelectorAK8_Wjj",                          "nJetAK8_wSelectorAK8_Wjj",                         20, -0.5, +19.5);


  hdihiggsVisMass_sel_inclusive1j_                     = book1D(dir, "dihiggsVisMass_sel_inclusive1j",                    "dihiggsVisMass_sel_inclusive1j",                   200, 0, 1500); 
  hmet_                                                = book1D(dir, "met",                                               "met",                                              200, 0,500); 
  hmht_                                                = book1D(dir, "mht",                                               "mht",                                              200, 0,500); 

  hmT_MEtLep1_                                         = book1D(dir, "mT_MEtLep1",                                        "mT_MEtLep1",                                      100, 0,500);
  hmindr_lep1_jet_                                     = book1D(dir, "mindr_lep1_jet",                                    "mindr_lep1_jet",                                  100, 0, 7);
  
  hdr_lss_                                             = book1D(dir, "dr_lss",                                            "dr_lss",                                           100, 0, 7);

  hm_LeptonIdx1_LeptonIdx2_Approach0_                  = book1D(dir, "m_LeptonIdx1_LeptonIdx2_Approach0",                 "m_LeptonIdx1_LeptonIdx2_Approach0",                 50, 0, 200);
  hm_LeptonIdx1_LeptonIdx3_Approach0_                  = book1D(dir, "m_LeptonIdx1_LeptonIdx3_Approach0",                 "m_LeptonIdx1_LeptonIdx3_Approach0",                 50, 0, 200);
  hdPhi_LeptonIdx1_LeptonIdx3_Approach0_               = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx3_Approach0",              "dPhi_LeptonIdx1_LeptonIdx3_Approach0",              100, 0,   TMath::Pi());
  hm_LeptonIdx3_Jet1_Approach0_                        = book1D(dir, "m_LeptonIdx3_Jet1_Approach0",                       "m_LeptonIdx3_Jet1_Approach0",                       100, 0, 500);
  hm_LeptonIdx3_JetNear_Approach0_                     = book1D(dir, "m_LeptonIdx3_JetNear_Approach0",                    "m_LeptonIdx3_JetNear_Approach0",                    100, 0, 500);
  
  hmT_LeptonIdx3_Met_Approach2_                        = book1D(dir, "mT_LeptonIdx3_Met_Approach2",                       "mT_LeptonIdx3_Met_Approach2",                      100, 0, 500);
  hm_LeptonIdx1_LeptonIdx2_Approach2_                  = book1D(dir, "m_LeptonIdx1_LeptonIdx2_Approach2",                 "m_LeptonIdx1_LeptonIdx2_Approach2",                 50, 0, 200);
  hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2_   = book1D(dir, "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2",   "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2", 100, 0, TMath::Pi());

  
  if (isControlRegion_)
  {
    hmT_WZctrl_leptonW_MET_                            = book1D(dir, "mT_WZctrl_leptonW_MET",                             "mT_WZctrl_leptonW_MET",                           100, 0,500);

    hjetMass_sel_WZctrl_2lss_                          = book1D(dir, "jetMass_sel_WZctrl_2lss",                           "jetMass_sel_WZctrl_2lss",                         200, 0,  600);
    hleptonPairMass_sel_WZctrl_2lss_                   = book1D(dir, "leptonPairMass_sel_WZctrl_2lss",                    "leptonPairMass_sel_WZctrl_2lss",                  200, 0,  600);
    hmindr_lep1_jet_WZctrl_2lss_                       = book1D(dir, "mindr_lep1_jet_WZctrl_2lss",                        "mindr_lep1_jet_WZctrl_2lss",                      100, 0,   10);
    hmT_lep1_WZctrl_2lss_                              = book1D(dir, "mT_lep1_WZctrl_2lss",                               "mT_lep1_WZctrl_2lss",                             100, 0,500);
    hmindr_lep2_jet_WZctrl_2lss_                       = book1D(dir, "mindr_lep2_jet_WZctrl_2lss",                        "mindr_lep2_jet_WZctrl_2lss",                      100, 0,   10);
    hmT_lep2_WZctrl_2lss_                              = book1D(dir, "mT_lep2_WZctrl_2lss",                               "mT_lep2_WZctrl_2lss",                             100, 0,500);
    hdR_ll_WZctrl_2lss_                                = book1D(dir, "dR_ll_WZctrl_2lss",                                 "dR_ll_WZctrl_2lss",                               100, 0,   7);
    hmax_lep_eta_WZctrl_2lss_                          = book1D(dir, "max_lep_eta_WZctrl_2lss",                           "max_lep_eta_WZctrl_2lss",                         100, 0,   3);

    hnLostHits_selElectron_                            = book1D(dir, "nLostHits_selElectron",                             "nLostHits_selElectron",                           12, -1.5,10.5);
    hpassesConversionVeto_selElectron_                 = book1D(dir, "passesConversionVeto_selElectron",                  "passesConversionVeto_selElectron",                 3, -1.5,1.5);
    hntightLeptonsFull_                                = book1D(dir, "ntightLeptonsFull",                             "ntightLeptonsFull",                           11, -0.5,10.5);
  }

  
  //
  //hmvaOutput_xgb_conversions_SUMBk_HH_    = book1D(dir, "mvaOutput_xgb_conversions_SUMBk_HH","mvaOutput_xgb_conversions_SUMBk_HH",120,  0., 1.);
  //


  if (analysisRunLevel >= 1)
  {  
  hnBJetLoose_                                         = book1D(dir, "nBJetLoose",                                        "nBJetLoose",                                       20, -0.5, +19.5 ); 
  //  
  hsumLeptonCharge_3l_                                 = book1D(dir, "sumLeptonCharge_3l",                                "sumLeptonCharge_3l",                                7, -3.5,  +3.5);
  hnumSameFlavor_OS_Full_                              = book1D(dir, "numSameFlavor_OS_FullPresel",                       "numSameFlavor_OS_FullPresel",                       9, -0.5,  +8.5); 
  
  //
  hlep1_pt_                                            = book1D(dir, "lep1_pt",                                           "lep1_pt",                                         100, 0,400); 
  hlep1_conePt_                                        = book1D(dir, "lep1_conePt",                                       "lep1_conePt",                                     100, 0,400); 
  hlep1_eta_                                           = book1D(dir, "lep1_eta",                                          "lep1_eta",                                        100,-5,5); 
  
  
  //
  hlep2_pt_                                            = book1D(dir, "lep2_pt",                                           "lep2_pt",                                         100, 0,400); 
  hlep2_conePt_                                        = book1D(dir, "lep2_conePt",                                       "lep2_conePt",                                     100, 0,400); 
  hlep2_eta_                                           = book1D(dir, "lep2_eta",                                          "lep2_eta",                                        100,-5,5); 
  hmindr_lep2_jet_                                     = book1D(dir, "mindr_lep2_jet",                                    "mindr_lep2_jet",                                  100, 0, 7); 
  hmT_MEtLep2_                                         = book1D(dir, "mT_MEtLep2",                                        "mT_MEtLep2",                                      100, 0,500);
  //
  hlep3_pt_                                            = book1D(dir, "lep3_pt",                                           "lep3_pt",                                         100, 0,400); 
  hlep3_conePt_                                        = book1D(dir, "lep3_conePt",                                       "lep3_conePt",                                     100, 0,400); 
  hlep3_eta_                                           = book1D(dir, "lep3_eta",                                          "lep3_eta",                                        100,-5,5); 
  hmindr_lep3_jet_                                     = book1D(dir, "mindr_lep3_jet",                                    "mindr_lep3_jet",                                  100, 0, 7); 
  hmT_MEtLep3_                                         = book1D(dir, "mT_MEtLep3",                                        "mT_MEtLep3",                                      100, 0,500);
  //
  hjet1_pt_                                            = book1D(dir, "jet1_pt",                                           "jet1_pt",                                         120, 0, 600);
  hjet1_eta_                                           = book1D(dir, "jet1_eta",                                          "jet1_eta",                                        100,-5,5); 
  hjet2_pt_                                            = book1D(dir, "jet2_pt",                                           "jet2_pt",                                         120, 0, 600);
  hjet2_eta_                                           = book1D(dir, "jet2_eta",                                          "jet2_eta",                                        100,-5,5); 
  hjet1plus2_pt_                                       = book1D(dir, "jet1plus2_pt",                                      "jet1plus2_pt",                                    240, 0,1200);
  hjet1plus2_eta_                                      = book1D(dir, "jet1plus2_eta",                                     "jet1plus2_eta",                                   100,-5,5); 
  hjet1_m_                                             = book1D(dir, "jet1_m",                                            "jet1_m",                                           50, 0, 200); 
  hjet2_m_                                             = book1D(dir, "jet2_m",                                            "jet2_m",                                           50, 0, 200);
  //
  
  hHT_                                                 = book1D(dir, "HT",                                                "HT",                                               200, 0,1000); 
  hSTMET_                                              = book1D(dir, "STMET",                                             "STMET",                                            200, 0,1000);
  //
  
  
  hWTojjMass_                                          = book1D(dir, "WTojjMass",                                         "WTojjMass",                                        200, 0,  600); 
  
  
  hdihiggsMass_                                        = book1D(dir, "dihiggsMass",                                       "dihiggsMass",                                      200, 0, 1500);
  hdihiggsMass_inclusive1j_                            = book1D(dir, "dihiggsMass_inclusive1j",                           "dihiggsMass_inclusive1j",                          200, 0, 1500);
  //
  hmTMetLepton1_chargeEqualSumCharge3l_                = book1D(dir, "mTMetLepton1_chargeEqualSumCharge3l",               "mTMetLepton1_chargeEqualSumCharge3l",              200, 0,  400); 
  hmTMetLepton2_chargeEqualSumCharge3l_                = book1D(dir, "mTMetLepton2_chargeEqualSumCharge3l",               "mTMetLepton2_chargeEqualSumCharge3l",              200, 0,  400);
  //
  hdr_l12_                                             = book1D(dir, "dr_l12",                                            "dr_l12",                                           100, 0, 7); 
  hdr_l23_                                             = book1D(dir, "dr_l23",                                            "dr_l23",                                           100, 0, 7); 
  hdr_l13_                                             = book1D(dir, "dr_l13",                                            "dr_l13",                                           100, 0, 7); 
  
 
  //
  havg_dr_jet_                                         = book1D(dir, "avg_dr_jet",                                        "avg_dr_jet",                                       100, 0, 7);
  hdr_Wjj_                                             = book1D(dir, "dr_Wjj",                                            "dr_Wjj",                                           100, 0, 7);
  //
  hdPhi_3l_2j_                                         = book1D(dir, "dPhi_3l_2j",                                        "dPhi_3l_2j",                                       100, 0, TMath::Pi());
  hdPhi_3l_2j_inclusive1j_                             = book1D(dir, "dPhi_3l_2j_inclusive1j",                            "dPhi_3l_2j_inclusive1j",                           100, 0, TMath::Pi());
  hdEta_3l_2j_                                         = book1D(dir, "dEta_3l_2j",                                        "dEta_3l_2j",                                       100, 0, 7);
  hdEta_3l_2j_inclusive1j_                             = book1D(dir, "dEta_3l_2j_inclusive1j",                            "dEta_3l_2j_inclusive1j",                           100, 0, 7);
  hdR_3l_2j_                                           = book1D(dir, "dR_3l_2j",                                          "dR_3l_2j",                                         100, 0, 7);
  hdR_3l_2j_inclusive1j_                               = book1D(dir, "dR_3l_2j_inclusive1j",                              "dR_3l_2j_inclusive1j",                             100, 0, 7);
  //
  hdEta_3l_avg2j_                                      = book1D(dir, "dEta_3l_avg2j",                                     "dEta_3l_avg2j",                                    100, 0, 7);
  hdEta_3l_avg2j_inclusive1j_                          = book1D(dir, "dEta_3l_avg2j_inclusive1j",                         "dEta_3l_avg2j_inclusive1j",                        100, 0, 7);
  //
  hbTag_jet1_                                          = book1D(dir, "bTag_jet1",                                         "bTag_jet1",                                         40, 0,  1);
  hbTag_jet2_                                          = book1D(dir, "bTag_jet2",                                         "bTag_jet2",                                         40, 0,  1);
  hbTag_sum_jet1And2_                                  = book1D(dir, "bTag_sum_jet1And2",                                 "bTag_sum_jet1And2",                                 40, 0,  2);
  hbTag_max_jet1or2_                                   = book1D(dir, "bTag_max_jet1or2",                                  "bTag_max_jet1or2",                                  40, 0,  1);
  hbTag_max_AK4_                                       = book1D(dir, "bTag_max_AK4",                                      "bTag_max_AK4",                                      40, 0,  1);
  hbTag_sum_AK4_                                       = book1D(dir, "bTag_sum_AK4",                                      "bTag_sum_AK4",                                      60, 0,  4);
  //
  hpt_lastAK4_                                         = book1D(dir, "pt_lastAK4",                                        "pt_lastAK4",                                       120, 0, 600);
  //
  hm_AK8_                                              = book1D(dir, "m_AK8",                                             "m_AK8",                                            200, 0,  500); 
  //
  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  hmT_LeptonIdx1_Met_Approach0_                        = book1D(dir, "mT_LeptonIdx1_Met_Approach0",                       "mT_LeptonIdx1_Met_Approach0",                      100, 0, 500); 
  hmT_LeptonIdx2_Met_Approach0_                        = book1D(dir, "mT_LeptonIdx2_Met_Approach0",                       "mT_LeptonIdx2_Met_Approach0",                      100, 0, 500); 
  hmT_LeptonIdx3_Met_Approach0_                        = book1D(dir, "mT_LeptonIdx3_Met_Approach0",                       "mT_LeptonIdx3_Met_Approach0",                      100, 0, 500);
  //
  
  hm_LeptonIdx2_LeptonIdx3_Approach0_                  = book1D(dir, "m_LeptonIdx2_LeptonIdx3_Approach0",                 "m_LeptonIdx2_LeptonIdx3_Approach0",                 50, 0, 200); 
  
  //
  hdPhi_LeptonIdx1_LeptonIdx2_Approach0_               = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx2_Approach0",              "dPhi_LeptonIdx1_LeptonIdx2_Approach0",              100, 0,   TMath::Pi()); 
  hdPhi_LeptonIdx2_LeptonIdx3_Approach0_               = book1D(dir, "dPhi_LeptonIdx2_LeptonIdx3_Approach0",              "dPhi_LeptonIdx2_LeptonIdx3_Approach0",              100, 0,   TMath::Pi()); 
  
  //
  hdEta_LeptonIdx1_LeptonIdx2_Approach0_               = book1D(dir, "dEta_LeptonIdx1_LeptonIdx2_Approach0",              "dEta_LeptonIdx1_LeptonIdx2_Approach0",              100, 0,   7); 
  hdEta_LeptonIdx2_LeptonIdx3_Approach0_               = book1D(dir, "dEta_LeptonIdx2_LeptonIdx3_Approach0",              "dEta_LeptonIdx2_LeptonIdx3_Approach0",              100, 0,   7); 
  hdEta_LeptonIdx1_LeptonIdx3_Approach0_               = book1D(dir, "dEta_LeptonIdx1_LeptonIdx3_Approach0",              "dEta_LeptonIdx1_LeptonIdx3_Approach0",              100, 0,   7);
  //
  hdr_LeptonIdx1_LeptonIdx2_Approach0_                 = book1D(dir, "dr_LeptonIdx1_LeptonIdx2_Approach0",                "dr_LeptonIdx1_LeptonIdx2_Approach0",                100, 0,   7); 
  hdr_LeptonIdx2_LeptonIdx3_Approach0_                 = book1D(dir, "dr_LeptonIdx2_LeptonIdx3_Approach0",                "dr_LeptonIdx2_LeptonIdx3_Approach0",                100, 0,   7); 
  hdr_LeptonIdx1_LeptonIdx3_Approach0_                 = book1D(dir, "dr_LeptonIdx1_LeptonIdx3_Approach0",                "dr_LeptonIdx1_LeptonIdx3_Approach0",                100, 0,   7);
  //
  
  hdr_LeptonIdx3_Jet1_Approach0_                       = book1D(dir, "dr_LeptonIdx3_Jet1_Approach0",                      "dr_LeptonIdx3_Jet1_Approach0",                      100, 0,   7);
  //
  
  hdr_LeptonIdx3_JetNear_Approach0_                    = book1D(dir, "dr_LeptonIdx3_JetNear_Approach0",                   "dr_LeptonIdx3_JetNear_Approach0",                   100, 0,   7);
  //
  hdr_LeptonIdx3_2j_Approach0_                         = book1D(dir, "dr_LeptonIdx3_2j_Approach0",                        "dr_LeptonIdx3_2j_Approach0",                        100, 0,   7);
  hdr_LeptonIdx3_2j_inclusive1j_Approach0_             = book1D(dir, "dr_LeptonIdx3_2j_inclusive1j_Approach0",            "dr_LeptonIdx3_2j_inclusive1j_Approach0",            100, 0,   7);
  //
  hdr_LeptonIdx3_AK4jNear_Approach0_                   = book1D(dir, "dr_LeptonIdx3_AK4jNear_Approach0",                  "dr_LeptonIdx3_AK4jNear_Approach0",                  100, 0,   7);
  hdr_LeptonIdx3_2AK4jNear_Approach0_                  = book1D(dir, "dr_LeptonIdx3_2AK4jNear_Approach0",                 "dr_LeptonIdx3_2AK4jNear_Approach0",                 100, 0,   7);
  hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach0_      = book1D(dir, "dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach0",     "dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach0",     100, 0,   7);
  hm_LeptonIdx3_2AK4jNear_Approach0_                   = book1D(dir, "m_LeptonIdx3_2AK4jNear_Approach0",                  "m_LeptonIdx3_2AK4jNear_Approach0",                  200, 0, 800);
  hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach0_       = book1D(dir, "m_LeptonIdx3_2AK4jNear_inclusive1j_Approach0",      "m_LeptonIdx3_2AK4jNear_inclusive1j_Approach0",      200, 0, 800);
  hdr_2AK4J_NearestToLeptonIdx3_Approach0_             = book1D(dir, "dr_2AK4J_NearestToLeptonIdx3_Approach0",            "dr_2AK4J_NearestToLeptonIdx3_Approach0",            100, 0,   7);
  //
  hdr_LeptonIdx3_AK8_Approach0_                        = book1D(dir, "dr_LeptonIdx3_AK8_Approach0",                        "dr_LeptonIdx3_AK8_Approach0",                      100, 0,   7);
  hm_LeptonIdx3_AK8_Approach0_                         = book1D(dir, "m_LeptonIdx3_AK8_Approach0",                         "m_LeptonIdx3_AK8_Approach0",                       200, 0, 800);
  //
  hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0_   = book1D(dir, "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0",   "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0", 100, 0, TMath::Pi());
  //
  hdPhi_LeptonIdx3_Met_Approach0_                      = book1D(dir, "dPhi_LeptonIdx3_Met_Approach0",                      "dPhi_LeptonIdx3_Met_Approach0",                    100, 0, TMath::Pi());
  //
  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  hmT_LeptonIdx1_Met_Approach2_                        = book1D(dir, "mT_LeptonIdx1_Met_Approach2",                       "mT_LeptonIdx1_Met_Approach2",                      100, 0, 500); 
  hmT_LeptonIdx2_Met_Approach2_                        = book1D(dir, "mT_LeptonIdx2_Met_Approach2",                       "mT_LeptonIdx2_Met_Approach2",                      100, 0, 500); 
  
  //
  
  hm_LeptonIdx2_LeptonIdx3_Approach2_                  = book1D(dir, "m_LeptonIdx2_LeptonIdx3_Approach2",                 "m_LeptonIdx2_LeptonIdx3_Approach2",                 50, 0, 200); 
  hm_LeptonIdx1_LeptonIdx3_Approach2_                  = book1D(dir, "m_LeptonIdx1_LeptonIdx3_Approach2",                 "m_LeptonIdx1_LeptonIdx3_Approach2",                 50, 0, 200);
  //
  hdPhi_LeptonIdx1_LeptonIdx2_Approach2_               = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx2_Approach2",              "dPhi_LeptonIdx1_LeptonIdx2_Approach2",              100, 0,   TMath::Pi()); 
  hdPhi_LeptonIdx2_LeptonIdx3_Approach2_               = book1D(dir, "dPhi_LeptonIdx2_LeptonIdx3_Approach2",              "dPhi_LeptonIdx2_LeptonIdx3_Approach2",              100, 0,   TMath::Pi()); 
  hdPhi_LeptonIdx1_LeptonIdx3_Approach2_               = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx3_Approach2",              "dPhi_LeptonIdx1_LeptonIdx3_Approach2",              100, 0,   TMath::Pi());
  //
  hdEta_LeptonIdx1_LeptonIdx2_Approach2_               = book1D(dir, "dEta_LeptonIdx1_LeptonIdx2_Approach2",              "dEta_LeptonIdx1_LeptonIdx2_Approach2",              100, 0,   7); 
  hdEta_LeptonIdx2_LeptonIdx3_Approach2_               = book1D(dir, "dEta_LeptonIdx2_LeptonIdx3_Approach2",              "dEta_LeptonIdx2_LeptonIdx3_Approach2",              100, 0,   7); 
  hdEta_LeptonIdx1_LeptonIdx3_Approach2_               = book1D(dir, "dEta_LeptonIdx1_LeptonIdx3_Approach2",              "dEta_LeptonIdx1_LeptonIdx3_Approach2",              100, 0,   7);
  //
  hdr_LeptonIdx1_LeptonIdx2_Approach2_                 = book1D(dir, "dr_LeptonIdx1_LeptonIdx2_Approach2",                "dr_LeptonIdx1_LeptonIdx2_Approach2",                100, 0,   7); 
  hdr_LeptonIdx2_LeptonIdx3_Approach2_                 = book1D(dir, "dr_LeptonIdx2_LeptonIdx3_Approach2",                "dr_LeptonIdx2_LeptonIdx3_Approach2",                100, 0,   7); 
  hdr_LeptonIdx1_LeptonIdx3_Approach2_                 = book1D(dir, "dr_LeptonIdx1_LeptonIdx3_Approach2",                "dr_LeptonIdx1_LeptonIdx3_Approach2",                100, 0,   7);
  //
  hm_LeptonIdx3_Jet1_Approach2_                        = book1D(dir, "m_LeptonIdx3_Jet1_Approach2",                       "m_LeptonIdx3_Jet1_Approach2",                       100, 0, 500); 
  hdr_LeptonIdx3_Jet1_Approach2_                       = book1D(dir, "dr_LeptonIdx3_Jet1_Approach2",                      "dr_LeptonIdx3_Jet1_Approach2",                      100, 0,   7);
  //
  hm_LeptonIdx3_JetNear_Approach2_                     = book1D(dir, "m_LeptonIdx3_JetNear_Approach2",                    "m_LeptonIdx3_JetNear_Approach2",                    100, 0, 500); 
  hdr_LeptonIdx3_JetNear_Approach2_                    = book1D(dir, "dr_LeptonIdx3_JetNear_Approach2",                   "dr_LeptonIdx3_JetNear_Approach2",                   100, 0,   7);
  //
  hdr_LeptonIdx3_2j_Approach2_                         = book1D(dir, "dr_LeptonIdx3_2j_Approach2",                        "dr_LeptonIdx3_2j_Approach2",                        100, 0,   7);
  
  //
  
  hdr_LeptonIdx3_2AK4jNear_Approach2_                  = book1D(dir, "dr_LeptonIdx3_2AK4jNear_Approach2",                 "dr_LeptonIdx3_2AK4jNear_Approach2",                 100, 0,   7);
  hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach2_      = book1D(dir, "dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach2",     "dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach2",     100, 0,   7);
  hm_LeptonIdx3_2AK4jNear_Approach2_                   = book1D(dir, "m_LeptonIdx3_2AK4jNear_Approach2",                  "m_LeptonIdx3_2AK4jNear_Approach2",                  200, 0, 800);
  hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach2_       = book1D(dir, "m_LeptonIdx3_2AK4jNear_inclusive1j_Approach2",      "m_LeptonIdx3_2AK4jNear_inclusive1j_Approach2",      200, 0, 800);
  hdr_2AK4J_NearestToLeptonIdx3_Approach2_             = book1D(dir, "dr_2AK4J_NearestToLeptonIdx3_Approach2",            "dr_2AK4J_NearestToLeptonIdx3_Approach2",            100, 0,   7);
  //
  hdr_LeptonIdx3_AK8_Approach2_                        = book1D(dir, "dr_LeptonIdx3_AK8_Approach2",                        "dr_LeptonIdx3_AK8_Approach2",                      100, 0,   7);
  hm_LeptonIdx3_AK8_Approach2_                         = book1D(dir, "m_LeptonIdx3_AK8_Approach2",                         "m_LeptonIdx3_AK8_Approach2",                       200, 0, 800);
  //
  
  //
  hdPhi_LeptonIdx3_Met_Approach2_                      = book1D(dir, "dPhi_LeptonIdx3_Met_Approach2",                      "dPhi_LeptonIdx3_Met_Approach2",                    100, 0, TMath::Pi());
  //
  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  hmT_LeptonIdx1_Met_Approach3_                        = book1D(dir, "mT_LeptonIdx1_Met_Approach3",                       "mT_LeptonIdx1_Met_Approach3",                      100, 0, 500); 
  hmT_LeptonIdx2_Met_Approach3_                        = book1D(dir, "mT_LeptonIdx2_Met_Approach3",                       "mT_LeptonIdx2_Met_Approach3",                      100, 0, 500); 
  hmT_LeptonIdx3_Met_Approach3_                        = book1D(dir, "mT_LeptonIdx3_Met_Approach3",                       "mT_LeptonIdx3_Met_Approach3",                      100, 0, 500);
  //
  hm_LeptonIdx1_LeptonIdx2_Approach3_                  = book1D(dir, "m_LeptonIdx1_LeptonIdx2_Approach3",                 "m_LeptonIdx1_LeptonIdx2_Approach3",                 50, 0, 200); 
  hm_LeptonIdx2_LeptonIdx3_Approach3_                  = book1D(dir, "m_LeptonIdx2_LeptonIdx3_Approach3",                 "m_LeptonIdx2_LeptonIdx3_Approach3",                 50, 0, 200); 
  hm_LeptonIdx1_LeptonIdx3_Approach3_                  = book1D(dir, "m_LeptonIdx1_LeptonIdx3_Approach3",                 "m_LeptonIdx1_LeptonIdx3_Approach3",                 50, 0, 200);
  //
  hdPhi_LeptonIdx1_LeptonIdx2_Approach3_               = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx2_Approach3",              "dPhi_LeptonIdx1_LeptonIdx2_Approach3",              100, 0,   TMath::Pi()); 
  hdPhi_LeptonIdx2_LeptonIdx3_Approach3_               = book1D(dir, "dPhi_LeptonIdx2_LeptonIdx3_Approach3",              "dPhi_LeptonIdx2_LeptonIdx3_Approach3",              100, 0,   TMath::Pi()); 
  hdPhi_LeptonIdx1_LeptonIdx3_Approach3_               = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx3_Approach3",              "dPhi_LeptonIdx1_LeptonIdx3_Approach3",              100, 0,   TMath::Pi());
  //
  hdEta_LeptonIdx1_LeptonIdx2_Approach3_               = book1D(dir, "dEta_LeptonIdx1_LeptonIdx2_Approach3",              "dEta_LeptonIdx1_LeptonIdx2_Approach3",              100, 0,   7); 
  hdEta_LeptonIdx2_LeptonIdx3_Approach3_               = book1D(dir, "dEta_LeptonIdx2_LeptonIdx3_Approach3",              "dEta_LeptonIdx2_LeptonIdx3_Approach3",              100, 0,   7); 
  hdEta_LeptonIdx1_LeptonIdx3_Approach3_               = book1D(dir, "dEta_LeptonIdx1_LeptonIdx3_Approach3",              "dEta_LeptonIdx1_LeptonIdx3_Approach3",              100, 0,   7);
  //
  hdr_LeptonIdx1_LeptonIdx2_Approach3_                 = book1D(dir, "dr_LeptonIdx1_LeptonIdx2_Approach3",                "dr_LeptonIdx1_LeptonIdx2_Approach3",                100, 0,   7); 
  hdr_LeptonIdx2_LeptonIdx3_Approach3_                 = book1D(dir, "dr_LeptonIdx2_LeptonIdx3_Approach3",                "dr_LeptonIdx2_LeptonIdx3_Approach3",                100, 0,   7); 
  hdr_LeptonIdx1_LeptonIdx3_Approach3_                 = book1D(dir, "dr_LeptonIdx1_LeptonIdx3_Approach3",                "dr_LeptonIdx1_LeptonIdx3_Approach3",                100, 0,   7);
  //
  hm_LeptonIdx3_Jet1_Approach3_                        = book1D(dir, "m_LeptonIdx3_Jet1_Approach3",                       "m_LeptonIdx3_Jet1_Approach3",                       100, 0, 500); 
  hdr_LeptonIdx3_Jet1_Approach3_                       = book1D(dir, "dr_LeptonIdx3_Jet1_Approach3",                      "dr_LeptonIdx3_Jet1_Approach3",                      100, 0,   7);
  //
  hm_LeptonIdx3_JetNear_Approach3_                     = book1D(dir, "m_LeptonIdx3_JetNear_Approach3",                    "m_LeptonIdx3_JetNear_Approach3",                    100, 0, 500); 
  hdr_LeptonIdx3_JetNear_Approach3_                    = book1D(dir, "dr_LeptonIdx3_JetNear_Approach3",                   "dr_LeptonIdx3_JetNear_Approach3",                   100, 0,   7);
  //
  hdr_LeptonIdx3_2j_Approach3_                         = book1D(dir, "dr_LeptonIdx3_2j_Approach3",                        "dr_LeptonIdx3_2j_Approach3",                        100, 0,   7);
  hdr_LeptonIdx3_2j_inclusive1j_Approach3_             = book1D(dir, "dr_LeptonIdx3_2j_inclusive1j_Approach3",            "dr_LeptonIdx3_2j_inclusive1j_Approach3",            100, 0,   7);
  //
  hdr_LeptonIdx3_AK4jNear_Approach3_                   = book1D(dir, "dr_LeptonIdx3_AK4jNear_Approach3",                  "dr_LeptonIdx3_AK4jNear_Approach3",                  100, 0,   7);
  hdr_LeptonIdx3_2AK4jNear_Approach3_                  = book1D(dir, "dr_LeptonIdx3_2AK4jNear_Approach3",                 "dr_LeptonIdx3_2AK4jNear_Approach3",                 100, 0,   7);
  hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach3_      = book1D(dir, "dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach3",     "dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach3",     100, 0,   7);
  hm_LeptonIdx3_2AK4jNear_Approach3_                   = book1D(dir, "m_LeptonIdx3_2AK4jNear_Approach3",                  "m_LeptonIdx3_2AK4jNear_Approach3",                  200, 0, 800);
  hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach3_       = book1D(dir, "m_LeptonIdx3_2AK4jNear_inclusive1j_Approach3",      "m_LeptonIdx3_2AK4jNear_inclusive1j_Approach3",      200, 0, 800);
  hdr_2AK4J_NearestToLeptonIdx3_Approach3_             = book1D(dir, "dr_2AK4J_NearestToLeptonIdx3_Approach3",            "dr_2AK4J_NearestToLeptonIdx3_Approach3",            100, 0,   7);
  //
  hdr_LeptonIdx3_AK8_Approach3_                        = book1D(dir, "dr_LeptonIdx3_AK8_Approach3",                        "dr_LeptonIdx3_AK8_Approach3",                      100, 0,   7);
  hm_LeptonIdx3_AK8_Approach3_                         = book1D(dir, "m_LeptonIdx3_AK8_Approach3",                         "m_LeptonIdx3_AK8_Approach3",                       200, 0, 800);
  //
  hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3_   = book1D(dir, "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3",   "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3", 100, 0, TMath::Pi());
  //
  hdPhi_LeptonIdx3_Met_Approach3_                      = book1D(dir, "dPhi_LeptonIdx3_Met_Approach3",                      "dPhi_LeptonIdx3_Met_Approach3",                    100, 0, TMath::Pi());
  //
  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  //
  //
  hdPhi_2lSFOS_one2lSFOSEvt_                           = book1D(dir, "dPhi_2lSFOS_one2lSFOSEvt",                          "dPhi_2lSFOS_one2lSFOSEvt",              100, 0,   TMath::Pi());
  hdR_2lSFOS_one2lSFOSEvt_                             = book1D(dir, "dR_2lSFOS_one2lSFOSEvt",                            "dR_2lSFOS_one2lSFOSEvt",                100, 0,  7);
  hm_2lSFOS_one2lSFOSEvt_                              = book1D(dir, "m_2lSFOS_one2lSFOSEvt",                             "m_2lSFOS_one2lSFOSEvt",                 50, 0, 200);
  hmT_LeptonNonSFOS_Met_one2lSFOSEvt_                  = book1D(dir, "mT_LeptonNonSFOS_Met_one2lSFOSEvt",                 "mT_LeptonNonSFOS_Met_one2lSFOSEvt",    100, 0, 500);
  hdPhi_LeptonNonSFOS_Met_one2lSFOSEvt_                = book1D(dir, "dPhi_LeptonNonSFOS_Met_one2lSFOSEvt",               "dPhi_LeptonNonSFOS_Met_one2lSFOSEvt",  100, 0, TMath::Pi());
  //
  //
  heventCategory_                                      = book1D(dir, "eventCategory",              "eventCategory",               3, 0.5, 3.5); 
  }



  
}

void
EvtHistManager_conversions::fillHistograms(
  int numElectrons,
  int numMuons,
  int nJetAK4,
  int nBJetLoose,
  int nJetAK8_wSelectorAK8_Wjj,
  //
  int sumLeptonCharge_3l,
  int numSameFlavor_OS_Full,
  int numSameFlavor_OS_3l,
  //
  double lep1_pt,
  double lep1_conePt,
  double lep1_eta,
  double mindr_lep1_jet,
  double mT_MEtLep1,
  //
  double lep2_pt,
  double lep2_conePt,
  double lep2_eta,
  double mindr_lep2_jet,
  double mT_MEtLep2,
  //
  double lep3_pt,
  double lep3_conePt,
  double lep3_eta,
  double mindr_lep3_jet,
  double mT_MEtLep3,
  //
  double jet1_pt,
  double jet1_eta,
  double jet2_pt,
  double jet2_eta,
  double jet1plus2_pt,
  double jet1plus2_eta,
  double jet1_m,
  double jet2_m,
  //
  double met,
  double mht,
  double met_LD,
  double HT,
  double STMET,
  //
  double mSFOS2l_closestToZ,
  double m3l,
  double WTojjMass,
  double dihiggsVisMass_sel,
  double dihiggsVisMass_sel_inclusive1j,
  double dihiggsMass,
  double dihiggsMass_inclusive1j,
  //
  double mTMetLepton1_chargeEqualSumCharge3l,
  double mTMetLepton2_chargeEqualSumCharge3l,
  //
  double dr_l12,
  double dr_l23,
  double dr_l13,
  double dr_lss,
  double dr_los_min,
  double dr_los_max,
  //		   //
  double avg_dr_jet,
  double dr_Wjj,
  //
  double dPhi_3l_2j,
  double dPhi_3l_2j_inclusive1j,
  double dEta_3l_2j,
  double dEta_3l_2j_inclusive1j,
  double dR_3l_2j,
  double dR_3l_2j_inclusive1j,
  //
  double dEta_3l_avg2j,
  double dEta_3l_avg2j_inclusive1j,
  //
  double bTag_jet1,
  double bTag_jet2,
  double bTag_sum_jet1And2,
  double bTag_max_jet1or2,
  double bTag_max_AK4,
  double bTag_sum_AK4,
  //
  double pt_lastAK4,
  //
  double m_AK8,
  //
  //
  double mT_LeptonIdx1_Met_Approach0,
  double mT_LeptonIdx2_Met_Approach0,
  double mT_LeptonIdx3_Met_Approach0,
  //
  double m_LeptonIdx1_LeptonIdx2_Approach0,
  double m_LeptonIdx2_LeptonIdx3_Approach0,
  double m_LeptonIdx1_LeptonIdx3_Approach0,
  //
  double dPhi_LeptonIdx1_LeptonIdx2_Approach0,
  double dPhi_LeptonIdx2_LeptonIdx3_Approach0,
  double dPhi_LeptonIdx1_LeptonIdx3_Approach0,
  //
  double dEta_LeptonIdx1_LeptonIdx2_Approach0,
  double dEta_LeptonIdx2_LeptonIdx3_Approach0,
  double dEta_LeptonIdx1_LeptonIdx3_Approach0,
  //
  double dr_LeptonIdx1_LeptonIdx2_Approach0,
  double dr_LeptonIdx2_LeptonIdx3_Approach0,
  double dr_LeptonIdx1_LeptonIdx3_Approach0,
  //
  double m_LeptonIdx3_Jet1_Approach0,
  double dr_LeptonIdx3_Jet1_Approach0,
  //
  double m_LeptonIdx3_JetNear_Approach0,
  double dr_LeptonIdx3_JetNear_Approach0,
  //
  double dr_LeptonIdx3_2j_Approach0,
  double dr_LeptonIdx3_2j_inclusive1j_Approach0,
  //
  double dr_LeptonIdx3_AK4jNear_Approach0,
  double dr_LeptonIdx3_2AK4jNear_Approach0,
  double dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach0,
  double m_LeptonIdx3_2AK4jNear_Approach0,
  double m_LeptonIdx3_2AK4jNear_inclusive1j_Approach0,
  double dr_2AK4J_NearestToLeptonIdx3_Approach0,
  //
  double dr_LeptonIdx3_AK8_Approach0,
  double m_LeptonIdx3_AK8_Approach0,
  //
  double dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0,
  //
  double dPhi_LeptonIdx3_Met_Approach0,
  //
  //
  double mT_LeptonIdx1_Met_Approach2,
  double mT_LeptonIdx2_Met_Approach2,
  double mT_LeptonIdx3_Met_Approach2,
  //
  double m_LeptonIdx1_LeptonIdx2_Approach2,
  double m_LeptonIdx2_LeptonIdx3_Approach2,
  double m_LeptonIdx1_LeptonIdx3_Approach2,
  //
  double dPhi_LeptonIdx1_LeptonIdx2_Approach2,
  double dPhi_LeptonIdx2_LeptonIdx3_Approach2,
  double dPhi_LeptonIdx1_LeptonIdx3_Approach2,
  //
  double dEta_LeptonIdx1_LeptonIdx2_Approach2,
  double dEta_LeptonIdx2_LeptonIdx3_Approach2,
  double dEta_LeptonIdx1_LeptonIdx3_Approach2,
  //
  double dr_LeptonIdx1_LeptonIdx2_Approach2,
  double dr_LeptonIdx2_LeptonIdx3_Approach2,
  double dr_LeptonIdx1_LeptonIdx3_Approach2,
  //
  double m_LeptonIdx3_Jet1_Approach2,
  double dr_LeptonIdx3_Jet1_Approach2,
  //
  double m_LeptonIdx3_JetNear_Approach2,
  double dr_LeptonIdx3_JetNear_Approach2,
  //
  double dr_LeptonIdx3_2j_Approach2,
  double dr_LeptonIdx3_2j_inclusive1j_Approach2,
  //
  double dr_LeptonIdx3_AK4jNear_Approach2,
  double dr_LeptonIdx3_2AK4jNear_Approach2,
  double dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach2,
  double m_LeptonIdx3_2AK4jNear_Approach2,
  double m_LeptonIdx3_2AK4jNear_inclusive1j_Approach2,
  double dr_2AK4J_NearestToLeptonIdx3_Approach2,
  //
  double dr_LeptonIdx3_AK8_Approach2,
  double m_LeptonIdx3_AK8_Approach2,
  //
  double dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2,
  //
  double dPhi_LeptonIdx3_Met_Approach2,  
  //
  //
  double mT_LeptonIdx1_Met_Approach3,
  double mT_LeptonIdx2_Met_Approach3,
  double mT_LeptonIdx3_Met_Approach3,
  //
  double m_LeptonIdx1_LeptonIdx2_Approach3,
  double m_LeptonIdx2_LeptonIdx3_Approach3,
  double m_LeptonIdx1_LeptonIdx3_Approach3,
  //
  double dPhi_LeptonIdx1_LeptonIdx2_Approach3,
  double dPhi_LeptonIdx2_LeptonIdx3_Approach3,
  double dPhi_LeptonIdx1_LeptonIdx3_Approach3,
  //
  double dEta_LeptonIdx1_LeptonIdx2_Approach3,
  double dEta_LeptonIdx2_LeptonIdx3_Approach3,
  double dEta_LeptonIdx1_LeptonIdx3_Approach3,
  //
  double dr_LeptonIdx1_LeptonIdx2_Approach3,
  double dr_LeptonIdx2_LeptonIdx3_Approach3,
  double dr_LeptonIdx1_LeptonIdx3_Approach3,
  //
  double m_LeptonIdx3_Jet1_Approach3,
  double dr_LeptonIdx3_Jet1_Approach3,
  //
  double m_LeptonIdx3_JetNear_Approach3,
  double dr_LeptonIdx3_JetNear_Approach3,
  //
  double dr_LeptonIdx3_2j_Approach3,
  double dr_LeptonIdx3_2j_inclusive1j_Approach3,
  //
  double dr_LeptonIdx3_AK4jNear_Approach3,
  double dr_LeptonIdx3_2AK4jNear_Approach3,
  double dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach3,
  double m_LeptonIdx3_2AK4jNear_Approach3,
  double m_LeptonIdx3_2AK4jNear_inclusive1j_Approach3,
  double dr_2AK4J_NearestToLeptonIdx3_Approach3,
  //
  double dr_LeptonIdx3_AK8_Approach3,
  double m_LeptonIdx3_AK8_Approach3,
  //
  double dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3,
  //
  double dPhi_LeptonIdx3_Met_Approach3,
  //
  //
  double dPhi_2lSFOS_one2lSFOSEvt,
  double dR_2lSFOS_one2lSFOSEvt,
  double m_2lSFOS_one2lSFOSEvt,
  double mT_LeptonNonSFOS_Met_one2lSFOSEvt,
  double dPhi_LeptonNonSFOS_Met_one2lSFOSEvt,    
  //
  //
  int eventCategory,
  //
  //
  //
  // WZctrl
  double mT_WZctrl_leptonW_MET,
  // WZctrl 2lss
  double jetMass_sel_WZctrl_2lss,
  double leptonPairMass_sel_WZctrl_2lss,
  double mindr_lep1_jet_WZctrl_2lss,
  double mT_lep1_WZctrl_2lss,
  double mindr_lep2_jet_WZctrl_2lss,
  double mT_lep2_WZctrl_2lss,
  double dR_ll_WZctrl_2lss,
  double max_lep_eta_WZctrl_2lss,    
  //
  double nLostHits_selElectron,
  double passesConversionVeto_selElectron,
  double ntightLeptonsFull,
  //
  //
  //  
  //
  double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(hEventCounter_,                                      0.,                                                evtWeight, evtWeightErr);

  if (m3l > 0.)
    fillWithOverFlow(hm3l_,                                               m3l,                                               evtWeight, evtWeightErr);
  if (dihiggsVisMass_sel > 0.)
    fillWithOverFlow(hdihiggsVisMass_sel_,                                dihiggsVisMass_sel,                                evtWeight, evtWeightErr);
  if (mSFOS2l_closestToZ > 0.)
    fillWithOverFlow(hmSFOS2l_closestToZ_,                                mSFOS2l_closestToZ,                                evtWeight, evtWeightErr);
  if (dr_LeptonIdx3_AK4jNear_Approach2 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_AK4jNear_Approach2_,                  dr_LeptonIdx3_AK4jNear_Approach2,                  evtWeight, evtWeightErr);
  if (dr_LeptonIdx3_2j_inclusive1j_Approach2 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_2j_inclusive1j_Approach2_,            dr_LeptonIdx3_2j_inclusive1j_Approach2,            evtWeight, evtWeightErr);
  fillWithOverFlow(hdr_los_min_,                                        dr_los_min,                                        evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_los_max_,                                        dr_los_max,                                        evtWeight, evtWeightErr); 
  fillWithOverFlow(hnumSameFlavor_OS_3l_,                               numSameFlavor_OS_3l,                               evtWeight, evtWeightErr);
  fillWithOverFlow(hmet_LD_,                                            met_LD,                                            evtWeight, evtWeightErr); 

  fillWithOverFlow(hnumElectrons_,                                      numElectrons,                                      evtWeight, evtWeightErr);
  fillWithOverFlow(hnumMuons_,                                          numMuons,                                          evtWeight, evtWeightErr);
  fillWithOverFlow(hnJetAK4_,                                           nJetAK4,                                           evtWeight, evtWeightErr); 
  fillWithOverFlow(hnJetAK8_wSelectorAK8_Wjj_,                          nJetAK8_wSelectorAK8_Wjj,                          evtWeight, evtWeightErr);


  if (dihiggsVisMass_sel_inclusive1j > 0.)
    fillWithOverFlow(hdihiggsVisMass_sel_inclusive1j_,                    dihiggsVisMass_sel_inclusive1j,                    evtWeight, evtWeightErr);

  fillWithOverFlow(hmindr_lep1_jet_,                                    mindr_lep1_jet,                                    evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_MEtLep1_,                                        mT_MEtLep1,                                        evtWeight, evtWeightErr);
  
  fillWithOverFlow(hmet_,                                               met,                                               evtWeight, evtWeightErr); 
  fillWithOverFlow(hmht_,                                               mht,                                               evtWeight, evtWeightErr); 

  fillWithOverFlow(hdr_lss_,                                            dr_lss,                                            evtWeight, evtWeightErr); 

  fillWithOverFlow(hm_LeptonIdx1_LeptonIdx2_Approach0_,                 m_LeptonIdx1_LeptonIdx2_Approach0,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx1_LeptonIdx3_Approach0_,                 m_LeptonIdx1_LeptonIdx3_Approach0,                 evtWeight, evtWeightErr);
  fillWithOverFlow(hdPhi_LeptonIdx1_LeptonIdx3_Approach0_,              dPhi_LeptonIdx1_LeptonIdx3_Approach0,              evtWeight, evtWeightErr);
  fillWithOverFlow(hm_LeptonIdx3_Jet1_Approach0_,                       m_LeptonIdx3_Jet1_Approach0,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx3_JetNear_Approach0_,                    m_LeptonIdx3_JetNear_Approach0,                    evtWeight, evtWeightErr); 

  
  fillWithOverFlow(hmT_LeptonIdx3_Met_Approach2_,                       mT_LeptonIdx3_Met_Approach2,                       evtWeight, evtWeightErr);
  fillWithOverFlow(hm_LeptonIdx1_LeptonIdx2_Approach2_,                 m_LeptonIdx1_LeptonIdx2_Approach2,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2_,  dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2,  evtWeight, evtWeightErr);





  

  if (isControlRegion_)
  {
    fillWithOverFlow(hmT_WZctrl_leptonW_MET_,                           mT_WZctrl_leptonW_MET,                             evtWeight, evtWeightErr);

    if (jetMass_sel_WZctrl_2lss > 0)
      fillWithOverFlow(hjetMass_sel_WZctrl_2lss_,                       jetMass_sel_WZctrl_2lss,                           evtWeight, evtWeightErr);
    if (leptonPairMass_sel_WZctrl_2lss > 0)
      fillWithOverFlow(hleptonPairMass_sel_WZctrl_2lss_,                leptonPairMass_sel_WZctrl_2lss,                    evtWeight, evtWeightErr);
    if (mindr_lep1_jet_WZctrl_2lss > 0)
      fillWithOverFlow(hmindr_lep1_jet_WZctrl_2lss_,                    mindr_lep1_jet_WZctrl_2lss,                        evtWeight, evtWeightErr);
    if (mT_lep1_WZctrl_2lss > 0)
      fillWithOverFlow(hmT_lep1_WZctrl_2lss_,                           mT_lep1_WZctrl_2lss,                               evtWeight, evtWeightErr);
    if (mindr_lep2_jet_WZctrl_2lss > 0)
      fillWithOverFlow(hmindr_lep2_jet_WZctrl_2lss_,                    mindr_lep2_jet_WZctrl_2lss,                        evtWeight, evtWeightErr);
    if (mT_lep2_WZctrl_2lss > 0)
      fillWithOverFlow(hmT_lep2_WZctrl_2lss_,                           mT_lep2_WZctrl_2lss,                               evtWeight, evtWeightErr);
    if (dR_ll_WZctrl_2lss > 0)
      fillWithOverFlow(hdR_ll_WZctrl_2lss_,                             dR_ll_WZctrl_2lss,                                 evtWeight, evtWeightErr);
    if (max_lep_eta_WZctrl_2lss > 0)
      fillWithOverFlow(hmax_lep_eta_WZctrl_2lss_,                       max_lep_eta_WZctrl_2lss,                           evtWeight, evtWeightErr);

    fillWithOverFlow(hnLostHits_selElectron_,                           nLostHits_selElectron,                             evtWeight, evtWeightErr);
    fillWithOverFlow(hpassesConversionVeto_selElectron_,                passesConversionVeto_selElectron,                  evtWeight, evtWeightErr);
    fillWithOverFlow(hntightLeptonsFull_,                               ntightLeptonsFull,                             evtWeight, evtWeightErr);
  }
  

  if (analysisRunLevel >= 1)
  {
  fillWithOverFlow(hnBJetLoose_,                                        nBJetLoose,                                        evtWeight, evtWeightErr); 
  //
  fillWithOverFlow(hsumLeptonCharge_3l_,                                sumLeptonCharge_3l,                                evtWeight, evtWeightErr); 
  fillWithOverFlow(hnumSameFlavor_OS_Full_,                             numSameFlavor_OS_Full,                             evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hlep1_pt_,                                           lep1_pt,                                           evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep1_conePt_,                                       lep1_conePt,                                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep1_eta_,                                          lep1_eta,                                          evtWeight, evtWeightErr); 
  //
  fillWithOverFlow(hlep2_pt_,                                           lep2_pt,                                           evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep2_conePt_,                                       lep2_conePt,                                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep2_eta_,                                          lep2_eta,                                          evtWeight, evtWeightErr); 
  fillWithOverFlow(hmindr_lep2_jet_,                                    mindr_lep2_jet,                                    evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_MEtLep2_,                                        mT_MEtLep2,                                        evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hlep3_pt_,                                           lep3_pt,                                           evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep3_conePt_,                                       lep3_conePt,                                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep3_eta_,                                          lep3_eta,                                          evtWeight, evtWeightErr); 
  fillWithOverFlow(hmindr_lep3_jet_,                                    mindr_lep3_jet,                                    evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_MEtLep3_,                                        mT_MEtLep3,                                        evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hjet1_pt_,                                           jet1_pt,                                           evtWeight, evtWeightErr);
  fillWithOverFlow(hjet1_eta_,                                          jet1_eta,                                          evtWeight, evtWeightErr);
  if (jet2_pt > 0.) 
    fillWithOverFlow(hjet2_pt_,                                           jet2_pt,                                           evtWeight, evtWeightErr);
  if (jet2_eta > -4.) 
    fillWithOverFlow(hjet2_eta_,                                          jet2_eta,                                          evtWeight, evtWeightErr);
  if (jet1plus2_pt > 0.)
    fillWithOverFlow(hjet1plus2_pt_,                                      jet1plus2_pt,                                      evtWeight, evtWeightErr);
  if (jet1plus2_eta > -4.)
    fillWithOverFlow(hjet1plus2_eta_,                                     jet1plus2_eta,                                     evtWeight, evtWeightErr); 
  fillWithOverFlow(hjet1_m_,                                            jet1_m,                                            evtWeight, evtWeightErr);
  if (jet2_m > 0.) 
    fillWithOverFlow(hjet2_m_,                                            jet2_m,                                            evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hHT_,                                                HT,                                                evtWeight, evtWeightErr); 
  fillWithOverFlow(hSTMET_,                                             STMET,                                             evtWeight, evtWeightErr);
  //
  if (WTojjMass > 0.)
    fillWithOverFlow(hWTojjMass_,                                         WTojjMass,                                         evtWeight, evtWeightErr);
  if (dihiggsMass > 0.)
    fillWithOverFlow(hdihiggsMass_,                                       dihiggsMass,                                       evtWeight, evtWeightErr);
  if (dihiggsMass_inclusive1j > 0.)
    fillWithOverFlow(hdihiggsMass_inclusive1j_,                           dihiggsMass_inclusive1j,                           evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hmTMetLepton1_chargeEqualSumCharge3l_,               mTMetLepton1_chargeEqualSumCharge3l,               evtWeight, evtWeightErr); 
  fillWithOverFlow(hmTMetLepton2_chargeEqualSumCharge3l_,               mTMetLepton2_chargeEqualSumCharge3l,               evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdr_l12_,                                            dr_l12,                                            evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_l23_,                                            dr_l23,                                            evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_l13_,                                            dr_l13,                                            evtWeight, evtWeightErr); 
  //
  if (avg_dr_jet > 0.)
    fillWithOverFlow(havg_dr_jet_,                                        avg_dr_jet,                                        evtWeight, evtWeightErr);
  if (dr_Wjj > 0.)
    fillWithOverFlow(hdr_Wjj_,                                            dr_Wjj,                                            evtWeight, evtWeightErr);
  //
  if (dPhi_3l_2j > 0.)
    fillWithOverFlow(hdPhi_3l_2j_,                                        dPhi_3l_2j,                                        evtWeight, evtWeightErr);
  if (dPhi_3l_2j_inclusive1j > 0.)
    fillWithOverFlow(hdPhi_3l_2j_inclusive1j_,                            dPhi_3l_2j_inclusive1j,                            evtWeight, evtWeightErr);
  if (dEta_3l_2j > 0.)
    fillWithOverFlow(hdEta_3l_2j_,                                        dEta_3l_2j,                                        evtWeight, evtWeightErr);
  if (dEta_3l_2j_inclusive1j > 0.)
    fillWithOverFlow(hdEta_3l_2j_inclusive1j_,                            dEta_3l_2j_inclusive1j,                            evtWeight, evtWeightErr);
  if (dR_3l_2j > 0.)
    fillWithOverFlow(hdR_3l_2j_,                                          dR_3l_2j,                                          evtWeight, evtWeightErr);
  if (dR_3l_2j_inclusive1j > 0.)
    fillWithOverFlow(hdR_3l_2j_inclusive1j_,                              dR_3l_2j_inclusive1j,                              evtWeight, evtWeightErr);
  //
  if (dEta_3l_avg2j > 0.)
    fillWithOverFlow(hdEta_3l_avg2j_,                                     dEta_3l_avg2j,                                     evtWeight, evtWeightErr);
  if (dEta_3l_avg2j_inclusive1j > 0.)
    fillWithOverFlow(hdEta_3l_avg2j_inclusive1j_,                         dEta_3l_avg2j_inclusive1j,                         evtWeight, evtWeightErr);
  //
  if (bTag_jet1 > 0.)
    fillWithOverFlow(hbTag_jet1_,                                         bTag_jet1,                                         evtWeight, evtWeightErr);
  if (bTag_jet2 > 0.)
    fillWithOverFlow(hbTag_jet2_,                                         bTag_jet2,                                         evtWeight, evtWeightErr);
  if (bTag_sum_jet1And2 > 0.)
    fillWithOverFlow(hbTag_sum_jet1And2_,                                 bTag_sum_jet1And2,                                 evtWeight, evtWeightErr);
  if (bTag_max_jet1or2 > 0.)
    fillWithOverFlow(hbTag_max_jet1or2_,                                  bTag_max_jet1or2,                                  evtWeight, evtWeightErr);
  if (bTag_max_AK4 > 0.)
    fillWithOverFlow(hbTag_max_AK4_,                                      bTag_max_AK4,                                      evtWeight, evtWeightErr);
  if (bTag_sum_AK4 > 0.)
    fillWithOverFlow(hbTag_sum_AK4_,                                      bTag_sum_AK4,                                      evtWeight, evtWeightErr);
  //
  if (pt_lastAK4 > 0.)
    fillWithOverFlow(hpt_lastAK4_,                                        pt_lastAK4,                                        evtWeight, evtWeightErr);
  //
  if (m_AK8 > 0.)
    fillWithOverFlow(hm_AK8_,                                             m_AK8,                                             evtWeight, evtWeightErr);
  //
  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  fillWithOverFlow(hmT_LeptonIdx1_Met_Approach0_,                       mT_LeptonIdx1_Met_Approach0,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx2_Met_Approach0_,                       mT_LeptonIdx2_Met_Approach0,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx3_Met_Approach0_,                       mT_LeptonIdx3_Met_Approach0,                       evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hm_LeptonIdx2_LeptonIdx3_Approach0_,                 m_LeptonIdx2_LeptonIdx3_Approach0,                 evtWeight, evtWeightErr); 
  //
  fillWithOverFlow(hdPhi_LeptonIdx1_LeptonIdx2_Approach0_,              dPhi_LeptonIdx1_LeptonIdx2_Approach0,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx2_LeptonIdx3_Approach0_,              dPhi_LeptonIdx2_LeptonIdx3_Approach0,              evtWeight, evtWeightErr); 
  //
  fillWithOverFlow(hdEta_LeptonIdx1_LeptonIdx2_Approach0_,              dEta_LeptonIdx1_LeptonIdx2_Approach0,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdEta_LeptonIdx2_LeptonIdx3_Approach0_,              dEta_LeptonIdx2_LeptonIdx3_Approach0,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdEta_LeptonIdx1_LeptonIdx3_Approach0_,              dEta_LeptonIdx1_LeptonIdx3_Approach0,              evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdr_LeptonIdx1_LeptonIdx2_Approach0_,                dr_LeptonIdx1_LeptonIdx2_Approach0,                evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx2_LeptonIdx3_Approach0_,                dr_LeptonIdx2_LeptonIdx3_Approach0,                evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx1_LeptonIdx3_Approach0_,                dr_LeptonIdx1_LeptonIdx3_Approach0,                evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdr_LeptonIdx3_Jet1_Approach0_,                      dr_LeptonIdx3_Jet1_Approach0,                      evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdr_LeptonIdx3_JetNear_Approach0_,                   dr_LeptonIdx3_JetNear_Approach0,                   evtWeight, evtWeightErr);
  //
  if (dr_LeptonIdx3_2j_Approach0 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_2j_Approach0_,                        dr_LeptonIdx3_2j_Approach0,                        evtWeight, evtWeightErr);
  if (dr_LeptonIdx3_2j_inclusive1j_Approach0 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_2j_inclusive1j_Approach0_,            dr_LeptonIdx3_2j_inclusive1j_Approach0,            evtWeight, evtWeightErr);
  //
  if (dr_LeptonIdx3_AK4jNear_Approach0 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_AK4jNear_Approach0_,                  dr_LeptonIdx3_AK4jNear_Approach0,                  evtWeight, evtWeightErr);
  if (dr_LeptonIdx3_2AK4jNear_Approach0 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_2AK4jNear_Approach0_,                 dr_LeptonIdx3_2AK4jNear_Approach0,                 evtWeight, evtWeightErr);
  if (dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach0 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach0_,     dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach0,     evtWeight, evtWeightErr);
  if (m_LeptonIdx3_2AK4jNear_Approach0 > 0.)
    fillWithOverFlow(hm_LeptonIdx3_2AK4jNear_Approach0_,                  m_LeptonIdx3_2AK4jNear_Approach0,                  evtWeight, evtWeightErr);
  if (m_LeptonIdx3_2AK4jNear_inclusive1j_Approach0 > 0.)
    fillWithOverFlow(hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach0_,      m_LeptonIdx3_2AK4jNear_inclusive1j_Approach0,      evtWeight, evtWeightErr);
  if (dr_2AK4J_NearestToLeptonIdx3_Approach0 > 0.)
    fillWithOverFlow(hdr_2AK4J_NearestToLeptonIdx3_Approach0_,            dr_2AK4J_NearestToLeptonIdx3_Approach0,            evtWeight, evtWeightErr);
  //
  if (dr_LeptonIdx3_AK8_Approach0 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_AK8_Approach0_,                       dr_LeptonIdx3_AK8_Approach0,                       evtWeight, evtWeightErr);
  if (m_LeptonIdx3_AK8_Approach0 > 0.)
    fillWithOverFlow(hm_LeptonIdx3_AK8_Approach0_,                        m_LeptonIdx3_AK8_Approach0,                        evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0_,  dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0,  evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdPhi_LeptonIdx3_Met_Approach0_,                     dPhi_LeptonIdx3_Met_Approach0,                     evtWeight, evtWeightErr);
  //
  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  fillWithOverFlow(hmT_LeptonIdx1_Met_Approach2_,                       mT_LeptonIdx1_Met_Approach2,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx2_Met_Approach2_,                       mT_LeptonIdx2_Met_Approach2,                       evtWeight, evtWeightErr); 
  //
  fillWithOverFlow(hm_LeptonIdx2_LeptonIdx3_Approach2_,                 m_LeptonIdx2_LeptonIdx3_Approach2,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx1_LeptonIdx3_Approach2_,                 m_LeptonIdx1_LeptonIdx3_Approach2,                 evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdPhi_LeptonIdx1_LeptonIdx2_Approach2_,              dPhi_LeptonIdx1_LeptonIdx2_Approach2,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx2_LeptonIdx3_Approach2_,              dPhi_LeptonIdx2_LeptonIdx3_Approach2,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx1_LeptonIdx3_Approach2_,              dPhi_LeptonIdx1_LeptonIdx3_Approach2,              evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdEta_LeptonIdx1_LeptonIdx2_Approach2_,              dEta_LeptonIdx1_LeptonIdx2_Approach2,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdEta_LeptonIdx2_LeptonIdx3_Approach2_,              dEta_LeptonIdx2_LeptonIdx3_Approach2,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdEta_LeptonIdx1_LeptonIdx3_Approach2_,              dEta_LeptonIdx1_LeptonIdx3_Approach2,              evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdr_LeptonIdx1_LeptonIdx2_Approach2_,                dr_LeptonIdx1_LeptonIdx2_Approach2,                evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx2_LeptonIdx3_Approach2_,                dr_LeptonIdx2_LeptonIdx3_Approach2,                evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx1_LeptonIdx3_Approach2_,                dr_LeptonIdx1_LeptonIdx3_Approach2,                evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hm_LeptonIdx3_Jet1_Approach2_,                       m_LeptonIdx3_Jet1_Approach2,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx3_Jet1_Approach2_,                      dr_LeptonIdx3_Jet1_Approach2,                      evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hm_LeptonIdx3_JetNear_Approach2_,                    m_LeptonIdx3_JetNear_Approach2,                    evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx3_JetNear_Approach2_,                   dr_LeptonIdx3_JetNear_Approach2,                   evtWeight, evtWeightErr);
  //
  if (dr_LeptonIdx3_2j_Approach2 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_2j_Approach2_,                        dr_LeptonIdx3_2j_Approach2,                        evtWeight, evtWeightErr);
  //
  if (dr_LeptonIdx3_2AK4jNear_Approach2 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_2AK4jNear_Approach2_,                 dr_LeptonIdx3_2AK4jNear_Approach2,                 evtWeight, evtWeightErr);
  if (dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach2 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach2_,     dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach2,     evtWeight, evtWeightErr);
  if (m_LeptonIdx3_2AK4jNear_Approach2 > 0.)
    fillWithOverFlow(hm_LeptonIdx3_2AK4jNear_Approach2_,                  m_LeptonIdx3_2AK4jNear_Approach2,                  evtWeight, evtWeightErr);
  if (m_LeptonIdx3_2AK4jNear_inclusive1j_Approach2 > 0.)
    fillWithOverFlow(hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach2_,      m_LeptonIdx3_2AK4jNear_inclusive1j_Approach2,      evtWeight, evtWeightErr);
  if (dr_2AK4J_NearestToLeptonIdx3_Approach2 > 0.)
    fillWithOverFlow(hdr_2AK4J_NearestToLeptonIdx3_Approach2_,            dr_2AK4J_NearestToLeptonIdx3_Approach2,            evtWeight, evtWeightErr);
  //
  if (dr_LeptonIdx3_AK8_Approach2 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_AK8_Approach2_,                       dr_LeptonIdx3_AK8_Approach2,                       evtWeight, evtWeightErr);
  if (m_LeptonIdx3_AK8_Approach2 > 0.)
    fillWithOverFlow(hm_LeptonIdx3_AK8_Approach2_,                        m_LeptonIdx3_AK8_Approach2,                        evtWeight, evtWeightErr);
  //
  //
  fillWithOverFlow(hdPhi_LeptonIdx3_Met_Approach2_,                     dPhi_LeptonIdx3_Met_Approach2,                     evtWeight, evtWeightErr);
  //
  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  fillWithOverFlow(hmT_LeptonIdx1_Met_Approach3_,                       mT_LeptonIdx1_Met_Approach3,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx2_Met_Approach3_,                       mT_LeptonIdx2_Met_Approach3,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx3_Met_Approach3_,                       mT_LeptonIdx3_Met_Approach3,                       evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hm_LeptonIdx1_LeptonIdx2_Approach3_,                 m_LeptonIdx1_LeptonIdx2_Approach3,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx2_LeptonIdx3_Approach3_,                 m_LeptonIdx2_LeptonIdx3_Approach3,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx1_LeptonIdx3_Approach3_,                 m_LeptonIdx1_LeptonIdx3_Approach3,                 evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdPhi_LeptonIdx1_LeptonIdx2_Approach3_,              dPhi_LeptonIdx1_LeptonIdx2_Approach3,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx2_LeptonIdx3_Approach3_,              dPhi_LeptonIdx2_LeptonIdx3_Approach3,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx1_LeptonIdx3_Approach3_,              dPhi_LeptonIdx1_LeptonIdx3_Approach3,              evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdEta_LeptonIdx1_LeptonIdx2_Approach3_,              dEta_LeptonIdx1_LeptonIdx2_Approach3,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdEta_LeptonIdx2_LeptonIdx3_Approach3_,              dEta_LeptonIdx2_LeptonIdx3_Approach3,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdEta_LeptonIdx1_LeptonIdx3_Approach3_,              dEta_LeptonIdx1_LeptonIdx3_Approach3,              evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdr_LeptonIdx1_LeptonIdx2_Approach3_,                dr_LeptonIdx1_LeptonIdx2_Approach3,                evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx2_LeptonIdx3_Approach3_,                dr_LeptonIdx2_LeptonIdx3_Approach3,                evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx1_LeptonIdx3_Approach3_,                dr_LeptonIdx1_LeptonIdx3_Approach3,                evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hm_LeptonIdx3_Jet1_Approach3_,                       m_LeptonIdx3_Jet1_Approach3,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx3_Jet1_Approach3_,                      dr_LeptonIdx3_Jet1_Approach3,                      evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hm_LeptonIdx3_JetNear_Approach3_,                    m_LeptonIdx3_JetNear_Approach3,                    evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx3_JetNear_Approach3_,                   dr_LeptonIdx3_JetNear_Approach3,                   evtWeight, evtWeightErr);
  //
  if (dr_LeptonIdx3_2j_Approach3 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_2j_Approach3_,                        dr_LeptonIdx3_2j_Approach3,                        evtWeight, evtWeightErr);
  if (dr_LeptonIdx3_2j_inclusive1j_Approach3 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_2j_inclusive1j_Approach3_,            dr_LeptonIdx3_2j_inclusive1j_Approach3,            evtWeight, evtWeightErr);
  //
  if (dr_LeptonIdx3_AK4jNear_Approach3 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_AK4jNear_Approach3_,                  dr_LeptonIdx3_AK4jNear_Approach3,                  evtWeight, evtWeightErr);
  if (dr_LeptonIdx3_2AK4jNear_Approach3 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_2AK4jNear_Approach3_,                 dr_LeptonIdx3_2AK4jNear_Approach3,                 evtWeight, evtWeightErr);
  if (dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach3 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach3_,     dr_LeptonIdx3_2AK4jNear_inclusive1j_Approach3,     evtWeight, evtWeightErr);
  if (m_LeptonIdx3_2AK4jNear_Approach3 > 0.)
    fillWithOverFlow(hm_LeptonIdx3_2AK4jNear_Approach3_,                  m_LeptonIdx3_2AK4jNear_Approach3,                  evtWeight, evtWeightErr);
  if (m_LeptonIdx3_2AK4jNear_inclusive1j_Approach3 > 0.)
    fillWithOverFlow(hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach3_,      m_LeptonIdx3_2AK4jNear_inclusive1j_Approach3,      evtWeight, evtWeightErr);
  if (dr_2AK4J_NearestToLeptonIdx3_Approach3 > 0.)
    fillWithOverFlow(hdr_2AK4J_NearestToLeptonIdx3_Approach3_,            dr_2AK4J_NearestToLeptonIdx3_Approach3,            evtWeight, evtWeightErr);
  //
  if (dr_LeptonIdx3_AK8_Approach3 > 0.)
    fillWithOverFlow(hdr_LeptonIdx3_AK8_Approach3_,                       dr_LeptonIdx3_AK8_Approach3,                       evtWeight, evtWeightErr);
  if (m_LeptonIdx3_AK8_Approach3 > 0.)
    fillWithOverFlow(hm_LeptonIdx3_AK8_Approach3_,                        m_LeptonIdx3_AK8_Approach3,                        evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3_,  dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3,  evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdPhi_LeptonIdx3_Met_Approach3_,                     dPhi_LeptonIdx3_Met_Approach3,                     evtWeight, evtWeightErr);
  //
  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  if (dPhi_2lSFOS_one2lSFOSEvt > 0.) fillWithOverFlow(hdPhi_2lSFOS_one2lSFOSEvt_,  dPhi_2lSFOS_one2lSFOSEvt,  evtWeight, evtWeightErr);
  if (dR_2lSFOS_one2lSFOSEvt > 0.) fillWithOverFlow(hdR_2lSFOS_one2lSFOSEvt_,  dR_2lSFOS_one2lSFOSEvt,  evtWeight, evtWeightErr);
  if (m_2lSFOS_one2lSFOSEvt > 0.) fillWithOverFlow(hm_2lSFOS_one2lSFOSEvt_,  m_2lSFOS_one2lSFOSEvt,  evtWeight, evtWeightErr);
  if (mT_LeptonNonSFOS_Met_one2lSFOSEvt > 0.) fillWithOverFlow(hmT_LeptonNonSFOS_Met_one2lSFOSEvt_,  mT_LeptonNonSFOS_Met_one2lSFOSEvt,  evtWeight, evtWeightErr);
  if (dPhi_LeptonNonSFOS_Met_one2lSFOSEvt > 0.) fillWithOverFlow(hdPhi_LeptonNonSFOS_Met_one2lSFOSEvt_,  dPhi_LeptonNonSFOS_Met_one2lSFOSEvt,  evtWeight, evtWeightErr);
  //
  //
  fillWithOverFlow(heventCategory_,                                     eventCategory,                                     evtWeight, evtWeightErr);
  //
  }




  
}
 
