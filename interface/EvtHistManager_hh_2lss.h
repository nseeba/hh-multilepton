#ifndef hhAnalysis_multilepton_EvtHistManager_hh_2lss_h
#define hhAnalysis_multilepton_EvtHistManager_hh_2lss_h

/** \class EvtHistManager_hh_2lss
 *
 * Book and fill histograms for event-level quantities in the 2l+2tau_h category 
 * of the HH->wwww, WWtt, and WWWW analysis 
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

//#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult

class EvtHistManager_hh_2lss
  : public HistManagerBase
{
public:
  EvtHistManager_hh_2lss(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_2lss() {}

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
		 double met,
		 double mht,
		 double met_LD,
		 double HT,
		 double STMET,
		 //
		 double lep1_conePt,
		 double mindr_lep1_jet,
		 double mT_lep1,
                 double dPhi_lep1_met,
                 double dPhi_lep1_mht,
		 //
		 double lep2_conePt,
		 double mindr_lep2_jet,
		 double mT_lep2,
                 double dPhi_lep2_met,
                 double dPhi_lep2_mht,
		 //
		 double dR_ll,
		 double max_lep_eta,
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
  TH1 * histogram_met_;
  TH1 * histogram_mht_;
  TH1 * histogram_met_LD_;
  TH1 * histogram_HT_;
  TH1 * histogram_STMET_;
  TH1 * histogram_EventCounter_;
  //
  TH1 * histogram_lep1_conePt_;
  TH1 * histogram_mindr_lep1_jet_;
  TH1 * histogram_mT_lep1_;
  TH1 * histogram_dPhi_lep1_met_;
  TH1 * histogram_dPhi_lep1_mht_;
  //
  TH1 * histogram_lep2_conePt_;
  TH1 * histogram_mindr_lep2_jet_;
  TH1 * histogram_mT_lep2_;
  TH1 * histogram_dPhi_lep2_met_;
  TH1 * histogram_dPhi_lep2_mht_;
  //
  TH1 * histogram_dR_ll_;
  TH1 * histogram_max_lep_eta_;
};

#endif
