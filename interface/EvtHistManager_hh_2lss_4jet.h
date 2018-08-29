#ifndef hhAnalysis_wwww_EvtHistManager_hh_2lss_4jet_h
#define hhAnalysis_wwww_EvtHistManager_hh_2lss_4jet_h

/** \class EvtHistManager_hh_2lss_4jet
 *
 * Book and fill histograms for event-level quantities in the 2l+2tau_h category 
 * of the HH->wwww, WWtt, and WWWW analysis 
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

//#include "hhAnalysis/wwww/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult

class EvtHistManager_hh_2lss_4jet
  : public HistManagerBase
{
public:
  EvtHistManager_hh_2lss_4jet(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_2lss_4jet() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(int numElectrons,
                 int numMuons,
                 int numHadTaus,
                 int numJets,
		 int numJetsPtGt40,
                 int numBJets_loose,
                 int numBJets_medium,
		 double mTauTauVis,
		 double leptonPairCharge,
                 double hadTauPairCharge,
		 double HT,
		 double STMET,
                 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

 private:
  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numHadTaus_;
  TH1 * histogram_numJets_;
  TH1 * histogram_numJetsPtGt40_;
  TH1 * histogram_numBJets_loose_;
  TH1 * histogram_numBJets_medium_;

  TH1 * histogram_mTauTauVis_;

  TH1 * histogram_leptonPairCharge_;
  TH1 * histogram_hadTauPairCharge_;

  TH1 * histogram_HT_;
  TH1 * histogram_STMET_;
      
  TH1 * histogram_EventCounter_;
};

#endif
