#ifndef hhAnalysis_multilepton_EvtHistManager_hh_3l_h
#define hhAnalysis_multilepton_EvtHistManager_hh_3l_h

/** \class EvtHistManager_hh_3l
 *
 * Book and fill histograms for event-level quantities in ttH multilepton analysis
 * in 3l category
 *
 * \author Christian Veelken, Tallin
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

class EvtHistManager_hh_3l
  : public HistManagerBase
{
 public:
  EvtHistManager_hh_3l(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_3l() {}

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
		 int chargedSum3l,
		 int numSFOS2l,
		 double dihiggsVisMass,
		 double dihiggsMass,		 
		 double WTojjMass,
		 double mSFOS2l,
		 double mTMetLepton1,
		 double mTMetLepton2,
		 double vbf_m_jj, double vbf_dEta_jj, int numSelJets_nonVBF,                
		 double HT,
		 double STMET,
		 double mvaOutput_xgb_hh_3l_SUMBk_HH,
                 double evtWeight);
  
  const TH1 *
  getHistogram_EventCounter() const;

 private:
  int era_;

	/*
  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numHadTaus_;
  TH1 * histogram_numJets_;
  TH1 * histogram_numBJets_loose_;
  TH1 * histogram_numBJets_medium_;

  // CV: used to check loss in signal efficiency in case events with high jet and b-jet multiplicity are vetoed
  // to avoid overlap with ttH, H->bb analysis (alternative: ttH, H->bb analysis adds hadronic tau veto)
  TH2 * histogram_numBJets_loose_vs_numJets_;
  TH2 * histogram_numBJets_medium_vs_numJets_;

  TH1 * histogram_mvaOutput_3l_ttV_;
  TH1 * histogram_mvaOutput_3l_ttbar_;
  TH1 * histogram_mvaDiscr_3l_; */

  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numJets_;
  TH1 * histogram_numJetsPtGt40_;
  TH1 * histogram_numBJets_loose_;
  TH1 * histogram_numBJets_medium_;	
  TH1 * histogram_chargedSum3l_;
  TH1 * histogram_numSFOS2l_;
  
  TH1 * histogram_dihiggsVisMass_;
  TH1 * histogram_dihiggsMass_;
  TH1 * histogram_WTojjMass_;
  TH1 * histogram_mSFOS2l_;
  TH1 * histogram_mTMetLepton1_;
  TH1 * histogram_mTMetLepton2_;
  
  TH1 * histogram_vbf_m_jj_;
  TH1 * histogram_vbf_dEta_jj_;
  TH1 * histogram_numJets_nonVBF_;
  
  TH1 * histogram_HT_;
  TH1 * histogram_STMET_;

  TH1 * histogram_mvaOutput_xgb_hh_3l_SUMBk_HH_;

  TH1 * histogram_EventCounter_;
};

#endif
