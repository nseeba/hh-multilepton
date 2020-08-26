#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_1l_3tau.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

EvtHistManager_hh_1l_3tau::EvtHistManager_hh_1l_3tau(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numHadTaus"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["numJetsPtGt40"] = { "central" };
  central_or_shiftOptions_["numBJets_loose"] = { "central" };
  central_or_shiftOptions_["numBJets_medium"] = { "central" };
  central_or_shiftOptions_["dihiggsVisMass"] = { "central" };
  central_or_shiftOptions_["dihiggsMass"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
  central_or_shiftOptions_["antiE_tau1_OS_matched"] = { "central" };
  central_or_shiftOptions_["antiE_tau1_OS_unmatched"] = { "central" };
  central_or_shiftOptions_["antiE_tau2_OS_matched"] = { "central" };
  central_or_shiftOptions_["antiE_tau2_OS_unmatched"] = { "central" };
  central_or_shiftOptions_["antiE_tau3_OS_matched"] = { "central" };
  central_or_shiftOptions_["antiE_tau3_OS_unmatched"] = { "central" };
  central_or_shiftOptions_["m_OS_etau_closestToZ"] = { "central" };
  central_or_shiftOptions_["eta_OS_etau1"] = { "central" };
  central_or_shiftOptions_["eta_OS_etau2"] = { "central" };
  central_or_shiftOptions_["eta_OS_etau3"] = { "central" };
}

const TH1 *
EvtHistManager_hh_1l_3tau::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_1l_3tau::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_    = book1D(dir, "numElectrons",    "numElectrons",      5, -0.5,  +4.5);
  histogram_numMuons_        = book1D(dir, "numMuons",        "numMuons",          5, -0.5,  +4.5);
  histogram_numHadTaus_      = book1D(dir, "numHadTaus",      "numHadTaus",        5, -0.5,  +4.5);
  histogram_numJets_         = book1D(dir, "numJets",         "numJets",          20, -0.5, +19.5);
  histogram_numJetsPtGt40_   = book1D(dir, "numJetsPtGt40",   "numJetsPtGt40",    20, -0.5, +19.5);
  histogram_numBJets_loose_  = book1D(dir, "numBJets_loose",  "numBJets_loose",   10, -0.5,  +9.5);
  histogram_numBJets_medium_ = book1D(dir, "numBJets_medium", "numBJets_medium",  10, -0.5,  +9.5);

  histogram_dihiggsVisMass_  = book1D(dir, "dihiggsVisMass",  "dihiggsVisMass",  150,  0., 1500.);
  histogram_dihiggsMass_     = book1D(dir, "dihiggsMass",     "dihiggsMass",     150,  0., 1500.);

  histogram_HT_              = book1D(dir, "HT",              "HT",              150,  0., 1500.);
  histogram_STMET_           = book1D(dir, "STMET",           "STMET",           150,  0., 1500.);

  histogram_EventCounter_    = book1D(dir, "EventCounter",    "EventCounter",      1, -0.5,  +0.5);
  
  histogram_antiE_tau1_OS_matched_   = book1D(dir, "antiE_tau1_OS_matched",   "antiE_tau1_OS_matched", 11, -2.5, 8.5);
  histogram_antiE_tau1_OS_unmatched_ = book1D(dir, "antiE_tau1_OS_unmatched", "antiE_tau1_OS_unmatched", 11, -2.5, 8.5);
  histogram_antiE_tau2_OS_matched_   = book1D(dir, "antiE_tau2_OS_matched",   "antiE_tau2_OS_matched", 11, -2.5, 8.5);
  histogram_antiE_tau2_OS_unmatched_ = book1D(dir, "antiE_tau2_OS_unmatched", "antiE_tau2_OS_unmatched", 11, -2.5, 8.5);
  histogram_antiE_tau3_OS_matched_   = book1D(dir, "antiE_tau3_OS_matched",   "antiE_tau3_OS_matched", 11, -2.5, 8.5);
  histogram_antiE_tau3_OS_unmatched_ = book1D(dir, "antiE_tau3_OS_unmatched", "antiE_tau3_OS_unmatched", 11, -2.5, 8.5);
  histogram_m_OS_etau_closestToZ_ = book1D(dir, "m_OS_etau_closestToZ", "m_OS_etau_closestToZ", 100, 0.,200);
  histogram_eta_OS_etau1_ = book1D(dir, "eta_OS_etau1", "eta_OS_etau1", 46, -2.3, 2.3);
  histogram_eta_OS_etau2_ = book1D(dir, "eta_OS_etau2", "eta_OS_etau2", 46, -2.3, 2.3);
  histogram_eta_OS_etau3_ = book1D(dir, "eta_OS_etau3", "eta_OS_etau3", 46, -2.3, 2.3);
}

void
EvtHistManager_hh_1l_3tau::fillHistograms(int numElectrons,
					  int numMuons,
					  int numHadTaus,
					  int numJets,
					  int numJetsPtGt40,
					  int numBJets_loose,
					  int numBJets_medium,
					  double dihiggsVisMass,
					  double dihiggsMass,
					  double HT,
					  double STMET,
					  double evtWeight,
					  double antiE_tau1_OS_matched,
					  double antiE_tau1_OS_unmatched,
					  double antiE_tau2_OS_matched,
					  double antiE_tau2_OS_unmatched,
					  double antiE_tau3_OS_matched,
					  double antiE_tau3_OS_unmatched,
					  double m_OS_etau_closestToZ,
					  double eta_OS_etau1,
					  double eta_OS_etau2,
					  double eta_OS_etau3
					  )
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,    numElectrons,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,        numMuons,        evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numHadTaus_,      numHadTaus,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,         numJets,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsPtGt40_,   numJetsPtGt40,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,  numBJets_loose,  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_, numBJets_medium, evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_dihiggsVisMass_,  dihiggsVisMass,  evtWeight, evtWeightErr);
  if ( dihiggsMass > 0. ) {
    fillWithOverFlow(histogram_dihiggsMass_,   dihiggsMass,     evtWeight, evtWeightErr);
  }

  fillWithOverFlow(histogram_HT_,              HT,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,           STMET,           evtWeight, evtWeightErr);
  
  fillWithOverFlow(histogram_EventCounter_,    0.,              evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_antiE_tau1_OS_matched_,   antiE_tau1_OS_matched,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_antiE_tau1_OS_unmatched_, antiE_tau1_OS_unmatched, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_antiE_tau2_OS_matched_,   antiE_tau2_OS_matched,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_antiE_tau2_OS_unmatched_, antiE_tau2_OS_unmatched, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_antiE_tau3_OS_matched_,   antiE_tau3_OS_matched,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_antiE_tau3_OS_unmatched_, antiE_tau3_OS_unmatched, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_m_OS_etau_closestToZ_, m_OS_etau_closestToZ, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_eta_OS_etau1_, eta_OS_etau1, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_eta_OS_etau2_, eta_OS_etau2, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_eta_OS_etau3_, eta_OS_etau3, evtWeight, evtWeightErr);


}
