#include "hhAnalysis/multilepton/interface/RecoMuonCollectionSelectorTight_hh_multilepton.h" // RecoMuonSelectorTight_hh_multilepton

#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // kEra_*
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()

RecoMuonSelectorTight_hh_multilepton::RecoMuonSelectorTight_hh_multilepton(Era era,
                                                   int index,
                                                   bool debug,
                                                   bool set_selection_flags)
  : era_(era)
  , debug_(debug)
  , set_selection_flags_(set_selection_flags)
  , min_lepton_pt_(5.) // L
  , min_cone_pt_(10.) // F
  , max_absEta_(2.4) // L
  , max_dxy_(0.05) // L
  , max_dz_(0.1) // L
  , max_relIso_(0.4) // L
  , max_sip3d_(8.) // L
  , apply_looseIdPOG_(true) // L
  , apply_mediumIdPOG_(true) // T
  , min_jetPtRatio_(2. / 3) // F
  , min_jetBtagCSV_(get_BtagWP(era_, Btag::kDeepJet, BtagWP::kLoose)) // F
  , max_jetBtagCSV_(get_BtagWP(era_, Btag::kDeepJet, BtagWP::kMedium)) // F
  , smoothBtagCut_minPt_(20.)
  , smoothBtagCut_maxPt_(45.)
  , smoothBtagCut_ptDiff_(smoothBtagCut_maxPt_ - smoothBtagCut_minPt_)
  , apply_jetBtagCSVLoose_(false)
  , apply_jetBtagCSVInterp_(true)
{
  // L -- inherited from the preselection (loose cut)
  // F -- additional fakeable cut not applied in the preselection
  // T -- additional tight cut not applied in the fakeable selection
}

void
RecoMuonSelectorTight_hh_multilepton::set_min_lepton_pt(double min_lepton_pt)
{
  min_lepton_pt_ = min_lepton_pt;
}

void
RecoMuonSelectorTight_hh_multilepton::set_min_cone_pt(double min_cone_pt)
{
  min_cone_pt_ = min_cone_pt;
}

void
RecoMuonSelectorTight_hh_multilepton::set_max_absEta(double max_absEta)
{
  max_absEta_ = max_absEta;
}

void
RecoMuonSelectorTight_hh_multilepton::set_selection_flags(bool selection_flags)
{
  set_selection_flags_ = selection_flags;
}

double
RecoMuonSelectorTight_hh_multilepton::get_min_lepton_pt() const
{
  return min_lepton_pt_;
}

double
RecoMuonSelectorTight_hh_multilepton::get_min_cone_pt() const
{
  return min_cone_pt_;
}

double
RecoMuonSelectorTight_hh_multilepton::get_max_absEta() const
{
  return max_absEta_;
}

bool
RecoMuonSelectorTight_hh_multilepton::operator()(const RecoMuon & muon) const
{
  if(debug_)
  {
    std::cout << get_human_line(this, __func__) << ":\n" << muon;
  }

  if(muon.cone_pt() < min_cone_pt_)
  {
    if(debug_)
    {
      std::cout << "FAILS cone pT = " << muon.cone_pt() << " >= " << min_cone_pt_ << " fakeable cut\n";
    }
    return false;
  }

  if(muon.lepton_pt() < min_lepton_pt_)
  {
    if(debug_)
    {
      std::cout << "FAILS pT = " << muon.pt() << " >= " << min_lepton_pt_ << " fakeable cut\n";
    }
  }

  if(muon.absEta() > max_absEta_)
  {
    if(debug_)
    {
      std::cout << "FAILS abs(eta) = " << muon.absEta() << " <= " << max_absEta_ << " fakeable cut\n";
    }
    return false;
  }

  if(std::fabs(muon.dxy()) > max_dxy_)
  {
    if(debug_)
    {
      std::cout << "FAILS abs(dxy) = " << std::fabs(muon.dxy()) << " <= " << max_dxy_ << " fakeable cut\n";
    }
    return false;
  }

  if(std::fabs(muon.dz()) > max_dz_)
  {
    if(debug_)
    {
      std::cout << "FAILS abs(dz) = " << std::fabs(muon.dz()) << " <= " << max_dz_ << " fakeable cut\n";
    }
    return false;
  }

  if(muon.relIso() > max_relIso_)
  {
    if(debug_)
    {
      std::cout << "FAILS relIso = " << muon.relIso() << " <= " << max_relIso_ << " fakeable cut\n";
    }
    return false;
  }

  if(muon.sip3d() > max_sip3d_)
  {
    if(debug_)
    {
      std::cout << "FAILS sip3d = " << muon.sip3d() << " <= " << max_sip3d_ << " fakeable cut\n";
    }
    return false;
  }

  if(! muon.passesLooseIdPOG() && apply_looseIdPOG_)
  {
    if(debug_)
    {
      std::cout << "FAILS loose POG fakeable cut\n";
    }
    return false;
  }

  if(! muon.passesMediumIdPOG() && apply_mediumIdPOG_)
  {
    if(debug_)
    {
      std::cout << "FAILS medium POG fakeable cut\n";
    }
    return false;
  }

  
  if(apply_jetBtagCSVLoose_ && muon.jetBtagCSV() > max_jetBtagCSV_)
  {
    if(debug_)
    {
      std::cout << "FAILS jetBtagCSV = " << muon.jetBtagCSV() << " <= " << max_jetBtagCSV_ << " fakeable cut\n";
    }
    return false;
  }
  const double max_jetBtagCSV = smoothBtagCut(muon.assocJet_pt());
  if(debug_)
  {
    std::cout << get_human_line(this, __func__) << ": smooth jetBtagCSV cut = " << max_jetBtagCSV << '\n';
  }
  if (apply_jetBtagCSVInterp_ && muon.jetBtagCSV() > max_jetBtagCSV)
  {
    if(debug_)
    {
      std::cout << "FAILS smooth jetBtagCSV = " << muon.jetBtagCSV() << " <= " << max_jetBtagCSV << " fakeable cut\n";
    }
    return false;
  }  

  if(set_selection_flags_)
  {
    muon.set_isTight();  
  }

  return true;
}

double
RecoMuonSelectorTight_hh_multilepton::smoothBtagCut(double assocJet_pt) const
{
  const double ptInterp = std::min(1., std::max(0., assocJet_pt - smoothBtagCut_minPt_) / smoothBtagCut_ptDiff_);
  return ptInterp * min_jetBtagCSV_ + (1. - ptInterp) * max_jetBtagCSV_;
}

RecoMuonCollectionSelectorTight_hh_multilepton::RecoMuonCollectionSelectorTight_hh_multilepton(Era era,
                                                                       int index,
                                                                       bool debug,
                                                                       bool set_selection_flags)
  : ParticleCollectionSelector<RecoMuon, RecoMuonSelectorTight_hh_multilepton>(era, index, debug)
{
  selector_.set_selection_flags(set_selection_flags);
}
