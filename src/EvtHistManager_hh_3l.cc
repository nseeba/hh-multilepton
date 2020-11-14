#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_3l.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), getLogWeight()
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()

EvtHistManager_hh_3l::EvtHistManager_hh_3l(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
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
    "dPhi_3l_avg2j",
    "dPhi_3l_avg2j_inclusive1j",
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
    "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0",
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
    "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2",
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
    "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3",
    //
    //
    "eventCategory",
    //
  };
  const std::vector<std::string> sysOpts_all = {
    //"mvaOutput_xgb_hh_3l_SUMBk_HH",
    "EventCounter"
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
EvtHistManager_hh_3l::getHistogram_EventCounter() const
{
  return hEventCounter_;
}

void
EvtHistManager_hh_3l::bookHistograms(TFileDirectory & dir)
{
  hnumElectrons_                                       = book1D(dir, "numElectrons",                                      "numElectrons",                                      5, -0.5,  +4.5); 
  hnumMuons_                                           = book1D(dir, "numMuons",                                          "numMuons",                                          5, -0.5,  +4.5);
  hnJetAK4_                                            = book1D(dir, "nJetAK4",                                           "nJetAK4",                                          20, -0.5, +19.5); 
  hnBJetLoose_                                         = book1D(dir, "nBJetLoose",                                        "nBJetLoose",                                       20, -0.5, +19.5 ); 
  hnJetAK8_wSelectorAK8_Wjj_                           = book1D(dir, "nJetAK8_wSelectorAK8_Wjj",                          "nJetAK8_wSelectorAK8_Wjj",                         20, -0.5, +19.5);
  //  
  hsumLeptonCharge_3l_                                 = book1D(dir, "sumLeptonCharge_3l",                                "sumLeptonCharge_3l",                                7, -3.5,  +3.5);
  hnumSameFlavor_OS_Full_                              = book1D(dir, "numSameFlavor_OS_FullPresel",                       "numSameFlavor_OS_FullPresel",                       9, -0.5,  +8.5); 
  hnumSameFlavor_OS_3l_                                = book1D(dir, "numSameFlavor_OS_3l",                               "numSameFlavor_OS_3l",                               9, -0.5,  +8.5);
  //
  hlep1_pt_                                            = book1D(dir, "lep1_pt",                                           "lep1_pt",                                         100, 0,400); 
  hlep1_conePt_                                        = book1D(dir, "lep1_conePt",                                       "lep1_conePt",                                     100, 0,400); 
  hlep1_eta_                                           = book1D(dir, "lep1_eta",                                          "lep1_eta",                                        100,-5,5); 
  hmindr_lep1_jet_                                     = book1D(dir, "mindr_lep1_jet",                                    "mindr_lep1_jet",                                  100, 0, 10); 
  hmT_MEtLep1_                                         = book1D(dir, "mT_MEtLep1",                                        "mT_MEtLep1",                                      100, 0,500);
  //
  hlep2_pt_                                            = book1D(dir, "lep2_pt",                                           "lep2_pt",                                         100, 0,400); 
  hlep2_conePt_                                        = book1D(dir, "lep2_conePt",                                       "lep2_conePt",                                     100, 0,400); 
  hlep2_eta_                                           = book1D(dir, "lep2_eta",                                          "lep2_eta",                                        100,-5,5); 
  hmindr_lep2_jet_                                     = book1D(dir, "mindr_lep2_jet",                                    "mindr_lep2_jet",                                  100, 0, 10); 
  hmT_MEtLep2_                                         = book1D(dir, "mT_MEtLep2",                                        "mT_MEtLep2",                                      100, 0,500);
  //
  hlep3_pt_                                            = book1D(dir, "lep3_pt",                                           "lep3_pt",                                         100, 0,400); 
  hlep3_conePt_                                        = book1D(dir, "lep3_conePt",                                       "lep3_conePt",                                     100, 0,400); 
  hlep3_eta_                                           = book1D(dir, "lep3_eta",                                          "lep3_eta",                                        100,-5,5); 
  hmindr_lep3_jet_                                     = book1D(dir, "mindr_lep3_jet",                                    "mindr_lep3_jet",                                  100, 0, 10); 
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
  hmet_                                                = book1D(dir, "met",                                               "met",                                              200, 0,500); 
  hmht_                                                = book1D(dir, "mht",                                               "mht",                                              200, 0,500); 
  hmet_LD_                                             = book1D(dir, "met_LD",                                            "met_LD",                                           200, 0,500); 
  hHT_                                                 = book1D(dir, "HT",                                                "HT",                                               200, 0,1000); 
  hSTMET_                                              = book1D(dir, "STMET",                                             "STMET",                                            200, 0,1000);
  //
  hmSFOS2l_closestToZ_                                 = book1D(dir, "mSFOS2l_closestToZ",                                "mSFOS2l_closestToZ",                                40,-1,  320);
  hm3l_                                                = book1D(dir, "m3l",                                               "m3l",                                              200, 0,  400); 
  hWTojjMass_                                          = book1D(dir, "WTojjMass",                                         "WTojjMass",                                        200,-1,  500); 
  hdihiggsVisMass_sel_                                 = book1D(dir, "dihiggsVisMass_sel",                                "dihiggsVisMass_sel",                               200,-1, 1500);
  hdihiggsVisMass_sel_inclusive1j_                     = book1D(dir, "dihiggsVisMass_sel_inclusive1j",                    "dihiggsVisMass_sel_inclusive1j",                   200,-1, 1500); 
  hdihiggsMass_                                        = book1D(dir, "dihiggsMass",                                       "dihiggsMass",                                      200,-1, 1500);
  hdihiggsMass_inclusive1j_                            = book1D(dir, "dihiggsMass_inclusive1j",                           "dihiggsMass_inclusive1j",                          200,-1, 1500);
  //
  hmTMetLepton1_chargeEqualSumCharge3l_                = book1D(dir, "mTMetLepton1_chargeEqualSumCharge3l",               "mTMetLepton1_chargeEqualSumCharge3l",              200, 0,  400); 
  hmTMetLepton2_chargeEqualSumCharge3l_                = book1D(dir, "mTMetLepton2_chargeEqualSumCharge3l",               "mTMetLepton2_chargeEqualSumCharge3l",              200, 0,  400);
  //
  hdr_l12_                                             = book1D(dir, "dr_l12",                                            "dr_l12",                                           100, 0, 10); 
  hdr_l23_                                             = book1D(dir, "dr_l23",                                            "dr_l23",                                           100, 0, 10); 
  hdr_l13_                                             = book1D(dir, "dr_l13",                                            "dr_l13",                                           100, 0, 10); 
  hdr_lss_                                             = book1D(dir, "dr_lss",                                            "dr_lss",                                           100, 0, 10); 
  hdr_los_min_                                         = book1D(dir, "dr_los_min",                                        "dr_los_min",                                       100, 0, 10); 
  hdr_los_max_                                         = book1D(dir, "dr_los_max",                                        "dr_los_max",                                       100, 0, 10);
  //
  havg_dr_jet_                                         = book1D(dir, "avg_dr_jet",                                        "avg_dr_jet",                                       100, 0, 10);
  hdr_Wjj_                                             = book1D(dir, "dr_Wjj",                                            "dr_Wjj",                                           100, 0, 10);
  //
  hdPhi_3l_2j_                                         = book1D(dir, "dPhi_3l_2j",                                        "dPhi_3l_2j",                                       100, -1, 7.3);
  hdPhi_3l_2j_inclusive1j_                             = book1D(dir, "dPhi_3l_2j_inclusive1j",                            "dPhi_3l_2j_inclusive1j",                           100, -1, 7.3);
  hdEta_3l_2j_                                         = book1D(dir, "dEta_3l_2j",                                        "dEta_3l_2j",                                       100, -1, 10);
  hdEta_3l_2j_inclusive1j_                             = book1D(dir, "dEta_3l_2j_inclusive1j",                            "dEta_3l_2j_inclusive1j",                           100, -1, 10);
  hdR_3l_2j_                                           = book1D(dir, "dR_3l_2j",                                          "dR_3l_2j",                                         100, -1, 10);
  hdR_3l_2j_inclusive1j_                               = book1D(dir, "dR_3l_2j_inclusive1j",                              "dR_3l_2j_inclusive1j",                             100, -1, 10);
  //
  hdPhi_3l_avg2j_                                      = book1D(dir, "dPhi_3l_avg2j",                                     "dPhi_3l_avg2j",                                    100, -1, 7.3);
  hdPhi_3l_avg2j_inclusive1j_                          = book1D(dir, "dPhi_3l_avg2j_inclusive1j",                         "dPhi_3l_avg2j_inclusive1j",                        100, -1, 7.3);
  hdEta_3l_avg2j_                                      = book1D(dir, "dEta_3l_avg2j",                                     "dEta_3l_avg2j",                                    100, -1, 10);
  hdEta_3l_avg2j_inclusive1j_                          = book1D(dir, "dEta_3l_avg2j_inclusive1j",                         "dEta_3l_avg2j_inclusive1j",                        100, -1, 10);
  //
  hbTag_jet1_                                          = book1D(dir, "bTag_jet1",                                         "bTag_jet1",                                         40, -2,  2);
  hbTag_jet2_                                          = book1D(dir, "bTag_jet2",                                         "bTag_jet2",                                         40, -2,  2);
  hbTag_sum_jet1And2_                                  = book1D(dir, "bTag_sum_jet1And2",                                 "bTag_sum_jet1And2",                                 40, -2,  2);
  hbTag_max_jet1or2_                                   = book1D(dir, "bTag_max_jet1or2",                                  "bTag_max_jet1or2",                                  40, -2,  2);
  hbTag_max_AK4_                                       = book1D(dir, "bTag_max_AK4",                                      "bTag_max_AK4",                                      40, -2,  2);
  hbTag_sum_AK4_                                       = book1D(dir, "bTag_sum_AK4",                                      "bTag_sum_AK4",                                      60, -2,  4);
  //
  hpt_lastAK4_                                         = book1D(dir, "pt_lastAK4",                                        "pt_lastAK4",                                       120, -1, 600); 
  //
  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  hmT_LeptonIdx1_Met_Approach0_                        = book1D(dir, "mT_LeptonIdx1_Met_Approach0",                       "mT_LeptonIdx1_Met_Approach0",                      100, 0, 500); 
  hmT_LeptonIdx2_Met_Approach0_                        = book1D(dir, "mT_LeptonIdx2_Met_Approach0",                       "mT_LeptonIdx2_Met_Approach0",                      100, 0, 500); 
  hmT_LeptonIdx3_Met_Approach0_                        = book1D(dir, "mT_LeptonIdx3_Met_Approach0",                       "mT_LeptonIdx3_Met_Approach0",                      100, 0, 500);
  //
  hm_LeptonIdx1_LeptonIdx2_Approach0_                  = book1D(dir, "m_LeptonIdx1_LeptonIdx2_Approach0",                 "m_LeptonIdx1_LeptonIdx2_Approach0",                 50, 0, 200); 
  hm_LeptonIdx2_LeptonIdx3_Approach0_                  = book1D(dir, "m_LeptonIdx2_LeptonIdx3_Approach0",                 "m_LeptonIdx2_LeptonIdx3_Approach0",                 50, 0, 200); 
  hm_LeptonIdx1_LeptonIdx3_Approach0_                  = book1D(dir, "m_LeptonIdx1_LeptonIdx3_Approach0",                 "m_LeptonIdx1_LeptonIdx3_Approach0",                 50, 0, 200);
  //
  hdPhi_LeptonIdx1_LeptonIdx2_Approach0_               = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx2_Approach0",              "dPhi_LeptonIdx1_LeptonIdx2_Approach0",              100, 0,   7.3); 
  hdPhi_LeptonIdx2_LeptonIdx3_Approach0_               = book1D(dir, "dPhi_LeptonIdx2_LeptonIdx3_Approach0",              "dPhi_LeptonIdx2_LeptonIdx3_Approach0",              100, 0,   7.3); 
  hdPhi_LeptonIdx1_LeptonIdx3_Approach0_               = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx3_Approach0",              "dPhi_LeptonIdx1_LeptonIdx3_Approach0",              100, 0,   7.3);
  //
  hdEta_LeptonIdx1_LeptonIdx2_Approach0_               = book1D(dir, "dEta_LeptonIdx1_LeptonIdx2_Approach0",              "dEta_LeptonIdx1_LeptonIdx2_Approach0",              100, 0,  10); 
  hdEta_LeptonIdx2_LeptonIdx3_Approach0_               = book1D(dir, "dEta_LeptonIdx2_LeptonIdx3_Approach0",              "dEta_LeptonIdx2_LeptonIdx3_Approach0",              100, 0,  10); 
  hdEta_LeptonIdx1_LeptonIdx3_Approach0_               = book1D(dir, "dEta_LeptonIdx1_LeptonIdx3_Approach0",              "dEta_LeptonIdx1_LeptonIdx3_Approach0",              100, 0,  10);
  //
  hdr_LeptonIdx1_LeptonIdx2_Approach0_                 = book1D(dir, "dr_LeptonIdx1_LeptonIdx2_Approach0",                "dr_LeptonIdx1_LeptonIdx2_Approach0",                100, 0,  10); 
  hdr_LeptonIdx2_LeptonIdx3_Approach0_                 = book1D(dir, "dr_LeptonIdx2_LeptonIdx3_Approach0",                "dr_LeptonIdx2_LeptonIdx3_Approach0",                100, 0,  10); 
  hdr_LeptonIdx1_LeptonIdx3_Approach0_                 = book1D(dir, "dr_LeptonIdx1_LeptonIdx3_Approach0",                "dr_LeptonIdx1_LeptonIdx3_Approach0",                100, 0,  10);
  //
  hm_LeptonIdx3_Jet1_Approach0_                        = book1D(dir, "m_LeptonIdx3_Jet1_Approach0",                       "m_LeptonIdx3_Jet1_Approach0",                       100, 0, 500); 
  hdr_LeptonIdx3_Jet1_Approach0_                       = book1D(dir, "dr_LeptonIdx3_Jet1_Approach0",                      "dr_LeptonIdx3_Jet1_Approach0",                      100, 0,  10);
  //
  hm_LeptonIdx3_JetNear_Approach0_                     = book1D(dir, "m_LeptonIdx3_JetNear_Approach0",                    "m_LeptonIdx3_JetNear_Approach0",                    100, 0, 500); 
  hdr_LeptonIdx3_JetNear_Approach0_                    = book1D(dir, "dr_LeptonIdx3_JetNear_Approach0",                   "dr_LeptonIdx3_JetNear_Approach0",                   100, 0,  10);
  //
  hdr_LeptonIdx3_2j_Approach0_                         = book1D(dir, "dr_LeptonIdx3_2j_Approach0",                        "dr_LeptonIdx3_2j_Approach0",                        100, 0, 10);
  hdr_LeptonIdx3_2j_inclusive1j_Approach0_             = book1D(dir, "dr_LeptonIdx3_2j_inclusive1j_Approach0",            "dr_LeptonIdx3_2j_inclusive1j_Approach0",            100, 0, 10);
  //
  hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0_   = book1D(dir, "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0",  "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0",  100, -1, 7.3);
  //
  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  hmT_LeptonIdx1_Met_Approach2_                        = book1D(dir, "mT_LeptonIdx1_Met_Approach2",                       "mT_LeptonIdx1_Met_Approach2",                      100, 0, 500); 
  hmT_LeptonIdx2_Met_Approach2_                        = book1D(dir, "mT_LeptonIdx2_Met_Approach2",                       "mT_LeptonIdx2_Met_Approach2",                      100, 0, 500); 
  hmT_LeptonIdx3_Met_Approach2_                        = book1D(dir, "mT_LeptonIdx3_Met_Approach2",                       "mT_LeptonIdx3_Met_Approach2",                      100, 0, 500);
  //
  hm_LeptonIdx1_LeptonIdx2_Approach2_                  = book1D(dir, "m_LeptonIdx1_LeptonIdx2_Approach2",                 "m_LeptonIdx1_LeptonIdx2_Approach2",                 50, 0, 200); 
  hm_LeptonIdx2_LeptonIdx3_Approach2_                  = book1D(dir, "m_LeptonIdx2_LeptonIdx3_Approach2",                 "m_LeptonIdx2_LeptonIdx3_Approach2",                 50, 0, 200); 
  hm_LeptonIdx1_LeptonIdx3_Approach2_                  = book1D(dir, "m_LeptonIdx1_LeptonIdx3_Approach2",                 "m_LeptonIdx1_LeptonIdx3_Approach2",                 50, 0, 200);
  //
  hdPhi_LeptonIdx1_LeptonIdx2_Approach2_               = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx2_Approach2",              "dPhi_LeptonIdx1_LeptonIdx2_Approach2",              100, 0,   7.3); 
  hdPhi_LeptonIdx2_LeptonIdx3_Approach2_               = book1D(dir, "dPhi_LeptonIdx2_LeptonIdx3_Approach2",              "dPhi_LeptonIdx2_LeptonIdx3_Approach2",              100, 0,   7.3); 
  hdPhi_LeptonIdx1_LeptonIdx3_Approach2_               = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx3_Approach2",              "dPhi_LeptonIdx1_LeptonIdx3_Approach2",              100, 0,   7.3);
  //
  hdEta_LeptonIdx1_LeptonIdx2_Approach2_               = book1D(dir, "dEta_LeptonIdx1_LeptonIdx2_Approach2",              "dEta_LeptonIdx1_LeptonIdx2_Approach2",              100, 0,  10); 
  hdEta_LeptonIdx2_LeptonIdx3_Approach2_               = book1D(dir, "dEta_LeptonIdx2_LeptonIdx3_Approach2",              "dEta_LeptonIdx2_LeptonIdx3_Approach2",              100, 0,  10); 
  hdEta_LeptonIdx1_LeptonIdx3_Approach2_               = book1D(dir, "dEta_LeptonIdx1_LeptonIdx3_Approach2",              "dEta_LeptonIdx1_LeptonIdx3_Approach2",              100, 0,  10);
  //
  hdr_LeptonIdx1_LeptonIdx2_Approach2_                 = book1D(dir, "dr_LeptonIdx1_LeptonIdx2_Approach2",                "dr_LeptonIdx1_LeptonIdx2_Approach2",                100, 0,  10); 
  hdr_LeptonIdx2_LeptonIdx3_Approach2_                 = book1D(dir, "dr_LeptonIdx2_LeptonIdx3_Approach2",                "dr_LeptonIdx2_LeptonIdx3_Approach2",                100, 0,  10); 
  hdr_LeptonIdx1_LeptonIdx3_Approach2_                 = book1D(dir, "dr_LeptonIdx1_LeptonIdx3_Approach2",                "dr_LeptonIdx1_LeptonIdx3_Approach2",                100, 0,  10);
  //
  hm_LeptonIdx3_Jet1_Approach2_                        = book1D(dir, "m_LeptonIdx3_Jet1_Approach2",                       "m_LeptonIdx3_Jet1_Approach2",                       100, 0, 500); 
  hdr_LeptonIdx3_Jet1_Approach2_                       = book1D(dir, "dr_LeptonIdx3_Jet1_Approach2",                      "dr_LeptonIdx3_Jet1_Approach2",                      100, 0,  10);
  //
  hm_LeptonIdx3_JetNear_Approach2_                     = book1D(dir, "m_LeptonIdx3_JetNear_Approach2",                    "m_LeptonIdx3_JetNear_Approach2",                    100, 0, 500); 
  hdr_LeptonIdx3_JetNear_Approach2_                    = book1D(dir, "dr_LeptonIdx3_JetNear_Approach2",                   "dr_LeptonIdx3_JetNear_Approach2",                   100, 0,  10);
  //
  hdr_LeptonIdx3_2j_Approach2_                         = book1D(dir, "dr_LeptonIdx3_2j_Approach2",                        "dr_LeptonIdx3_2j_Approach2",                        100, 0, 10);
  hdr_LeptonIdx3_2j_inclusive1j_Approach2_             = book1D(dir, "dr_LeptonIdx3_2j_inclusive1j_Approach2",            "dr_LeptonIdx3_2j_inclusive1j_Approach2",            100, 0, 10);
  //
  hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2_   = book1D(dir, "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2",  "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2",  100, -1, 7.3);
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
  hdPhi_LeptonIdx1_LeptonIdx2_Approach3_               = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx2_Approach3",              "dPhi_LeptonIdx1_LeptonIdx2_Approach3",              100, 0,   7.3); 
  hdPhi_LeptonIdx2_LeptonIdx3_Approach3_               = book1D(dir, "dPhi_LeptonIdx2_LeptonIdx3_Approach3",              "dPhi_LeptonIdx2_LeptonIdx3_Approach3",              100, 0,   7.3); 
  hdPhi_LeptonIdx1_LeptonIdx3_Approach3_               = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx3_Approach3",              "dPhi_LeptonIdx1_LeptonIdx3_Approach3",              100, 0,   7.3);
  //
  hdEta_LeptonIdx1_LeptonIdx2_Approach3_               = book1D(dir, "dEta_LeptonIdx1_LeptonIdx2_Approach3",              "dEta_LeptonIdx1_LeptonIdx2_Approach3",              100, 0,  10); 
  hdEta_LeptonIdx2_LeptonIdx3_Approach3_               = book1D(dir, "dEta_LeptonIdx2_LeptonIdx3_Approach3",              "dEta_LeptonIdx2_LeptonIdx3_Approach3",              100, 0,  10); 
  hdEta_LeptonIdx1_LeptonIdx3_Approach3_               = book1D(dir, "dEta_LeptonIdx1_LeptonIdx3_Approach3",              "dEta_LeptonIdx1_LeptonIdx3_Approach3",              100, 0,  10);
  //
  hdr_LeptonIdx1_LeptonIdx2_Approach3_                 = book1D(dir, "dr_LeptonIdx1_LeptonIdx2_Approach3",                "dr_LeptonIdx1_LeptonIdx2_Approach3",                100, 0,  10); 
  hdr_LeptonIdx2_LeptonIdx3_Approach3_                 = book1D(dir, "dr_LeptonIdx2_LeptonIdx3_Approach3",                "dr_LeptonIdx2_LeptonIdx3_Approach3",                100, 0,  10); 
  hdr_LeptonIdx1_LeptonIdx3_Approach3_                 = book1D(dir, "dr_LeptonIdx1_LeptonIdx3_Approach3",                "dr_LeptonIdx1_LeptonIdx3_Approach3",                100, 0,  10);
  //
  hm_LeptonIdx3_Jet1_Approach3_                        = book1D(dir, "m_LeptonIdx3_Jet1_Approach3",                       "m_LeptonIdx3_Jet1_Approach3",                       100, 0, 500); 
  hdr_LeptonIdx3_Jet1_Approach3_                       = book1D(dir, "dr_LeptonIdx3_Jet1_Approach3",                      "dr_LeptonIdx3_Jet1_Approach3",                      100, 0,  10);
  //
  hm_LeptonIdx3_JetNear_Approach3_                     = book1D(dir, "m_LeptonIdx3_JetNear_Approach3",                    "m_LeptonIdx3_JetNear_Approach3",                    100, 0, 500); 
  hdr_LeptonIdx3_JetNear_Approach3_                    = book1D(dir, "dr_LeptonIdx3_JetNear_Approach3",                   "dr_LeptonIdx3_JetNear_Approach3",                   100, 0,  10);
  //
  hdr_LeptonIdx3_2j_Approach3_                         = book1D(dir, "dr_LeptonIdx3_2j_Approach3",                        "dr_LeptonIdx3_2j_Approach3",                        100, 0, 10);
  hdr_LeptonIdx3_2j_inclusive1j_Approach3_             = book1D(dir, "dr_LeptonIdx3_2j_inclusive1j_Approach3",            "dr_LeptonIdx3_2j_inclusive1j_Approach3",            100, 0, 10);
  //
  hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3_   = book1D(dir, "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3",  "dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3",  100, -1, 7.3);
  //
  heventCategory_                                      = book1D(dir, "eventCategory",              "eventCategory",               4, -0.5, 3.5); 
  //hmvaOutput_xgb_hh_3l_SUMBk_HH_    = book1D(dir, "mvaOutput_xgb_hh_3l_SUMBk_HH","mvaOutput_xgb_hh_3l_SUMBk_HH",120,  0., 1.);
  //
  hEventCounter_                                       = book1D(dir, "EventCounter", "EventCounter",                              1, -0.5, +0.5);    
}

void
EvtHistManager_hh_3l::fillHistograms(
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
  double dPhi_3l_avg2j,
  double dPhi_3l_avg2j_inclusive1j,
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
  double dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0,
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
  double dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2,
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
  double dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3,
  //
  //
  int eventCategory,
  //
  //double mvaOutput_xgb_hh_3l_SUMBk_HH,
  double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(hnumElectrons_,                                      numElectrons,                                      evtWeight, evtWeightErr); 
  fillWithOverFlow(hnumMuons_,                                          numMuons,                                          evtWeight, evtWeightErr);
  fillWithOverFlow(hnJetAK4_,                                           nJetAK4,                                           evtWeight, evtWeightErr); 
  fillWithOverFlow(hnBJetLoose_,                                        nBJetLoose,                                        evtWeight, evtWeightErr); 
  fillWithOverFlow(hnJetAK8_wSelectorAK8_Wjj_,                          nJetAK8_wSelectorAK8_Wjj,                          evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hsumLeptonCharge_3l_,                                sumLeptonCharge_3l,                                evtWeight, evtWeightErr); 
  fillWithOverFlow(hnumSameFlavor_OS_Full_,                             numSameFlavor_OS_Full,                             evtWeight, evtWeightErr);
  fillWithOverFlow(hnumSameFlavor_OS_3l_,                               numSameFlavor_OS_3l,                               evtWeight, evtWeightErr); 
  //
  fillWithOverFlow(hlep1_pt_,                                           lep1_pt,                                           evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep1_conePt_,                                       lep1_conePt,                                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep1_eta_,                                          lep1_eta,                                          evtWeight, evtWeightErr); 
  fillWithOverFlow(hmindr_lep1_jet_,                                    mindr_lep1_jet,                                    evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_MEtLep1_,                                        mT_MEtLep1,                                        evtWeight, evtWeightErr);
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
  fillWithOverFlow(hjet2_pt_,                                           jet2_pt,                                           evtWeight, evtWeightErr);
  fillWithOverFlow(hjet2_eta_,                                          jet2_eta,                                          evtWeight, evtWeightErr); 
  fillWithOverFlow(hjet1plus2_pt_,                                      jet1plus2_pt,                                      evtWeight, evtWeightErr);
  fillWithOverFlow(hjet1plus2_eta_,                                     jet1plus2_eta,                                     evtWeight, evtWeightErr); 
  fillWithOverFlow(hjet1_m_,                                            jet1_m,                                            evtWeight, evtWeightErr); 
  fillWithOverFlow(hjet2_m_,                                            jet2_m,                                            evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hmet_,                                               met,                                               evtWeight, evtWeightErr); 
  fillWithOverFlow(hmht_,                                               mht,                                               evtWeight, evtWeightErr); 
  fillWithOverFlow(hmet_LD_,                                            met_LD,                                            evtWeight, evtWeightErr); 
  fillWithOverFlow(hHT_,                                                HT,                                                evtWeight, evtWeightErr); 
  fillWithOverFlow(hSTMET_,                                             STMET,                                             evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hmSFOS2l_closestToZ_,                                mSFOS2l_closestToZ,                                evtWeight, evtWeightErr);
  fillWithOverFlow(hm3l_,                                               m3l,                                               evtWeight, evtWeightErr); 
  fillWithOverFlow(hWTojjMass_,                                         WTojjMass,                                         evtWeight, evtWeightErr);
  fillWithOverFlow(hdihiggsVisMass_sel_,                                dihiggsVisMass_sel,                                evtWeight, evtWeightErr);
  fillWithOverFlow(hdihiggsVisMass_sel_inclusive1j_,                    dihiggsVisMass_sel_inclusive1j,                    evtWeight, evtWeightErr);
  fillWithOverFlow(hdihiggsMass_,                                       dihiggsMass,                                       evtWeight, evtWeightErr);
  fillWithOverFlow(hdihiggsMass_inclusive1j_,                           dihiggsMass_inclusive1j,                           evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hmTMetLepton1_chargeEqualSumCharge3l_,               mTMetLepton1_chargeEqualSumCharge3l,               evtWeight, evtWeightErr); 
  fillWithOverFlow(hmTMetLepton2_chargeEqualSumCharge3l_,               mTMetLepton2_chargeEqualSumCharge3l,               evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdr_l12_,                                            dr_l12,                                            evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_l23_,                                            dr_l23,                                            evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_l13_,                                            dr_l13,                                            evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_lss_,                                            dr_lss,                                            evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_los_min_,                                        dr_los_min,                                        evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_los_max_,                                        dr_los_max,                                        evtWeight, evtWeightErr); 
  //
  fillWithOverFlow(havg_dr_jet_,                                        avg_dr_jet,                                        evtWeight, evtWeightErr);
  fillWithOverFlow(hdr_Wjj_,                                            dr_Wjj,                                            evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdPhi_3l_2j_,                                        dPhi_3l_2j,                                        evtWeight, evtWeightErr);
  fillWithOverFlow(hdPhi_3l_2j_inclusive1j_,                            dPhi_3l_2j_inclusive1j,                            evtWeight, evtWeightErr);
  fillWithOverFlow(hdEta_3l_2j_,                                        dEta_3l_2j,                                        evtWeight, evtWeightErr);
  fillWithOverFlow(hdEta_3l_2j_inclusive1j_,                            dEta_3l_2j_inclusive1j,                            evtWeight, evtWeightErr);
  fillWithOverFlow(hdR_3l_2j_,                                          dR_3l_2j,                                          evtWeight, evtWeightErr);
  fillWithOverFlow(hdR_3l_2j_inclusive1j_,                              dR_3l_2j_inclusive1j,                              evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdPhi_3l_avg2j_,                                     dPhi_3l_avg2j,                                     evtWeight, evtWeightErr);
  fillWithOverFlow(hdPhi_3l_avg2j_inclusive1j_,                         dPhi_3l_avg2j_inclusive1j,                         evtWeight, evtWeightErr);
  fillWithOverFlow(hdEta_3l_avg2j_,                                     dEta_3l_avg2j,                                     evtWeight, evtWeightErr);
  fillWithOverFlow(hdEta_3l_avg2j_inclusive1j_,                         dEta_3l_avg2j_inclusive1j,                         evtWeight, evtWeightErr);
   //
  fillWithOverFlow(hbTag_jet1_,                                         bTag_jet1,                                         evtWeight, evtWeightErr);
  fillWithOverFlow(hbTag_jet2_,                                         bTag_jet2,                                         evtWeight, evtWeightErr);
  fillWithOverFlow(hbTag_sum_jet1And2_,                                 bTag_sum_jet1And2,                                 evtWeight, evtWeightErr);
  fillWithOverFlow(hbTag_max_jet1or2_,                                  bTag_max_jet1or2,                                  evtWeight, evtWeightErr);
  fillWithOverFlow(hbTag_max_AK4_,                                      bTag_max_AK4,                                      evtWeight, evtWeightErr);
  fillWithOverFlow(hbTag_sum_AK4_,                                      bTag_sum_AK4,                                      evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hpt_lastAK4_,                                        pt_lastAK4,                                        evtWeight, evtWeightErr);
  //
  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  fillWithOverFlow(hmT_LeptonIdx1_Met_Approach0_,                       mT_LeptonIdx1_Met_Approach0,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx2_Met_Approach0_,                       mT_LeptonIdx2_Met_Approach0,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx3_Met_Approach0_,                       mT_LeptonIdx3_Met_Approach0,                       evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hm_LeptonIdx1_LeptonIdx2_Approach0_,                 m_LeptonIdx1_LeptonIdx2_Approach0,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx2_LeptonIdx3_Approach0_,                 m_LeptonIdx2_LeptonIdx3_Approach0,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx1_LeptonIdx3_Approach0_,                 m_LeptonIdx1_LeptonIdx3_Approach0,                 evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdPhi_LeptonIdx1_LeptonIdx2_Approach0_,              dPhi_LeptonIdx1_LeptonIdx2_Approach0,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx2_LeptonIdx3_Approach0_,              dPhi_LeptonIdx2_LeptonIdx3_Approach0,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx1_LeptonIdx3_Approach0_,              dPhi_LeptonIdx1_LeptonIdx3_Approach0,              evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdEta_LeptonIdx1_LeptonIdx2_Approach0_,              dEta_LeptonIdx1_LeptonIdx2_Approach0,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdEta_LeptonIdx2_LeptonIdx3_Approach0_,              dEta_LeptonIdx2_LeptonIdx3_Approach0,              evtWeight, evtWeightErr); 
  fillWithOverFlow(hdEta_LeptonIdx1_LeptonIdx3_Approach0_,              dEta_LeptonIdx1_LeptonIdx3_Approach0,              evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdr_LeptonIdx1_LeptonIdx2_Approach0_,                dr_LeptonIdx1_LeptonIdx2_Approach0,                evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx2_LeptonIdx3_Approach0_,                dr_LeptonIdx2_LeptonIdx3_Approach0,                evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx1_LeptonIdx3_Approach0_,                dr_LeptonIdx1_LeptonIdx3_Approach0,                evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hm_LeptonIdx3_Jet1_Approach0_,                       m_LeptonIdx3_Jet1_Approach0,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx3_Jet1_Approach0_,                      dr_LeptonIdx3_Jet1_Approach0,                      evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hm_LeptonIdx3_JetNear_Approach0_,                    m_LeptonIdx3_JetNear_Approach0,                    evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx3_JetNear_Approach0_,                   dr_LeptonIdx3_JetNear_Approach0,                   evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdr_LeptonIdx3_2j_Approach0_,                        dr_LeptonIdx3_2j_Approach0,                        evtWeight, evtWeightErr);
  fillWithOverFlow(hdr_LeptonIdx3_2j_inclusive1j_Approach0_,            dr_LeptonIdx3_2j_inclusive1j_Approach0,            evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0_,  dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0,  evtWeight, evtWeightErr);
  //
  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  fillWithOverFlow(hmT_LeptonIdx1_Met_Approach2_,                       mT_LeptonIdx1_Met_Approach2,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx2_Met_Approach2_,                       mT_LeptonIdx2_Met_Approach2,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx3_Met_Approach2_,                       mT_LeptonIdx3_Met_Approach2,                       evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hm_LeptonIdx1_LeptonIdx2_Approach2_,                 m_LeptonIdx1_LeptonIdx2_Approach2,                 evtWeight, evtWeightErr); 
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
  fillWithOverFlow(hdr_LeptonIdx3_2j_Approach2_,                        dr_LeptonIdx3_2j_Approach2,                        evtWeight, evtWeightErr);
  fillWithOverFlow(hdr_LeptonIdx3_2j_inclusive1j_Approach2_,            dr_LeptonIdx3_2j_inclusive1j_Approach2,            evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2_,  dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2,  evtWeight, evtWeightErr);
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
  fillWithOverFlow(hdr_LeptonIdx3_2j_Approach3_,                        dr_LeptonIdx3_2j_Approach3,                        evtWeight, evtWeightErr);
  fillWithOverFlow(hdr_LeptonIdx3_2j_inclusive1j_Approach3_,            dr_LeptonIdx3_2j_inclusive1j_Approach3,            evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3_,  dPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3,  evtWeight, evtWeightErr);
  //  
  // -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  fillWithOverFlow(heventCategory_,                                     eventCategory,                                     evtWeight, evtWeightErr);
  //
  //fillWithOverFlow(hmvaOutput_xgb_hh_3l_SUMBk_HH_,  mvaOutput_xgb_hh_3l_SUMBk_HH,  evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hEventCounter_,                                      0.,                                                evtWeight, evtWeightErr);
}
 
