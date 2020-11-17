#include "hhAnalysis/multilepton/interface/DatacardHistManagerBase_hh.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h"          // cmsException
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h"   // format_vdouble(), format_vstring()

#include <TString.h> // Form

#include <boost/algorithm/string/replace.hpp> // boost::replace_all()

#include <string>
#include <map>

DatacardHistManagerBase_hh::DatacardHistManagerBase_hh(const edm::ParameterSet & cfg,
                                                       const AnalysisConfig_hh & analysisConfig, 
                                                       const EventInfo & eventInfo, 
                                                       const HHWeightInterface2 * HHWeight_calc,
                                                       bool isDEBUG)
  : HistManagerBase(cfg)
  , analysisConfig_(analysisConfig)
  , eventInfo_(eventInfo)
  , HHWeight_calc_(HHWeight_calc)
  , apply_HH_rwgt_(HHWeight_calc_ != nullptr)
  , eventCategoryBase_(nullptr)
  , numBinsX_(100)
  , xMin_(0.)
  , xMax_(1.)
  , isDEBUG_(isDEBUG)
{}

DatacardHistManagerBase_hh::DatacardHistManagerBase_hh(const edm::ParameterSet & cfg,
                                                       const AnalysisConfig_hh & analysisConfig, 
                                                       const EventInfo & eventInfo, 
                                                       const HHWeightInterface2 * HHWeight_calc,
                                                       const EventCategoryBase * eventCategoryBase,
                                                       bool isDEBUG)
  : HistManagerBase(cfg)
  , analysisConfig_(analysisConfig)
  , eventInfo_(eventInfo)
  , HHWeight_calc_(HHWeight_calc)
  , apply_HH_rwgt_(HHWeight_calc_ != nullptr)
  , eventCategoryBase_(eventCategoryBase)
  , numBinsX_(100)
  , xMin_(0.)
  , xMax_(1.)
  , isDEBUG_(isDEBUG)
{}

void
DatacardHistManagerBase_hh::initialize()
{
  if ( central_or_shift_ == "central" )
  {
    std::cout << "<DatacardHistManager_hh>: booking histograms for process = '" << process_ << "'" << std::endl;
  }

  if ( analysisConfig_.isMC_HH_resonant() )
  {
    resonant_gen_mHH_ = { analysisConfig_.get_HH_resonant_mass() };
  }
  else if ( !analysisConfig_.isMC_HH_nonresonant() )
  {
    resonant_gen_mHH_ = analysisConfig_.get_HH_resonant_mass_points();
  }
  if ( central_or_shift_ == "central" )
  {
    std::cout << " using resonant HH mass-points = " << format_vdouble(resonant_gen_mHH_) << std::endl;
  }
  for ( const auto & gen_mHH : resonant_gen_mHH_ )
  {
    if ( !(analysisConfig_.isMC_HH_nonresonant() || analysisConfig_.isMC_HH_resonant_spin0()) )
    {
      std::string histogramName_resonant_spin2 = Form("MVAOutput_%0.0f_spin2", gen_mHH);
      central_or_shiftOptions_[histogramName_resonant_spin2] = { "*" };
      std::string key_resonant_spin2 = Form("%0.0f_spin2", gen_mHH);
      histogramNames_mvaOutput_resonant_spin2_[key_resonant_spin2] = histogramName_resonant_spin2;
    }
    if ( !(analysisConfig_.isMC_HH_nonresonant() || analysisConfig_.isMC_HH_resonant_spin2()) )
    {
      std::string histogramName_resonant_spin0 = Form("MVAOutput_%0.0f_spin0", gen_mHH);
      central_or_shiftOptions_[histogramName_resonant_spin0] = { "*" };
      std::string key_resonant_spin0 = Form("%0.0f_spin0", gen_mHH);
      histogramNames_mvaOutput_resonant_spin0_[key_resonant_spin0] = histogramName_resonant_spin0;
    }
  }

  if ( !analysisConfig_.isMC_HH_resonant() )
  {
    nonresonant_BMs_ = analysisConfig_.get_bmNames();
  }
  if ( central_or_shift_ == "central" )
  {
    std::cout << " using non-resonant HH benchmark scenarios = " << format_vstring(nonresonant_BMs_) << std::endl;
  }
  for ( const auto & BM : nonresonant_BMs_ )
  {
    std::string histogramName_nonresonant = Form("MVAOutput_%s", BM.data());
    central_or_shiftOptions_[histogramName_nonresonant] = { "*" };
    std::string key_nonresonant = BM;
    histogramNames_mvaOutput_nonresonant_[key_nonresonant] = histogramName_nonresonant;
  }
  
  if ( analysisConfig_.isMC_HH_resonant() || analysisConfig_.isMC_HH_nonresonant() )
  {
    decayModeMap_["_tttt"] = { "tttt" };
    decayModeMap_["_wwww"] = { "zzzz", "wwww", "zzww" };
    decayModeMap_["_wwtt"] = { "ttzz", "ttww" };
    decayModeMap_["_bbtt"] = { "bbtt" };
    decayModeMap_["_bbvv"] = { "bbzz", "bbww" };

    bool is_known_decayMode = false;
    const std::string process_hh = analysisConfig_.process_hh();
    for ( const auto & decayModeIter : decayModeMap_ )
    {
      if ( process_hh.find(decayModeIter.first) != std::string::npos )
      {
        decayModes_ = decayModeIter.second;
        is_known_decayMode = true;
        break;
      }
    }
    if ( !is_known_decayMode ) decayModes_ = analysisConfig_.get_decayModes_HH();

    if ( central_or_shift_ == "central" )
    {
      std::cout << " using HH decay modes = " << format_vstring(decayModes_) << std::endl;
    }
    // CV: book & fill extra histogram for HH signal without splitting by decay mode
    decayModes_.push_back("*");
  }
  else if ( analysisConfig_.isMC_H() )
  {
    productionModeMap_["VH"] = { "WH", "ZH" };
    const std::string process = analysisConfig_.process();
    for ( const auto & decayModeIter : productionModeMap_ )
    {
      if ( process.find(decayModeIter.first) != std::string::npos )
      {
        productionModes_ = decayModeIter.second;
        break;
      }
    }

    decayModes_ = analysisConfig_.get_decayModes_H();
    if ( central_or_shift_ == "central" )
    {
      std::cout << " using H decay modes = " << format_vstring(decayModes_) << std::endl;
    }
    // CV: book & fill extra histogram for H signal without splitting by decay mode
    decayModes_.push_back("*");
  }
  else
  {
    decayModes_.push_back("*");
  }
  productionModes_.push_back("*");
}

void
DatacardHistManagerBase_hh::bookHistograms(TFileDirectory & dir)
{
  const std::string process = analysisConfig_.process();
  const std::string process_hh = analysisConfig_.process_hh();
  for ( auto category: categories_ )
  {
    categoryEntryType categoryEntry;

    for ( const auto & decayMode: decayModes_ )
    {
      std::string process_and_decayMode;
      if ( decayMode != "*" ) 
      {
        bool is_known_decayMode = false;
        for ( const auto & decayModeIter : decayModeMap_ )
        {
          if ( process_hh.find(decayModeIter.first) != std::string::npos )
          {
            process_and_decayMode = process_;
            boost::replace_all(process_and_decayMode, process, process_hh);
            boost::replace_all(process_and_decayMode, decayModeIter.first, Form("_%s", decayMode.data()));
            is_known_decayMode = true;
            break;
          }
        }
        if ( !is_known_decayMode )
        {
          process_and_decayMode = process_;
          boost::replace_all(process_and_decayMode, process_hh, Form("%s_%s", process_hh.data(), decayMode.data()));
        }
      }
      else 
      {
        process_and_decayMode = process_;
      }
      for( auto productionMode: productionModes_ )
      {
        std::string process_production_and_decayMode = process_and_decayMode;
        if( productionMode != "*" )
        {
          boost::replace_all(process_production_and_decayMode, analysisConfig_.process(), productionMode);
        }

        const std::string processBAK = process_;

        process_ = "";
        if ( category != -1 )
        {
          assert(eventCategoryBase_);
          process_ += Form("%s/", eventCategoryBase_->categoryName(category).data());
        }
        process_ += process_production_and_decayMode;

        for ( std::map<std::string, std::string>::const_iterator histogramName = histogramNames_mvaOutput_resonant_spin2_.begin();
              histogramName != histogramNames_mvaOutput_resonant_spin2_.end(); ++histogramName ) {
          TH1* histogram = book1D(dir, histogramName->second, histogramName->second, numBinsX_, xMin_, xMax_);
          categoryEntry.histograms_mvaOutput_resonant_spin2_[productionMode][decayMode][histogramName->first] = histogram;
        }
        for ( std::map<std::string, std::string>::const_iterator histogramName = histogramNames_mvaOutput_resonant_spin0_.begin();
              histogramName != histogramNames_mvaOutput_resonant_spin0_.end(); ++histogramName ) {
          TH1* histogram = book1D(dir, histogramName->second, histogramName->second, numBinsX_, xMin_, xMax_);
          categoryEntry.histograms_mvaOutput_resonant_spin0_[productionMode][decayMode][histogramName->first] = histogram;
        }

        for ( std::map<std::string, std::string>::const_iterator histogramName = histogramNames_mvaOutput_nonresonant_.begin();
              histogramName != histogramNames_mvaOutput_nonresonant_.end(); ++histogramName ) {
          TH1* histogram = book1D(dir, histogramName->second, histogramName->second, numBinsX_, xMin_, xMax_);
          categoryEntry.histograms_mvaOutput_nonresonant_[productionMode][decayMode][histogramName->first] = histogram;
        }

        process_ = processBAK;
      }
    }

    categoryEntry.category_ = category;
    histograms_in_categories_.push_back(categoryEntry);
  }
}

void
DatacardHistManagerBase_hh::compHHReweightMap()
{
  if ( analysisConfig_.isMC_HH_nonresonant() && apply_HH_rwgt_ )
  {
    for ( std::map<std::string, std::string>::const_iterator histogramName = histogramNames_mvaOutput_nonresonant_.begin();
          histogramName != histogramNames_mvaOutput_nonresonant_.end(); ++histogramName ) {
      const std::string& bmName = histogramName->first;
      assert(HHWeight_calc_);
      double HHReweight = HHWeight_calc_->getReWeight(bmName, eventInfo_.gen_mHH, eventInfo_.gen_cosThetaStar, isDEBUG_);
      HHReweightMap_[histogramName->first] = HHReweight;
    }
  }
}
