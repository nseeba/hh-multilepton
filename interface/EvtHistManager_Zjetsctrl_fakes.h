#ifndef hhAnalysis_multilepton_EvtHistManager_Zjetsctrl_fakes_h
#define hhAnalysis_multilepton_EvtHistManager_Zjetsctrl_fakes_h

/** \class EvtHistManager_Zjetsctrl_fakes
 *
 * Book and fill histograms for event-level quantities in ttH multilepton analysis
 * in 3l category
 *
 * \author Christian Veelken, Tallin
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

class EvtHistManager_Zjetsctrl_fakes
  : public HistManagerBase
{
 public:
  EvtHistManager_Zjetsctrl_fakes(const edm::ParameterSet & cfg);
  ~EvtHistManager_Zjetsctrl_fakes() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
    fillHistograms(
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
		   double mvaOutput_xgb_Zjetsctrl_fakes_SUMBk_HH,
		   double evtWeight);

  
  const TH1 *
  getHistogram_EventCounter() const;

 private:
  TH1 * hnumElectrons_;
  TH1 * hnumMuons_;
  TH1 * hnumLeptons_;
  TH1 * hsumLeptonCharge_3l_;
  TH1 * hsumLeptonCharge_FullSel_;
  TH1 * hnumSameFlavor_OS_3l_;
  TH1 * hnumSameFlavor_OS_FullPresel_;
  TH1 * hnJetAK4_;
  TH1 * hnBJetLoose_;
  TH1 * hnBJetMedium_;
  TH1 * hnJetAK8_;
  TH1 * hnJetAK8_wSelectorAK8_Wjj_;
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
  TH1 * hjet2_pt_;
  TH1 * hjet1plus2pt_;
  TH1 * hjet1_m_;
  TH1 * hjet2_m_;
  //
  TH1 * havg_dr_jet_;
  TH1 * hdr_Wjj_;
  //
  TH1 * hdr_l12_;
  TH1 * hdr_l23_;
  TH1 * hdr_l13_;
  TH1 * hdr_lss_;
  TH1 * hdr_los_min_;
  TH1 * hdr_los_max_;
  //
  TH1 * hdr_WjjLepIdx3_;
  TH1 * hdr_Wjet1LepIdx3_;
  TH1 * hdr_Wjet2LepIdx3_;
  TH1 * hdr_LepIdx3WjetNear_;
  TH1 * hdr_LepIdx3WjetFar_;
  //
  TH1 * hmet_;
  TH1 * hmht_;
  TH1 * hmet_LD_;
  TH1 * hHT_;
  TH1 * hSTMET_;
  //
  TH1 * hmSFOS2l_;
  TH1 * hWTojjMass_;
  TH1 * hdihiggsVisMass_sel_;
  TH1 * hdihiggsMass_;
  TH1 * hmTMetLepton1_;
  TH1 * hmTMetLepton2_;
  //
  TH1 * hlep1_isTight_;
  TH1 * hlep2_isTight_;
  TH1 * hlep3_isTight_;
  //
  TH1 * hlep1_genLepPt_;
  TH1 * hlep2_genLepPt_;
  TH1 * hlep3_genLepPt_;
  TH1 * hlep1_frWeight_;
  TH1 * hlep2_frWeight_;
  TH1 * hlep3_frWeight_;
  TH1 * hlep1_fake_prob_;
  TH1 * hlep2_fake_prob_;
  TH1 * hlep3_fake_prob_;
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
  TH1 * heventCategory_;
  //
  TH1 * hmvaOutput_xgb_Zjetsctrl_fakes_SUMBk_HH_;
  //  
  TH1 * hEventCounter_;
};

#endif
