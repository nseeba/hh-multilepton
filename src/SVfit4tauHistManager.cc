#include "hhAnalysis/tttt/interface/SVfit4tauHistManager.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Log

SVfit4tauHistManager::SVfit4tauHistManager(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{}

void
SVfit4tauHistManager::bookHistograms(TFileDirectory & dir)
{
  histogram_dihiggsVisMass_ = book1D(dir, "dihiggsVisMass", "dihiggsVisMass", 150,   0., 1500.);
  histogram_dihiggsMass1_   = book1D(dir, "dihiggsMass1",   "dihiggsMass1",   150,   0., 1500.);
  histogram_dihiggsMass2_   = book1D(dir, "dihiggsMass2",   "dihiggsMass2",   150,   0., 1500.);

  histogram_ditau1VisMass_  = book1D(dir, "ditau1VisMass",  "ditau1VisMass",   50,   0.,  250.);
  histogram_ditau1Mass1_    = book1D(dir, "ditau1Mass1",    "ditau1Mass1",     50,   0.,  250.);
  histogram_ditau1Mass2_    = book1D(dir, "ditau1Mass2",    "ditau1Mass2",     50,   0.,  250.);

  histogram_ditau2VisMass_  = book1D(dir, "ditau2VisMass",  "ditau2VisMass",   50,   0.,  250.);
  histogram_ditau2Mass1_    = book1D(dir, "ditau2Mass1",    "ditau2Mass1",     50,   0.,  250.);
  histogram_ditau2Mass2_    = book1D(dir, "ditau2Mass2",    "ditau2Mass2",     50,   0.,  250.);

  histogram_logProbMax1_    = book1D(dir, "logProbMax1",    "logProbMax1",    200, -50.,  +50.);
  histogram_logProbMax2_    = book1D(dir, "logProbMax2",    "logProbMax2",    200, -50.,  +50.);
}

void
SVfit4tauHistManager::fillHistograms(const std::vector<SVfit4tauResult>& results,
				     double evtWeight)
{
  const double evtWeightErr = 0.;

  if ( results.size() >= 1 ) {
    const SVfit4tauResult& result = results[0];
    if ( result.isValidSolution_ ) {
      fillWithOverFlow(histogram_dihiggsVisMass_, result.dihiggs_visMass_,     evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_dihiggsMass1_,   result.dihiggs_mass_,        evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_ditau1VisMass_,  result.ditau1_visMass_,      evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_ditau1Mass1_,    result.ditau1_mass_,         evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_ditau2VisMass_,  result.ditau2_visMass_,      evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_ditau2Mass1_,    result.ditau2_mass_,         evtWeight, evtWeightErr);
      if ( result.probMax_ > 0. ) {
	fillWithOverFlow(histogram_logProbMax1_,  TMath::Log(result.probMax_), evtWeight, evtWeightErr);
      }
    }
  }
  if ( results.size() >= 2 ) {
    const SVfit4tauResult& result = results[1];
    if ( result.isValidSolution_ ) {
      fillWithOverFlow(histogram_dihiggsMass2_,   result.dihiggs_mass_,        evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_ditau1Mass2_,    result.ditau1_mass_,         evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_ditau2Mass2_,    result.ditau2_mass_,         evtWeight, evtWeightErr);
      if ( result.probMax_ > 0. ) {
	fillWithOverFlow(histogram_logProbMax2_,  TMath::Log(result.probMax_), evtWeight, evtWeightErr);
      }
    }
  }
}
