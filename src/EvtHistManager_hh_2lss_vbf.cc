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
  central_or_shiftOptions_["EventCounter"] = {"*"};
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
      dir, "dihiggsVisMass", "dihiggsVisMass", 150, 0., 1500.);
  histogram_dihiggsMass_wMet_ = book1D(
      dir, "dihiggsMass_wMet", "dihiggsMass_wMet", 150, 0., 1500.);
  histogram_vbf_m_jj_ = book1D(
      dir, "vbf_m_jj", "vbf_m_jj", 40, 0., 4000.);
  histogram_vbf_dEta_jj_ = book1D(
      dir, "vbf_dEta_jj", "vbf_dEta_jj", 50, 0.,5.);
  histogram_EventCounter_ = book1D(
      dir, "EventCounter", "EventCounter", 1, -0.5, +0.5);
}

void EvtHistManager_hh_2lss_vbf::fillHistograms(
    int numElectrons, int numMuons, int numJets, int numJetsPtGt40,
    double dihiggsVisMass, double dihiggsMass_wMet, double vbf_m_jj,
    double vbf_dEta_jj, double evtWeight)

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
  fillWithOverFlow(histogram_EventCounter_, 0., evtWeight, evtWeightErr);
}
