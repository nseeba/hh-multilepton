#ifndef hhAnalysis_multilepton_AnalysisConfig_hh_h
#define hhAnalysis_multilepton_AnalysisConfig_hh_h

/** \class AnalysisConfig_hh
 *
 * Parse process name and determine type of sample that is being processed.
 * The information on the type of sample being processed is used to configure 
 * the histogram booking & filling in the DatacardHistManager class,
 * such that only the histograms relevant for a given sample are booked & filled.
 * (In order to reduce the size of the ROOT files and make the hadd step faster and use less memory)
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet

#include "tthAnalysis/HiggsToTauTau/interface/AnalysisConfig.h"

#include <vector>
#include <string>

class AnalysisConfig_hh : public AnalysisConfig
{
 public:
  AnalysisConfig_hh(const std::string & analysis, const edm::ParameterSet & cfg);
  ~AnalysisConfig_hh() {}

  /// mass-points for resonant HH analysis
  std::vector<double> get_HH_resonant_mass_points() const;

  /// benchmark scenarios for coupling scan of non-resonant HH analysis
  std::vector<std::string> get_bmNames() const;

  /// decay modes considered for HH signal
  std::vector<std::string> get_decayModes_HH() const;

 private:
  enum { kHH_multilepton, kHH_bbWW };
  int analysis_;
  std::vector<double> gen_mHH_;
  std::vector<std::string> bmNames_;
  std::vector<std::string> decayModes_HH_;
};

#endif
