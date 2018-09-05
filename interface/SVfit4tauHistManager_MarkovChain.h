#ifndef hhAnalysis_multilepton_SVfit4tauHistManager_MarkovChain_h
#define hhAnalysis_multilepton_SVfit4tauHistManager_MarkovChain_h

/** \class SVfit4tauHistManager_MarkovChain
 *
 * Book and fill histograms for di-Higgs system reconstructed by ClassicSVfit4tau algorithm with Markov-Chain integration,
 * used by HH->tttt, WWtt, and WWWW analysis 
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult

class SVfit4tauHistManager_MarkovChain
  : public HistManagerBase
{
public:
  SVfit4tauHistManager_MarkovChain(const edm::ParameterSet & cfg);
  ~SVfit4tauHistManager_MarkovChain() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;
  void
  bookHistograms2d(TFileDirectory & dir);

  void
  fillHistograms(const std::vector<SVfit4tauResult>& results,
                 double evtWeight);

 private:

  TH1 * histogram_numValidSolutions_;

  TH1 * histogram_dihiggsVisMass1_;
  TH1 * histogram_ditau1VisMass1_;
  TH1 * histogram_ditau2VisMass1_;
  TH1 * histogram_dihiggsMass1_;
  TH1 * histogram_ditau1Mass1_;
  TH1 * histogram_ditau2Mass1_;
  TH1 * histogram_logLmax1_;
  TH2 * histogram_logLmax1_vs_dihiggsMass1_;

  TH1 * histogram_dihiggsVisMass2_;
  TH1 * histogram_ditau1VisMass2_;
  TH1 * histogram_ditau2VisMass2_;
  TH1 * histogram_dihiggsMass2_;
  TH1 * histogram_ditau1Mass2_;
  TH1 * histogram_ditau2Mass2_;
  TH1 * histogram_logLmax2_;
  TH2 * histogram_logLmax2_vs_dihiggsMass2_;
};

#endif
