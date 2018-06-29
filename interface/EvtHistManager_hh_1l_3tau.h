#ifndef hhAnalysis_tttt_EvtHistManager_hh_1l_3tau_h
#define hhAnalysis_tttt_EvtHistManager_hh_1l_3tau_h

/** \class EvtHistManager_hh_1l_3tau
 *
 * Book and fill histograms for event-level quantities in the 3l+1tau_h category 
 * of the HH->tttt, WWtt, and WWWW analysis 
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

class EvtHistManager_hh_1l_3tau
  : public HistManagerBase
{
public:
  EvtHistManager_hh_1l_3tau(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_1l_3tau() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(int numElectrons,
                 int numMuons,
                 int numHadTaus,
                 int numJets,
                 int numBJets_loose,
                 int numBJets_medium,
                 double m4Vis,
		 double m4_1,
		 double m4_2,
                 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

 private:
  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numHadTaus_;
  TH1 * histogram_numJets_;
  TH1 * histogram_numBJets_loose_;
  TH1 * histogram_numBJets_medium_;

  TH1 * histogram_m4Vis_;
  TH1 * histogram_m4_;
  
  TH1 * histogram_EventCounter_;
};

#endif
