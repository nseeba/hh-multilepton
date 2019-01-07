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
		 double HT,
		 double STMET,
		 //double BDTOutput_SUM,
		 double BDTOutput_SUM_gen_mHH_400,
		 double BDTOutput_SUM_gen_mHH_700,
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
  //TH1 * histogram_BDTOutput_SUM_;
  TH1 * histogram_BDTOutput_SUM_gen_mHH_400_;
  TH1 * histogram_BDTOutput_SUM_gen_mHH_700_;
  TH1 * histogram_EventCounter_;
};

#endif
