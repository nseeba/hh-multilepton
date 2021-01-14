#ifndef hhAnalysis_multilepton_EvtHistManager_hh_3l_1tau_h
#define hhAnalysis_multilepton_EvtHistManager_hh_3l_1tau_h

/** \class EvtHistManager_hh_3l_1tau
 *
 * Book and fill histograms for event-level quantities in the 1l+3tau_h category 
 * of the HH->tttt, WWtt, and WWWW analysis 
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult


#include <vector>
#include <map>

using namespace std; 

class EvtHistManager_hh_3l_1tau
  : public HistManagerBase
{
public:
  EvtHistManager_hh_3l_1tau(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_3l_1tau() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
    fillHistograms(int numElectrons,
		   int numMuons,
		   int numHadTaus,
		   int numJets,
		   double MET,
		   int nSFOS,
		   double HT,
		   double STMET,
		   double MET_LD,
		   double dihiggsVisMass,
		   double dihiggsMass,
		   double dR_smartpair_ltau,
		   double m_smartpair_ltau,
		   double dR_smartpair_ll,
		   double m_smartpair_ll,
		   double mllOS_closestToZ,
		   double leadMuonPt,
		   double leadMuonEta,
		   double leadMuonPhi,
		   double subleadMuonPt,
		   double subleadMuonEta,
		   double subleadMuonPhi,
		   double leadElectronPt,
		   double leadElectronEta,
		   double leadElectronPhi,
		   double subleadElectronPt,
		   double subleadElectronEta,
		   double subleadElectronPhi,
		   double thirdLepPt,
		   double thirdLepEta,
		   double thirdLepPhi,
                   unsigned int evt_number,
		   double evtWeight);

  const TH1 *
  getHistogram_EventCounter() const;

 private:
  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numHadTaus_;
  TH1 * histogram_numJets_;
  TH1 * histogram_MET_;
  TH1 * histogram_nSFOS_;
  TH1 * histogram_HT_;
  TH1 * histogram_STMET_;
  TH1 * histogram_MET_LD_;
  TH1 * histogram_dihiggsVisMass_;
  TH1 * histogram_dihiggsMass_;
  TH1 * histogram_dR_smartpair_ltau_;
  TH1 * histogram_m_smartpair_ltau_;
  TH1 * histogram_dR_smartpair_ll_;
  TH1 * histogram_m_smartpair_ll_;
  TH1 * histogram_mllOS_closestToZ_;
  TH1 * histogram_leadMuonPt_;
  TH1 * histogram_leadMuonEta_;
  TH1 * histogram_leadMuonPhi_;
  TH1 * histogram_subleadMuonPt_;
  TH1 * histogram_subleadMuonEta_;
  TH1 * histogram_subleadMuonPhi_;
  TH1 * histogram_leadElectronPt_;
  TH1 * histogram_leadElectronEta_;
  TH1 * histogram_leadElectronPhi_;
  TH1 * histogram_subleadElectronPt_;
  TH1 * histogram_subleadElectronEta_;
  TH1 * histogram_subleadElectronPhi_;
  TH1 * histogram_thirdLepPt_;
  TH1 * histogram_thirdLepEta_;
  TH1 * histogram_thirdLepPhi_;
  TH1 * histogram_EventCounter_;
  TH1 * histogram_EventNumber_;
};

#endif
