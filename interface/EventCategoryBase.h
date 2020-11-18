#ifndef hhAnalysis_multilepton_EventCategoryBase_h
#define hhAnalysis_multilepton_EventCategoryBase_h

/** \class EventCategoryBase
 *
 * Base class for EventCategory and EventCategory_multiclass
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet

#include "tthAnalysis/HiggsToTauTau/interface/AnalysisConfig.h" // AnalysisConfig

#include <vector>
#include <string>

class EventCategoryBase
{
 public:
  EventCategoryBase();
  virtual ~EventCategoryBase() {}

  const std::vector<std::string> & categoryNames() const;
  const std::vector<int> & categories() const;

  const std::string & categoryName(int for_category) const;

 protected:
  void initialize();

  std::vector<std::string> categoryNames_;
  std::vector<int> categories_;
  std::map<int, std::string> categoryMap_;

  bool isInitialized_;
};

#endif
