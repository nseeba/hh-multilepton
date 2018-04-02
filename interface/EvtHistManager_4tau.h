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

class EvtHistManager_4tau
  : public HistManagerBase
{
 public:
  EvtHistManager_4tau(const edm::ParameterSet & cfg);
  ~EvtHistManager_4tau() {}

  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(const Particle::LorentzVector& measuredTau1P4, 
		 const Particle::LorentzVector& measuredTau2P4, 
		 const Particle::LorentzVector& measuredTau3P4, 
		 const Particle::LorentzVector& measuredTau4P4, 
		 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

 private:
  int era_;

  TH1 * histogram_mh1Vis_;
  TH1 * histogram_mh2Vis_;

  TH1 * histogram_mhhVis_;

  TH1 * histogram_EventCounter_;
};

#endif
