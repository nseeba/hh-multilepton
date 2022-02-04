#ifndef hhAnalysis_multilepton_EvtHistManager_hh_2lss_vbf_h
#define hhAnalysis_multilepton_EvtHistManager_hh_2lss_vbf_h

/** \class EvtHistManager_hh_2lss
 *
 * Book and fill histograms for event-level quantities in the 2l+2tau_h category
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
                      int numJetsPtGt40, double dihiggsVisMass_sel,
                      double dihiggsMass_wMet_sel,
                      double evtWeight);

  const TH1 *getHistogram_EventCounter() const;

private:
  TH1 *histogram_numElectrons_;
  TH1 *histogram_numMuons_;
  TH1 *histogram_numJets_;
  TH1 *histogram_numJetsPtGt40_;
  TH1 *histogram_dihiggsVisMass_sel_;
  TH1 *histogram_dihiggsMass_wMet_sel_;
  TH1 *histogram_EventCounter_;
};

#endif
