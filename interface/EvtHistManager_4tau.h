#ifndef hhAnalysis_tttt_EvtHistManager_4tau_h
#define hhAnalysis_tttt_EvtHistManager_4tau_h

/** \class EvtHistManager_4tau
 *
 * Book and fill histograms for event-level quantities in hh->4tau analysis
 *
 * \author Christian Veelken, Tallin
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector

#include <TMatrixD.h> // TMatrixD

class EvtHistManager_4tau
  : public HistManagerBase
{
 public:
  EvtHistManager_4tau(const edm::ParameterSet & cfg);
  ~EvtHistManager_4tau() {}

  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(const Particle::LorentzVector& measuredTau1P4, const Particle::LorentzVector& measuredTau1P4_gen, 
		 const Particle::LorentzVector& measuredTau2P4, const Particle::LorentzVector& measuredTau2P4_gen, 
		 const Particle::LorentzVector& measuredTau3P4, const Particle::LorentzVector& measuredTau3P4_gen, 
		 const Particle::LorentzVector& measuredTau4P4, const Particle::LorentzVector& measuredTau4P4_gen,
		 double metPx, double metPy, const TMatrixD& metCov, double metPx_gen, double metPy_gen, 
		 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

 private:
  int era_;

  TH1 * histogram_mh1Vis_;
  TH1 * histogram_mh1Vis_gen_;
  TH1 * histogram_mh2Vis_;
  TH1 * histogram_mh2Vis_gen_;

  TH1 * histogram_mhhVis_;
  TH1 * histogram_mhhVis_gen_;

  TH1* histogram_ratiomeasuredTau1Pt_;
  TH1* histogram_ratiomeasuredTau2Pt_;
  TH1* histogram_ratiomeasuredTau3Pt_;
  TH1* histogram_ratiomeasuredTau4Pt_;
  
  TH1* histogram_deltametPx_;
  TH1* histogram_pullmetPx_;
  TH1* histogram_deltametPy_;
  TH1* histogram_pullmetPy_;

  TH1 * histogram_EventCounter_;
};

#endif
