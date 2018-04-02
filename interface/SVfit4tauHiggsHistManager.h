#ifndef hhAnalysis_tttt_SVfit4tauHiggsHistManager_h
#define hhAnalysis_tttt_SVfit4tauHiggsHistManager_h

/** \class SVfit4tauDiHiggsHistManager
 *
 * Book and fill histograms for reconstructed pT, eta, phi, and mass of Higgs bosons reconstructed by ClassicSVfit4tau algorithm
 *
 * \author Christian Veelken, Tallin
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector

#include "TauAnalysis/ClassicSVfit/interface/svFitAuxFunctions.h" // classic_svFit::LorentzVector

class SVfit4tauHiggsHistManager
  : public HistManagerBase
{
 public:
  SVfit4tauHiggsHistManager(const edm::ParameterSet& cfg);
  ~SVfit4tauHiggsHistManager() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory& dir) override;

  void
  fillHistograms(const classic_svFit::LorentzVector& recHiggsP4, 
                 double evtWeight, const Particle::LorentzVector* genHiggsP4 = 0);

 private:
  TH1* histogram_pt_;
  TH1* histogram_eta_;
  TH1* histogram_phi_;
  TH1* histogram_mass_;

  TH1* histogram_deltapt_;
  TH1* histogram_deltaeta_;
  TH1* histogram_deltaphi_;
  TH1* histogram_deltamass_;

  std::vector<TH1*> histograms_;
};

#endif
