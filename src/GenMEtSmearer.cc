#include "hhAnalysis/multilepton/interface/GenMEtSmearer.h"

#include <TMath.h>

GenMEtSmearer::GenMEtSmearer(const edm::ParameterSet& cfg)
{ 
  sigmaX_ = cfg.getParameter<double>("sigmaX");
  sigmaY_ = cfg.getParameter<double>("sigmaY");

  rnd_.SetSeed(0);
}

GenMEtSmearer::~GenMEtSmearer()
{}

std::pair<double, double> GenMEtSmearer::operator()(double metPx, double metPy) const
{
  //std::cout << "<GenMEtSmearer::operator()>:" << std::endl;

  double metPx_smeared = rnd_.Gaus(metPx, sigmaX_);
  double metPy_smeared = rnd_.Gaus(metPy, sigmaY_);
  return std::pair<double, double>(metPx_smeared, metPy_smeared);
}
