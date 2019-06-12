#ifndef EventInfoHH_H
#define EventInfoHH_H

#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo

class EventInfoHH
  : public EventInfo
{
public:
  EventInfoHH();
  EventInfoHH(bool is_mc,
              bool is_signal = false,
              bool is_hh_nonresonant = false);
  EventInfoHH(const EventInfoHH & eventInfo);
  EventInfoHH &
  operator=(const EventInfoHH & eventInfo);

  ~EventInfoHH();

  Int_t   genDiHiggsDecayMode; ///< Decay mode of both Higgs bosons (only if HH signal MC)
  Float_t gen_mHH;             ///< LHE parton-level di-Higgs mass
  Float_t gen_cosThetaStar;    ///< LHE parton-level cos(theta*) variable

  bool
  is_hh_nonresonant() const;

  std::string
  getDiHiggsDecayModeString() const;

  static std::vector<std::string>
  getDiHiggsDecayModes();

  friend class EventInfoReaderHH;

protected:
  bool is_hh_nonresonant_;

  static const std::map<std::string, Int_t> decayMode_idString_diHiggs_multilepton;
};

#endif // EventInfoHH_H
