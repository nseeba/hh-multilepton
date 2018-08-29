#include "hhAnalysis/tttt/interface/Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger.h"

#include "tthAnalysis/TauTriggerSFs2017/interface/TauTriggerSFs2017.h"
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // kEra_2017
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/data_to_MC_corrections_auxFunctions.h" // aux::
#include "tthAnalysis/HiggsToTauTau/interface/sysUncertOptions.h" // TriggerSFsys, getTriggerSF_option()

#include <TString.h> // Form()
#include <TMath.h> // TMath::Abs()

#include <boost/algorithm/string/predicate.hpp> // boost::ends_with()

#include <cassert> // assert()

Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger::Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger(const edm::ParameterSet & cfg)
  : Data_to_MC_CorrectionInterface_0l_2tau_trigger(cfg)
  , hadTau3_genPdgId_(0)
  , hadTau3_pt_(0.)
  , hadTau3_eta_(0.)
  , hadTau3_phi_(0.)
  , hadTau3_decayMode_(0)
  , hadTau4_genPdgId_(0)
  , hadTau4_pt_(0.)
  , hadTau4_eta_(0.)
  , hadTau4_phi_(0.)
  , hadTau4_decayMode_(0)
{}

Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger::~Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger()
{}

void
Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger::setHadTaus(double hadTau1_pt, double hadTau1_eta, double hadTau1_phi,
                                                              double hadTau2_pt, double hadTau2_eta, double hadTau2_phi)
{
  throw cmsException(this, __func__, __LINE__) << "Invalid call";
}

void
Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger::setHadTaus(int hadTau1_genPdgId, double hadTau1_pt, double hadTau1_eta, int hadTau1_decayMode,
                                                              int hadTau2_genPdgId, double hadTau2_pt, double hadTau2_eta, int hadTau2_decayMode)
{
  throw cmsException(this, __func__, __LINE__) << "Invalid call";
}

void
Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger::setHadTaus(double hadTau1_pt, double hadTau1_eta, double hadTau1_phi,
                                                              double hadTau2_pt, double hadTau2_eta, double hadTau2_phi,
                                                              double hadTau3_pt, double hadTau3_eta, double hadTau3_phi,
                                                              double hadTau4_pt, double hadTau4_eta, double hadTau4_phi)
{
  hadTau1_pt_  = hadTau1_pt;
  hadTau1_eta_ = hadTau1_eta;
  hadTau1_phi_ = hadTau1_phi;

  hadTau2_pt_  = hadTau2_pt;
  hadTau2_eta_ = hadTau2_eta;
  hadTau2_phi_ = hadTau2_phi;

  hadTau3_pt_  = hadTau3_pt;
  hadTau3_eta_ = hadTau3_eta;
  hadTau3_phi_ = hadTau3_phi;

  hadTau4_pt_  = hadTau4_pt;
  hadTau4_eta_ = hadTau4_eta;
  hadTau4_phi_ = hadTau4_phi;
}

void
Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger::setHadTaus(int hadTau1_genPdgId, double hadTau1_pt, double hadTau1_eta, int hadTau1_decayMode,
                                                              int hadTau2_genPdgId, double hadTau2_pt, double hadTau2_eta, int hadTau2_decayMode,
                                                              int hadTau3_genPdgId, double hadTau3_pt, double hadTau3_eta, int hadTau3_decayMode,
                                                              int hadTau4_genPdgId, double hadTau4_pt, double hadTau4_eta, int hadTau4_decayMode)
{
  hadTau1_genPdgId_  = hadTau1_genPdgId;
  hadTau1_pt_        = hadTau1_pt;
  hadTau1_eta_       = hadTau1_eta;
  hadTau1_decayMode_ = hadTau1_decayMode;

  hadTau2_genPdgId_  = hadTau2_genPdgId;
  hadTau2_pt_        = hadTau2_pt;
  hadTau2_eta_       = hadTau2_eta;
  hadTau2_decayMode_ = hadTau2_decayMode;

  hadTau3_genPdgId_  = hadTau3_genPdgId;
  hadTau3_pt_        = hadTau3_pt;
  hadTau3_eta_       = hadTau3_eta;
  hadTau3_decayMode_ = hadTau3_decayMode;

  hadTau4_genPdgId_  = hadTau4_genPdgId;
  hadTau4_pt_        = hadTau4_pt;
  hadTau4_eta_       = hadTau4_eta;
  hadTau4_decayMode_ = hadTau4_decayMode;
}

double
Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger::getSF_triggerEff() const
{
  if(isDEBUG_)
  {
    std::cout << get_human_line(this, __func__, __LINE__) << '\n';
  }

  double eff_2tau_tauLeg1_data = 0.;
  double eff_2tau_tauLeg1_mc   = 0.;
  double eff_2tau_tauLeg2_data = 0.;
  double eff_2tau_tauLeg2_mc   = 0.;
  double eff_2tau_tauLeg3_data = 0.;
  double eff_2tau_tauLeg3_mc   = 0.;
  double eff_2tau_tauLeg4_data = 0.;
  double eff_2tau_tauLeg4_mc   = 0.;

  if(era_ == kEra_2016)
  {
    const bool hadTau1_isGenTau = (hadTau1_genPdgId_ == 11 || hadTau1_genPdgId_ == 13 || hadTau1_genPdgId_ == 15);
    if(hadTau1_isGenTau)
    {
      eff_2tau_tauLeg1_data = get_from_lut(effTrigger_2tau_perLeg_data_gentau_, hadTau1_pt_, hadTau1_eta_, hadTau1_decayMode_, isDEBUG_);
      eff_2tau_tauLeg1_mc   = get_from_lut(effTrigger_2tau_perLeg_mc_gentau_, hadTau1_pt_, hadTau1_eta_, hadTau1_decayMode_, isDEBUG_);
    }
    else
    {
      eff_2tau_tauLeg1_data = get_from_lut(effTrigger_2tau_perLeg_data_faketau_, hadTau1_pt_, hadTau1_eta_, hadTau1_decayMode_, isDEBUG_);
      eff_2tau_tauLeg1_mc   = get_from_lut(effTrigger_2tau_perLeg_mc_faketau_, hadTau1_pt_, hadTau1_eta_, hadTau1_decayMode_, isDEBUG_);
    }

    const bool hadTau2_isGenTau = (hadTau2_genPdgId_ == 11 || hadTau2_genPdgId_ == 13 || hadTau2_genPdgId_ == 15);
    if(hadTau2_isGenTau)
    {
      eff_2tau_tauLeg2_data = get_from_lut(effTrigger_2tau_perLeg_data_gentau_, hadTau2_pt_, hadTau2_eta_, hadTau2_decayMode_, isDEBUG_);
      eff_2tau_tauLeg2_mc   = get_from_lut(effTrigger_2tau_perLeg_mc_gentau_, hadTau2_pt_, hadTau2_eta_, hadTau2_decayMode_, isDEBUG_);
    }
    else
    {
      eff_2tau_tauLeg2_data = get_from_lut(effTrigger_2tau_perLeg_data_faketau_, hadTau2_pt_, hadTau2_eta_, hadTau2_decayMode_, isDEBUG_);
      eff_2tau_tauLeg2_mc   = get_from_lut(effTrigger_2tau_perLeg_mc_faketau_, hadTau2_pt_, hadTau2_eta_, hadTau2_decayMode_, isDEBUG_);
    }

    const bool hadTau3_isGenTau = (hadTau3_genPdgId_ == 11 || hadTau3_genPdgId_ == 13 || hadTau3_genPdgId_ == 15);
    if(hadTau3_isGenTau)
    {
      eff_2tau_tauLeg3_data = get_from_lut(effTrigger_2tau_perLeg_data_gentau_, hadTau3_pt_, hadTau3_eta_, hadTau3_decayMode_, isDEBUG_);
      eff_2tau_tauLeg3_mc   = get_from_lut(effTrigger_2tau_perLeg_mc_gentau_,   hadTau3_pt_, hadTau3_eta_, hadTau3_decayMode_, isDEBUG_);
    }
    else
    {
      eff_2tau_tauLeg3_data = get_from_lut(effTrigger_2tau_perLeg_data_faketau_, hadTau3_pt_, hadTau3_eta_, hadTau3_decayMode_, isDEBUG_);
      eff_2tau_tauLeg3_mc   = get_from_lut(effTrigger_2tau_perLeg_mc_faketau_,   hadTau3_pt_, hadTau3_eta_, hadTau3_decayMode_, isDEBUG_);
    }

    const bool hadTau4_isGenTau = (hadTau4_genPdgId_ == 11 || hadTau4_genPdgId_ == 13 || hadTau4_genPdgId_ == 15);
    if(hadTau4_isGenTau)
    {
      eff_2tau_tauLeg4_data = get_from_lut(effTrigger_2tau_perLeg_data_gentau_, hadTau4_pt_, hadTau4_eta_, hadTau4_decayMode_, isDEBUG_);
      eff_2tau_tauLeg4_mc   = get_from_lut(effTrigger_2tau_perLeg_mc_gentau_,   hadTau4_pt_, hadTau4_eta_, hadTau4_decayMode_, isDEBUG_);
    }
    else
    {
      eff_2tau_tauLeg4_data = get_from_lut(effTrigger_2tau_perLeg_data_faketau_, hadTau4_pt_, hadTau4_eta_, hadTau4_decayMode_, isDEBUG_);
      eff_2tau_tauLeg4_mc   = get_from_lut(effTrigger_2tau_perLeg_mc_faketau_,   hadTau4_pt_, hadTau4_eta_, hadTau4_decayMode_, isDEBUG_);
    }
  }
  if(era_ == kEra_2017)
  {
    if(std::fabs(hadTau1_eta_) <= 2.1)
    {
      eff_2tau_tauLeg1_data = effTrigger_tauLeg_->getDiTauEfficiencyData(hadTau1_pt_, hadTau1_eta_, hadTau1_phi_, triggerSF_option_);
      eff_2tau_tauLeg1_mc   = effTrigger_tauLeg_->getDiTauEfficiencyMC  (hadTau1_pt_, hadTau1_eta_, hadTau1_phi_, triggerSF_option_);
    }

    if(std::fabs(hadTau2_eta_) <= 2.1)
    {
      eff_2tau_tauLeg2_data = effTrigger_tauLeg_->getDiTauEfficiencyData(hadTau2_pt_, hadTau2_eta_, hadTau2_phi_, triggerSF_option_);
      eff_2tau_tauLeg2_mc   = effTrigger_tauLeg_->getDiTauEfficiencyMC  (hadTau2_pt_, hadTau2_eta_, hadTau2_phi_, triggerSF_option_);
    }

    if(std::fabs(hadTau3_eta_) <= 2.1)
    {
      eff_2tau_tauLeg3_data = effTrigger_tauLeg_->getDiTauEfficiencyData(hadTau3_pt_, hadTau3_eta_, hadTau3_phi_, triggerSF_option_);
      eff_2tau_tauLeg3_mc   = effTrigger_tauLeg_->getDiTauEfficiencyMC  (hadTau3_pt_, hadTau3_eta_, hadTau3_phi_, triggerSF_option_);
    }

    if(std::fabs(hadTau4_eta_) <= 2.1)
    {
      eff_2tau_tauLeg4_data = effTrigger_tauLeg_->getDiTauEfficiencyData(hadTau4_pt_, hadTau4_eta_, hadTau4_phi_, triggerSF_option_);
      eff_2tau_tauLeg4_mc   = effTrigger_tauLeg_->getDiTauEfficiencyMC  (hadTau4_pt_, hadTau4_eta_, hadTau4_phi_, triggerSF_option_);
    }
  }
  else if(era_ == kEra_2018)
  {
    throw cmsException(this, __func__, __LINE__) << "Implement me!";
  }
  else
  {
    throw cmsException(this, __func__, __LINE__) << "Invalid era = " << era_;
  }

  double prob_data = 0.;
  double prob_mc   = 0.;

  for(int tau1_status = k2tau; tau1_status <= kNot2tau; ++tau1_status)
  {
    const double prob_tau1_data = getProb_tau(tau1_status, eff_2tau_tauLeg1_data);
    const double prob_tau1_mc   = getProb_tau(tau1_status, eff_2tau_tauLeg1_mc);

    for(int tau2_status = k2tau; tau2_status <= kNot2tau; ++tau2_status)
    {
      const double prob_tau2_data = getProb_tau(tau2_status, eff_2tau_tauLeg2_data);
      const double prob_tau2_mc   = getProb_tau(tau2_status, eff_2tau_tauLeg2_mc);

      for(int tau3_status = k2tau; tau3_status <= kNot2tau; ++tau3_status)
      {
        const double prob_tau3_data = getProb_tau(tau3_status, eff_2tau_tauLeg3_data);
        const double prob_tau3_mc   = getProb_tau(tau3_status, eff_2tau_tauLeg3_mc);

        for(int tau4_status = k2tau; tau4_status <= kNot2tau; ++tau4_status)
        {
	  const double prob_tau4_data = getProb_tau(tau4_status, eff_2tau_tauLeg4_data);
          const double prob_tau4_mc   = getProb_tau(tau4_status, eff_2tau_tauLeg4_mc);

	  int nTrig_2tau_tauLeg = 0;
	  if(tau1_status == k2tau)
	  {
	    ++nTrig_2tau_tauLeg;
	  }
	  if(tau2_status == k2tau)
          {
	    ++nTrig_2tau_tauLeg;
	  }
	  if(tau3_status == k2tau)
          {
            ++nTrig_2tau_tauLeg;
          }
          if(tau4_status == k2tau)
          {
            ++nTrig_2tau_tauLeg;
          }

          const bool isTrig_2tau_toy = nTrig_2tau_tauLeg >= 2;

          if(isTriggered_2tau_ == isTrig_2tau_toy)
          {
            prob_data += prob_tau1_data * prob_tau2_data * prob_tau3_data * prob_tau4_data;
            prob_mc   += prob_tau1_mc   * prob_tau2_mc   * prob_tau3_mc   * prob_tau4_mc;
          }
        }
      }
    }
  }

  if(isDEBUG_)
  {
    std::cout << "hadTau (lead):    pT = " << hadTau1_pt_ << ", eta = " << hadTau1_eta_ << "\n"
                 "hadTau (sublead): pT = " << hadTau2_pt_ << ", eta = " << hadTau2_eta_ << "\n"
                 "hadTau (third):   pT = " << hadTau3_pt_ << ", eta = " << hadTau3_eta_ << "\n"
                 "hadTau (fourth):  pT = " << hadTau4_pt_ << ", eta = " << hadTau4_eta_ << "\n"
                 "eff (X_tau1): data = " << eff_2tau_tauLeg1_data   << ", MC = " << eff_2tau_tauLeg1_mc   << "\n"
                 "eff (X_tau2): data = " << eff_2tau_tauLeg2_data   << ", MC = " << eff_2tau_tauLeg2_mc   << "\n"
                 "eff (X_tau3): data = " << eff_2tau_tauLeg3_data   << ", MC = " << eff_2tau_tauLeg3_mc   << "\n"
                 "eff (X_tau4): data = " << eff_2tau_tauLeg4_data   << ", MC = " << eff_2tau_tauLeg4_mc   << '\n'
    ;
  }

  const double sf = aux::compSF(prob_data, prob_mc);
  if(isDEBUG_)
  {
    const int idxCase = isTriggered_2tau_ ? 1 : 0;
    const std::string text_2tau = isTriggered_2tau_ ? "ditau trigger doesn't fire" : "ditau trigger fires";
    std::cout << "case " << idxCase << ": " << text_2tau << "\n"
                 " eff: data = " << prob_data << ", MC = " << prob_mc << " --> SF = " << sf << '\n'
    ;
  }

  return sf;
}
 
double
Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger::getProb_tau(int tau_status,
                                                               double eff_2tau_tauLeg) const
{
  double prob = 0.;
  switch(tau_status)
  {
    case k2tau:    prob = eff_2tau_tauLeg;      break;
    case kNot2tau: prob = 1. - eff_2tau_tauLeg; break;
    default:       assert(0);
  }
  return prob;
}
