#include "hhAnalysis/multilepton/interface/HHGenKinematicsHistManager.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h"  // isHigherPt
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h"     // comp_cosThetaStar()

#include <algorithm> // std::sort

HHGenKinematicsHistManager::HHGenKinematicsHistManager(const edm::ParameterSet & cfg, 
                                                       const AnalysisConfig_hh & analysisConfig,
                                                       const EventInfo & eventInfo,
						       const HHWeightInterfaceCouplings * hhWeight_couplings,
                                                       const HHWeightInterfaceLO * HHWeightLO_calc,
                                                       const HHWeightInterfaceNLO * HHWeightNLO_calc)
  : HistManagerBase(cfg)
  , analysisConfig_(analysisConfig)
  , eventInfo_(eventInfo)
  , hhWeight_couplings_(hhWeight_couplings)
  , HHWeightLO_calc_(HHWeightLO_calc)
  , apply_HH_rwgt_lo_(HHWeightLO_calc_ != nullptr)
  , HHWeightNLO_calc_(HHWeightNLO_calc)
  , apply_HH_rwgt_nlo_(HHWeightNLO_calc_ != nullptr)
{
  if (hhWeight_couplings_  != nullptr)
  {
    HHWeightNames_ = hhWeight_couplings_->get_weight_names();
    HHBMNames_ = hhWeight_couplings_->get_bm_names();
  }
  for (size_t iBM = 0; iBM < HHBMNames_.size(); iBM++)
  {
    central_or_shiftOptions_[Form("gen_mHH_%s",HHBMNames_[iBM].c_str())]             = { "central" };
    central_or_shiftOptions_[Form("gen_absCosThetaStar_%s",HHBMNames_[iBM].c_str())] = { "central" };
  }
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
  int numBins_gen_absCosThetaStar = 4;
  double binning_gen_absCosThetaStar[] = { 0.0, 0.4, 0.6, 0.8, 1.0  };

  histograms_gen_mHH_ = new TH1*[HHBMNames_.size()];
  histograms_gen_absCosThetaStar_ = new TH1*[HHBMNames_.size()];
  for (size_t iBM = 0; iBM < HHBMNames_.size(); iBM++)
  {
    histograms_gen_mHH_[iBM]             = book1D(dir, Form("gen_mHH_%s",HHBMNames_[iBM].c_str()),             Form("gen_mHH_%s",HHBMNames_[iBM].c_str()),             numBins_gen_mHH, binning_gen_mHH);
    histograms_gen_absCosThetaStar_[iBM] = book1D(dir, Form("gen_absCosThetaStar_%s",HHBMNames_[iBM].c_str()), Form("gen_absCosThetaStar_%s",HHBMNames_[iBM].c_str()), numBins_gen_absCosThetaStar, binning_gen_absCosThetaStar);
  }
}

void
HHGenKinematicsHistManager::fillHistograms(double evtWeight)
{
  if ( analysisConfig_.isMC_HH_nonresonant() )
  {
    for (size_t iBM = 0; iBM < HHBMNames_.size(); iBM++)
    {
      const double evtWeightErr = 0.;
      double HHReweight = 1.;

      if ( apply_HH_rwgt_lo_ )
      {
	assert(HHWeightLO_calc_);
	HHReweight = HHWeightLO_calc_->getRelativeWeight(HHBMNames_[iBM], eventInfo_.gen_mHH, eventInfo_.gen_cosThetaStar, false);
      }
      if ( apply_HH_rwgt_nlo_ )
      {
	assert(HHWeightNLO_calc_);
	//HHReweight *= HHWeightNLO_calc_->getRelativeWeight_LOtoNLO_V2("SM", eventInfo_.gen_mHH, eventInfo_.gen_cosThetaStar, false);
	HHReweight *= HHWeightNLO_calc_->getRelativeWeight_LOtoNLO(HHBMNames_[iBM], eventInfo_.gen_mHH, eventInfo_.gen_cosThetaStar, false); // always 1 for "SM"      
      }
    
      fillWithOverFlow(histograms_gen_mHH_[iBM], eventInfo_.gen_mHH, HHReweight*evtWeight, HHReweight*evtWeightErr);
      fillWithOverFlow(histograms_gen_absCosThetaStar_[iBM], eventInfo_.gen_cosThetaStar, HHReweight*evtWeight, HHReweight*evtWeightErr);
    }
  }
}
