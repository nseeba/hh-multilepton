#include "hhAnalysis/tttt/interface/EvtHistManager_hh_3l_1tau.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

EvtHistManager_hh_3l_1tau::EvtHistManager_hh_3l_1tau(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{}

const TH1 *
EvtHistManager_hh_3l_1tau::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_3l_1tau::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_    = book1D(dir, "numElectrons",    "numElectrons",      5, -0.5,  +4.5);
  histogram_numMuons_        = book1D(dir, "numMuons",        "numMuons",          5, -0.5,  +4.5);
  histogram_numHadTaus_      = book1D(dir, "numHadTaus",      "numHadTaus",        5, -0.5,  +4.5);
  histogram_numJets_         = book1D(dir, "numJets",         "numJets",          20, -0.5, +19.5);
  histogram_numJetsPtGt40_   = book1D(dir, "numJetsPtGt40",   "numJetsPtGt40",    20, -0.5, +19.5);
  histogram_numBJets_loose_  = book1D(dir, "numBJets_loose",  "numBJets_loose",   10, -0.5,  +9.5);
  histogram_numBJets_medium_ = book1D(dir, "numBJets_medium", "numBJets_medium",  10, -0.5,  +9.5);

  histogram_m4Vis_           = book1D(dir, "m4Vis",           "m4Vis",           150,  0., 1500.);
  histogram_m4_              = book1D(dir, "m4",              "m4",              150,  0., 1500.);

  histogram_EventCounter_    = book1D(dir, "EventCounter",    "EventCounter",      1, -0.5,  +0.5);
}

void
EvtHistManager_hh_3l_1tau::fillHistograms(int numElectrons,
					  int numMuons,
					  int numHadTaus,
					  int numJets,
					  int numJetsPtGt40,
					  int numBJets_loose,
					  int numBJets_medium,
					  double m4Vis,
					  double m4_1,
					  double m4_2,
					  double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,    numElectrons,        evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,        numMuons,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numHadTaus_,      numHadTaus,          evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numJets_,         numJets,             evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numJetsPtGt40_,   numJetsPtGt40,       evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,  numBJets_loose,      evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_, numBJets_medium,     evtWeight,     evtWeightErr);

  fillWithOverFlow(histogram_m4Vis_,           m4Vis,               evtWeight,     evtWeightErr);
  if ( m4_1 > 0. ) {
    double factor = ( m4_2 > 0. ) ? 0.5 : 1.;
    fillWithOverFlow(histogram_m4_,            m4_1,         factor*evtWeight, factor*evtWeightErr);
  }
  if ( m4_2 > 0. ) {
    double factor = ( m4_1 > 0. ) ? 0.5 : 1.;
    fillWithOverFlow(histogram_m4_,            m4_2,         factor*evtWeight, factor*evtWeightErr);
  }
  
  fillWithOverFlow(histogram_EventCounter_,    0.,                  evtWeight,     evtWeightErr);
}
