#include "hhAnalysis/multilepton/interface/HHGenKinematicsHistManager.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h"  // isHigherPt
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h"     // comp_cosThetaStar()

#include <algorithm> // std::sort

HHGenKinematicsHistManager::HHGenKinematicsHistManager(const edm::ParameterSet & cfg, 
                                                       const AnalysisConfig_hh & analysisConfig,
                                                       const EventInfo & eventInfo, 
                                                       const HHWeightInterfaceLO * HHWeightLO_calc,
                                                       const HHWeightInterfaceNLO * HHWeightNLO_calc)
  : HistManagerBase(cfg)
  , analysisConfig_(analysisConfig)
  , eventInfo_(eventInfo)
  , HHWeightLO_calc_(HHWeightLO_calc)
  , apply_HH_rwgt_lo_(HHWeightLO_calc_ != nullptr)
  , HHWeightNLO_calc_(HHWeightNLO_calc)
  , apply_HH_rwgt_nlo_(HHWeightNLO_calc_ != nullptr)
{
  central_or_shiftOptions_["gen_mHH"]             = { "central" };
  central_or_shiftOptions_["gen_absCosThetaStar"] = { "central" };
}

void
HHGenKinematicsHistManager::bookHistograms(TFileDirectory & dir)
{
  int numBins_gen_mHH = 36;
  double binning_gen_mHH[] = {
     250,  270,  290,  310,  330,  350,  370, 390,  410,  430, 
     450,  470,  490,  510,  530,  550,  570, 590,  610,  630, 
     650,  670,  700,  750,  800,  850,  900, 950, 1000, 1100, 
    1200, 1300, 1400, 1500, 1750, 2000, 5000
  };
  histogram_gen_mHH_             = book1D(dir, "gen_mHH",             "gen_mHH",             numBins_gen_mHH, binning_gen_mHH);
  histogram_gen_absCosThetaStar_ = book1D(dir, "gen_absCosThetaStar", "gen_absCosThetaStar", 10, 0.,   +1.);  
}

void
HHGenKinematicsHistManager::fillHistograms(double evtWeight)
{
  if ( analysisConfig_.isMC_HH_nonresonant() )
  {
    const double evtWeightErr = 0.;
    double HHReweight = 1.;

    if ( apply_HH_rwgt_lo_ )
    {
      assert(HHWeightLO_calc_);
      HHReweight = HHWeightLO_calc_->getRelativeWeight("SM", eventInfo_.gen_mHH, eventInfo_.gen_cosThetaStar, false);
    }
    if ( apply_HH_rwgt_nlo_ )
    {
      assert(HHWeightNLO_calc_);
      HHReweight *= HHWeightNLO_calc_->getRelativeWeight_V2("SM", eventInfo_.gen_mHH, eventInfo_.gen_cosThetaStar, false);
    }

    fillWithOverFlow(histogram_gen_mHH_, eventInfo_.gen_mHH, HHReweight*evtWeight, HHReweight*evtWeightErr);
    fillWithOverFlow(histogram_gen_absCosThetaStar_, eventInfo_.gen_cosThetaStar, HHReweight*evtWeight, HHReweight*evtWeightErr);
  }
}
