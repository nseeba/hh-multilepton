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

class EvtHistManager_hh_4l : public HistManagerBase
{
public:
  EvtHistManager_hh_4l(const edm::ParameterSet &cfg);
  ~EvtHistManager_hh_4l() {}

  /// book and fill histograms
  void bookHistograms(TFileDirectory &dir) override;

  void fillHistograms(
		      int numElectrons, int numMuons, int numJets, int numJetsPtGt40, int numBJets_loose, int numBJets_medium, double dihiggsVisMass, double dihiggsMass, double HT,
		      double STMET, double lep1_pt, double lep2_pt, double lep3_pt, double lep4_pt, double lep1_conePt, double lep2_conePt, double lep3_conePt, double lep4_conePt,
		      double lep1_eta, double lep2_eta, double lep3_eta, double lep4_eta, double lep1_phi, double lep2_phi, double lep3_phi, double lep4_phi, double lep1_dxy, 
		      double lep2_dxy, double lep3_dxy, double lep4_dxy, double lep1_dz, double lep2_dz, double lep3_dz, double lep4_dz, double pt4l, double pt4lParallelHadT, 
		      double pt4lPerpendicularHadT, double maxPtSum_pair1_pt, double maxPtSum_pair1_eta, double maxPtSum_pair1_phi, double maxPtSum_pair1_deltaEtaLep1, 
		      double maxPtSum_pair1_deltaPhiLep1, double maxPtSum_pair1_deltaEta, double maxPtSum_pair1_deltaPhi, double maxPtSum_pair1_deltaR, double maxPtSum_pair1_deltaPt, 
		      double maxPtSum_pair1_m, double maxPtSum_pair2_pt, double maxPtSum_pair2_eta, double maxPtSum_pair2_phi, double maxPtSum_pair2_deltaEtaLep1, 
		      double maxPtSum_pair2_deltaPhiLep1, double maxPtSum_pair2_deltaEta, double maxPtSum_pair2_deltaPhi, double maxPtSum_pair2_deltaR, double maxPtSum_pair2_deltaPt, 
		      double maxPtSum_pair2_m, double maxSubleadPt_pair1_pt, double maxSubleadPt_pair1_eta, double maxSubleadPt_pair1_phi, double maxSubleadPt_pair1_deltaEtaLep1, 
		      double maxSubleadPt_pair1_deltaPhiLep1, double maxSubleadPt_pair1_deltaEta, double maxSubleadPt_pair1_deltaPhi, double maxSubleadPt_pair1_deltaR, 
		      double maxSubleadPt_pair1_deltaPt, double maxSubleadPt_pair1_m, double maxSubleadPt_pair2_pt, double maxSubleadPt_pair2_eta, double maxSubleadPt_pair2_phi, 
		      double maxSubleadPt_pair2_deltaEtaLep1, double maxSubleadPt_pair2_deltaPhiLep1, double maxSubleadPt_pair2_deltaEta, double maxSubleadPt_pair2_deltaPhi, 
		      double maxSubleadPt_pair2_deltaR, double maxSubleadPt_pair2_deltaPt, double maxSubleadPt_pair2_m, double minDeltaRSum_pair1_pt, double minDeltaRSum_pair1_eta, 
		      double minDeltaRSum_pair1_phi, double minDeltaRSum_pair1_deltaEtaLep1, double minDeltaRSum_pair1_deltaPhiLep1, double minDeltaRSum_pair1_deltaEta, 
		      double minDeltaRSum_pair1_deltaPhi, double minDeltaRSum_pair1_deltaR, double minDeltaRSum_pair1_deltaPt, double minDeltaRSum_pair1_m, double minDeltaRSum_pair2_pt, 
		      double minDeltaRSum_pair2_eta, double minDeltaRSum_pair2_phi, double minDeltaRSum_pair2_deltaEtaLep1, double minDeltaRSum_pair2_deltaPhiLep1, 
		      double minDeltaRSum_pair2_deltaEta, double minDeltaRSum_pair2_deltaPhi, double minDeltaRSum_pair2_deltaR, double minDeltaRSum_pair2_deltaPt, 
		      double minDeltaRSum_pair2_m, double minSubclosestDeltaR_pair1_pt, double minSubclosestDeltaR_pair1_eta, double minSubclosestDeltaR_pair1_phi, 
		      double minSubclosestDeltaR_pair1_deltaEtaLep1,double minSubclosestDeltaR_pair1_deltaPhiLep1, double minSubclosestDeltaR_pair1_deltaEta, 
		      double minSubclosestDeltaR_pair1_deltaPhi, double minSubclosestDeltaR_pair1_deltaR, double minSubclosestDeltaR_pair1_deltaPt, double minSubclosestDeltaR_pair1_m, 
		      double minSubclosestDeltaR_pair2_pt, double minSubclosestDeltaR_pair2_eta, double minSubclosestDeltaR_pair2_phi, double minSubclosestDeltaR_pair2_deltaEtaLep1,
		      double minSubclosestDeltaR_pair2_deltaPhiLep1, double minSubclosestDeltaR_pair2_deltaEta, double minSubclosestDeltaR_pair2_deltaPhi,
		      double minSubclosestDeltaR_pair2_deltaR, double minSubclosestDeltaR_pair2_deltaPt, double minSubclosestDeltaR_pair2_m, double MET, double METParallelHadT, 
		      double METPerpendicularHadT, double METPhi, double METDeltaPhiLep1, double MET_LD, double HTmiss, int lep1_isElectron, int lep1_charge, int lep2_isElectron, 
		      int lep2_charge, int lep3_isElectron, int lep3_charge, int lep4_isElectron, int lep4_charge, int leptonChargeSum, int electronChargeSum, int muonChargeSum, int nSFOS,
		      double evtWeight);

  const TH1 *getHistogram_EventCounter() const;

private:
  TH1 *histogram_numElectrons_;
  TH1 *histogram_numMuons_;
  TH1 *histogram_numJets_;
  TH1 *histogram_numJetsPtGt40_;
  TH1 *histogram_numBJets_loose_;
  TH1 *histogram_numBJets_medium_;

  TH1 *histogram_dihiggsVisMass_;
  TH1 *histogram_dihiggsMass_;

  TH1 *histogram_HT_;
  TH1 *histogram_STMET_;

  TH1 *histogram_EventCounter_;
  TH1 *histogram_lep1_pt_;
  TH1 *histogram_lep2_pt_;
  TH1 *histogram_lep3_pt_;
  TH1 *histogram_lep4_pt_;
  TH1 *histogram_lep1_conePt_;
  TH1 *histogram_lep2_conePt_;
  TH1 *histogram_lep3_conePt_;
  TH1 *histogram_lep4_conePt_;
  TH1 *histogram_lep1_eta_;
  TH1 *histogram_lep2_eta_;
  TH1 *histogram_lep3_eta_;
  TH1 *histogram_lep4_eta_;
  TH1 *histogram_lep1_phi_;
  TH1 *histogram_lep2_phi_;
  TH1 *histogram_lep3_phi_;
  TH1 *histogram_lep4_phi_;
  TH1 *histogram_lep1_dxy_;
  TH1 *histogram_lep2_dxy_;
  TH1 *histogram_lep3_dxy_;
  TH1 *histogram_lep4_dxy_;
  TH1 *histogram_lep1_dz_;
  TH1 *histogram_lep2_dz_;
  TH1 *histogram_lep3_dz_;
  TH1 *histogram_lep4_dz_;
  TH1 *histogram_pt4l_;
  TH1 *histogram_pt4lParallelHadT_;
  TH1 *histogram_pt4lPerpendicularHadT_;
  TH1 *histogram_maxPtSum_pair1_pt_;
  TH1 *histogram_maxPtSum_pair1_eta_;
  TH1 *histogram_maxPtSum_pair1_phi_;
  TH1 *histogram_maxPtSum_pair1_deltaEtaLep1_;
  TH1 *histogram_maxPtSum_pair1_deltaPhiLep1_;
  TH1 *histogram_maxPtSum_pair1_deltaEta_;
  TH1 *histogram_maxPtSum_pair1_deltaPhi_;
  TH1 *histogram_maxPtSum_pair1_deltaR_;
  TH1 *histogram_maxPtSum_pair1_deltaPt_;
  TH1 *histogram_maxPtSum_pair1_m_;
  TH1 *histogram_maxPtSum_pair2_pt_;
  TH1 *histogram_maxPtSum_pair2_eta_;
  TH1 *histogram_maxPtSum_pair2_phi_;
  TH1 *histogram_maxPtSum_pair2_deltaEtaLep1_;
  TH1 *histogram_maxPtSum_pair2_deltaPhiLep1_;
  TH1 *histogram_maxPtSum_pair2_deltaEta_;
  TH1 *histogram_maxPtSum_pair2_deltaPhi_;
  TH1 *histogram_maxPtSum_pair2_deltaR_;
  TH1 *histogram_maxPtSum_pair2_deltaPt_;
  TH1 *histogram_maxPtSum_pair2_m_;
  TH1 *histogram_maxSubleadPt_pair1_pt_;
  TH1 *histogram_maxSubleadPt_pair1_eta_;
  TH1 *histogram_maxSubleadPt_pair1_phi_;
  TH1 *histogram_maxSubleadPt_pair1_deltaEtaLep1_;
  TH1 *histogram_maxSubleadPt_pair1_deltaPhiLep1_;
  TH1 *histogram_maxSubleadPt_pair1_deltaEta_;
  TH1 *histogram_maxSubleadPt_pair1_deltaPhi_;
  TH1 *histogram_maxSubleadPt_pair1_deltaR_;
  TH1 *histogram_maxSubleadPt_pair1_deltaPt_;
  TH1 *histogram_maxSubleadPt_pair1_m_;
  TH1 *histogram_maxSubleadPt_pair2_pt_;
  TH1 *histogram_maxSubleadPt_pair2_eta_;
  TH1 *histogram_maxSubleadPt_pair2_phi_;
  TH1 *histogram_maxSubleadPt_pair2_deltaEtaLep1_;
  TH1 *histogram_maxSubleadPt_pair2_deltaPhiLep1_;
  TH1 *histogram_maxSubleadPt_pair2_deltaEta_;
  TH1 *histogram_maxSubleadPt_pair2_deltaPhi_;
  TH1 *histogram_maxSubleadPt_pair2_deltaR_;
  TH1 *histogram_maxSubleadPt_pair2_deltaPt_;
  TH1 *histogram_maxSubleadPt_pair2_m_;
  TH1 *histogram_minDeltaRSum_pair1_pt_;
  TH1 *histogram_minDeltaRSum_pair1_eta_;
  TH1 *histogram_minDeltaRSum_pair1_phi_;
  TH1 *histogram_minDeltaRSum_pair1_deltaEtaLep1_;
  TH1 *histogram_minDeltaRSum_pair1_deltaPhiLep1_;
  TH1 *histogram_minDeltaRSum_pair1_deltaEta_;
  TH1 *histogram_minDeltaRSum_pair1_deltaPhi_;
  TH1 *histogram_minDeltaRSum_pair1_deltaR_;
  TH1 *histogram_minDeltaRSum_pair1_deltaPt_;
  TH1 *histogram_minDeltaRSum_pair1_m_;
  TH1 *histogram_minDeltaRSum_pair2_pt_;
  TH1 *histogram_minDeltaRSum_pair2_eta_;
  TH1 *histogram_minDeltaRSum_pair2_phi_;
  TH1 *histogram_minDeltaRSum_pair2_deltaEtaLep1_;
  TH1 *histogram_minDeltaRSum_pair2_deltaPhiLep1_;
  TH1 *histogram_minDeltaRSum_pair2_deltaEta_;
  TH1 *histogram_minDeltaRSum_pair2_deltaPhi_;
  TH1 *histogram_minDeltaRSum_pair2_deltaR_;
  TH1 *histogram_minDeltaRSum_pair2_deltaPt_;
  TH1 *histogram_minDeltaRSum_pair2_m_;
  TH1 *histogram_minSubclosestDeltaR_pair1_pt_;
  TH1 *histogram_minSubclosestDeltaR_pair1_eta_;
  TH1 *histogram_minSubclosestDeltaR_pair1_phi_;
  TH1 *histogram_minSubclosestDeltaR_pair1_deltaEtaLep1_;
  TH1 *histogram_minSubclosestDeltaR_pair1_deltaPhiLep1_;
  TH1 *histogram_minSubclosestDeltaR_pair1_deltaEta_;
  TH1 *histogram_minSubclosestDeltaR_pair1_deltaPhi_;
  TH1 *histogram_minSubclosestDeltaR_pair1_deltaR_;
  TH1 *histogram_minSubclosestDeltaR_pair1_deltaPt_;
  TH1 *histogram_minSubclosestDeltaR_pair1_m_;
  TH1 *histogram_minSubclosestDeltaR_pair2_pt_;
  TH1 *histogram_minSubclosestDeltaR_pair2_eta_;
  TH1 *histogram_minSubclosestDeltaR_pair2_phi_;
  TH1 *histogram_minSubclosestDeltaR_pair2_deltaEtaLep1_;
  TH1 *histogram_minSubclosestDeltaR_pair2_deltaPhiLep1_;
  TH1 *histogram_minSubclosestDeltaR_pair2_deltaEta_;
  TH1 *histogram_minSubclosestDeltaR_pair2_deltaPhi_;
  TH1 *histogram_minSubclosestDeltaR_pair2_deltaR_;
  TH1 *histogram_minSubclosestDeltaR_pair2_deltaPt_;
  TH1 *histogram_minSubclosestDeltaR_pair2_m_;
  TH1 *histogram_MET_;
  TH1 *histogram_METParallelHadT_;
  TH1 *histogram_METPerpendicularHadT_;
  TH1 *histogram_METPhi_;
  TH1 *histogram_METDeltaPhiLep1_;
  TH1 *histogram_MET_LD_;
  TH1 *histogram_HTmiss_;
  TH1 *histogram_lep1_isElectron_;
  TH1 *histogram_lep1_charge_;
  TH1 *histogram_lep2_isElectron_;
  TH1 *histogram_lep2_charge_;
  TH1 *histogram_lep3_isElectron_;
  TH1 *histogram_lep3_charge_;
  TH1 *histogram_lep4_isElectron_;
  TH1 *histogram_lep4_charge_;
  TH1 *histogram_leptonChargeSum_;
  TH1 *histogram_electronChargeSum_;
  TH1 *histogram_muonChargeSum_;
  TH1 *histogram_nSFOS_;
};

#endif
