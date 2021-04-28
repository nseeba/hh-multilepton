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

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h"      // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h"            // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceCouplings.h" // HHWeightInterfaceCouplings
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceLO.h"  // HHWeightInterfaceLO
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceNLO.h" // HHWeightInterfaceNLO
#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h"       // AnalysisConfig_hh
#include "tthAnalysis/HiggsToTauTau/interface/LHEParticle.h"          // LHEParticle

class HHGenKinematicsHistManager
  : public HistManagerBase
{
 public:
  HHGenKinematicsHistManager(const edm::ParameterSet & cfg,
                             const AnalysisConfig_hh & analysisConfig, 
                             const EventInfo & eventInfo,
			     const HHWeightInterfaceCouplings * hhWeight_couplings,
                             const HHWeightInterfaceLO * HHWeightLO_calc,
                             const HHWeightInterfaceNLO * HHWeightNLO_calc);
  ~HHGenKinematicsHistManager() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(double evtWeight);

 private:
  const AnalysisConfig_hh & analysisConfig_;
  const EventInfo & eventInfo_;
  const HHWeightInterfaceCouplings * hhWeight_couplings_;
  const HHWeightInterfaceLO * HHWeightLO_calc_;
  bool apply_HH_rwgt_lo_;
  const HHWeightInterfaceNLO * HHWeightNLO_calc_;
  bool apply_HH_rwgt_nlo_;
  std::vector<std::string> HHWeightNames_;
  std::vector<std::string> HHBMNames_;

  
  TH1 ** histograms_gen_mHH_;
  TH1 ** histograms_gen_absCosThetaStar_;
};

#endif
