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
HHGenKinematicsHistManager::fillHistograms(const std::vector<LHEParticle> & lheParticles, double evtWeight)
{
  const double evtWeightErr = 0.;

  std::vector<const LHEParticle*> lheHiggsBosons;
  for ( std::vector<LHEParticle>::const_iterator lheParticle = lheParticles.begin();
        lheParticle != lheParticles.end(); ++lheParticle ) {
    if ( lheParticle->pdgId() == 25 && lheParticle->status() == 1 )
    {
      lheHiggsBosons.push_back(&(*lheParticle));
    }
  }
  std::sort(lheHiggsBosons.begin(), lheHiggsBosons.end(), isHigherPt);

  if ( lheHiggsBosons.size() == 2 )
  {
    const LHEParticle* lheHiggsBoson_lead    = lheHiggsBosons[0];
    const LHEParticle* lheHiggsBoson_sublead = lheHiggsBosons[1];

    double HHReweight = 1.;
    if ( analysisConfig_.isMC_HH_nonresonant() && (apply_HH_rwgt_ || apply_HH_rwgt_LOtoNLO_) )
    {
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
    }

    double gen_mHH = (lheHiggsBoson_lead->p4() + lheHiggsBoson_sublead->p4()).mass();    
    //std::cout << "gen_mHH = " << gen_mHH << ": eventInfo_.gen_mHH = " << eventInfo_.gen_mHH << std::endl;
    fillWithOverFlow(histogram_gen_mHH_, gen_mHH, HHReweight*evtWeight, HHReweight*evtWeightErr);

    double gen_absCosThetaStar = std::fabs(comp_cosThetaStar(lheHiggsBoson_lead->p4(), lheHiggsBoson_sublead->p4()));
    //std::cout << "gen_absCosThetaStar = " << gen_absCosThetaStar << ": eventInfo_.gen_cosThetaStar = " << eventInfo_.gen_cosThetaStar << std::endl;
    fillWithOverFlow(histogram_gen_absCosThetaStar_, gen_absCosThetaStar, HHReweight*evtWeight, HHReweight*evtWeightErr);
  }
}
