#ifndef hhAnalysis_tttt_SVfit4tauDisambiguationHistManager_h
#define hhAnalysis_tttt_SVfit4tauDisambiguationHistManager_h

/** \class SVfit4tauDisambiguationHistManager
 *
 * Book and fill histograms for correct vs spurious associations of tau decay products to Higgs bosons
 * used by HH->tttt, WWtt, and WWWW analysis 
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult

class SVfit4tauDisambiguationHistManager
  : public HistManagerBase
{
public:
  SVfit4tauDisambiguationHistManager(const edm::ParameterSet & cfg);
  ~SVfit4tauDisambiguationHistManager() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(const SVfit4tauResult& result_correctAssoc,
		 const Particle::LorentzVector& measuredTau1Higgs1P4_correctAssoc,
		 const Particle::LorentzVector& measuredTau2Higgs1P4_correctAssoc,
		 const Particle::LorentzVector& measuredTau1Higgs2P4_correctAssoc,
		 const Particle::LorentzVector& measuredTau2Higgs2P4_correctAssoc,
		 const SVfit4tauResult& result_incorrectAssoc,
		 const Particle::LorentzVector& measuredTau1Higgs1P4_incorrectAssoc,
		 const Particle::LorentzVector& measuredTau2Higgs1P4_incorrectAssoc,
		 const Particle::LorentzVector& measuredTau1Higgs2P4_incorrectAssoc,
		 const Particle::LorentzVector& measuredTau2Higgs2P4_incorrectAssoc,
		 double evtWeight);

 private:

  TH2 * histogram_dihiggsMass_;
  TH2 * histogram_dihiggsMassErr_;
  TH2 * histogram_dihiggsPt_; // CV: only filled if Markov-Chain integration is used
  TH2 * histogram_logLmax_;

  TH2 * histogram_avDeltaPhi_;
  TH2 * histogram_avDeltaEta_;
  TH2 * histogram_avDeltaR_;

  TH2 * histogram_avDiTauVisPt_;
  TH2 * histogram_avDiTauPt_; // CV: only filled if Markov-Chain integration is used
};

#endif
