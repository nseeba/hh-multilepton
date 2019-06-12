#include "hhAnalysis/multilepton/interface/EventInfoHHReader.h" // EventInfoHHReader

#include "hhAnalysis/multilepton/interface/EventInfoHH.h" // EventInfoHH

#include "tthAnalysis/HiggsToTauTau/interface/BranchAddressInitializer.h" // BranchAddressInitializer, TTree, Form()

EventInfoHHReader::EventInfoHHReader(PUsys puSys_option,
                                     bool read_genHiggsDecayMode,
                                     bool read_puWeight)
  : EventInfoHHReader(nullptr, puSys_option, read_genHiggsDecayMode, read_puWeight)
{}

EventInfoHHReader::EventInfoHHReader(EventInfoHH * info,
                                     PUsys puSys_option,
                                     bool read_genHiggsDecayMode,
                                     bool read_puWeight)
  : EventInfoReader(info, puSys_option, read_genHiggsDecayMode, read_puWeight)
  , info_hh_(info)
  , branchName_gen_mHH("mHH_lhe")
  , branchName_gen_cosThetaStar("cosThetaStar_lhe")
{}

void
EventInfoHHReader::setBranchAddresses(TTree * tree)
{
  EventInfoReader::setBranchAddresses(tree);
  if(info_hh_ -> is_hh_nonresonant())
  {
    BranchAddressInitializer bai(tree);
    bai.setBranchAddress(info_hh_ -> gen_mHH, branchName_gen_mHH);
    bai.setBranchAddress(info_hh_ -> gen_cosThetaStar, branchName_gen_cosThetaStar);
  }
}

void
EventInfoHHReader::setEventInfo(EventInfoHH * info)
{
  EventInfoReader::setEventInfo(info);
  info_hh_ = info;
}

