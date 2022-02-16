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
                      double vbf_dEta_jj, double evtWeight
                      , int nJet, int nJet_vbf, int isVBF,
                      double mindr_lep1_jet, double mindr_lep2_jet,
                      double max_jet_eta
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
  TH1 *histogram_EventCounter_;
  TH1 *histogram_nJet_;
  TH1 *histogram_nJet_vbf_;
  TH1 *histogram_isVBF_;
  TH1 *histogram_mindr_lep1_jet_;
  TH1 *histogram_mindr_lep2_jet_;
  TH1 *histogram_max_jet_eta_;
};

#endif
