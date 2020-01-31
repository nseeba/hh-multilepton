#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_WjPlusLepton.h" // RecoJetSelectorAK8_hh_WjPlusLepton

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // kEra_*

#include "DataFormats/Math/interface/deltaR.h" // deltaR()

#include <TString.h> // Form()

RecoJetSelectorAK8_hh_WjPlusLepton::RecoJetSelectorAK8_hh_WjPlusLepton(int era, int index, bool debug)
  : min_pt_(-1.) // CV: only subjet pT cut is applied by default
  , max_absEta_(2.4)
  , max_dR_lepton_(0.1)
  , min_subJet_pt_(20.)
  , max_subJet_absEta_(2.4)
  , debug_(debug)
{
  switch(era)
  {
    case kEra_2016: min_jetId_ = 1; break; // 1 means loose
    case kEra_2018:
    case kEra_2017: min_jetId_ = 2; break; // 2 means tight (loose jet ID deprecated since 94x)
    default: throw cmsException(this) << "Implement me!";
  }
}

void
RecoJetSelectorAK8_hh_WjPlusLepton::set_min_pt(double min_pt)
{
  min_pt_ = min_pt;
}

void
RecoJetSelectorAK8_hh_WjPlusLepton::set_max_absEta(double max_absEta)
{
  max_absEta_ = max_absEta;
}

void
RecoJetSelectorAK8_hh_WjPlusLepton::set_max_dR_lepton(double max_dR_lepton)
{
  max_dR_lepton_ = max_dR_lepton;
}

void
RecoJetSelectorAK8_hh_WjPlusLepton::set_min_subJet_pt(double min_pt)
{
  min_subJet_pt_ = min_pt;
}

void
RecoJetSelectorAK8_hh_WjPlusLepton::set_max_subJet_absEta(double max_absEta)
{
  max_subJet_absEta_ = max_absEta;
}

void 
RecoJetSelectorAK8_hh_WjPlusLepton::set_min_jetId(int min_jetId)
{
  min_jetId_ = min_jetId;
}

void
RecoJetSelectorAK8_hh_WjPlusLepton::set_lepton(const RecoLepton * lepton) const
{
  leptons_ = { lepton };
}

void
RecoJetSelectorAK8_hh_WjPlusLepton::set_leptons(const std::vector<const RecoLepton *> & leptons) const
{
  leptons_ = leptons;
}

double
RecoJetSelectorAK8_hh_WjPlusLepton::get_min_pt() const
{
  return min_pt_;
}

double
RecoJetSelectorAK8_hh_WjPlusLepton::get_max_absEta() const
{
  return max_absEta_;
}

double
RecoJetSelectorAK8_hh_WjPlusLepton::get_max_dR_lepton() const
{
  return max_dR_lepton_;
}

double
RecoJetSelectorAK8_hh_WjPlusLepton::get_min_subJet_pt() const
{
  return min_subJet_pt_;
}

double
RecoJetSelectorAK8_hh_WjPlusLepton::get_max_subJet_absEta() const
{
  return max_subJet_absEta_;
}

int 
RecoJetSelectorAK8_hh_WjPlusLepton::get_min_jetId() const
{
  return min_jetId_;
}

bool
RecoJetSelectorAK8_hh_WjPlusLepton::operator()(const RecoJetAK8 & jet,
                                               std::string & returnType) const
{
  returnType = "";
  std::vector<const RecoSubjetAK8*> subJets;
  if ( jet.subJet1() ) subJets.push_back(jet.subJet1());
  if ( jet.subJet2() ) subJets.push_back(jet.subJet2());
  const RecoLepton * lepton = nullptr;
  double min_dR_lepton = 1.e+3;
  for(const RecoLepton * lepton_: leptons_)
  {
    for(const RecoSubjetAK8 * subJet: subJets)
    {
      const double dR_lepton = deltaR(subJet->p4(), lepton_->p4());
      if(dR_lepton < min_dR_lepton)
      {
        min_dR_lepton = dR_lepton;
        lepton = lepton_;
      }
    }
  }
  std::vector<const RecoSubjetAK8*> subJet_Wj;
  for(const RecoSubjetAK8 * subJet: subJets)
  {
    double min_dR = 1.e+3;
    for(const RecoLepton * lepton_: leptons_)
    {
      const double dR = deltaR(subJet->p4(), lepton_->p4());
      if(dR < min_dR)
      {
        min_dR = dR;
      }
    }
    if(min_dR >= max_dR_lepton_)
    {
      subJet_Wj.push_back(subJet);
    }
  }
  if(! lepton)
  {
    if(leptons_.size() == 0)
    {
      throw cmsException(this, __func__, __LINE__)
        << "Value of 'lepton' has not been set. Did you call the 'set_leptons' function prior to calling operator() ?"
      ;
    }
    if(debug_)
    {
      std::cout << "No lepton matches to subjets of the AK8 jet " << jet << '\n';
    }
    returnType = Form("FAILS dR(subjet,lepton) < %g cut", max_dR_lepton_);
    return false;
  }
  if(jet.pt() < min_pt_)
  {
    if( debug_)
    {
      std::cout << "FAILS pT = " << jet.pt() << " >= " << min_pt_ << " cut\n";
    }
    returnType = Form("FAILS pT >= %g cut", min_pt_);
    return false;
  }
  if(jet.absEta() > max_absEta_)
  {
    if(debug_)
    {
      std::cout << "FAILS abs(eta) = " << jet.absEta() << " <= " << max_absEta_ << " cut\n";
    }
    returnType = Form("FAILS abs(eta) <= %g cut", max_absEta_);
    return false;
  }
  if(jet.jetId() < min_jetId_)
  {
    if(debug_)
    {
      std::cout << "FAILS jet ID = " << jet.jetId() << " >= " << min_jetId_ << " cut\n";
    }
    returnType = Form("FAILS jet ID mod 4 >= %i cut", min_jetId_);
    return false;
  }
  if(min_dR_lepton > max_dR_lepton_)
  {
    if(debug_)
    {
      std::cout << "FAILS dR(lepton) = " << min_dR_lepton << " <= " << max_dR_lepton_ << " cut\n";
    }
    returnType = Form("FAILS dR(lepton) <= %g cut", max_dR_lepton_);
    return false;
  }
  if(! ((subJet_Wj.size() >= 1 && subJet_Wj[0]->pt() >= min_subJet_pt_ && subJet_Wj[0]->absEta() <= max_subJet_absEta_) ||
        (subJet_Wj.size() >= 2 && subJet_Wj[1]->pt() >= min_subJet_pt_ && subJet_Wj[1]->absEta() <= max_subJet_absEta_)) )
  {
    if(debug_)
    {
      std::cout << "FAILS subjet selection criteria\njet: " << jet;
      returnType = Form("FAILS subjet selection criteria");

      if(! ((subJet_Wj.size() >= 1 && subJet_Wj[0]->pt() >= min_subJet_pt_) ||
            (subJet_Wj.size() >= 2 && subJet_Wj[1]->pt() >= min_subJet_pt_)) )
      {
        returnType += Form("  pT < trsh");
      }
      if(! ((subJet_Wj.size() >= 1 && subJet_Wj[0]->absEta() <= max_subJet_absEta_) ||
            (subJet_Wj.size() >= 2 && subJet_Wj[1]->absEta() <= max_subJet_absEta_)) )
      {
        returnType += Form("  |eta| > trsh");
      }
    }
    return false;
  }

  return true;
}

bool
RecoJetSelectorAK8_hh_WjPlusLepton::operator()(const RecoJetAK8 & jet) const
{
  std::string returnType = "";
  return this->operator()(jet, returnType);
}
