#include "hhAnalysis/multilepton/interface/SVfit4tauHistManager_VAMP.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Log

SVfit4tauHistManager_VAMP::SVfit4tauHistManager_VAMP(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
  , histogram_logLmax1_vs_dihiggsMass1_(nullptr)
  , histogram_logLmax2_vs_dihiggsMass2_(nullptr)
{
  central_or_shiftOptions_["numValidSolutions"] = { "central" };
  central_or_shiftOptions_["dihiggsVisMass1"] = { "central" };
  central_or_shiftOptions_["dihiggsMass1"] = { "central" };
  central_or_shiftOptions_["logLmax1"] = { "central" };
  central_or_shiftOptions_["dihiggsVisMass2"] = { "central" };
  central_or_shiftOptions_["dihiggsMass2"] = { "central" };
  central_or_shiftOptions_["logLmax2"] = { "central" };
  central_or_shiftOptions_["logLmax1_vs_dihiggsMass1"] = { "central" };
  central_or_shiftOptions_["logLmax2_vs_dihiggsMass2"] = { "central" };
}

void
SVfit4tauHistManager_VAMP::bookHistograms(TFileDirectory & dir)
{
  histogram_numValidSolutions_        = book1D(dir, "numValidSolutions",        "numValidSolutions",          5,  -0.5,   4.5);
                  
  histogram_dihiggsVisMass1_          = book1D(dir, "dihiggsVisMass1",          "dihiggsVisMass1",          150,   0., 1500.);
  histogram_dihiggsMass1_             = book1D(dir, "dihiggsMass1",             "dihiggsMass1",             150,   0., 1500.);
  histogram_logLmax1_                 = book1D(dir, "logLmax1",                 "logLmax1",                 200, -50.,  +50.);

  histogram_dihiggsVisMass2_          = book1D(dir, "dihiggsVisMass2",          "dihiggsVisMass2",          150,   0., 1500.);
  histogram_dihiggsMass2_             = book1D(dir, "dihiggsMass2",             "dihiggsMass2",             150,   0., 1500.);
  histogram_logLmax2_                 = book1D(dir, "logLmax2",                 "logLmax2",                 200, -50.,  +50.);
}

void
SVfit4tauHistManager_VAMP::bookHistograms2d(TFileDirectory & dir)
{
  histogram_logLmax1_vs_dihiggsMass1_ = book2D(dir, "logLmax1_vs_dihiggsMass1", "logLmax1_vs_dihiggsMass1", 150,   0., 1500., 200, -50., +50.);
  
  histogram_logLmax2_vs_dihiggsMass2_ = book2D(dir, "logLmax2_vs_dihiggsMass2", "logLmax2_vs_dihiggsMass2", 150,   0., 1500., 200, -50., +50.);
}

void
SVfit4tauHistManager_VAMP::fillHistograms(const std::vector<SVfit4tauResult>& results,
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
    fillWithOverFlow(histogram_dihiggsVisMass1_, result1.dihiggs_visMass_, evtWeight, evtWeightErr);
    if ( result1.isValidSolution_ ) {
      fillWithOverFlow(histogram_dihiggsMass1_,  result1.dihiggs_mass_,    evtWeight, evtWeightErr);
      if ( result1.Lmax_ > 0. ) {
	double logLmax = TMath::Log(result1.Lmax_);
	fillWithOverFlow(histogram_logLmax1_, logLmax, evtWeight, evtWeightErr);
	if ( histogram_logLmax1_vs_dihiggsMass1_ ) {
	  fillWithOverFlow2d(histogram_logLmax1_vs_dihiggsMass1_, result1.dihiggs_mass_, logLmax, evtWeight, evtWeightErr);
	}
      }
    }
  }

  if ( results.size() >= 2 ) {
    const SVfit4tauResult& result2 = results[1];
    fillWithOverFlow(histogram_dihiggsVisMass2_, result2.dihiggs_visMass_, evtWeight, evtWeightErr);
    if ( result2.isValidSolution_ ) {
      fillWithOverFlow(histogram_dihiggsMass2_,  result2.dihiggs_mass_,    evtWeight, evtWeightErr);
      if ( result2.Lmax_ > 0. ) {
	double logLmax = TMath::Log(result2.Lmax_);
	fillWithOverFlow(histogram_logLmax2_, logLmax, evtWeight, evtWeightErr);
	if ( histogram_logLmax2_vs_dihiggsMass2_ ) {
	  fillWithOverFlow2d(histogram_logLmax2_vs_dihiggsMass2_, result2.dihiggs_mass_, logLmax, evtWeight, evtWeightErr);
	}
      }
    }
  }
}
