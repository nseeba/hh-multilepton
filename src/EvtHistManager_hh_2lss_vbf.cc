#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_2lss_vbf.h"
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()
#include <TMath.h> // TMath::Pi()

EvtHistManager_hh_2lss_vbf::EvtHistManager_hh_2lss_vbf(
    const edm::ParameterSet &cfg)
    : HistManagerBase(cfg) {
  central_or_shiftOptions_["numElectrons"] = {"central"};
  central_or_shiftOptions_["numMuons"] = {"central"};
  central_or_shiftOptions_["numJets"] = {"central"};
  central_or_shiftOptions_["numJetsPtGt40"] = {"central"};
  central_or_shiftOptions_["dihiggsVisMass"] = {"*"};
  central_or_shiftOptions_["dihiggsMass_wMet"] = {"central"};
  central_or_shiftOptions_["vbf_m_jj"] = {"central"};
  central_or_shiftOptions_["vbf_dEta_jj"] = {"central"};
  central_or_shiftOptions_["vbf_dR_jj"] = {"central"};
  central_or_shiftOptions_["EventCounter"] = {"*"};
  central_or_shiftOptions_["nJet_vbf"] = {"central"};
  central_or_shiftOptions_["isVBF"] = {"central"};
  central_or_shiftOptions_["mindr_lep1_jet"] = { "central" };
  central_or_shiftOptions_["mindr_lep2_jet"] = { "central" };
  central_or_shiftOptions_["max_jet_eta"] = { "central" };
  central_or_shiftOptions_["matched_dEta_jj"] = { "central" };
  central_or_shiftOptions_["matched_m_jj"] = { "central" };
  central_or_shiftOptions_["matched_dR_jj"] = { "central" };
  central_or_shiftOptions_["lhe_dEta_jj"] = { "central" };
  central_or_shiftOptions_["lhe_m_jj"] = { "central" };
  central_or_shiftOptions_["lhe_dR_jj"] = { "central" };
  central_or_shiftOptions_["best_m_jj"] = { "central" };
  central_or_shiftOptions_["best_dEta_jj"] = { "central" };
  central_or_shiftOptions_["best_dR_jj"] = { "central" };
}

const TH1 *EvtHistManager_hh_2lss_vbf::getHistogram_EventCounter() const {
  return histogram_EventCounter_;
}

void EvtHistManager_hh_2lss_vbf::bookHistograms(TFileDirectory &dir) {
  histogram_numElectrons_ = book1D(
      dir, "numElectrons", "numElectrons", 5, -0.5, +4.5);
  histogram_numMuons_ = book1D(
      dir, "numMuons", "numMuons", 5, -0.5, +4.5);
  histogram_numJets_ = book1D(
      dir, "numJets", "numJets", 20, -0.5, +19.5);
  histogram_numJetsPtGt40_ = book1D(
      dir, "numJetsPtGt40", "numJetsPtGt40", 20, -0.5, +19.5);
  histogram_dihiggsVisMass_ = book1D(
      dir, "dihiggsVisMass", "dihiggsVisMass", 150, 0., 1500);
  histogram_dihiggsMass_wMet_ = book1D(
      dir, "dihiggsMass_wMet", "dihiggsMass_wMet", 150, 0., 1500);
  histogram_vbf_m_jj_ = book1D(
      dir, "vbf_m_jj", "vbf_m_jj", 250, 0., 5000);
  histogram_vbf_dEta_jj_ = book1D(
      dir, "vbf_dEta_jj", "vbf_dEta_jj", 50, -10.,10);
  histogram_vbf_dEta_jj_ = book1D(
      dir, "vbf_dR_jj", "vbf_dR_jj", 100, 0.,10);
  histogram_EventCounter_ = book1D(
      dir, "EventCounter", "EventCounter", 1, -0.5, +0.5);
  histogram_nJet_vbf_ = book1D(
      dir, "nJet_vbf", "nJet_vbf", 20, -0.5, +19.5);
  histogram_isVBF_ = book1D(
      dir, "isVBF", "isVBF", 20, -0.5, +19.5);
  histogram_mindr_lep1_jet_   = book1D(dir, "mindr_lep1_jet",   "mindr_lep1_jet",   100, 0,   7);
  histogram_mindr_lep2_jet_   = book1D(dir, "mindr_lep2_jet",   "mindr_lep2_jet",   100, 0,   7);
  histogram_max_jet_eta_      = book1D(dir, "max_jet_eta",      "max_jet_eta",      100, 0, 5);
  histogram_matched_dEta_jj_ = book1D(
      dir, "matched_dEta_jj", "matched_dEta_jj", 50, -10.,10);
  histogram_matched_m_jj_ = book1D(
      dir, "matched_m_jj", "matched_m_jj", 250, 0., 5000);
  histogram_matched_dR_jj_ = book1D(
      dir, "matched_dR_jj", "matched_dR_jj", 100, 0., 10);
  histogram_lhe_dEta_jj_ = book1D(
      dir, "lhe_dEta_jj", "lhe_dEta_jj", 50, -10.,10);
  histogram_lhe_m_jj_ = book1D(
      dir, "lhe_m_jj", "lhe_m_jj", 250, 0., 5000);
  histogram_lhe_dR_jj_ = book1D(
      dir, "lhe_dR_jj", "lhe_dR_jj", 100, 0., 10);
  histogram_best_dEta_jj_ = book1D(
      dir, "best_dEta_jj", "best_dEta_jj", 50, -10.,10);
  histogram_best_m_jj_ = book1D(
      dir, "best_m_jj", "best_m_jj", 250, 0., 5000);
  histogram_best_dR_jj_ = book1D(
      dir, "best_dR_jj", "best_dR_jj", 100, 0., 10);
}

void EvtHistManager_hh_2lss_vbf::fillHistograms(
    int numElectrons, int numMuons, int numJets, int numJetsPtGt40,
    double dihiggsVisMass, double dihiggsMass_wMet, double vbf_m_jj,
    double vbf_dEta_jj, double vbf_dR_jj, double evtWeight
    , int nJet_vbf, int isVBF,
    double mindr_lep1_jet, double mindr_lep2_jet,
    double max_jet_eta, 
    double matched_dEta_jj, double matched_m_jj, double matched_dR_jj, 
    double lhe_dEta_jj, double lhe_m_jj, double lhe_dR_jj,
    double best_m_jj, double best_dEta_jj, double best_dR_jj
    )

{
  const double evtWeightErr = 0.;
  fillWithOverFlow(histogram_numElectrons_, numElectrons, evtWeight,
                   evtWeightErr);
  fillWithOverFlow(histogram_numMuons_, numMuons, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_, numJets, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsPtGt40_, numJetsPtGt40, evtWeight,
                   evtWeightErr);
  fillWithOverFlow(histogram_dihiggsVisMass_, dihiggsVisMass, evtWeight,
                   evtWeightErr);
  fillWithOverFlow(histogram_dihiggsMass_wMet_, dihiggsMass_wMet,
                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_m_jj_, vbf_m_jj,
                   evtWeight, evtWeightErr);
  if(vbf_dEta_jj>-999){
  fillWithOverFlow(histogram_vbf_dEta_jj_, vbf_dEta_jj,
                   evtWeight, evtWeightErr);
  }
  if(vbf_dR_jj>0){
    fillWithOverFlow(histogram_vbf_dR_jj_, vbf_dR_jj,
                     evtWeight, evtWeightErr);
  }
  fillWithOverFlow(histogram_EventCounter_, 0., evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_nJet_vbf_, nJet_vbf,
                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_isVBF_, isVBF,
                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mindr_lep1_jet_,   mindr_lep1_jet,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mindr_lep2_jet_,   mindr_lep2_jet,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_max_jet_eta_,      max_jet_eta,      evtWeight, evtWeightErr);
  if(matched_dEta_jj>-999){
      fillWithOverFlow(histogram_matched_dEta_jj_,     matched_dEta_jj,     evtWeight, evtWeightErr);
  }
  if(matched_m_jj>0){
      fillWithOverFlow(histogram_matched_m_jj_,        matched_m_jj,        evtWeight, evtWeightErr);
  }
  if(matched_dR_jj>0){
      fillWithOverFlow(histogram_matched_dR_jj_,       matched_dR_jj,       evtWeight, evtWeightErr);
  }
  fillWithOverFlow(histogram_lhe_dEta_jj_,      lhe_dEta_jj,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lhe_m_jj_,         lhe_m_jj,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lhe_dR_jj_,        lhe_dR_jj,        evtWeight, evtWeightErr);
  if(best_dEta_jj>-999){
    fillWithOverFlow(histogram_best_dEta_jj_,      best_dEta_jj,      evtWeight, evtWeightErr);
  }
  if(best_m_jj>0){
    fillWithOverFlow(histogram_best_m_jj_,         best_m_jj,         evtWeight, evtWeightErr);
  }
  if(best_dR_jj>0){
    fillWithOverFlow(histogram_best_dR_jj_,        best_dR_jj,        evtWeight, evtWeightErr);
  }
}
