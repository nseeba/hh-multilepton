#include "hhAnalysis/multilepton/interface/EventCategoryBase.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()

EventCategoryBase::EventCategoryBase()
  : isInitialized_(false)
{}

const std::vector<std::string> &
EventCategoryBase::categoryNames() const
{
  return categoryNames_;
}

const std::vector<int> &
EventCategoryBase::categories() const
{
  return categories_;
}

const std::string &
EventCategoryBase::categoryName(int category) const
{
  std::map<int, std::string>::const_iterator categoryName = categoryMap_.find(category);
  if ( categoryName == categoryMap_.end() )
    throw cmsException(__func__, __LINE__) << "Invalid argument: " << category << " !!\n";
  return categoryName->second;
}

void
EventCategoryBase::initialize()
{
  for ( std::map<int, std::string>::const_iterator category = categoryMap_.begin();
        category != categoryMap_.end(); ++category ) {
    if ( category->first >= 0 ) // skip "undefined" category (which has value = -1)
    {
      categoryNames_.push_back(category->second);
      categories_.push_back(category->first);
    }
  }
}
