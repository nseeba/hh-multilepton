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
                      double mindr_lep1_jet, double mindr_lep2_jet,
                      double max_jet_eta,
                      double lhe_dEta_jj, double lhe_dPhi_jj, double lhe_m_jj, double lhe_dR_jj, 
                      double matched_dEta_jj, double matched_dPhi_jj, double matched_m_jj, double matched_dR_jj,
                      double best_dEta_jj, double best_dPhi_jj, double best_m_jj, double best_dR_jj,
                      double lhe_pt_lead, double lhe_pt_sublead, double matched_pt_lead, double matched_pt_sublead, double best_pt_lead, double best_pt_sublead,
                      double genjet_dEta_jj, double genjet_dPhi_jj, double genjet_m_jj, double genjet_dR_jj,
                      double mass_jj_W, double mass_jj_W2, double sum_mass_W,
                      double sum_m_lj, double pT_sum, double m_ll, bool isVBF
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
  TH1 *histogram_mindr_lep1_jet_;
  TH1 *histogram_mindr_lep2_jet_;
  TH1 *histogram_max_jet_eta_;

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
};

#endif
