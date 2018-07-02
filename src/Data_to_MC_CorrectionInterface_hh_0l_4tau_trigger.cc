#include "hhAnalysis/tttt/interface/Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger.h"

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
  : effTrigger_tauLeg_(nullptr)
  , hadTauSelection_(cfg.getParameter<std::string>("hadTauSelection"))
  , isDEBUG_(cfg.exists("isDEBUG") ? cfg.getParameter<bool>("isDEBUG") : false)
  , triggerSF_option_(TauTriggerSFs2017::kCentral)
  , hadTau1_pt_(0.)
  , hadTau1_eta_(0.)
  , hadTau1_phi_(0.)
  , hadTau2_pt_(0.)
  , hadTau2_eta_(0.)
  , hadTau2_phi_(0.)
  , hadTau3_pt_(0.)
  , hadTau3_eta_(0.)
  , hadTau3_phi_(0.)  
  , hadTau4_pt_(0.)
  , hadTau4_eta_(0.)
  , hadTau4_phi_(0.)

{
  const std::string era_string = cfg.getParameter<std::string>("era");
  if(era_string == "2017")
  {
    era_ = kEra_2017;
  }
  else
  {
    throw cmsException(this) << "Invalid Configuration parameter 'era' = " << era_string;
  }

  const std::string central_or_shift = cfg.getParameter<std::string>("central_or_shift");
  const TriggerSFsys triggerSF_option = getTriggerSF_option(central_or_shift);
  switch(triggerSF_option)
  {
    // applies to only e+tau and mu+tau legs
    case TriggerSFsys::central:   triggerSF_option_ = TauTriggerSFs2017::kCentral;  break;
    case TriggerSFsys::shiftUp:   triggerSF_option_ = TauTriggerSFs2017::kStatUp;   break;
    case TriggerSFsys::shiftDown: triggerSF_option_ = TauTriggerSFs2017::kStatDown; break;
    default: throw cmsException(this) << "Invalid triggerSF option = " << static_cast<int>(triggerSF_option);
  }

  LocalFileInPath inputFileName_tauLeg("tthAnalysis/TauTriggerSFs2017/data/tauTriggerEfficiencies2017.root");
  std::string hadTauSelection_TauTriggerSFs2017;
  if      ( hadTauSelection_ == "dR03mvaVVLoose" ) hadTauSelection_TauTriggerSFs2017 = "medium"; // CV: trigger efficiency turn-on curve has not been measured for this working-point
  else if ( hadTauSelection_ == "dR03mvaVLoose"  ) hadTauSelection_TauTriggerSFs2017 = "medium"; // CV: trigger efficiency turn-on curve has not been measured for this working-point
  else if ( hadTauSelection_ == "dR03mvaLoose"   ) hadTauSelection_TauTriggerSFs2017 = "medium"; // CV: trigger efficiency turn-on curve has not been measured for this working-point
  else if ( hadTauSelection_ == "dR03mvaMedium"  ) hadTauSelection_TauTriggerSFs2017 = "medium";
  else if ( hadTauSelection_ == "dR03mvaTight"   ) hadTauSelection_TauTriggerSFs2017 = "tight";
  else if ( hadTauSelection_ == "dR03mvaVTight"  ) hadTauSelection_TauTriggerSFs2017 = "vtight";
  else if ( hadTauSelection_ == "dR03mvaVVTight" ) hadTauSelection_TauTriggerSFs2017 = "vtight"; // CV: trigger efficiency turn-on curve has not been measured for this working-point
  else throw cmsException(__func__, __LINE__)
    << "Invalid Configuration parameter 'hadTauSelection' = " << hadTauSelection_ << " !!";
  effTrigger_tauLeg_ = new TauTriggerSFs2017(inputFileName_tauLeg.fullPath().data(), hadTauSelection_TauTriggerSFs2017);
}

Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger::~Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger()
{}

void
Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger::setTriggerBits(bool isTriggered_2tau)
{
  isTriggered_2tau_ = isTriggered_2tau;
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

double
Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger::getSF_triggerEff() const
{
  if(isDEBUG_)
  {
    std::cout << "<Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger::getSF_triggerEff>:\n";
  }

  double sf = 1.;
  if(era_ == kEra_2017)
  {
    double eff_2tau_tauLeg1_data   = effTrigger_tauLeg_->getDiTauEfficiencyData(hadTau1_pt_, hadTau1_eta_, hadTau1_phi_, triggerSF_option_);
    double eff_2tau_tauLeg1_mc     = effTrigger_tauLeg_->getDiTauEfficiencyMC(hadTau1_pt_, hadTau1_eta_, hadTau1_phi_, triggerSF_option_);
    
    double eff_2tau_tauLeg2_data   = effTrigger_tauLeg_->getDiTauEfficiencyData(hadTau2_pt_, hadTau2_eta_, hadTau2_phi_, triggerSF_option_);
    double eff_2tau_tauLeg2_mc     = effTrigger_tauLeg_->getDiTauEfficiencyMC(hadTau2_pt_, hadTau2_eta_, hadTau2_phi_, triggerSF_option_);

    double eff_2tau_tauLeg3_data   = effTrigger_tauLeg_->getDiTauEfficiencyData(hadTau3_pt_, hadTau3_eta_, hadTau3_phi_, triggerSF_option_);
    double eff_2tau_tauLeg3_mc     = effTrigger_tauLeg_->getDiTauEfficiencyMC(hadTau3_pt_, hadTau3_eta_, hadTau3_phi_, triggerSF_option_);

    double eff_2tau_tauLeg4_data   = effTrigger_tauLeg_->getDiTauEfficiencyData(hadTau4_pt_, hadTau4_eta_, hadTau4_phi_, triggerSF_option_);
    double eff_2tau_tauLeg4_mc     = effTrigger_tauLeg_->getDiTauEfficiencyMC(hadTau4_pt_, hadTau4_eta_, hadTau4_phi_, triggerSF_option_);

    double prob_data = 0.;
    double prob_mc   = 0.;
    
    for ( int tau1_status = k2tau; tau1_status <= kNot2tau; ++tau1_status ) {
      int nTrig_2tau_tauLeg = 0;
      if ( tau1_status == k2tau ) ++nTrig_2tau_tauLeg;

      double prob_tau1_data = getProb_tau(tau1_status, eff_2tau_tauLeg1_data);
      double prob_tau1_mc   = getProb_tau(tau1_status, eff_2tau_tauLeg1_mc);

      for ( int tau2_status = k2tau; tau2_status <= kNot2tau; ++tau2_status ) {
	if ( tau2_status == k2tau ) ++nTrig_2tau_tauLeg;
	
	double prob_tau2_data = getProb_tau(tau2_status, eff_2tau_tauLeg2_data);
	double prob_tau2_mc   = getProb_tau(tau2_status, eff_2tau_tauLeg2_mc);

	for ( int tau3_status = k2tau; tau3_status <= kNot2tau; ++tau3_status ) {
	  if ( tau3_status == k2tau ) ++nTrig_2tau_tauLeg;

	  double prob_tau3_data = getProb_tau(tau3_status, eff_2tau_tauLeg3_data);
	  double prob_tau3_mc   = getProb_tau(tau3_status, eff_2tau_tauLeg3_mc);
	    
	  for ( int tau4_status = k2tau; tau4_status <= kNot2tau; ++tau4_status ) {
	    if ( tau4_status == k2tau ) ++nTrig_2tau_tauLeg;
	    
	    double prob_tau4_data = getProb_tau(tau4_status, eff_2tau_tauLeg4_data);
	    double prob_tau4_mc   = getProb_tau(tau4_status, eff_2tau_tauLeg4_mc);
	    
	    bool isTrig_2tau_toy   = nTrig_2tau_tauLeg >= 2;
	    
	    if ( isTriggered_2tau_ == isTrig_2tau_toy ) {
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
	           "hadTau (third): pT = " << hadTau3_pt_ << ", eta = " << hadTau3_eta_ << "\n"
	           "hadTau (fourth): pT = " << hadTau4_pt_ << ", eta = " << hadTau4_eta_ << "\n"
                   "eff (X_tau1): data = " << eff_2tau_tauLeg1_data   << ", MC = " << eff_2tau_tauLeg1_mc   << "\n"
	           "eff (X_tau2): data = " << eff_2tau_tauLeg2_data   << ", MC = " << eff_2tau_tauLeg2_mc   << "\n"
                   "eff (X_tau3): data = " << eff_2tau_tauLeg3_data   << ", MC = " << eff_2tau_tauLeg3_mc   << "\n"
                   "eff (X_tau4): data = " << eff_2tau_tauLeg4_data   << ", MC = " << eff_2tau_tauLeg4_mc   << '\n'                  
      ;
    }

    sf = aux::compSF(prob_data, prob_mc);
    if ( isDEBUG_ ) {
      int idxCase = 0;
      if ( isTriggered_2tau_  ) idxCase += 1;
      std::string text_2tau;
      if ( isTriggered_2tau_ ) text_2tau = "ditau trigger doesn't fire";
      else text_2tau = "ditau trigger fires";
      std::cout << "case " << idxCase << ": " << text_2tau << "\n"	
	           " eff: data = " << prob_data << ", MC = " << prob_mc << " --> SF = " << sf << '\n';
    }
  } // era_
  else
  {
    assert(0);
  }

  return sf;
}
 
double Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger::getProb_tau(int tau_status, double eff_2tau_tauLeg) const
{
  double prob = 0.;
  if ( tau_status == k2tau ) {
    prob = eff_2tau_tauLeg;
  } else if ( tau_status == kNot2tau ) {
    prob = 1. - eff_2tau_tauLeg;
  } else assert(0);
  return prob;
}
