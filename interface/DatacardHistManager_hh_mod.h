#ifndef hhAnalysis_multilepton_DatacardHistManager_hh_mod_h
#define hhAnalysis_multilepton_DatacardHistManager_hh_mod_h

/** \class DatacardHistManager_hh
 *
 * Book and fill histograms of BDT output for non-resonant (SM and non-SM kinematics) and resonant (spin 0 and 2) HH analyses.
 * The code supports multiple event categories.
 * This class can be used for the HH->multilepton as well as for the HH->bbWW analysis.
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h"         // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h"               // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceLO.h"     // HHWeightInterfaceLO
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceNLO.h"    // HHWeightInterfaceNLO
#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h"          // AnalysisConfig_hh
#include "hhAnalysis/multilepton/interface/DatacardHistManagerBase_hh.h" // DatacardHistManagerBase_hh
#include "hhAnalysis/multilepton/interface/EventCategory.h"              // EventCategory

#include <vector>
#include <map>
#include <TH2.h>

using namespace std;

class DatacardHistManager_hh_mod
  : public DatacardHistManagerBase_hh
{
 public:
  DatacardHistManager_hh_mod(const edm::ParameterSet & cfg,
                         const AnalysisConfig_hh & analysisConfig, 
                         const EventInfo & eventInfo, 
                         const HHWeightInterfaceLO * HHWeightLO_calc,
                         const HHWeightInterfaceNLO * HHWeightNLO_calc,
                         bool isDEBUG = false,
                         bool fillHistograms_nonresonant = true, bool fillHistograms_resonant_spin0 = true, bool fillHistograms_resonant_spin2 = true, bool overlap=false,
                         bool use2d=true);
  DatacardHistManager_hh_mod(const edm::ParameterSet & cfg,
                         const AnalysisConfig_hh & analysisConfig, 
                         const EventInfo & eventInfo, 
                         const HHWeightInterfaceLO * HHWeightLO_calc,
                         const HHWeightInterfaceNLO * HHWeightNLO_calc,
                         const EventCategory * eventCategory,
                         bool isDEBUG = false,
                         bool fillHistograms_nonresonant = true, bool fillHistograms_resonant_spin0 = true, bool fillHistograms_resonant_spin2 = true, bool overlap=false,
                         bool use2d=true);

  ~DatacardHistManager_hh_mod() {}

  /// fill histograms
  // void
  // fillHistograms(const std::map<std::string, double> & mvaOutputs_resonant_spin2,
  //                const std::map<std::string, double> & mvaOutputs_resonant_spin0,
  //                const std::map<std::string, double> & mvaOutputs_nonresonant,
  //                double mvaOutput_nonresonant_allBMs,
  //                double evtWeight);
  void
  fillHistograms(const std::map<std::string, double> & mvaOutputs_nonresonant,
                 const std::map<std::string, double> & vbfOutputs_nonresonant,
                 double mvaOutput_nonresonant_allBMs,
                 double evtWeight);
 private:
  const EventCategory * eventCategory_;
};

#endif
