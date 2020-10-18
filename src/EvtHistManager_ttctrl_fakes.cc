#include "hhAnalysis/multilepton/interface/EvtHistManager_ttctrl_fakes.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

const double kNullDouble = -99999.0;
const bool skipBookingAdditionalHistos = true;

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
  central_or_shiftOptions_["dR_ll"] = { "central" };
  central_or_shiftOptions_["mT_met_lepLead"] = { "central" };
  central_or_shiftOptions_["mT_met_lepSublead"] = { "central" };
  central_or_shiftOptions_["mT_met_lep_max"] = { "central" };
  central_or_shiftOptions_["mT_met_lep_min"] = { "central" };
  central_or_shiftOptions_["BDTOutput_SUM"] = { "*" };
  central_or_shiftOptions_["BDTOutput_SUM_gen_mHH_400"] = { "*" };
  central_or_shiftOptions_["BDTOutput_SUM_gen_mHH_700"] = { "*" };
  central_or_shiftOptions_["EventCounter"] = { "*" };

  central_or_shiftOptions_["histogram_pt_eTight_lead_"] = { "central" };
  central_or_shiftOptions_["histogram_cone_pt_eTight_lead_"] = { "central" };
  central_or_shiftOptions_["histogram_eta_eTight_lead_"] = { "central" };
  //
  central_or_shiftOptions_["histogram_pt_eTight_sublead_"] = { "central" };
  central_or_shiftOptions_["histogram_cone_pt_eTight_sublead_"] = { "central" };
  central_or_shiftOptions_["histogram_eta_eTight_sublead_"] = { "central" };
  //
  central_or_shiftOptions_["histogram_pt_muTight_lead_"] = { "central" };
  central_or_shiftOptions_["histogram_cone_pt_muTight_lead_"] = { "central" };
  central_or_shiftOptions_["histogram_eta_muTight_lead_"] = { "central" };
  //
  central_or_shiftOptions_["histogram_pt_muTight_sublead_"] = { "central" };
  central_or_shiftOptions_["histogram_cone_pt_muTight_sublead_"] = { "central" };
  central_or_shiftOptions_["histogram_eta_muTight_sublead_"] = { "central" };	  	    
  //
  central_or_shiftOptions_["histogram_pt_eFakeable_lead_"] = { "central" };
  central_or_shiftOptions_["histogram_cone_pt_eFakeable_lead_"] = { "central" };
  central_or_shiftOptions_["histogram_eta_eFakeable_lead_"] = { "central" };
  //
  central_or_shiftOptions_["histogram_pt_eFakeable_sublead_"] = { "central" };
  central_or_shiftOptions_["histogram_cone_pt_eFakeable_sublead_"] = { "central" };
  central_or_shiftOptions_["histogram_eta_eFakeable_sublead_"] = { "central" };
  //
  central_or_shiftOptions_["histogram_pt_muFakeable_lead_"] = { "central" };
  central_or_shiftOptions_["histogram_cone_pt_muFakeable_lead_"] = { "central" };
  central_or_shiftOptions_["histogram_eta_muFakeable_lead_"] = { "central" };
  //
  central_or_shiftOptions_["histogram_pt_muFakeable_sublead_"] = { "central" };
  central_or_shiftOptions_["histogram_cone_pt_muFakeable_sublead_"] = { "central" };
  central_or_shiftOptions_["histogram_eta_muFakeable_sublead_"] = { "central" };
  
  central_or_shiftOptions_["histogram_electronFR_sum_"] = { "central" };
  central_or_shiftOptions_["histogram_electronFR_nEntries_"] = { "central" };
  central_or_shiftOptions_["histogram_muonFR_sum_"] = { "central" };
  central_or_shiftOptions_["histogram_muonFR_nEntries_"] = { "central" };
}

const TH1 *
EvtHistManager_ttctrl_fakes::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_ttctrl_fakes::bookHistograms(TFileDirectory & dir)
{
  /*
  histogram_numElectrons_     = book1D(dir, "numElectrons",     "numElectrons",       5, -0.5,  +4.5);
  histogram_numMuons_         = book1D(dir, "numMuons",         "numMuons",           5, -0.5,  +4.5);
  histogram_numJets_          = book1D(dir, "numJets",          "numJets",           20, -0.5, +19.5);
  histogram_numJetsPtGt40_    = book1D(dir, "numJetsPtGt40",    "numJetsPtGt40",     20, -0.5, +19.5);
  histogram_dihiggsVisMass_   = book1D(dir, "dihiggsVisMass",   "dihiggsVisMass",   150,  0., 1500.);
  histogram_dihiggsMass_wMet_ = book1D(dir, "dihiggsMass_wMet", "dihiggsMass_wMet", 150,  0., 1500.);
  histogram_jetMass_          = book1D(dir, "jetMass",          "jetMass",          150,  0., 1500.);
  histogram_leptonPairMass_   = book1D(dir, "leptonPairMass",   "leptonPairMass",    50,  0.,  200.);
  histogram_electronPairMass_ = book1D(dir, "electronPairMass", "electronPairMass",  50,  0.,  200.);
  histogram_muonPairMass_     = book1D(dir, "muonPairMass",     "muonPairMass",      50,  0.,  200.);
  histogram_leptonPairCharge_ = book1D(dir, "leptonPairCharge", "leptonPairCharge",   5, -2.5,  +2.5);
  histogram_HT_               = book1D(dir, "HT",               "HT",               150,  0., 1500.);
  histogram_STMET_            = book1D(dir, "STMET",            "STMET",            150,  0., 1500.); //
  histogram_dR_ll_            = book1D(dir, "dR_ll",            "dR_ll",             60,  0.,    3.);
  histogram_mT_met_lepLead_   = book1D(dir, "mT_met_lepLead",   "mT_met_lepLead",    50,  0.,  200.);
  histogram_mT_met_lepSublead_= book1D(dir, "mT_met_lepSublead","mT_met_lepSublead", 50,  0.,  200.);
  histogram_mT_met_lep_max_   = book1D(dir, "mT_met_lep_max",   "mT_met_lep_max",    50,  0.,  200.);
  histogram_mT_met_lep_min_   = book1D(dir, "mT_met_lep_min",   "mT_met_lep_min",    50,  0.,  200.);
  
  //histogram_BDTOutput_SUM_    = book1D(dir, "BDTOutput_SUM",    "BDTOutput_SUM",    100,  0.,    1.);
  histogram_BDTOutput_SUM_gen_mHH_400_    = book1D(dir, "BDTOutput_SUM_gen_mHH_400",    "BDTOutput_SUM_gen_mHH_400",    100,  0.,    1.);
  histogram_BDTOutput_SUM_gen_mHH_700_    = book1D(dir, "BDTOutput_SUM_gen_mHH_700",    "BDTOutput_SUM_gen_mHH_700",    100,  0.,    1.);
  histogram_EventCounter_     = book1D(dir, "EventCounter",     "EventCounter",       1, -0.5,  +0.5);
  */


  histogram_numElectrons_     = book1D(dir, "numElectrons",     "numElectrons",       5, -0.5,  +4.5);
  histogram_numMuons_         = book1D(dir, "numMuons",         "numMuons",           5, -0.5,  +4.5);
  histogram_numJets_          = book1D(dir, "numJets",          "numJets",           20, -0.5, +19.5);
  histogram_numJetsPtGt40_    = book1D(dir, "numJetsPtGt40",    "numJetsPtGt40",     20, -0.5, +19.5);
  if ( ! skipBookingAdditionalHistos) histogram_dihiggsVisMass_   = book1D(dir, "dihiggsVisMass",   "dihiggsVisMass",   150,  0., 1500.);
  if ( ! skipBookingAdditionalHistos) histogram_dihiggsMass_wMet_ = book1D(dir, "dihiggsMass_wMet", "dihiggsMass_wMet", 150,  0., 1500.);
  histogram_jetMass_          = book1D(dir, "jetMass",          "jetMass",          150,  0., 1500.);
  histogram_leptonPairMass_   = book1D(dir, "leptonPairMass",   "leptonPairMass",    50,  0.,  200.);
  histogram_electronPairMass_ = book1D(dir, "electronPairMass", "electronPairMass",  50,  0.,  200.);
  histogram_muonPairMass_     = book1D(dir, "muonPairMass",     "muonPairMass",      50,  0.,  200.);
  histogram_leptonPairCharge_ = book1D(dir, "leptonPairCharge", "leptonPairCharge",   5, -2.5,  +2.5);
  histogram_HT_               = book1D(dir, "HT",               "HT",               150,  0., 1500.);
  histogram_STMET_            = book1D(dir, "STMET",            "STMET",            150,  0., 1500.); //
  histogram_dR_ll_            = book1D(dir, "dR_ll",            "dR_ll",             60,  0.,    3.);
  histogram_mT_met_lepLead_   = book1D(dir, "mT_met_lepLead",   "mT_met_lepLead",    50,  0.,  200.);
  histogram_mT_met_lepSublead_= book1D(dir, "mT_met_lepSublead","mT_met_lepSublead", 50,  0.,  200.);
  histogram_mT_met_lep_max_   = book1D(dir, "mT_met_lep_max",   "mT_met_lep_max",    50,  0.,  200.);
  histogram_mT_met_lep_min_   = book1D(dir, "mT_met_lep_min",   "mT_met_lep_min",    50,  0.,  200.);
  
  //histogram_BDTOutput_SUM_    = book1D(dir, "BDTOutput_SUM",    "BDTOutput_SUM",    100,  0.,    1.);
  if ( ! skipBookingAdditionalHistos) histogram_BDTOutput_SUM_gen_mHH_400_    = book1D(dir, "BDTOutput_SUM_gen_mHH_400",    "BDTOutput_SUM_gen_mHH_400",    100,  0.,    1.);
  if ( ! skipBookingAdditionalHistos) histogram_BDTOutput_SUM_gen_mHH_700_    = book1D(dir, "BDTOutput_SUM_gen_mHH_700",    "BDTOutput_SUM_gen_mHH_700",    100,  0.,    1.);
  histogram_EventCounter_     = book1D(dir, "EventCounter",     "EventCounter",       1, -0.5,  +0.5);



  


  histogram_pt_eTight_lead_             = book1D(dir, "pt_eTight_lead",             "pt_eTight_lead",             150, 0.,  150.);
  histogram_cone_pt_eTight_lead_        = book1D(dir, "cone_pt_eTight_lead",        "cone_pt_eTight_lead",        150, 0.,  150.);
  histogram_eta_eTight_lead_            = book1D(dir, "eta_eTight_lead",            "eta_eTight_lead",            100,-3.,   +3.);
  //
  histogram_pt_eTight_sublead_          = book1D(dir, "pt_eTight_sublead",          "pt_eTight_sublead",          150, 0.,  150.);
  histogram_cone_pt_eTight_sublead_     = book1D(dir, "cone_pt_eTight_sublead",     "cone_pt_eTight_sublead",     150, 0.,  150.);
  histogram_eta_eTight_sublead_         = book1D(dir, "eta_eTight_sublead",         "eta_eTight_sublead",         100,-3.,   +3.);
  //
  histogram_pt_muTight_lead_            = book1D(dir, "pt_muTight_lead",            "pt_muTight_lead",            150, 0.,  150.);
  histogram_cone_pt_muTight_lead_       = book1D(dir, "cone_pt_muTight_lead",       "cone_pt_muTight_lead",       150, 0.,  150.);
  histogram_eta_muTight_lead_           = book1D(dir, "eta_muTight_lead",           "eta_muTight_lead",           100,-3.,   +3.);
  //
  histogram_pt_muTight_sublead_         = book1D(dir, "pt_muTight_sublead",         "pt_muTight_sublead",         150, 0.,  150.);
  histogram_cone_pt_muTight_sublead_    = book1D(dir, "cone_pt_muTight_sublead",    "cone_pt_muTight_sublead",    150, 0.,  150.);
  histogram_eta_muTight_sublead_        = book1D(dir, "eta_muTight_sublead",        "eta_muTight_sublead",        100,-3.,   +3.);	  	    
  //
  histogram_pt_eFakeable_lead_          = book1D(dir, "pt_eFakeable_lead",          "pt_eFakeable_lead",          150, 0.,  150.);
  histogram_cone_pt_eFakeable_lead_     = book1D(dir, "cone_pt_eFakeable_lead",     "cone_pt_eFakeable_lead",     150, 0.,  150.);
  histogram_eta_eFakeable_lead_         = book1D(dir, "eta_eFakeable_lead",         "eta_eFakeable_lead",         100,-3.,   +3.);
  //
  histogram_pt_eFakeable_sublead_       = book1D(dir, "pt_eFakeable_sublead",       "pt_eFakeable_sublead",       150, 0.,  150.);
  histogram_cone_pt_eFakeable_sublead_  = book1D(dir, "cone_pt_eFakeable_sublead",  "cone_pt_eFakeable_sublead",  150, 0.,  150.);
  histogram_eta_eFakeable_sublead_      = book1D(dir, "eta_eFakeable_sublead",      "eta_eFakeable_sublead",      100,-3.,   +3.);
  //
  histogram_pt_muFakeable_lead_         = book1D(dir, "pt_muFakeable_lead",         "pt_muFakeable_lead",         150, 0.,  150.);
  histogram_cone_pt_muFakeable_lead_    = book1D(dir, "cone_pt_muFakeable_lead",    "cone_pt_muFakeable_lead",    150, 0.,  150.);
  histogram_eta_muFakeable_lead_        = book1D(dir, "eta_muFakeable_lead",        "eta_muFakeable_lead",        100,-3.,   +3.);
  //
  histogram_pt_muFakeable_sublead_      = book1D(dir, "pt_muFakeable_sublead",      "pt_muFakeable_sublead",      150, 0.,  150.);
  histogram_cone_pt_muFakeable_sublead_ = book1D(dir, "cone_pt_muFakeable_sublead", "cone_pt_muFakeable_sublead", 150, 0.,  150.);
  histogram_eta_muFakeable_sublead_     = book1D(dir, "eta_muFakeable_sublead",     "eta_muFakeable_sublead",     100,-3.,   +3.);

  histogram_electronFR_sum_      = book1D(dir, "electronFR_sum_",        "electronFR_sum_",        1, -0.5,  +0.5);
  histogram_electronFR_nEntries_ = book1D(dir, "electronFR_nEntries_",   "electronFR_nEntries_",   1, -0.5,  +0.5);
  histogram_muonFR_sum_          = book1D(dir, "muonFR_sum_",            "muonFR_sum_",            1, -0.5,  +0.5);
  histogram_muonFR_nEntries_     = book1D(dir, "muonFR_nEntries_",       "muonFR_nEntries_",       1, -0.5,  +0.5);
  histogram_electronFR_sum_->SetBinContent(1, 0.);
  histogram_muonFR_sum_->SetBinContent(1, 0.);
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
					    double STMET,//
					    double dR_ll,
					    double mT_met_lepLead,
					    double mT_met_lepSublead,
					    double mT_met_lep_max,
					    double mT_met_lep_min,
					    //double BDTOutput_SUM,
					    double BDTOutput_SUM_gen_mHH_400,
					    double BDTOutput_SUM_gen_mHH_700,
					    //
					    double pt_eTight_lead,
					    double cone_pt_eTight_lead,
					    double eta_eTight_lead,
					    //
					    double pt_eTight_sublead,
					    double cone_pt_eTight_sublead,
					    double eta_eTight_sublead,
					    //
					    double pt_muTight_lead,
					    double cone_pt_muTight_lead,
					    double eta_muTight_lead,
					    //
					    double pt_muTight_sublead,
					    double cone_pt_muTight_sublead,
					    double eta_muTight_sublead,	  	    
					    //
					    double pt_eFakeable_lead,
					    double cone_pt_eFakeable_lead,
					    double eta_eFakeable_lead,
					    //
					    double pt_eFakeable_sublead,
					    double cone_pt_eFakeable_sublead,
					    double eta_eFakeable_sublead,
					    //
					    double pt_muFakeable_lead,
					    double cone_pt_muFakeable_lead,
					    double eta_muFakeable_lead,
					    //
					    double pt_muFakeable_sublead,
					    double cone_pt_muFakeable_sublead,
					    double eta_muFakeable_sublead,
					    //
					    double evtWeight)
{
  const double evtWeightErr = 0.;
  /*
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
  fillWithOverFlow(histogram_STMET_,            STMET,            evtWeight, evtWeightErr); //
  fillWithOverFlow(histogram_dR_ll_,            dR_ll,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_met_lepLead_,   mT_met_lepLead,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_met_lepSublead_,mT_met_lepSublead,evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_met_lep_max_,   mT_met_lep_max,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_met_lep_min_,   mT_met_lep_min,   evtWeight, evtWeightErr); 
  
  //fillWithOverFlow(histogram_BDTOutput_SUM_,    BDTOutput_SUM,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_BDTOutput_SUM_gen_mHH_400_,    BDTOutput_SUM_gen_mHH_400,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_BDTOutput_SUM_gen_mHH_700_,    BDTOutput_SUM_gen_mHH_700,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_,     0.,               evtWeight, evtWeightErr);
  */

  fillWithOverFlow(histogram_numElectrons_,     numElectrons,     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,         numMuons,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,          numJets,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsPtGt40_,    numJetsPtGt40,    evtWeight, evtWeightErr);
  if ( ! skipBookingAdditionalHistos) fillWithOverFlow(histogram_dihiggsVisMass_,   dihiggsVisMass,   evtWeight, evtWeightErr);
  if ( ! skipBookingAdditionalHistos) fillWithOverFlow(histogram_dihiggsMass_wMet_, dihiggsMass_wMet, evtWeight, evtWeightErr);
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
  fillWithOverFlow(histogram_STMET_,            STMET,            evtWeight, evtWeightErr); //
  fillWithOverFlow(histogram_dR_ll_,            dR_ll,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_met_lepLead_,   mT_met_lepLead,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_met_lepSublead_,mT_met_lepSublead,evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_met_lep_max_,   mT_met_lep_max,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_met_lep_min_,   mT_met_lep_min,   evtWeight, evtWeightErr); 
  
  //fillWithOverFlow(histogram_BDTOutput_SUM_,    BDTOutput_SUM,    evtWeight, evtWeightErr);
  if ( ! skipBookingAdditionalHistos) fillWithOverFlow(histogram_BDTOutput_SUM_gen_mHH_400_,    BDTOutput_SUM_gen_mHH_400,    evtWeight, evtWeightErr);
  if ( ! skipBookingAdditionalHistos) fillWithOverFlow(histogram_BDTOutput_SUM_gen_mHH_700_,    BDTOutput_SUM_gen_mHH_700,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_,     0.,               evtWeight, evtWeightErr);
  

  if (abs(pt_eTight_lead         - kNullDouble) > 1e-6)        fillWithOverFlow(histogram_pt_eTight_lead_,                pt_eTight_lead,               evtWeight, evtWeightErr);
  if (abs(cone_pt_eTight_lead    - kNullDouble) > 1e-6)        fillWithOverFlow(histogram_cone_pt_eTight_lead_,           cone_pt_eTight_lead,          evtWeight, evtWeightErr);
  if (abs(eta_eTight_lead        - kNullDouble) > 1e-6)        fillWithOverFlow(histogram_eta_eTight_lead_,               eta_eTight_lead,              evtWeight, evtWeightErr);
  //
  if (abs(pt_eTight_sublead      - kNullDouble) > 1e-6)        fillWithOverFlow(histogram_pt_eTight_sublead_,             pt_eTight_sublead,            evtWeight, evtWeightErr);
  if (abs(cone_pt_eTight_sublead - kNullDouble) > 1e-6)        fillWithOverFlow(histogram_cone_pt_eTight_sublead_,        cone_pt_eTight_sublead,       evtWeight, evtWeightErr);
  if (abs(eta_eTight_sublead     - kNullDouble) > 1e-6)        fillWithOverFlow(histogram_eta_eTight_sublead_,            eta_eTight_sublead,           evtWeight, evtWeightErr);
  //
  if (abs(pt_muTight_lead         - kNullDouble) > 1e-6)       fillWithOverFlow(histogram_pt_muTight_lead_,               pt_muTight_lead,              evtWeight, evtWeightErr);
  if (abs(cone_pt_muTight_lead    - kNullDouble) > 1e-6)       fillWithOverFlow(histogram_cone_pt_muTight_lead_,          cone_pt_muTight_lead,         evtWeight, evtWeightErr);
  if (abs(eta_muTight_lead        - kNullDouble) > 1e-6)       fillWithOverFlow(histogram_eta_muTight_lead_,              eta_muTight_lead,             evtWeight, evtWeightErr);
  //
  if (abs(pt_muTight_sublead      - kNullDouble) > 1e-6)       fillWithOverFlow(histogram_pt_muTight_sublead_,            pt_muTight_sublead,           evtWeight, evtWeightErr);
  if (abs(cone_pt_muTight_sublead - kNullDouble) > 1e-6)       fillWithOverFlow(histogram_cone_pt_muTight_sublead_,       cone_pt_muTight_sublead,      evtWeight, evtWeightErr);
  if (abs(eta_muTight_sublead     - kNullDouble) > 1e-6)       fillWithOverFlow(histogram_eta_muTight_sublead_,           eta_muTight_sublead,          evtWeight, evtWeightErr);
  //
  if (abs(pt_eFakeable_lead         - kNullDouble) > 1e-6)     fillWithOverFlow(histogram_pt_eFakeable_lead_,             pt_eFakeable_lead,            evtWeight, evtWeightErr);
  if (abs(cone_pt_eFakeable_lead    - kNullDouble) > 1e-6)     fillWithOverFlow(histogram_cone_pt_eFakeable_lead_,        cone_pt_eFakeable_lead,       evtWeight, evtWeightErr);
  if (abs(eta_eFakeable_lead        - kNullDouble) > 1e-6)     fillWithOverFlow(histogram_eta_eFakeable_lead_,            eta_eFakeable_lead,           evtWeight, evtWeightErr);
  //
  if (abs(pt_eFakeable_sublead      - kNullDouble) > 1e-6)     fillWithOverFlow(histogram_pt_eFakeable_sublead_,          pt_eFakeable_sublead,         evtWeight, evtWeightErr);
  if (abs(cone_pt_eFakeable_sublead - kNullDouble) > 1e-6)     fillWithOverFlow(histogram_cone_pt_eFakeable_sublead_,     cone_pt_eFakeable_sublead,    evtWeight, evtWeightErr);
  if (abs(eta_eFakeable_sublead     - kNullDouble) > 1e-6)     fillWithOverFlow(histogram_eta_eFakeable_sublead_,         eta_eFakeable_sublead,        evtWeight, evtWeightErr);
  //
  if (abs(pt_muFakeable_lead         - kNullDouble) > 1e-6)    fillWithOverFlow(histogram_pt_muFakeable_lead_,            pt_muFakeable_lead,           evtWeight, evtWeightErr);
  if (abs(cone_pt_muFakeable_lead    - kNullDouble) > 1e-6)    fillWithOverFlow(histogram_cone_pt_muFakeable_lead_,       cone_pt_muFakeable_lead,      evtWeight, evtWeightErr);
  if (abs(eta_muFakeable_lead        - kNullDouble) > 1e-6)    fillWithOverFlow(histogram_eta_muFakeable_lead_,           eta_muFakeable_lead,          evtWeight, evtWeightErr);
  //
  if (abs(pt_muFakeable_sublead      - kNullDouble) > 1e-6)    fillWithOverFlow(histogram_pt_muFakeable_sublead_,         pt_muFakeable_sublead,        evtWeight, evtWeightErr);
  if (abs(cone_pt_muFakeable_sublead - kNullDouble) > 1e-6)    fillWithOverFlow(histogram_cone_pt_muFakeable_sublead_,    cone_pt_muFakeable_sublead,   evtWeight, evtWeightErr);
  if (abs(eta_muFakeable_sublead     - kNullDouble) > 1e-6)    fillWithOverFlow(histogram_eta_muFakeable_sublead_,        eta_muFakeable_sublead,       evtWeight, evtWeightErr);

  
}


void
EvtHistManager_ttctrl_fakes::fillHistograms_avgLeptonFR(int    leptonPdgId,
							double leptonFR_thisEvt)
{
  if (abs(leptonFR_thisEvt - (-99999.)) < 1e-6) return;

  double leptonFR_sum;
  if (leptonPdgId == 11)
  {
    leptonFR_sum  = histogram_electronFR_sum_->GetBinContent(1);
    leptonFR_sum += leptonFR_thisEvt;
    histogram_electronFR_sum_->SetBinContent(1, leptonFR_sum);
    fillWithOverFlow(histogram_electronFR_nEntries_,     0.,               1, 0);
  }
  else if (leptonPdgId == 13)
  {
    leptonFR_sum  = histogram_muonFR_sum_->GetBinContent(1);
    leptonFR_sum += leptonFR_thisEvt;
    histogram_muonFR_sum_->SetBinContent(1, leptonFR_sum);
    fillWithOverFlow(histogram_muonFR_nEntries_,     0.,               1, 0);
  }
}
