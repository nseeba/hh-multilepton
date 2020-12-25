#include "hhAnalysis/multilepton/interface/HHGenKinematicsHistManager.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h"  // isHigherPt
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h"     // comp_cosThetaStar()

#include <algorithm> // std::sort

HHGenKinematicsHistManager::HHGenKinematicsHistManager(const edm::ParameterSet & cfg, 
                                                       const AnalysisConfig_hh & analysisConfig,
                                                       const EventInfo & eventInfo, 
                                                       const HHWeightInterface2 * HHWeight_calc,
                                                       const HHWeightInterfaceLOtoNLO * HHWeight_calc_LOtoNLO)
  : HistManagerBase(cfg)
  , analysisConfig_(analysisConfig)
  , eventInfo_(eventInfo)
  , HHWeight_calc_(HHWeight_calc)
  , apply_HH_rwgt_(HHWeight_calc_ != nullptr)
  , HHWeight_calc_LOtoNLO_(HHWeight_calc_LOtoNLO)
  , apply_HH_rwgt_LOtoNLO_(HHWeight_calc_LOtoNLO_ != nullptr)
{
  central_or_shiftOptions_["gen_mHH"]             = { "central" };
  central_or_shiftOptions_["gen_absCosThetaStar"] = { "central" };
}

void
HHGenKinematicsHistManager::bookHistograms(TFileDirectory & dir)
{
  histogram_gen_mHH_             = book1D(dir, "gen_mHH",             "gen_mHH",             60, 0., 1200.);
  histogram_gen_absCosThetaStar_ = book1D(dir, "gen_absCosThetaStar", "gen_absCosThetaStar", 10, 0.,   +1.);  
}

void
HHGenKinematicsHistManager::fillHistograms(double evtWeight)
{
  if ( analysisConfig_.isMC_HH_nonresonant() && (apply_HH_rwgt_ || apply_HH_rwgt_LOtoNLO_) )
  {
    const double evtWeightErr = 0.;
    double HHReweight = 1.;

    if ( apply_HH_rwgt_ )
    {
      assert(HHWeight_calc_);
      HHReweight = HHWeight_calc_->getReWeight("SM", eventInfo_.gen_mHH, eventInfo_.gen_cosThetaStar, false);
    }
    if ( apply_HH_rwgt_LOtoNLO_ )
    {
      assert(HHWeight_calc_LOtoNLO_);
      HHReweight *= HHWeight_calc_LOtoNLO_->getReWeight("SM", eventInfo_.gen_mHH, eventInfo_.gen_cosThetaStar, false);
    }

    fillWithOverFlow(histogram_gen_mHH_, eventInfo_.gen_mHH, HHReweight*evtWeight, HHReweight*evtWeightErr);
    fillWithOverFlow(histogram_gen_absCosThetaStar_, eventInfo_.gen_cosThetaStar, HHReweight*evtWeight, HHReweight*evtWeightErr);
  }
}
