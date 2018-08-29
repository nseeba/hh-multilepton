#ifndef hhAnalysis_multilepton_SVfit4tauResolutionHistManager_VAMP_h
#define hhAnalysis_multilepton_SVfit4tauResolutionHistManager_VAMP_h

/** \class SVfit4tauResolutionHistManager_VAMP
 *
 * Book and fill histograms for resolution on di-Higgs mass reconstructed by ClassicSVfit4tau algorithm with VAMP integration
 *
 * \author Christian Veelken, Tallin
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector

#include "TauAnalysis/ClassicSVfit/interface/svFitAuxFunctions.h" // classic_svFit::LorentzVector

#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult

class SVfit4tauResolutionHistManager_VAMP
  : public HistManagerBase
{
 public:
  SVfit4tauResolutionHistManager_VAMP(const edm::ParameterSet& cfg);
  ~SVfit4tauResolutionHistManager_VAMP() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory& dir) override;

  void
  fillHistograms(const std::vector<SVfit4tauResult>& results,
		 const Particle::LorentzVector* genDiHiggsP4, 
		 double evtWeight);

 private:
  TH1* histogram_dihiggsDeltaMass1_;
  TH1* histogram_dihiggsRatioVisMass1_;
  TH1* histogram_dihiggsRatioMass1_;
  
  TH1* histogram_dihiggsDeltaMass2_;
  TH1* histogram_dihiggsRatioVisMass2_;
  TH1* histogram_dihiggsRatioMass2_;

  std::vector<TH1*> histograms_;
};

#endif
