#ifndef hhAnalysis_multilepton_DatacardHistManager_hh
#define hhAnalysis_multilepton_DatacardHistManager_hh

/** \class DatacardHistManager_hh
 *
 * Book and fill histograms of BDT output for non-resonant (SM and non-SM kinematics) and resonant (spin 0 and 2) HH analyses,
 * which are used for the signal extraction.
 * This class can be used for the HH->multilepton as well as for the HH->bbWW analysis.
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h"    // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h"          // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterface2.h" // HHWeightInterface2
#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h"     // AnalysisConfig_hh

#include <vector>
#include <map>

using namespace std;

class DatacardHistManager_hh
  : public HistManagerBase
{
public:
  DatacardHistManager_hh(const edm::ParameterSet & cfg,
                         const AnalysisConfig_hh & analysisConfig, 
                         const EventInfo & eventInfo, 
                         const HHWeightInterface2 * HHWeight_calc);
  ~DatacardHistManager_hh() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(const std::map<std::string, double> & bdtOutputs_resonant_spin2,
                 const std::map<std::string, double> & bdtOutputs_resonant_spin0,
                 const std::map<std::string, double> & bdtOutputs_nonresonant,
                 double evtWeight);

 private:
  const AnalysisConfig_hh & analysisConfig_;
  const EventInfo & eventInfo_;
  const HHWeightInterface2 * HHWeight_calc_;

  std::vector<double> resonant_gen_mHH_;
  std::vector<std::string> nonresonant_BMs_;
  std::vector<std::string> decayModes_;

  std::vector<string> histogramNames_bdtOutput_resonant_spin2_;
  std::vector<string> histogramNames_bdtOutput_resonant_spin0_;
  std::vector<string> histogramNames_bdtOutput_nonresonant_;

  int numBinsX_;
  double xMin_;
  double xMax_;

  std::map<std::string, std::map<std::string, TH1*>> histograms_bdtOutput_resonant_spin2_; // key = decayMode ("*" for data and background), histogramName
  std::map<std::string, std::map<std::string, TH1*>> histograms_bdtOutput_resonant_spin0_; // key = decayMode ("*" for data and background), histogramName
  std::map<std::string, std::map<std::string, TH1*>> histograms_bdtOutput_nonresonant_;    // key = decayMode ("*" for data and background), histogramName

  bool isDEBUG_;
};

#endif
