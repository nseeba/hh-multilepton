#ifndef hhAnalysis_tttt_EvtHistManager_SVfit4tau_h
#define hhAnalysis_tttt_EvtHistManager_SVfit4tau_h

/** \class EvtHistManager_SVfit4tau
 *
 * Book and fill histograms for event-level quantities in HH->4tau analysis
 *
 * \author Christian Veelken, Tallin
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector

#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult

#include <TMatrixD.h> // TMatrixD

class EvtHistManager_SVfit4tau
  : public HistManagerBase
{
 public:
  EvtHistManager_SVfit4tau(const edm::ParameterSet & cfg);
  ~EvtHistManager_SVfit4tau() {}

  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(const SVfit4tauResult& svFit4tauResult_MarkovChain, const SVfit4tauResult& svFit4tauResult_VAMP, 
		 const Particle::LorentzVector* genDiHiggsP4, 
		 const Particle::LorentzVector* genDiTau1P4, 
		 const Particle::LorentzVector* genDiTau2P4, 
		 const Particle::LorentzVector& measuredTau1P4, const Particle::LorentzVector& measuredTau1P4_gen, 
		 const Particle::LorentzVector& measuredTau2P4, const Particle::LorentzVector& measuredTau2P4_gen, 
		 const Particle::LorentzVector& measuredTau3P4, const Particle::LorentzVector& measuredTau3P4_gen, 
		 const Particle::LorentzVector& measuredTau4P4, const Particle::LorentzVector& measuredTau4P4_gen,
		 double metPx, double metPy, const TMatrixD& metCov, double metPx_gen, double metPy_gen, 
		 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

 private:
  int era_;

  TH1 * histogram_mhh_MarkovChain_;
  TH1 * histogram_mhh_VAMP_;
  TH1 * histogram_mhh_gen_;
  TH1 * histogram_mh1_;
  TH1 * histogram_mh1_gen_;
  TH1 * histogram_mh2_;
  TH1 * histogram_mh2_gen_;

  TH1 * histogram_mhhVis_;
  TH1 * histogram_mhhVis_gen_;
  TH1 * histogram_mh1Vis_;
  TH1 * histogram_mh1Vis_gen_;
  TH1 * histogram_mh2Vis_;
  TH1 * histogram_mh2Vis_gen_;

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
