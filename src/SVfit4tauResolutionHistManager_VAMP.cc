#include "hhAnalysis/tttt/interface/SVfit4tauResolutionHistManager_VAMP.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()

#include <TMath.h> // TMath::Pi()

SVfit4tauResolutionHistManager_VAMP::SVfit4tauResolutionHistManager_VAMP(const edm::ParameterSet& cfg)
  : HistManagerBase(cfg)
{}

void SVfit4tauResolutionHistManager_VAMP::bookHistograms(TFileDirectory& dir)
{
  histogram_dihiggsDeltaMass1_    = book1D(dir, "dihiggsDeltaMass1",    "dihiggsDeltaMass1",    400, -200.,  +200.);
  histogram_dihiggsRatioVisMass1_ = book1D(dir, "dihiggsRatioVisMass1", "dihiggsRatioVisMass1", 200,    0.,    10.);
  histogram_dihiggsRatioMass1_    = book1D(dir, "dihiggsRatioMass1",    "dihiggsRatioMass1",    200,    0.,    10.);
  
  histogram_dihiggsDeltaMass2_    = book1D(dir, "dihiggsDeltaMass2",    "dihiggsDeltaMass2",    400, -200.,  +200.);
  histogram_dihiggsRatioVisMass2_ = book1D(dir, "dihiggsRatioVisMass2", "dihiggsRatioVisMass2", 200,    0.,    10.);
  histogram_dihiggsRatioMass2_    = book1D(dir, "dihiggsRatioMass2",    "dihiggsRatioMass2",    200,    0.,    10.);
}

namespace
{
  void fillSVfit4tauResolutionHistograms(const SVfit4tauResult& result,
					 const Particle::LorentzVector* genDiHiggsP4, 
					 TH1* histogram_dihiggsDeltaMass, TH1* histogram_dihiggsRatioVisMass, TH1* histogram_dihiggsRatioMass,
					 double evtWeight, double evtWeightErr)
  {
    assert(genDiHiggsP4);

    fillWithOverFlow(histogram_dihiggsDeltaMass,      result.dihiggs_mass_ - genDiHiggsP4->mass(),  evtWeight, evtWeightErr);
    if ( genDiHiggsP4->mass() > 50. ) {
      fillWithOverFlow(histogram_dihiggsRatioVisMass, result.dihiggs_visMass_/genDiHiggsP4->mass(), evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_dihiggsRatioMass,    result.dihiggs_mass_/genDiHiggsP4->mass(),    evtWeight, evtWeightErr);
    }
  }
}

void
SVfit4tauResolutionHistManager_VAMP::fillHistograms(const std::vector<SVfit4tauResult>& results,
						    const Particle::LorentzVector* genDiHiggsP4, 
						    double evtWeight)
{
  const double evtWeightErr = 0.;
  
  if ( !genDiHiggsP4 ) return;

  if ( results.size() >= 1 ) {
    const SVfit4tauResult& result1 = results[0];
    if ( result1.isValidSolution_ ) {
      fillSVfit4tauResolutionHistograms(
        result1, 
	genDiHiggsP4, 
	histogram_dihiggsDeltaMass1_, histogram_dihiggsRatioVisMass1_, histogram_dihiggsRatioMass1_,
	evtWeight, evtWeightErr);
    }
  }

  if ( results.size() >= 2 ) {
    const SVfit4tauResult& result2 = results[1];
    if ( result2.isValidSolution_ ) {
      fillSVfit4tauResolutionHistograms(
        result2, 
	genDiHiggsP4, 
	histogram_dihiggsDeltaMass2_, histogram_dihiggsRatioVisMass2_, histogram_dihiggsRatioMass2_,
	evtWeight, evtWeightErr);
    }
  }
}
