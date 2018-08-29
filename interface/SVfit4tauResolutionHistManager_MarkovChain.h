#ifndef hhAnalysis_multilepton_SVfit4tauResolutionHistManager_MarkovChain_h
#define hhAnalysis_multilepton_SVfit4tauResolutionHistManager_MarkovChain_h

/** \class SVfit4tauResolutionHistManager_MarkovChain
 *
 * Book and fill histograms for pT, eta, phi, and mass resolution of di-Higgs system reconstructed by ClassicSVfit4tau algorithm with Markov-Chain integration
 *
 * \author Christian Veelken, Tallin
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector

#include "TauAnalysis/ClassicSVfit/interface/svFitAuxFunctions.h" // classic_svFit::LorentzVector

#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult

class SVfit4tauResolutionHistManager_MarkovChain
  : public HistManagerBase
{
 public:
  SVfit4tauResolutionHistManager_MarkovChain(const edm::ParameterSet& cfg);
  ~SVfit4tauResolutionHistManager_MarkovChain() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory& dir) override;

  void
  fillHistograms(const std::vector<SVfit4tauResult>& results,
		 const Particle::LorentzVector* genDiHiggsP4, 
		 const Particle::LorentzVector* genDiTau1P4, 
		 const Particle::LorentzVector* genDiTau2P4, 
		 double evtWeight);

 private:
  TH1* histogram_dihiggsPt1_;
  TH1* histogram_dihiggsEta1_;
  TH1* histogram_dihiggsPhi1_;
  TH1* histogram_ditau1Pt1_;
  TH1* histogram_ditau1Eta1_;
  TH1* histogram_ditau1Phi1_;
  TH1* histogram_ditau2Pt1_;
  TH1* histogram_ditau2Eta1_;
  TH1* histogram_ditau2Phi1_;
  
  TH1* histogram_dihiggsDeltaMass1_;
  TH1* histogram_dihiggsRatioVisMass1_;
  TH1* histogram_dihiggsRatioMass1_;
  TH1* histogram_ditau1DeltaMass1_;
  TH1* histogram_ditau1RatioVisMass1_;
  TH1* histogram_ditau1RatioMass1_;
  TH1* histogram_ditau2DeltaMass1_;
  TH1* histogram_ditau2RatioVisMass1_;
  TH1* histogram_ditau2RatioMass1_;
  
  TH1* histogram_dihiggsDeltaPt1_;
  TH1* histogram_dihiggsDeltaEta1_;
  TH1* histogram_dihiggsDeltaPhi1_;
  TH1* histogram_ditau1DeltaPt1_;
  TH1* histogram_ditau1DeltaEta1_;
  TH1* histogram_ditau1DeltaPhi1_;
  TH1* histogram_ditau2DeltaPt1_;
  TH1* histogram_ditau2DeltaEta1_;
  TH1* histogram_ditau2DeltaPhi1_;

  TH1* histogram_dihiggsPt2_;
  TH1* histogram_dihiggsEta2_;
  TH1* histogram_dihiggsPhi2_;
  TH1* histogram_ditau1Pt2_;
  TH1* histogram_ditau1Eta2_;
  TH1* histogram_ditau1Phi2_;
  TH1* histogram_ditau2Pt2_;
  TH1* histogram_ditau2Eta2_;
  TH1* histogram_ditau2Phi2_;
  
  TH1* histogram_dihiggsDeltaMass2_;
  TH1* histogram_dihiggsRatioVisMass2_;
  TH1* histogram_dihiggsRatioMass2_;
  TH1* histogram_ditau1DeltaMass2_;
  TH1* histogram_ditau1RatioVisMass2_;
  TH1* histogram_ditau1RatioMass2_;
  TH1* histogram_ditau2DeltaMass2_;
  TH1* histogram_ditau2RatioVisMass2_;
  TH1* histogram_ditau2RatioMass2_;
  
  TH1* histogram_dihiggsDeltaPt2_;
  TH1* histogram_dihiggsDeltaEta2_;
  TH1* histogram_dihiggsDeltaPhi2_;
  TH1* histogram_ditau1DeltaPt2_;
  TH1* histogram_ditau1DeltaEta2_;
  TH1* histogram_ditau1DeltaPhi2_;
  TH1* histogram_ditau2DeltaPt2_;
  TH1* histogram_ditau2DeltaEta2_;
  TH1* histogram_ditau2DeltaPhi2_;

  std::vector<TH1*> histograms_;
};

#endif
