#include "hhAnalysis/multilepton/interface/EventInfoHH.h" // EventInfoHH

#include <cassert> // assert()

const std::map<std::string, Int_t> EventInfoHH::decayMode_idString_diHiggs_multilepton =
{
  { "tttt",       15 },
  { "zzzz",       23 },
  { "wwww",       24 },
  { "ttzz", 15000023 },
  { "ttww", 15000024 },
  { "zzww", 23000024 },
};

EventInfoHH::EventInfoHH()
  : EventInfoHH(false)
{}

EventInfoHH::EventInfoHH(bool is_mc,
                         bool is_signal,
                         bool is_hh_nonresonant)
  : EventInfo(is_mc, is_signal)
  , genDiHiggsDecayMode(-1)
  , is_hh_nonresonant_(is_hh_nonresonant)
{
  assert(is_mc_ || ! is_hh_nonresonant_);
}

EventInfoHH::EventInfoHH(const EventInfoHH & eventInfo)
{
  *this = eventInfo;
}

EventInfoHH &
EventInfoHH::operator=(const EventInfoHH & eventInfo)
{
  EventInfo::operator=(eventInfo);
  genDiHiggsDecayMode = eventInfo.genDiHiggsDecayMode;
  is_hh_nonresonant_ = eventInfo.is_hh_nonresonant_;
  return *this;
}

EventInfoHH::~EventInfoHH()
{}

bool
EventInfoHH::is_hh_nonresonant() const
{
  return is_hh_nonresonant_;
}

std::string
EventInfoHH::getDiHiggsDecayModeString() const
{
  return EventInfoHH::getDecayModeString(decayMode_idString_diHiggs_multilepton);
}

std::vector<std::string>
EventInfoHH::getDiHiggsDecayModes()
{
  return getDecayModes(decayMode_idString_diHiggs_multilepton);
}

