#ifndef hhAnalysis_multilepton_EvtHistManager_hh_3l_h
#define hhAnalysis_multilepton_EvtHistManager_hh_3l_h

/** \class EvtHistManager_hh_3l
 *
 * Book and fill histograms for event-level quantities in ttH multilepton analysis
 * in 3l category
 *
 * \author Christian Veelken, Tallin
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

class EvtHistManager_hh_3l
  : public HistManagerBase
{
 public:
  EvtHistManager_hh_3l(const edm::ParameterSet & cfg, bool isControlRegion = false);
  ~EvtHistManager_hh_3l() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(
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
  //
  //  
  double evtWeight);

  
  const TH1 *
  getHistogram_EventCounter() const;

 private:
  bool isControlRegion_;
  
  TH1 * hnumElectrons_;
  TH1 * hnumMuons_;
  TH1 * hnJetAK4_;
  TH1 * hnBJetLoose_;
  TH1 * hnJetAK8_wSelectorAK8_Wjj_;
  //
  TH1 * hsumLeptonCharge_3l_;
  TH1 * hnumSameFlavor_OS_Full_;  
  TH1 * hnumSameFlavor_OS_3l_;
  //
  TH1 * hlep1_pt_;
  TH1 * hlep1_conePt_;
  TH1 * hlep1_eta_;
  TH1 * hmindr_lep1_jet_;
  TH1 * hmT_MEtLep1_;
  //
  TH1 * hlep2_pt_;
  TH1 * hlep2_conePt_;
  TH1 * hlep2_eta_;
  TH1 * hmindr_lep2_jet_;
  TH1 * hmT_MEtLep2_;
  //
  TH1 * hlep3_pt_;
  TH1 * hlep3_conePt_;
  TH1 * hlep3_eta_;
  TH1 * hmindr_lep3_jet_;
  TH1 * hmT_MEtLep3_;
  //
  TH1 * hjet1_pt_;
  TH1 * hjet1_eta_;
  TH1 * hjet2_pt_;
  TH1 * hjet2_eta_;
  TH1 * hjet1plus2_pt_;
  TH1 * hjet1plus2_eta_;
  TH1 * hjet1_m_;
  TH1 * hjet2_m_;
  //
  TH1 * hmet_;
  TH1 * hmht_;
  TH1 * hmet_LD_;
  TH1 * hHT_;
  TH1 * hSTMET_;
  //
  TH1 * hmSFOS2l_closestToZ_;
  TH1 * hm3l_;
  TH1 * hWTojjMass_;
  TH1 * hdihiggsVisMass_sel_;
  TH1 * hdihiggsVisMass_sel_inclusive1j_;
  TH1 * hdihiggsMass_;
  TH1 * hdihiggsMass_inclusive1j_;
  //
  TH1 * hmTMetLepton1_chargeEqualSumCharge3l_;
  TH1 * hmTMetLepton2_chargeEqualSumCharge3l_;
  //
  TH1 * hdr_l12_;
  TH1 * hdr_l23_;
  TH1 * hdr_l13_;
  TH1 * hdr_lss_;
  TH1 * hdr_los_min_;
  TH1 * hdr_los_max_;
  //
  TH1 * havg_dr_jet_;
  TH1 * hdr_Wjj_;
  //
  TH1 * hdPhi_3l_2j_;
  TH1 * hdPhi_3l_2j_inclusive1j_;
  TH1 * hdEta_3l_2j_;
  TH1 * hdEta_3l_2j_inclusive1j_;
  TH1 * hdR_3l_2j_;
  TH1 * hdR_3l_2j_inclusive1j_;
  //
  TH1 * hdEta_3l_avg2j_;
  TH1 * hdEta_3l_avg2j_inclusive1j_;
  //
  TH1 * hbTag_jet1_;
  TH1 * hbTag_jet2_;
  TH1 * hbTag_sum_jet1And2_;
  TH1 * hbTag_max_jet1or2_;
  TH1 * hbTag_max_AK4_;
  TH1 * hbTag_sum_AK4_;
  //
  TH1 * hpt_lastAK4_;
  //
  TH1 *hm_AK8_;
  //
  //
  TH1 * hmT_LeptonIdx1_Met_Approach0_;
  TH1 * hmT_LeptonIdx2_Met_Approach0_;
  TH1 * hmT_LeptonIdx3_Met_Approach0_;
  //
  TH1 * hm_LeptonIdx1_LeptonIdx2_Approach0_;
  TH1 * hm_LeptonIdx2_LeptonIdx3_Approach0_;
  TH1 * hm_LeptonIdx1_LeptonIdx3_Approach0_;
  //
  TH1 * hdPhi_LeptonIdx1_LeptonIdx2_Approach0_;
  TH1 * hdPhi_LeptonIdx2_LeptonIdx3_Approach0_;
  TH1 * hdPhi_LeptonIdx1_LeptonIdx3_Approach0_;
  //
  TH1 * hdEta_LeptonIdx1_LeptonIdx2_Approach0_;
  TH1 * hdEta_LeptonIdx2_LeptonIdx3_Approach0_;
  TH1 * hdEta_LeptonIdx1_LeptonIdx3_Approach0_;
  //
  TH1 * hdr_LeptonIdx1_LeptonIdx2_Approach0_;
  TH1 * hdr_LeptonIdx2_LeptonIdx3_Approach0_;
  TH1 * hdr_LeptonIdx1_LeptonIdx3_Approach0_;
  //
  TH1 * hm_LeptonIdx3_Jet1_Approach0_;
  TH1 * hdr_LeptonIdx3_Jet1_Approach0_;
  //
  TH1 * hm_LeptonIdx3_JetNear_Approach0_;
  TH1 * hdr_LeptonIdx3_JetNear_Approach0_;
  //
  TH1 * hdr_LeptonIdx3_2j_Approach0_;
  TH1 * hdr_LeptonIdx3_2j_inclusive1j_Approach0_;
  //
  TH1 *hdr_LeptonIdx3_AK4jNear_Approach0_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_Approach0_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach0_;
  TH1 *hm_LeptonIdx3_2AK4jNear_Approach0_;
  TH1 *hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach0_;
  TH1 *hdr_2AK4J_NearestToLeptonIdx3_Approach0_;
  //
  TH1 *hdr_LeptonIdx3_AK8_Approach0_;
  TH1 *hm_LeptonIdx3_AK8_Approach0_;
  //
  TH1 * hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0_;
  //
  TH1 *hdPhi_LeptonIdx3_Met_Approach0_;
  //
  //
  TH1 * hmT_LeptonIdx1_Met_Approach2_;
  TH1 * hmT_LeptonIdx2_Met_Approach2_;
  TH1 * hmT_LeptonIdx3_Met_Approach2_;
  //
  TH1 * hm_LeptonIdx1_LeptonIdx2_Approach2_;
  TH1 * hm_LeptonIdx2_LeptonIdx3_Approach2_;
  TH1 * hm_LeptonIdx1_LeptonIdx3_Approach2_;
  //
  TH1 * hdPhi_LeptonIdx1_LeptonIdx2_Approach2_;
  TH1 * hdPhi_LeptonIdx2_LeptonIdx3_Approach2_;
  TH1 * hdPhi_LeptonIdx1_LeptonIdx3_Approach2_;
  //
  TH1 * hdEta_LeptonIdx1_LeptonIdx2_Approach2_;
  TH1 * hdEta_LeptonIdx2_LeptonIdx3_Approach2_;
  TH1 * hdEta_LeptonIdx1_LeptonIdx3_Approach2_;
  //
  TH1 * hdr_LeptonIdx1_LeptonIdx2_Approach2_;
  TH1 * hdr_LeptonIdx2_LeptonIdx3_Approach2_;
  TH1 * hdr_LeptonIdx1_LeptonIdx3_Approach2_;
  //
  TH1 * hm_LeptonIdx3_Jet1_Approach2_;
  TH1 * hdr_LeptonIdx3_Jet1_Approach2_;
  //
  TH1 * hm_LeptonIdx3_JetNear_Approach2_;
  TH1 * hdr_LeptonIdx3_JetNear_Approach2_;
  //
  TH1 * hdr_LeptonIdx3_2j_Approach2_;
  TH1 * hdr_LeptonIdx3_2j_inclusive1j_Approach2_;
  //
  TH1 *hdr_LeptonIdx3_AK4jNear_Approach2_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_Approach2_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach2_;
  TH1 *hm_LeptonIdx3_2AK4jNear_Approach2_;
  TH1 *hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach2_;
  TH1 *hdr_2AK4J_NearestToLeptonIdx3_Approach2_;
  //
  TH1 *hdr_LeptonIdx3_AK8_Approach2_;
  TH1 *hm_LeptonIdx3_AK8_Approach2_;
  //
  TH1 * hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2_;
  //
  TH1 *hdPhi_LeptonIdx3_Met_Approach2_;
  //
  //
  TH1 * hmT_LeptonIdx1_Met_Approach3_;
  TH1 * hmT_LeptonIdx2_Met_Approach3_;
  TH1 * hmT_LeptonIdx3_Met_Approach3_;
  //
  TH1 * hm_LeptonIdx1_LeptonIdx2_Approach3_;
  TH1 * hm_LeptonIdx2_LeptonIdx3_Approach3_;
  TH1 * hm_LeptonIdx1_LeptonIdx3_Approach3_;
  //
  TH1 * hdPhi_LeptonIdx1_LeptonIdx2_Approach3_;
  TH1 * hdPhi_LeptonIdx2_LeptonIdx3_Approach3_;
  TH1 * hdPhi_LeptonIdx1_LeptonIdx3_Approach3_;
  //
  TH1 * hdEta_LeptonIdx1_LeptonIdx2_Approach3_;
  TH1 * hdEta_LeptonIdx2_LeptonIdx3_Approach3_;
  TH1 * hdEta_LeptonIdx1_LeptonIdx3_Approach3_;
  //
  TH1 * hdr_LeptonIdx1_LeptonIdx2_Approach3_;
  TH1 * hdr_LeptonIdx2_LeptonIdx3_Approach3_;
  TH1 * hdr_LeptonIdx1_LeptonIdx3_Approach3_;
  //
  TH1 * hm_LeptonIdx3_Jet1_Approach3_;
  TH1 * hdr_LeptonIdx3_Jet1_Approach3_;
  //
  TH1 * hm_LeptonIdx3_JetNear_Approach3_;
  TH1 * hdr_LeptonIdx3_JetNear_Approach3_;
  //
  TH1 * hdr_LeptonIdx3_2j_Approach3_;
  TH1 * hdr_LeptonIdx3_2j_inclusive1j_Approach3_;
  //
  TH1 *hdr_LeptonIdx3_AK4jNear_Approach3_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_Approach3_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach3_;
  TH1 *hm_LeptonIdx3_2AK4jNear_Approach3_;
  TH1 *hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach3_;
  TH1 *hdr_2AK4J_NearestToLeptonIdx3_Approach3_;
  //
  TH1 *hdr_LeptonIdx3_AK8_Approach3_;
  TH1 *hm_LeptonIdx3_AK8_Approach3_;
  //
  TH1 * hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3_;
  //
  TH1 *hdPhi_LeptonIdx3_Met_Approach3_;
  //
  //
  //
  TH1 * hdPhi_2lSFOS_one2lSFOSEvt_;
  TH1 * hdR_2lSFOS_one2lSFOSEvt_;
  TH1 * hm_2lSFOS_one2lSFOSEvt_;
  TH1 * hmT_LeptonNonSFOS_Met_one2lSFOSEvt_;
  TH1 * hdPhi_LeptonNonSFOS_Met_one2lSFOSEvt_;
  //
  //
  TH1 * heventCategory_;
  //
  //TH1 * hmvaOutput_xgb_hh_3l_SUMBk_HH_;
  //  
  TH1 * hEventCounter_;
  //------------------------------------------------------------------------------------



  TH1 * hnumElectrons_zero2lSFOSEvt_;
  TH1 * hnumMuons_zero2lSFOSEvt_;
  TH1 * hnJetAK4_zero2lSFOSEvt_;
  TH1 * hnBJetLoose_zero2lSFOSEvt_;
  TH1 * hnJetAK8_wSelectorAK8_Wjj_zero2lSFOSEvt_;
  //
  TH1 * hsumLeptonCharge_3l_zero2lSFOSEvt_;
  TH1 * hnumSameFlavor_OS_Full_zero2lSFOSEvt_;  
  TH1 * hnumSameFlavor_OS_3l_zero2lSFOSEvt_;
  //
  TH1 * hlep1_pt_zero2lSFOSEvt_;
  TH1 * hlep1_conePt_zero2lSFOSEvt_;
  TH1 * hlep1_eta_zero2lSFOSEvt_;
  TH1 * hmindr_lep1_jet_zero2lSFOSEvt_;
  TH1 * hmT_MEtLep1_zero2lSFOSEvt_;
  //
  TH1 * hlep2_pt_zero2lSFOSEvt_;
  TH1 * hlep2_conePt_zero2lSFOSEvt_;
  TH1 * hlep2_eta_zero2lSFOSEvt_;
  TH1 * hmindr_lep2_jet_zero2lSFOSEvt_;
  TH1 * hmT_MEtLep2_zero2lSFOSEvt_;
  //
  TH1 * hlep3_pt_zero2lSFOSEvt_;
  TH1 * hlep3_conePt_zero2lSFOSEvt_;
  TH1 * hlep3_eta_zero2lSFOSEvt_;
  TH1 * hmindr_lep3_jet_zero2lSFOSEvt_;
  TH1 * hmT_MEtLep3_zero2lSFOSEvt_;
  //
  TH1 * hjet1_pt_zero2lSFOSEvt_;
  TH1 * hjet1_eta_zero2lSFOSEvt_;
  TH1 * hjet2_pt_zero2lSFOSEvt_;
  TH1 * hjet2_eta_zero2lSFOSEvt_;
  TH1 * hjet1plus2_pt_zero2lSFOSEvt_;
  TH1 * hjet1plus2_eta_zero2lSFOSEvt_;
  TH1 * hjet1_m_zero2lSFOSEvt_;
  TH1 * hjet2_m_zero2lSFOSEvt_;
  //
  TH1 * hmet_zero2lSFOSEvt_;
  TH1 * hmht_zero2lSFOSEvt_;
  TH1 * hmet_LD_zero2lSFOSEvt_;
  TH1 * hHT_zero2lSFOSEvt_;
  TH1 * hSTMET_zero2lSFOSEvt_;
  //
  TH1 * hmSFOS2l_closestToZ_zero2lSFOSEvt_;
  TH1 * hm3l_zero2lSFOSEvt_;
  TH1 * hWTojjMass_zero2lSFOSEvt_;
  TH1 * hdihiggsVisMass_sel_zero2lSFOSEvt_;
  TH1 * hdihiggsVisMass_sel_inclusive1j_zero2lSFOSEvt_;
  TH1 * hdihiggsMass_zero2lSFOSEvt_;
  TH1 * hdihiggsMass_inclusive1j_zero2lSFOSEvt_;
  //
  TH1 * hmTMetLepton1_chargeEqualSumCharge3l_zero2lSFOSEvt_;
  TH1 * hmTMetLepton2_chargeEqualSumCharge3l_zero2lSFOSEvt_;
  //
  TH1 * hdr_l12_zero2lSFOSEvt_;
  TH1 * hdr_l23_zero2lSFOSEvt_;
  TH1 * hdr_l13_zero2lSFOSEvt_;
  TH1 * hdr_lss_zero2lSFOSEvt_;
  TH1 * hdr_los_min_zero2lSFOSEvt_;
  TH1 * hdr_los_max_zero2lSFOSEvt_;
  //
  TH1 * havg_dr_jet_zero2lSFOSEvt_;
  TH1 * hdr_Wjj_zero2lSFOSEvt_;
  //
  TH1 * hdPhi_3l_2j_zero2lSFOSEvt_;
  TH1 * hdPhi_3l_2j_inclusive1j_zero2lSFOSEvt_;
  TH1 * hdEta_3l_2j_zero2lSFOSEvt_;
  TH1 * hdEta_3l_2j_inclusive1j_zero2lSFOSEvt_;
  TH1 * hdR_3l_2j_zero2lSFOSEvt_;
  TH1 * hdR_3l_2j_inclusive1j_zero2lSFOSEvt_;
  //
  TH1 * hdEta_3l_avg2j_zero2lSFOSEvt_;
  TH1 * hdEta_3l_avg2j_inclusive1j_zero2lSFOSEvt_;
  //
  TH1 * hbTag_jet1_zero2lSFOSEvt_;
  TH1 * hbTag_jet2_zero2lSFOSEvt_;
  TH1 * hbTag_sum_jet1And2_zero2lSFOSEvt_;
  TH1 * hbTag_max_jet1or2_zero2lSFOSEvt_;
  TH1 * hbTag_max_AK4_zero2lSFOSEvt_;
  TH1 * hbTag_sum_AK4_zero2lSFOSEvt_;
  //
  TH1 * hpt_lastAK4_zero2lSFOSEvt_;
  //
  TH1 *hm_AK8_zero2lSFOSEvt_;
  //
  //
  TH1 * hmT_LeptonIdx1_Met_Approach0_zero2lSFOSEvt_;
  TH1 * hmT_LeptonIdx2_Met_Approach0_zero2lSFOSEvt_;
  TH1 * hmT_LeptonIdx3_Met_Approach0_zero2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx1_LeptonIdx2_Approach0_zero2lSFOSEvt_;
  TH1 * hm_LeptonIdx2_LeptonIdx3_Approach0_zero2lSFOSEvt_;
  TH1 * hm_LeptonIdx1_LeptonIdx3_Approach0_zero2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx1_LeptonIdx2_Approach0_zero2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx2_LeptonIdx3_Approach0_zero2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx1_LeptonIdx3_Approach0_zero2lSFOSEvt_;
  //
  TH1 * hdEta_LeptonIdx1_LeptonIdx2_Approach0_zero2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx2_LeptonIdx3_Approach0_zero2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx1_LeptonIdx3_Approach0_zero2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx1_LeptonIdx2_Approach0_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx2_LeptonIdx3_Approach0_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx1_LeptonIdx3_Approach0_zero2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_Jet1_Approach0_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_Jet1_Approach0_zero2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_JetNear_Approach0_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_JetNear_Approach0_zero2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx3_2j_Approach0_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_2j_inclusive1j_Approach0_zero2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK4jNear_Approach0_zero2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_Approach0_zero2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach0_zero2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_Approach0_zero2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach0_zero2lSFOSEvt_;
  TH1 *hdr_2AK4J_NearestToLeptonIdx3_Approach0_zero2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK8_Approach0_zero2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_AK8_Approach0_zero2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0_zero2lSFOSEvt_;
  //
  TH1 *hdPhi_LeptonIdx3_Met_Approach0_zero2lSFOSEvt_;
  //
  //
  TH1 * hmT_LeptonIdx1_Met_Approach2_zero2lSFOSEvt_;
  TH1 * hmT_LeptonIdx2_Met_Approach2_zero2lSFOSEvt_;
  TH1 * hmT_LeptonIdx3_Met_Approach2_zero2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx1_LeptonIdx2_Approach2_zero2lSFOSEvt_;
  TH1 * hm_LeptonIdx2_LeptonIdx3_Approach2_zero2lSFOSEvt_;
  TH1 * hm_LeptonIdx1_LeptonIdx3_Approach2_zero2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx1_LeptonIdx2_Approach2_zero2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx2_LeptonIdx3_Approach2_zero2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx1_LeptonIdx3_Approach2_zero2lSFOSEvt_;
  //
  TH1 * hdEta_LeptonIdx1_LeptonIdx2_Approach2_zero2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx2_LeptonIdx3_Approach2_zero2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx1_LeptonIdx3_Approach2_zero2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx1_LeptonIdx2_Approach2_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx2_LeptonIdx3_Approach2_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx1_LeptonIdx3_Approach2_zero2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_Jet1_Approach2_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_Jet1_Approach2_zero2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_JetNear_Approach2_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_JetNear_Approach2_zero2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx3_2j_Approach2_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_2j_inclusive1j_Approach2_zero2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK4jNear_Approach2_zero2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_Approach2_zero2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach2_zero2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_Approach2_zero2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach2_zero2lSFOSEvt_;
  TH1 *hdr_2AK4J_NearestToLeptonIdx3_Approach2_zero2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK8_Approach2_zero2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_AK8_Approach2_zero2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2_zero2lSFOSEvt_;
  //
  TH1 *hdPhi_LeptonIdx3_Met_Approach2_zero2lSFOSEvt_;
  //
  //
  TH1 * hmT_LeptonIdx1_Met_Approach3_zero2lSFOSEvt_;
  TH1 * hmT_LeptonIdx2_Met_Approach3_zero2lSFOSEvt_;
  TH1 * hmT_LeptonIdx3_Met_Approach3_zero2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx1_LeptonIdx2_Approach3_zero2lSFOSEvt_;
  TH1 * hm_LeptonIdx2_LeptonIdx3_Approach3_zero2lSFOSEvt_;
  TH1 * hm_LeptonIdx1_LeptonIdx3_Approach3_zero2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx1_LeptonIdx2_Approach3_zero2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx2_LeptonIdx3_Approach3_zero2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx1_LeptonIdx3_Approach3_zero2lSFOSEvt_;
  //
  TH1 * hdEta_LeptonIdx1_LeptonIdx2_Approach3_zero2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx2_LeptonIdx3_Approach3_zero2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx1_LeptonIdx3_Approach3_zero2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx1_LeptonIdx2_Approach3_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx2_LeptonIdx3_Approach3_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx1_LeptonIdx3_Approach3_zero2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_Jet1_Approach3_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_Jet1_Approach3_zero2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_JetNear_Approach3_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_JetNear_Approach3_zero2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx3_2j_Approach3_zero2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_2j_inclusive1j_Approach3_zero2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK4jNear_Approach3_zero2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_Approach3_zero2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach3_zero2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_Approach3_zero2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach3_zero2lSFOSEvt_;
  TH1 *hdr_2AK4J_NearestToLeptonIdx3_Approach3_zero2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK8_Approach3_zero2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_AK8_Approach3_zero2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3_zero2lSFOSEvt_;
  //
  TH1 *hdPhi_LeptonIdx3_Met_Approach3_zero2lSFOSEvt_;
  //------------------------------------------------------------------------------------ 


   TH1 * hnumElectrons_one2lSFOSEvt_;
  TH1 * hnumMuons_one2lSFOSEvt_;
  TH1 * hnJetAK4_one2lSFOSEvt_;
  TH1 * hnBJetLoose_one2lSFOSEvt_;
  TH1 * hnJetAK8_wSelectorAK8_Wjj_one2lSFOSEvt_;
  //
  TH1 * hsumLeptonCharge_3l_one2lSFOSEvt_;
  TH1 * hnumSameFlavor_OS_Full_one2lSFOSEvt_;  
  TH1 * hnumSameFlavor_OS_3l_one2lSFOSEvt_;
  //
  TH1 * hlep1_pt_one2lSFOSEvt_;
  TH1 * hlep1_conePt_one2lSFOSEvt_;
  TH1 * hlep1_eta_one2lSFOSEvt_;
  TH1 * hmindr_lep1_jet_one2lSFOSEvt_;
  TH1 * hmT_MEtLep1_one2lSFOSEvt_;
  //
  TH1 * hlep2_pt_one2lSFOSEvt_;
  TH1 * hlep2_conePt_one2lSFOSEvt_;
  TH1 * hlep2_eta_one2lSFOSEvt_;
  TH1 * hmindr_lep2_jet_one2lSFOSEvt_;
  TH1 * hmT_MEtLep2_one2lSFOSEvt_;
  //
  TH1 * hlep3_pt_one2lSFOSEvt_;
  TH1 * hlep3_conePt_one2lSFOSEvt_;
  TH1 * hlep3_eta_one2lSFOSEvt_;
  TH1 * hmindr_lep3_jet_one2lSFOSEvt_;
  TH1 * hmT_MEtLep3_one2lSFOSEvt_;
  //
  TH1 * hjet1_pt_one2lSFOSEvt_;
  TH1 * hjet1_eta_one2lSFOSEvt_;
  TH1 * hjet2_pt_one2lSFOSEvt_;
  TH1 * hjet2_eta_one2lSFOSEvt_;
  TH1 * hjet1plus2_pt_one2lSFOSEvt_;
  TH1 * hjet1plus2_eta_one2lSFOSEvt_;
  TH1 * hjet1_m_one2lSFOSEvt_;
  TH1 * hjet2_m_one2lSFOSEvt_;
  //
  TH1 * hmet_one2lSFOSEvt_;
  TH1 * hmht_one2lSFOSEvt_;
  TH1 * hmet_LD_one2lSFOSEvt_;
  TH1 * hHT_one2lSFOSEvt_;
  TH1 * hSTMET_one2lSFOSEvt_;
  //
  TH1 * hmSFOS2l_closestToZ_one2lSFOSEvt_;
  TH1 * hm3l_one2lSFOSEvt_;
  TH1 * hWTojjMass_one2lSFOSEvt_;
  TH1 * hdihiggsVisMass_sel_one2lSFOSEvt_;
  TH1 * hdihiggsVisMass_sel_inclusive1j_one2lSFOSEvt_;
  TH1 * hdihiggsMass_one2lSFOSEvt_;
  TH1 * hdihiggsMass_inclusive1j_one2lSFOSEvt_;
  //
  TH1 * hmTMetLepton1_chargeEqualSumCharge3l_one2lSFOSEvt_;
  TH1 * hmTMetLepton2_chargeEqualSumCharge3l_one2lSFOSEvt_;
  //
  TH1 * hdr_l12_one2lSFOSEvt_;
  TH1 * hdr_l23_one2lSFOSEvt_;
  TH1 * hdr_l13_one2lSFOSEvt_;
  TH1 * hdr_lss_one2lSFOSEvt_;
  TH1 * hdr_los_min_one2lSFOSEvt_;
  TH1 * hdr_los_max_one2lSFOSEvt_;
  //
  TH1 * havg_dr_jet_one2lSFOSEvt_;
  TH1 * hdr_Wjj_one2lSFOSEvt_;
  //
  TH1 * hdPhi_3l_2j_one2lSFOSEvt_;
  TH1 * hdPhi_3l_2j_inclusive1j_one2lSFOSEvt_;
  TH1 * hdEta_3l_2j_one2lSFOSEvt_;
  TH1 * hdEta_3l_2j_inclusive1j_one2lSFOSEvt_;
  TH1 * hdR_3l_2j_one2lSFOSEvt_;
  TH1 * hdR_3l_2j_inclusive1j_one2lSFOSEvt_;
  //
  TH1 * hdEta_3l_avg2j_one2lSFOSEvt_;
  TH1 * hdEta_3l_avg2j_inclusive1j_one2lSFOSEvt_;
  //
  TH1 * hbTag_jet1_one2lSFOSEvt_;
  TH1 * hbTag_jet2_one2lSFOSEvt_;
  TH1 * hbTag_sum_jet1And2_one2lSFOSEvt_;
  TH1 * hbTag_max_jet1or2_one2lSFOSEvt_;
  TH1 * hbTag_max_AK4_one2lSFOSEvt_;
  TH1 * hbTag_sum_AK4_one2lSFOSEvt_;
  //
  TH1 * hpt_lastAK4_one2lSFOSEvt_;
  //
  TH1 *hm_AK8_one2lSFOSEvt_;
  //
  //
  TH1 * hmT_LeptonIdx1_Met_Approach0_one2lSFOSEvt_;
  TH1 * hmT_LeptonIdx2_Met_Approach0_one2lSFOSEvt_;
  TH1 * hmT_LeptonIdx3_Met_Approach0_one2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx1_LeptonIdx2_Approach0_one2lSFOSEvt_;
  TH1 * hm_LeptonIdx2_LeptonIdx3_Approach0_one2lSFOSEvt_;
  TH1 * hm_LeptonIdx1_LeptonIdx3_Approach0_one2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx1_LeptonIdx2_Approach0_one2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx2_LeptonIdx3_Approach0_one2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx1_LeptonIdx3_Approach0_one2lSFOSEvt_;
  //
  TH1 * hdEta_LeptonIdx1_LeptonIdx2_Approach0_one2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx2_LeptonIdx3_Approach0_one2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx1_LeptonIdx3_Approach0_one2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx1_LeptonIdx2_Approach0_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx2_LeptonIdx3_Approach0_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx1_LeptonIdx3_Approach0_one2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_Jet1_Approach0_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_Jet1_Approach0_one2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_JetNear_Approach0_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_JetNear_Approach0_one2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx3_2j_Approach0_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_2j_inclusive1j_Approach0_one2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK4jNear_Approach0_one2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_Approach0_one2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach0_one2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_Approach0_one2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach0_one2lSFOSEvt_;
  TH1 *hdr_2AK4J_NearestToLeptonIdx3_Approach0_one2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK8_Approach0_one2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_AK8_Approach0_one2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0_one2lSFOSEvt_;
  //
  TH1 *hdPhi_LeptonIdx3_Met_Approach0_one2lSFOSEvt_;
  //
  //
  TH1 * hmT_LeptonIdx1_Met_Approach2_one2lSFOSEvt_;
  TH1 * hmT_LeptonIdx2_Met_Approach2_one2lSFOSEvt_;
  TH1 * hmT_LeptonIdx3_Met_Approach2_one2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx1_LeptonIdx2_Approach2_one2lSFOSEvt_;
  TH1 * hm_LeptonIdx2_LeptonIdx3_Approach2_one2lSFOSEvt_;
  TH1 * hm_LeptonIdx1_LeptonIdx3_Approach2_one2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx1_LeptonIdx2_Approach2_one2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx2_LeptonIdx3_Approach2_one2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx1_LeptonIdx3_Approach2_one2lSFOSEvt_;
  //
  TH1 * hdEta_LeptonIdx1_LeptonIdx2_Approach2_one2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx2_LeptonIdx3_Approach2_one2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx1_LeptonIdx3_Approach2_one2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx1_LeptonIdx2_Approach2_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx2_LeptonIdx3_Approach2_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx1_LeptonIdx3_Approach2_one2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_Jet1_Approach2_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_Jet1_Approach2_one2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_JetNear_Approach2_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_JetNear_Approach2_one2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx3_2j_Approach2_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_2j_inclusive1j_Approach2_one2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK4jNear_Approach2_one2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_Approach2_one2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach2_one2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_Approach2_one2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach2_one2lSFOSEvt_;
  TH1 *hdr_2AK4J_NearestToLeptonIdx3_Approach2_one2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK8_Approach2_one2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_AK8_Approach2_one2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2_one2lSFOSEvt_;
  //
  TH1 *hdPhi_LeptonIdx3_Met_Approach2_one2lSFOSEvt_;
  //
  //
  TH1 * hmT_LeptonIdx1_Met_Approach3_one2lSFOSEvt_;
  TH1 * hmT_LeptonIdx2_Met_Approach3_one2lSFOSEvt_;
  TH1 * hmT_LeptonIdx3_Met_Approach3_one2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx1_LeptonIdx2_Approach3_one2lSFOSEvt_;
  TH1 * hm_LeptonIdx2_LeptonIdx3_Approach3_one2lSFOSEvt_;
  TH1 * hm_LeptonIdx1_LeptonIdx3_Approach3_one2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx1_LeptonIdx2_Approach3_one2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx2_LeptonIdx3_Approach3_one2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx1_LeptonIdx3_Approach3_one2lSFOSEvt_;
  //
  TH1 * hdEta_LeptonIdx1_LeptonIdx2_Approach3_one2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx2_LeptonIdx3_Approach3_one2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx1_LeptonIdx3_Approach3_one2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx1_LeptonIdx2_Approach3_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx2_LeptonIdx3_Approach3_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx1_LeptonIdx3_Approach3_one2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_Jet1_Approach3_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_Jet1_Approach3_one2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_JetNear_Approach3_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_JetNear_Approach3_one2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx3_2j_Approach3_one2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_2j_inclusive1j_Approach3_one2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK4jNear_Approach3_one2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_Approach3_one2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach3_one2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_Approach3_one2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach3_one2lSFOSEvt_;
  TH1 *hdr_2AK4J_NearestToLeptonIdx3_Approach3_one2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK8_Approach3_one2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_AK8_Approach3_one2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3_one2lSFOSEvt_;
  //
  TH1 *hdPhi_LeptonIdx3_Met_Approach3_one2lSFOSEvt_;
  //------------------------------------------------------------------------------------


  TH1 * hnumElectrons_two2lSFOSEvt_;
  TH1 * hnumMuons_two2lSFOSEvt_;
  TH1 * hnJetAK4_two2lSFOSEvt_;
  TH1 * hnBJetLoose_two2lSFOSEvt_;
  TH1 * hnJetAK8_wSelectorAK8_Wjj_two2lSFOSEvt_;
  //
  TH1 * hsumLeptonCharge_3l_two2lSFOSEvt_;
  TH1 * hnumSameFlavor_OS_Full_two2lSFOSEvt_;  
  TH1 * hnumSameFlavor_OS_3l_two2lSFOSEvt_;
  //
  TH1 * hlep1_pt_two2lSFOSEvt_;
  TH1 * hlep1_conePt_two2lSFOSEvt_;
  TH1 * hlep1_eta_two2lSFOSEvt_;
  TH1 * hmindr_lep1_jet_two2lSFOSEvt_;
  TH1 * hmT_MEtLep1_two2lSFOSEvt_;
  //
  TH1 * hlep2_pt_two2lSFOSEvt_;
  TH1 * hlep2_conePt_two2lSFOSEvt_;
  TH1 * hlep2_eta_two2lSFOSEvt_;
  TH1 * hmindr_lep2_jet_two2lSFOSEvt_;
  TH1 * hmT_MEtLep2_two2lSFOSEvt_;
  //
  TH1 * hlep3_pt_two2lSFOSEvt_;
  TH1 * hlep3_conePt_two2lSFOSEvt_;
  TH1 * hlep3_eta_two2lSFOSEvt_;
  TH1 * hmindr_lep3_jet_two2lSFOSEvt_;
  TH1 * hmT_MEtLep3_two2lSFOSEvt_;
  //
  TH1 * hjet1_pt_two2lSFOSEvt_;
  TH1 * hjet1_eta_two2lSFOSEvt_;
  TH1 * hjet2_pt_two2lSFOSEvt_;
  TH1 * hjet2_eta_two2lSFOSEvt_;
  TH1 * hjet1plus2_pt_two2lSFOSEvt_;
  TH1 * hjet1plus2_eta_two2lSFOSEvt_;
  TH1 * hjet1_m_two2lSFOSEvt_;
  TH1 * hjet2_m_two2lSFOSEvt_;
  //
  TH1 * hmet_two2lSFOSEvt_;
  TH1 * hmht_two2lSFOSEvt_;
  TH1 * hmet_LD_two2lSFOSEvt_;
  TH1 * hHT_two2lSFOSEvt_;
  TH1 * hSTMET_two2lSFOSEvt_;
  //
  TH1 * hmSFOS2l_closestToZ_two2lSFOSEvt_;
  TH1 * hm3l_two2lSFOSEvt_;
  TH1 * hWTojjMass_two2lSFOSEvt_;
  TH1 * hdihiggsVisMass_sel_two2lSFOSEvt_;
  TH1 * hdihiggsVisMass_sel_inclusive1j_two2lSFOSEvt_;
  TH1 * hdihiggsMass_two2lSFOSEvt_;
  TH1 * hdihiggsMass_inclusive1j_two2lSFOSEvt_;
  //
  TH1 * hmTMetLepton1_chargeEqualSumCharge3l_two2lSFOSEvt_;
  TH1 * hmTMetLepton2_chargeEqualSumCharge3l_two2lSFOSEvt_;
  //
  TH1 * hdr_l12_two2lSFOSEvt_;
  TH1 * hdr_l23_two2lSFOSEvt_;
  TH1 * hdr_l13_two2lSFOSEvt_;
  TH1 * hdr_lss_two2lSFOSEvt_;
  TH1 * hdr_los_min_two2lSFOSEvt_;
  TH1 * hdr_los_max_two2lSFOSEvt_;
  //
  TH1 * havg_dr_jet_two2lSFOSEvt_;
  TH1 * hdr_Wjj_two2lSFOSEvt_;
  //
  TH1 * hdPhi_3l_2j_two2lSFOSEvt_;
  TH1 * hdPhi_3l_2j_inclusive1j_two2lSFOSEvt_;
  TH1 * hdEta_3l_2j_two2lSFOSEvt_;
  TH1 * hdEta_3l_2j_inclusive1j_two2lSFOSEvt_;
  TH1 * hdR_3l_2j_two2lSFOSEvt_;
  TH1 * hdR_3l_2j_inclusive1j_two2lSFOSEvt_;
  //
  TH1 * hdEta_3l_avg2j_two2lSFOSEvt_;
  TH1 * hdEta_3l_avg2j_inclusive1j_two2lSFOSEvt_;
  //
  TH1 * hbTag_jet1_two2lSFOSEvt_;
  TH1 * hbTag_jet2_two2lSFOSEvt_;
  TH1 * hbTag_sum_jet1And2_two2lSFOSEvt_;
  TH1 * hbTag_max_jet1or2_two2lSFOSEvt_;
  TH1 * hbTag_max_AK4_two2lSFOSEvt_;
  TH1 * hbTag_sum_AK4_two2lSFOSEvt_;
  //
  TH1 * hpt_lastAK4_two2lSFOSEvt_;
  //
  TH1 *hm_AK8_two2lSFOSEvt_;
  //
  //
  TH1 * hmT_LeptonIdx1_Met_Approach0_two2lSFOSEvt_;
  TH1 * hmT_LeptonIdx2_Met_Approach0_two2lSFOSEvt_;
  TH1 * hmT_LeptonIdx3_Met_Approach0_two2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx1_LeptonIdx2_Approach0_two2lSFOSEvt_;
  TH1 * hm_LeptonIdx2_LeptonIdx3_Approach0_two2lSFOSEvt_;
  TH1 * hm_LeptonIdx1_LeptonIdx3_Approach0_two2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx1_LeptonIdx2_Approach0_two2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx2_LeptonIdx3_Approach0_two2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx1_LeptonIdx3_Approach0_two2lSFOSEvt_;
  //
  TH1 * hdEta_LeptonIdx1_LeptonIdx2_Approach0_two2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx2_LeptonIdx3_Approach0_two2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx1_LeptonIdx3_Approach0_two2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx1_LeptonIdx2_Approach0_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx2_LeptonIdx3_Approach0_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx1_LeptonIdx3_Approach0_two2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_Jet1_Approach0_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_Jet1_Approach0_two2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_JetNear_Approach0_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_JetNear_Approach0_two2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx3_2j_Approach0_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_2j_inclusive1j_Approach0_two2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK4jNear_Approach0_two2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_Approach0_two2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach0_two2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_Approach0_two2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach0_two2lSFOSEvt_;
  TH1 *hdr_2AK4J_NearestToLeptonIdx3_Approach0_two2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK8_Approach0_two2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_AK8_Approach0_two2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach0_two2lSFOSEvt_;
  //
  TH1 *hdPhi_LeptonIdx3_Met_Approach0_two2lSFOSEvt_;
  //
  //
  TH1 * hmT_LeptonIdx1_Met_Approach2_two2lSFOSEvt_;
  TH1 * hmT_LeptonIdx2_Met_Approach2_two2lSFOSEvt_;
  TH1 * hmT_LeptonIdx3_Met_Approach2_two2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx1_LeptonIdx2_Approach2_two2lSFOSEvt_;
  TH1 * hm_LeptonIdx2_LeptonIdx3_Approach2_two2lSFOSEvt_;
  TH1 * hm_LeptonIdx1_LeptonIdx3_Approach2_two2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx1_LeptonIdx2_Approach2_two2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx2_LeptonIdx3_Approach2_two2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx1_LeptonIdx3_Approach2_two2lSFOSEvt_;
  //
  TH1 * hdEta_LeptonIdx1_LeptonIdx2_Approach2_two2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx2_LeptonIdx3_Approach2_two2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx1_LeptonIdx3_Approach2_two2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx1_LeptonIdx2_Approach2_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx2_LeptonIdx3_Approach2_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx1_LeptonIdx3_Approach2_two2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_Jet1_Approach2_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_Jet1_Approach2_two2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_JetNear_Approach2_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_JetNear_Approach2_two2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx3_2j_Approach2_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_2j_inclusive1j_Approach2_two2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK4jNear_Approach2_two2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_Approach2_two2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach2_two2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_Approach2_two2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach2_two2lSFOSEvt_;
  TH1 *hdr_2AK4J_NearestToLeptonIdx3_Approach2_two2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK8_Approach2_two2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_AK8_Approach2_two2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach2_two2lSFOSEvt_;
  //
  TH1 *hdPhi_LeptonIdx3_Met_Approach2_two2lSFOSEvt_;
  //
  //
  TH1 * hmT_LeptonIdx1_Met_Approach3_two2lSFOSEvt_;
  TH1 * hmT_LeptonIdx2_Met_Approach3_two2lSFOSEvt_;
  TH1 * hmT_LeptonIdx3_Met_Approach3_two2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx1_LeptonIdx2_Approach3_two2lSFOSEvt_;
  TH1 * hm_LeptonIdx2_LeptonIdx3_Approach3_two2lSFOSEvt_;
  TH1 * hm_LeptonIdx1_LeptonIdx3_Approach3_two2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx1_LeptonIdx2_Approach3_two2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx2_LeptonIdx3_Approach3_two2lSFOSEvt_;
  TH1 * hdPhi_LeptonIdx1_LeptonIdx3_Approach3_two2lSFOSEvt_;
  //
  TH1 * hdEta_LeptonIdx1_LeptonIdx2_Approach3_two2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx2_LeptonIdx3_Approach3_two2lSFOSEvt_;
  TH1 * hdEta_LeptonIdx1_LeptonIdx3_Approach3_two2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx1_LeptonIdx2_Approach3_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx2_LeptonIdx3_Approach3_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx1_LeptonIdx3_Approach3_two2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_Jet1_Approach3_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_Jet1_Approach3_two2lSFOSEvt_;
  //
  TH1 * hm_LeptonIdx3_JetNear_Approach3_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_JetNear_Approach3_two2lSFOSEvt_;
  //
  TH1 * hdr_LeptonIdx3_2j_Approach3_two2lSFOSEvt_;
  TH1 * hdr_LeptonIdx3_2j_inclusive1j_Approach3_two2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK4jNear_Approach3_two2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_Approach3_two2lSFOSEvt_;
  TH1 *hdr_LeptonIdx3_2AK4jNear_inclusive1j_Approach3_two2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_Approach3_two2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_2AK4jNear_inclusive1j_Approach3_two2lSFOSEvt_;
  TH1 *hdr_2AK4J_NearestToLeptonIdx3_Approach3_two2lSFOSEvt_;
  //
  TH1 *hdr_LeptonIdx3_AK8_Approach3_two2lSFOSEvt_;
  TH1 *hm_LeptonIdx3_AK8_Approach3_two2lSFOSEvt_;
  //
  TH1 * hdPhi_LeptonIdx3plusMet_LeptonIdx1plus2_Approach3_two2lSFOSEvt_;
  //
  TH1 *hdPhi_LeptonIdx3_Met_Approach3_two2lSFOSEvt_;
  //------------------------------------------------------------------------------------

  //
  //
  //
  // WZctrl
  TH1 * hmT_WZctrl_leptonW_MET_;
  // WZctrl 2lss
  TH1 * hjetMass_sel_WZctrl_2lss_;
  TH1 * hleptonPairMass_sel_WZctrl_2lss_;
  TH1 * hmindr_lep1_jet_WZctrl_2lss_;
  TH1 * hmT_lep1_WZctrl_2lss_;
  TH1 * hmindr_lep2_jet_WZctrl_2lss_;
  TH1 * hmT_lep2_WZctrl_2lss_;
  TH1 * hdR_ll_WZctrl_2lss_;
  TH1 * hmax_lep_eta_WZctrl_2lss_;    
  //
  //
  //  
  
};

#endif
