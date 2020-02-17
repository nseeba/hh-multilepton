#ifndef hhAnalysis_multilepton_RecoJetCollectionSelectorAK8_hh_WjPlusLepton_h
#define hhAnalysis_multilepton_RecoJetCollectionSelectorAK8_hh_WjPlusLepton_h

#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionSelector.h" // ParticleCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetAK8.h" // RecoJetAK8

#include <string> // std::string

class RecoLepton;

class RecoJetSelectorAK8_hh_WjPlusLepton
{
public:
  explicit RecoJetSelectorAK8_hh_WjPlusLepton(int era,
                                              int index = -1,
                                              bool debug = false);
  ~RecoJetSelectorAK8_hh_WjPlusLepton() {}

  /**
   * @brief Set cut thresholds
   */
  void set_min_pt(double min_pt);
  void set_max_absEta(double max_absEta);
  void set_max_dR_lepton(double max_dR_lepton);
  void set_min_subJet_pt(double min_pt);
  void set_max_subJet_absEta(double max_absEta);
  void set_min_jetId(int min_jetId);

  void set_lepton(const RecoLepton * lepton) const;
  void set_leptons(const std::vector<const RecoLepton *> & leptons) const;

  /**
   * @brief Get cut thresholds
   */
  double get_min_pt() const;
  double get_max_absEta() const;
  double get_max_dR_lepton() const;
  double get_min_subJet_pt() const;
  double get_max_subJet_absEta() const;
  int get_min_jetId() const;

  /**
   * @brief Check if jet given as function argument passes pT and eta cuts (pT > 25 GeV and |eta| < 2.4, cf. Section 3.1 of AN-2015/321)
   * @return True if jet passes selection; false otherwise
   */
  bool
  operator()(const RecoJetAK8 & jet) const;

  bool
  operator()(const RecoJetAK8 & jet,
             std::string & returnType) const;
 
protected:
  Double_t min_pt_;                   ///< lower cut threshold on pT of "fat" (AK8) jet
  Double_t max_absEta_;               ///< upper cut threshold on absolute value of eta of "fat" (AK8) jet
  Int_t min_jetId_;                   ///< lower cut threshold on jet ID value 
  Double_t max_dR_lepton_;            ///< upper cut threshold on distance between "fat" (AK8) jet and electron or muon
  Double_t min_subJet_pt_;            ///< lower cut threshold on pT on the subjet not corresponding to the lepton
  Double_t max_subJet_absEta_;        ///< upper cut threshold on absolute value of eta of the subjet not corresponding to the lepton

  mutable std::vector<const RecoLepton *> leptons_; ///< pointer to electron or muon produced in H->WW*->jj lnu decay
  
  bool debug_;
};

typedef ParticleCollectionSelector<RecoJetAK8, RecoJetSelectorAK8_hh_WjPlusLepton> RecoJetCollectionSelectorAK8_hh_WjPlusLepton;

#endif // hhAnalysis_bbww_RecoJetCollectionSelectorAK8_hh_WjPlusLepton_h
