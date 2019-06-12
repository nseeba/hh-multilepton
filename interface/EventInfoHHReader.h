#ifndef EventInfoHHReader_H
#define EventInfoHHReader_H

#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h"

// forward declarations
class EventInfoHH;

class EventInfoHHReader
  : public virtual EventInfoReader
{
public:
  explicit EventInfoHHReader(PUsys puSys_option = PUsys::central,
                             bool read_genHiggsDecayMode = true,
                             bool read_puWeight = true);
  explicit EventInfoHHReader(EventInfoHH * info,
                             PUsys puSys_option = PUsys::central,
                             bool read_genHiggsDecayMode = true,
                             bool read_puWeight = true);
  ~EventInfoHHReader() override {}

  void
  setBranchAddresses(TTree * tree) override;

  void
  setEventInfo(EventInfoHH * info);

protected:
  EventInfoHH * info_hh_;

public:
  const std::string branchName_gen_mHH;
  const std::string branchName_gen_cosThetaStar;
};

#endif // EventInfoHHReader_H
