#include "hhAnalysis/multilepton/interface/EvtHistManager_ttctrl_fakes.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

EvtHistManager_ttctrl_fakes::EvtHistManager_ttctrl_fakes(const edm::ParameterSet & cfg)
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
  central_or_shiftOptions_["BDTOutput_SUM"] = { "*" };
  central_or_shiftOptions_["BDTOutput_SUM_gen_mHH_400"] = { "*" };
  central_or_shiftOptions_["BDTOutput_SUM_gen_mHH_700"] = { "*" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
}

const TH1 *
EvtHistManager_ttctrl_fakes::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_ttctrl_fakes::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_     = book1D(dir, "numElectrons",     "numElectrons",       5, -0.5,  +4.5);
  histogram_numMuons_         = book1D(dir, "numMuons",         "numMuons",           5, -0.5,  +4.5);
  histogram_numJets_          = book1D(dir, "numJets",          "numJets",           20, -0.5, +19.5);
  histogram_numJetsPtGt40_    = book1D(dir, "numJetsPtGt40",    "numJetsPtGt40",     20, -0.5, +19.5);
  histogram_dihiggsVisMass_   = book1D(dir, "dihiggsVisMass",   "dihiggsVisMass",   150,  0., 1500.);
  histogram_dihiggsMass_wMet_ = book1D(dir, "dihiggsMass_wMet", "dihiggsMass_wMet", 150,  0., 1500.);
  histogram_jetMass_          = book1D(dir, "jetMass",          "jetMass",          150,  0., 1500.);
  histogram_leptonPairMass_   = book1D(dir, "leptonPairMass",   "leptonPairMass",    40,  0.,  200.);
  histogram_electronPairMass_ = book1D(dir, "electronPairMass", "electronPairMass",  40,  0.,  200.);
  histogram_muonPairMass_     = book1D(dir, "muonPairMass",     "muonPairMass",      40,  0.,  200.);
  histogram_leptonPairCharge_ = book1D(dir, "leptonPairCharge", "leptonPairCharge",   5, -2.5,  +2.5);
  histogram_HT_               = book1D(dir, "HT",               "HT",               150,  0., 1500.);
  histogram_STMET_            = book1D(dir, "STMET",            "STMET",            150,  0., 1500.);
  //histogram_BDTOutput_SUM_    = book1D(dir, "BDTOutput_SUM",    "BDTOutput_SUM",    100,  0.,    1.);
  histogram_BDTOutput_SUM_gen_mHH_400_    = book1D(dir, "BDTOutput_SUM_gen_mHH_400",    "BDTOutput_SUM_gen_mHH_400",    100,  0.,    1.);
  histogram_BDTOutput_SUM_gen_mHH_700_    = book1D(dir, "BDTOutput_SUM_gen_mHH_700",    "BDTOutput_SUM_gen_mHH_700",    100,  0.,    1.);
  histogram_EventCounter_     = book1D(dir, "EventCounter",     "EventCounter",       1, -0.5,  +0.5);
}

void
EvtHistManager_ttctrl_fakes::fillHistograms(int numElectrons,
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
				       //double BDTOutput_SUM,
				       double BDTOutput_SUM_gen_mHH_400,
				       double BDTOutput_SUM_gen_mHH_700,
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
  //fillWithOverFlow(histogram_BDTOutput_SUM_,    BDTOutput_SUM,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_BDTOutput_SUM_gen_mHH_400_,    BDTOutput_SUM_gen_mHH_400,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_BDTOutput_SUM_gen_mHH_700_,    BDTOutput_SUM_gen_mHH_700,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_,     0.,               evtWeight, evtWeightErr);
}
