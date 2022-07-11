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

  central_or_shiftOptions_["EventCounter"] = {"*"};
  central_or_shiftOptions_["nJet_vbf"] = {"central"};
  central_or_shiftOptions_["isVBF"] = {"central"};
  central_or_shiftOptions_["mindR_vbfjet_lep1"] = { "central" };
  central_or_shiftOptions_["mindR_vbfjet_lep2"] = { "central" };
  central_or_shiftOptions_["maxJetEta_vbf"] = { "central" };
  central_or_shiftOptions_["minJetEta_vbf"] = { "central" };

  // central_or_shiftOptions_["lhe_dEta_jj"] = { "central" };
  // central_or_shiftOptions_["lhe_dPhi_jj"] = { "central" };
  // central_or_shiftOptions_["lhe_m_jj"] = { "central" };
  // central_or_shiftOptions_["lhe_dR_jj"] = { "central" };

  // central_or_shiftOptions_["matched_dEta_jj"] = { "central" };
  // central_or_shiftOptions_["matched_dPhi_jj"] = { "central" };
  // central_or_shiftOptions_["matched_m_jj"] = { "central" };
  // central_or_shiftOptions_["matched_dR_jj"] = { "central" };

  central_or_shiftOptions_["vbf_dEta_jj"] = { "central" };
  central_or_shiftOptions_["vbf_dPhi_jj"] = { "central" };
  central_or_shiftOptions_["vbf_m_jj"] = { "central" };
  central_or_shiftOptions_["vbf_dR_jj"] = { "central" };

  // central_or_shiftOptions_["lhe_pt_lead"] = { "central" };
  // central_or_shiftOptions_["lhe_pt_sublead"] = { "central" };
  // central_or_shiftOptions_["matched_pt_lead"] = { "central" };
  // central_or_shiftOptions_["matched_pt_sublead"] = { "central" };
  central_or_shiftOptions_["vbf_pt_lead"] = { "central" };
  central_or_shiftOptions_["vbf_pt_sublead"] = { "central" };

  // central_or_shiftOptions_["genjet_dEta_jj"] = { "central" };
  // central_or_shiftOptions_["genjet_dPhi_jj"] = { "central" };
  // central_or_shiftOptions_["genjet_m_jj"] = { "central" };
  // central_or_shiftOptions_["genjet_dR_jj"] = { "central" };

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

  central_or_shiftOptions_["H1H2_centrality"] = { "central" };
  central_or_shiftOptions_["vbfj1_cosphi"] = { "central" };
  central_or_shiftOptions_["vbfj2_cosphi"] = { "central" };
}

// EvtHistManager_hh_2lss_vbf::EvtHistManager_hh_2lss_vbf(const edm::ParameterSet & cfg)
//   : HistManagerBase(cfg)
// {
//   central_or_shiftOptions_["numElectrons"] = { "central" };
//   central_or_shiftOptions_["numMuons"] = { "central" };
//   central_or_shiftOptions_["numJets"] = { "central" };
//   central_or_shiftOptions_["numJetsPtGt40"] = { "central" };
//   central_or_shiftOptions_["dihiggsVisMass"] = { "*" };
//   central_or_shiftOptions_["dihiggsMass_wMet"] = { "central" };
//   central_or_shiftOptions_["jetMass"] = { "central" };
//   central_or_shiftOptions_["leptonPairMass"] = { "central" };
//   central_or_shiftOptions_["electronPairMass"] = { "central" };
//   central_or_shiftOptions_["muonPairMass"] = { "central" };
//   central_or_shiftOptions_["leptonPairCharge"] = { "central" };
//   central_or_shiftOptions_["met"] = { "central" };
//   central_or_shiftOptions_["mht"] = { "central" };
//   central_or_shiftOptions_["met_LD"] = { "central" };
//   central_or_shiftOptions_["HT"] = { "central" };
//   central_or_shiftOptions_["STMET"] = { "central" };
//   central_or_shiftOptions_["EventCounter"] = { "*" };

//   central_or_shiftOptions_["lep1_conePt"] = { "central" };
//   central_or_shiftOptions_["mindr_lep1_jet"] = { "central" };
//   central_or_shiftOptions_["mT_lep1"] = { "central" };
//   central_or_shiftOptions_["dPhi_lep1_met"] = { "central" };
//   central_or_shiftOptions_["dPhi_lep1_mht"] = { "central" };

//   central_or_shiftOptions_["lep2_conePt"] = { "central" };
//   central_or_shiftOptions_["mindr_lep2_jet"] = { "central" };
//   central_or_shiftOptions_["mT_lep2"] = { "central" };
//   central_or_shiftOptions_["dPhi_lep2_met"] = { "central" };
//   central_or_shiftOptions_["dPhi_lep2_mht"] = { "central" };

//   central_or_shiftOptions_["dR_ll"] = { "central" };
//   central_or_shiftOptions_["max_lep_eta"] = { "central" };
// }


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


  histogram_EventCounter_ = book1D(
      dir, "EventCounter", "EventCounter", 1, -0.5, +0.5);
  histogram_mindR_vbfjet_lep1_   = book1D(dir, "mindR_vbfjet_lep1",   "mindR_vbfjet_lep1",   100, 0,   7);
  histogram_mindR_vbfjet_lep2_   = book1D(dir, "mindR_vbfjet_lep2",   "mindR_vbfjet_lep2",   100, 0,   7);
  histogram_maxJetEta_vbf_      = book1D(dir, "maxJetEta_vbf",      "maxJetEta_vbf",      100, 0, 5);
  histogram_minJetEta_vbf_      = book1D(dir, "minJetEta_vbf",      "minJetEta_vbf",      100, 0, 5);

  // histogram_lhe_dEta_jj_ = book1D(
  //     dir, "lhe_dEta_jj", "lhe_dEta_jj", 50, -10.,10);
  // histogram_lhe_dPhi_jj_ = book1D(
  //     dir, "lhe_dPhi_jj", "lhe_dPhi_jj", 50, -10.,10);
  // histogram_lhe_m_jj_ = book1D(
  //     dir, "lhe_m_jj", "lhe_m_jj", 250, 0., 5000);
  // histogram_lhe_dR_jj_ = book1D(
  //     dir, "lhe_dR_jj", "lhe_dR_jj", 100, 0., 10);

  // histogram_matched_dEta_jj_ = book1D(
  //     dir, "matched_dEta_jj", "matched_dEta_jj", 50, -10.,10);
  // histogram_matched_dPhi_jj_ = book1D(
  //     dir, "matched_dPhi_jj", "matched_dPhi_jj", 50, -10.,10);
  // histogram_matched_m_jj_ = book1D(
  //     dir, "matched_m_jj", "matched_m_jj", 250, 0., 5000);
  // histogram_matched_dR_jj_ = book1D(
  //     dir, "matched_dR_jj", "matched_dR_jj", 100, 0., 10);
  histogram_vbf_dEta_jj_ = book1D(
      dir, "vbf_dEta_jj", "vbf_dEta_jj", 50, -10.,10);
  histogram_vbf_dPhi_jj_ = book1D(
      dir, "vbf_dPhi_jj", "vbf_dPhi_jj", 50, -10.,10);
  histogram_vbf_m_jj_ = book1D(
      dir, "vbf_m_jj", "vbf_m_jj", 250, 0., 5000);
  histogram_vbf_dR_jj_ = book1D(
      dir, "vbf_dR_jj", "vbf_dR_jj", 100, 0., 10);


  // histogram_lhe_pt_lead_ = book1D(
  //     dir, "lhe_pt_lead", "lhe_pt_lead", 100, 0., 1000);
  // histogram_lhe_pt_sublead_ = book1D(
  //     dir, "lhe_pt_sublead", "lhe_pt_sublead", 100, 0., 1000);
  // histogram_matched_pt_lead_ = book1D(
  //     dir, "matched_pt_lead", "matched_pt_lead", 100, 0., 1000);
  // histogram_matched_pt_sublead_ = book1D(
  //     dir, "matched_pt_sublead", "matched_pt_sublead", 100, 0., 1000);
  histogram_vbf_pt_lead_ = book1D(
      dir, "vbf_pt_lead", "vbf_pt_lead", 100, 0., 1000);
  histogram_vbf_pt_sublead_ = book1D(
      dir, "vbf_pt_sublead", "vbf_pt_sublead", 100, 0., 1000);


  // histogram_genjet_dEta_jj_ = book1D(
  //     dir, "genjet_dEta_jj", "genjet_dEta_jj", 50, -10.,10);
  // histogram_genjet_dPhi_jj_ = book1D(
  //     dir, "genjet_dPhi_jj", "genjet_dPhi_jj", 50, -10.,10);
  // histogram_genjet_m_jj_ = book1D(
  //     dir, "genjet_m_jj", "genjet_m_jj", 250, 0., 5000);
  // histogram_genjet_dR_jj_ = book1D(
  //     dir, "genjet_dR_jj", "genjet_dR_jj", 100, 0., 10);

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

  histogram_H1H2_centrality_ = book1D(
      dir, "H1H2_centrality", "H1H2_centrality", 30, 0., 1.5);
  histogram_vbfj1_cosphi_ = book1D(
      dir, "vbfj1_cosphi", "vbfj1_cosphi", 30, 0., 1.2);
  histogram_vbfj2_cosphi_ = book1D(
      dir, "vbfj2_cosphi", "vbfj2_cosphi", 30, 0., 1.2);
}

// void
// EvtHistManager_hh_2lss_vbf::bookHistograms(TFileDirectory & dir)
// {
//   histogram_numElectrons_     = book1D(dir, "numElectrons",     "numElectrons",       5, -0.5,  +4.5);
//   histogram_numMuons_         = book1D(dir, "numMuons",         "numMuons",           5, -0.5,  +4.5);
//   histogram_numJets_          = book1D(dir, "numJets",          "numJets",           20, -0.5, +19.5);
//   histogram_numJetsPtGt40_    = book1D(dir, "numJetsPtGt40",    "numJetsPtGt40",     20, -0.5, +19.5);
//   histogram_dihiggsVisMass_   = book1D(dir, "dihiggsVisMass",   "dihiggsVisMass",   150,  0., 1500.);
//   histogram_dihiggsMass_wMet_ = book1D(dir, "dihiggsMass_wMet", "dihiggsMass_wMet", 150,  0., 1500.);
//   histogram_jetMass_          = book1D(dir, "jetMass",          "jetMass",          150,  0., 1500.);
//   histogram_leptonPairMass_   = book1D(dir, "leptonPairMass",   "leptonPairMass",   100,  0.,  200.);
//   histogram_electronPairMass_ = book1D(dir, "electronPairMass", "electronPairMass", 100,  0.,  200.);
//   histogram_muonPairMass_     = book1D(dir, "muonPairMass",     "muonPairMass",     100,  0.,  200.);
//   histogram_leptonPairCharge_ = book1D(dir, "leptonPairCharge", "leptonPairCharge",   5, -2.5,  +2.5);
//   histogram_met_              = book1D(dir, "met",              "met",               200, 0,500);
//   histogram_mht_              = book1D(dir, "mht",              "mht",               200, 0,500);
//   histogram_met_LD_           = book1D(dir, "met_LD",           "met_LD",            200, 0,500);
//   histogram_HT_               = book1D(dir, "HT",               "HT",               150,  0., 1500.);
//   histogram_STMET_            = book1D(dir, "STMET",            "STMET",            150,  0., 1500.);
//   histogram_EventCounter_     = book1D(dir, "EventCounter",     "EventCounter",       1, -0.5,  +0.5);

//   histogram_lep1_conePt_      = book1D(dir, "lep1_conePt",      "lep1_conePt",      150, 0, 300);
//   histogram_mindr_lep1_jet_   = book1D(dir, "mindr_lep1_jet",   "mindr_lep1_jet",   100, 0,   7);
//   histogram_mT_lep1_          = book1D(dir, "mT_lep1",          "mT_lep1",          200, 0, 500);
//   histogram_dPhi_lep1_met_    = book1D(dir, "dPhi_lep1_met",    "dPhi_lep1_met",     36, 0., TMath::Pi());
//   histogram_dPhi_lep1_mht_    = book1D(dir, "dPhi_lep1_mht",    "dPhi_lep1_mht",     36, 0., TMath::Pi());

//   histogram_lep2_conePt_      = book1D(dir, "lep2_conePt",      "lep2_conePt",      150, 0, 300);
//   histogram_mindr_lep2_jet_   = book1D(dir, "mindr_lep2_jet",   "mindr_lep2_jet",   100, 0,   7);
//   histogram_mT_lep2_          = book1D(dir, "mT_lep2",          "mT_lep2",          200, 0, 500);
//   histogram_dPhi_lep2_met_    = book1D(dir, "dPhi_lep2_met",    "dPhi_lep2_met",     36, 0., TMath::Pi());
//   histogram_dPhi_lep2_mht_    = book1D(dir, "dPhi_lep2_mht",    "dPhi_lep2_mht",     36, 0., TMath::Pi());

//   histogram_dR_ll_            = book1D(dir, "dR_ll",            "dR_ll",            100, 0,   7);
//   histogram_max_lep_eta_      = book1D(dir, "max_lep_eta",      "max_lep_eta",      100, 0, 2.5);
 
// }





void EvtHistManager_hh_2lss_vbf::fillHistograms(
    int numElectrons, int numMuons, int numJets, int numJetsPtGt40,
    double dihiggsVisMass, double dihiggsMass_wMet,

    double evtWeight,
    double mindR_vbfjet_lep1, double mindR_vbfjet_lep2,
    double maxJetEta_vbf, double minJetEta_vbf,
    // double lhe_dEta_jj, double lhe_dPhi_jj, double lhe_m_jj, double lhe_dR_jj,
    // double matched_dEta_jj, double matched_dPhi_jj, double matched_m_jj, double matched_dR_jj,
    double vbf_dEta_jj, double vbf_dPhi_jj, double vbf_m_jj, double vbf_dR_jj,
    // double lhe_pt_lead, double lhe_pt_sublead, double matched_pt_lead, double matched_pt_sublead, 
    double vbf_pt_lead, double vbf_pt_sublead,
    // double genjet_dEta_jj, double genjet_dPhi_jj, double genjet_m_jj, double genjet_dR_jj,
    double mass_jj_W, double mass_jj_W2, double sum_mass_W,
    double sum_m_lj, double pT_sum, double m_ll, bool isVBF,
    double maxJetPt_vbf, double minJetPt_vbf, double mindR_vbfJet_W1, double maxdR_vbfJet_W1, double mindR_vbfjet_lep, double maxdR_vbfjet_lep,
    double dR_h1h2, double pT_h1, double pT_h2, double dR_h1_j1, double dR_h1_j2, double dR_h2_j1, double dR_h2_j2, double mass_h1, double mass_h2,
    double H1H2_centrality, double vbfj1_cosphi, double vbfj2_cosphi
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

  fillWithOverFlow(histogram_EventCounter_, 0., evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mindR_vbfjet_lep1_,   mindR_vbfjet_lep1,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mindR_vbfjet_lep2_,   mindR_vbfjet_lep2,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_maxJetEta_vbf_,      maxJetEta_vbf,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_minJetEta_vbf_,      minJetEta_vbf,      evtWeight, evtWeightErr);

  // if(lhe_dEta_jj>-999){
  // fillWithOverFlow(histogram_lhe_dEta_jj_,      lhe_dEta_jj,      evtWeight, evtWeightErr);
  // }
  // if(lhe_dPhi_jj>-999){
  // fillWithOverFlow(histogram_lhe_dPhi_jj_,      lhe_dPhi_jj,      evtWeight, evtWeightErr);
  // }
  // if(lhe_m_jj>0){
  // fillWithOverFlow(histogram_lhe_m_jj_,         lhe_m_jj,         evtWeight, evtWeightErr);
  // }
  // if(lhe_dR_jj>0){
  // fillWithOverFlow(histogram_lhe_dR_jj_,        lhe_dR_jj,        evtWeight, evtWeightErr);
  // }

  // if(matched_dEta_jj>-999){
  //     fillWithOverFlow(histogram_matched_dEta_jj_,     matched_dEta_jj,     evtWeight, evtWeightErr);
  // }
  // if(matched_dPhi_jj>-999){
  //     fillWithOverFlow(histogram_matched_dPhi_jj_,     matched_dPhi_jj,     evtWeight, evtWeightErr);
  // }
  // if(matched_m_jj>0){
  //     fillWithOverFlow(histogram_matched_m_jj_,        matched_m_jj,        evtWeight, evtWeightErr);
  // }
  // if(matched_dR_jj>0){
  //     fillWithOverFlow(histogram_matched_dR_jj_,       matched_dR_jj,       evtWeight, evtWeightErr);
  // }

  if(vbf_dEta_jj>-999){
      fillWithOverFlow(histogram_vbf_dEta_jj_,      vbf_dEta_jj,      evtWeight, evtWeightErr);
  }
  if(vbf_dPhi_jj>-999){
      fillWithOverFlow(histogram_vbf_dPhi_jj_,      vbf_dPhi_jj,      evtWeight, evtWeightErr);
  }
  if(vbf_m_jj>0){
      fillWithOverFlow(histogram_vbf_m_jj_,         vbf_m_jj,         evtWeight, evtWeightErr);
  }
  if(vbf_dR_jj>0){
      fillWithOverFlow(histogram_vbf_dR_jj_,        vbf_dR_jj,        evtWeight, evtWeightErr);
  }

  // if(lhe_pt_lead>0){
  //     fillWithOverFlow(histogram_lhe_pt_lead_,        lhe_pt_lead,        evtWeight, evtWeightErr);
  // }
  // if(lhe_pt_sublead>0){
  //     fillWithOverFlow(histogram_lhe_pt_sublead_,        lhe_pt_sublead,        evtWeight, evtWeightErr);
  // }
  // if(matched_pt_lead>0){
  //     fillWithOverFlow(histogram_matched_pt_lead_,        matched_pt_lead,        evtWeight, evtWeightErr);
  // }
  // if(matched_pt_sublead>0){
  //     fillWithOverFlow(histogram_matched_pt_sublead_,        matched_pt_sublead,        evtWeight, evtWeightErr);
  // }
  if(vbf_pt_lead>0){
      fillWithOverFlow(histogram_vbf_pt_lead_,        vbf_pt_lead,        evtWeight, evtWeightErr);
  }
  if(vbf_pt_sublead>0){
      fillWithOverFlow(histogram_vbf_pt_sublead_,        vbf_pt_sublead,        evtWeight, evtWeightErr);
  }

  // if(genjet_dEta_jj>-999){
  //     fillWithOverFlow(histogram_genjet_dEta_jj_,     genjet_dEta_jj,     evtWeight, evtWeightErr);
  // }
  // if(genjet_dPhi_jj>-999){
  //     fillWithOverFlow(histogram_genjet_dPhi_jj_,     genjet_dPhi_jj,     evtWeight, evtWeightErr);
  // }
  // if(genjet_m_jj>0){
  //     fillWithOverFlow(histogram_genjet_m_jj_,        genjet_m_jj,        evtWeight, evtWeightErr);
  // }
  // if(genjet_dR_jj>0){
  //     fillWithOverFlow(histogram_genjet_dR_jj_,       genjet_dR_jj,       evtWeight, evtWeightErr);
  // }

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
  if(mass_h1<9999){
      fillWithOverFlow(histogram_mass_h1_,       mass_h1,       evtWeight, evtWeightErr);
  }
  if(mass_h2<9999){
      fillWithOverFlow(histogram_mass_h2_,       mass_h2,       evtWeight, evtWeightErr);
  }
  if(H1H2_centrality>0){
    fillWithOverFlow(histogram_H1H2_centrality_,      H1H2_centrality,      evtWeight, evtWeightErr);
  }
  fillWithOverFlow(histogram_vbfj1_cosphi_,      vbfj1_cosphi,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_vbfj2_cosphi_,      vbfj2_cosphi,      evtWeight, evtWeightErr);

}



// void
// EvtHistManager_hh_2lss_vbf::fillHistograms(int numElectrons,
//                int numMuons,
//                int numJets,
//                int numJetsPtGt40,
//                double dihiggsVisMass,
//                double dihiggsMass_wMet,
//                double jetMass,
//                double leptonPairMass,
//                double electronPairMass,
//                double muonPairMass,
//                double leptonPairCharge,
//                double met,
//                double mht,
//                double met_LD,
//                double HT,
//                double STMET,
//                //
//                double lep1_conePt,
//                double mindr_lep1_jet,
//                double mT_lep1,
//                                        double dPhi_lep1_met,
//                                        double dPhi_lep1_mht,
//                //
//                double lep2_conePt,
//                double mindr_lep2_jet,
//                double mT_lep2,
//                                        double dPhi_lep2_met,
//                                        double dPhi_lep2_mht,
//                //
//                double dR_ll,
//                double max_lep_eta,
//                //    
//                double evtWeight)
// {
//   const double evtWeightErr = 0.;
//   fillWithOverFlow(histogram_numElectrons_,     numElectrons,     evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_numMuons_,         numMuons,         evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_numJets_,          numJets,          evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_numJetsPtGt40_,    numJetsPtGt40,    evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_dihiggsVisMass_,   dihiggsVisMass,   evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_dihiggsMass_wMet_, dihiggsMass_wMet, evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_jetMass_,          jetMass,          evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_leptonPairMass_,   leptonPairMass,   evtWeight, evtWeightErr);
//   if ( electronPairMass > 0. ) {
//     fillWithOverFlow(histogram_electronPairMass_, electronPairMass, evtWeight, evtWeightErr);
//   }
//   if ( muonPairMass > 0. ) {
//     fillWithOverFlow(histogram_muonPairMass_,     muonPairMass,     evtWeight, evtWeightErr);
//   }
//   fillWithOverFlow(histogram_leptonPairCharge_, leptonPairCharge, evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_met_,              met,              evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_mht_,              mht,              evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_met_LD_,           met_LD,           evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_HT_,               HT,               evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_STMET_,            STMET,            evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_EventCounter_,     0.,               evtWeight, evtWeightErr);
//   //
//   fillWithOverFlow(histogram_lep1_conePt_,      lep1_conePt,      evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_mindr_lep1_jet_,   mindr_lep1_jet,   evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_mT_lep1_,          mT_lep1,          evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_dPhi_lep1_met_,    dPhi_lep1_met,    evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_dPhi_lep1_mht_,    dPhi_lep1_mht,    evtWeight, evtWeightErr);
//   //
//   fillWithOverFlow(histogram_lep2_conePt_,      lep2_conePt,      evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_mindr_lep2_jet_,   mindr_lep2_jet,   evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_mT_lep2_,          mT_lep2,          evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_dPhi_lep2_met_,    dPhi_lep2_met,    evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_dPhi_lep2_mht_,    dPhi_lep2_mht,    evtWeight, evtWeightErr);
//   //
//   fillWithOverFlow(histogram_dR_ll_,            dR_ll,            evtWeight, evtWeightErr);
//   fillWithOverFlow(histogram_max_lep_eta_,      max_lep_eta,      evtWeight, evtWeightErr);
// }

