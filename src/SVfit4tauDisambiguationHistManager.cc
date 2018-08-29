#include "hhAnalysis/tttt/interface/SVfit4tauDisambiguationHistManager.h"

#include "DataFormats/Math/interface/deltaPhi.h" // deltaPhi
#include "DataFormats/Math/interface/deltaR.h" // deltaR

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Log

SVfit4tauDisambiguationHistManager::SVfit4tauDisambiguationHistManager(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{}

void
SVfit4tauDisambiguationHistManager::bookHistograms(TFileDirectory & dir)
{
  histogram_dihiggsMass_    = book2D(dir, "dihiggsMass",    "dihiggsMass",    150,   0., 1500., 150,   0., 1500.);
  histogram_dihiggsMassErr_ = book2D(dir, "dihiggsMassErr", "dihiggsMassErr", 150,   0.,  150., 150,   0.,  150.);
  histogram_dihiggsPt_      = book2D(dir, "dihiggsPt",      "dihiggsPt",      200,   0., 1000., 200,   0., 1000.);
  histogram_logLmax_        = book2D(dir, "logLmax",        "logLmax",        200, -50.,  +50., 200, -50.,  +50.);

  histogram_avDeltaPhi_     = book2D(dir, "avDeltaPhi",     "avDeltaPhi",      50,   0.,    5.,  50,   0.,    5.);
  histogram_avDeltaEta_     = book2D(dir, "avDeltaEta",     "avDeltaEta",      50,   0.,    5.,  50,   0.,    5.);
  histogram_avDeltaR_       = book2D(dir, "avDeltaR",       "avDeltaR",        50,   0.,    5.,  50,   0.,    5.);

  histogram_avDiTauVisPt_   = book2D(dir, "avDiTauVisPt",   "avDiTauVisPt",   200,   0., 1000., 200,   0., 1000.);
  histogram_avDiTauPt_      = book2D(dir, "avDiTauPt",      "avDiTauPt",      200,   0., 1000., 200,   0., 1000.);
}

namespace
{
  double compAvDeltaPhi(const Particle::LorentzVector& measuredTau1Higgs1P4, const Particle::LorentzVector& measuredTau2Higgs1P4,
			const Particle::LorentzVector& measuredTau1Higgs2P4, const Particle::LorentzVector& measuredTau2Higgs2P4) 
  {
    double retVal = 0.5*(TMath::Abs(reco::deltaPhi(measuredTau1Higgs1P4.phi(), measuredTau2Higgs1P4.phi())) + TMath::Abs(deltaPhi(measuredTau1Higgs2P4.phi(), measuredTau2Higgs2P4.phi())));
    return retVal;
  }
  double compAvDeltaEta(const Particle::LorentzVector& measuredTau1Higgs1P4, const Particle::LorentzVector& measuredTau2Higgs1P4,
			const Particle::LorentzVector& measuredTau1Higgs2P4, const Particle::LorentzVector& measuredTau2Higgs2P4) 
  {
    double retVal = 0.5*(TMath::Abs(measuredTau1Higgs1P4.eta() - measuredTau2Higgs1P4.eta()) + TMath::Abs(measuredTau1Higgs2P4.eta() - measuredTau2Higgs2P4.eta()));
    return retVal;
  }
  double compAvDeltaR(const Particle::LorentzVector& measuredTau1Higgs1P4, const Particle::LorentzVector& measuredTau2Higgs1P4,
		      const Particle::LorentzVector& measuredTau1Higgs2P4, const Particle::LorentzVector& measuredTau2Higgs2P4) 
  {
    double retVal = 0.5*(reco::deltaR(measuredTau1Higgs1P4, measuredTau2Higgs1P4) + reco::deltaR(measuredTau1Higgs2P4, measuredTau2Higgs2P4));
    return retVal;
  }
  double compAvDiTauVisPt(const Particle::LorentzVector& measuredTau1Higgs1P4, const Particle::LorentzVector& measuredTau2Higgs1P4,
			  const Particle::LorentzVector& measuredTau1Higgs2P4, const Particle::LorentzVector& measuredTau2Higgs2P4) 
  {
    double retVal = 0.5*((measuredTau1Higgs1P4 + measuredTau2Higgs1P4).pt() + (measuredTau1Higgs2P4 + measuredTau2Higgs2P4).pt());
    return retVal;
  }
}

void
SVfit4tauDisambiguationHistManager::fillHistograms(const SVfit4tauResult& result_correctAssoc,
						   const Particle::LorentzVector& measuredTau1Higgs1P4_correctAssoc,
						   const Particle::LorentzVector& measuredTau2Higgs1P4_correctAssoc,
						   const Particle::LorentzVector& measuredTau1Higgs2P4_correctAssoc,
						   const Particle::LorentzVector& measuredTau2Higgs2P4_correctAssoc,
						   const SVfit4tauResult& result_incorrectAssoc,
						   const Particle::LorentzVector& measuredTau1Higgs1P4_incorrectAssoc,
						   const Particle::LorentzVector& measuredTau2Higgs1P4_incorrectAssoc,
						   const Particle::LorentzVector& measuredTau1Higgs2P4_incorrectAssoc,
						   const Particle::LorentzVector& measuredTau2Higgs2P4_incorrectAssoc,
						   double evtWeight)
{
  const double evtWeightErr = 0.;

  if ( result_correctAssoc.isValidSolution_ && result_incorrectAssoc.isValidSolution_ ) {
    fillWithOverFlow2d(histogram_dihiggsMass_, result_correctAssoc.dihiggs_mass_, result_incorrectAssoc.dihiggs_mass_, evtWeight, evtWeightErr);
    fillWithOverFlow2d(histogram_dihiggsMassErr_, result_correctAssoc.dihiggs_massErr_, result_incorrectAssoc.dihiggs_massErr_, evtWeight, evtWeightErr);
    if ( result_correctAssoc.dihiggs_pt_ > 0. && result_incorrectAssoc.dihiggs_pt_ > 0. ) {
      fillWithOverFlow2d(histogram_dihiggsPt_, result_correctAssoc.dihiggs_pt_, result_incorrectAssoc.dihiggs_pt_, evtWeight, evtWeightErr);
    }
    if ( result_correctAssoc.Lmax_   > 0. && 
	 result_incorrectAssoc.Lmax_ > 0. ) {
      fillWithOverFlow2d(histogram_logLmax_, TMath::Log(result_correctAssoc.Lmax_), TMath::Log(result_incorrectAssoc.Lmax_), evtWeight, evtWeightErr);
    }
    double avDeltaPhi_correctAssoc = compAvDeltaPhi(
      measuredTau1Higgs1P4_correctAssoc, measuredTau2Higgs1P4_correctAssoc, 
      measuredTau1Higgs2P4_correctAssoc, measuredTau2Higgs2P4_correctAssoc);
    double avDeltaPhi_incorrectAssoc = compAvDeltaPhi(
      measuredTau1Higgs1P4_incorrectAssoc, measuredTau2Higgs1P4_incorrectAssoc, 
      measuredTau1Higgs2P4_incorrectAssoc, measuredTau2Higgs2P4_incorrectAssoc);
    fillWithOverFlow2d(histogram_avDeltaPhi_, avDeltaPhi_correctAssoc, avDeltaPhi_incorrectAssoc, evtWeight, evtWeightErr);
    double avDeltaEta_correctAssoc = compAvDeltaEta(
      measuredTau1Higgs1P4_correctAssoc, measuredTau2Higgs1P4_correctAssoc, 
      measuredTau1Higgs2P4_correctAssoc, measuredTau2Higgs2P4_correctAssoc);
    double avDeltaEta_incorrectAssoc = compAvDeltaEta(
      measuredTau1Higgs1P4_incorrectAssoc, measuredTau2Higgs1P4_incorrectAssoc, 
      measuredTau1Higgs2P4_incorrectAssoc, measuredTau2Higgs2P4_incorrectAssoc);
    fillWithOverFlow2d(histogram_avDeltaEta_, avDeltaEta_correctAssoc, avDeltaEta_incorrectAssoc, evtWeight, evtWeightErr);
    double avDeltaR_correctAssoc = compAvDeltaR(
      measuredTau1Higgs1P4_correctAssoc, measuredTau2Higgs1P4_correctAssoc, 
      measuredTau1Higgs2P4_correctAssoc, measuredTau2Higgs2P4_correctAssoc);
    double avDeltaR_incorrectAssoc = compAvDeltaR(
      measuredTau1Higgs1P4_incorrectAssoc, measuredTau2Higgs1P4_incorrectAssoc, 
      measuredTau1Higgs2P4_incorrectAssoc, measuredTau2Higgs2P4_incorrectAssoc);
    fillWithOverFlow2d(histogram_avDeltaR_, avDeltaR_correctAssoc, avDeltaR_incorrectAssoc, evtWeight, evtWeightErr);
    double avDiTauVisPt_correctAssoc = compAvDiTauVisPt(
      measuredTau1Higgs1P4_correctAssoc, measuredTau2Higgs1P4_correctAssoc, 
      measuredTau1Higgs2P4_correctAssoc, measuredTau2Higgs2P4_correctAssoc);
    double avDiTauVisPt_incorrectAssoc = compAvDiTauVisPt(
      measuredTau1Higgs1P4_incorrectAssoc, measuredTau2Higgs1P4_incorrectAssoc, 
      measuredTau1Higgs2P4_incorrectAssoc, measuredTau2Higgs2P4_incorrectAssoc);
    fillWithOverFlow2d(histogram_avDiTauVisPt_, avDiTauVisPt_correctAssoc, avDiTauVisPt_incorrectAssoc, evtWeight, evtWeightErr);
    if ( result_correctAssoc.ditau1_pt_   > 0. && result_correctAssoc.ditau2_pt_   > 0. &&
	 result_incorrectAssoc.ditau1_pt_ > 0. && result_incorrectAssoc.ditau2_pt_ > 0. ) {
      double avDiTauPt_correctAssoc = 0.5*(result_correctAssoc.ditau1_pt_ + result_correctAssoc.ditau2_pt_);
      double avDiTauPt_incorrectAssoc = 0.5*(result_incorrectAssoc.ditau1_pt_ + result_incorrectAssoc.ditau2_pt_);
      fillWithOverFlow2d(histogram_avDiTauPt_, avDiTauPt_correctAssoc, avDiTauPt_incorrectAssoc, evtWeight, evtWeightErr);
    }
  }
}
