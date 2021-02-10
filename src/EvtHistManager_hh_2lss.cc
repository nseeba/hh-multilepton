#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_2lss.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <TMath.h> // TMath::Pi()

EvtHistManager_hh_2lss::EvtHistManager_hh_2lss(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["numJetsPtGt40"] = { "central" };
  central_or_shiftOptions_["dihiggsVisMass"] = { "*" };
  central_or_shiftOptions_["dihiggsMass_wMet"] = { "central" };
  central_or_shiftOptions_["jetMass"] = { "central" };
  central_or_shiftOptions_["leptonPairMass"] = { "central" };
  central_or_shiftOptions_["electronPairMass"] = { "central" };
  central_or_shiftOptions_["muonPairMass"] = { "central" };
  central_or_shiftOptions_["leptonPairCharge"] = { "central" };
  central_or_shiftOptions_["met"] = { "central" };
  central_or_shiftOptions_["mht"] = { "central" };
  central_or_shiftOptions_["met_LD"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };

  central_or_shiftOptions_["lep1_conePt"] = { "central" };
  central_or_shiftOptions_["mindr_lep1_jet"] = { "central" };
  central_or_shiftOptions_["mT_lep1"] = { "central" };
  central_or_shiftOptions_["dPhi_lep1_met"] = { "central" };
  central_or_shiftOptions_["dPhi_lep1_mht"] = { "central" };

  central_or_shiftOptions_["lep2_conePt"] = { "central" };
  central_or_shiftOptions_["mindr_lep2_jet"] = { "central" };
  central_or_shiftOptions_["mT_lep2"] = { "central" };
  central_or_shiftOptions_["dPhi_lep2_met"] = { "central" };
  central_or_shiftOptions_["dPhi_lep2_mht"] = { "central" };

  central_or_shiftOptions_["dR_ll"] = { "central" };
  central_or_shiftOptions_["max_lep_eta"] = { "central" };
}

const TH1 *
EvtHistManager_hh_2lss::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_2lss::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_     = book1D(dir, "numElectrons",     "numElectrons",       5, -0.5,  +4.5);
  histogram_numMuons_         = book1D(dir, "numMuons",         "numMuons",           5, -0.5,  +4.5);
  histogram_numJets_          = book1D(dir, "numJets",          "numJets",           20, -0.5, +19.5);
  histogram_numJetsPtGt40_    = book1D(dir, "numJetsPtGt40",    "numJetsPtGt40",     20, -0.5, +19.5);
  histogram_dihiggsVisMass_   = book1D(dir, "dihiggsVisMass",   "dihiggsVisMass",   150,  0., 1500.);
  histogram_dihiggsMass_wMet_ = book1D(dir, "dihiggsMass_wMet", "dihiggsMass_wMet", 150,  0., 1500.);
  histogram_jetMass_          = book1D(dir, "jetMass",          "jetMass",          150,  0., 1500.);
  histogram_leptonPairMass_   = book1D(dir, "leptonPairMass",   "leptonPairMass",   100,  0.,  200.);
  histogram_electronPairMass_ = book1D(dir, "electronPairMass", "electronPairMass", 100,  0.,  200.);
  histogram_muonPairMass_     = book1D(dir, "muonPairMass",     "muonPairMass",     100,  0.,  200.);
  histogram_leptonPairCharge_ = book1D(dir, "leptonPairCharge", "leptonPairCharge",   5, -2.5,  +2.5);
  histogram_met_              = book1D(dir, "met",              "met",               200, 0,500);
  histogram_mht_              = book1D(dir, "mht",              "mht",               200, 0,500);
  histogram_met_LD_           = book1D(dir, "met_LD",           "met_LD",            200, 0,500);
  histogram_HT_               = book1D(dir, "HT",               "HT",               150,  0., 1500.);
  histogram_STMET_            = book1D(dir, "STMET",            "STMET",            150,  0., 1500.);
  histogram_EventCounter_     = book1D(dir, "EventCounter",     "EventCounter",       1, -0.5,  +0.5);

  histogram_lep1_conePt_      = book1D(dir, "lep1_conePt",      "lep1_conePt",      150, 0, 300);
  histogram_mindr_lep1_jet_   = book1D(dir, "mindr_lep1_jet",   "mindr_lep1_jet",   100, 0,   7);
  histogram_mT_lep1_          = book1D(dir, "mT_lep1",          "mT_lep1",          200, 0, 500);
  histogram_dPhi_lep1_met_    = book1D(dir, "dPhi_lep1_met",    "dPhi_lep1_met",     36, 0., TMath::Pi());
  histogram_dPhi_lep1_mht_    = book1D(dir, "dPhi_lep1_mht",    "dPhi_lep1_mht",     36, 0., TMath::Pi());

  histogram_lep2_conePt_      = book1D(dir, "lep2_conePt",      "lep2_conePt",      150, 0, 300);
  histogram_mindr_lep2_jet_   = book1D(dir, "mindr_lep2_jet",   "mindr_lep2_jet",   100, 0,   7);
  histogram_mT_lep2_          = book1D(dir, "mT_lep2",          "mT_lep2",          200, 0, 500);
  histogram_dPhi_lep2_met_    = book1D(dir, "dPhi_lep2_met",    "dPhi_lep2_met",     36, 0., TMath::Pi());
  histogram_dPhi_lep2_mht_    = book1D(dir, "dPhi_lep2_mht",    "dPhi_lep2_mht",     36, 0., TMath::Pi());

  histogram_dR_ll_            = book1D(dir, "dR_ll",            "dR_ll",            100, 0,   7);
  histogram_max_lep_eta_      = book1D(dir, "max_lep_eta",      "max_lep_eta",      100, 0, 2.5);
 
}

void
EvtHistManager_hh_2lss::fillHistograms(int numElectrons,
				       int numMuons,
				       int numJets,
				       int numJetsPtGt40,
				       double dihiggsVisMass,
				       double dihiggsMass_wMet,
				       double jetMass,
				       double leptonPairMass,
				       double electronPairMass,
				       double muonPairMass,
				       double leptonPairCharge,
				       double met,
				       double mht,
				       double met_LD,
				       double HT,
				       double STMET,
				       //
				       double lep1_conePt,
				       double mindr_lep1_jet,
				       double mT_lep1,
                                       double dPhi_lep1_met,
                                       double dPhi_lep1_mht,
				       //
				       double lep2_conePt,
				       double mindr_lep2_jet,
				       double mT_lep2,
                                       double dPhi_lep2_met,
                                       double dPhi_lep2_mht,
				       //
				       double dR_ll,
				       double max_lep_eta,
				       //		 
				       double evtWeight)
{
  const double evtWeightErr = 0.;
  fillWithOverFlow(histogram_numElectrons_,     numElectrons,     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,         numMuons,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,          numJets,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsPtGt40_,    numJetsPtGt40,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dihiggsVisMass_,   dihiggsVisMass,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dihiggsMass_wMet_, dihiggsMass_wMet, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_jetMass_,          jetMass,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_leptonPairMass_,   leptonPairMass,   evtWeight, evtWeightErr);
  if ( electronPairMass > 0. ) {
    fillWithOverFlow(histogram_electronPairMass_, electronPairMass, evtWeight, evtWeightErr);
  }
  if ( muonPairMass > 0. ) {
    fillWithOverFlow(histogram_muonPairMass_,     muonPairMass,     evtWeight, evtWeightErr);
  }
  fillWithOverFlow(histogram_leptonPairCharge_, leptonPairCharge, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_met_,              met,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mht_,              mht,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_met_LD_,           met_LD,           evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_HT_,               HT,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,            STMET,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_,     0.,               evtWeight, evtWeightErr);
  //
  fillWithOverFlow(histogram_lep1_conePt_,      lep1_conePt,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mindr_lep1_jet_,   mindr_lep1_jet,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_lep1_,          mT_lep1,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_lep1_met_,    dPhi_lep1_met,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_lep1_mht_,    dPhi_lep1_mht,    evtWeight, evtWeightErr);
  //
  fillWithOverFlow(histogram_lep2_conePt_,      lep2_conePt,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mindr_lep2_jet_,   mindr_lep2_jet,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_lep2_,          mT_lep2,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_lep2_met_,    dPhi_lep2_met,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_lep2_mht_,    dPhi_lep2_mht,    evtWeight, evtWeightErr);
  //
  fillWithOverFlow(histogram_dR_ll_,            dR_ll,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_max_lep_eta_,      max_lep_eta,      evtWeight, evtWeightErr);
}
