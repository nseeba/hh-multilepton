#ifndef hhAnalysis_multilepton_HHGenKinematicsHistManager_h
#define hhAnalysis_multilepton_HHGenKinematicsHistManager_h

/** \class HHGenKinematicsHistManager
 *
 * Book and fill histograms of mHH and cos(theta*)
 * that are used to compute weights for reweighting the kinematics of HH non-resonant signal MC samples
 *
 * \author Christian Veelken, Tallin
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h"    // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h"          // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterface2.h" // HHWeightInterface2
#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h"     // AnalysisConfig_hh
#include "tthAnalysis/HiggsToTauTau/interface/LHEParticle.h"        // LHEParticle

class HHGenKinematicsHistManager
  : public HistManagerBase
{
 public:
  HHGenKinematicsHistManager(const edm::ParameterSet & cfg,
                             const AnalysisConfig_hh & analysisConfig, 
                             const EventInfo & eventInfo, 
                             const HHWeightInterface2 * HHWeight_calc);
  ~HHGenKinematicsHistManager() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(const std::vector<LHEParticle> & lheParticles, double evtWeight);

 private:
  const AnalysisConfig_hh & analysisConfig_;
  const EventInfo & eventInfo_;
  const HHWeightInterface2 * HHWeight_calc_;
  bool apply_HH_rwgt_;

  TH1 * histogram_gen_mHH_;
  TH1 * histogram_gen_absCosThetaStar_;
};

#endif
