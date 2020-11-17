#ifndef hhAnalysis_multilepton_EventCategory_multiclass_h
#define hhAnalysis_multilepton_EventCategory_multiclass_h

/** \class EventCategory_multiclass
 *
 * Auxiliary class, to be used together DatacardHistManager_multiclass
 * when filling histograms for multiple event categories
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet

#include "tthAnalysis/HiggsToTauTau/interface/AnalysisConfig.h" // AnalysisConfig
#include "hhAnalysis/multilepton/interface/EventCategoryBase.h" // EventCategoryBase

#include <vector>
#include <string>

class EventCategory_multiclass 
  : public EventCategoryBase
{
 public:
  EventCategory_multiclass() {}
  virtual ~EventCategory_multiclass() {}

  virtual bool isSelected(int for_category, const std::string & for_class) const = 0;
};

#endif
