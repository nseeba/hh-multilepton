#ifndef hhAnalysis_multilepton_RecoElectronCollectionSelectorFakeable_hh_multilepton_h
#define hhAnalysis_multilepton_RecoElectronCollectionSelectorFakeable_hh_multilepton_h

#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionSelector.h" // ParticleCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectron.h" // RecoElectron
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h"       // Era

class RecoElectronSelectorFakeable_hh_multilepton
{
public:
  explicit
  RecoElectronSelectorFakeable_hh_multilepton(Era era,
                            int index = -1,
                            bool debug = false,
                            bool set_selection_flags = true);
  ~RecoElectronSelectorFakeable_hh_multilepton() {}

  /**
   * @brief Set cut thresholds
   */
  
  // enable/disable cuts on electron ID variables to mimic electron ID cuts applied by single electron trigger 
  void enable_offline_e_trigger_cuts();
  void disable_offline_e_trigger_cuts();

  
  void set_min_pt(double min_pt);
  void set_min_cone_pt(double min_cone_pt);
  void set_max_absEta(double max_absEta);

  /**
   * @brief Get cut thresholds
   */
  double get_min_pt() const;
  double get_min_cone_pt() const;
  double get_max_absEta() const;

  void set_selection_flags(bool selection_flags);
  
  /**
   * @brief Check if electron given as function argument passes "loose" electron selection, defined in Table 13 of AN-2015/321
   * @return True if electron passes selection; false otherwise
   */
  bool operator()(const RecoElectron & electron) const;

protected:
  const Era era_;
  bool debug_;
  bool set_selection_flags_;
  bool apply_offline_e_trigger_cuts_;

  Double_t min_pt_;                         ///< lower cut threshold on reco::GSFElectron pT
  Double_t min_cone_pt_;                    ///< lower cut threshold on cone pT
  Double_t max_absEta_;                     ///< upper cut threshold on absolute value of eta
  const Double_t max_dxy_;                  ///< upper cut threshold on d_{xy}, distance in the transverse plane w.r.t PV
  const Double_t max_dz_;                   ///< upper cut threshold on d_{z}, distance on the z axis w.r.t PV
  const Double_t max_relIso_;               ///< upper cut threshold on relative isolation
  const Double_t max_sip3d_;                ///< upper cut threshold on significance of IP
//-------------------------------------------------------------------------------
  const bool apply_tightCharge_;            ///< apply (True) or do not apply (False) tight charge cut
  const bool apply_conversionVeto_;         ///< apply (True) or do not apply (False) conversion veto
  const Int_t max_nLostHits_;               ///< upper cut threshold on lost hits in the innermost layer of the tracker (electrons with lost_hits equal to cut threshold pass)
//-------------------------------------------------------------------------------
};

class RecoElectronCollectionSelectorFakeable_hh_multilepton
  : public ParticleCollectionSelector<RecoElectron, RecoElectronSelectorFakeable_hh_multilepton>
{
public:
  explicit
  RecoElectronCollectionSelectorFakeable_hh_multilepton(Era era,
                                         int index = -1,
                                         bool debug = false,
                                         bool set_selection_flags = true);
  ~RecoElectronCollectionSelectorFakeable_hh_multilepton() {}

  void enable_offline_e_trigger_cuts();
  void disable_offline_e_trigger_cuts();
};

#endif // hhAnalysis_multilepton_RecoElectronCollectionSelectorFakeable_hh_multilepton_h
