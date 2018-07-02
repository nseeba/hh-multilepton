#ifndef hhAnalysis_tttt_Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger_h
#define hhAnalysis_tttt_Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger_h

#include "tthAnalysis/TauTriggerSFs2017/interface/TauTriggerSFs2017.h"

#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // lutWrapperBase, vLutWrapperBase

class Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger
{
public:
  Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger(const edm::ParameterSet & cfg);
  ~Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger();

  //-----------------------------------------------------------------------------
  // set HLT trigger bits
  // (to be called once per event, before calling any of the getSF.. functions)
  void
  setTriggerBits(bool isTriggered_2tau);
  //-----------------------------------------------------------------------------

  //-----------------------------------------------------------------------------
  // set hadTau pT, eta and decay mode
  // (to be called once per event, before calling any of the getSF.. functions)

  void
  setHadTaus(double hadTau1_pt, double hadTau1_eta, double hadTau1_phi,
             double hadTau2_pt, double hadTau2_eta, double hadTau2_phi,
	     double hadTau3_pt, double hadTau3_eta, double hadTau3_phi,
	     double hadTau4_pt, double hadTau4_eta, double hadTau4_phi);
  //-----------------------------------------------------------------------------

  //-----------------------------------------------------------------------------
  // data/MC correction for trigger efficiency 
  double
  getSF_triggerEff() const;
  //-----------------------------------------------------------------------------

private:
    
  // define states of tau leg of ditau trigger for each reconstructed tau
  enum { k2tau, kNot2tau };

  // define auxiliary functions
  double getProb_tau(int tau_status, double eff_2tau_tauLeg) const;

  //-----------------------------------------------------------------------------
  // data/MC corrections for trigger efficiencies in 2017 ReReco data and Summer17 MC

  TauTriggerSFs2017* effTrigger_tauLeg_;
  //-----------------------------------------------------------------------------

  int era_;
  std::string hadTauSelection_;
  bool isDEBUG_;
  int triggerSF_option_;

  bool isTriggered_2tau_;

  double hadTau1_pt_;
  double hadTau1_eta_;
  double hadTau1_phi_;
  double hadTau2_pt_;
  double hadTau2_eta_;
  double hadTau2_phi_;
  double hadTau3_pt_;
  double hadTau3_eta_;
  double hadTau3_phi_;
  double hadTau4_pt_;
  double hadTau4_eta_;
  double hadTau4_phi_;
};

#endif // tthAnalysis_HiggsToTauTau_data_to_MC_corrections_hh_0l_4tau_trigger_h
