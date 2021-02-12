#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_2lss_leq1tau.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()
#include <TMath.h>

EvtHistManager_hh_2lss_leq1tau::EvtHistManager_hh_2lss_leq1tau(const edm::ParameterSet & cfg)
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
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };

  central_or_shiftOptions_["nElectrons_in_2lss"] = { "central" };
  central_or_shiftOptions_["dR_ll"] = { "central" };
  central_or_shiftOptions_["dPhi_ll"] = { "central" };
  
  central_or_shiftOptions_["nAK8_w2subjets"] = { "central" };
  central_or_shiftOptions_["nWJets_selected"] = { "central" }; 

  central_or_shiftOptions_["mass_2j_fromW1"] = { "central" };
  central_or_shiftOptions_["mass_2j_fromW2"] = { "central" };
  central_or_shiftOptions_["dR_2j_fromW1"] = { "central" };
  central_or_shiftOptions_["dR_2j_fromW2"] = { "central" };
  
  central_or_shiftOptions_["dR_Wjets_min"] = { "central" }; 
  central_or_shiftOptions_["dR_Wjets_max"] = { "central" };
  central_or_shiftOptions_["dR_l_Wjets_min"] = { "central" };
  central_or_shiftOptions_["dR_l_Wjets_max"] = { "central" };
  central_or_shiftOptions_["dR_l_AK4jets_min"] = { "central" };
  central_or_shiftOptions_["dR_l_AK4jets_max"] = { "central" }; 

  central_or_shiftOptions_["dR_l_leadWjet_min"] = { "central" };
  central_or_shiftOptions_["dR_l_leadWjet_max"] = { "central" };
  central_or_shiftOptions_["dR_l_leadAK4jet_min"] = { "central" };
  central_or_shiftOptions_["dR_l_leadAK4jet_max"] = { "central" };
  
  central_or_shiftOptions_["met"] = { "central" };
  central_or_shiftOptions_["mht"] = { "central" };
  central_or_shiftOptions_["met_LD"] = { "central" };

  central_or_shiftOptions_["mT_lep1_met"] = { "central" };
  central_or_shiftOptions_["mT_lep2_met"] = { "central" };

  central_or_shiftOptions_["eventCategory"] = { "central" };

  central_or_shiftOptions_["nTaus"] = { "central" }; 

  
}

const TH1 *
EvtHistManager_hh_2lss_leq1tau::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_2lss_leq1tau::bookHistograms(TFileDirectory & dir)
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
  histogram_HT_               = book1D(dir, "HT",               "HT",               150,  0., 1500.);
  histogram_STMET_            = book1D(dir, "STMET",            "STMET",            150,  0., 1500.);
  histogram_EventCounter_     = book1D(dir, "EventCounter",     "EventCounter",       1, -0.5,  +0.5);


  histogram_nElectrons_in_2lss_  = book1D(dir, "nElectrons_in_2lss",     "nElectrons_in_2lss",   3, -0.5,2.5);
  histogram_dR_ll_               = book1D(dir, "dR_ll",     "dR_ll",                           100, 0,   7);
  histogram_dPhi_ll_             = book1D(dir, "dPhi_ll",     "dPhi_ll",                       100, 0, TMath::Pi());
  //
  histogram_nAK8_w2subjets_      = book1D(dir, "nAK8_w2subjets",     "nAK8_w2subjets",           8, -0.5,7.5);
  histogram_nWJets_selected_     = book1D(dir, "nWJets_selected",     "nWJets_selected",         8, -0.5,7.5);
  //
  histogram_mass_2j_fromW1_      = book1D(dir, "mass_2j_fromW1",     "mass_2j_fromW1",         200, 0,  600);
  histogram_mass_2j_fromW2_      = book1D(dir, "mass_2j_fromW2",     "mass_2j_fromW2",         200, 0,  600);
  histogram_dR_2j_fromW1_        = book1D(dir, "dR_2j_fromW1",     "dR_2j_fromW1",             100, 0,   7);
  histogram_dR_2j_fromW2_        = book1D(dir, "dR_2j_fromW2",     "dR_2j_fromW2",             100, 0,   7);
  //
  histogram_dR_Wjets_min_        = book1D(dir, "dR_Wjets_min",         "dR_Wjets_min",         100, 0,   7);
  histogram_dR_Wjets_max_        = book1D(dir, "dR_Wjets_max",         "dR_Wjets_max",         100, 0,   7);
  histogram_dR_l_Wjets_min_      = book1D(dir, "dR_l_Wjets_min",       "dR_l_Wjets_min",       100, 0,   7);
  histogram_dR_l_Wjets_max_      = book1D(dir, "dR_l_Wjets_max",       "dR_l_Wjets_max",       100, 0,   7);
  histogram_dR_l_AK4jets_min_    = book1D(dir, "dR_l_AK4jets_min",     "dR_l_AK4jets_min",     100, 0,   7);
  histogram_dR_l_AK4jets_max_    = book1D(dir, "dR_l_AK4jets_max",     "dR_l_AK4jets_max",     100, 0,   7);
  histogram_dR_l_leadWjet_min_   = book1D(dir, "dR_l_leadWjet_min",    "dR_l_leadWjet_min",    100, 0,   7);
  histogram_dR_l_leadWjet_max_   = book1D(dir, "dR_l_leadWjet_max",    "dR_l_leadWjet_max",    100, 0,   7);
  histogram_dR_l_leadAK4jet_min_ = book1D(dir, "dR_l_leadAK4jet_min",  "dR_l_leadAK4jet_min",  100, 0,   7);
  histogram_dR_l_leadAK4jet_max_ = book1D(dir, "dR_l_leadAK4jet_max",  "dR_l_leadAK4jet_max",  100, 0,   7);
  //
  histogram_met_                 = book1D(dir, "met",                  "met",                  150, 0,500);
  histogram_mht_                 = book1D(dir, "mht",                  "mht",                  150, 0,500);
  histogram_met_LD_              = book1D(dir, "met_LD",               "met_LD",               150, 0,500);

  histogram_mT_lep1_met_         = book1D(dir, "mT_lep1_met",          "mT_lep1_met",          150, 0,500);
  histogram_mT_lep2_met_         = book1D(dir, "mT_lep2_met",          "mT_lep2_met",          150, 0,500);
  
  histogram_eventCategory_       = book1D(dir, "eventCategory",        "eventCategory",          3, 0.5,3.5);

  histogram_nTaus_               = book1D(dir, "nTaus",                "nTaus",                  3, -0.5,2.5);
}

void
EvtHistManager_hh_2lss_leq1tau::fillHistograms(int numElectrons,
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
				       double HT,
				       double STMET,
				       //
				       //
				       //
				       int nElectrons_in_2lss,
				       //leptonPairMass_sel,
				       //leptonPairCharge_sel,
				       double dR_ll,
				       double dPhi_ll,
				       //
				       //nAK4,
				       int nAK8_w2subjets,
				       int nWJets_selected,
				       //
				       double mass_2j_fromW1,
				       double mass_2j_fromW2,
				       double dR_2j_fromW1,
				       double dR_2j_fromW2,
				       //
				       double dR_Wjets_min,
				       double dR_Wjets_max,
				       double dR_l_Wjets_min,
				       double dR_l_Wjets_max,
				       double dR_l_AK4jets_min,
				       double dR_l_AK4jets_max,
				       double dR_l_leadWjet_min,
				       double dR_l_leadWjet_max,
				       double dR_l_leadAK4jet_min,
				       double dR_l_leadAK4jet_max,
				       //
				       double met,
				       double mht,
				       double met_LD,
				       //HT,
				       //STMET,
				       //
				       double mT_lep1_met,
				       double mT_lep2_met,
				       //
				       int eventCategory,
				       //
				       int nTaus,
				       //
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
  fillWithOverFlow(histogram_HT_,               HT,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,            STMET,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_,     0.,               evtWeight, evtWeightErr);




  fillWithOverFlow(histogram_nElectrons_in_2lss_, nElectrons_in_2lss, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_ll_, dR_ll, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_ll_, dPhi_ll, evtWeight, evtWeightErr);
  //
  fillWithOverFlow(histogram_nAK8_w2subjets_, nAK8_w2subjets, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_nWJets_selected_, nWJets_selected, evtWeight, evtWeightErr);
  //
  if (mass_2j_fromW1 > 0)
  fillWithOverFlow(histogram_mass_2j_fromW1_, mass_2j_fromW1, evtWeight, evtWeightErr);
  if (mass_2j_fromW2 > 0)
  fillWithOverFlow(histogram_mass_2j_fromW2_, mass_2j_fromW2, evtWeight, evtWeightErr);
  if (dR_2j_fromW1 > 0)
  fillWithOverFlow(histogram_dR_2j_fromW1_, dR_2j_fromW1, evtWeight, evtWeightErr);
  if (dR_2j_fromW2 > 0)
  fillWithOverFlow(histogram_dR_2j_fromW2_, dR_2j_fromW2, evtWeight, evtWeightErr);
  //
  if (dR_Wjets_min > 0)
  fillWithOverFlow(histogram_dR_Wjets_min_, dR_Wjets_min, evtWeight, evtWeightErr);
  if (dR_Wjets_max > 0)
  fillWithOverFlow(histogram_dR_Wjets_max_, dR_Wjets_max, evtWeight, evtWeightErr);
  if (dR_l_Wjets_min > 0)
  fillWithOverFlow(histogram_dR_l_Wjets_min_, dR_l_Wjets_min, evtWeight, evtWeightErr);
  if (dR_l_Wjets_max > 0)
  fillWithOverFlow(histogram_dR_l_Wjets_max_, dR_l_Wjets_max, evtWeight, evtWeightErr);
  if (dR_l_AK4jets_min > 0)
  fillWithOverFlow(histogram_dR_l_AK4jets_min_, dR_l_AK4jets_min, evtWeight, evtWeightErr);
  if (dR_l_AK4jets_max > 0)
  fillWithOverFlow(histogram_dR_l_AK4jets_max_, dR_l_AK4jets_max, evtWeight, evtWeightErr);
  if (dR_l_leadWjet_min > 0)
  fillWithOverFlow(histogram_dR_l_leadWjet_min_, dR_l_leadWjet_min, evtWeight, evtWeightErr);
  if (dR_l_leadWjet_max > 0)
  fillWithOverFlow(histogram_dR_l_leadWjet_max_, dR_l_leadWjet_max, evtWeight, evtWeightErr);
  if (dR_l_leadAK4jet_min > 0)
  fillWithOverFlow(histogram_dR_l_leadAK4jet_min_, dR_l_leadAK4jet_min, evtWeight, evtWeightErr);
  if (dR_l_leadAK4jet_max > 0)
  fillWithOverFlow(histogram_dR_l_leadAK4jet_max_, dR_l_leadAK4jet_max, evtWeight, evtWeightErr);
  //
  fillWithOverFlow(histogram_met_, met, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mht_, mht, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_met_LD_, met_LD, evtWeight, evtWeightErr);
  //
  fillWithOverFlow(histogram_mT_lep1_met_, mT_lep1_met, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_lep2_met_, mT_lep2_met, evtWeight, evtWeightErr);
  //
  fillWithOverFlow(histogram_eventCategory_, eventCategory, evtWeight, evtWeightErr);
  //
  fillWithOverFlow(histogram_nTaus_, nTaus, evtWeight, evtWeightErr);
  
}
