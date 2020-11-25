#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_3l_1tau.h"
//#include "tthAnalysis/HiggsToTauTau/interface/BM_list.h" // BMS
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

EvtHistManager_hh_3l_1tau::EvtHistManager_hh_3l_1tau(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numHadTaus"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["MET"] = { "central" };
  central_or_shiftOptions_["nSFOS"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["MET_LD"] = { "central" };
  central_or_shiftOptions_["dihiggsVisMass"] = { "central" };
  central_or_shiftOptions_["dihiggsMass"] = { "central" };
  central_or_shiftOptions_["dR_smartpair_ltau"] = { "central" };
  central_or_shiftOptions_["m_smartpair_ltau"] = { "central" };
  central_or_shiftOptions_["dR_smartpair_ll"] = { "central" };
  central_or_shiftOptions_["m_smartpair_ll"] = { "central" };
  central_or_shiftOptions_["mllOS_closestToZ"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
  central_or_shiftOptions_["EventNumber"] = { "*" };
}

const TH1 *
EvtHistManager_hh_3l_1tau::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_3l_1tau::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_     = book1D(dir, "numElectrons",     "numElectrons",      5,   -0.5,  +4.5  );
  histogram_numMuons_         = book1D(dir, "numMuons",         "numMuons",          5,   -0.5,  +4.5  );
  histogram_numHadTaus_       = book1D(dir, "numHadTaus",       "numHadTaus",        5,   -0.5,  +4.5  );
  histogram_numJets_          = book1D(dir, "numJets",          "numJets",           20,  -0.5,  +19.5 );
  histogram_MET_              = book1D(dir, "MET",              "MET",               125, -0.,   +250  );
  histogram_nSFOS_            = book1D(dir, "nSFOS",            "nSFOS",             5,   -0.5,  +4.5  );
  histogram_HT_               = book1D(dir, "HT",               "HT",                150, -0.,   +1500.);
  histogram_STMET_            = book1D(dir, "STMET",            "STMET",             150, -0.,   +1500.);
  histogram_MET_LD_           = book1D(dir, "MET_LD",           "MET_LD",            125, -0.,   +250. );
  histogram_dihiggsVisMass_   = book1D(dir, "dihiggsVisMass",   "dihiggsVisMass",    150, -0.,   +1500.);
  histogram_dihiggsMass_      = book1D(dir, "dihiggsMass",      "dihiggsMass",       150, -0.,   +1500.);
  histogram_dR_smartpair_ltau_= book1D(dir, "dR_smartpair_ltau","dR_smartpair_ltau", 35,  -0.,   +3.5  );
  histogram_m_smartpair_ltau_ = book1D(dir, "m_smartpair_ltau", "m_smartpair_ltau",  100, -0.,   +200. );
  histogram_dR_smartpair_ll_  = book1D(dir, "dR_smartpair_ll",  "dR_smartpair_ll",   35,  -0.,   +3.5  );
  histogram_m_smartpair_ll_   = book1D(dir, "m_smartpair_ll",   "m_smartpair_ll",    100, -0.,   +200. );
  histogram_mllOS_closestToZ_ = book1D(dir, "mllOS_closestToZ", "mllOS_closestToZ",  126, -2.,   +250. );
  histogram_EventCounter_     = book1D(dir, "EventCounter",     "EventCounter",      1,   -0.5,  +0.5  );
  histogram_EventNumber_      = book1D(dir, "EventNumber",      "EventNumber",       2,   -0.5,  +1.5  );
  histogram_EventNumber_->GetXaxis()->SetBinLabel(1,"Odd");
  histogram_EventNumber_->GetXaxis()->SetBinLabel(2,"Even");
}

void
EvtHistManager_hh_3l_1tau::fillHistograms(int numElectrons,
					  int numMuons,
					  int numHadTaus,
					  int numJets,
					  double MET,
					  int nSFOS,
					  double HT,
					  double STMET,
					  double MET_LD,
					  double dihiggsVisMass,
					  double dihiggsMass,
					  double dR_smartpair_ltau,
					  double m_smartpair_ltau,
					  double dR_smartpair_ll,
					  double m_smartpair_ll,
					  double mllOS_closestToZ,
                                          unsigned int evt_number,
					  double evtWeight)
{
  const double evtWeightErr = 0.;
  fillWithOverFlow(histogram_numElectrons_,      numElectrons,        evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,          numMuons,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numHadTaus_,        numHadTaus,          evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numJets_,           numJets,             evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_MET_,               MET,                 evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_nSFOS_,             nSFOS,               evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_HT_,                HT,                  evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_STMET_,             STMET,               evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_MET_LD_,            MET_LD,              evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dihiggsVisMass_,    dihiggsVisMass,      evtWeight,     evtWeightErr);
  if ( dihiggsMass > 0. ) {
    fillWithOverFlow(histogram_dihiggsMass_,     dihiggsMass,         evtWeight,     evtWeightErr);
  }
  fillWithOverFlow(histogram_dR_smartpair_ll_,   dR_smartpair_ltau,   evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_m_smartpair_ll_,    m_smartpair_ltau,    evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dR_smartpair_ltau_, dR_smartpair_ll,     evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_m_smartpair_ltau_,  m_smartpair_ll,      evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_mllOS_closestToZ_,  mllOS_closestToZ,    evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_,      0.,                  evtWeight,     evtWeightErr);
  if(evt_number % 2){// ODD EVENT NUMBER CASE                                                                                                                                                    
    fillWithOverFlow(histogram_EventNumber_,     0.,                  evtWeight,     evtWeightErr);                                                                                                                         
  }else{ // EVEN EVENT NUMBER CASE                                                                                                                                                                   
    fillWithOverFlow(histogram_EventNumber_,     1.,                  evtWeight,     evtWeightErr);     
  }      
}
