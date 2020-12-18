#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_4l.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

EvtHistManager_hh_4l::EvtHistManager_hh_4l(const edm::ParameterSet &cfg) : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numElectrons"] = {"central"};
  central_or_shiftOptions_["numMuons"] = {"central"};
  central_or_shiftOptions_["numLeptons"] = {"central"};
  central_or_shiftOptions_["numJets"] = {"central"};
  central_or_shiftOptions_["numJetsPtGt40"] = {"central"};
  central_or_shiftOptions_["numBJets_loose"] = {"central"};
  central_or_shiftOptions_["numBJets_medium"] = {"central"};
  central_or_shiftOptions_["dihiggsVisMass"] = {"*"};
  central_or_shiftOptions_["dihiggsMass"] = {"central"};
  central_or_shiftOptions_["HT"] = {"central"};
  central_or_shiftOptions_["STMET"] = {"central"};
  central_or_shiftOptions_["EventCounter"] = {"*"};
  central_or_shiftOptions_["lep1_pt"] = {"central"};
  central_or_shiftOptions_["lep2_pt"] = {"central"};
  central_or_shiftOptions_["lep3_pt"] = {"central"};
  central_or_shiftOptions_["lep4_pt"] = {"central"};
  central_or_shiftOptions_["lep1_conePt"] = {"central"};
  central_or_shiftOptions_["lep2_conePt"] = {"central"};
  central_or_shiftOptions_["lep3_conePt"] = {"central"};
  central_or_shiftOptions_["lep4_conePt"] = {"central"};
  central_or_shiftOptions_["lep1_eta"] = {"central"};
  central_or_shiftOptions_["lep2_eta"] = {"central"};
  central_or_shiftOptions_["lep3_eta"] = {"central"};
  central_or_shiftOptions_["lep4_eta"] = {"central"};
  central_or_shiftOptions_["lep1_rapidity"] = {"central"};
  central_or_shiftOptions_["lep2_rapidity"] = {"central"};
  central_or_shiftOptions_["lep3_rapidity"] = {"central"};
  central_or_shiftOptions_["lep4_rapidity"] = {"central"};
  central_or_shiftOptions_["lep1_phi"] = {"central"};
  central_or_shiftOptions_["lep2_phi"] = {"central"};
  central_or_shiftOptions_["lep3_phi"] = {"central"};
  central_or_shiftOptions_["lep4_phi"] = {"central"};
  central_or_shiftOptions_["lep1_dxy"] = {"central"};
  central_or_shiftOptions_["lep2_dxy"] = {"central"};
  central_or_shiftOptions_["lep3_dxy"] = {"central"};
  central_or_shiftOptions_["lep4_dxy"] = {"central"};
  central_or_shiftOptions_["lep1_dz"] = {"central"};
  central_or_shiftOptions_["lep2_dz"] = {"central"};
  central_or_shiftOptions_["lep3_dz"] = {"central"};
  central_or_shiftOptions_["lep4_dz"] = {"central"};
  central_or_shiftOptions_["pt4l"] = {"central"};
  central_or_shiftOptions_["pt4lParallelHadT"] = {"central"};
  central_or_shiftOptions_["pt4lPerpendicularHadT"] = {"central"};
  central_or_shiftOptions_["mt4l"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair1_pt"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair1_eta"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair1_phi"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair1_deltaEtaLep1"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair1_deltaPhiLep1"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair1_deltaEta"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair1_deltaPhi"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair1_deltaR"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair1_deltaPt"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair1_m"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair2_pt"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair2_eta"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair2_phi"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair2_deltaEtaLep1"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair2_deltaPhiLep1"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair2_deltaEta"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair2_deltaPhi"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair2_deltaR"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair2_deltaPt"] = {"central"};
  central_or_shiftOptions_["maxPtSum_pair2_m"] = {"central"};
  central_or_shiftOptions_["MET"] = {"central"};
  central_or_shiftOptions_["METParallelHadT"] = {"central"};
  central_or_shiftOptions_["METPerpendicularHadT"] = {"central"};
  central_or_shiftOptions_["METPhi"] = {"central"};
  central_or_shiftOptions_["METDeltaPhiLep1"] = {"central"};
  central_or_shiftOptions_["MET_LD"] = {"central"};
  central_or_shiftOptions_["HTmiss"] = {"central"};
  central_or_shiftOptions_["lep1_isElectron"] = {"central"};
  central_or_shiftOptions_["lep1_charge"] = {"central"};
  central_or_shiftOptions_["lep2_isElectron"] = {"central"};
  central_or_shiftOptions_["lep2_charge"] = {"central"};
  central_or_shiftOptions_["lep3_isElectron"] = {"central"};
  central_or_shiftOptions_["lep3_charge"] = {"central"};
  central_or_shiftOptions_["lep4_isElectron"] = {"central"};
  central_or_shiftOptions_["lep4_charge"] = {"central"};
  central_or_shiftOptions_["leptonChargeSum"] = {"central"};
  central_or_shiftOptions_["electronChargeSum"] = {"central"};
  central_or_shiftOptions_["muonChargeSum"] = {"central"};
  central_or_shiftOptions_["nSFOS"] = {"central"};
}

const TH1 *EvtHistManager_hh_4l::getHistogram_EventCounter() const { return histogram_EventCounter_; }

void EvtHistManager_hh_4l::bookHistograms(TFileDirectory &dir)
{
  histogram_numElectrons_ = book1D(dir, "numElectrons", "numElectrons", 7, -0.5, +6.5);
  histogram_numMuons_ = book1D(dir, "numMuons", "numMuons", 7, -0.5, +6.5);
  histogram_numLeptons_ = book1D(dir, "numLeptons", "numLeptons", 7, -0.5, +6.5);
  histogram_numJets_ = book1D(dir, "numJets", "numJets", 20, -0.5, +19.5);
  histogram_numJetsPtGt40_ = book1D(dir, "numJetsPtGt40", "numJetsPtGt40", 20, -0.5, +19.5);
  histogram_numBJets_loose_ = book1D(dir, "numBJets_loose", "numBJets_loose", 10, -0.5, +9.5);
  histogram_numBJets_medium_ = book1D(dir, "numBJets_medium", "numBJets_medium", 10, -0.5, +9.5);

  histogram_dihiggsVisMass_ = book1D(dir, "dihiggsVisMass", "dihiggsVisMass", 150, 0., 1500.);
  histogram_dihiggsMass_ = book1D(dir, "dihiggsMass", "dihiggsMass", 150, 0., 1500.);

  histogram_HT_ = book1D(dir, "HT", "HT", 150, 0., 1500.);
  histogram_STMET_ = book1D(dir, "STMET", "STMET", 150, 0., 1500.);

  histogram_EventCounter_ = book1D(dir, "EventCounter", "EventCounter", 1, -0.5, +0.5);
  histogram_lep1_pt_ = book1D(dir, "lep1_pt", "lep1_pt", 50, 0, 250);
  histogram_lep2_pt_ = book1D(dir, "lep2_pt", "lep2_pt", 50, 0, 250);
  histogram_lep3_pt_ = book1D(dir, "lep3_pt", "lep3_pt", 50, 0, 250);
  histogram_lep4_pt_ = book1D(dir, "lep4_pt", "lep4_pt", 50, 0, 250);
  histogram_lep1_conePt_ = book1D(dir, "lep1_conePt", "lep1_conePt", 50, 0, 250);
  histogram_lep2_conePt_ = book1D(dir, "lep2_conePt", "lep2_conePt", 50, 0, 250);
  histogram_lep3_conePt_ = book1D(dir, "lep3_conePt", "lep3_conePt", 50, 0, 250);
  histogram_lep4_conePt_ = book1D(dir, "lep4_conePt", "lep4_conePt", 50, 0, 250);
  histogram_lep1_eta_ = book1D(dir, "lep1_eta", "lep1_eta", 50, -2.5, 2.5);
  histogram_lep2_eta_ = book1D(dir, "lep2_eta", "lep2_eta", 50, -2.5, 2.5);
  histogram_lep3_eta_ = book1D(dir, "lep3_eta", "lep3_eta", 50, -2.5, 2.5);
  histogram_lep4_eta_ = book1D(dir, "lep4_eta", "lep4_eta", 50, -2.5, 2.5);
  histogram_lep1_phi_ = book1D(dir, "lep1_phi", "lep1_phi", 70, -3.5, 3.5);
  histogram_lep2_phi_ = book1D(dir, "lep2_phi", "lep2_phi", 70, -3.5, 3.5);
  histogram_lep3_phi_ = book1D(dir, "lep3_phi", "lep3_phi", 70, -3.5, 3.5);
  histogram_lep4_phi_ = book1D(dir, "lep4_phi", "lep4_phi", 70, -3.5, 3.5);
  histogram_lep1_dxy_ = book1D(dir, "lep1_dxy", "lep1_dxy", 100, 0, 0.02);
  histogram_lep2_dxy_ = book1D(dir, "lep2_dxy", "lep2_dxy", 100, 0, 0.02);
  histogram_lep3_dxy_ = book1D(dir, "lep3_dxy", "lep3_dxy", 100, 0, 0.02);
  histogram_lep4_dxy_ = book1D(dir, "lep4_dxy", "lep4_dxy", 100, 0, 0.02);
  histogram_lep1_dz_ = book1D(dir, "lep1_dz", "lep1_dz", 100, 0, 0.04);
  histogram_lep2_dz_ = book1D(dir, "lep2_dz", "lep2_dz", 100, 0, 0.04);
  histogram_lep3_dz_ = book1D(dir, "lep3_dz", "lep3_dz", 100, 0, 0.04);
  histogram_lep4_dz_ = book1D(dir, "lep4_dz", "lep4_dz", 100, 0, 0.04);
  histogram_pt4l_ = book1D(dir, "pt4l", "pt4l", 200, 0, 200);
  histogram_pt4lParallelHadT_ = book1D(dir, "pt4lParallelHadT", "pt4lParallelHadT", 200, -200, 200);
  histogram_pt4lPerpendicularHadT_ = book1D(dir, "pt4lPerpendicularHadT", "pt4lPerpendicularHadT", 200, 0, 200);
  histogram_mt4l_ = book1D(dir, "mt4l", "mt4l", 150, 0, 1500);
  histogram_maxPtSum_pair1_pt_ = book1D(dir, "maxPtSum_pair1_pt", "maxPtSum_pair1_pt", 50, 0, 250);
  histogram_maxPtSum_pair1_eta_ = book1D(dir, "maxPtSum_pair1_eta", "maxPtSum_pair1_eta", 80, -4, 4);
  histogram_maxPtSum_pair1_phi_ = book1D(dir, "maxPtSum_pair1_phi", "maxPtSum_pair1_phi", 70, -3.5, +3.5);
  histogram_maxPtSum_pair1_deltaEtaLep1_ = book1D(dir, "maxPtSum_pair1_deltaEtaLep1", "maxPtSum_pair1_deltaEtaLep1", 50, 0, 5);
  histogram_maxPtSum_pair1_deltaPhiLep1_ = book1D(dir, "maxPtSum_pair1_deltaPhiLep1", "maxPtSum_pair1_deltaPhiLep1", 35, 0, 3.5);
  histogram_maxPtSum_pair1_deltaEta_ = book1D(dir, "maxPtSum_pair1_deltaEta", "maxPtSum_pair1_deltaEta", 50, 0, 5);
  histogram_maxPtSum_pair1_deltaPhi_ = book1D(dir, "maxPtSum_pair1_deltaPhi", "maxPtSum_pair1_deltaPhi", 35, 0, 3.5);
  histogram_maxPtSum_pair1_deltaR_ = book1D(dir, "maxPtSum_pair1_deltaR", "maxPtSum_pair1_deltaR", 80, 0, 8);
  histogram_maxPtSum_pair1_deltaPt_ = book1D(dir, "maxPtSum_pair1_deltaPt", "maxPtSum_pair1_deltaPt", 200, 0, 200);
  histogram_maxPtSum_pair1_m_ = book1D(dir, "maxPtSum_pair1_m", "maxPtSum_pair1_m", 50, 0, 250);
  histogram_maxPtSum_pair2_pt_ = book1D(dir, "maxPtSum_pair2_pt", "maxPtSum_pair2_pt", 50, 0, 250);
  histogram_maxPtSum_pair2_eta_ = book1D(dir, "maxPtSum_pair2_eta", "maxPtSum_pair2_eta", 80, -4, 4);
  histogram_maxPtSum_pair2_phi_ = book1D(dir, "maxPtSum_pair2_phi", "maxPtSum_pair2_phi", 70, -3.5, +3.5);
  histogram_maxPtSum_pair2_deltaEtaLep1_ = book1D(dir, "maxPtSum_pair2_deltaEtaLep1", "maxPtSum_pair2_deltaEtaLep1", 50, 0, 5);
  histogram_maxPtSum_pair2_deltaPhiLep1_ = book1D(dir, "maxPtSum_pair2_deltaPhiLep1", "maxPtSum_pair2_deltaPhiLep1", 35, 0, 3.5);
  histogram_maxPtSum_pair2_deltaEta_ = book1D(dir, "maxPtSum_pair2_deltaEta", "maxPtSum_pair2_deltaEta", 50, 0, 5);
  histogram_maxPtSum_pair2_deltaPhi_ = book1D(dir, "maxPtSum_pair2_deltaPhi", "maxPtSum_pair2_deltaPhi", 35, 0, 3.5);
  histogram_maxPtSum_pair2_deltaR_ = book1D(dir, "maxPtSum_pair2_deltaR", "maxPtSum_pair2_deltaR", 80, 0, 8);
  histogram_maxPtSum_pair2_deltaPt_ = book1D(dir, "maxPtSum_pair2_deltaPt", "maxPtSum_pair2_deltaPt", 200, 0, 200);
  histogram_maxPtSum_pair2_m_ = book1D(dir, "maxPtSum_pair2_m", "maxPtSum_pair2_m", 50, 0, 250);
  histogram_MET_ = book1D(dir, "MET", "MET", 50, 0, 250);
  histogram_METParallelHadT_ = book1D(dir, "METParallelHadT", "METParallelHadT", 100, -250, 250);
  histogram_METPerpendicularHadT_ = book1D(dir, "METPerpendicularHadT", "METPerpendicularHadT", 50, 0, 250);
  histogram_METPhi_ = book1D(dir, "METPhi", "METPhi", 70, -3.5, +3.5);
  histogram_METDeltaPhiLep1_ = book1D(dir, "METDeltaPhiLep1", "METDeltaPhiLep1", 35, 0, +3.5);
  histogram_MET_LD_ = book1D(dir, "MET_LD", "MET_LD", 50, 0, 250);
  histogram_HTmiss_ = book1D(dir, "HTmiss", "HTmiss", 50, 0, 250);
  histogram_lep1_isElectron_ = book1D(dir, "lep1_isElectron", "lep1_isElectron", 2, 0, 2);
  histogram_lep1_charge_ = book1D(dir, "lep1_charge", "lep1_charge", 3, -1, 2);
  histogram_lep2_isElectron_ = book1D(dir, "lep2_isElectron", "lep2_isElectron", 2, 0, 2);
  histogram_lep2_charge_ = book1D(dir, "lep2_charge", "lep2_charge", 3, -1, 2);
  histogram_lep3_isElectron_ = book1D(dir, "lep3_isElectron", "lep3_isElectron", 2, 0, 2);
  histogram_lep3_charge_ = book1D(dir, "lep3_charge", "lep3_charge", 3, -1, 2);
  histogram_lep4_isElectron_ = book1D(dir, "lep4_isElectron", "lep4_isElectron", 2, 0, 2);
  histogram_lep4_charge_ = book1D(dir, "lep4_charge", "lep4_charge", 3, -1, 2);
  histogram_leptonChargeSum_ = book1D(dir, "leptonChargeSum", "leptonChargeSum", 5, -2, 3);
  histogram_electronChargeSum_ = book1D(dir, "electronChargeSum", "electronChargeSum", 5, -2, 3);
  histogram_muonChargeSum_ = book1D(dir, "muonChargeSum", "muonChargeSum", 5, -2, 3);
  histogram_nSFOS_ = book1D(dir, "nSFOS", "nSFOS", 5, 0, 5);
}

void EvtHistManager_hh_4l::fillHistograms(
    int numElectrons, int numMuons, int numLeptons, int numJets, int numJetsPtGt40, int numBJets_loose, int numBJets_medium, double dihiggsVisMass, double dihiggsMass, double HT,
    double STMET, double lep1_pt, double lep2_pt, double lep3_pt, double lep4_pt, double lep1_conePt, double lep2_conePt, double lep3_conePt, double lep4_conePt,
    double lep1_eta, double lep2_eta, double lep3_eta, double lep4_eta, double lep1_phi, double lep2_phi, double lep3_phi, double lep4_phi, double lep1_dxy, double lep2_dxy, 
    double lep3_dxy, double lep4_dxy, double lep1_dz, double lep2_dz, double lep3_dz, double lep4_dz, double pt4l, double pt4lParallelHadT, double pt4lPerpendicularHadT, double mt4l, 
    double maxPtSum_pair1_pt, double maxPtSum_pair1_eta, double maxPtSum_pair1_phi, double maxPtSum_pair1_deltaEtaLep1, double maxPtSum_pair1_deltaPhiLep1, double maxPtSum_pair1_deltaEta,
    double maxPtSum_pair1_deltaPhi, double maxPtSum_pair1_deltaR, double maxPtSum_pair1_deltaPt, double maxPtSum_pair1_m, double maxPtSum_pair2_pt,
    double maxPtSum_pair2_eta, double maxPtSum_pair2_phi, double maxPtSum_pair2_deltaEtaLep1, double maxPtSum_pair2_deltaPhiLep1, double maxPtSum_pair2_deltaEta,
    double maxPtSum_pair2_deltaPhi, double maxPtSum_pair2_deltaR, double maxPtSum_pair2_deltaPt, double maxPtSum_pair2_m, double MET, double METParallelHadT, 
    double METPerpendicularHadT, double METPhi, double METDeltaPhiLep1, double MET_LD, double HTmiss, int lep1_isElectron, int lep1_charge, int lep2_isElectron, int lep2_charge, 
    int lep3_isElectron, int lep3_charge, int lep4_isElectron, int lep4_charge, int leptonChargeSum, int electronChargeSum, int muonChargeSum, int nSFOS, double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_, numElectrons, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_, numMuons, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numLeptons_, numLeptons, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_, numJets, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsPtGt40_, numJetsPtGt40, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_, numBJets_loose, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_, numBJets_medium, evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_dihiggsVisMass_, dihiggsVisMass, evtWeight, evtWeightErr);
  if (dihiggsMass > 0.)
  {
    fillWithOverFlow(histogram_dihiggsMass_, dihiggsMass, evtWeight, evtWeightErr);
  }

  fillWithOverFlow(histogram_HT_, HT, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_, STMET, evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_EventCounter_, 0., evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep1_pt_, lep1_pt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep2_pt_, lep2_pt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep3_pt_, lep3_pt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep4_pt_, lep4_pt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep1_conePt_, lep1_conePt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep2_conePt_, lep2_conePt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep3_conePt_, lep3_conePt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep4_conePt_, lep4_conePt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep1_eta_, lep1_eta, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep2_eta_, lep2_eta, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep3_eta_, lep3_eta, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep4_eta_, lep4_eta, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep1_phi_, lep1_phi, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep2_phi_, lep2_phi, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep3_phi_, lep3_phi, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep4_phi_, lep4_phi, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep1_dxy_, lep1_dxy, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep2_dxy_, lep2_dxy, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep3_dxy_, lep3_dxy, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep4_dxy_, lep4_dxy, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep1_dz_, lep1_dz, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep2_dz_, lep2_dz, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep3_dz_, lep3_dz, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep4_dz_, lep4_dz, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pt4l_, pt4l, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pt4lParallelHadT_, pt4lParallelHadT, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pt4lPerpendicularHadT_, pt4lPerpendicularHadT, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mt4l_, mt4l, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair1_pt_, maxPtSum_pair1_pt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair1_eta_, maxPtSum_pair1_eta, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair1_phi_, maxPtSum_pair1_phi, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair1_deltaEtaLep1_, maxPtSum_pair1_deltaEtaLep1, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair1_deltaPhiLep1_, maxPtSum_pair1_deltaPhiLep1, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair1_deltaEta_, maxPtSum_pair1_deltaEta, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair1_deltaPhi_, maxPtSum_pair1_deltaPhi, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair1_deltaR_, maxPtSum_pair1_deltaR, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair1_deltaPt_, maxPtSum_pair1_deltaPt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair1_m_, maxPtSum_pair1_m, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair2_pt_, maxPtSum_pair2_pt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair2_eta_, maxPtSum_pair2_eta, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair2_phi_, maxPtSum_pair2_phi, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair2_deltaEtaLep1_, maxPtSum_pair2_deltaEtaLep1, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair2_deltaPhiLep1_, maxPtSum_pair2_deltaPhiLep1, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair2_deltaEta_, maxPtSum_pair2_deltaEta, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair2_deltaPhi_, maxPtSum_pair2_deltaPhi, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair2_deltaR_, maxPtSum_pair2_deltaR, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair2_deltaPt_, maxPtSum_pair2_deltaPt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxPtSum_pair2_m_, maxPtSum_pair2_m, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MET_, MET, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_METParallelHadT_, METParallelHadT, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_METPerpendicularHadT_, METPerpendicularHadT, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_METPhi_, METPhi, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_METDeltaPhiLep1_, METDeltaPhiLep1, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MET_LD_, MET_LD, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_HTmiss_, HTmiss, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep1_isElectron_, lep1_isElectron, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep1_charge_, lep1_charge, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep2_isElectron_, lep2_isElectron, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep2_charge_, lep2_charge, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep3_isElectron_, lep3_isElectron, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep3_charge_, lep3_charge, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep4_isElectron_, lep4_isElectron, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep4_charge_, lep4_charge, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_leptonChargeSum_, leptonChargeSum, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_electronChargeSum_, electronChargeSum, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_muonChargeSum_, muonChargeSum, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_nSFOS_, nSFOS, evtWeight, evtWeightErr);
}
