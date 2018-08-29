#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_2l_2tau.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

EvtHistManager_hh_2l_2tau::EvtHistManager_hh_2l_2tau(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{}

const TH1 *
EvtHistManager_hh_2l_2tau::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_2l_2tau::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_     = book1D(dir, "numElectrons",     "numElectrons",      5, -0.5,  +4.5);
  histogram_numMuons_         = book1D(dir, "numMuons",         "numMuons",          5, -0.5,  +4.5);
  histogram_numHadTaus_       = book1D(dir, "numHadTaus",       "numHadTaus",        5, -0.5,  +4.5);
  histogram_numJets_          = book1D(dir, "numJets",          "numJets",          20, -0.5, +19.5);
  histogram_numJetsPtGt40_    = book1D(dir, "numJetsPtGt40",    "numJetsPtGt40",    20, -0.5, +19.5);
  histogram_numBJets_loose_   = book1D(dir, "numBJets_loose",   "numBJets_loose",   10, -0.5,  +9.5);
  histogram_numBJets_medium_  = book1D(dir, "numBJets_medium",  "numBJets_medium",  10, -0.5,  +9.5);

  histogram_mTauTauVis_       = book1D(dir, "mTauTauVis",       "mTauTauVis",       40,  0.,  200.);

  histogram_leptonPairCharge_ = book1D(dir, "leptonPairCharge", "leptonPairCharge",  5, -2.5,  +2.5);
  histogram_hadTauPairCharge_ = book1D(dir, "hadTauPairCharge", "hadTauPairCharge",  5, -2.5,  +2.5);

  histogram_dihiggsVisMass_   = book1D(dir, "dihiggsVisMass",   "dihiggsVisMass",  150,  0., 1500.);
  histogram_dihiggsMass_      = book1D(dir, "dihiggsMass",      "dihiggsMass",     150,  0., 1500.);

  histogram_HT_               = book1D(dir, "HT",               "HT",              150,  0., 1500.);
  histogram_STMET_            = book1D(dir, "STMET",            "STMET",           150,  0., 1500.);

  histogram_EventCounter_     = book1D(dir, "EventCounter",     "EventCounter",      1, -0.5,  +0.5);
}

void
EvtHistManager_hh_2l_2tau::fillHistograms(int numElectrons,
					  int numMuons,
					  int numHadTaus,
					  int numJets,
					  int numJetsPtGt40,
					  int numBJets_loose,
					  int numBJets_medium,
					  double mTauTauVis,
					  double leptonPairCharge,
					  double hadTauPairCharge,
					  double dihiggsVisMass,
					  double dihiggsMass,
					  double HT,
					  double STMET,
					  double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,     numElectrons,     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,         numMuons,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numHadTaus_,       numHadTaus,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,          numJets,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsPtGt40_,    numJetsPtGt40,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,   numBJets_loose,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,  numBJets_medium,  evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mTauTauVis_,       mTauTauVis,       evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_leptonPairCharge_, leptonPairCharge, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_hadTauPairCharge_, hadTauPairCharge, evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_dihiggsVisMass_,   dihiggsVisMass,   evtWeight, evtWeightErr);
  if ( dihiggsMass > 0. ) {
    fillWithOverFlow(histogram_dihiggsMass_,    dihiggsMass,      evtWeight, evtWeightErr);
  }

  fillWithOverFlow(histogram_HT_,               HT,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,            STMET,            evtWeight, evtWeightErr);
  
  fillWithOverFlow(histogram_EventCounter_,     0.,               evtWeight, evtWeightErr);
}
