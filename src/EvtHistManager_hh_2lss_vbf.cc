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
  central_or_shiftOptions_["mindR_vbfjet_lep1"] = { "central" };
  central_or_shiftOptions_["mindR_vbfjet_lep2"] = { "central" };
  central_or_shiftOptions_["maxJetEta_vbf"] = { "central" };
  central_or_shiftOptions_["minJetEta_vbf"] = { "central" };

  central_or_shiftOptions_["lhe_dEta_jj"] = { "central" };
  central_or_shiftOptions_["lhe_dPhi_jj"] = { "central" };
  central_or_shiftOptions_["lhe_m_jj"] = { "central" };
  central_or_shiftOptions_["lhe_dR_jj"] = { "central" };

  central_or_shiftOptions_["matched_dEta_jj"] = { "central" };
  central_or_shiftOptions_["matched_dPhi_jj"] = { "central" };
  central_or_shiftOptions_["matched_m_jj"] = { "central" };
  central_or_shiftOptions_["matched_dR_jj"] = { "central" };

  central_or_shiftOptions_["best_dEta_jj"] = { "central" };
  central_or_shiftOptions_["best_dPhi_jj"] = { "central" };
  central_or_shiftOptions_["best_m_jj"] = { "central" };
  central_or_shiftOptions_["best_dR_jj"] = { "central" };

  central_or_shiftOptions_["lhe_pt_lead"] = { "central" };
  central_or_shiftOptions_["lhe_pt_sublead"] = { "central" };
  central_or_shiftOptions_["matched_pt_lead"] = { "central" };
  central_or_shiftOptions_["matched_pt_sublead"] = { "central" };
  central_or_shiftOptions_["best_pt_lead"] = { "central" };
  central_or_shiftOptions_["best_pt_sublead"] = { "central" };

  central_or_shiftOptions_["genjet_dEta_jj"] = { "central" };
  central_or_shiftOptions_["genjet_dPhi_jj"] = { "central" };
  central_or_shiftOptions_["genjet_m_jj"] = { "central" };
  central_or_shiftOptions_["genjet_dR_jj"] = { "central" };

  central_or_shiftOptions_["mass_jj_W"] = { "central" };
  central_or_shiftOptions_["mass_jj_W2"] = { "central" };
  central_or_shiftOptions_["sum_mass_W"] = { "central" };

  central_or_shiftOptions_["sum_m_lj"] = { "central" };
  central_or_shiftOptions_["pT_sum"] = { "central" };
  central_or_shiftOptions_["m_ll"] = { "central" };
  central_or_shiftOptions_["isVBF"] = { "central" };

  central_or_shiftOptions_["maxJetPt_vbf"] = { "central" };
  central_or_shiftOptions_["minJetPt_vbf"] = { "central" };
  central_or_shiftOptions_["mindR_vbfJet_W1"] = { "central" };
  central_or_shiftOptions_["maxdR_vbfJet_W1"] = { "central" };
  central_or_shiftOptions_["mindR_vbfjet_lep"] = { "central" };
  central_or_shiftOptions_["maxdR_vbfjet_lep"] = { "central" };

  central_or_shiftOptions_["dR_h1h2"] = { "central" };
  central_or_shiftOptions_["pT_h1"] = { "central" };
  central_or_shiftOptions_["pT_h2"] = { "central" };
  central_or_shiftOptions_["dR_h1_j1"] = { "central" };
  central_or_shiftOptions_["dR_h1_j2"] = { "central" };
  central_or_shiftOptions_["dR_h2_j1"] = { "central" };
  central_or_shiftOptions_["dR_h2_j2"] = { "central" };
  central_or_shiftOptions_["mass_h1"] = { "central" };
  central_or_shiftOptions_["mass_h2"] = { "central" };
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
  histogram_vbf_dR_jj_ = book1D(
      dir, "vbf_dR_jj", "vbf_dR_jj", 100, 0.,10);
  histogram_EventCounter_ = book1D(
      dir, "EventCounter", "EventCounter", 1, -0.5, +0.5);
  histogram_mindR_vbfjet_lep1_   = book1D(dir, "mindR_vbfjet_lep1",   "mindR_vbfjet_lep1",   100, 0,   7);
  histogram_mindR_vbfjet_lep2_   = book1D(dir, "mindR_vbfjet_lep2",   "mindR_vbfjet_lep2",   100, 0,   7);
  histogram_maxJetEta_vbf_      = book1D(dir, "maxJetEta_vbf",      "maxJetEta_vbf",      100, 0, 5);
  histogram_minJetEta_vbf_      = book1D(dir, "minJetEta_vbf",      "minJetEta_vbf",      100, 0, 5);

  histogram_lhe_dEta_jj_ = book1D(
      dir, "lhe_dEta_jj", "lhe_dEta_jj", 50, -10.,10);
  histogram_lhe_dPhi_jj_ = book1D(
      dir, "lhe_dPhi_jj", "lhe_dPhi_jj", 50, -10.,10);
  histogram_lhe_m_jj_ = book1D(
      dir, "lhe_m_jj", "lhe_m_jj", 250, 0., 5000);
  histogram_lhe_dR_jj_ = book1D(
      dir, "lhe_dR_jj", "lhe_dR_jj", 100, 0., 10);

  histogram_matched_dEta_jj_ = book1D(
      dir, "matched_dEta_jj", "matched_dEta_jj", 50, -10.,10);
  histogram_matched_dPhi_jj_ = book1D(
      dir, "matched_dPhi_jj", "matched_dPhi_jj", 50, -10.,10);
  histogram_matched_m_jj_ = book1D(
      dir, "matched_m_jj", "matched_m_jj", 250, 0., 5000);
  histogram_matched_dR_jj_ = book1D(
      dir, "matched_dR_jj", "matched_dR_jj", 100, 0., 10);

  histogram_best_dEta_jj_ = book1D(
      dir, "best_dEta_jj", "best_dEta_jj", 50, -10.,10);
  histogram_best_dPhi_jj_ = book1D(
      dir, "best_dPhi_jj", "best_dPhi_jj", 50, -10.,10);
  histogram_best_m_jj_ = book1D(
      dir, "best_m_jj", "best_m_jj", 250, 0., 5000);
  histogram_best_dR_jj_ = book1D(
      dir, "best_dR_jj", "best_dR_jj", 100, 0., 10);


  histogram_lhe_pt_lead_ = book1D(
      dir, "lhe_pt_lead", "lhe_pt_lead", 100, 0., 1000);
  histogram_lhe_pt_sublead_ = book1D(
      dir, "lhe_pt_sublead", "lhe_pt_sublead", 100, 0., 1000);
  histogram_matched_pt_lead_ = book1D(
      dir, "matched_pt_lead", "matched_pt_lead", 100, 0., 1000);
  histogram_matched_pt_sublead_ = book1D(
      dir, "matched_pt_sublead", "matched_pt_sublead", 100, 0., 1000);
  histogram_best_pt_lead_ = book1D(
      dir, "best_pt_lead", "best_pt_lead", 100, 0., 1000);
  histogram_best_pt_sublead_ = book1D(
      dir, "best_pt_sublead", "best_pt_sublead", 100, 0., 1000);


  histogram_genjet_dEta_jj_ = book1D(
      dir, "genjet_dEta_jj", "genjet_dEta_jj", 50, -10.,10);
  histogram_genjet_dPhi_jj_ = book1D(
      dir, "genjet_dPhi_jj", "genjet_dPhi_jj", 50, -10.,10);
  histogram_genjet_m_jj_ = book1D(
      dir, "genjet_m_jj", "genjet_m_jj", 250, 0., 5000);
  histogram_genjet_dR_jj_ = book1D(
      dir, "genjet_dR_jj", "genjet_dR_jj", 100, 0., 10);

  histogram_mass_jj_W_ = book1D(
      dir, "mass_jj_W", "mass_jj_W", 50, 0., 150);
  histogram_mass_jj_W2_ = book1D(
      dir, "mass_jj_W2", "mass_jj_W2", 50, 0., 150);
  histogram_sum_mass_W_ = book1D(
      dir, "sum_mass_W", "sum_mass_W", 50, 0., 300);

  histogram_sum_m_lj_ = book1D(
      dir, "sum_m_lj", "sum_m_lj", 250, 0., 5000);
  histogram_pT_sum_ = book1D(
      dir, "pT_sum", "pT_sum", 100, 0., 1000);
  histogram_m_ll_ = book1D(
      dir, "m_ll", "m_ll", 250, 0., 5000);
  histogram_isVBF_ = book1D(
      dir, "isVBF", "isVBF", 20, -0.5, +19.5);

  histogram_maxJetPt_vbf_ = book1D(
      dir, "maxJetPt_vbf", "maxJetPt_vbf", 30, 0., 600);
    histogram_minJetPt_vbf_ = book1D(
      dir, "minJetPt_vbf", "minJetPt_vbf", 30, 0., 600);
  histogram_mindR_vbfJet_W1_ = book1D(
      dir, "mindR_vbfJet_W1", "mindR_vbfJet_W1", 100, 0., 10);
  histogram_maxdR_vbfJet_W1_ = book1D(
      dir, "maxdR_vbfJet_W1", "maxdR_vbfJet_W1", 100, 0., 10);
  histogram_mindR_vbfjet_lep_ = book1D(
      dir, "mindR_vbfjet_lep", "mindR_vbfjet_lep", 100, 0., 10);
  histogram_maxdR_vbfjet_lep_ = book1D(
      dir, "maxdR_vbfjet_lep", "maxdR_vbfjet_lep", 100, 0., 10);

  histogram_dR_h1h2_ = book1D(
      dir, "dR_h1h2", "dR_h1h2", 100, 0., 10);
  histogram_pT_h1_ = book1D(
      dir, "pT_h1", "pT_h1", 100, 0., 1000);
  histogram_pT_h2_ = book1D(
      dir, "pT_h2", "pT_h2", 100, 0., 1000);
  histogram_dR_h1_j1_ = book1D(
      dir, "dR_h1_j1", "dR_h1_j1", 100, 0., 10);
  histogram_dR_h1_j2_ = book1D(
      dir, "dR_h1_j2", "dR_h1_j2", 100, 0., 10);
  histogram_dR_h2_j1_ = book1D(
      dir, "dR_h2_j1", "dR_h2_j1", 100, 0., 10);
  histogram_dR_h2_j2_ = book1D(
      dir, "dR_h2_j2", "dR_h2_j2", 100, 0., 10);
  histogram_mass_h1_ = book1D(
      dir, "mass_h1", "mass_h1", 30, 0., 600);
  histogram_mass_h2_ = book1D(
      dir, "mass_h2", "mass_h2", 30, 0., 600);
}

void EvtHistManager_hh_2lss_vbf::fillHistograms(
    int numElectrons, int numMuons, int numJets, int numJetsPtGt40,
    double dihiggsVisMass, double dihiggsMass_wMet, double vbf_m_jj,
    double vbf_dEta_jj, double vbf_dR_jj, double evtWeight,
    double mindR_vbfjet_lep1, double mindR_vbfjet_lep2,
    double maxJetEta_vbf, double minJetEta_vbf,
    double lhe_dEta_jj, double lhe_dPhi_jj, double lhe_m_jj, double lhe_dR_jj,
    double matched_dEta_jj, double matched_dPhi_jj, double matched_m_jj, double matched_dR_jj,
    double best_dEta_jj, double best_dPhi_jj, double best_m_jj, double best_dR_jj,
    double lhe_pt_lead, double lhe_pt_sublead, double matched_pt_lead, double matched_pt_sublead, double best_pt_lead, double best_pt_sublead,
    double genjet_dEta_jj, double genjet_dPhi_jj, double genjet_m_jj, double genjet_dR_jj,
    double mass_jj_W, double mass_jj_W2, double sum_mass_W,
    double sum_m_lj, double pT_sum, double m_ll, bool isVBF,
    double maxJetPt_vbf, double minJetPt_vbf, double mindR_vbfJet_W1, double maxdR_vbfJet_W1, double mindR_vbfjet_lep, double maxdR_vbfjet_lep,
    double dR_h1h2, double pT_h1, double pT_h2, double dR_h1_j1, double dR_h1_j2, double dR_h2_j1, double dR_h2_j2, double mass_h1, double mass_h2
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
  fillWithOverFlow(histogram_vbf_dEta_jj_, vbf_dEta_jj,
                   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbf_dR_jj_, vbf_dR_jj,
                     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_, 0., evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mindR_vbfjet_lep1_,   mindR_vbfjet_lep1,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mindR_vbfjet_lep2_,   mindR_vbfjet_lep2,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxJetEta_vbf_,      maxJetEta_vbf,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_minJetEta_vbf_,      minJetEta_vbf,      evtWeight, evtWeightErr);

  if(lhe_dEta_jj>-999){
  fillWithOverFlow(histogram_lhe_dEta_jj_,      lhe_dEta_jj,      evtWeight, evtWeightErr);
  }
  if(lhe_dPhi_jj>-999){
  fillWithOverFlow(histogram_lhe_dPhi_jj_,      lhe_dPhi_jj,      evtWeight, evtWeightErr);
  }
  if(lhe_m_jj>0){
  fillWithOverFlow(histogram_lhe_m_jj_,         lhe_m_jj,         evtWeight, evtWeightErr);
  }
  if(lhe_dR_jj>0){
  fillWithOverFlow(histogram_lhe_dR_jj_,        lhe_dR_jj,        evtWeight, evtWeightErr);
  }

  if(matched_dEta_jj>-999){
      fillWithOverFlow(histogram_matched_dEta_jj_,     matched_dEta_jj,     evtWeight, evtWeightErr);
  }
  if(matched_dPhi_jj>-999){
      fillWithOverFlow(histogram_matched_dPhi_jj_,     matched_dPhi_jj,     evtWeight, evtWeightErr);
  }
  if(matched_m_jj>0){
      fillWithOverFlow(histogram_matched_m_jj_,        matched_m_jj,        evtWeight, evtWeightErr);
  }
  if(matched_dR_jj>0){
      fillWithOverFlow(histogram_matched_dR_jj_,       matched_dR_jj,       evtWeight, evtWeightErr);
  }

  if(best_dEta_jj>-999){
      fillWithOverFlow(histogram_best_dEta_jj_,      best_dEta_jj,      evtWeight, evtWeightErr);
  }
  if(best_dPhi_jj>-999){
      fillWithOverFlow(histogram_best_dPhi_jj_,      best_dPhi_jj,      evtWeight, evtWeightErr);
  }
  if(best_m_jj>0){
      fillWithOverFlow(histogram_best_m_jj_,         best_m_jj,         evtWeight, evtWeightErr);
  }
  if(best_dR_jj>0){
      fillWithOverFlow(histogram_best_dR_jj_,        best_dR_jj,        evtWeight, evtWeightErr);
  }

  if(lhe_pt_lead>0){
      fillWithOverFlow(histogram_lhe_pt_lead_,        lhe_pt_lead,        evtWeight, evtWeightErr);
  }
  if(lhe_pt_sublead>0){
      fillWithOverFlow(histogram_lhe_pt_sublead_,        lhe_pt_sublead,        evtWeight, evtWeightErr);
  }
  if(matched_pt_lead>0){
      fillWithOverFlow(histogram_matched_pt_lead_,        matched_pt_lead,        evtWeight, evtWeightErr);
  }
  if(matched_pt_sublead>0){
      fillWithOverFlow(histogram_matched_pt_sublead_,        matched_pt_sublead,        evtWeight, evtWeightErr);
  }
  if(best_pt_lead>0){
      fillWithOverFlow(histogram_best_pt_lead_,        best_pt_lead,        evtWeight, evtWeightErr);
  }
  if(best_pt_sublead>0){
      fillWithOverFlow(histogram_best_pt_sublead_,        best_pt_sublead,        evtWeight, evtWeightErr);
  }

  if(genjet_dEta_jj>-999){
      fillWithOverFlow(histogram_genjet_dEta_jj_,     genjet_dEta_jj,     evtWeight, evtWeightErr);
  }
  if(genjet_dPhi_jj>-999){
      fillWithOverFlow(histogram_genjet_dPhi_jj_,     genjet_dPhi_jj,     evtWeight, evtWeightErr);
  }
  if(genjet_m_jj>0){
      fillWithOverFlow(histogram_genjet_m_jj_,        genjet_m_jj,        evtWeight, evtWeightErr);
  }
  if(genjet_dR_jj>0){
      fillWithOverFlow(histogram_genjet_dR_jj_,       genjet_dR_jj,       evtWeight, evtWeightErr);
  }

  if(mass_jj_W>0){
      fillWithOverFlow(histogram_mass_jj_W_,       mass_jj_W,       evtWeight, evtWeightErr);
  }
  if(mass_jj_W2>0){
      fillWithOverFlow(histogram_mass_jj_W2_,       mass_jj_W2,       evtWeight, evtWeightErr);
  }
  if(sum_mass_W>0){
      fillWithOverFlow(histogram_sum_mass_W_,       sum_mass_W,       evtWeight, evtWeightErr);
  }

  if(sum_m_lj>0){
      fillWithOverFlow(histogram_sum_m_lj_,       sum_m_lj,       evtWeight, evtWeightErr);
  }
  if(pT_sum>0){
      fillWithOverFlow(histogram_pT_sum_,       pT_sum,       evtWeight, evtWeightErr);
  }
  if(m_ll>0){
      fillWithOverFlow(histogram_m_ll_,       m_ll,       evtWeight, evtWeightErr);
  }
  fillWithOverFlow(histogram_isVBF_,       isVBF,       evtWeight, evtWeightErr);

  if(maxJetPt_vbf>0){
      fillWithOverFlow(histogram_maxJetPt_vbf_,       maxJetPt_vbf,       evtWeight, evtWeightErr);
  }
  if(minJetPt_vbf>0){
      fillWithOverFlow(histogram_minJetPt_vbf_,       minJetPt_vbf,       evtWeight, evtWeightErr);
  }
  if(mindR_vbfJet_W1>0){
      fillWithOverFlow(histogram_mindR_vbfJet_W1_,       mindR_vbfJet_W1,       evtWeight, evtWeightErr);
  }
  if(maxdR_vbfJet_W1>0){
      fillWithOverFlow(histogram_maxdR_vbfJet_W1_,       maxdR_vbfJet_W1,       evtWeight, evtWeightErr);
  }
  if(mindR_vbfjet_lep>0){
      fillWithOverFlow(histogram_mindR_vbfjet_lep_,       mindR_vbfjet_lep,       evtWeight, evtWeightErr);
  }
  if(maxdR_vbfjet_lep>0){
      fillWithOverFlow(histogram_maxdR_vbfjet_lep_,       maxdR_vbfjet_lep,       evtWeight, evtWeightErr);
  }

  if(dR_h1h2>0){
      fillWithOverFlow(histogram_dR_h1h2_,       dR_h1h2,       evtWeight, evtWeightErr);
  }
  if(pT_h1>0){
      fillWithOverFlow(histogram_pT_h1_,       pT_h1,       evtWeight, evtWeightErr);
  }
  if(pT_h2>0){
      fillWithOverFlow(histogram_pT_h2_,       pT_h2,       evtWeight, evtWeightErr);
  }
  if(dR_h1_j1>0){
      fillWithOverFlow(histogram_dR_h1_j1_,       dR_h1_j1,       evtWeight, evtWeightErr);
  }
  if(dR_h1_j2>0){
      fillWithOverFlow(histogram_dR_h1_j2_,       dR_h1_j2,       evtWeight, evtWeightErr);
  }
  if(dR_h2_j1>0){
      fillWithOverFlow(histogram_dR_h2_j1_,       dR_h2_j1,       evtWeight, evtWeightErr);
  }
  if(dR_h2_j2>0){
      fillWithOverFlow(histogram_dR_h2_j2_,       dR_h2_j2,       evtWeight, evtWeightErr);
  }
  if(mass_h1<999){
      fillWithOverFlow(histogram_mass_h1_,       mass_h1,       evtWeight, evtWeightErr);
  }
  if(mass_h2<999){
      fillWithOverFlow(histogram_mass_h2_,       mass_h2,       evtWeight, evtWeightErr);
  }
}
