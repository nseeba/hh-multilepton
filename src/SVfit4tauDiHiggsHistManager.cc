#include "hhAnalysis/tttt/interface/SVfit4tauDiHiggsHistManager.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()

#include <TMath.h> // TMath::Pi()

SVfit4tauDiHiggsHistManager::SVfit4tauDiHiggsHistManager(const edm::ParameterSet& cfg)
  : HistManagerBase(cfg)
{}

void SVfit4tauDiHiggsHistManager::bookHistograms(TFileDirectory& dir)
{
  histogram_pt_        = book1D(dir, "pt",        "pt",        200,    0.,  1000.);
  histogram_eta_       = book1D(dir, "eta",       "eta",        46,   -2.3,   +2.3);
  histogram_phi_       = book1D(dir, "phi",       "phi",        36, -TMath::Pi(), +TMath::Pi());
  histogram_mass_      = book1D(dir, "mass",      "mass",      400,    0.,  2000.);

  histogram_deltapt_   = book1D(dir, "deltapt",   "deltapt",   200, -100.,  +100.);
  histogram_deltaeta_  = book1D(dir, "deltaeta",  "deltaeta",   80,   -0.2,   +0.2);
  histogram_deltaphi_  = book1D(dir, "deltaphi",  "deltaphi",  200,   -0.5,   +0.5);
  histogram_deltamass_ = book1D(dir, "deltamass", "deltamass", 400, -200.,  +200.);
}

void
SVfit4tauDiHiggsHistManager::fillHistograms(const classic_svFit::LorentzVector& recDiHiggsP4, 
					    double evtWeight, const Particle::LorentzVector* genDiHiggsP4)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_pt_,   recDiHiggsP4.pt(),   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_eta_,  recDiHiggsP4.eta(),  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_phi_,  recDiHiggsP4.phi(),  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mass_, recDiHiggsP4.mass(), evtWeight, evtWeightErr);

  if ( genDiHiggsP4 ) {
    fillWithOverFlow(histogram_deltapt_,   recDiHiggsP4.pt()   - genDiHiggsP4->pt(),   evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltaeta_,  recDiHiggsP4.eta()  - genDiHiggsP4->eta(),  evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltaphi_,  recDiHiggsP4.phi()  - genDiHiggsP4->phi(),  evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_deltamass_, recDiHiggsP4.mass() - genDiHiggsP4->mass(), evtWeight, evtWeightErr);
  }
}
