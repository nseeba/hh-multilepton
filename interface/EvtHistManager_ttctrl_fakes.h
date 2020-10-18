#ifndef hhAnalysis_multilepton_EvtHistManager_ttctrl_fakes_h
#define hhAnalysis_multilepton_EvtHistManager_ttctrl_fakes_h

/** \class EvtHistManager_ttctrl_fakes
 *
 * Book and fill histograms for event-level quantities in the 2l+2tau_h category 
 * of the HH->wwww, WWtt, and WWWW analysis 
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

//#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult

class EvtHistManager_ttctrl_fakes
  : public HistManagerBase
{
public:
  EvtHistManager_ttctrl_fakes(const edm::ParameterSet & cfg);
  ~EvtHistManager_ttctrl_fakes() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(int numElectrons,
                 int numMuons,
                 int numJets,
		 int numJetsPtGt40,
		 double dihiggsVisMass,
		 double dihiggsMass_wMet,
		 double jetMass,
		 double leptonPairMass,
		 double electronPairMass,
		 double muonPairMass,
		 double leptonPairCharge,
		 double HT,
		 double STMET,//
		 double dR_ll,
		 double mT_met_lepLead,
		 double mT_met_lepSublead,
		 double mT_met_lep_max,
		 double mT_met_lep_min,
		 //double BDTOutput_SUM,
		 double BDTOutput_SUM_gen_mHH_400,
		 double BDTOutput_SUM_gen_mHH_700,
		 //
		 double pt_eTight_lead,
		 double cone_pt_eTight_lead,
		 double eta_eTight_lead,
		 //
		 double pt_eTight_sublead,
		 double cone_pt_eTight_sublead,
		 double eta_eTight_sublead,
		 //
		 double pt_muTight_lead,
		 double cone_pt_muTight_lead,
		 double eta_muTight_lead,
		 //
		 double pt_muTight_sublead,
		 double cone_pt_muTight_sublead,
		 double eta_muTight_sublead,	  	    
		 //
		 double pt_eFakeable_lead,
		 double cone_pt_eFakeable_lead,
		 double eta_eFakeable_lead,
		 //
		 double pt_eFakeable_sublead,
		 double cone_pt_eFakeable_sublead,
		 double eta_eFakeable_sublead,
		 //
		 double pt_muFakeable_lead,
		 double cone_pt_muFakeable_lead,
		 double eta_muFakeable_lead,
		 //
		 double pt_muFakeable_sublead,
		 double cone_pt_muFakeable_sublead,
		 double eta_muFakeable_sublead,
		 //
                 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

  void
  fillHistograms_avgLeptonFR(int    leptonPdgId,
			     double leptonFR_thisEvt);

 private:
  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numJets_;
  TH1 * histogram_numJetsPtGt40_;
  TH1 * histogram_dihiggsVisMass_;
  TH1 * histogram_dihiggsMass_wMet_;
  TH1 * histogram_jetMass_;
  TH1 * histogram_leptonPairMass_;
  TH1 * histogram_electronPairMass_;
  TH1 * histogram_muonPairMass_;
  TH1 * histogram_leptonPairCharge_;
  TH1 * histogram_HT_;
  TH1 * histogram_STMET_;  //
  TH1 * histogram_dR_ll_;
  TH1 * histogram_mT_met_lepLead_;
  TH1 * histogram_mT_met_lepSublead_;
  TH1 * histogram_mT_met_lep_max_;
  TH1 * histogram_mT_met_lep_min_;
  //TH1 * histogram_BDTOutput_SUM_;
  TH1 * histogram_BDTOutput_SUM_gen_mHH_400_;
  TH1 * histogram_BDTOutput_SUM_gen_mHH_700_;
  TH1 * histogram_EventCounter_;

  TH1 * histogram_pt_eTight_lead_;
  TH1 * histogram_cone_pt_eTight_lead_;
  TH1 * histogram_eta_eTight_lead_;
  //
  TH1 * histogram_pt_eTight_sublead_;
  TH1 * histogram_cone_pt_eTight_sublead_;
  TH1 * histogram_eta_eTight_sublead_;
  //
  TH1 * histogram_pt_muTight_lead_;
  TH1 * histogram_cone_pt_muTight_lead_;
  TH1 * histogram_eta_muTight_lead_;
  //
  TH1 * histogram_pt_muTight_sublead_;
  TH1 * histogram_cone_pt_muTight_sublead_;
  TH1 * histogram_eta_muTight_sublead_;	  	    
  //
  TH1 * histogram_pt_eFakeable_lead_;
  TH1 * histogram_cone_pt_eFakeable_lead_;
  TH1 * histogram_eta_eFakeable_lead_;
  //
  TH1 * histogram_pt_eFakeable_sublead_;
  TH1 * histogram_cone_pt_eFakeable_sublead_;
  TH1 * histogram_eta_eFakeable_sublead_;
  //
  TH1 * histogram_pt_muFakeable_lead_;
  TH1 * histogram_cone_pt_muFakeable_lead_;
  TH1 * histogram_eta_muFakeable_lead_;
  //
  TH1 * histogram_pt_muFakeable_sublead_;
  TH1 * histogram_cone_pt_muFakeable_sublead_;
  TH1 * histogram_eta_muFakeable_sublead_;
  
  TH1 * histogram_electronFR_sum_;
  TH1 * histogram_electronFR_nEntries_;
  TH1 * histogram_muonFR_sum_;
  TH1 * histogram_muonFR_nEntries_;
  
};

#endif
