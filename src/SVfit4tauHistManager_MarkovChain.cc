#include "hhAnalysis/tttt/interface/SVfit4tauHistManager_MarkovChain.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Log

SVfit4tauHistManager_MarkovChain::SVfit4tauHistManager_MarkovChain(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{}

void
SVfit4tauHistManager_MarkovChain::bookHistograms(TFileDirectory & dir)
{
  histogram_numValidSolutions_             = book1D(dir, "numValidSolutions",             "numValidSolutions",               5,  -0.5,   4.5);
            
  histogram_dihiggsVisMass1_               = book1D(dir, "dihiggsVisMass1",               "dihiggsVisMass1",               150,   0., 1500.);
  histogram_ditau1VisMass1_                = book1D(dir, "ditau1VisMass1",                "ditau1VisMass1",                 50,   0.,  250.);
  histogram_ditau2VisMass1_                = book1D(dir, "ditau2VisMass1",                "ditau2VisMass1",                 50,   0.,  250.);
  histogram_dihiggsMass1_                  = book1D(dir, "dihiggsMass1",                  "dihiggsMass1",                  150,   0., 1500.);
  histogram_ditau1Mass1_                   = book1D(dir, "ditau1Mass1",                   "ditau1Mass1",                    50,   0.,  250.);
  histogram_ditau2Mass1_                   = book1D(dir, "ditau2Mass1",                   "ditau2Mass1",                    50,   0.,  250.);
  histogram_logProbMax1_                   = book1D(dir, "logProbMax1",                   "logProbMax1",                   200, -50.,  +50.);

  histogram_dihiggsVisMass2_               = book1D(dir, "dihiggsVisMass2",               "dihiggsVisMass2",               150,   0., 1500.);
  histogram_ditau1VisMass2_                = book1D(dir, "ditau1VisMass2",                "ditau1VisMass2",                 50,   0.,  250.);
  histogram_ditau2VisMass2_                = book1D(dir, "ditau2VisMass2",                "ditau2VisMass2",                 50,   0.,  250.);
  histogram_dihiggsMass2_                  = book1D(dir, "dihiggsMass2",                  "dihiggsMass2",                  150,   0., 1500.);
  histogram_ditau1Mass2_                   = book1D(dir, "ditau1Mass2",                   "ditau1Mass2",                    50,   0.,  250.);
  histogram_ditau2Mass2_                   = book1D(dir, "ditau2Mass2",                   "ditau2Mass2",                    50,   0.,  250.);
  histogram_logProbMax2_                   = book1D(dir, "logProbMax2",                   "logProbMax2",                   200, -50.,  +50.);

  histogram_logProbMax2_minus_logProbMax1_ = book1D(dir, "logProbMax2_minus_logProbMax1", "logProbMax2_minus_logProbMax1", 200, -50.,  +50.);
}

void
SVfit4tauHistManager_MarkovChain::fillHistograms(const std::vector<SVfit4tauResult>& results,
						 double evtWeight)
{
  const double evtWeightErr = 0.;

  int numValidSolutions = 0;  
  for ( std::vector<SVfit4tauResult>::const_iterator result = results.begin();
	result != results.end(); ++result ) {
    if ( result->isValidSolution_ ) ++numValidSolutions;
  }
  fillWithOverFlow(histogram_numValidSolutions_, numValidSolutions, evtWeight, evtWeightErr);

  if ( results.size() >= 1 ) {
    const SVfit4tauResult& result1 = results[0];
    fillWithOverFlow(histogram_dihiggsVisMass1_,  result1.dihiggs_visMass_,     evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau1VisMass1_,   result1.ditau1_visMass_,      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau2VisMass1_,   result1.ditau2_visMass_,      evtWeight, evtWeightErr);
    if ( result1.isValidSolution_ ) {
      fillWithOverFlow(histogram_dihiggsMass1_,   result1.dihiggs_mass_,        evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_ditau1Mass1_,    result1.ditau1_mass_,         evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_ditau2Mass1_,    result1.ditau2_mass_,         evtWeight, evtWeightErr);
      if ( result1.probMax_ > 0. ) {
	fillWithOverFlow(histogram_logProbMax1_,  TMath::Log(result1.probMax_), evtWeight, evtWeightErr);
      }
    }
  }

  if ( results.size() >= 2 ) {
    const SVfit4tauResult& result2 = results[1];
    fillWithOverFlow(histogram_dihiggsVisMass2_,  result2.dihiggs_visMass_,     evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau1VisMass2_,   result2.ditau1_visMass_,      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau2VisMass2_,   result2.ditau2_visMass_,      evtWeight, evtWeightErr);
    if ( result2.isValidSolution_ ) {
      fillWithOverFlow(histogram_dihiggsMass2_,   result2.dihiggs_mass_,        evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_ditau1Mass2_,    result2.ditau1_mass_,         evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_ditau2Mass2_,    result2.ditau2_mass_,         evtWeight, evtWeightErr);
      if ( result2.probMax_ > 0. ) {
	fillWithOverFlow(histogram_logProbMax2_,  TMath::Log(result2.probMax_), evtWeight, evtWeightErr);
      }
    }
  }

  if ( results.size() >= 2 ) {
    const SVfit4tauResult& result1 = results[0];
    const SVfit4tauResult& result2 = results[1];
    if ( result1.isValidSolution_ && result1.probMax_ > 0. &&
	 result2.isValidSolution_ && result2.probMax_ > 0. ) {
      fillWithOverFlow(histogram_logProbMax2_minus_logProbMax1_, TMath::Log(result2.probMax_) - TMath::Log(result1.probMax_), evtWeight, evtWeightErr);
    }
  }
}
