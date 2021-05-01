#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h"        // cmsException
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h" // format_vdouble

#include <TString.h> // Form

#include <iostream>
#include <iomanip>
#include <cmath>     // std::fabs
#include <algorithm> // std::sort
#include <assert.h>

AnalysisConfig_hh::AnalysisConfig_hh(const std::string & analysis, const edm::ParameterSet & cfg)
  : AnalysisConfig(analysis, cfg)
{
  if      ( analysis == "HH->multilepton" ) analysis_ = kHH_multilepton;
  else if ( analysis == "HH->bbWW"        ) analysis_ = kHH_bbWW;
  else throw cmsException(this, __func__, __LINE__)
    << "Invalid Configuration parameter 'analysis' = " << analysis << " !!\n";

  decayModes_H_ = { "hww", "hzz", "htt", "hbb" };

  gen_mHH_ = cfg.getParameter<std::vector<double>>("gen_mHH");
  if ( isMC_HH_resonant_ && mass_HH_resonant_ )
  {
    bool mass_HH_resonant_in_gen_mHH = false;
    for ( auto gen_mHH : gen_mHH_ )
    {
      if ( std::fabs(mass_HH_resonant_ - gen_mHH) < 1.e-1 )
      {
        mass_HH_resonant_in_gen_mHH = true;
        break;
      }
    }
    if ( !mass_HH_resonant_in_gen_mHH ) 
    {
      std::cerr << "Warning in <AnalysisConfig_hh>: Sample = " << process_string_ << " interpreted as resonant HH production with mass = " << mass_HH_resonant_ << "," << std::endl;
      std::cerr << " but no such mass-point included in Configuration parameter 'gen_mHH' = " << format_vdouble(gen_mHH_) << " in the python config."  << std::endl;
      std::cerr << "Adding the mass-point " << mass_HH_resonant_ << " manually." << std::endl;
      gen_mHH_.push_back(mass_HH_resonant_);
    }
  }
  std::sort(gen_mHH_.begin(), gen_mHH_.end());

  bmNames_ = cfg.getParameter<std::vector<std::string>>("nonRes_BMs");

  if      ( analysis_ == kHH_multilepton ) decayModes_HH_ = { "tttt", "zzzz", "wwww", "ttzz", "ttww", "zzww" };
  else if ( analysis_ == kHH_bbWW        ) decayModes_HH_ = { "bbtt", "bbzz", "bbww" };
  else assert(0);
}

std::vector<double>
AnalysisConfig_hh::get_HH_resonant_mass_points() const
{
  return gen_mHH_;
}

std::vector<std::string>
AnalysisConfig_hh::get_bmNames() const
{
  return bmNames_;
}

std::vector<std::string>
AnalysisConfig_hh::get_decayModes_HH() const
{
  return decayModes_HH_;
}
