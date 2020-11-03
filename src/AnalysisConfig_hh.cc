#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h"

#include "FWCore/Utilities/interface/Exception.h" // cms::Exception

#include <TString.h> // Form

#include <iostream>
#include <iomanip>
#include <assert.h>

AnalysisConfig_hh::AnalysisConfig_hh(const std::string & analysis, const edm::ParameterSet & cfg)
  : AnalysisConfig(analysis, cfg)
{
  if      ( analysis == "HH->multilepton" ) analysis_ = kHH_multilepton;
  else if ( analysis == "HH->bbWW"        ) analysis_ = kHH_bbWW;
  else throw cmsException(this, _func_, _LINE_)
    << "Invalid Configuration parameter 'analysis' = " << analysis << " !!\n";

  decayModes_H_ = { "hww", "hzz", "htt", "hbb" };

  gen_mHH_ = cfg.getParameter<std::vector<double>>("gen_mHH");

  std::vector<double> nonRes_BMs = cfg.getParameter<std::vector<double>>("nonRes_BMs");
  for ( auto nonRes_BM : nonRes_BMs ) 
  {
    if ( nonRes_BM == 0 )
    {
      bmNames_.push_back("SM");
    }
    else
    {
      bmNames_.push_back(Form("BM%0.0f", nonRes_BM));
    }
  }

  if      ( analysis_ == kHH_multilepton ) decayModes_HH_ = { "tttt", "zzzz", "wwww", "ttzz", "ttww", "zzww" };
  else if ( analysis_ == kHH_bbWW        ) decayModes_HH_ = { "bbtt", "bbzz", "bbww" };
  else assert(0);
}

std::vector<double>
AnalysisConfig_hh::get_gen_mHH() const
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
