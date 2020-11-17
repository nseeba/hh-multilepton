#ifndef hhAnalysis_multilepton_EventCategory_h
#define hhAnalysis_multilepton_EventCategory_h

/** \class EventCategory
 *
 * Auxiliary class, to be used together DatacardHistManager
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

class EventCategory 
  : public EventCategoryBase
{
 public:
  EventCategory() {}
  virtual ~EventCategory() {}

  virtual bool isSelected(int for_category) const = 0;
};

#endif
