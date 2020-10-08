#include "hhAnalysis/multilepton/interface/EvtHistManager_WZctrl_SFstudy.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), getLogWeight()
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()

EvtHistManager_WZctrl_SFstudy::EvtHistManager_WZctrl_SFstudy(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numElectrons"]                   = { "central" }; 
  central_or_shiftOptions_["numMuons"]                       = { "central" }; 
  central_or_shiftOptions_["numLeptons"]                     = { "central" }; 
  central_or_shiftOptions_["sumLeptonCharge_3l"]             = { "central" }; 
  central_or_shiftOptions_["sumLeptonCharge_FullSel"]        = { "central" }; 
  central_or_shiftOptions_["numSameFlavor_OS_3l"]            = { "central" }; 
  central_or_shiftOptions_["numSameFlavor_OS_FullPresel"]    = { "central" }; 
  central_or_shiftOptions_["nJetAK4"]                        = { "central" }; 
  central_or_shiftOptions_["nBJetLoose"]                     = { "central" }; 
  central_or_shiftOptions_["nBJetMedium"]                    = { "central" }; 
  central_or_shiftOptions_["nJetAK8"]                        = { "central" }; 
  central_or_shiftOptions_["nJetAK8_wSelectorAK8_Wjj"]       = { "central" };
  //
  central_or_shiftOptions_["lep1_pt"]                        = { "central" }; 
  central_or_shiftOptions_["lep1_conePt"]                    = { "central" }; 
  central_or_shiftOptions_["lep1_eta"]                       = { "central" }; 
  central_or_shiftOptions_["mindr_lep1_jet"]                 = { "central" }; 
  central_or_shiftOptions_["mT_MEtLep1"]                     = { "central" };
  //
  central_or_shiftOptions_["lep2_pt"]                        = { "central" }; 
  central_or_shiftOptions_["lep2_conePt"]                    = { "central" }; 
  central_or_shiftOptions_["lep2_eta"]                       = { "central" }; 
  central_or_shiftOptions_["mindr_lep2_jet"]                 = { "central" }; 
  central_or_shiftOptions_["mT_MEtLep2"]                     = { "central" };
  //
  central_or_shiftOptions_["lep3_pt"]                        = { "central" }; 
  central_or_shiftOptions_["lep3_conePt"]                    = { "central" }; 
  central_or_shiftOptions_["lep3_eta"]                       = { "central" }; 
  central_or_shiftOptions_["mindr_lep3_jet"]                 = { "central" }; 
  central_or_shiftOptions_["mT_MEtLep3"]                     = { "central" };
  //
  central_or_shiftOptions_["jet1_pt"]                        = { "central" }; 
  central_or_shiftOptions_["jet2_pt"]                        = { "central" }; 
  central_or_shiftOptions_["jet1plus2pt"]                    = { "central" }; 
  central_or_shiftOptions_["jet1_m"]                         = { "central" }; 
  central_or_shiftOptions_["jet2_m"]                         = { "central" };
  //
  central_or_shiftOptions_["avg_dr_jet"]                     = { "central" };
  central_or_shiftOptions_["dr_Wjj"]                         = { "central" };
  //
  central_or_shiftOptions_["dr_l12"]                         = { "central" }; 
  central_or_shiftOptions_["dr_l23"]                         = { "central" }; 
  central_or_shiftOptions_["dr_l13"]                         = { "central" }; 
  central_or_shiftOptions_["dr_lss"]                         = { "central" }; 
  central_or_shiftOptions_["dr_los_min"]                     = { "central" }; 
  central_or_shiftOptions_["dr_los_max"]                     = { "central" }; 
  central_or_shiftOptions_["dr_WjjLepIdx3"]                  = { "central" }; 
  central_or_shiftOptions_["dr_Wjet1LepIdx3"]                = { "central" }; 
  central_or_shiftOptions_["dr_Wjet2LepIdx3"]                = { "central" }; 
  central_or_shiftOptions_["dr_LepIdx3WjetNear"]             = { "central" }; 
  central_or_shiftOptions_["dr_LepIdx3WjetFar"]              = { "central" };
  //
  central_or_shiftOptions_["met"]                            = { "central" }; 
  central_or_shiftOptions_["mht"]                            = { "central" }; 
  central_or_shiftOptions_["met_LD"]                         = { "central" }; 
  central_or_shiftOptions_["HT"]                             = { "central" }; 
  central_or_shiftOptions_["STMET"]                          = { "central" };
  //
  central_or_shiftOptions_["mSFOS2l"]                        = { "central" }; 
  central_or_shiftOptions_["WTojjMass"]                      = { "*" }; 
  central_or_shiftOptions_["dihiggsVisMass_sel"]             = { "*" }; 
  central_or_shiftOptions_["dihiggsMass"]                    = { "*" }; 
  central_or_shiftOptions_["mTMetLepton1"]                   = { "central" }; 
  central_or_shiftOptions_["mTMetLepton2"]                   = { "central" };
  //
  central_or_shiftOptions_["lep1_isTight"]                   = { "central" }; 
  central_or_shiftOptions_["lep2_isTight"]                   = { "central" }; 
  central_or_shiftOptions_["lep3_isTight"]                   = { "central" }; 
  central_or_shiftOptions_["lep1_genLepPt"]                  = { "central" }; 
  central_or_shiftOptions_["lep2_genLepPt"]                  = { "central" }; 
  central_or_shiftOptions_["lep3_genLepPt"]                  = { "central" }; 
  central_or_shiftOptions_["lep1_frWeight"]                  = { "central" }; 
  central_or_shiftOptions_["lep2_frWeight"]                  = { "central" }; 
  central_or_shiftOptions_["lep3_frWeight"]                  = { "central" }; 
  central_or_shiftOptions_["lep1_fake_prob"]                 = { "central" }; 
  central_or_shiftOptions_["lep2_fake_prob"]                 = { "central" }; 
  central_or_shiftOptions_["lep3_fake_prob"]                 = { "central" };
  //
  central_or_shiftOptions_["mT_LeptonIdx1_Met_Approach0"]              = { "central" }; 
  central_or_shiftOptions_["mT_LeptonIdx2_Met_Approach0"]              = { "central" }; 
  central_or_shiftOptions_["mT_LeptonIdx3_Met_Approach0"]              = { "central" }; 
  central_or_shiftOptions_["m_LeptonIdx1_LeptonIdx2_Approach0"]        = { "central" }; 
  central_or_shiftOptions_["m_LeptonIdx2_LeptonIdx3_Approach0"]        = { "central" }; 
  central_or_shiftOptions_["m_LeptonIdx1_LeptonIdx3_Approach0"]        = { "central" }; 
  central_or_shiftOptions_["dPhi_LeptonIdx1_LeptonIdx2_Approach0"]     = { "central" }; 
  central_or_shiftOptions_["dPhi_LeptonIdx2_LeptonIdx3_Approach0"]     = { "central" }; 
  central_or_shiftOptions_["dPhi_LeptonIdx1_LeptonIdx3_Approach0"]     = { "central" }; 
  central_or_shiftOptions_["dr_LeptonIdx1_LeptonIdx2_Approach0"]       = { "central" }; 
  central_or_shiftOptions_["dr_LeptonIdx2_LeptonIdx3_Approach0"]       = { "central" }; 
  central_or_shiftOptions_["dr_LeptonIdx1_LeptonIdx3_Approach0"]       = { "central" }; 
  central_or_shiftOptions_["m_LeptonIdx3_Jet1_Approach0"]              = { "central" }; 
  central_or_shiftOptions_["dr_LeptonIdx3_Jet1_Approach0"]             = { "central" }; 
  central_or_shiftOptions_["m_LeptonIdx3_JetNear_Approach0"]           = { "central" }; 
  central_or_shiftOptions_["dr_LeptonIdx3_JetNear_Approach0"]          = { "central" }; 
  central_or_shiftOptions_["mT_LeptonIdx1_Met_Approach2"]              = { "central" }; 
  central_or_shiftOptions_["mT_LeptonIdx2_Met_Approach2"]              = { "central" }; 
  central_or_shiftOptions_["mT_LeptonIdx3_Met_Approach2"]              = { "central" }; 
  central_or_shiftOptions_["m_LeptonIdx1_LeptonIdx2_Approach2"]        = { "central" }; 
  central_or_shiftOptions_["m_LeptonIdx2_LeptonIdx3_Approach2"]        = { "central" }; 
  central_or_shiftOptions_["m_LeptonIdx1_LeptonIdx3_Approach2"]        = { "central" }; 
  central_or_shiftOptions_["dPhi_LeptonIdx1_LeptonIdx2_Approach2"]     = { "central" }; 
  central_or_shiftOptions_["dPhi_LeptonIdx2_LeptonIdx3_Approach2"]     = { "central" }; 
  central_or_shiftOptions_["dPhi_LeptonIdx1_LeptonIdx3_Approach2"]     = { "central" }; 
  central_or_shiftOptions_["dr_LeptonIdx1_LeptonIdx2_Approach2"]       = { "central" }; 
  central_or_shiftOptions_["dr_LeptonIdx2_LeptonIdx3_Approach2"]       = { "central" }; 
  central_or_shiftOptions_["dr_LeptonIdx1_LeptonIdx3_Approach2"]       = { "central" }; 
  central_or_shiftOptions_["m_LeptonIdx3_Jet1_Approach2"]              = { "central" }; 
  central_or_shiftOptions_["dr_LeptonIdx3_Jet1_Approach2"]             = { "central" }; 
  central_or_shiftOptions_["m_LeptonIdx3_JetNear_Approach2"]           = { "central" }; 
  central_or_shiftOptions_["dr_LeptonIdx3_JetNear_Approach2"]          = { "central" };   
  //
  central_or_shiftOptions_["eventCategory"]                  = { "central" };
  //
  central_or_shiftOptions_["mvaOutput_xgb_WZctrl_SFstudy_SUMBk_HH"]   = { "*" };
  //
  central_or_shiftOptions_["hpt_vs_eta_lepton3_mu"]                   = { "central" };
  central_or_shiftOptions_["hpt_vs_eta_lepton3_e"]                    = { "central" };
  //
  central_or_shiftOptions_["EventCounter"]                   = { "*" }; 
}

const TH1 *
EvtHistManager_WZctrl_SFstudy::getHistogram_EventCounter() const
{
  return hEventCounter_;
}

void
EvtHistManager_WZctrl_SFstudy::bookHistograms(TFileDirectory & dir)
{
  hnumElectrons_                    = book1D(dir, "numElectrons",                "numElectrons",                 5, -0.5,  +4.5); 
  hnumMuons_                        = book1D(dir, "numMuons",                    "numMuons",                     5, -0.5,  +4.5); 
  hnumLeptons_                      = book1D(dir, "numLeptons",                  "numLeptons",                   8, -0.5,  +7.5); 
  hsumLeptonCharge_3l_              = book1D(dir, "sumLeptonCharge_3l",          "sumLeptonCharge_3l",           7, -3.5,  +3.5);
  hsumLeptonCharge_FullSel_         = book1D(dir, "sumLeptonCharge_FullSel",     "sumLeptonCharge_FullSel",     19, -9.5,  +9.5); 
  hnumSameFlavor_OS_3l_             = book1D(dir, "numSameFlavor_OS_3l",         "numSameFlavor_OS_3l",          9, -0.5,  +8.5); 
  hnumSameFlavor_OS_FullPresel_     = book1D(dir, "numSameFlavor_OS_FullPresel", "numSameFlavor_OS_FullPresel",  9, -0.5,  +8.5); 
  hnJetAK4_                         = book1D(dir, "nJetAK4",                     "nJetAK4",                     20, -0.5, +19.5); 
  hnBJetLoose_                      = book1D(dir, "nBJetLoose",                  "nBJetLoose",                  20, -0.5, +19.5 ); 
  hnBJetMedium_                     = book1D(dir, "nBJetMedium",                 "nBJetMedium",                 20, -0.5, +19.5); 
  hnJetAK8_                         = book1D(dir, "nJetAK8",                     "nJetAK8",                     20, -0.5, +19.5); 
  hnJetAK8_wSelectorAK8_Wjj_        = book1D(dir, "nJetAK8_wSelectorAK8_Wjj",    "nJetAK8_wSelectorAK8_Wjj",    20, -0.5, +19.5);
  //
  hlep1_pt_                         = book1D(dir, "lep1_pt",                     "lep1_pt",                    200, 0,400 ); 
  hlep1_conePt_                     = book1D(dir, "lep1_conePt",                 "lep1_conePt",                200, 0,400); 
  hlep1_eta_                        = book1D(dir, "lep1_eta",                    "lep1_eta",                   200,-5,5); 
  hmindr_lep1_jet_                  = book1D(dir, "mindr_lep1_jet",              "mindr_lep1_jet",             200, 0, 3); 
  hmT_MEtLep1_                      = book1D(dir, "mT_MEtLep1",                  "mT_MEtLep1",                 200, 0,500);
  //
  hlep2_pt_                         = book1D(dir, "lep2_pt",                     "lep2_pt",                    200, 0,400); 
  hlep2_conePt_                     = book1D(dir, "lep2_conePt",                 "lep2_conePt",                200, 0,400); 
  hlep2_eta_                        = book1D(dir, "lep2_eta",                    "lep2_eta",                   200,-5,5); 
  hmindr_lep2_jet_                  = book1D(dir, "mindr_lep2_jet",              "mindr_lep2_jet",             200, 0, 3); 
  hmT_MEtLep2_                      = book1D(dir, "mT_MEtLep2",                  "mT_MEtLep2",                 200, 0,500);
  //
  hlep3_pt_                         = book1D(dir, "lep3_pt",                     "lep3_pt",                    200, 0,400); 
  hlep3_conePt_                     = book1D(dir, "lep3_conePt",                 "lep3_conePt",                200, 0,400); 
  hlep3_eta_                        = book1D(dir, "lep3_eta",                    "lep3_eta",                   200,-5,5); 
  hmindr_lep3_jet_                  = book1D(dir, "mindr_lep3_jet",              "mindr_lep3_jet",             200, 0, 3); 
  hmT_MEtLep3_                      = book1D(dir, "mT_MEtLep3",                  "mT_MEtLep3",                 200, 0,500);
  //
  hjet1_pt_                         = book1D(dir, "jet1_pt",                     "jet1_pt",                    200, 0,400); 
  hjet2_pt_                         = book1D(dir, "jet2_pt",                     "jet2_pt",                    200, 0,400); 
  hjet1plus2pt_                     = book1D(dir, "jet1plus2pt",                 "jet1plus2pt",                200, 0,600); 
  hjet1_m_                          = book1D(dir, "jet1_m",                      "jet1_m",                     200, 0,500); 
  hjet2_m_                          = book1D(dir, "jet2_m",                      "jet2_m",                     200, 0,500);
  //
  havg_dr_jet_                      = book1D(dir, "avg_dr_jet",                  "avg_dr_jet",                 200, 0, 3);
  hdr_Wjj_                          = book1D(dir, "dr_Wjj",                     "dr_Wjj",                      200, 0, 3);
  //
  hdr_l12_                          = book1D(dir, "dr_l12",                     "dr_l12",                      200, 0, 3); 
  hdr_l23_                          = book1D(dir, "dr_l23",                     "dr_l23",                      200, 0, 3); 
  hdr_l13_                          = book1D(dir, "dr_l13",                     "dr_l13",                      200, 0, 3); 
  hdr_lss_                          = book1D(dir, "dr_lss",                     "dr_lss",                      200, 0, 3); 
  hdr_los_min_                      = book1D(dir, "dr_los_min",                 "dr_los_min",                  200, 0, 3); 
  hdr_los_max_                      = book1D(dir, "dr_los_max",                 "dr_los_max",                  200, 0, 3);
  //
  hdr_WjjLepIdx3_                   = book1D(dir, "dr_WjjLepIdx3",              "dr_WjjLepIdx3",               200, 0, 3); 
  hdr_Wjet1LepIdx3_                 = book1D(dir, "dr_Wjet1LepIdx3",            "dr_Wjet1LepIdx3",             200, 0, 3); 
  hdr_Wjet2LepIdx3_                 = book1D(dir, "dr_Wjet2LepIdx3",            "dr_Wjet2LepIdx3",             200, 0, 3); 
  hdr_LepIdx3WjetNear_              = book1D(dir, "dr_LepIdx3WjetNear",         "dr_LepIdx3WjetNear",          200, 0, 3); 
  hdr_LepIdx3WjetFar_               = book1D(dir, "dr_LepIdx3WjetFar",          "dr_LepIdx3WjetFar",           200, 0, 3);
  //
  hmet_                             = book1D(dir, "met",                        "met",                         200, 0,500); 
  hmht_                             = book1D(dir, "mht",                        "mht",                         200, 0,500); 
  hmet_LD_                          = book1D(dir, "met_LD",                     "met_LD",                      200, 0,500); 
  hHT_                              = book1D(dir, "HT",                         "HT",                          200, 0,1000); 
  hSTMET_                           = book1D(dir, "STMET",                      "STMET",                       200, 0,1000);
  //
  hmSFOS2l_                         = book1D(dir, "mSFOS2l",                    "mSFOS2l",                     200, 0,  400); 
  hWTojjMass_                       = book1D(dir, "WTojjMass",                  "WTojjMass",                   200, 0,  500); 
  hdihiggsVisMass_sel_              = book1D(dir, "dihiggsVisMass_sel",         "dihiggsVisMass_sel",          200, 0, 1500); 
  hdihiggsMass_                     = book1D(dir, "dihiggsMass",                "dihiggsMass",                 200, 0, 1500); 
  hmTMetLepton1_                    = book1D(dir, "mTMetLepton1",               "mTMetLepton1",                200, 0,  400); 
  hmTMetLepton2_                    = book1D(dir, "mTMetLepton2",               "mTMetLepton2",                200, 0,  400);
  //
  hlep1_isTight_                    = book1D(dir, "lep1_isTight",               "lep1_isTight",                5, -2.5, 2.5); 
  hlep2_isTight_                    = book1D(dir, "lep2_isTight",               "lep2_isTight",                5, -2.5, 2.5); 
  hlep3_isTight_                    = book1D(dir, "lep3_isTight",               "lep3_isTight",                5, -2.5, 2.5);
  //
  hlep1_genLepPt_                   = book1D(dir, "lep1_genLepPt",              "lep1_genLepPt",               200, 0, 400); 
  hlep2_genLepPt_                   = book1D(dir, "lep2_genLepPt",              "lep2_genLepPt",               200, 0, 400); 
  hlep3_genLepPt_                   = book1D(dir, "lep3_genLepPt",              "lep3_genLepPt",               200, 0, 400); 
  hlep1_frWeight_                   = book1D(dir, "lep1_frWeight",              "lep1_frWeight",               200, -0.5, 2.0); 
  hlep2_frWeight_                   = book1D(dir, "lep2_frWeight",              "lep2_frWeight",               200, -0.5, 2.0); 
  hlep3_frWeight_                   = book1D(dir, "lep3_frWeight",              "lep3_frWeight",               200, -0.5, 2.0); 
  hlep1_fake_prob_                  = book1D(dir, "lep1_fake_prob",             "lep1_fake_prob",              200, -0.5, 2.0); 
  hlep2_fake_prob_                  = book1D(dir, "lep2_fake_prob",             "lep2_fake_prob",              200, -0.5, 2.0); 
  hlep3_fake_prob_                  = book1D(dir, "lep3_fake_prob",             "lep3_fake_prob",              200, -0.5, 2.0);
  //
  hmT_LeptonIdx1_Met_Approach0_               = book1D(dir, "mT_LeptonIdx1_Met_Approach0",             "mT_LeptonIdx1_Met_Approach0",             200, 0,500); 
  hmT_LeptonIdx2_Met_Approach0_               = book1D(dir, "mT_LeptonIdx2_Met_Approach0",             "mT_LeptonIdx2_Met_Approach0",             200, 0,500); 
  hmT_LeptonIdx3_Met_Approach0_               = book1D(dir, "mT_LeptonIdx3_Met_Approach0",             "mT_LeptonIdx3_Met_Approach0",             200, 0,500);
  //
  hm_LeptonIdx1_LeptonIdx2_Approach0_         = book1D(dir, "m_LeptonIdx1_LeptonIdx2_Approach0",       "m_LeptonIdx1_LeptonIdx2_Approach0",       200, 0,200); 
  hm_LeptonIdx2_LeptonIdx3_Approach0_         = book1D(dir, "m_LeptonIdx2_LeptonIdx3_Approach0",       "m_LeptonIdx2_LeptonIdx3_Approach0",       200, 0,200); 
  hm_LeptonIdx1_LeptonIdx3_Approach0_         = book1D(dir, "m_LeptonIdx1_LeptonIdx3_Approach0",       "m_LeptonIdx1_LeptonIdx3_Approach0",       200, 0,200);
  //
  hdPhi_LeptonIdx1_LeptonIdx2_Approach0_      = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx2_Approach0",    "dPhi_LeptonIdx1_LeptonIdx2_Approach0",    200, 0,3.14); 
  hdPhi_LeptonIdx2_LeptonIdx3_Approach0_      = book1D(dir, "dPhi_LeptonIdx2_LeptonIdx3_Approach0",    "dPhi_LeptonIdx2_LeptonIdx3_Approach0",    200, 0,3.14); 
  hdPhi_LeptonIdx1_LeptonIdx3_Approach0_      = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx3_Approach0",    "dPhi_LeptonIdx1_LeptonIdx3_Approach0",    200, 0,3.14);
  //
  hdr_LeptonIdx1_LeptonIdx2_Approach0_        = book1D(dir, "dr_LeptonIdx1_LeptonIdx2_Approach0",      "dr_LeptonIdx1_LeptonIdx2_Approach0",      200, 0, 3); 
  hdr_LeptonIdx2_LeptonIdx3_Approach0_        = book1D(dir, "dr_LeptonIdx2_LeptonIdx3_Approach0",      "dr_LeptonIdx2_LeptonIdx3_Approach0",      200, 0, 3); 
  hdr_LeptonIdx1_LeptonIdx3_Approach0_        = book1D(dir, "dr_LeptonIdx1_LeptonIdx3_Approach0",      "dr_LeptonIdx1_LeptonIdx3_Approach0",      200, 0, 3);
  //
  hm_LeptonIdx3_Jet1_Approach0_               = book1D(dir, "m_LeptonIdx3_Jet1_Approach0",             "m_LeptonIdx3_Jet1_Approach0",             200, 0,200); 
  hdr_LeptonIdx3_Jet1_Approach0_              = book1D(dir, "dr_LeptonIdx3_Jet1_Approach0",            "dr_LeptonIdx3_Jet1_Approach0",            200, 0, 3);
  //
  hm_LeptonIdx3_JetNear_Approach0_            = book1D(dir, "m_LeptonIdx3_JetNear_Approach0",          "m_LeptonIdx3_JetNear_Approach0",          200, 0,200); 
  hdr_LeptonIdx3_JetNear_Approach0_           = book1D(dir, "dr_LeptonIdx3_JetNear_Approach0",         "dr_LeptonIdx3_JetNear_Approach0",         200, 0, 3);
  //
  hmT_LeptonIdx1_Met_Approach2_               = book1D(dir, "mT_LeptonIdx1_Met_Approach2",             "mT_LeptonIdx1_Met_Approach2",             200, 0,500); 
  hmT_LeptonIdx2_Met_Approach2_               = book1D(dir, "mT_LeptonIdx2_Met_Approach2",             "mT_LeptonIdx2_Met_Approach2",             200, 0,500); 
  hmT_LeptonIdx3_Met_Approach2_               = book1D(dir, "mT_LeptonIdx3_Met_Approach2",             "mT_LeptonIdx3_Met_Approach2",             200, 0,500);
  //
  hm_LeptonIdx1_LeptonIdx2_Approach2_         = book1D(dir, "m_LeptonIdx1_LeptonIdx2_Approach2",       "m_LeptonIdx1_LeptonIdx2_Approach2",       200, 0,200); 
  hm_LeptonIdx2_LeptonIdx3_Approach2_         = book1D(dir, "m_LeptonIdx2_LeptonIdx3_Approach2",       "m_LeptonIdx2_LeptonIdx3_Approach2",       200, 0,200); 
  hm_LeptonIdx1_LeptonIdx3_Approach2_         = book1D(dir, "m_LeptonIdx1_LeptonIdx3_Approach2",       "m_LeptonIdx1_LeptonIdx3_Approach2",       200, 0,200);
  //
  hdPhi_LeptonIdx1_LeptonIdx2_Approach2_      = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx2_Approach2",    "dPhi_LeptonIdx1_LeptonIdx2_Approach2",    200, 0,3.14); 
  hdPhi_LeptonIdx2_LeptonIdx3_Approach2_      = book1D(dir, "dPhi_LeptonIdx2_LeptonIdx3_Approach2",    "dPhi_LeptonIdx2_LeptonIdx3_Approach2",    200, 0,3.14); 
  hdPhi_LeptonIdx1_LeptonIdx3_Approach2_      = book1D(dir, "dPhi_LeptonIdx1_LeptonIdx3_Approach2",    "dPhi_LeptonIdx1_LeptonIdx3_Approach2",    200, 0,3.14);
  //
  hdr_LeptonIdx1_LeptonIdx2_Approach2_        = book1D(dir, "dr_LeptonIdx1_LeptonIdx2_Approach2",      "dr_LeptonIdx1_LeptonIdx2_Approach2",      200, 0, 3); 
  hdr_LeptonIdx2_LeptonIdx3_Approach2_        = book1D(dir, "dr_LeptonIdx2_LeptonIdx3_Approach2",      "dr_LeptonIdx2_LeptonIdx3_Approach2",      200, 0, 3); 
  hdr_LeptonIdx1_LeptonIdx3_Approach2_        = book1D(dir, "dr_LeptonIdx1_LeptonIdx3_Approach2",      "dr_LeptonIdx1_LeptonIdx3_Approach2",      200, 0, 3);
  //
  hm_LeptonIdx3_Jet1_Approach2_               = book1D(dir, "m_LeptonIdx3_Jet1_Approach2",             "m_LeptonIdx3_Jet1_Approach2",             200, 0,200); 
  hdr_LeptonIdx3_Jet1_Approach2_              = book1D(dir, "dr_LeptonIdx3_Jet1_Approach2",            "dr_LeptonIdx3_Jet1_Approach2",            200, 0, 3);
  //
  hm_LeptonIdx3_JetNear_Approach2_            = book1D(dir, "m_LeptonIdx3_JetNear_Approach2",          "m_LeptonIdx3_JetNear_Approach2",          200, 0,200); 
  hdr_LeptonIdx3_JetNear_Approach2_           = book1D(dir, "dr_LeptonIdx3_JetNear_Approach2",         "dr_LeptonIdx3_JetNear_Approach2",         200, 0, 3);   
  //
  heventCategory_                   = book1D(dir, "eventCategory",              "eventCategory",               6, -0.5, 5.5); 
  hmvaOutput_xgb_WZctrl_SFstudy_SUMBk_HH_    = book1D(dir, "mvaOutput_xgb_WZctrl_SFstudy_SUMBk_HH","mvaOutput_xgb_WZctrl_SFstudy_SUMBk_HH",120,  0., 1.);
  //
  hEventCounter_                    = book1D(dir, "EventCounter", "EventCounter",                              1, -0.5, +0.5);

  
  int    nBinsX_leptonSF_pt_vs_eta_mu  = 4;
  double binsX_leptonSF_pt_vs_eta_mu[] = {0, 0.9, 1.2, 2.1, 2.4};
  
  int    nBinsY_leptonSF_pt_vs_eta_mu  = 10;
  double binsY_leptonSF_pt_vs_eta_mu[] = {10, 15, 20, 25, 30, 35, 40, 45, 60, 80, 120};
  
  int    nBinsX_leptonSF_pt_vs_eta_e   = 4;
  double binsX_leptonSF_pt_vs_eta_e[]  = {0, 0.9, 1.2, 2.1, 2.5};
  
  int    nBinsY_leptonSF_pt_vs_eta_e   = 10;
  double binsY_leptonSF_pt_vs_eta_e[]  = {10, 15, 20, 25, 30, 35, 40, 45, 60, 80, 120};

  hpt_vs_eta_lepton3_mu = book2D(dir, "hpt_vs_eta_lepton3_mu", "hpt_vs_eta_lepton3_mu", nBinsX_leptonSF_pt_vs_eta_mu,binsX_leptonSF_pt_vs_eta_mu, nBinsY_leptonSF_pt_vs_eta_mu,binsY_leptonSF_pt_vs_eta_mu);
  hpt_vs_eta_lepton3_e  = book2D(dir, "hpt_vs_eta_lepton3_e",  "hpt_vs_eta_lepton3_e",  nBinsX_leptonSF_pt_vs_eta_e, binsX_leptonSF_pt_vs_eta_e,  nBinsY_leptonSF_pt_vs_eta_e, binsY_leptonSF_pt_vs_eta_e);
}

void
EvtHistManager_WZctrl_SFstudy::fillHistograms(
		   int numElectrons,
		   int numMuons,
		   int numLeptons,
		   int sumLeptonCharge_3l,
		   int sumLeptonCharge_FullSel,
		   int numSameFlavor_OS_3l,
		   int numSameFlavor_OS_FullPresel,
		   int nJetAK4,
		   int nBJetLoose,
		   int nBJetMedium,
		   int nJetAK8,
		   int nJetAK8_wSelectorAK8_Wjj,
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
		   double jet2_pt,
		   double jet1plus2pt,
		   double jet1_m,
		   double jet2_m,
		   //
		   double avg_dr_jet,
		   double dr_Wjj,
		   //
		   double dr_l12,
		   double dr_l23,
		   double dr_l13,
		   double dr_lss,
		   double dr_los_min,
		   double dr_los_max,
		   //
		   double dr_WjjLepIdx3,
		   double dr_Wjet1LepIdx3,
		   double dr_Wjet2LepIdx3,
		   double dr_LepIdx3WjetNear,
		   double dr_LepIdx3WjetFar,
		   //
		   double met,
		   double mht,
		   double met_LD,
		   double HT,
		   double STMET,
		   //
		   double mSFOS2l,
		   double WTojjMass,
		   double dihiggsVisMass_sel,
		   double dihiggsMass,
		   double mTMetLepton1,
		   double mTMetLepton2,
		   //
		   double lep1_isTight,
		   double lep2_isTight,
		   double lep3_isTight,
		   //
		   double lep1_genLepPt,
		   double lep2_genLepPt,
		   double lep3_genLepPt,
		   double lep1_frWeight,
		   double lep2_frWeight,
		   double lep3_frWeight,
		   double lep1_fake_prob,
		   double lep2_fake_prob,
		   double lep3_fake_prob,
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
		   int eventCategory,
		   //
		   double mvaOutput_xgb_WZctrl_SFstudy_SUMBk_HH,
		   //
		   int    lepton3PID,
		   double lepton3_pt,
		   double lepton3_eta,
		   //
		   double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(hnumElectrons_,                  numElectrons,                  evtWeight, evtWeightErr); 
  fillWithOverFlow(hnumMuons_,                      numMuons,                      evtWeight, evtWeightErr); 
  fillWithOverFlow(hnumLeptons_,                    numLeptons,                    evtWeight, evtWeightErr); 
  fillWithOverFlow(hsumLeptonCharge_3l_,            sumLeptonCharge_3l,            evtWeight, evtWeightErr); 
  fillWithOverFlow(hsumLeptonCharge_FullSel_,       sumLeptonCharge_FullSel,       evtWeight, evtWeightErr); 
  fillWithOverFlow(hnumSameFlavor_OS_3l_,           numSameFlavor_OS_3l,           evtWeight, evtWeightErr); 
  fillWithOverFlow(hnumSameFlavor_OS_FullPresel_,   numSameFlavor_OS_FullPresel,   evtWeight, evtWeightErr);
  fillWithOverFlow(hnJetAK4_,                       nJetAK4,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hnBJetLoose_,                    nBJetLoose,                    evtWeight, evtWeightErr); 
  fillWithOverFlow(hnBJetMedium_,                   nBJetMedium,                   evtWeight, evtWeightErr); 
  fillWithOverFlow(hnJetAK8_,                       nJetAK8,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hnJetAK8_wSelectorAK8_Wjj_,      nJetAK8_wSelectorAK8_Wjj,      evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hlep1_pt_,                       lep1_pt,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep1_conePt_,                   lep1_conePt,                   evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep1_eta_,                      lep1_eta,                      evtWeight, evtWeightErr); 
  fillWithOverFlow(hmindr_lep1_jet_,                mindr_lep1_jet,                evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_MEtLep1_,                    mT_MEtLep1,                    evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hlep2_pt_,                       lep2_pt,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep2_conePt_,                   lep2_conePt,                   evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep2_eta_,                      lep2_eta,                      evtWeight, evtWeightErr); 
  fillWithOverFlow(hmindr_lep2_jet_,                mindr_lep2_jet,                evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_MEtLep2_,                    mT_MEtLep2,                    evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hlep3_pt_,                       lep3_pt,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep3_conePt_,                   lep3_conePt,                   evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep3_eta_,                      lep3_eta,                      evtWeight, evtWeightErr); 
  fillWithOverFlow(hmindr_lep3_jet_,                mindr_lep3_jet,                evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_MEtLep3_,                    mT_MEtLep3,                    evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hjet1_pt_,                       jet1_pt,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hjet2_pt_,                       jet2_pt,                       evtWeight, evtWeightErr); 
  fillWithOverFlow(hjet1plus2pt_,                   jet1plus2pt,                   evtWeight, evtWeightErr); 
  fillWithOverFlow(hjet1_m_,                        jet1_m,                        evtWeight, evtWeightErr); 
  fillWithOverFlow(hjet2_m_,                        jet2_m,                        evtWeight, evtWeightErr);
  //
  fillWithOverFlow(havg_dr_jet_,                    avg_dr_jet,                    evtWeight, evtWeightErr);
  fillWithOverFlow(hdr_Wjj_,                        dr_Wjj,                        evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hdr_l12_,                        dr_l12,                        evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_l23_,                        dr_l23,                        evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_l13_,                        dr_l13,                        evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_lss_,                        dr_lss,                        evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_los_min_,                    dr_los_min,                    evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_los_max_,                    dr_los_max,                    evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_WjjLepIdx3_,                 dr_WjjLepIdx3,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_Wjet1LepIdx3_,               dr_Wjet1LepIdx3,               evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_Wjet2LepIdx3_,               dr_Wjet2LepIdx3,               evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LepIdx3WjetNear_,            dr_LepIdx3WjetNear,            evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LepIdx3WjetFar_,             dr_LepIdx3WjetFar,             evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hmet_,                           met,                           evtWeight, evtWeightErr); 
  fillWithOverFlow(hmht_,                           mht,                           evtWeight, evtWeightErr); 
  fillWithOverFlow(hmet_LD_,                        met_LD,                        evtWeight, evtWeightErr); 
  fillWithOverFlow(hHT_,                            HT,                            evtWeight, evtWeightErr); 
  fillWithOverFlow(hSTMET_,                         STMET,                         evtWeight, evtWeightErr);
  //
  if (mSFOS2l > 0.) 
    fillWithOverFlow(hmSFOS2l_,                     mSFOS2l,                       evtWeight, evtWeightErr); 
  if (WTojjMass > 0.)
    fillWithOverFlow(hWTojjMass_,                   WTojjMass,                     evtWeight, evtWeightErr);
  if (dihiggsVisMass_sel > 0.)
    fillWithOverFlow(hdihiggsVisMass_sel_,          dihiggsVisMass_sel,            evtWeight, evtWeightErr);
  if (dihiggsMass > 0.)
    fillWithOverFlow(hdihiggsMass_,                 dihiggsMass,                   evtWeight, evtWeightErr); 
  fillWithOverFlow(hmTMetLepton1_,                  mTMetLepton1,                  evtWeight, evtWeightErr); 
  fillWithOverFlow(hmTMetLepton2_,                  mTMetLepton2,                  evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hlep1_isTight_,                  lep1_isTight,                  evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep2_isTight_,                  lep2_isTight,                  evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep3_isTight_,                  lep3_isTight,                  evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep1_genLepPt_,                 lep1_genLepPt,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep2_genLepPt_,                 lep2_genLepPt,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep3_genLepPt_,                 lep3_genLepPt,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep1_frWeight_,                 lep1_frWeight,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep2_frWeight_,                 lep2_frWeight,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep3_frWeight_,                 lep3_frWeight,                 evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep1_fake_prob_,                lep1_fake_prob,                evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep2_fake_prob_,                lep2_fake_prob,                evtWeight, evtWeightErr); 
  fillWithOverFlow(hlep3_fake_prob_,                lep3_fake_prob,                evtWeight, evtWeightErr); 
  fillWithOverFlow(heventCategory_,                 eventCategory,                 evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hmT_LeptonIdx1_Met_Approach0_,             mT_LeptonIdx1_Met_Approach0,             evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx2_Met_Approach0_,             mT_LeptonIdx2_Met_Approach0,             evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx3_Met_Approach0_,             mT_LeptonIdx3_Met_Approach0,             evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx1_LeptonIdx2_Approach0_,       m_LeptonIdx1_LeptonIdx2_Approach0,       evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx2_LeptonIdx3_Approach0_,       m_LeptonIdx2_LeptonIdx3_Approach0,       evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx1_LeptonIdx3_Approach0_,       m_LeptonIdx1_LeptonIdx3_Approach0,       evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx1_LeptonIdx2_Approach0_,    dPhi_LeptonIdx1_LeptonIdx2_Approach0,    evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx2_LeptonIdx3_Approach0_,    dPhi_LeptonIdx2_LeptonIdx3_Approach0,    evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx1_LeptonIdx3_Approach0_,    dPhi_LeptonIdx1_LeptonIdx3_Approach0,    evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx1_LeptonIdx2_Approach0_,      dr_LeptonIdx1_LeptonIdx2_Approach0,      evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx2_LeptonIdx3_Approach0_,      dr_LeptonIdx2_LeptonIdx3_Approach0,      evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx1_LeptonIdx3_Approach0_,      dr_LeptonIdx1_LeptonIdx3_Approach0,      evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx3_Jet1_Approach0_,             m_LeptonIdx3_Jet1_Approach0,             evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx3_Jet1_Approach0_,            dr_LeptonIdx3_Jet1_Approach0,            evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx3_JetNear_Approach0_,          m_LeptonIdx3_JetNear_Approach0,          evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx3_JetNear_Approach0_,         dr_LeptonIdx3_JetNear_Approach0,         evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx1_Met_Approach2_,             mT_LeptonIdx1_Met_Approach2,             evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx2_Met_Approach2_,             mT_LeptonIdx2_Met_Approach2,             evtWeight, evtWeightErr); 
  fillWithOverFlow(hmT_LeptonIdx3_Met_Approach2_,             mT_LeptonIdx3_Met_Approach2,             evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx1_LeptonIdx2_Approach2_,       m_LeptonIdx1_LeptonIdx2_Approach2,       evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx2_LeptonIdx3_Approach2_,       m_LeptonIdx2_LeptonIdx3_Approach2,       evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx1_LeptonIdx3_Approach2_,       m_LeptonIdx1_LeptonIdx3_Approach2,       evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx1_LeptonIdx2_Approach2_,    dPhi_LeptonIdx1_LeptonIdx2_Approach2,    evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx2_LeptonIdx3_Approach2_,    dPhi_LeptonIdx2_LeptonIdx3_Approach2,    evtWeight, evtWeightErr); 
  fillWithOverFlow(hdPhi_LeptonIdx1_LeptonIdx3_Approach2_,    dPhi_LeptonIdx1_LeptonIdx3_Approach2,    evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx1_LeptonIdx2_Approach2_,      dr_LeptonIdx1_LeptonIdx2_Approach2,      evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx2_LeptonIdx3_Approach2_,      dr_LeptonIdx2_LeptonIdx3_Approach2,      evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx1_LeptonIdx3_Approach2_,      dr_LeptonIdx1_LeptonIdx3_Approach2,      evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx3_Jet1_Approach2_,             m_LeptonIdx3_Jet1_Approach2,             evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx3_Jet1_Approach2_,            dr_LeptonIdx3_Jet1_Approach2,            evtWeight, evtWeightErr); 
  fillWithOverFlow(hm_LeptonIdx3_JetNear_Approach2_,          m_LeptonIdx3_JetNear_Approach2,          evtWeight, evtWeightErr); 
  fillWithOverFlow(hdr_LeptonIdx3_JetNear_Approach2_,         dr_LeptonIdx3_JetNear_Approach2,         evtWeight, evtWeightErr);   
  //
  fillWithOverFlow(hmvaOutput_xgb_WZctrl_SFstudy_SUMBk_HH_,  mvaOutput_xgb_WZctrl_SFstudy_SUMBk_HH,  evtWeight, evtWeightErr);
  //
  if      (abs(lepton3PID) == 13)  fillWithOverFlow2d(hpt_vs_eta_lepton3_mu, abs(lepton3_eta), lepton3_pt, evtWeight, evtWeightErr);
  else if (abs(lepton3PID) == 11)  fillWithOverFlow2d(hpt_vs_eta_lepton3_e,  abs(lepton3_eta), lepton3_pt, evtWeight, evtWeightErr);
  //
  fillWithOverFlow(hEventCounter_,                  0.,                            evtWeight, evtWeightErr);
}
 
