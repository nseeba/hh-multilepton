#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_3l.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), getLogWeight()
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // get_era(), kEra_*
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()

EvtHistManager_hh_3l::EvtHistManager_hh_3l(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
  , era_(get_era(cfg.getParameter<std::string>("era")))
{
  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["numJetsPtGt40"] = { "central" };
  central_or_shiftOptions_["numBJets_loose"] = { "central" };
  central_or_shiftOptions_["numBJets_medium"] = { "central" };
  central_or_shiftOptions_["chargedSum3l"] = { "central" };
  central_or_shiftOptions_["numSFOS2l"] = { "central" };
  central_or_shiftOptions_["dihiggsVisMass"] = { "central" };
  central_or_shiftOptions_["dihiggsMass"] = { "central" };
  central_or_shiftOptions_["WTojjMass"] = { "central" };
  central_or_shiftOptions_["mSFOS2l"] = { "central" };
  central_or_shiftOptions_["mTMetLepton1"] = { "central" };
  central_or_shiftOptions_["mTMetLepton2"] = { "central" };
  central_or_shiftOptions_["vbf_m_jj"] = { "central" };
  central_or_shiftOptions_["vbf_dEta_jj"] = { "central" };
  central_or_shiftOptions_["numJets_nonVBF"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["mvaOutput_xgb_hh_3l_SUMBk_HH"] = { "*" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
}

const TH1 *
EvtHistManager_hh_3l::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_3l::bookHistograms(TFileDirectory & dir)
{
	/*
  histogram_numElectrons_    = book1D(dir, "numElectrons",    "numElectrons",     5, -0.5,  +4.5);
  histogram_numMuons_        = book1D(dir, "numMuons",        "numMuons",         5, -0.5,  +4.5);
  histogram_numHadTaus_      = book1D(dir, "numHadTaus",      "numHadTaus",       5, -0.5,  +4.5);
  histogram_numJets_         = book1D(dir, "numJets",         "numJets",         20, -0.5, +19.5);
  histogram_numBJets_loose_  = book1D(dir, "numBJets_loose",  "numBJets_loose",  10, -0.5,  +9.5);
  histogram_numBJets_medium_ = book1D(dir, "numBJets_medium", "numBJets_medium", 10, -0.5,  +9.5);

  histogram_numBJets_loose_vs_numJets_  = book2D(dir, "numBJets_loose_vs_numJets",  "numBJets_loose_vs_numJets",  8, -0.5, +7.5, 6, -0.5, +5.5);
  histogram_numBJets_medium_vs_numJets_ = book2D(dir, "numBJets_medium_vs_numJets", "numBJets_medium_vs_numJets", 8, -0.5, +7.5, 6, -0.5, +5.5);

  histogram_mvaOutput_3l_ttV_   = book1D(dir, "mvaOutput_3l_ttV",   "mvaOutput_3l_ttV",   40, -1., +1.);
  histogram_mvaOutput_3l_ttbar_ = book1D(dir, "mvaOutput_3l_ttbar", "mvaOutput_3l_ttbar", 40, -1., +1.);
  histogram_mvaDiscr_3l_        = book1D(dir, "mvaDiscr_3l",        "mvaDiscr_3l",         5,  0.5, 5.5); */

  histogram_numElectrons_    = book1D(dir, "numElectrons",    "numElectrons",      5, -0.5,  +4.5);
  histogram_numMuons_        = book1D(dir, "numMuons",        "numMuons",          5, -0.5,  +4.5);
  histogram_numJets_         = book1D(dir, "numJets",         "numJets",          20, -0.5, +19.5);
  histogram_numJetsPtGt40_   = book1D(dir, "numJetsPtGt40",   "numJetsPtGt40",    20, -0.5, +19.5);
  histogram_numBJets_loose_  = book1D(dir, "numBJets_loose",  "numBJets_loose",   10, -0.5,  +9.5);
  histogram_numBJets_medium_ = book1D(dir, "numBJets_medium", "numBJets_medium",  10, -0.5,  +9.5);
  
  histogram_chargedSum3l_    = book1D(dir, "chargedSum3l",    "chargedSum3l",      7, -3.5,  +3.5);
  histogram_numSFOS2l_       = book1D(dir, "numSFOS2l",       "numSameFlavorOppositeSign2l",  9, -0.5,  +8.5);
  
  histogram_dihiggsVisMass_  = book1D(dir, "dihiggsVisMass",  "dihiggsVisMass",  150,  0., 1500.);
  histogram_dihiggsMass_     = book1D(dir, "dihiggsMass",     "dihiggsMass",     150,  0., 1500.);
  histogram_WTojjMass_       = book1D(dir, "WTojjMass",       "WTojjMass",       150,  0.,  500.);
  histogram_mSFOS2l_         = book1D(dir, "mSFOS2l",         "mSFOS2l",         150,  0.,  500.);
  histogram_mTMetLepton1_    = book1D(dir, "mTMetLepton1",    "mTMetLepton1",    150,  0.,  500.);
  histogram_mTMetLepton2_    = book1D(dir, "mTMetLepton2",    "mTMetLepton2",    150,  0.,  500.);
  
  histogram_vbf_m_jj_        = book1D(dir, "vbf_m_jj",        "vbf_m_jj",               150,  0., 1500.);
  histogram_vbf_dEta_jj_     = book1D(dir, "vbf_dEta_jj",     "vbf_dEta_jj",            100,  0.,   10.);
  histogram_numJets_nonVBF_  = book1D(dir, "numJets_nonVBF",  "numJets_nonVBF",          20, -0.5, +19.5);
  
  histogram_HT_              = book1D(dir, "HT",              "HT",              150,  0., 1500.);
  histogram_STMET_           = book1D(dir, "STMET",           "STMET",           150,  0., 1500.);	

  histogram_mvaOutput_xgb_hh_3l_SUMBk_HH_ = book1D(dir, "mvaOutput_xgb_hh_3l_SUMBk_HH", "BDTscore", 50,  0., 1.);
  
  histogram_EventCounter_ = book1D(dir, "EventCounter", "EventCounter", 1, -0.5, +0.5);
}

void
EvtHistManager_hh_3l::fillHistograms(int numElectrons,
				     int numMuons,
				     int numJets,
				     int numJetsPtGt40,
				     int numBJets_loose,
				     int numBJets_medium,
				     int chargedSum3l,
				     int numSFOS2l,
				     double dihiggsVisMass,
				     double dihiggsMass,
				     double WTojjMass,
				     double mSFOS2l,
				     double mTMetLepton1,
				     double mTMetLepton2,
				     double vbf_m_jj, double vbf_dEta_jj,	 int numJets_nonVBF,		 
				     double HT,
				     double STMET,
				     double mvaOutput_xgb_hh_3l_SUMBk_HH,
				     double evtWeight)
{
  const double evtWeightErr = 0.;

	/*
  fillWithOverFlow(histogram_numElectrons_,    numElectrons,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,        numMuons,        evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numHadTaus_,      numHadTaus,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,         numJets,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,  numBJets_loose,  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_, numBJets_medium, evtWeight, evtWeightErr);

  fillWithOverFlow2d(histogram_numBJets_loose_vs_numJets_,  numJets, numBJets_loose,  evtWeight, evtWeightErr);
  fillWithOverFlow2d(histogram_numBJets_medium_vs_numJets_, numJets, numBJets_medium, evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mvaOutput_3l_ttV_,   mvaOutput_3l_ttV,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mvaOutput_3l_ttbar_, mvaOutput_3l_ttbar, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mvaDiscr_3l_,        mvaDiscr_3l,        evtWeight, evtWeightErr); */

  fillWithOverFlow(histogram_numElectrons_,    numElectrons,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,        numMuons,        evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,         numJets,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsPtGt40_,   numJetsPtGt40,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,  numBJets_loose,  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_, numBJets_medium, evtWeight, evtWeightErr);
  
  fillWithOverFlow(histogram_chargedSum3l_,    chargedSum3l,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numSFOS2l_,       numSFOS2l,       evtWeight, evtWeightErr);
  
  fillWithOverFlow(histogram_dihiggsVisMass_,  dihiggsVisMass,  evtWeight, evtWeightErr);
  if ( dihiggsMass > 0. ) 
    fillWithOverFlow(histogram_dihiggsMass_,   dihiggsMass,     evtWeight, evtWeightErr);  
  if (WTojjMass > 0.) 
    fillWithOverFlow(histogram_WTojjMass_,     WTojjMass,       evtWeight, evtWeightErr);
  if (mSFOS2l > 0.) 
    fillWithOverFlow(histogram_mSFOS2l_,       mSFOS2l,         evtWeight, evtWeightErr);
  if (mTMetLepton1 > 0.)
    fillWithOverFlow(histogram_mTMetLepton1_,  mTMetLepton1,    evtWeight, evtWeightErr);
  if (mTMetLepton2 > 0.)
    fillWithOverFlow(histogram_mTMetLepton2_,  mTMetLepton2,    evtWeight, evtWeightErr);
  
  fillWithOverFlow(histogram_vbf_m_jj_,        vbf_m_jj,        evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dEta_jj_,     vbf_dEta_jj,     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_nonVBF_,  numJets_nonVBF,         evtWeight, evtWeightErr);
  
  fillWithOverFlow(histogram_HT_,              HT,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,           STMET,           evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mvaOutput_xgb_hh_3l_SUMBk_HH_, mvaOutput_xgb_hh_3l_SUMBk_HH, evtWeight, evtWeightErr);
  
  fillWithOverFlow(histogram_EventCounter_, 0., evtWeight, evtWeightErr);
}
 
