#include "hhAnalysis/tttt/interface/EvtHistManager_4tau.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // kEra_2017
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()

EvtHistManager_4tau::EvtHistManager_4tau(const edm::ParameterSet& cfg)
  : HistManagerBase(cfg)
{}

const TH1 *
EvtHistManager_4tau::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void EvtHistManager_4tau::bookHistograms(TFileDirectory & dir)
{
  histogram_mh1Vis_ = book1D(dir, "mh1Vis", "mh1Vis",  50, 0.,  500.);
  histogram_mh2Vis_ = book1D(dir, "mh2Vis", "mh2Vis",  50, 0.,  500.);

  histogram_mhhVis_ = book1D(dir, "mhhVis", "mhhVis", 100, 0., 1000.);

  histogram_EventCounter_ = book1D(dir, "EventCounter", "EventCounter", 1, -0.5, +0.5);
}

void
EvtHistManager_4tau::fillHistograms(const Particle::LorentzVector& measuredTau1P4, 
				    const Particle::LorentzVector& measuredTau2P4, 
				    const Particle::LorentzVector& measuredTau3P4, 
				    const Particle::LorentzVector& measuredTau4P4, 
				    double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_mh1Vis_, (measuredTau1P4 + measuredTau2P4).mass(), evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mh2Vis_, (measuredTau3P4 + measuredTau4P4).mass(), evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mhhVis_, (measuredTau1P4 + measuredTau2P4 + measuredTau3P4 + measuredTau4P4).mass(), evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_EventCounter_, 0., evtWeight, evtWeightErr);
}
