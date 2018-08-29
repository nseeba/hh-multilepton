#include "hhAnalysis/tttt/interface/SVfit4tauResolutionHistManager_MarkovChain.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()

#include <TMath.h> // TMath::Pi()

SVfit4tauResolutionHistManager_MarkovChain::SVfit4tauResolutionHistManager_MarkovChain(const edm::ParameterSet& cfg)
  : HistManagerBase(cfg)
{}

void SVfit4tauResolutionHistManager_MarkovChain::bookHistograms(TFileDirectory& dir)
{
  histogram_dihiggsPt1_           = book1D(dir, "dihiggsPt1",           "dihiggsPt1",           200,    0.,  1000.);
  histogram_dihiggsEta1_          = book1D(dir, "dihiggsEta1",          "dihiggsEta1",           46,   -2.3,   +2.3);
  histogram_dihiggsPhi1_          = book1D(dir, "dihiggsPhi1",          "dihiggsPhi1",           36, -TMath::Pi(), +TMath::Pi());
  histogram_ditau1Pt1_            = book1D(dir, "ditau1Pt1",            "ditau1Pt1",            200,    0.,  1000.);
  histogram_ditau1Eta1_           = book1D(dir, "ditau1Eta1",           "ditau1Eta1",            46,   -2.3,   +2.3);
  histogram_ditau1Phi1_           = book1D(dir, "ditau1Phi1",           "ditau1Phi1",            36, -TMath::Pi(), +TMath::Pi());
  histogram_ditau2Pt1_            = book1D(dir, "ditau2Pt1",            "ditau2Pt1",            200,    0.,  1000.);
  histogram_ditau2Eta1_           = book1D(dir, "ditau2Eta1",           "ditau2Eta1",            46,   -2.3,   +2.3);
  histogram_ditau2Phi1_           = book1D(dir, "ditau2Phi1",           "ditau2Phi1",            36, -TMath::Pi(), +TMath::Pi());
  
  histogram_dihiggsDeltaMass1_    = book1D(dir, "dihiggsDeltaMass1",    "dihiggsDeltaMass1",    400, -200.,  +200.);
  histogram_dihiggsRatioVisMass1_ = book1D(dir, "dihiggsRatioVisMass1", "dihiggsRatioVisMass1", 200,    0.,    10.);
  histogram_dihiggsRatioMass1_    = book1D(dir, "dihiggsRatioMass1",    "dihiggsRatioMass1",    200,    0.,    10.);
  histogram_ditau1DeltaMass1_     = book1D(dir, "ditau1DeltaMass1",     "ditau1DeltaMass1",     400, -200.,  +200.);
  histogram_ditau1RatioVisMass1_  = book1D(dir, "ditau1RatioVisMass1",  "ditau1RatioVisMass1",  200,    0.,    10.);
  histogram_ditau1RatioMass1_     = book1D(dir, "ditau1RatioMass1",     "ditau1RatioMass1",     200,    0.,    10.);
  histogram_ditau2DeltaMass1_     = book1D(dir, "ditau2DeltaMass1",     "ditau2DeltaMass1",     400, -200.,  +200.);
  histogram_ditau2RatioVisMass1_  = book1D(dir, "ditau2RatioVisMass1",  "ditau2RatioVisMass1",  200,    0.,    10.);
  histogram_ditau2RatioMass1_     = book1D(dir, "ditau2RatioMass1",     "ditau2RatioMass1",     200,    0.,    10.);
  
  histogram_dihiggsDeltaPt1_      = book1D(dir, "dihiggsDeltaPt1",      "dihiggsDeltaPt1",      200, -100.,  +100.);
  histogram_dihiggsDeltaEta1_     = book1D(dir, "dihiggsDeltaEta1",     "dihiggsDeltaEta1",      80,   -0.2,   +0.2);
  histogram_dihiggsDeltaPhi1_     = book1D(dir, "dihiggsDeltaPhi1",     "dihiggsDeltaPhi1",     200,   -0.5,   +0.5);
  histogram_ditau1DeltaPt1_       = book1D(dir, "ditau1DeltaPt1",       "ditau1DeltaPt1",       200, -100.,  +100.);
  histogram_ditau1DeltaEta1_      = book1D(dir, "ditau1DeltaEta1",      "ditau1DeltaEta1",       80,   -0.2,   +0.2);
  histogram_ditau1DeltaPhi1_      = book1D(dir, "ditau1DeltaPhi1",      "ditau1DeltaPhi1",      200,   -0.5,   +0.5);
  histogram_ditau2DeltaPt1_       = book1D(dir, "ditau2DeltaPt1",       "ditau2PDeltat1",       200, -100.,  +100.);
  histogram_ditau2DeltaEta1_      = book1D(dir, "ditau2DeltaEta1",      "ditau2DeltaEta1",       80,   -0.2,   +0.2);
  histogram_ditau2DeltaPhi1_      = book1D(dir, "ditau2DeltaPhi1",      "ditau2DeltaPhi1",      200,   -0.5,   +0.5);

  histogram_dihiggsPt2_           = book1D(dir, "dihiggsPt2",           "dihiggsPt2",           200,    0.,  1000.);
  histogram_dihiggsEta2_          = book1D(dir, "dihiggsEta2",          "dihiggsEta2",           46,   -2.3,   +2.3);
  histogram_dihiggsPhi2_          = book1D(dir, "dihiggsPhi2",          "dihiggsPhi2",           36, -TMath::Pi(), +TMath::Pi());
  histogram_ditau1Pt2_            = book1D(dir, "ditau1Pt2",            "ditau1Pt2",            200,    0.,  1000.);
  histogram_ditau1Eta2_           = book1D(dir, "ditau1Eta2",           "ditau1Eta2",            46,   -2.3,   +2.3);
  histogram_ditau1Phi2_           = book1D(dir, "ditau1Phi2",           "ditau1Phi2",            36, -TMath::Pi(), +TMath::Pi());
  histogram_ditau2Pt2_            = book1D(dir, "ditau2Pt2",            "ditau2Pt2",            200,    0.,  1000.);
  histogram_ditau2Eta2_           = book1D(dir, "ditau2Eta2",           "ditau2Eta2",            46,   -2.3,   +2.3);
  histogram_ditau2Phi2_           = book1D(dir, "ditau2Phi2",           "ditau2Phi2",            36, -TMath::Pi(), +TMath::Pi());
  
  histogram_dihiggsDeltaMass2_    = book1D(dir, "dihiggsDeltaMass2",    "dihiggsDeltaMass2",    400, -200.,  +200.);
  histogram_dihiggsRatioVisMass2_ = book1D(dir, "dihiggsRatioVisMass2", "dihiggsRatioVisMass2", 200,    0.,    10.);
  histogram_dihiggsRatioMass2_    = book1D(dir, "dihiggsRatioMass2",    "dihiggsRatioMass2",    200,    0.,    10.);
  histogram_ditau1DeltaMass2_     = book1D(dir, "ditau1DeltaMass2",     "ditau1DeltaMass2",     400, -200.,  +200.);
  histogram_ditau1RatioVisMass2_  = book1D(dir, "ditau1RatioVisMass2",  "ditau1RatioVisMass2",  200,    0.,    10.);
  histogram_ditau1RatioMass2_     = book1D(dir, "ditau1RatioMass2",     "ditau1RatioMass2",     200,    0.,    10.);
  histogram_ditau2DeltaMass2_     = book1D(dir, "ditau2DeltaMass2",     "ditau2DeltaMass2",     400, -200.,  +200.);
  histogram_ditau2RatioVisMass2_  = book1D(dir, "ditau2RatioVisMass2",  "ditau2RatioVisMass2",  200,    0.,    10.);
  histogram_ditau2RatioMass2_     = book1D(dir, "ditau2RatioMass2",     "ditau2RatioMass2",     200,    0.,    10.);
  
  histogram_dihiggsDeltaPt2_      = book1D(dir, "dihiggsDeltaPt2",      "dihiggsDeltaPt2",      200, -100.,  +100.);
  histogram_dihiggsDeltaEta2_     = book1D(dir, "dihiggsDeltaEta2",     "dihiggsDeltaEta2",      80,   -0.2,   +0.2);
  histogram_dihiggsDeltaPhi2_     = book1D(dir, "dihiggsDeltaPhi2",     "dihiggsDeltaPhi2",     200,   -0.5,   +0.5);
  histogram_ditau1DeltaPt2_       = book1D(dir, "ditau1DeltaPt2",       "ditau1DeltaPt2",       200, -100.,  +100.);
  histogram_ditau1DeltaEta2_      = book1D(dir, "ditau1DeltaEta2",      "ditau1DeltaEta2",       80,   -0.2,   +0.2);
  histogram_ditau1DeltaPhi2_      = book1D(dir, "ditau1DeltaPhi2",      "ditau1DeltaPhi2",      200,   -0.5,   +0.5);
  histogram_ditau2DeltaPt2_       = book1D(dir, "ditau2DeltaPt2",       "ditau2PDeltat2",       200, -100.,  +100.);
  histogram_ditau2DeltaEta2_      = book1D(dir, "ditau2DeltaEta2",      "ditau2DeltaEta2",       80,   -0.2,   +0.2);
  histogram_ditau2DeltaPhi2_      = book1D(dir, "ditau2DeltaPhi2",      "ditau2DeltaPhi2",      200,   -0.5,   +0.5);
}

namespace
{
  void fillSVfit4tauResolutionHistograms(const SVfit4tauResult& result,
					 const Particle::LorentzVector* genDiHiggsP4, 
					 const Particle::LorentzVector* genDiTau1P4, 
					 const Particle::LorentzVector* genDiTau2P4, 
					 TH1* histogram_dihiggsPt, TH1* histogram_dihiggsEta, TH1* histogram_dihiggsPhi,
					 TH1* histogram_ditau1Pt, TH1* histogram_ditau1Eta, TH1* histogram_ditau1Phi,
					 TH1* histogram_ditau2Pt, TH1* histogram_ditau2Eta, TH1* histogram_ditau2Phi,
					 TH1* histogram_dihiggsDeltaMass, TH1* histogram_dihiggsRatioVisMass, TH1* histogram_dihiggsRatioMass,
					 TH1* histogram_ditau1DeltaMass, TH1* histogram_ditau1RatioVisMass, TH1* histogram_ditau1RatioMass, 
					 TH1* histogram_ditau2DeltaMass, TH1* histogram_ditau2RatioVisMass, TH1* histogram_ditau2RatioMass,
					 TH1* histogram_dihiggsDeltaPt, TH1* histogram_dihiggsDeltaEta, TH1* histogram_dihiggsDeltaPhi,
					 TH1* histogram_ditau1DeltaPt, TH1* histogram_ditau1DeltaEta, TH1* histogram_ditau1DeltaPhi,
					 TH1* histogram_ditau2DeltaPt, TH1* histogram_ditau2DeltaEta, TH1* histogram_ditau2DeltaPhi,
					 double evtWeight, double evtWeightErr)
  {
    fillWithOverFlow(histogram_dihiggsPt,             result.dihiggs_pt_,                           evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_dihiggsEta,            result.dihiggs_eta_,                          evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_dihiggsPhi,            result.dihiggs_phi_,                          evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau1Pt,              result.ditau1_pt_,                            evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau1Eta,             result.ditau1_eta_,                           evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau1Phi,             result.ditau1_phi_,                           evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau2Pt,              result.ditau2_pt_,                            evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau2Eta,             result.ditau2_eta_,                           evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau2Phi,             result.ditau2_phi_,                           evtWeight, evtWeightErr);

    assert(genDiHiggsP4 && genDiTau1P4 && genDiTau2P4);

    fillWithOverFlow(histogram_dihiggsDeltaMass,      result.dihiggs_mass_ - genDiHiggsP4->mass(),  evtWeight, evtWeightErr);
    if ( genDiHiggsP4->mass() > 50. ) {
      fillWithOverFlow(histogram_dihiggsRatioVisMass, result.dihiggs_visMass_/genDiHiggsP4->mass(), evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_dihiggsRatioMass,    result.dihiggs_mass_/genDiHiggsP4->mass(),    evtWeight, evtWeightErr);
    }
    fillWithOverFlow(histogram_ditau1DeltaMass,       result.ditau1_mass_ - genDiTau1P4->mass(),    evtWeight, evtWeightErr);
    if ( genDiTau1P4->mass() > 50. ) {
      fillWithOverFlow(histogram_ditau1RatioVisMass,  result.ditau1_visMass_/genDiTau1P4->mass(),   evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_ditau1RatioMass,     result.ditau1_mass_/genDiTau1P4->mass(),      evtWeight, evtWeightErr);
    }
    fillWithOverFlow(histogram_ditau2DeltaMass,       result.ditau2_mass_ - genDiTau2P4->mass(),    evtWeight, evtWeightErr);
    if ( genDiTau2P4->mass() > 50. ) {
      fillWithOverFlow(histogram_ditau2RatioVisMass,  result.ditau2_visMass_/genDiTau2P4->mass(),   evtWeight, evtWeightErr);
      fillWithOverFlow(histogram_ditau2RatioMass,     result.ditau2_mass_/genDiTau2P4->mass(),      evtWeight, evtWeightErr);
    }
    
    fillWithOverFlow(histogram_dihiggsDeltaPt,        result.dihiggs_pt_ - genDiHiggsP4->pt(),      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_dihiggsDeltaEta,       result.dihiggs_eta_ - genDiHiggsP4->eta(),    evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_dihiggsDeltaPhi,       result.dihiggs_phi_ - genDiHiggsP4->phi(),    evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau1DeltaPt,         result.ditau1_pt_ - genDiTau1P4->pt(),        evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau1DeltaEta,        result.ditau1_eta_ - genDiTau1P4->eta(),      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau1DeltaPhi,        result.ditau1_phi_ - genDiTau1P4->phi(),      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau2DeltaPt,         result.ditau2_pt_ - genDiTau2P4->pt(),        evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau2DeltaEta,        result.ditau2_eta_ - genDiTau2P4->eta(),      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_ditau2DeltaPhi,        result.ditau2_phi_ - genDiTau2P4->phi(),      evtWeight, evtWeightErr);
  }
}

void
SVfit4tauResolutionHistManager_MarkovChain::fillHistograms(const std::vector<SVfit4tauResult>& results,
							   const Particle::LorentzVector* genDiHiggsP4, 
							   const Particle::LorentzVector* genDiTau1P4, 
							   const Particle::LorentzVector* genDiTau2P4, 
							   double evtWeight)
{
  const double evtWeightErr = 0.;
  
  if ( !(genDiHiggsP4 && genDiTau1P4 && genDiTau2P4) ) return;

  if ( results.size() >= 1 ) {
    const SVfit4tauResult& result1 = results[0];
    if ( result1.isValidSolution_ ) {
      fillSVfit4tauResolutionHistograms(
        result1, 
	genDiHiggsP4, genDiTau1P4, genDiTau2P4,
	histogram_dihiggsPt1_, histogram_dihiggsEta1_, histogram_dihiggsPhi1_,
	histogram_ditau1Pt1_, histogram_ditau1Eta1_, histogram_ditau1Phi1_,
	histogram_ditau2Pt1_, histogram_ditau2Eta1_, histogram_ditau2Phi1_,
	histogram_dihiggsDeltaMass1_, histogram_dihiggsRatioVisMass1_, histogram_dihiggsRatioMass1_,
	histogram_ditau1DeltaMass1_, histogram_ditau1RatioVisMass1_, histogram_ditau1RatioMass1_,
	histogram_ditau2DeltaMass1_, histogram_ditau2RatioVisMass1_, histogram_ditau2RatioMass1_,
	histogram_dihiggsDeltaPt1_, histogram_dihiggsDeltaEta1_, histogram_dihiggsDeltaPhi1_,
	histogram_ditau1DeltaPt1_, histogram_ditau1DeltaEta1_, histogram_ditau1DeltaPhi1_,
	histogram_ditau2DeltaPt1_, histogram_ditau2DeltaEta1_, histogram_ditau2DeltaPhi1_,
	evtWeight, evtWeightErr);
    }
  }

  if ( results.size() >= 2 ) {
    const SVfit4tauResult& result2 = results[1];
    if ( result2.isValidSolution_ ) {
      fillSVfit4tauResolutionHistograms(
        result2, 
	genDiHiggsP4, genDiTau1P4, genDiTau2P4,
	histogram_dihiggsPt2_, histogram_dihiggsEta2_, histogram_dihiggsPhi2_,
	histogram_ditau1Pt2_, histogram_ditau1Eta2_, histogram_ditau1Phi2_,
	histogram_ditau2Pt2_, histogram_ditau2Eta2_, histogram_ditau2Phi2_,
	histogram_dihiggsDeltaMass2_, histogram_dihiggsRatioVisMass2_, histogram_dihiggsRatioMass2_,
	histogram_ditau1DeltaMass2_, histogram_ditau1RatioVisMass2_, histogram_ditau1RatioMass2_,
	histogram_ditau2DeltaMass2_, histogram_ditau2RatioVisMass2_, histogram_ditau2RatioMass2_,
	histogram_dihiggsDeltaPt2_, histogram_dihiggsDeltaEta2_, histogram_dihiggsDeltaPhi2_,
	histogram_ditau1DeltaPt2_, histogram_ditau1DeltaEta2_, histogram_ditau1DeltaPhi2_,
	histogram_ditau2DeltaPt2_, histogram_ditau2DeltaEta2_, histogram_ditau2DeltaPhi2_,
	evtWeight, evtWeightErr);
    }
  }
}
