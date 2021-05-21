#ifndef hhAnalysis_multilepton_EvtHistManager_hh_2lss_leq1tau_h
#define hhAnalysis_multilepton_EvtHistManager_hh_2lss_leq1tau_h

/** \class EvtHistManager_hh_2lss_leq1tau
 *
 * Book and fill histograms for event-level quantities in the 2l+2tau_h category 
 * of the HH->wwww, WWtt, and WWWW analysis 
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

//#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult

class EvtHistManager_hh_2lss_leq1tau
  : public HistManagerBase
{
public:
  EvtHistManager_hh_2lss_leq1tau(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_2lss_leq1tau() {}

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
		 double STMET,
		 //
		 //
		 //
		 int nElectrons_in_2lss,
		 //leptonPairMass_sel,
		 //leptonPairCharge_sel,
		 double dR_ll,
		 double dPhi_ll,
		 //
		 //nAK4,
		 int nAK8_w2subjets,
		 int nWJets_selected,
		 //
		 double mass_2j_fromW1,
		 double mass_2j_fromW2,
		 double dR_2j_fromW1,
		 double dR_2j_fromW2,
		 //
		 double dR_Wjets_min,
		 double dR_Wjets_max,
		 double dR_l_Wjets_min,
		 double dR_l_Wjets_max,
		 double dR_l_AK4jets_min,
		 double dR_l_AK4jets_max,
		 double dR_l_leadWjet_min,
		 double dR_l_leadWjet_max,
		 double dR_l_leadAK4jet_min,
		 double dR_l_leadAK4jet_max,
		 //
		 double met,
		 double mht,
		 double met_LD,
		 //HT,
		 //STMET,
		 //
		 double mT_lep1_met,
		 double mT_lep2_met,
                 //
		 int eventCategory,
		 //
		 int nTaus,
		 //
		 //
		 double mindr_lep1_jet,
		 double mindr_lep2_jet,
		 double pT_ll,
		 double max_lep_eta,
		 double pT_llMEt,
		 double Smin_llMEt,
		 double lep1_conePt,
		 double lep1_eta,
		 double lep2_conePt,
		 double lep2_eta,
		 //
		 //		 
                 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

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
  TH1 * histogram_STMET_;
  TH1 * histogram_EventCounter_;


  TH1 * histogram_nElectrons_in_2lss_;
  //leptonPairMass_sel_;
  //leptonPairCharge_sel_;
  TH1 * histogram_dR_ll_;
  TH1 * histogram_dPhi_ll_;
  //
  //nAK4_;
  TH1 * histogram_nAK8_w2subjets_;
  TH1 * histogram_nWJets_selected_;
  //
  TH1 * histogram_mass_2j_fromW1_;
  TH1 * histogram_mass_2j_fromW2_;
  TH1 * histogram_dR_2j_fromW1_;
  TH1 * histogram_dR_2j_fromW2_;
  //
  TH1 * histogram_dR_Wjets_min_;
  TH1 * histogram_dR_Wjets_max_;
  TH1 * histogram_dR_l_Wjets_min_;
  TH1 * histogram_dR_l_Wjets_max_;
  TH1 * histogram_dR_l_AK4jets_min_;
  TH1 * histogram_dR_l_AK4jets_max_;
  TH1 * histogram_dR_l_leadWjet_min_;
  TH1 * histogram_dR_l_leadWjet_max_;
  TH1 * histogram_dR_l_leadAK4jet_min_;
  TH1 * histogram_dR_l_leadAK4jet_max_;
  //
  TH1 * histogram_met_;
  TH1 * histogram_mht_;
  TH1 * histogram_met_LD_;
  //HT_;
  //STMET_;
  //
  TH1 * histogram_mT_lep1_met_;
  TH1 * histogram_mT_lep2_met_;
  //
  TH1 * histogram_eventCategory_;
  //
  TH1 * histogram_nTaus_;
  //
  //
  TH1 * histogram_mindr_lep1_jet_;
  TH1 * histogram_mindr_lep2_jet_;
  TH1 * histogram_pT_ll_;
  TH1 * histogram_max_lep_eta_;
  TH1 * histogram_pT_llMEt_;
  TH1 * histogram_Smin_llMEt_;
  TH1 * histogram_lep1_conePt_;
  TH1 * histogram_lep1_eta_;
  TH1 * histogram_lep2_conePt_;
  TH1 * histogram_lep2_eta_;
 
 
};

#endif
