#include "hhAnalysis/multilepton/interface/DatacardHistManager_hh.h"

#include "FWCore/Utilities/interface/Exception.h" // cms::Exception

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()

#include <TString.h> // Form

#include <string>
#include <map>

DatacardHistManager_hh::DatacardHistManager_hh(const edm::ParameterSet & cfg,
                                               const AnalysisConfig_hh & analysisConfig, 
                                               const EventInfo & eventInfo, 
                                               const HHWeightInterface2 * HHWeight_calc)
  : HistManagerBase(cfg)
  , analysisConfig_(analysisConfig)
  , eventInfo_(eventInfo)
  , HHWeight_calc_(HHWeight_calc)
  , numBinsX_(100)
  , xMin_(0.)
  , xMax_(1.)
  , isDEBUG_(cfg.getParameter<bool>("isDEBUG"))
{
  if ( !analysisConfig_.isMC_HH_nonresonant() )
  {
    resonant_gen_mHH_ = analysisConfig_.get_gen_mHH();
  }
  for ( auto gen_mHH : resonant_gen_mHH_ ) 
  {
    std::string histogramName_resonant_spin2 = Form("BDTOutput_%0.0f_hypo_spin2", gen_mHH);
    central_or_shiftOptions_[histogramName_resonant_spin2] = { "*" };
    histogramNames_bdtOutput_resonant_spin2_.push_back(histogramName_resonant_spin2);
    std::string histogramName_resonant_spin0 = Form("BDTOutput_%0.0f_hypo_spin0", gen_mHH);
    central_or_shiftOptions_[histogramName_resonant_spin0] = { "*" };
    histogramNames_bdtOutput_resonant_spin0_.push_back(histogramName_resonant_spin0);
  }

  if ( !analysisConfig_.isMC_HH_resonant() )
  {
    nonresonant_BMs_ = analysisConfig_.get_bmNames();
  }
  for ( auto BM : nonresonant_BMs_ ) 
  {
    std::string histogramName_nonresonant = Form("BDTOutput_%s", BM.data());
    central_or_shiftOptions_[histogramName_nonresonant] = { "*" };
    histogramNames_bdtOutput_nonresonant_.push_back(histogramName_nonresonant);
  }
  
  if ( analysisConfig_.isMC_HH_resonant() || analysisConfig_.isMC_HH_nonresonant() )
  {
    decayModes_ = analysisConfig_.get_decayModes_HH();
  }
  else if ( analysisConfig_.isMC_H() )
  {
    decayModes_ = analysisConfig_.get_decayModes_H();
  }
  else
  {
    decayModes_.push_back("*");
  } 
}

void
DatacardHistManager_hh::bookHistograms(TFileDirectory & dir)
{
  for ( auto decayMode : decayModes_ )
  {
    std::string process_and_decayMode;
    if ( decayMode != "*" ) process_and_decayMode = Form("%s_%s", analysisConfig_.process().data(), decayMode.data());
    else process_and_decayMode = analysisConfig_.process();
    process_ = process_and_decayMode;

    for ( auto histogramName : histogramNames_bdtOutput_resonant_spin2_ )
    {
      TH1* histogram = book1D(dir, histogramName, histogramName, numBinsX_, xMin_, xMax_);
      histograms_bdtOutput_resonant_spin2_[decayMode][histogramName] = histogram; 
    }
    for ( auto histogramName : histogramNames_bdtOutput_resonant_spin0_ )
    {
      TH1* histogram = book1D(dir, histogramName, histogramName, numBinsX_, xMin_, xMax_);
      histograms_bdtOutput_resonant_spin0_[decayMode][histogramName] = histogram; 
    }
      
    for ( auto histogramName : histogramNames_bdtOutput_nonresonant_ )
    {
      TH1* histogram = book1D(dir, histogramName, histogramName, numBinsX_, xMin_, xMax_);
      histograms_bdtOutput_nonresonant_[decayMode][histogramName] = histogram; 
    }
  }
}

void
DatacardHistManager_hh::fillHistograms(const std::map<std::string, double> & bdtOutputs_resonant_spin2,
                                       const std::map<std::string, double> & bdtOutputs_resonant_spin0,
                                       const std::map<std::string, double> & bdtOutputs_nonresonant,
                                       double evtWeight)
{
  const double evtWeightErr = 0.;

  for ( auto decayMode : decayModes_ )
  {
    if ( decayMode == "*" || decayMode == eventInfo_.getDiHiggsDecayModeString() )
    {
      for ( auto histogramName : histogramNames_bdtOutput_resonant_spin2_ )
      {
        TH1* histogram = histograms_bdtOutput_resonant_spin2_[decayMode][histogramName];
        std::map<std::string, double>::const_iterator bdtOutput = bdtOutputs_resonant_spin2.find(histogramName);
        if ( bdtOutput == bdtOutputs_resonant_spin2.end() )
          throw cmsException(this, _func_, _LINE_)
            << "No BDT output provided to fill histogram = '" << histogram << "' !!\n";
        fillWithOverFlow(histogram, bdtOutput->second, evtWeight, evtWeightErr);
      }
      for ( auto histogramName : histogramNames_bdtOutput_resonant_spin0_ )
      {
        TH1* histogram = histograms_bdtOutput_resonant_spin0_[decayMode][histogramName];
        std::map<std::string, double>::const_iterator bdtOutput = bdtOutputs_resonant_spin0.find(histogramName);
        if ( bdtOutput == bdtOutputs_resonant_spin0.end() )
          throw cmsException(this, _func_, _LINE_)
            << "No BDT output provided to fill histogram = '" << histogram << "' !!\n";
        fillWithOverFlow(histogram, bdtOutput->second, evtWeight, evtWeightErr);
      }

      for ( auto histogramName : histogramNames_bdtOutput_nonresonant_ )
      {
        TH1* histogram = histograms_bdtOutput_nonresonant_[decayMode][histogramName];
        std::map<std::string, double>::const_iterator bdtOutput = bdtOutputs_nonresonant.find(histogramName);
        if ( bdtOutput == bdtOutputs_nonresonant.end() )
          throw cmsException(this, _func_, _LINE_)
            << "No BDT output provided to fill histogram = '" << histogram << "' !!\n";
        double hh_reweight = HHWeight_calc_->getReWeight(histogramName, eventInfo_.gen_mHH, eventInfo_.gen_cosThetaStar, isDEBUG_);        
        double evtWeight_reweighted = evtWeight*hh_reweight;
        double evtWeightErr_reweighted = evtWeight*hh_reweight;
        fillWithOverFlow(histogram, bdtOutput->second, evtWeight_reweighted, evtWeightErr_reweighted);
      }
    }
  }
}
