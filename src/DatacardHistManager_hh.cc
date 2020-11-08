#include "hhAnalysis/multilepton/interface/DatacardHistManager_hh.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h"          // cmsException
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h"   // format_vdouble(), format_vstring()

#include <TString.h> // Form

#include <string>
#include <map>

namespace
{
  void replaceAll(std::string& str, const std::string& from, const std::string& to)
  {
    if ( from.empty() ) return;
    size_t start_pos = str.find(from, start_pos);
    while ( start_pos != std::string::npos ) 
    {
      str.replace(start_pos, from.length(), to);
      start_pos += to.length(); // In case 'to' contains 'from', like replacing 'x' with 'yx'
      start_pos = str.find(from, start_pos);
    }
  }
}

DatacardHistManager_hh::DatacardHistManager_hh(const edm::ParameterSet & cfg,
                                               const AnalysisConfig_hh & analysisConfig, 
                                               const EventInfo & eventInfo, 
                                               const HHWeightInterface2 * HHWeight_calc,
                                               bool isDEBUG)
  : HistManagerBase(cfg)
  , analysisConfig_(analysisConfig)
  , eventInfo_(eventInfo)
  , HHWeight_calc_(HHWeight_calc)
  , apply_HH_rwgt_(HHWeight_calc_ != nullptr)
  , numBinsX_(100)
  , xMin_(0.)
  , xMax_(1.)
  , isDEBUG_(isDEBUG)
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
  for ( auto gen_mHH : resonant_gen_mHH_ ) 
  {
    if ( !(analysisConfig_.isMC_HH_nonresonant() || analysisConfig_.isMC_HH_resonant_spin0()) )
    {
      std::string histogramName_resonant_spin2 = Form("BDTOutput_%0.0f_hypo_spin2", gen_mHH);
      central_or_shiftOptions_[histogramName_resonant_spin2] = { "*" };
      histogramNames_bdtOutput_resonant_spin2_.push_back(histogramName_resonant_spin2);
    }
    if ( !(analysisConfig_.isMC_HH_nonresonant() || analysisConfig_.isMC_HH_resonant_spin2()) )
    {
      std::string histogramName_resonant_spin0 = Form("BDTOutput_%0.0f_hypo_spin0", gen_mHH);
      central_or_shiftOptions_[histogramName_resonant_spin0] = { "*" };
      histogramNames_bdtOutput_resonant_spin0_.push_back(histogramName_resonant_spin0);
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
  for ( auto BM : nonresonant_BMs_ ) 
  {
    std::string histogramName_nonresonant = Form("BDTOutput_%s", BM.data());
    central_or_shiftOptions_[histogramName_nonresonant] = { "*" };
    histogramNames_bdtOutput_nonresonant_.push_back(histogramName_nonresonant);
    std::string bmName = BM;
    bmNames_[histogramName_nonresonant] = bmName;
  }
  
  if ( analysisConfig_.isMC_HH_resonant() || analysisConfig_.isMC_HH_nonresonant() )
  {
    decayModeMap_["_tttt"] = { "tttt" };
    decayModeMap_["_wwww"] = { "zzzz", "wwww", "zzww" };
    decayModeMap_["_wwtt"] = { "ttzz", "ttww" };
    decayModeMap_["_bbtt"] = { "bbtt" };
    decayModeMap_["_bbvv"] = { "bbzz", "bbww" };
    bool is_known_decayMode = false;
    for ( auto decayModeIter : decayModeMap_ )
    {
      if ( process_.find(decayModeIter.first) != std::string::npos )
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
}

void
DatacardHistManager_hh::bookHistograms(TFileDirectory & dir)
{
  for ( auto decayMode : decayModes_ )
  {
    std::string process_and_decayMode;
    if ( decayMode != "*" ) 
    {
      bool is_known_decayMode = false;
      for ( auto decayModeIter : decayModeMap_ )
      {
        if ( process_.find(decayModeIter.first) != std::string::npos )
        {
          process_and_decayMode = process_;
          replaceAll(process_and_decayMode, decayModeIter.first, Form("_%s", decayMode.data()));
          is_known_decayMode = true;
          break;
        }
      }
      if ( !is_known_decayMode ) process_and_decayMode = Form("%s_%s", process_.data(), decayMode.data());
    }
    else 
    {
      process_and_decayMode = process_;
    }
    std::string processBAK = process_;
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

    process_ = processBAK;
  }
}

namespace
{
  std::vector<std::string>
  get_keys(const std::map<std::string, double> & bdtOutputs)
  {
    std::vector<std::string> keys;
    for ( auto bdtOutput : bdtOutputs )
    {
      keys.push_back(bdtOutput.first);
    }
    return keys;
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
    if ( decayMode == "*" || 
        (analysisConfig_.isMC_HH() && decayMode == eventInfo_.getDiHiggsDecayModeString()) || 
        (analysisConfig_.isMC_H()  && decayMode == eventInfo_.getDecayModeString())        )
    {
      for ( auto histogramName : histogramNames_bdtOutput_resonant_spin2_ )
      {
        TH1* histogram = histograms_bdtOutput_resonant_spin2_[decayMode][histogramName];
        std::map<std::string, double>::const_iterator bdtOutput = bdtOutputs_resonant_spin2.find(histogramName);
        if ( bdtOutput == bdtOutputs_resonant_spin2.end() )
          throw cmsException(this, __func__, __LINE__)
            << "No BDT output provided to fill histogram = '" << histogramName << "' !!\n"
            << "(available BDT outputs = " << format_vstring(get_keys(bdtOutputs_resonant_spin2)) << ")\n";
        fillWithOverFlow(histogram, bdtOutput->second, evtWeight, evtWeightErr);
      }
      for ( auto histogramName : histogramNames_bdtOutput_resonant_spin0_ )
      {
        TH1* histogram = histograms_bdtOutput_resonant_spin0_[decayMode][histogramName];
        std::map<std::string, double>::const_iterator bdtOutput = bdtOutputs_resonant_spin0.find(histogramName);
        if ( bdtOutput == bdtOutputs_resonant_spin0.end() )
          throw cmsException(this, __func__, __LINE__)
            << "No BDT output provided to fill histogram = '" << histogramName << "' !!\n"
            << "(available BDT outputs = " << format_vstring(get_keys(bdtOutputs_resonant_spin0)) << ")\n";
        fillWithOverFlow(histogram, bdtOutput->second, evtWeight, evtWeightErr);
      }

      for ( auto histogramName : histogramNames_bdtOutput_nonresonant_ )
      {
        TH1* histogram = histograms_bdtOutput_nonresonant_[decayMode][histogramName];
        std::map<std::string, double>::const_iterator bdtOutput = bdtOutputs_nonresonant.find(histogramName);
        if ( bdtOutput == bdtOutputs_nonresonant.end() )
          throw cmsException(this, __func__, __LINE__)
            << "No BDT output provided to fill histogram = '" << histogramName << "' !!\n"
            << "(available BDT outputs = " << format_vstring(get_keys(bdtOutputs_nonresonant)) << ")\n";
        double evtWeight_reweighted = evtWeight;
        double evtWeightErr_reweighted = evtWeightErr;
        if ( analysisConfig_.isMC_HH_nonresonant() && apply_HH_rwgt_ )
        {
          std::map<std::string, std::string>::const_iterator bmName = bmNames_.find(histogramName);
          if ( bmName == bmNames_.end() )
            throw cmsException(this, __func__, __LINE__)
              << "No non-resonant HH benchmark scenario available to fill histogram = '" << histogramName << "' !!\n";
          assert(HHWeight_calc_);
          double hh_reweight = HHWeight_calc_->getReWeight(bmName->second, eventInfo_.gen_mHH, eventInfo_.gen_cosThetaStar, isDEBUG_);        
          evtWeight_reweighted *= hh_reweight;
          evtWeightErr_reweighted *= hh_reweight;
        }
        fillWithOverFlow(histogram, bdtOutput->second, evtWeight_reweighted, evtWeightErr_reweighted);
      }
    }
  }
}
