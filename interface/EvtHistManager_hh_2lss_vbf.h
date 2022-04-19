#ifndef hhAnalysis_multilepton_EvtHistManager_hh_2lss_vbf_h
#define hhAnalysis_multilepton_EvtHistManager_hh_2lss_vbf_h

/** \class EvtHistManager_hh_2lss
 *
 * Book and fill histograms for event-level quantities in the 2lss_vbf category
 * of the HH->wwww, WWtt, and WWWW analysis
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase


class EvtHistManager_hh_2lss_vbf : public HistManagerBase {
public:
  EvtHistManager_hh_2lss_vbf(const edm::ParameterSet &cfg);
  ~EvtHistManager_hh_2lss_vbf() {}

  /// book and fill histograms
  void bookHistograms(TFileDirectory &dir) override;

  void fillHistograms(int numElectrons, int numMuons, int numJets,
                      int numJetsPtGt40, double dihiggsVisMass,
                      double dihiggsMass_wMet, double vbf_m_jj,
                      double vbf_dEta_jj, double vbf_dR_jj, double evtWeight,
                      double mindR_vbfjet_lep1, double mindR_vbfjet_lep2,
                      double maxJetEta_vbf, double minJetEta_vbf,
                      double lhe_dEta_jj, double lhe_dPhi_jj, double lhe_m_jj, double lhe_dR_jj, 
                      double matched_dEta_jj, double matched_dPhi_jj, double matched_m_jj, double matched_dR_jj,
                      double best_dEta_jj, double best_dPhi_jj, double best_m_jj, double best_dR_jj,
                      double lhe_pt_lead, double lhe_pt_sublead, double matched_pt_lead, double matched_pt_sublead, double best_pt_lead, double best_pt_sublead,
                      double genjet_dEta_jj, double genjet_dPhi_jj, double genjet_m_jj, double genjet_dR_jj,
                      double mass_jj_W, double mass_jj_W2, double sum_mass_W,
                      double sum_m_lj, double pT_sum, double m_ll, bool isVBF,
                      double maxJetPt_vbf, double minJetPt_vbf, double mindR_vbfJet_W1, double maxdR_vbfJet_W1, double mindR_vbfjet_lep, double maxdR_vbfjet_lep,
                      double dR_h1h2, double pT_h1, double pT_h2, double dR_h1_j1, double dR_h1_j2, double dR_h2_j1, double dR_h2_j2, double mass_h1, double mass_h2,
                      double dihiggsm, double dihiggsm_wmet
                      );

  const TH1 *getHistogram_EventCounter() const;

private:
  TH1 *histogram_numElectrons_;
  TH1 *histogram_numMuons_;
  TH1 *histogram_numJets_;
  TH1 *histogram_numJetsPtGt40_;
  TH1 *histogram_dihiggsVisMass_;
  TH1 *histogram_dihiggsMass_wMet_;
  TH1 *histogram_vbf_m_jj_;
  TH1 *histogram_vbf_dEta_jj_;
  TH1 *histogram_vbf_dR_jj_;
  TH1 *histogram_EventCounter_;
  TH1 *histogram_mindR_vbfjet_lep1_;
  TH1 *histogram_mindR_vbfjet_lep2_;
  TH1 *histogram_maxJetEta_vbf_;
  TH1 *histogram_minJetEta_vbf_;

  TH1 *histogram_lhe_dEta_jj_;
  TH1 *histogram_lhe_dPhi_jj_;
  TH1 *histogram_lhe_m_jj_;
  TH1 *histogram_lhe_dR_jj_;

  TH1 *histogram_matched_dEta_jj_;
  TH1 *histogram_matched_dPhi_jj_;
  TH1 *histogram_matched_m_jj_;
  TH1 *histogram_matched_dR_jj_;

  TH1 *histogram_best_dEta_jj_;
  TH1 *histogram_best_dPhi_jj_;
  TH1 *histogram_best_m_jj_;
  TH1 *histogram_best_dR_jj_;

  TH1 *histogram_lhe_pt_lead_;
  TH1 *histogram_lhe_pt_sublead_;
  TH1 *histogram_matched_pt_lead_;
  TH1 *histogram_matched_pt_sublead_;
  TH1 *histogram_best_pt_lead_;
  TH1 *histogram_best_pt_sublead_;

  TH1 *histogram_genjet_dEta_jj_;
  TH1 *histogram_genjet_dPhi_jj_;
  TH1 *histogram_genjet_m_jj_;
  TH1 *histogram_genjet_dR_jj_;

  TH1 *histogram_mass_jj_W_;
  TH1 *histogram_mass_jj_W2_;
  TH1 *histogram_sum_mass_W_;

  TH1 *histogram_sum_m_lj_;
  TH1 *histogram_pT_sum_;
  TH1 *histogram_m_ll_;
  TH1 *histogram_isVBF_;

  TH1 *histogram_maxJetPt_vbf_;
  TH1 *histogram_minJetPt_vbf_;
  TH1 *histogram_mindR_vbfJet_W1_;
  TH1 *histogram_maxdR_vbfJet_W1_;
  TH1 *histogram_mindR_vbfjet_lep_;
  TH1 *histogram_maxdR_vbfjet_lep_;

  TH1 *histogram_dR_h1h2_;
  TH1 *histogram_pT_h1_;
  TH1 *histogram_pT_h2_;
  TH1 *histogram_dR_h1_j1_;
  TH1 *histogram_dR_h1_j2_;
  TH1 *histogram_dR_h2_j1_;
  TH1 *histogram_dR_h2_j2_;
  TH1 *histogram_mass_h1_;
  TH1 *histogram_mass_h2_;
  TH1 *histogram_dihiggsm_;
  TH1 *histogram_dihiggsm_wmet_;
};

#endif
