#include "hhAnalysis/4tau/interface/SVfit4tauHiggsHistManager.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()

#include <TMath.h> // TMath::Pi()

SVfit4tauHiggsHistManager::SVfit4tauHiggsHistManager(const edm::ParameterSet& cfg)
  : HistManagerBase(cfg)
{}

void SVfit4tauHiggsHistManager::bookHistograms(TFileDirectory& dir)
{
  histogram_pt_        = book1D(dir, "pt",        "pt",        200,    0.,  1000.);
  histogram_eta_       = book1D(dir, "eta",       "eta",        46,   -2.3,   +2.3);
  histogram_phi_       = book1D(dir, "phi",       "phi",        36, -TMath::Pi(), +TMath::Pi());
  histogram_mass_      = book1D(dir, "mass",      "mass",      250,    0.,   250.);

  histogram_deltapt_   = book1D(dir, "deltapt",   "deltapt",   500, -250.,  +250.);
  histogram_deltaeta_  = book1D(dir, "deltaeta",  "deltaeta",   80,   -0.2,   +0.2);
  histogram_deltaphi_  = book1D(dir, "deltaphi",  "deltaphi",  200,   -0.5,   +0.5);
  histogram_deltamass_ = book1D(dir, "deltamass", "deltamass", 200, -100.,  +100.);
}

void
SVfit4tauHiggsHistManager::fillHistograms(const classic_svFit::LorentzVector& recHiggsP4, 
					  double evtWeight, const Particle::LorentzVector* genHiggsP4)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_pt_,   recHiggsP4.pt(),   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_eta_,  recHiggsP4.eta(),  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_phi_,  recHiggsP4.phi(),  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mass_, recHiggsP4.mass(), evtWeight, evtWeightErr);

  if ( genHiggsP4 ) {
    fillWithOverFlow(histogram_deltapt_,   recHiggsP4.pt()   - genHiggsP4->pt(),   evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltaeta_,  recHiggsP4.eta()  - genHiggsP4->eta(),  evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltaphi_,  recHiggsP4.phi()  - genHiggsP4->phi(),  evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltamass_, recHiggsP4.mass() - genHiggsP4->mass(), evtWeight, evtWeightErr);
  }
}
