#ifndef hhAnalysis_tttt_SVfit4tauHistManager_h
#define hhAnalysis_tttt_SVfit4tauHistManager_h

/** \class SVfit4tauHistManager
 *
 * Book and fill histograms for di-Higgs system reconstructed by ClassicSVfit4tau algorithm,
 * used by HH->tttt, WWtt, and WWWW analysis 
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

#include "hhAnalysis/tttt/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult

class SVfit4tauHistManager
  : public HistManagerBase
{
public:
  SVfit4tauHistManager(const edm::ParameterSet & cfg);
  ~SVfit4tauHistManager() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

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
  TH1 * histogram_logProbMax1_;

  TH1 * histogram_dihiggsVisMass2_;
  TH1 * histogram_ditau1VisMass2_;
  TH1 * histogram_ditau2VisMass2_;
  TH1 * histogram_dihiggsMass2_;
  TH1 * histogram_ditau1Mass2_;
  TH1 * histogram_ditau2Mass2_;
  TH1 * histogram_logProbMax2_;

  TH1 * histogram_logProbMax2_minus_logProbMax1_;
};

#endif
