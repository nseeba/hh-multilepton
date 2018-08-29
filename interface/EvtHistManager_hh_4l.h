#ifndef hhAnalysis_multilepton_EvtHistManager_hh_4l_h
#define hhAnalysis_multilepton_EvtHistManager_hh_4l_h

/** \class EvtHistManager_hh_4l
 *
 * Book and fill histograms for event-level quantities in the 4l category 
 * of the HH->tttt, WWtt, and WWWW analysis 
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

class EvtHistManager_hh_4l
  : public HistManagerBase
{
public:
  EvtHistManager_hh_4l(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_4l() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(int numElectrons,
                 int numMuons,
                 int numJets,
		 int numJetsPtGt40,
                 int numBJets_loose,
                 int numBJets_medium,
		 double dihiggsVisMass,
		 double dihiggsMass,
		 double HT,
		 double STMET,
                 double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

 private:
  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numJets_;
  TH1 * histogram_numJetsPtGt40_;
  TH1 * histogram_numBJets_loose_;
  TH1 * histogram_numBJets_medium_;

  TH1 * histogram_dihiggsVisMass_;
  TH1 * histogram_dihiggsMass_;

  TH1 * histogram_HT_;
  TH1 * histogram_STMET_;
  
  TH1 * histogram_EventCounter_;
};

#endif
