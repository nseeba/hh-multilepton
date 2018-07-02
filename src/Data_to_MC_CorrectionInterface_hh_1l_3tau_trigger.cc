#include "hhAnalysis/tttt/interface/Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger.h"

#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // kEra_2017
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/data_to_MC_corrections_auxFunctions.h" // aux::
#include "tthAnalysis/HiggsToTauTau/interface/sysUncertOptions.h" // TriggerSFsys, getTriggerSF_option()

#include <TString.h> // Form()
#include <TMath.h> // TMath::Abs()

#include <boost/algorithm/string/predicate.hpp> // boost::ends_with()

#include <cassert> // assert()

Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger::Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger(const edm::ParameterSet & cfg)
  : effTrigger_tauLeg_(nullptr)
  , hadTauSelection_(cfg.getParameter<std::string>("hadTauSelection"))
  , isDEBUG_(cfg.exists("isDEBUG") ? cfg.getParameter<bool>("isDEBUG") : false)
  , triggerSF_option_(TauTriggerSFs2017::kCentral)
  , lepton_type_(-1)
  , lepton_pt_(0.)
  , lepton_eta_(0.)
  , hadTau1_pt_(0.)
  , hadTau1_eta_(0.)
  , hadTau1_phi_(0.)
  , hadTau2_pt_(0.)
  , hadTau2_eta_(0.)
  , hadTau2_phi_(0.)
  , hadTau3_pt_(0.)
  , hadTau3_eta_(0.)
  , hadTau3_phi_(0.)
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

  if(era_ == kEra_2017)
  {
    const std::vector<double> etaBinEdges_1e = { -1., 1.48, 2.1 };
    const int numEtaBins_1e = etaBinEdges_1e.size() - 1;

    for(int idxEtaBin = 0; idxEtaBin < numEtaBins_1e; ++idxEtaBin)
    {
      const double etaMin = etaBinEdges_1e[idxEtaBin];
      const double etaMax = etaBinEdges_1e[idxEtaBin + 1];
      const std::string etaBinLabel = aux::getEtaBinLabel(etaMin, etaMax);

      effTrigger_1e_data_.push_back(new lutWrapperTGraph(
        inputFiles_,
        "tthAnalysis/HiggsToTauTau/data/triggerSF/2017/Electron_Ele32orEle35_eff.root",
        Form("ZMassEta%s_Data", etaBinLabel.data()),
        lut::kXptYabsEta, -1., -1., lut::kLimit, etaMin, etaMax, lut::kCut
      ));
      effTrigger_1e_mc_.push_back(new lutWrapperTGraph(
        inputFiles_,
        "tthAnalysis/HiggsToTauTau/data/triggerSF/2017/Electron_Ele32orEle35_eff.root",
        Form("ZMassEta%s_MC", etaBinLabel.data()),
        lut::kXptYabsEta, -1., -1., lut::kLimit, etaMin, etaMax, lut::kCut
      ));
    }

    const std::vector<double> etaBinEdges_1e_1tau_lepLeg = { -1., 1.48, 2.1 };
    const int numEtaBins_1e_1tau_lepLeg = etaBinEdges_1e_1tau_lepLeg.size() - 1;

    for(int idxEtaBin = 0; idxEtaBin < numEtaBins_1e_1tau_lepLeg; ++idxEtaBin)
    {
      const double etaMin = etaBinEdges_1e_1tau_lepLeg[idxEtaBin];
      const double etaMax = etaBinEdges_1e_1tau_lepLeg[idxEtaBin + 1];
      const std::string etaBinLabel = aux::getEtaBinLabel(etaMin, etaMax);

      effTrigger_1e1tau_lepLeg_data_.push_back(new lutWrapperTGraph(
        inputFiles_,
        "tthAnalysis/HiggsToTauTau/data/triggerSF/2017/Electron_EleTau_Ele24_eff.root",
        Form("ZMassEta%s_Data", etaBinLabel.data()),
        lut::kXptYabsEta, -1., -1., lut::kLimit, etaMin, etaMax, lut::kCut
      ));
      effTrigger_1e1tau_lepLeg_mc_.push_back(new lutWrapperTGraph(
        inputFiles_,
        "tthAnalysis/HiggsToTauTau/data/triggerSF/2017/Electron_EleTau_Ele24_eff.root",
        Form("ZMassEta%s_MC", etaBinLabel.data()),
        lut::kXptYabsEta, -1., -1., lut::kLimit, etaMin, etaMax, lut::kCut
      ));
    }

    const std::vector<double> etaBinEdges_1m = { -1., 0.9, 1.2, 2.1 };
    const int numEtaBins_1m = etaBinEdges_1m.size() - 1;

    for(int idxEtaBin = 0; idxEtaBin < numEtaBins_1m; ++idxEtaBin)
    {
      const double etaMin = etaBinEdges_1m[idxEtaBin];
      const double etaMax = etaBinEdges_1m[idxEtaBin + 1];
      const std::string etaBinLabel = aux::getEtaBinLabel(etaMin, etaMax);

      effTrigger_1m_data_.push_back(new lutWrapperTGraph(
        inputFiles_,
        "tthAnalysis/HiggsToTauTau/data/triggerSF/2017/Muon_IsoMu24orIsoMu27_eff.root",
        Form("ZMassEta%s_Data", etaBinLabel.data()),
        lut::kXptYabsEta, -1., -1., lut::kLimit, etaMin, etaMax, lut::kCut
      ));
      effTrigger_1m_mc_.push_back(new lutWrapperTGraph(
        inputFiles_,
        "tthAnalysis/HiggsToTauTau/data/triggerSF/2017/Muon_IsoMu24orIsoMu27_eff.root",
        Form("ZMassEta%s_MC", etaBinLabel.data()),
        lut::kXptYabsEta, -1., -1., lut::kLimit, etaMin, etaMax, lut::kCut
      ));
    }

    const std::vector<double> etaBinEdges_1m1tau_lepLeg = { -1., 0.9, 1.2, 2.1 };
    const int numEtaBins_1m1tau_lepLeg = etaBinEdges_1m1tau_lepLeg.size() - 1;

    for(int idxEtaBin = 0; idxEtaBin < numEtaBins_1m1tau_lepLeg; ++idxEtaBin)
    {
      const double etaMin = etaBinEdges_1m1tau_lepLeg[idxEtaBin];
      const double etaMax = etaBinEdges_1m1tau_lepLeg[idxEtaBin + 1];
      const std::string etaBinLabel = aux::getEtaBinLabel(etaMin, etaMax);

      effTrigger_1m1tau_lepLeg_data_.push_back(new lutWrapperTGraph(
        inputFiles_,
        "tthAnalysis/HiggsToTauTau/data/triggerSF/2017/Muon_MuTau_IsoMu20_eff.root",
        Form("ZMassEta%s_Data", etaBinLabel.data()),
        lut::kXptYabsEta, -1., -1., lut::kLimit, etaMin, etaMax, lut::kCut
      ));
      effTrigger_1m1tau_lepLeg_mc_.push_back(new lutWrapperTGraph(
        inputFiles_,
        "tthAnalysis/HiggsToTauTau/data/triggerSF/2017/Muon_MuTau_IsoMu20_eff.root",
        Form("ZMassEta%s_MC", etaBinLabel.data()),
        lut::kXptYabsEta, -1., -1., lut::kLimit, etaMin, etaMax, lut::kCut
      ));
    }
  } // era_
  else
  {
    assert(0);
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

Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger::~Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger()
{
  aux::clearCollection(effTrigger_1e_data_);
  aux::clearCollection(effTrigger_1e_mc_);
  aux::clearCollection(effTrigger_1e1tau_lepLeg_data_);
  aux::clearCollection(effTrigger_1e1tau_lepLeg_mc_);

  aux::clearCollection(effTrigger_1m_data_);
  aux::clearCollection(effTrigger_1m_mc_);
  aux::clearCollection(effTrigger_1m1tau_lepLeg_data_);
  aux::clearCollection(effTrigger_1m1tau_lepLeg_mc_);
}

void
Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger::setTriggerBits(bool isTriggered_1e,
								  bool isTriggered_1e1tau,
								  bool isTriggered_1m,
								  bool isTriggered_1m1tau,
								  bool isTriggered_2tau)
{
  isTriggered_1e_     = isTriggered_1e;
  isTriggered_1e1tau_ = isTriggered_1e1tau;
  isTriggered_1m_     = isTriggered_1m;
  isTriggered_1m1tau_ = isTriggered_1m1tau;
  isTriggered_2tau_   = isTriggered_2tau;
}

void
Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger::setLeptons(int lepton_type,
							      double lepton_pt,
							      double lepton_eta)
{
  lepton_type_ = lepton_type;
  lepton_pt_   = lepton_pt;
  lepton_eta_  = lepton_eta;
}

void
Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger::setHadTaus(double hadTau1_pt, double hadTau1_eta, double hadTau1_phi,
							      double hadTau2_pt, double hadTau2_eta, double hadTau2_phi,
							      double hadTau3_pt, double hadTau3_eta, double hadTau3_phi)
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
}

double
Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger::getSF_triggerEff() const
{
  if(isDEBUG_)
  {
    std::cout << "<Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger::getSF_triggerEff>:\n";
  }

  double sf = 1.;
  if(era_ == kEra_2017)
  {
    double eff_1l_data             = 0.;
    double eff_1l_mc               = 0.;
    double eff_1l1tau_lepLeg_data  = 0.;
    double eff_1l1tau_lepLeg_mc    = 0.;
    double eff_1l1tau_tauLeg1_data = 0.;
    double eff_1l1tau_tauLeg1_mc   = 0.;
    double eff_1l1tau_tauLeg2_data = 0.;
    double eff_1l1tau_tauLeg2_mc   = 0.;
    double eff_1l1tau_tauLeg3_data = 0.;
    double eff_1l1tau_tauLeg3_mc   = 0.;

    bool isTriggered_1l     = false;
    bool isTriggered_1l1tau = false;

    if(lepton_type_ == kElectron)
    {
      if(isDEBUG_)
      {
        std::cout << "electron: pT = " << lepton_pt_ << ", eta = " << lepton_eta_ << '\n';
      }
      eff_1l_data               = get_from_lut(effTrigger_1e_data_,            lepton_pt_, lepton_eta_, isDEBUG_);
      eff_1l_mc                 = get_from_lut(effTrigger_1e_mc_,              lepton_pt_, lepton_eta_, isDEBUG_);
      eff_1l1tau_lepLeg_data    = get_from_lut(effTrigger_1e1tau_lepLeg_data_, lepton_pt_, lepton_eta_, isDEBUG_);
      eff_1l1tau_lepLeg_mc      = get_from_lut(effTrigger_1e1tau_lepLeg_mc_,   lepton_pt_, lepton_eta_, isDEBUG_);

      eff_1l1tau_tauLeg1_data   = 0.;
      eff_1l1tau_tauLeg1_mc     = 0.;
      if ( TMath::Abs(hadTau1_eta_) <= 2.1 ) {
        eff_1l1tau_tauLeg1_data = effTrigger_tauLeg_->getETauEfficiencyData(hadTau1_pt_, hadTau1_eta_, hadTau1_phi_, triggerSF_option_);
        eff_1l1tau_tauLeg1_mc   = effTrigger_tauLeg_->getETauEfficiencyMC(hadTau1_pt_, hadTau1_eta_, hadTau1_phi_, triggerSF_option_);
      }

      eff_1l1tau_tauLeg2_data   = 0.;
      eff_1l1tau_tauLeg2_mc     = 0.;
      if ( TMath::Abs(hadTau2_eta_) <= 2.1 ) {
        eff_1l1tau_tauLeg2_data = effTrigger_tauLeg_->getETauEfficiencyData(hadTau2_pt_, hadTau2_eta_, hadTau2_phi_, triggerSF_option_);
        eff_1l1tau_tauLeg2_mc   = effTrigger_tauLeg_->getETauEfficiencyMC(hadTau2_pt_, hadTau2_eta_, hadTau2_phi_, triggerSF_option_);
      }

      eff_1l1tau_tauLeg3_data   = 0.;
      eff_1l1tau_tauLeg3_mc     = 0.;
      if ( TMath::Abs(hadTau3_eta_) <= 2.1 ) {
        eff_1l1tau_tauLeg3_data = effTrigger_tauLeg_->getETauEfficiencyData(hadTau3_pt_, hadTau3_eta_, hadTau3_phi_, triggerSF_option_);
        eff_1l1tau_tauLeg3_mc   = effTrigger_tauLeg_->getETauEfficiencyMC(hadTau3_pt_, hadTau3_eta_, hadTau3_phi_, triggerSF_option_);
      }

      isTriggered_1l     = isTriggered_1e_;
      isTriggered_1l1tau = isTriggered_1e1tau_;
    }
    else if(lepton_type_ == kMuon)
    {
      if(isDEBUG_)
      {
        std::cout << "muon: pT = " << lepton_pt_ << ", eta = " << lepton_eta_ << '\n';
      }
      eff_1l_data               = get_from_lut(effTrigger_1m_data_,            lepton_pt_, lepton_eta_, isDEBUG_);
      eff_1l_mc                 = get_from_lut(effTrigger_1m_mc_,              lepton_pt_, lepton_eta_, isDEBUG_);
      eff_1l1tau_lepLeg_data    = get_from_lut(effTrigger_1m1tau_lepLeg_data_, lepton_pt_, lepton_eta_, isDEBUG_);
      eff_1l1tau_lepLeg_mc      = get_from_lut(effTrigger_1m1tau_lepLeg_mc_,   lepton_pt_, lepton_eta_, isDEBUG_);

      eff_1l1tau_tauLeg1_data   = 0.;
      eff_1l1tau_tauLeg1_mc     = 0.;
      if ( TMath::Abs(hadTau1_eta_) <= 2.1 ) {
        eff_1l1tau_tauLeg1_data = effTrigger_tauLeg_->getMuTauEfficiencyData(hadTau1_pt_, hadTau1_eta_, hadTau1_phi_, triggerSF_option_);
        eff_1l1tau_tauLeg1_mc   = effTrigger_tauLeg_->getMuTauEfficiencyMC(hadTau1_pt_, hadTau1_eta_, hadTau1_phi_, triggerSF_option_);
      }
      
      eff_1l1tau_tauLeg2_data   = 0.;
      eff_1l1tau_tauLeg2_mc     = 0.;
      if ( TMath::Abs(hadTau2_eta_) <= 2.1 ) {
        eff_1l1tau_tauLeg2_data = effTrigger_tauLeg_->getMuTauEfficiencyData(hadTau2_pt_, hadTau2_eta_, hadTau2_phi_, triggerSF_option_);
        eff_1l1tau_tauLeg2_mc   = effTrigger_tauLeg_->getMuTauEfficiencyMC(hadTau2_pt_, hadTau2_eta_, hadTau2_phi_, triggerSF_option_);
      }

      isTriggered_1l     = isTriggered_1m_;
      isTriggered_1l1tau = isTriggered_1m1tau_;
    }
    else
    {
      assert(0);
    }

    double eff_2tau_tauLeg1_data   = effTrigger_tauLeg_->getDiTauEfficiencyData(hadTau1_pt_, hadTau1_eta_, hadTau1_phi_, triggerSF_option_);
    double eff_2tau_tauLeg1_mc     = effTrigger_tauLeg_->getDiTauEfficiencyMC(hadTau1_pt_, hadTau1_eta_, hadTau1_phi_, triggerSF_option_);
    
    double eff_2tau_tauLeg2_data   = effTrigger_tauLeg_->getDiTauEfficiencyData(hadTau2_pt_, hadTau2_eta_, hadTau2_phi_, triggerSF_option_);
    double eff_2tau_tauLeg2_mc     = effTrigger_tauLeg_->getDiTauEfficiencyMC(hadTau2_pt_, hadTau2_eta_, hadTau2_phi_, triggerSF_option_);

    double eff_2tau_tauLeg3_data   = effTrigger_tauLeg_->getDiTauEfficiencyData(hadTau3_pt_, hadTau3_eta_, hadTau3_phi_, triggerSF_option_);
    double eff_2tau_tauLeg3_mc     = effTrigger_tauLeg_->getDiTauEfficiencyMC(hadTau3_pt_, hadTau3_eta_, hadTau3_phi_, triggerSF_option_);

    double prob_data = 0.;
    double prob_mc   = 0.;
    
    for ( int lepton_status = k1lAnd1l1tau; lepton_status <= kNot1lAndNot1l1tau; ++lepton_status ) {
      int nTrig_1l = 0;
      if ( lepton_status == k1lAnd1l1tau || lepton_status == k1lAndNot1l1tau ) ++nTrig_1l;
      int nTrig_1l1tau_lepLeg = 0;
      if ( lepton_status == k1lAnd1l1tau || lepton_status == kNot1lAnd1l1tau ) ++nTrig_1l1tau_lepLeg;

      double prob_lepton_data = getProb_lepton(lepton_status, eff_1l_data, eff_1l1tau_lepLeg_data);
      double prob_lepton_mc   = getProb_lepton(lepton_status, eff_1l_mc,   eff_1l1tau_lepLeg_mc);

      for ( int tau1_status = k1l1tauAnd2tau; tau1_status <= kNot1l1tauAndNot2tau; ++tau1_status ) {
	int nTrig_1l1tau_tauLeg = 0;
	if ( tau1_status == k1l1tauAnd2tau || tau1_status == k1l1tauAndNot2tau ) ++nTrig_1l1tau_tauLeg;
	int nTrig_2tau_tauLeg = 0;
	if ( tau1_status == k1l1tauAnd2tau || tau1_status == kNot1l1tauAnd2tau ) ++nTrig_2tau_tauLeg;

	double prob_tau1_data = getProb_tau(tau1_status, eff_1l1tau_lepLeg_data, eff_2tau_tauLeg1_data);
	double prob_tau1_mc   = getProb_tau(tau1_status, eff_1l1tau_lepLeg_mc,   eff_2tau_tauLeg1_mc);

	for ( int tau2_status = k1l1tauAnd2tau; tau2_status <= kNot1l1tauAndNot2tau; ++tau2_status ) {
	  if ( tau2_status == k1l1tauAnd2tau || tau2_status == k1l1tauAndNot2tau ) ++nTrig_1l1tau_tauLeg;
	  if ( tau2_status == k1l1tauAnd2tau || tau2_status == kNot1l1tauAnd2tau ) ++nTrig_2tau_tauLeg;

	  double prob_tau2_data = getProb_tau(tau2_status, eff_1l1tau_lepLeg_data, eff_2tau_tauLeg2_data);
	  double prob_tau2_mc   = getProb_tau(tau2_status, eff_1l1tau_lepLeg_mc,   eff_2tau_tauLeg2_mc);

	  for ( int tau3_status = k1l1tauAnd2tau; tau3_status <= kNot1l1tauAndNot2tau; ++tau3_status ) {
	    if ( tau3_status == k1l1tauAnd2tau || tau3_status == k1l1tauAndNot2tau ) ++nTrig_1l1tau_tauLeg;
	    if ( tau3_status == k1l1tauAnd2tau || tau3_status == kNot1l1tauAnd2tau ) ++nTrig_2tau_tauLeg;

	    double prob_tau3_data = getProb_tau(tau3_status, eff_1l1tau_lepLeg_data, eff_2tau_tauLeg3_data);
	    double prob_tau3_mc   = getProb_tau(tau3_status, eff_1l1tau_lepLeg_mc,   eff_2tau_tauLeg3_mc);
	    
	    bool isTrig_1l_toy     = nTrig_1l >= 1;
	    bool isTrig_1l1tau_toy = nTrig_1l1tau_lepLeg >= 1 && nTrig_1l1tau_tauLeg >= 1;
	    bool isTrig_2tau_toy   = nTrig_2tau_tauLeg >= 2;
	    
	    if ( isTriggered_1l == isTrig_1l_toy && isTriggered_1l1tau == isTrig_1l1tau_toy && isTriggered_2tau_ == isTrig_2tau_toy ) {
	      prob_data += prob_lepton_data * prob_tau1_data * prob_tau2_data * prob_tau3_data;
	      prob_mc   += prob_lepton_mc   * prob_tau1_mc   * prob_tau2_mc   * prob_tau3_mc;
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
                   "eff (L):      data = " << eff_1l_data             << ", MC = " << eff_1l_mc             << "\n"
                   "eff (X_lep):  data = " << eff_1l1tau_lepLeg_data  << ", MC = " << eff_1l1tau_lepLeg_mc  << "\n"
                   "eff (X_tau1): data = " << eff_1l1tau_tauLeg1_data << ", MC = " << eff_1l1tau_tauLeg1_mc << "\n"
                   "eff (X_tau2): data = " << eff_1l1tau_tauLeg2_data << ", MC = " << eff_1l1tau_tauLeg2_mc << "\n"
                   "eff (X_tau3): data = " << eff_1l1tau_tauLeg3_data << ", MC = " << eff_1l1tau_tauLeg3_mc << "\n"	
                   "eff (T_tau1): data = " << eff_2tau_tauLeg1_data   << ", MC = " << eff_2tau_tauLeg1_mc   << "\n"
	           "eff (T_tau2): data = " << eff_2tau_tauLeg2_data   << ", MC = " << eff_2tau_tauLeg2_mc   << "\n"
                   "eff (T_tau3): data = " << eff_2tau_tauLeg3_data   << ", MC = " << eff_2tau_tauLeg3_mc   << '\n'
      ;
    }

    sf = aux::compSF(prob_data, prob_mc);
    if ( isDEBUG_ ) {
      int idxCase = 0;
      if ( isTriggered_1l     ) idxCase += 1;
      if ( isTriggered_1l1tau ) idxCase += 2;
      if ( isTriggered_2tau_  ) idxCase += 4;
      std::string text_1l;
      if ( isTriggered_1l ) text_1l = "single lepton trigger doesn't fire";
      else text_1l = "single lepton trigger fires";
      std::string text_1l1tau;
      if ( isTriggered_1l1tau ) text_1l1tau = "lepton+tau cross trigger doesn't fire";
      else text_1l1tau = "lepton+tau cross trigger fires";
      std::string text_2tau;
      if ( isTriggered_2tau_ ) text_2tau = "ditau trigger doesn't fire";
      else text_2tau = "ditau trigger fires";
      std::cout << "case " << idxCase << ": " << text_1l << " and " << text_1l1tau << " and " << text_2tau << "\n"	
	           " eff: data = " << prob_data << ", MC = " << prob_mc << " --> SF = " << sf << '\n';
    }
  } // era_
  else
  {
    assert(0);
  }

  return sf;
}

double Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger::getProb_lepton(int lepton_status, double eff_1l, double eff_1l1tau_lepLeg) const
{
  double prob = 0.;
  if ( lepton_status == k1lAnd1l1tau ) {
    prob = std::min(eff_1l, eff_1l1tau_lepLeg);
  } else if ( lepton_status == k1lAndNot1l1tau ) {
    prob = std::max(1.e-2, eff_1l - eff_1l1tau_lepLeg);
  } else if ( lepton_status == kNot1lAnd1l1tau ) {
    prob = std::max(1.e-2, eff_1l1tau_lepLeg - eff_1l);
  } else if ( lepton_status ==  kNot1lAndNot1l1tau ) {
    prob = 1. - std::max(eff_1l, eff_1l1tau_lepLeg);
  } else assert(0);
  return prob;
}
 
double Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger::getProb_tau(int tau_status, double eff_1l1tau_tauLeg, double eff_2tau_tauLeg) const
{
  double prob = 0.;
  if ( tau_status == k1l1tauAnd2tau ) {
    prob = std::min(eff_1l1tau_tauLeg, eff_2tau_tauLeg);
  } else if ( tau_status == k1l1tauAndNot2tau ) {
    prob = std::max(1.e-2, eff_1l1tau_tauLeg - eff_2tau_tauLeg);
  } else if ( tau_status == kNot1l1tauAnd2tau ) {
    prob = std::max(1.e-2, eff_2tau_tauLeg - eff_1l1tau_tauLeg);
  } else if ( tau_status == kNot1l1tauAndNot2tau ) {
    prob = 1. - std::max(eff_1l1tau_tauLeg, eff_2tau_tauLeg);
  } else assert(0);
  return prob;
}
