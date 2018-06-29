#ifndef hhAnalysis_tttt_Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger_h
#define hhAnalysis_tttt_Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger_h

#include "tthAnalysis/TauTriggerSFs2017/interface/TauTriggerSFs2017.h"

#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // lutWrapperBase, vLutWrapperBase

class Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger
{
public:
  Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger(const edm::ParameterSet & cfg);
  ~Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger();

  //-----------------------------------------------------------------------------
  // set HLT trigger bits
  // (to be called once per event, before calling any of the getSF.. functions)
  void
  setTriggerBits(bool isTriggered_1e,
                 bool isTriggered_1e1tau,
                 bool isTriggered_1m,
                 bool isTriggered_1m1tau,
		 bool isTriggered_2tau);
  //-----------------------------------------------------------------------------

  //-----------------------------------------------------------------------------
  // set lepton type, pT and eta as well as hadTau pT, eta and decay mode
  // (to be called once per event, before calling any of the getSF.. functions)
  void
  setLeptons(int lepton_type,
             double lepton_pt,
             double lepton_eta);

  void
  setHadTaus(double hadTau1_pt, double hadTau1_eta, double hadTau1_phi,
             double hadTau2_pt, double hadTau2_eta, double hadTau2_phi,
	     double hadTau3_pt, double hadTau3_eta, double hadTau3_phi);
  //-----------------------------------------------------------------------------

  //-----------------------------------------------------------------------------
  // trigger efficiency turn-on curves for Spring16 non-reHLT MC (not yet implemented)
  double
  getWeight_triggerEff() const;
  //-----------------------------------------------------------------------------

  //-----------------------------------------------------------------------------
  // data/MC correction for trigger efficiency 
  double
  getSF_triggerEff() const;
  //-----------------------------------------------------------------------------

private:

  // define states of single lepton trigger and of lepton leg of lepton+tau cross trigger for each reconstructed lepton
  enum { k1lAnd1l1tau, k1lAndNot1l1tau, kNot1lAnd1l1tau, kNot1lAndNot1l1tau };
    
  // define states of tau leg of lepton+tau cross trigger and of tau leg of ditau trigger for each reconstructed tau
  enum { k1l1tauAnd2tau, k1l1tauAndNot2tau, kNot1l1tauAnd2tau, kNot1l1tauAndNot2tau };

  // define auxiliary functions
  double getProb_lepton(int lepton_status, double eff_1l, double eff_1l1tau_lepLeg) const;
  double getProb_tau(int tau_status, double eff_1l1tau_tauLeg, double eff_2tau_tauLeg) const;

  //-----------------------------------------------------------------------------
  // data/MC corrections for trigger efficiencies in 2017 ReReco data and Summer17 MC

  vLutWrapperBase effTrigger_1e_data_;
  vLutWrapperBase effTrigger_1e_mc_;
  vLutWrapperBase effTrigger_1e1tau_lepLeg_data_;
  vLutWrapperBase effTrigger_1e1tau_lepLeg_mc_;
  
  vLutWrapperBase effTrigger_1m_data_;
  vLutWrapperBase effTrigger_1m_mc_;
  vLutWrapperBase effTrigger_1m1tau_lepLeg_data_;
  vLutWrapperBase effTrigger_1m1tau_lepLeg_mc_;

  TauTriggerSFs2017* effTrigger_tauLeg_;
  //-----------------------------------------------------------------------------

  std::map<std::string, TFile *> inputFiles_;

  int era_;
  std::string hadTauSelection_;
  bool isDEBUG_;
  int triggerSF_option_;

  bool isTriggered_1e_;
  bool isTriggered_1e1tau_;
  bool isTriggered_1m_;
  bool isTriggered_1m1tau_;
  bool isTriggered_2tau_;

  int lepton_type_;
  double lepton_pt_;
  double lepton_eta_;
  double hadTau1_pt_;
  double hadTau1_eta_;
  double hadTau1_phi_;
  double hadTau2_pt_;
  double hadTau2_eta_;
  double hadTau2_phi_;
  double hadTau3_pt_;
  double hadTau3_eta_;
  double hadTau3_phi_;
};

#endif // tthAnalysis_HiggsToTauTau_data_to_MC_corrections_hh_1l_3tau_trigger_h
