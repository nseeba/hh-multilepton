// Import stuff TEST_xps_13
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector
#include "DataFormats/Math/interface/deltaR.h"        // deltaR
#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/Utilities/interface/Exception.h"       // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService

#if __has_include(<FWCore/ParameterSetReader/interface/ParameterSetReader.h>)
#include <FWCore/ParameterSetReader/interface/ParameterSetReader.h> // edm::readPSetsFrom()
#else
#include <FWCore/PythonParameterSet/interface/MakeParameterSets.h> // edm::readPSetsFrom()
#endif


#include <TBenchmark.h>     // TBenchmark
#include <TError.h>         // gErrorAbortLevel, kError
#include <TLorentzVector.h> // TLorentzVector
#include <TROOT.h>          // TROOT
#include <TString.h>        // TString, Form
#include <TVector3.h>

#include "tthAnalysis/HiggsToTauTau/interface/BtagSFRatioFacility.h" // BtagSFRatioFacility
#include "tthAnalysis/HiggsToTauTau/interface/ChargeMisIdRate.h" // ChargeMisIdRate
#include "tthAnalysis/HiggsToTauTau/interface/CutFlowTableHistManager.h" // CutFlowTableHistManager
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2016.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2017.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2018.h"
#include "tthAnalysis/HiggsToTauTau/interface/ElectronHistManager.h" // ElectronHistManager
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager
#include "tthAnalysis/HiggsToTauTau/interface/EvtYieldHistManager.h" // EvtYieldHistManager
#include "tthAnalysis/HiggsToTauTau/interface/GenEvtHistManager.h" // GenEvtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h"         // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTauReader.h" // GenHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h"          // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h"    // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h"       // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenMatchInterface.h" // GenMatchInterface
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEParticleReader.h" //.LHEParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/GenPhotonFilter.h" // GenPhotonFilter
#include "tthAnalysis/HiggsToTauTau/interface/GenPhotonReader.h" // GenPhotonReader
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceCouplings.h" // HHWeightInterfaceCouplings
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceLO.h" // HHWeightInterfaceLO
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceNLO.h" // HHWeightInterfaceNLO
#include "tthAnalysis/HiggsToTauTau/interface/HadTauHistManager.h" // HadTauHistManager
#include "tthAnalysis/HiggsToTauTau/interface/JetHistManager.h" // JetHistManager
#include "tthAnalysis/HiggsToTauTau/interface/JetHistManagerAK8.h" // JetHistManagerAK8
#include "tthAnalysis/HiggsToTauTau/interface/JetToTauFakeRateInterface.h" // JetToTauFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/L1PreFiringWeightReader.h" // L1PreFiringWeightReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoHistManager.h" // LHEInfoHistManager
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoReader.h" // LHEInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/LeptonFakeRateInterface.h" // LeptonFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterHistManager.h" // MEtFilterHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterReader.h" // MEtFilterReader
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterSelector.h" // MEtFilterSelector
#include "tthAnalysis/HiggsToTauTau/interface/MEtHistManager.h" // MEtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MVAInputVarCorrelationHistManager.h" // MVAInputVarCorrelationHistManager, getKeys()
#include "tthAnalysis/HiggsToTauTau/interface/MuonHistManager.h" // MuonHistManager
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/ObjectMultiplicity.h" // ObjectMultiplicity
#include "tthAnalysis/HiggsToTauTau/interface/ObjectMultiplicityReader.h" // ObjectMultiplicityReader
#include "tthAnalysis/HiggsToTauTau/interface/PSWeightReader.h" // PSWeightReader
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionCleaner.h" // RecoElectronCollectionCleaner, RecoMuonCollectionCleaner, RecoHadTauCollectionCleaner, RecoJetCollectionCleaner
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionGenMatcher.h" // RecoElectronCollectionGenMatcher, RecoMuonCollectionGenMatcher, RecoHadTauCollectionGenMatcher, RecoJetCollectionGenMatcher
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorFakeable.h" // RecoElectronCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorLoose.h" // RecoElectronCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorTight.h" // RecoElectronCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h" // RecoHadTau
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorFakeable.h" // RecoHadTauCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorTight.h" // RecoHadTauCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauReader.h" // RecoHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h"          // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelector.h" // RecoJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorBtag.h" // RecoJetCollectionSelectorBtagLoose, RecoJetCollectionSelectorBtagMedium
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h"       // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h"          // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorFakeable.h" // RecoMuonCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorLoose.h" // RecoMuonCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorTight.h" // RecoMuonCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertex.h"     // RecoVertex
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertexReader.h" // RecoVertexReader
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventRejector.h" // RunLumiEventRejector
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/WeightHistManager.h" // WeightHistManager
#include "tthAnalysis/HiggsToTauTau/interface/XGBInterface.h" // XGBInterface
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched
#include "tthAnalysis/HiggsToTauTau/interface/convert_to_ptrs.h" // convert_to_ptrs
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h"
#include "tthAnalysis/HiggsToTauTau/interface/hltFilter.h" // hltFilter()
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath, create_hltPaths, hltPaths_isTriggered, hltPaths_delete
#include "tthAnalysis/HiggsToTauTau/interface/hltPathReader.h" // hltPathReader
#include "tthAnalysis/HiggsToTauTau/interface/leptonGenMatchingAuxFunctions.h" // getLeptonGenMatch_definitions_3lepton, getLeptonGenMatch_string, getLeptonGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // getLeptonType, kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // loadTH2, get_sf_from_TH2
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_lep1_conePt, comp_lep2_conePt
//
#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h" // AnalysisConfig_hh
#include "hhAnalysis/multilepton/interface/DatacardHistManager_hh.h" // DatacardHistManager_hh
#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_2lss_vbf.h" // EvtHistManager_hh_2lss
#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH
#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h"       // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorAK8.h" // RecoJetSelectorAK8

#include "hhAnalysis/multilepton/interface/RecoElectronCollectionSelectorFakeable_hh_multilepton.h"
#include "hhAnalysis/multilepton/interface/RecoMuonCollectionSelectorFakeable_hh_multilepton.h"

#include <boost/algorithm/string/predicate.hpp> // boost::starts_with()
#include <boost/algorithm/string/replace.hpp>   // boost::replace_all_copy()

#include <assert.h> // assert
#include <cstdlib>  // EXIT_SUCCESS, EXIT_FAILURE
#include <fstream>  // std::ofstream
#include <iomanip>  // std::setprecision(), std::setw()
#include <iostream> // std::cerr, std::fixed
#include <string>   // std::string
#include <vector>   // std::vector<>

// Typedef
typedef math::PtEtaPhiMLorentzVector LV;
typedef std::vector<std::string> vstring;
typedef std::vector<double> vdouble;

enum { kFR_disabled, kFR_2lepton };

const int hadTauSelection_antiElectron = -1; // not applied
const int hadTauSelection_antiMuon = -1;     // not applied
// hasOverlap true if deltaR < 0.3 between jet and all selSubjetsAK8
bool hasOverlapJets(const RecoJet *jet,
                    std::vector<const RecoSubjetAK8 *> selSubjetsAK8) {
  bool hasOverlap = false;
  for (size_t i = 0; i < selSubjetsAK8.size(); i++) {
    if (deltaR(jet->p4(), selSubjetsAK8[i]->p4()) < 0.3)
      hasOverlap = true;
  }
  return hasOverlap;
}


double comp_maxAbsEta_jet(const std::vector<const RecoJet *> & jets_cleaned){
  double maxEta = 1.e-3;
  for(const RecoJet * jet: jets_cleaned)
  {
    const double eta = jet->eta();
    maxEta = std::max(eta, maxEta);
  }
  return maxEta;
}

double comp_minAbsEta_jet(const std::vector<const RecoJet *> & jets_cleaned){
  double minEta = 999999;
  for(const RecoJet * jet: jets_cleaned)
  {
    const double eta = jet->eta();
    minEta = std::min(eta, minEta);
  }
  return minEta;
}


// comp_mindr_jet2(const Particle::LorentzVector & lorenzvector,
//                const std::vector<const RecoJet *> & jets_cleaned)
// {
//   double dRmin = 1.e+3;
//   for(const RecoJet * jet: jets_cleaned)
//   {
//     const double dR = deltaR(lorenzvector.eta(), lorenzvector.phi(), jet->eta(), jet->phi());
//     dRmin = std::min(dR, dRmin);
//   }
//   return dRmin;
// }

// comp_max_dr_jet2(const std::vector<const RecoJet *> & jets_cleaned)
// {
//   double dRmax = 0.;
//   for(auto jet1_it = jets_cleaned.cbegin(); jet1_it != jets_cleaned.cend(); ++jet1_it)
//   {
//     const RecoJet * jet1 = *jet1_it;
//     if(jet1->pt() > 25. && std::fabs(jet1->eta()) < 2.4)
//     {
//       for(auto jet2_it = jet1_it + 1; jet2_it != jets_cleaned.cend(); ++jet2_it)
//       {
//         const RecoJet * jet2 = *jet2_it;
//         if(jet2->pt() > 25. && std::fabs(jet2->eta()) < 2.4)
//         {
//           const double dR = deltaR(jet1->eta(), jet1->phi(), jet2->eta(), jet2->phi());
//           dRmax = std::max(dRmax, dR);
//         }
//       }
//     }
//   }
// //   return dRmax;
// }
/**
 * @brief Produce datacard and control plots for 2lss category of HH analysis.
 */
int main(int argc, char *argv[]) {
  //--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

  //--- stop ROOT from keeping track of all histograms
  TH1::AddDirectory(false);

  //--- parse command-line arguments
  if (argc < 2) {
    std::cout << "Usage: " << argv[0] << " [parameters.py]" << std::endl;
    return EXIT_FAILURE;
  }

  std::cout << "<analyze_hh_2lss_vbf>:" << std::endl;

  //--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_2lss_vbf");

  //--- read python configuration parameters
  if (!edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process"))
    throw cms::Exception("analyze_hh_2lss_vbf")
        << "No ParameterSet 'process' found in configuration file = " << argv[1]
        << " !!\n";

  edm::ParameterSet cfg =
      edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze =
      cfg.getParameter<edm::ParameterSet>("analyze_hh_2lss_vbf");
  AnalysisConfig_hh analysisConfig("HH->multilepton", cfg_analyze);

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  bool isMC_ttH = analysisConfig.isMC_ttH();
  bool isMC_tH = analysisConfig.isMC_tH();
  bool isMC_EWK = analysisConfig.isMC_EWK();

  std::string histogramDir =
      cfg_analyze.getParameter<std::string>("histogramDir");
  bool isMCClosure_e = histogramDir.find("mcClosure_e") != std::string::npos;
  bool isMCClosure_m = histogramDir.find("mcClosure_m") != std::string::npos;
  std::cout << "isMCClosure: e = " << isMCClosure_e
            << ", mu = " << isMCClosure_m << std::endl;

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const Era era = get_era(era_string);

  vstring triggerNames_1e = cfg_analyze.getParameter<vstring>("triggers_1e");
  std::vector<hltPath *> triggers_1e = create_hltPaths(triggerNames_1e);
  bool use_triggers_1e = cfg_analyze.getParameter<bool>("use_triggers_1e");
  vstring triggerNames_2e = cfg_analyze.getParameter<vstring>("triggers_2e");
  std::vector<hltPath *> triggers_2e = create_hltPaths(triggerNames_2e);
  bool use_triggers_2e = cfg_analyze.getParameter<bool>("use_triggers_2e");
  vstring triggerNames_1mu = cfg_analyze.getParameter<vstring>("triggers_1mu");
  std::vector<hltPath *> triggers_1mu = create_hltPaths(triggerNames_1mu);
  bool use_triggers_1mu = cfg_analyze.getParameter<bool>("use_triggers_1mu");
  vstring triggerNames_2mu = cfg_analyze.getParameter<vstring>("triggers_2mu");
  std::vector<hltPath *> triggers_2mu = create_hltPaths(triggerNames_2mu);
  bool use_triggers_2mu = cfg_analyze.getParameter<bool>("use_triggers_2mu");
  vstring triggerNames_1e1mu =
      cfg_analyze.getParameter<vstring>("triggers_1e1mu");
  std::vector<hltPath *> triggers_1e1mu = create_hltPaths(triggerNames_1e1mu);
  bool use_triggers_1e1mu =
      cfg_analyze.getParameter<bool>("use_triggers_1e1mu");

  bool apply_offline_e_trigger_cuts_1e =
      cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e");
  bool apply_offline_e_trigger_cuts_2e =
      cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2e");
  bool apply_offline_e_trigger_cuts_1mu =
      cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1mu");
  bool apply_offline_e_trigger_cuts_2mu =
      cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2mu");
  bool apply_offline_e_trigger_cuts_1e1mu =
      cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e1mu");

  // Lepton charge stuff, opposite sign, same sign
  enum { kOS, kSS, kDisabled };
  std::string leptonChargeSelection_string =
      cfg_analyze.getParameter<std::string>("leptonChargeSelection");
  int leptonChargeSelection = -1;
  if (leptonChargeSelection_string == "OS")
    leptonChargeSelection = kOS;
  else if (leptonChargeSelection_string == "SS")
    leptonChargeSelection = kSS;
  else if (leptonChargeSelection_string == "disabled")
    leptonChargeSelection = kDisabled;
  else
    throw cms::Exception("analyze_hh_2lss_vbf")
        << "Invalid Configuration parameter 'leptonChargeSelection' = "
        << leptonChargeSelection_string << " !!\n";

  const std::string electronSelection_string =
      cfg_analyze.getParameter<std::string>("electronSelection");
  const std::string muonSelection_string =
      cfg_analyze.getParameter<std::string>("muonSelection");
  std::cout << "electronSelection_string = " << electronSelection_string
            << "\n"
               "muonSelection_string     = "
            << muonSelection_string << '\n';
  const int electronSelection = get_selection(electronSelection_string);
  const int muonSelection = get_selection(muonSelection_string);

  bool apply_leptonGenMatching =
      cfg_analyze.getParameter<bool>("apply_leptonGenMatching");
  std::vector<leptonChargeFlipGenMatchEntry> leptonGenMatch_definitions =
      getLeptonChargeFlipGenMatch_definitions_2lepton(true);
  std::cout << "leptonGenMatch_definitions:" << std::endl;
  std::cout << leptonGenMatch_definitions;

  GenMatchInterface genMatchInterface(2, apply_leptonGenMatching, true);

  TString hadTauSelection_string =
      cfg_analyze.getParameter<std::string>("hadTauSelection").data();
  TObjArray *hadTauSelection_parts = hadTauSelection_string.Tokenize("|");
  assert(hadTauSelection_parts->GetEntries() >= 1);
  std::string hadTauSelection_part2 =
      (hadTauSelection_parts->GetEntries() == 2)
          ? (dynamic_cast<TObjString *>(hadTauSelection_parts->At(1)))
                ->GetString()
                .Data()
          : "";
  delete hadTauSelection_parts;

  const double lep_mva_cut_mu =
      cfg_analyze.getParameter<double>("lep_mva_cut_mu");
  const double lep_mva_cut_e =
      cfg_analyze.getParameter<double>("lep_mva_cut_e");
  const std::string lep_mva_wp =
      cfg_analyze.getParameter<std::string>("lep_mva_wp");

  const int minNumJets = cfg_analyze.getParameter<int>("minNumJets");
  const int maxNumTaus = cfg_analyze.getParameter<int>("maxNumTaus");
  std::cout << "minNumJets = " << minNumJets << ",  maxNumTaus = " << maxNumTaus
            << '\n';

  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  bool hasLHE = cfg_analyze.getParameter<bool>("hasLHE");
  bool hasPS = cfg_analyze.getParameter<bool>("hasPS");
  bool apply_LHE_nom = cfg_analyze.getParameter<bool>("apply_LHE_nom");
  bool useObjectMultiplicity =
      cfg_analyze.getParameter<bool>("useObjectMultiplicity");
  std::string central_or_shift_main =
      cfg_analyze.getParameter<std::string>("central_or_shift");
  std::vector<std::string> central_or_shifts_local =
      cfg_analyze.getParameter<std::vector<std::string>>(
          "central_or_shifts_local");
  edm::VParameterSet lumiScale =
      cfg_analyze.getParameter<edm::VParameterSet>("lumiScale");
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");
  std::string apply_topPtReweighting_str =
      cfg_analyze.getParameter<std::string>("apply_topPtReweighting");
  bool apply_topPtReweighting = !apply_topPtReweighting_str.empty();
  bool apply_l1PreFireWeight =
      cfg_analyze.getParameter<bool>("apply_l1PreFireWeight");
  bool apply_btagSFRatio = cfg_analyze.getParameter<bool>("applyBtagSFRatio");
  bool apply_hlt_filter = cfg_analyze.getParameter<bool>("apply_hlt_filter");
  bool apply_met_filters = cfg_analyze.getParameter<bool>("apply_met_filters");
  edm::ParameterSet cfgMEtFilter =
      cfg_analyze.getParameter<edm::ParameterSet>("cfgMEtFilter");
  MEtFilterSelector metFilterSelector(cfgMEtFilter, isMC);
  const bool useNonNominal = cfg_analyze.getParameter<bool>("useNonNominal");
  const bool useNonNominal_jetmet = useNonNominal || !isMC;
  std::string apply_genPhotonFilter_string =
      cfg_analyze.getParameter<std::string>("apply_genPhotonFilter");
  GenPhotonFilter genPhotonFilter(apply_genPhotonFilter_string);
  bool apply_genPhotonFilter = apply_genPhotonFilter_string != "disabled";

  if (!central_or_shifts_local.empty()) {
    assert(central_or_shift_main == "central");
    assert(std::find(central_or_shifts_local.cbegin(),
                     central_or_shifts_local.cend(),
                     "central") != central_or_shifts_local.cend());
  } else {
    central_or_shifts_local = {central_or_shift_main};
  }

  edm::ParameterSet triggerWhiteList;
  if (!isMC) {
    triggerWhiteList =
        cfg_analyze.getParameter<edm::ParameterSet>("triggerWhiteList");
  }

  const edm::ParameterSet additionalEvtWeight =
      cfg_analyze.getParameter<edm::ParameterSet>("evtWeight");
  const bool applyAdditionalEvtWeight =
      additionalEvtWeight.getParameter<bool>("apply");
  EvtWeightManager *eventWeightManager = nullptr;
  if (applyAdditionalEvtWeight) {
    eventWeightManager = new EvtWeightManager(additionalEvtWeight);
    eventWeightManager->set_central_or_shift(central_or_shift_main);
  }

  bool isDEBUG = cfg_analyze.getParameter<bool>("isDEBUG");

  checkOptionValidity(central_or_shift_main, isMC);
  const int met_option = useNonNominal_jetmet
                             ? kJetMET_central_nonNominal
                             : getMET_option(central_or_shift_main, isMC);
  const int jetPt_option = useNonNominal_jetmet
                               ? kJetMET_central_nonNominal
                               : getJet_option(central_or_shift_main, isMC);
  const int fatJetPt_option =
      useNonNominal_jetmet ? kFatJet_central_nonNominal
                           : getFatJet_option(central_or_shift_main, isMC);
  const int hadTauPt_option = useNonNominal_jetmet
                                  ? kHadTauPt_uncorrected
                                  : getHadTauPt_option(central_or_shift_main);

  std::cout << "central_or_shift = " << central_or_shift_main
            << "\n"
               " -> hadTauPt_option = "
            << hadTauPt_option
            << "\n"
               " -> met_option      = "
            << met_option
            << "\n"
               " -> jetPt_option    = "
            << jetPt_option
            << "\n"
               "--> fatJetPt_option = "
            << fatJetPt_option << '\n';

  edm::ParameterSet cfg_dataToMCcorrectionInterface;
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("era", era_string);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>(
      "hadTauSelection", hadTauSelection_part2);
  cfg_dataToMCcorrectionInterface.addParameter<int>(
      "hadTauSelection_antiElectron", hadTauSelection_antiElectron);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon",
                                                    hadTauSelection_antiMuon);
  cfg_dataToMCcorrectionInterface.addParameter<bool>("isDEBUG", isDEBUG);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("lep_mva_wp",
                                                            lep_mva_wp);
  Data_to_MC_CorrectionInterface_Base *dataToMCcorrectionInterface = nullptr;
  switch (era) {
  case Era::k2016:
    dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2016(
        cfg_dataToMCcorrectionInterface);
    break;
  case Era::k2017:
    dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2017(
        cfg_dataToMCcorrectionInterface);
    break;
  case Era::k2018:
    dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2018(
        cfg_dataToMCcorrectionInterface);
    break;
  default:
    throw cmsException("analyze_hh_2lss_vbf", __LINE__)
        << "Invalid era = " << static_cast<int>(era);
  }
  const ChargeMisIdRate chargeMisIdRate(era, lep_mva_wp);

  std::string applyFakeRateWeights_string =
      cfg_analyze.getParameter<std::string>("applyFakeRateWeights");
  int applyFakeRateWeights = -1;
  if (applyFakeRateWeights_string == "disabled")
    applyFakeRateWeights = kFR_disabled;
  else if (applyFakeRateWeights_string == "2lepton")
    applyFakeRateWeights = kFR_2lepton;
  else
    throw cms::Exception("analyze_hh_2ls_vbf")
        << "Invalid Configuration parameter 'applyFakeRateWeights' = "
        << applyFakeRateWeights_string << " !!\n";

  LeptonFakeRateInterface *leptonFakeRateInterface = 0;
  if (applyFakeRateWeights == kFR_2lepton) {
    edm::ParameterSet cfg_leptonFakeRateWeight =
        cfg_analyze.getParameter<edm::ParameterSet>("leptonFakeRateWeight");
    cfg_leptonFakeRateWeight.addParameter<std::string>("era", era_string);
    cfg_leptonFakeRateWeight.addParameter<std::vector<std::string>>(
        "central_or_shifts", central_or_shifts_local);
    leptonFakeRateInterface =
        new LeptonFakeRateInterface(cfg_leptonFakeRateWeight);
  }

  bool fillGenEvtHistograms =
      cfg_analyze.getParameter<bool>("fillGenEvtHistograms");
  edm::ParameterSet cfg_EvtYieldHistManager =
      cfg_analyze.getParameter<edm::ParameterSet>("cfgEvtYieldHistManager");

  std::string branchName_electrons =
      cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons =
      cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_hadTaus =
      cfg_analyze.getParameter<std::string>("branchName_hadTaus");
  std::string branchName_jets =
      cfg_analyze.getParameter<std::string>("branchName_jets_ak4");
  std::string branchName_jets_ak8 =
      cfg_analyze.getParameter<std::string>("branchName_jets_ak8_Wjj");
  std::string branchName_subjets_ak8 =
      cfg_analyze.getParameter<std::string>("branchName_subjets_ak8_Wjj");
  std::string branchName_met =
      cfg_analyze.getParameter<std::string>("branchName_met");
  std::string branchName_vertex =
      cfg_analyze.getParameter<std::string>("branchName_vertex");

  std::string branchName_genLeptons =
      cfg_analyze.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genHadTaus =
      cfg_analyze.getParameter<std::string>("branchName_genHadTaus");
  std::string branchName_genPhotons =
      cfg_analyze.getParameter<std::string>("branchName_genPhotons");
  std::string branchName_genProxyPhotons =
      cfg_analyze.getParameter<std::string>("branchName_genProxyPhotons");
  std::string branchName_genFromHardProcess =
      cfg_analyze.getParameter<std::string>("branchName_genFromHardProcess");
  std::string branchName_genJets =
      cfg_analyze.getParameter<std::string>("branchName_genJets");

  std::string branchName_muonGenMatch =
      cfg_analyze.getParameter<std::string>("branchName_muonGenMatch");
  std::string branchName_electronGenMatch =
      cfg_analyze.getParameter<std::string>("branchName_electronGenMatch");
  std::string branchName_hadTauGenMatch =
      cfg_analyze.getParameter<std::string>("branchName_hadTauGenMatch");
  std::string branchName_jetGenMatch =
      cfg_analyze.getParameter<std::string>("branchName_jetGenMatch");

  bool redoGenMatching = cfg_analyze.getParameter<bool>("redoGenMatching");
  bool jetCleaningByIndex =
      cfg_analyze.getParameter<bool>("jetCleaningByIndex");
  bool genMatchingByIndex =
      cfg_analyze.getParameter<bool>("genMatchingByIndex");

  std::string branchName_genHiggses =
      cfg_analyze.getParameter<std::string>("branchName_genHiggses");

  std::string branchName_genWBosons =
      cfg_analyze.getParameter<std::string>("branchName_genWBosons");
  std::string branchName_genWJets =
      cfg_analyze.getParameter<std::string>("branchName_genWJets");

  std::string selEventsFileName_input =
      cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input
            << std::endl;
  RunLumiEventSelector *run_lumi_eventSelector = 0;
  if (selEventsFileName_input != "") {
    edm::ParameterSet cfg_runLumiEventSelector;
    cfg_runLumiEventSelector.addParameter<std::string>("inputFileName",
                                                       selEventsFileName_input);
    cfg_runLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfg_runLumiEventSelector);
  }

  const bool enable_blacklist =
      cfg_analyze.getParameter<bool>("enable_blacklist");
  RunLumiEventRejector *blacklist = nullptr;
  if (enable_blacklist) {
    const edm::ParameterSet blacklist_cfg =
        cfg_analyze.getParameter<edm::ParameterSet>("blacklist");
    blacklist = new RunLumiEventRejector(blacklist_cfg);
  }

  std::string selEventsFileName_output =
      cfg_analyze.getParameter<std::string>("selEventsFileName_output");
  std::cout << "selEventsFileName_output = " << selEventsFileName_output
            << std::endl;

  fwlite::InputSource inputFiles(cfg);
  int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper *inputTree =
      new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s)."
            << std::endl;

  //--- declare event-level variables
  EventInfo eventInfo(analysisConfig);
  if (isMC) {
    const double ref_genWeight =
        cfg_analyze.getParameter<double>("ref_genWeight");
    eventInfo.set_refGetWeight(ref_genWeight);
  }

  //--- HH coupling scan
  const edm::ParameterSet hhWeight_cfg =
      cfg_analyze.getParameterSet("hhWeight_cfg");
  const bool apply_HH_rwgt_lo =
      analysisConfig.isHH_rwgt_allowed() &&
      hhWeight_cfg.getParameter<bool>("apply_rwgt_lo");
  const bool apply_HH_rwgt_nlo =
      analysisConfig.isHH_rwgt_allowed() &&
      hhWeight_cfg.getParameter<bool>("apply_rwgt_nlo");
  const HHWeightInterfaceCouplings *const hhWeight_couplings =
      new HHWeightInterfaceCouplings(hhWeight_cfg);
  const HHWeightInterfaceLO *HHWeightLO_calc = nullptr;
  const HHWeightInterfaceNLO *HHWeightNLO_calc = nullptr;
  std::vector<std::string> HHWeightNames;
  std::vector<std::string> HHBMNames;
  if (apply_HH_rwgt_lo || apply_HH_rwgt_nlo) {
    HHWeightNames = hhWeight_couplings->get_weight_names();
    HHBMNames = hhWeight_couplings->get_bm_names();

    if (apply_HH_rwgt_lo) {
      HHWeightLO_calc =
          new HHWeightInterfaceLO(hhWeight_couplings, hhWeight_cfg);
    }

    if (apply_HH_rwgt_nlo) {
      HHWeightNLO_calc = new HHWeightInterfaceNLO(hhWeight_couplings, era);
    }
  }

  const std::vector<edm::ParameterSet> tHweights =
      cfg_analyze.getParameterSetVector("tHweights");
  if ((isMC_tH || isMC_ttH) && !tHweights.empty()) {
    eventInfo.loadWeight_tH(tHweights);
  }
  EventInfoReader eventInfoReader(&eventInfo);
  if (apply_topPtReweighting) {
    eventInfoReader.setTopPtRwgtBranchName(apply_topPtReweighting_str);
  }
  inputTree->registerReader(&eventInfoReader);

  RecoVertex vertex;
  RecoVertexReader vertexReader(&vertex, branchName_vertex);
  inputTree->registerReader(&vertexReader);

  ObjectMultiplicity objectMultiplicity;
  ObjectMultiplicityReader objectMultiplicityReader(&objectMultiplicity);
  if (useObjectMultiplicity) {
    inputTree->registerReader(&objectMultiplicityReader);
  }
  const int minLeptonSelection = std::min(electronSelection, muonSelection);

  hltPathReader hltPathReader_instance(
      {triggers_1e, triggers_2e, triggers_1mu, triggers_2mu, triggers_1e1mu});
  inputTree->registerReader(&hltPathReader_instance);

  if (eventWeightManager) {
    inputTree->registerReader(eventWeightManager);
  }

  L1PreFiringWeightReader *l1PreFiringWeightReader = nullptr;
  if (apply_l1PreFireWeight) {
    l1PreFiringWeightReader = new L1PreFiringWeightReader(era);
    inputTree->registerReader(l1PreFiringWeightReader);
  }

  BtagSFRatioFacility *btagSFRatioFacility = nullptr;
  if (apply_btagSFRatio) {
    const edm::ParameterSet btagSFRatio =
        cfg_analyze.getParameterSet("btagSFRatio");
    btagSFRatioFacility = new BtagSFRatioFacility(btagSFRatio);
  }

  //--- declare particle collections
  const bool readGenObjects = isMC && !redoGenMatching;
  RecoMuonReader *muonReader =
      new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  inputTree->registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  // RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable_hh_multilepton fakeableMuonSelector(
      era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);
  muonReader->set_mvaTTH_wp(lep_mva_cut_mu);

  RecoElectronReader *electronReader =
      new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  // RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era, -1,
  // isDEBUG);
  RecoElectronCollectionSelectorFakeable_hh_multilepton
      fakeableElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era, -1, isDEBUG);
  electronReader->set_mvaTTH_wp(lep_mva_cut_e);

  RecoHadTauReader *hadTauReader =
      new RecoHadTauReader(era, branchName_hadTaus, isMC, readGenObjects);
  hadTauReader->setHadTauPt_central_or_shift(hadTauPt_option);
  inputTree->registerReader(hadTauReader);
  RecoHadTauCollectionGenMatcher hadTauGenMatcher;
  RecoHadTauCollectionCleaner hadTauCleaner(0.3, isDEBUG);
  RecoHadTauCollectionSelectorFakeable fakeableHadTauSelector(era, -1, isDEBUG);
  fakeableHadTauSelector.set_if_looser(hadTauSelection_part2);
  fakeableHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  fakeableHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  RecoHadTauCollectionSelectorTight tightHadTauSelector(era, -1, isDEBUG);
  tightHadTauSelector.set(hadTauSelection_part2);
  tightHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  tightHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  RecoHadTauSelectorTight tightHadTauFilter(era, -1, isDEBUG);
  tightHadTauFilter.set(hadTauSelection_part2);
  tightHadTauFilter.set_min_antiElectron(hadTauSelection_antiElectron);
  tightHadTauFilter.set_min_antiMuon(hadTauSelection_antiMuon);

  RecoJetReader *jetReader =
      new RecoJetReader(era, isMC, branchName_jets, readGenObjects);
  jetReader->setPtMass_central_or_shift(jetPt_option);
  jetReader->read_btag_systematics((central_or_shifts_local.size() > 1 ||
                                    central_or_shift_main != "central") &&
                                   isMC);
  inputTree->registerReader(jetReader);
  RecoJetCollectionGenMatcher jetGenMatcher;
  RecoJetCollectionCleaner jetCleaner(0.4, isDEBUG);
  RecoJetCollectionCleanerByIndex jetCleanerByIndex(isDEBUG);
  RecoJetCollectionSelector jetSelector(era, -1, isDEBUG);
  RecoJetCollectionSelector jetSelectorVBF(era, -1, isDEBUG);
  // jetSelectorVBF.getSelector().set_min_pt(30.);
  jetSelectorVBF.getSelector().set_max_absEta(4.7);
  RecoJetCollectionSelectorBtagLoose jetSelectorBtagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorBtagMedium(era, -1, isDEBUG);

  RecoJetReaderAK8 *jetReaderAK8 = new RecoJetReaderAK8(
      era, isMC, branchName_jets_ak8, branchName_subjets_ak8);
  jetReaderAK8->set_central_or_shift(fatJetPt_option);
  jetReaderAK8->ignoreSys(kFatJetNone);
  inputTree->registerReader(jetReaderAK8);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR16(1.6, isDEBUG);
  RecoJetCollectionSelectorAK8 jetSelectorAK8(era, -1, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_Wjj jetSelectorAK8_Wjj(
      era, -1, isDEBUG); // Need to redefine new class
                         // RecoJetCollectionSelectorAK8_WWWW_Wjj
  std::cout << "branchName_jets_ak8: " << branchName_jets_ak8 << ", "
            << "branchName_subjets_ak8: " << branchName_subjets_ak8 << "\n";
  if (branchName_jets_ak8.find("AK8LS") != std::string::npos &&
      branchName_subjets_ak8.find("AK8LS") != std::string::npos) {
    jetSelectorAK8_Wjj.disableDeltaRCut_between_AK8Subjets_NearestLepton();
    std::cout << "\t diable dR(AK8subjets, nearestLepton) cut ***** \n";
  } else {
    jetSelectorAK8_Wjj.enableDeltaRCut_between_AK8Subjets_NearestLepton();
    std::cout << "\t enable dR(AK8subjets, nearestLepton) cut ***** \n";
  }

  GenParticleReader *genWBosonReader = nullptr;
  GenParticleReader *genWJetReader = nullptr;
  if (isMC) {
    genWBosonReader = new GenParticleReader(branchName_genWBosons);
    inputTree->registerReader(genWBosonReader);
    genWJetReader = new GenParticleReader(branchName_genWJets);
    inputTree->registerReader(genWJetReader);
  }

  //--- declare missing transverse energy
  RecoMEtReader *metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(met_option);
  metReader->set_phiModulationCorrDetails(&eventInfo, &vertex);
  inputTree->registerReader(metReader);

  MEtFilter metFilters;
  MEtFilterReader *metFilterReader = new MEtFilterReader(&metFilters, era);
  inputTree->registerReader(metFilterReader);

  //--- declare generator level information
  GenLeptonReader *genLeptonReader = nullptr;
  GenHadTauReader *genHadTauReader = nullptr;
  GenPhotonReader *genPhotonReader = nullptr;
  GenPhotonReader *genProxyPhotonReader = nullptr;
  GenParticleReader *genFromHardProcessReader = nullptr;
  GenJetReader *genJetReader = nullptr;
  GenParticleReader *genHiggsReader = nullptr;
  LHEInfoReader *lheInfoReader = nullptr;
  PSWeightReader *psWeightReader = nullptr;

  GenParticleReader *genMatchToMuonReader = nullptr;
  GenParticleReader *genMatchToElectronReader = nullptr;
  GenParticleReader *genMatchToHadTauReader = nullptr;
  GenParticleReader *genMatchToJetReader = nullptr;

  LHEParticleReader *general_lhe_reader = nullptr;

  if (isMC) {
    general_lhe_reader = new LHEParticleReader("LHEPart");
    inputTree->registerReader(general_lhe_reader);
    genJetReader = new GenJetReader("GenJet");
    inputTree->registerReader(genJetReader);
    // genLeptonReader = new GenLeptonReader("GenLep");
    // inputTree->registerReader(genLeptonReader);
    bool readGenPhotons = apply_genPhotonFilter;
    if (!readGenObjects) {
      genLeptonReader = new GenLeptonReader(branchName_genLeptons);
      inputTree->registerReader(genLeptonReader);
      genHadTauReader = new GenHadTauReader(branchName_genHadTaus);
      inputTree->registerReader(genHadTauReader);
      // genJetReader = new GenJetReader(branchName_genJets);
      // inputTree->registerReader(genJetReader);

      if (genMatchingByIndex) {
        genMatchToMuonReader = new GenParticleReader(branchName_muonGenMatch);
        genMatchToMuonReader->readGenPartFlav(true);
        inputTree->registerReader(genMatchToMuonReader);

        genMatchToElectronReader =
            new GenParticleReader(branchName_electronGenMatch);
        genMatchToElectronReader->readGenPartFlav(true);
        inputTree->registerReader(genMatchToElectronReader);

        genMatchToHadTauReader =
            new GenParticleReader(branchName_hadTauGenMatch);
        genMatchToHadTauReader->readGenPartFlav(true);
        inputTree->registerReader(genMatchToHadTauReader);

        genMatchToJetReader = new GenParticleReader(branchName_jetGenMatch);
        genMatchToJetReader->readGenPartFlav(true);
        inputTree->registerReader(genMatchToJetReader);
      } else {
        readGenPhotons = true;
      }
    }


    if (readGenPhotons) {
      genPhotonReader = new GenPhotonReader(branchName_genPhotons);
      inputTree->registerReader(genPhotonReader);
    }

    if (apply_genPhotonFilter) {
      genProxyPhotonReader = new GenPhotonReader(branchName_genProxyPhotons);
      inputTree->registerReader(genProxyPhotonReader);

      genFromHardProcessReader =
          new GenParticleReader(branchName_genFromHardProcess);
      inputTree->registerReader(genFromHardProcessReader);
    }

    genHiggsReader = new GenParticleReader(branchName_genHiggses);
    inputTree->registerReader(genHiggsReader);
    lheInfoReader = new LHEInfoReader(hasLHE);
    inputTree->registerReader(lheInfoReader);
    psWeightReader = new PSWeightReader(hasPS, apply_LHE_nom);
    inputTree->registerReader(psWeightReader);
  }


  const bool selectBDT = cfg_analyze.exists("selectBDT")
                             ? cfg_analyze.getParameter<bool>("selectBDT")
                             : false;
  const edm::ParameterSet mvaInfo_res =
      cfg_analyze.getParameter<edm::ParameterSet>("mvaInfo_res");
  std::vector<double> gen_mHH = analysisConfig.get_HH_resonant_mass_points();
  std::string BDTFileName_spin0_even =
      mvaInfo_res.getParameter<std::string>("BDT_xml_FileName_spin0_even");
  std::string BDTFileName_spin0_odd =
      mvaInfo_res.getParameter<std::string>("BDT_xml_FileName_spin0_odd");
  std::string fitFunctionFileName_spin0 =
      mvaInfo_res.getParameter<std::string>("fitFunctionFileName_spin0");
  std::vector<std::string> BDTInputVariables_spin0 =
      mvaInfo_res.getParameter<std::vector<std::string>>("inputVars_spin0");
  std::string BDTFileName_spin2_even =
      mvaInfo_res.getParameter<std::string>("BDT_xml_FileName_spin2_even");
  std::string BDTFileName_spin2_odd =
      mvaInfo_res.getParameter<std::string>("BDT_xml_FileName_spin2_odd");
  std::string fitFunctionFileName_spin2 =
      mvaInfo_res.getParameter<std::string>("fitFunctionFileName_spin2");
  std::vector<std::string> BDTInputVariables_spin2 =
      mvaInfo_res.getParameter<std::vector<std::string>>("inputVars_spin2");
  const edm::ParameterSet mvaInfo_nonRes =
      cfg_analyze.getParameter<edm::ParameterSet>("mvaInfo_nonRes");
  std::vector<std::string> nonRes_BMs =
      cfg_analyze.getParameter<std::vector<std::string>>("nonRes_BMs");
  std::string BDTFileName_nonRes_even =
      mvaInfo_nonRes.getParameter<std::string>("BDT_xml_FileName_nonRes_even");
  std::string BDTFileName_nonRes_odd =
      mvaInfo_nonRes.getParameter<std::string>("BDT_xml_FileName_nonRes_odd");
  std::vector<std::string> BDTInputVariables_nonRes =
      mvaInfo_nonRes.getParameter<std::vector<std::string>>(
          "inputVars_nonRes"); // Include all Input Var.s except BM indices

  std::map<std::string, double> AllVars_Map;

  //--- open output file containing run:lumi:event numbers of events passing
  //final event selection criteria
  std::ostream *selEventsFile =
      (selEventsFileName_output != "")
          ? new std::ofstream(selEventsFileName_output.data(), std::ios::out)
          : 0;
  std::cout << "selEventsFileName_output = " << selEventsFileName_output
            << std::endl;

  //--- declare histograms
  struct selHistManagerType {
    ElectronHistManager *electrons_;
    ElectronHistManager *leadElectron_;
    ElectronHistManager *subleadElectron_;
    MuonHistManager *muons_;
    MuonHistManager *leadMuon_;
    MuonHistManager *subleadMuon_;
    JetHistManager *jets_;
    JetHistManager *leadJet_;
    JetHistManager *subleadJet_;
    JetHistManagerAK8 *jetsAK8_Wjj_;
    MEtHistManager *met_;
    MEtFilterHistManager *metFilters_;
    EvtHistManager_hh_2lss_vbf *evt_;
    DatacardHistManager_hh *datacard_;
    MVAInputVarCorrelationHistManager *mvaInputVarCorrelation_;
    EvtYieldHistManager *evtYield_;
    WeightHistManager *weights_;
  };

  std::map<std::string, GenEvtHistManager *> genEvtHistManager_beforeCuts;
  std::map<std::string, GenEvtHistManager *> genEvtHistManager_afterCuts;
  std::map<std::string, LHEInfoHistManager *> lheInfoHistManager;
  std::map<std::string, std::map<int, selHistManagerType *>> selHistManagers;
  for (const std::string &central_or_shift : central_or_shifts_local) {
    const bool skipBooking = central_or_shift != central_or_shift_main;
    std::vector<const GenMatchEntry *> genMatchDefinitions =
        genMatchInterface.getGenMatchDefinitions();
    for (const GenMatchEntry *genMatchDefinition : genMatchDefinitions) {
      std::string process_and_genMatch = process_string;
      process_and_genMatch += genMatchDefinition->getName();

      int idxLepton = genMatchDefinition->getIdx();

      selHistManagerType *selHistManager = new selHistManagerType();
      if (!skipBooking) {
        selHistManager->electrons_ = new ElectronHistManager(
            makeHistManager_cfg(process_and_genMatch,
                                Form("%s/sel/electrons", histogramDir.data()),
                                era_string, central_or_shift, "allHistograms"));
        selHistManager->electrons_->bookHistograms(fs);
        selHistManager->leadElectron_ =
            new ElectronHistManager(makeHistManager_cfg(
                process_and_genMatch,
                Form("%s/sel/leadElectron", histogramDir.data()), era_string,
                central_or_shift, "minimalHistograms"));
        selHistManager->leadElectron_->bookHistograms(fs);
        selHistManager->subleadElectron_ =
            new ElectronHistManager(makeHistManager_cfg(
                process_and_genMatch,
                Form("%s/sel/subleadElectron", histogramDir.data()), era_string,
                central_or_shift, "minimalHistograms"));
        selHistManager->subleadElectron_->bookHistograms(fs);
        selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(
            process_and_genMatch, Form("%s/sel/muons", histogramDir.data()),
            era_string, central_or_shift, "allHistograms"));
        selHistManager->muons_->bookHistograms(fs);
        selHistManager->leadMuon_ = new MuonHistManager(makeHistManager_cfg(
            process_and_genMatch, Form("%s/sel/leadMuon", histogramDir.data()),
            era_string, central_or_shift, "minimalHistograms"));
        selHistManager->leadMuon_->bookHistograms(fs);
        selHistManager->subleadMuon_ = new MuonHistManager(makeHistManager_cfg(
            process_and_genMatch,
            Form("%s/sel/subleadMuon", histogramDir.data()), era_string,
            central_or_shift, "minimalHistograms"));
        selHistManager->subleadMuon_->bookHistograms(fs);
        selHistManager->jets_ = new JetHistManager(makeHistManager_cfg(
            process_and_genMatch, Form("%s/sel/jets", histogramDir.data()),
            era_string, central_or_shift, "allHistograms"));
        selHistManager->jets_->bookHistograms(fs);
        selHistManager->leadJet_ = new JetHistManager(makeHistManager_cfg(
            process_and_genMatch, Form("%s/sel/leadJet", histogramDir.data()),
            era_string, central_or_shift, "minimalHistograms", 0));
        selHistManager->leadJet_->bookHistograms(fs);
        selHistManager->subleadJet_ = new JetHistManager(makeHistManager_cfg(
            process_and_genMatch,
            Form("%s/sel/subleadJet", histogramDir.data()), era_string,
            central_or_shift, "minimalHistograms", 1));
        selHistManager->subleadJet_->bookHistograms(fs);
        selHistManager->jetsAK8_Wjj_ = new JetHistManagerAK8(
            makeHistManager_cfg(process_and_genMatch,
                                Form("%s/sel/jetsAK8_Wjj", histogramDir.data()),
                                era_string, central_or_shift, "allHistograms"));
        selHistManager->jetsAK8_Wjj_->bookHistograms(fs);
        selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(
            process_and_genMatch, Form("%s/sel/met", histogramDir.data()),
            era_string, central_or_shift));
        selHistManager->met_->bookHistograms(fs);
        selHistManager->metFilters_ = new MEtFilterHistManager(
            makeHistManager_cfg(process_and_genMatch,
                                Form("%s/sel/metFilters", histogramDir.data()),
                                era_string, central_or_shift));
        selHistManager->metFilters_->bookHistograms(fs);
      }
      if (!skipBooking) {
        selHistManager->evt_ =
            new EvtHistManager_hh_2lss_vbf(makeHistManager_cfg(
                process_and_genMatch, Form("%s/sel/evt", histogramDir.data()),
                era_string, central_or_shift));
        selHistManager->evt_->bookHistograms(fs);
      }

      selHistManager->datacard_ = new DatacardHistManager_hh(
          makeHistManager_cfg(process_and_genMatch,
                              Form("%s/sel/datacard", histogramDir.data()),
                              era_string, central_or_shift),
          analysisConfig, eventInfo, HHWeightLO_calc, HHWeightNLO_calc,
          isDEBUG);
      selHistManager->datacard_->bookHistograms(fs);

      if (!skipBooking) {
        std::vector<std::string> mvaInputVariables = {
            "mindR_vbfjet_lep1", "mindR_vbfjet_lep2", "maxJetEta_vbf", "minJetEta_vbf"};
        selHistManager->mvaInputVarCorrelation_ =
            new MVAInputVarCorrelationHistManager(makeHistManager_cfg(
                process_and_genMatch,
                Form("%s/sel/mvaInputVarCorrelation", histogramDir.data()),
                era_string, central_or_shift));
        selHistManager->mvaInputVarCorrelation_->bookHistograms(
            fs, mvaInputVariables);
      }


      if (!skipBooking) {
        edm::ParameterSet cfg_EvtYieldHistManager_sel = makeHistManager_cfg(
            process_and_genMatch, Form("%s/sel/evtYield", histogramDir.data()),
            era_string, central_or_shift);
        cfg_EvtYieldHistManager_sel.addParameter<edm::ParameterSet>(
            "runPeriods", cfg_EvtYieldHistManager);
        cfg_EvtYieldHistManager_sel.addParameter<bool>("isMC", isMC);
        selHistManager->evtYield_ =
            new EvtYieldHistManager(cfg_EvtYieldHistManager_sel);
        selHistManager->evtYield_->bookHistograms(fs);
        selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(
            process_and_genMatch, Form("%s/sel/weights", histogramDir.data()),
            era_string, central_or_shift));
        selHistManager->weights_->bookHistograms(
            fs, {"genWeight", "pileupWeight", "triggerWeight",
                 "data_to_MC_correction", "fakeRate"});
      }
      selHistManagers[central_or_shift][idxLepton] = selHistManager;
    }

    if (isMC && !skipBooking) {
      genEvtHistManager_beforeCuts[central_or_shift] =
          new GenEvtHistManager(makeHistManager_cfg(
              process_string, Form("%s/unbiased/genEvt", histogramDir.data()),
              era_string, central_or_shift));
      genEvtHistManager_beforeCuts[central_or_shift]->bookHistograms(fs);
      genEvtHistManager_afterCuts[central_or_shift] =
          new GenEvtHistManager(makeHistManager_cfg(
              process_string, Form("%s/sel/genEvt", histogramDir.data()),
              era_string, central_or_shift));
      genEvtHistManager_afterCuts[central_or_shift]->bookHistograms(fs);
      lheInfoHistManager[central_or_shift] =
          new LHEInfoHistManager(makeHistManager_cfg(
              process_string, Form("%s/sel/lheInfo", histogramDir.data()),
              era_string, central_or_shift));
      lheInfoHistManager[central_or_shift]->bookHistograms(fs);

      if (eventWeightManager) {
        genEvtHistManager_beforeCuts[central_or_shift]->bookHistograms(
            fs, eventWeightManager);
        genEvtHistManager_afterCuts[central_or_shift]->bookHistograms(
            fs, eventWeightManager);
      }
    }
  }

  std::cout << "Book BDT filling" << std::endl;
  NtupleFillerBDT<float, int> *bdt_filler = nullptr;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::float_type
      float_type;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::int_type int_type;

  if (selectBDT) {
    bdt_filler =
        new std::remove_pointer<decltype(bdt_filler)>::type(makeHistManager_cfg(
            process_string, Form("%s/sel/evtntuple", histogramDir.data()),
            era_string, central_or_shift_main));
    if (apply_HH_rwgt_lo || apply_HH_rwgt_nlo) {
      for (auto bmName : HHWeightNames) {
        bdt_filler->register_variable<float_type>(bmName.data());
      }
    }
    bdt_filler->register_variable<float_type>(
        "dihiggsVisMass_sel",
        "dihiggsMass_wMet_sel",
        "evtWeight",
        "vbf_m_jj",
        "vbf_dEta_jj",
        "vbf_dR_jj",
        "mindR_vbfjet_lep1",
        "mindR_vbfjet_lep2",
        "maxJetEta_vbf", "minJetEta_vbf",
        "lhe_dEta_jj", "lhe_dPhi_jj", "lhe_m_jj", "lhe_dR_jj",
        "matched_dEta_jj", "matched_dPhi_jj", "matched_m_jj", "matched_dR_jj",
        "best_dEta_jj", "best_dPhi_jj", "best_m_jj", "best_dR_jj",
        "lhe_pt_lead", "lhe_pt_sublead", "matched_pt_lead", "matched_pt_sublead", "best_pt_lead", "best_pt_sublead",
        "genjet_dEta_jj", "genjet_dPhi_jj", "genjet_m_jj", "genjet_dR_jj",
        "mass_jj_W", "mass_jj_W2", "sum_mass_W",
        "sum_m_lj", "pT_sum", "m_ll",
        "maxJetPt_vbf", "minJetPt_vbf", "mindR_vbfJet_W1", "maxdR_vbfJet_W1", "mindR_vbfjet_lep", "maxdR_vbfjet_lep",
        "dR_h1h2", "pT_h1", "pT_h2", "dR_h1_j1", "dR_h1_j2", "dR_h2_j1", "dR_h2_j2", "mass_h1", "mass_h2",
        "H1H2_centrality", "vbfj1_cosphi", "vbfj2_cosphi"
    );
    bdt_filler->register_variable<int_type>("isVBF");
    bdt_filler->bookTree(fs);
  }

  std::vector<double> NormBM;

  int analyzedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  std::map<std::string, int>
      selectedEntries_byGenMatchType; // key = process_and_genMatch
  std::map<std::string, std::map<std::string, double>>
      selectedEntries_weighted_byGenMatchType; // key = process_and_genMatch
  TH1 *histogram_analyzedEntries =
      fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  TH1 *histogram_selectedEntries =
      fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  cutFlowTableType cutFlowTable;
  const edm::ParameterSet cutFlowTableCfg = makeHistManager_cfg(
      process_string, Form("%s/sel/cutFlow", histogramDir.data()), era_string,
      central_or_shift_main);
  const std::vector<std::string> cuts = {
      "run:ls:event selection", "object multiplicity", "gen photon filter",
      "trigger", ">= 2 presel leptons", ">= N jets", "b-jet veto",
      ">= 2 sel leptons", "<= 2 tight leptons",
      "trigger & fakeable lepton flavor matching", "trigger & dataset matching",
      "HLT filter matching", "m(ll) > 12 GeV",
      "lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV",
      "tight lepton charge", "sel lepton-pair SS/OS charge",
      // "Z-boson mass veto",
      "H->ZZ*->4l veto", "met LD", "MEt filters", "signal region veto",
      "VBF requirement"};
  CutFlowTableHistManager *cutFlowHistManager =
      new CutFlowTableHistManager(cutFlowTableCfg, cuts);
  cutFlowHistManager->bookHistograms(fs);
  while (inputTree->hasNextEvent() &&
         (!run_lumi_eventSelector ||
          (run_lumi_eventSelector && !run_lumi_eventSelector->areWeDone()))) {
    if (inputTree->canReport(reportEvery)) {
      std::cout << "processing Entry " << inputTree->getCurrentMaxEventIdx()
                << " or " << inputTree->getCurrentEventIdx() << " entry in #"
                << (inputTree->getProcessedFileCount() - 1) << " (" << eventInfo
                << ") file (" << selectedEntries << " Entries selected)\n";
    }
    ++analyzedEntries;
    histogram_analyzedEntries->Fill(0.);

    if (isDEBUG) {
      std::cout << "event #" << inputTree->getCurrentMaxEventIdx() << ' '
                << eventInfo << '\n';
    }

    if (run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo)) {
      continue;
    }
    EvtWeightRecorderHH evtWeightRecorder(central_or_shifts_local,
                                          central_or_shift_main, isMC);
    cutFlowTable.update("run:ls:event selection",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "run:ls:event selection", evtWeightRecorder.get(central_or_shift_main));

    if (run_lumi_eventSelector) {
      std::cout << "processing Entry #"
                << inputTree->getCumulativeMaxEventCount() << ": " << eventInfo
                << std::endl;
      if (inputTree->isOpen()) {
        std::cout << "input File = " << inputTree->getCurrentFileName()
                  << std::endl;
      }
    }

    if (useObjectMultiplicity) {
      if (objectMultiplicity.getNRecoLepton(minLeptonSelection) < 2 ||
          objectMultiplicity.getNRecoLepton(kTight) > 2) {
        if (isDEBUG || run_lumi_eventSelector) {
          std::cout << "event " << eventInfo.str()
                    << " FAILS preliminary object multiplicity cuts\n";
        }
        continue;
      }
    }
    cutFlowTable.update("object multiplicity",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "object multiplicity", evtWeightRecorder.get(central_or_shift_main));

    //--- build collections of generator level particles (before any cuts are
    //applied, to check distributions in unbiased event samples)
    std::vector<GenLepton> genLeptons;
    std::vector<GenLepton> genElectrons;
    std::vector<GenLepton> genMuons;
    std::vector<GenHadTau> genHadTaus;
    std::vector<GenPhoton> genPhotons;
    std::vector<GenPhoton> genPhotonsFinal;
    std::vector<GenPhoton> genProxyPhotons;
    std::vector<GenParticle> genFromHardProcess;
    std::vector<GenJet> genJets;
    std::vector<GenParticle> genHiggses;
    std::vector<LHEParticle> lheParticles;


    std::vector<GenParticle> muonGenMatch;
    std::vector<GenParticle> electronGenMatch;
    std::vector<GenParticle> hadTauGenMatch;
    std::vector<GenParticle> jetGenMatch;
    if (isMC && (fillGenEvtHistograms || apply_genPhotonFilter)) {
      if (genLeptonReader) {
        genLeptons = genLeptonReader->read();
        for (const GenLepton &genLepton : genLeptons) {
          const int abs_pdgId = std::abs(genLepton.pdgId());
          switch (abs_pdgId) {
          case 11:
            genElectrons.push_back(genLepton);
            break;
          case 13:
            genMuons.push_back(genLepton);
            break;
          default:
            assert(0);
          }
        }
      }
      if (genHadTauReader)
        genHadTaus = genHadTauReader->read();
      if (general_lhe_reader){
        lheParticles = general_lhe_reader->read();
        // std::cout << "1st particle id:" << lheParticles[0].pdgId() << endl;
        // std::cout << "2nd particle id:" << lheParticles[1].pdgId() << endl;
        // std::cout << "3rd particle id:" << lheParticles[2].pdgId() << endl;
        // std::cout << "4th particle id:" << lheParticles[3].pdgId() << endl;
        // std::cout << "3rd particle eta:" << lheParticles[2].eta() << endl;
        // std::cout << "4th particle eta:" << lheParticles[3].eta() << endl;
        // std::cout << "____________________________________" << endl;
      }
      if (genPhotonReader)
        genPhotons = genPhotonReader->read(apply_genPhotonFilter);
      if (genJetReader)
        genJets = genJetReader->read();
      // std::cout << "1st particle eta:" << genJets[0].eta() << endl;
      if (genHiggsReader)
        genHiggses = genHiggsReader->read();

      if (genProxyPhotonReader)
        genProxyPhotons = genProxyPhotonReader->read(apply_genPhotonFilter);
      if (genFromHardProcessReader)
        genFromHardProcess = genFromHardProcessReader->read();

      if (genMatchToMuonReader)
        muonGenMatch = genMatchToMuonReader->read();
      if (genMatchToElectronReader)
        electronGenMatch = genMatchToElectronReader->read();
      if (genMatchToHadTauReader)
        hadTauGenMatch = genMatchToHadTauReader->read();
      if (genMatchToJetReader)
        jetGenMatch = genMatchToJetReader->read();
    }
    genPhotonsFinal = filterByStatus(genPhotons, 1);
    // std::cout << "Gen leptons: " << genLeptons.size() << std::endl;
    if (!genPhotonFilter(genPhotons, genProxyPhotons, genFromHardProcess)) {
      if (isDEBUG || run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str()
                  << " FAILS gen photon filter\n";
      }
      continue;
    }
    cutFlowTable.update("gen photon filter",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "gen photon filter", evtWeightRecorder.get(central_or_shift_main));

    eventInfo.reset_productionMode();
    std::vector<GenParticle> genWBosons;
    std::vector<GenParticle> genWJets;
    if (isMC) {
      genWBosons = genWBosonReader->read();
      genWJets = genWJetReader->read();

      if (analysisConfig.isMC_VH()) {
        eventInfo.set_productionMode(get_VH_productionMode(genWBosons));
      }
    }


    if (isMC) {
      if (apply_genWeight)
        evtWeightRecorder.record_genWeight(eventInfo);
      if (eventWeightManager)
        evtWeightRecorder.record_auxWeight(eventWeightManager);
      if (l1PreFiringWeightReader)
        evtWeightRecorder.record_l1PrefireWeight(l1PreFiringWeightReader);
      if (apply_topPtReweighting)
        evtWeightRecorder.record_toppt_rwgt(eventInfo.topPtRwgtSF);
      if (apply_HH_rwgt_lo)
        evtWeightRecorder.record_hhWeight_lo(HHWeightLO_calc, eventInfo,
                                             isDEBUG);
      if (apply_HH_rwgt_nlo)
        evtWeightRecorder.record_hhWeight_nlo(HHWeightNLO_calc, eventInfo,
                                              isDEBUG);
      lheInfoReader->read();
      psWeightReader->read();
      evtWeightRecorder.record_lheScaleWeight(lheInfoReader);
      evtWeightRecorder.record_psWeight(psWeightReader);
      evtWeightRecorder.record_puWeight(&eventInfo);
      evtWeightRecorder.record_nom_tH_weight(&eventInfo);
      evtWeightRecorder.record_lumiScale(lumiScale);
      for (const std::string &central_or_shift : central_or_shifts_local) {
        if (central_or_shift != central_or_shift_main) {
          continue;
        }
        genEvtHistManager_beforeCuts[central_or_shift]->fillHistograms(
            genElectrons, genMuons, genHadTaus, genPhotonsFinal, genJets,
            evtWeightRecorder.get_inclusive(central_or_shift));
        if (eventWeightManager) {
          genEvtHistManager_beforeCuts[central_or_shift]->fillHistograms(
              eventWeightManager,
              evtWeightRecorder.get_inclusive(central_or_shift));
        }
      }
    }

    bool isTriggered_1e =
        hltPaths_isTriggered(triggers_1e, triggerWhiteList, eventInfo, isMC);
    bool isTriggered_2e =
        hltPaths_isTriggered(triggers_2e, triggerWhiteList, eventInfo, isMC);
    bool isTriggered_1mu =
        hltPaths_isTriggered(triggers_1mu, triggerWhiteList, eventInfo, isMC);
    bool isTriggered_2mu =
        hltPaths_isTriggered(triggers_2mu, triggerWhiteList, eventInfo, isMC);
    bool isTriggered_1e1mu =
        hltPaths_isTriggered(triggers_1e1mu, triggerWhiteList, eventInfo, isMC);

    bool selTrigger_1e = use_triggers_1e && isTriggered_1e;
    bool selTrigger_2e = use_triggers_2e && isTriggered_2e;
    bool selTrigger_1mu = use_triggers_1mu && isTriggered_1mu;
    bool selTrigger_2mu = use_triggers_2mu && isTriggered_2mu;
    bool selTrigger_1e1mu = use_triggers_1e1mu && isTriggered_1e1mu;
    if (!(selTrigger_1e || selTrigger_2e || selTrigger_1mu || selTrigger_2mu ||
          selTrigger_1e1mu)) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str() << " FAILS trigger selection."
                  << std::endl;
        std::cout << " (selTrigger_1e = " << selTrigger_1e
                  << ", selTrigger_2e = " << selTrigger_2e
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_2mu = " << selTrigger_2mu
                  << ", selTrigger_1e1mu = " << selTrigger_1e1mu << ")"
                  << std::endl;
      }
      continue;
    }
    cutFlowTable.update("trigger",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "trigger", evtWeightRecorder.get(central_or_shift_main));

    if ((selTrigger_2e && !apply_offline_e_trigger_cuts_2e) ||
        (selTrigger_1e1mu && !apply_offline_e_trigger_cuts_1e1mu) ||
        (selTrigger_1e && !apply_offline_e_trigger_cuts_1e) ||
        (selTrigger_1mu && !apply_offline_e_trigger_cuts_1mu) ||
        (selTrigger_2mu && !apply_offline_e_trigger_cuts_2mu)) {
      fakeableElectronSelector.disable_offline_e_trigger_cuts();
      tightElectronSelector.disable_offline_e_trigger_cuts();
    } else {
      tightElectronSelector.enable_offline_e_trigger_cuts();
      fakeableElectronSelector.enable_offline_e_trigger_cuts();
    }

    //--- build collections of electrons, muons and hadronic taus;
    //    resolve overlaps in order of priority: muon, electron,
    const std::vector<RecoMuon> muons = muonReader->read();
    const std::vector<const RecoMuon *> muon_ptrs = convert_to_ptrs(muons);
    const std::vector<const RecoMuon *> cleanedMuons =
        muon_ptrs; // CV: no cleaning needed for muons, as they have the highest
                   // priority in the overlap removal
    const std::vector<const RecoMuon *> preselMuons =
        preselMuonSelector(cleanedMuons, isHigherConePt);
    const std::vector<const RecoMuon *> fakeableMuons =
        fakeableMuonSelector(preselMuons, isHigherConePt);
    const std::vector<const RecoMuon *> tightMuons =
        tightMuonSelector(fakeableMuons, isHigherConePt);

    const std::vector<RecoElectron> electrons = electronReader->read();
    const std::vector<const RecoElectron *> electron_ptrs =
        convert_to_ptrs(electrons);
    const std::vector<const RecoElectron *> cleanedElectrons =
        electronCleaner(electron_ptrs, preselMuons);
    const std::vector<const RecoElectron *> preselElectrons =
        preselElectronSelector(cleanedElectrons, isHigherConePt);
    const std::vector<const RecoElectron *> preselElectronsUncleaned =
        preselElectronSelector(electron_ptrs, isHigherConePt);
    const std::vector<const RecoElectron *> fakeableElectrons =
        fakeableElectronSelector(preselElectrons, isHigherConePt);
    const std::vector<const RecoElectron *> tightElectrons =
        tightElectronSelector(fakeableElectrons, isHigherConePt);

    const std::vector<const RecoLepton *> preselLeptonsFull =
        mergeLeptonCollections(preselElectrons, preselMuons, isHigherConePt);
    const std::vector<const RecoLepton *> preselLeptonsFullUncleaned =
        mergeLeptonCollections(preselElectronsUncleaned, preselMuons,
                               isHigherConePt);
    const std::vector<const RecoLepton *> fakeableLeptonsFull =
        mergeLeptonCollections(fakeableElectrons, fakeableMuons,
                               isHigherConePt);
    const std::vector<const RecoLepton *> tightLeptonsFull =
        mergeLeptonCollections(tightElectrons, tightMuons, isHigherConePt);

    const std::vector<const RecoLepton *> preselLeptons =
        pickFirstNobjects(preselLeptonsFull, 2);
    const std::vector<const RecoLepton *> fakeableLeptons =
        pickFirstNobjects(fakeableLeptonsFull, 2);
    const std::vector<const RecoLepton *> tightLeptons =
        getIntersection(fakeableLeptons, tightLeptonsFull, isHigherConePt);

    std::vector<const RecoLepton *> selLeptons;
    std::vector<const RecoMuon *> selMuons;
    std::vector<const RecoElectron *> selElectrons;
    if (electronSelection == muonSelection) {
      // for SR, flip region and fake CR
      // doesn't matter if we supply electronSelection or muonSelection here
      selLeptons = selectObjects(muonSelection, preselLeptons, fakeableLeptons,
                                 tightLeptons);
      selMuons = getIntersection(preselMuons, selLeptons, isHigherConePt);
      selElectrons =
          getIntersection(preselElectrons, selLeptons, isHigherConePt);
    } else {
      // for MC closure
      // make sure that neither electron nor muon selections are loose
      assert(electronSelection != kLoose && muonSelection != kLoose);
      selMuons =
          selectObjects(muonSelection, preselMuons, fakeableMuons, tightMuons);
      selElectrons = selectObjects(electronSelection, preselElectrons,
                                   fakeableElectrons, tightElectrons);
    }
    const std::vector<const RecoLepton *> selLeptons_full =
        mergeLeptonCollections(selElectrons, selMuons, isHigherConePt);
    if (!(electronSelection == muonSelection))
      selLeptons =
          getIntersection(fakeableLeptons, selLeptons_full, isHigherConePt);

    const std::vector<RecoHadTau> hadTaus = hadTauReader->read();
    const std::vector<const RecoHadTau *> hadTau_ptrs =
        convert_to_ptrs(hadTaus);
    const std::vector<const RecoHadTau *> cleanedHadTaus =
        hadTauCleaner(hadTau_ptrs, preselMuons, preselElectrons);
    const std::vector<const RecoHadTau *> fakeableHadTaus =
        fakeableHadTauSelector(cleanedHadTaus, isHigherPt);
    const std::vector<const RecoHadTau *> selHadTaus =
        tightHadTauSelector(cleanedHadTaus, isHigherPt);

    //--- build collections of jets and select subset of jets passing b-tagging
    //criteria
    const std::vector<RecoJet> jets = jetReader->read();
    const std::vector<const RecoJet *> jet_ptrs = convert_to_ptrs(jets);
    const std::vector<const RecoJet *> cleanedJets =
        jetCleaningByIndex
            ? jetCleanerByIndex(
                  jet_ptrs, selectBDT ? selLeptons_full : fakeableLeptonsFull,
                  fakeableHadTaus)
            : jetCleaner(jet_ptrs,
                         selectBDT ? selLeptons_full : fakeableLeptonsFull,
                         fakeableHadTaus)

        ;
    const std::vector<const RecoJet *> selJets =
        jetSelector(cleanedJets, isHigherPt);
    const std::vector<const RecoJet *> selBJets_loose =
        jetSelectorBtagLoose(cleanedJets, isHigherPt);
    const std::vector<const RecoJet *> selBJets_medium =
        jetSelectorBtagMedium(cleanedJets, isHigherPt);
    int numSelJetsPtGt40 = countHighPtObjects(selJets, 40.);

    const std::vector<const RecoJet *> cleanedJetsVBF =
        jetCleaner(jet_ptrs, fakeableLeptons);
    const std::vector<const RecoJet *> selJetsVBF =
        jetSelectorVBF(cleanedJetsVBF, isHigherPt);

    //--- build collections of generator level particles (after some cuts are
    //applied, to save computing time)
    if (isMC && redoGenMatching && !fillGenEvtHistograms) {
      if (genLeptonReader) {
        genLeptons = genLeptonReader->read();
        for (const GenLepton &genLepton : genLeptons) {
          const int abs_pdgId = std::abs(genLepton.pdgId());
          switch (abs_pdgId) {
          case 11:
            genElectrons.push_back(genLepton);
            break;
          case 13:
            genMuons.push_back(genLepton);
            break;
          default:
            assert(0);
          }
        }
      }
      if (genHadTauReader)
        genHadTaus = genHadTauReader->read();
      if (general_lhe_reader)
        lheParticles = general_lhe_reader->read();
      if (genPhotonReader)
        genPhotonsFinal = genPhotonReader->read();
      if (genJetReader)
        genJets = genJetReader->read();
      if (genHiggsReader)
        genHiggses = genHiggsReader->read();

      if (genMatchToMuonReader)
        muonGenMatch = genMatchToMuonReader->read();
      if (genMatchToElectronReader)
        electronGenMatch = genMatchToElectronReader->read();
      if (genMatchToHadTauReader)
        hadTauGenMatch = genMatchToHadTauReader->read();
      if (genMatchToJetReader)
        jetGenMatch = genMatchToJetReader->read();
    }

    //--- match reconstructed to generator level particles
    if (isMC && redoGenMatching) {
      if (genMatchingByIndex) {
        muonGenMatcher.addGenLeptonMatchByIndex(preselMuons, muonGenMatch,
                                                GenParticleType::kGenMuon);
        muonGenMatcher.addGenHadTauMatch(preselMuons, genHadTaus);
        muonGenMatcher.addGenJetMatch(preselMuons, genJets);

        electronGenMatcher.addGenLeptonMatchByIndex(
            preselElectrons, electronGenMatch, GenParticleType::kGenElectron);
        electronGenMatcher.addGenPhotonMatchByIndex(preselElectrons,
                                                    electronGenMatch);
        electronGenMatcher.addGenHadTauMatch(preselElectrons, genHadTaus);
        electronGenMatcher.addGenJetMatch(preselElectrons, genJets);

        hadTauGenMatcher.addGenLeptonMatchByIndex(
            cleanedHadTaus, hadTauGenMatch, GenParticleType::kGenAnyLepton);
        hadTauGenMatcher.addGenHadTauMatch(cleanedHadTaus, genHadTaus);
        hadTauGenMatcher.addGenJetMatch(cleanedHadTaus, genJets);

        jetGenMatcher.addGenLeptonMatch(selJets, genLeptons);
        jetGenMatcher.addGenHadTauMatch(selJets, genHadTaus);
        jetGenMatcher.addGenJetMatchByIndex(selJets, jetGenMatch);
      } else {
        muonGenMatcher.addGenLeptonMatch(preselMuons, genMuons);
        muonGenMatcher.addGenHadTauMatch(preselMuons, genHadTaus);
        muonGenMatcher.addGenJetMatch(preselMuons, genJets);

        electronGenMatcher.addGenLeptonMatch(preselElectrons, genElectrons);
        electronGenMatcher.addGenPhotonMatch(preselElectrons, genPhotonsFinal);
        electronGenMatcher.addGenHadTauMatch(preselElectrons, genHadTaus);
        electronGenMatcher.addGenJetMatch(preselElectrons, genJets);

        hadTauGenMatcher.addGenLeptonMatch(cleanedHadTaus, genLeptons);
        hadTauGenMatcher.addGenHadTauMatch(cleanedHadTaus, genHadTaus);
        hadTauGenMatcher.addGenJetMatch(cleanedHadTaus, genJets);

        jetGenMatcher.addGenLeptonMatch(selJets, genLeptons);
        jetGenMatcher.addGenHadTauMatch(selJets, genHadTaus);
        jetGenMatcher.addGenJetMatch(selJets, genJets);
      }
    }

    //--- apply preselection
    // require exactly two leptons passing loose preselection criteria
    if (!(preselLeptonsFull.size() >= 2)) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str()
                  << " FAILS preselLeptons selection." << std::endl;
        printCollection("preselLeptons", preselLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update(">= 2 presel leptons",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        ">= 2 presel leptons", evtWeightRecorder.get(central_or_shift_main));

    // apply requirement on jets (incl. b-tagged jets) and hadronic taus on
    // preselection level
    if (!((int)selJets.size() >= minNumJets)) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str() << " FAILS selJets selection."
                  << std::endl;
        printCollection("selJets", selJets);
      }
      continue;
    }
    cutFlowTable.update(">= N jets",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        ">= N jets", evtWeightRecorder.get(central_or_shift_main));

    if (selBJets_loose.size() >= 2 || selBJets_medium.size() >= 1) {
      continue;
    }
    cutFlowTable.update("b-jet veto",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "b-jet veto", evtWeightRecorder.get(central_or_shift_main));

    //--- compute MHT and linear MET discriminant (met_LD)
    const RecoMEt met = metReader->read();
    const Particle::LorentzVector &metP4 = met.p4();
    Particle::LorentzVector mhtP4 =
        compMHT(fakeableLeptonsFull, fakeableHadTaus, selJets);
    // Particle::LorentzVector mhtP4 = compMHT(fakeableLeptons, {}, selJets);
    double met_LD = compMEt_LD(metP4, mhtP4);

    // double HT = compHT(fakeableLeptonsFull, fakeableHadTaus, selJets);
    // double HT = compHT(fakeableLeptons, {}, selJets);
    // double STMET = compSTMEt(fakeableLeptonsFull, fakeableHadTaus, selJets);
    // double STMET = compSTMEt(fakeableLeptons, {}, selJets, met.p4());

    //--- apply final event selection
    // require exactly two leptons passing tight selection criteria of final
    // event selection
    if (!(selLeptons.size() >= 2)) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str()
                  << " FAILS selLeptons selection." << std::endl;
        printCollection("selLeptons", selLeptons);
      }
      continue;
    }
    cutFlowTable.update(">= 2 sel leptons",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        ">= 2 sel leptons", evtWeightRecorder.get(central_or_shift_main));
    const RecoLepton *selLepton_lead = selLeptons[0];
    const Particle::LorentzVector& selLeptonP4_lead =
    selLepton_lead->cone_p4();
    const RecoLepton *selLepton_sublead = selLeptons[1];
    const Particle::LorentzVector& selLeptonP4_sublead =
    selLepton_sublead->cone_p4();
    const leptonChargeFlipGenMatchEntry &selLepton_genMatch =
        getLeptonChargeFlipGenMatch(leptonGenMatch_definitions, selLepton_lead,
                                    selLepton_sublead);

    // require exactly two leptons passing tight selection criteria, to avoid
    // overlap with other channels
    if (!(tightLeptonsFull.size() <= 2)) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str()
                  << " FAILS tightLeptons selection." << std::endl;
        printCollection("tightLeptonsFull", tightLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update("<= 2 tight leptons",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "<= 2 tight leptons", evtWeightRecorder.get(central_or_shift_main));

    // require that trigger paths match lepton flavor (for fakeable leptons)
    if (!((fakeableElectrons.size() >= 2 && (selTrigger_2e || selTrigger_1e)) ||
          (fakeableElectrons.size() >= 1 && fakeableMuons.size() >= 1 &&
           (selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
          (fakeableMuons.size() >= 2 && (selTrigger_2mu || selTrigger_1mu)))) {
      if (run_lumi_eventSelector) {
        std::cout
            << "event " << eventInfo.str()
            << " FAILS trigger selection for given fakeableLepton multiplicity."
            << std::endl;
        std::cout << " (#fakeableElectrons = " << fakeableElectrons.size()
                  << ", #fakeableMuons = " << fakeableMuons.size()
                  << ", selTrigger_2mu = " << selTrigger_2mu
                  << ", selTrigger_1e1mu = " << selTrigger_1e1mu
                  << ", selTrigger_2e = " << selTrigger_2e
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_1e = " << selTrigger_1e << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("trigger & fakeable lepton flavor matching",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "trigger & fakeable lepton flavor matching",
        evtWeightRecorder.get(central_or_shift_main));

    // Require that trigger paths match primary datasets,
    // to avoid that the same event is selected multiple times when processing
    // different primary datasets (PD). In case the same event passes the
    // triggers paths for more than one primary datasets, the event is selected
    // in the PD of highest priority only. The ranking of the PDs is as follows:
    // DoubleMuon, MuonEG, DoubleEG, SingleMuon, SingleElectron
    if (!isMC && !isDEBUG) {

      bool isTriggered_SingleMuon =
          isTriggered_1mu && fakeableMuons.size() >= 1;
      bool isTriggered_DoubleEG =
          isTriggered_2e && fakeableElectrons.size() >= 2;
      bool isTriggered_DoubleMuon =
          isTriggered_2mu && fakeableMuons.size() >= 2;
      bool isTriggered_MuonEG = isTriggered_1e1mu &&
                                fakeableElectrons.size() >= 1 &&
                                fakeableMuons.size() >= 1;

      bool selTrigger_SingleElectron = selTrigger_1e;
      bool selTrigger_SingleMuon = selTrigger_1mu;
      bool selTrigger_DoubleEG = selTrigger_2e;

      bool selTrigger_MuonEG = selTrigger_1e1mu;

      if (selTrigger_SingleElectron &&
          (isTriggered_SingleMuon || isTriggered_DoubleMuon ||
           isTriggered_MuonEG)) {
        if (run_lumi_eventSelector) {
          std::cout << "event " << eventInfo.str()
                    << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_SingleElectron = "
                    << selTrigger_SingleElectron
                    << ", isTriggered_SingleMuon = " << isTriggered_SingleMuon
                    << ", isTriggered_DoubleMuon = " << isTriggered_DoubleMuon
                    << ", isTriggered_MuonEG = " << isTriggered_MuonEG << ")"
                    << std::endl;
        }
        continue;
      }
      if (selTrigger_SingleElectron && isTriggered_DoubleEG &&
          era != Era::k2018) {
        if (run_lumi_eventSelector) {
          std::cout << "event " << eventInfo.str()
                    << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_SingleElectron = "
                    << selTrigger_SingleElectron
                    << ", isTriggered_DoubleEG = " << isTriggered_DoubleEG
                    << ")" << std::endl;
        }
        continue;
      }
      if (selTrigger_DoubleEG &&
          (isTriggered_DoubleMuon || isTriggered_MuonEG)) {
        if (run_lumi_eventSelector) {
          std::cout << "event " << eventInfo.str()
                    << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_DoubleEG = " << selTrigger_DoubleEG
                    << ", isTriggered_DoubleMuon = " << isTriggered_DoubleMuon
                    << ", isTriggered_MuonEG = " << isTriggered_MuonEG << ")"
                    << std::endl;
        }
        continue;
      }
      if (selTrigger_SingleMuon &&
          (isTriggered_DoubleEG || isTriggered_DoubleMuon ||
           isTriggered_MuonEG)) {
        if (run_lumi_eventSelector) {
          std::cout << "event " << eventInfo.str()
                    << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_SingleMuon = " << selTrigger_SingleMuon
                    << ", isTriggered_DoubleEG = " << isTriggered_DoubleEG
                    << ", isTriggered_DoubleMuon = " << isTriggered_DoubleMuon
                    << ", isTriggered_MuonEG = " << isTriggered_MuonEG << ")"
                    << std::endl;
        }
        continue;
      }
      if (selTrigger_MuonEG && isTriggered_DoubleMuon) {
        if (run_lumi_eventSelector) {
          std::cout << "event " << eventInfo.str()
                    << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_MuonEG = " << selTrigger_MuonEG
                    << ", isTriggered_DoubleMuon = " << isTriggered_DoubleMuon
                    << ")" << std::endl;
        }
        continue;
      }
    }
    cutFlowTable.update("trigger & dataset matching",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "trigger & dataset matching",
        evtWeightRecorder.get(central_or_shift_main));

    //--- apply HLT filter
    if (apply_hlt_filter) {
      const std::map<hltPathsE, bool> trigger_bits = {
          {hltPathsE::trigger_1e, selTrigger_1e},
          {hltPathsE::trigger_1mu, selTrigger_1mu},
          {hltPathsE::trigger_2e, selTrigger_2e},
          {hltPathsE::trigger_2mu, selTrigger_2mu},
          {hltPathsE::trigger_1e1mu, selTrigger_1e1mu},
      };
      if (!hltFilter(trigger_bits, fakeableLeptons, {})) {
        if (run_lumi_eventSelector || isDEBUG) {
          std::cout << "event " << eventInfo.str()
                    << " FAILS HLT filter matching\n";
        }
        continue;
      }
    }
    cutFlowTable.update("HLT filter matching",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "HLT filter matching", evtWeightRecorder.get(central_or_shift_main));

    if (isMC) {
      //--- compute event-level weight for data/MC correction of b-tagging
      //efficiency and mistag rate
      //   (using the method "Event reweighting using scale factors calculated
      //   with a tag and probe method",
      //    described on the BTV POG twiki
      //    https://twiki.cern.ch/twiki/bin/view/CMS/BTagShapeCalibration )
      evtWeightRecorder.record_btagWeight(selJets);
      if (btagSFRatioFacility) {
        evtWeightRecorder.record_btagSFRatio(btagSFRatioFacility,
                                             selJets.size());
      }

      if (isMC_EWK) {
        evtWeightRecorder.record_ewk_jet(selJets);
        evtWeightRecorder.record_ewk_bjet(selBJets_medium);
      }

      dataToMCcorrectionInterface->setLeptons(
          {selLepton_lead, selLepton_sublead}, true);

      //--- apply data/MC corrections for trigger efficiency
      evtWeightRecorder.record_leptonTriggerEff(dataToMCcorrectionInterface);

      //--- apply data/MC corrections for efficiencies for lepton to pass loose
      //identification and isolation criteria
      evtWeightRecorder.record_leptonIDSF_recoToLoose(
          dataToMCcorrectionInterface);

      //--- apply data/MC corrections for efficiencies of leptons passing the
      //loose identification and isolation criteria
      //    to also pass the tight identification and isolation criteria
      if (electronSelection >= kFakeable && muonSelection >= kFakeable) {
        // apply looseToTight SF to leptons matched to generator-level prompt
        // leptons and passing Tight selection conditions
        evtWeightRecorder.record_leptonIDSF_looseToTight(
            dataToMCcorrectionInterface, false);
      }
    }

    bool passesTight_lepton_lead = isMatched(*selLepton_lead, tightElectrons) ||
                                   isMatched(*selLepton_lead, tightMuons);
    bool passesTight_lepton_sublead =
        isMatched(*selLepton_sublead, tightElectrons) ||
        isMatched(*selLepton_sublead, tightMuons);

    if (leptonFakeRateInterface) {
      evtWeightRecorder.record_jetToLepton_FR_lead(leptonFakeRateInterface,
                                                   selLepton_lead);
      evtWeightRecorder.record_jetToLepton_FR_sublead(leptonFakeRateInterface,
                                                      selLepton_sublead);
    }

    if (!selectBDT) {
      if (applyFakeRateWeights == kFR_2lepton) {
        evtWeightRecorder.compute_FR_2l(passesTight_lepton_lead,
                                        passesTight_lepton_sublead);
      }
    }

    const bool failsLowMassVeto =
        isfailsLowMassVeto(preselLeptonsFullUncleaned);
    if (failsLowMassVeto) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str()
                  << " FAILS low mass lepton pair veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("m(ll) > 12 GeV",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "m(ll) > 12 GeV", evtWeightRecorder.get(central_or_shift_main));

    const double minPt_lead = 25.;
    const double minPt_sublead = 15.;
    if (!(selLepton_lead->cone_pt() > minPt_lead &&
          selLepton_sublead->cone_pt() > minPt_sublead)) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str()
                  << " FAILS lepton pT selection." << std::endl;
        std::cout << " (leading selLepton pT = " << selLepton_lead->pt()
                  << ", minPt_lead = " << minPt_lead
                  << ", subleading selLepton pT = " << selLepton_sublead->pt()
                  << ", minPt_sublead = " << minPt_sublead << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV",
        evtWeightRecorder.get(central_or_shift_main));

    bool failsTightChargeCut = false;
    for (std::vector<const RecoLepton *>::const_iterator lepton =
             fakeableLeptons.begin();
         lepton != fakeableLeptons.end(); ++lepton) {
      if ((*lepton)->is_electron()) {
        const RecoElectron *electron =
            dynamic_cast<const RecoElectron *>(*lepton);
        assert(electron);
        if (electron->tightCharge() < 2) {
          failsTightChargeCut = true;
          break;
        }
      } else if ((*lepton)->is_muon()) {
        const RecoMuon *muon = dynamic_cast<const RecoMuon *>(*lepton);
        assert(muon);
        if (muon->tightCharge() < 2) {
          failsTightChargeCut = true;
          break;
        }
      }
    }
    if (failsTightChargeCut) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str()
                  << " FAILS tight lepton charge requirement." << std::endl;
      }
      // if (!selectBDT)
      continue;
    }
    cutFlowTable.update("tight lepton charge",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "tight lepton charge", evtWeightRecorder.get(central_or_shift_main));

    bool isLeptonCharge_SS =
        selLepton_lead->charge() * selLepton_sublead->charge() > 0;
    bool isLeptonCharge_OS =
        selLepton_lead->charge() * selLepton_sublead->charge() < 0;
    if (leptonChargeSelection == kOS && isLeptonCharge_SS) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str()
                  << " FAILS lepton charge selection." << std::endl;
        std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
                  << ", subleading selLepton charge = "
                  << selLepton_sublead->charge()
                  << ", leptonChargeSelection = OS)" << std::endl;
      }
      continue;
    }
    if (leptonChargeSelection == kSS && isLeptonCharge_OS) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str()
                  << " FAILS lepton charge selection." << std::endl;
        std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
                  << ", subleading selLepton charge = "
                  << selLepton_sublead->charge()
                  << ", leptonChargeSelection = SS)" << std::endl;
      }
      continue;
    }
    if (leptonChargeSelection == kOS) {
      const double prob_chargeMisID_sum =
          chargeMisIdRate.get(selLepton_lead, selLepton_sublead);
      evtWeightRecorder.record_chargeMisIdProb(prob_chargeMisID_sum);

      // Karl: reject the event, if the applied probability of charge
      // misidentification is 0;
      //       we assume that the event weight was not 0 before including the
      //       charge flip weights Note that this can happen only if both
      //       selected leptons are muons (their misId prob is 0).
      if (prob_chargeMisID_sum == 0.) {
        if (run_lumi_eventSelector) {
          std::cout << "event " << eventInfo.str()
                    << " FAILS charge flip selection\n"
                       "(leading lepton charge (pdgId) = "
                    << selLepton_lead->charge() << " ("
                    << selLepton_lead->pdgId()
                    << "); "
                       "subleading lepton charge (pdgId) = "
                    << selLepton_sublead->charge() << " ("
                    << selLepton_sublead->pdgId() << "))\n";
        }
        continue;
      }
    }
    cutFlowTable.update(
        Form("sel lepton-pair %s charge", leptonChargeSelection_string.data()),
        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "sel lepton-pair OS/SS charge",
        evtWeightRecorder.get(central_or_shift_main));


// ################################################################################################################################################################################
// LHE particles
        double lhe_dEta_jj = -999;
        double lhe_dPhi_jj = -999;
        double lhe_m_jj = -1;
        double lhe_dR_jj = -1;
        double lhe_pt_lead = -1;
        double lhe_pt_sublead = -1;

    if (std::abs(lheParticles[2].eta()) < 4.7 and std::abs(lheParticles[3].eta()) < 4.7
      and lheParticles[2].pt() > 20 and lheParticles[3].pt() > 20){
        lhe_dEta_jj = lheParticles[2].eta()-lheParticles[3].eta();
        lhe_dPhi_jj = lheParticles[2].phi()-lheParticles[3].phi();
        lhe_m_jj = (lheParticles[2].p4() + lheParticles[3].p4()).mass();
        lhe_dR_jj = deltaR(lheParticles[2], lheParticles[3]);
        if (lheParticles[2].pt() > lheParticles[3].pt()){
          lhe_pt_lead = lheParticles[2].pt();
          lhe_pt_sublead = lheParticles[3].pt();
        }
        else{
          lhe_pt_lead = lheParticles[3].pt();
          lhe_pt_sublead = lheParticles[2].pt();
        }
    }

// Matched particles
    double matched_dEta_jj = -999;
    double matched_dPhi_jj = -999;
    double matched_m_jj = -1;
    double matched_dR_jj = -1;

    double matched_pt_lead = -1;
    double matched_pt_sublead = -1;

    math::PtEtaPhiMLorentzVector matched_vbf_jet1;
    math::PtEtaPhiMLorentzVector matched_vbf_jet2;
    double bestDR1 = 100000;
    double bestDR2 = 100000;
    int bestjet_id1 = 0;
    int bestjet_id2 = 0;
    for (size_t j=0; j < selJetsVBF.size(); j++){
      double dR1 = deltaR(lheParticles[2], selJetsVBF[j]->p4());
          if (dR1 < bestDR1){
              bestDR1 = dR1;
              bestjet_id1 = j;
          }
    }

    for (int j=0; j < static_cast<int>(selJetsVBF.size()); j++){
      double dR2 = deltaR(lheParticles[3], selJetsVBF[j]->p4());
          if (dR2 < bestDR2 and j != bestjet_id1){
              bestDR2 = dR2;
              bestjet_id2 = j;
          }
    }

    if (bestDR1<0.3 and bestDR2<0.3){
      matched_vbf_jet1 = selJetsVBF[bestjet_id1]->p4();
      matched_vbf_jet2 = selJetsVBF[bestjet_id2]->p4();
      if (std::abs(matched_vbf_jet1.eta()) < 4.7 and std::abs(matched_vbf_jet2.eta()) < 4.7
        and matched_vbf_jet1.pt() > 20 and matched_vbf_jet2.pt() > 20){
          matched_dEta_jj = matched_vbf_jet1.eta()-matched_vbf_jet2.eta();
          matched_dPhi_jj = matched_vbf_jet1.phi()-matched_vbf_jet2.phi();
          matched_m_jj = (matched_vbf_jet1 + matched_vbf_jet2).mass();
          matched_dR_jj = deltaR(matched_vbf_jet1, matched_vbf_jet2);
          if (matched_vbf_jet1.pt() > matched_vbf_jet2.pt()){
            matched_pt_lead = matched_vbf_jet1.pt();
            matched_pt_sublead = matched_vbf_jet2.pt();
          }
          else{
            matched_pt_lead = matched_vbf_jet2.pt();
            matched_pt_sublead = matched_vbf_jet1.pt();
          }
      }
  }


// New reco particles
    std::vector< const RecoJet *> VBFjets;
    double best_m_jj = -1.;
    double best_dEta_jj = -999;
    double best_dPhi_jj = -999;
    double best_dR_jj = -1;

    double best_pt_lead = -1;
    double best_pt_sublead = -1;

    math::PtEtaPhiMLorentzVector VBFjet1;
    math::PtEtaPhiMLorentzVector VBFjet2;

    int vbf_id1 = 0;
    int best_vbf_id1 = -999;
    int best_vbf_id2 = -999;
    bool isVBF = false;

    for (std::vector<const RecoJet *>::const_iterator selJetVBF1_ =
             selJetsVBF.begin(); selJetVBF1_ != selJetsVBF.end();
         ++selJetVBF1_) {
        int vbf_id2 = vbf_id1+1;
        for (std::vector<const RecoJet *>::const_iterator selJetVBF2_ =
               selJetVBF1_ + 1; selJetVBF2_ != selJetsVBF.end();++selJetVBF2_) {
            double m_jj_ = ((*selJetVBF1_)->p4() + (*selJetVBF2_)->p4()).mass();
            double dEta_jj_ = (*selJetVBF1_)->eta()-(*selJetVBF2_)->eta();
            double dPhi_jj_ = (*selJetVBF1_)->phi()-(*selJetVBF2_)->phi();
            double dR_jj_ = deltaR((*selJetVBF1_)->p4(), (*selJetVBF2_)->p4());
            double pt1_ = (*selJetVBF1_)->pt();
            double pt2_ = (*selJetVBF2_)->pt();
                if (m_jj_ > best_m_jj and std::abs((*selJetVBF1_)->eta()) < 4.7 and 
                  std::abs((*selJetVBF2_)->eta()) < 4.7 and pt1_ > 20 and pt2_ > 20){
                  best_m_jj = m_jj_;
                  best_dR_jj = dR_jj_;
                  best_dEta_jj = dEta_jj_;
                  best_dPhi_jj = dPhi_jj_;
                  VBFjet1= (*selJetVBF1_)->p4();
                  VBFjet2= (*selJetVBF2_)->p4();
                  best_vbf_id1 = vbf_id1;
                  best_vbf_id2 = vbf_id2;
                  isVBF = true;
                  if (pt1_ > pt2_){
                    best_pt_lead = pt1_;
                    best_pt_sublead = pt2_;
                  }
                  else{
                    best_pt_lead = pt2_;
                    best_pt_sublead = pt1_;
                  }
                  // if (best_m_jj > 400){
                  //   isVBF = true;
                  // }
                }
                vbf_id2++;
        }
      vbf_id1++;
    }


    double sum_m_lj = -1;
    if(best_vbf_id1 > -999 and best_vbf_id2 > -999){ 
        VBFjets.push_back(selJetsVBF[best_vbf_id1]);
        VBFjets.push_back(selJetsVBF[best_vbf_id2]);
        // std::cout << "m_lj: " << (selLepton_lead->p4() + selJetsVBF[best_vbf_id1]->p4()).mass()<< std::endl;
        sum_m_lj = (selLeptonP4_lead + selJetsVBF[best_vbf_id1]->p4()).mass() +
        (selLeptonP4_sublead + selJetsVBF[best_vbf_id1]->p4()).mass() +
        (selLeptonP4_lead + selJetsVBF[best_vbf_id2]->p4()).mass() +
        (selLeptonP4_sublead + selJetsVBF[best_vbf_id2]->p4()).mass();
  }


    double maxJetPt_vbf = -1;
    double minJetPt_vbf = -1;
    if (best_pt_lead > 0 and best_pt_sublead > 0){
    // if (VBFjets.size() == 2){
      maxJetPt_vbf = std::max(best_pt_lead,best_pt_sublead);
      minJetPt_vbf = std::min(best_pt_lead,best_pt_sublead);
    }


// Gen jets
    double genjet_dEta_jj = -999;
    double genjet_dPhi_jj = -999;
    double genjet_m_jj = -1;
    double genjet_dR_jj = -1;

    math::PtEtaPhiMLorentzVector gen_vbf_jet1;
    math::PtEtaPhiMLorentzVector gen_vbf_jet2;
    double gbestDR1 = 100000;
    double gbestDR2 = 100000;
    int gbestjet_id1 = 0;
    int gbestjet_id2 = 0;
    for (size_t j=0; j < genJets.size(); j++){
      double gdR1 = deltaR(lheParticles[2], genJets[j].p4());
      // std::cout << "dr1 out of loop: " << gdR1 << std::endl;
          if (gdR1 < gbestDR1){
              gbestDR1 = gdR1;
              gbestjet_id1 = j;
              // std::cout << "best dr1 in loop: " << gbestDR1 << std::endl;
          }
    }

    for (int j=0; j < static_cast<int>(genJets.size()); j++){
      double gdR2 = deltaR(lheParticles[3], genJets[j].p4());
          if (gdR2 < gbestDR2 and j != gbestjet_id1){
              gbestDR2 = gdR2;
              gbestjet_id2 = j;
          }
    }

    if (gbestDR1<0.3 and gbestDR2<0.3){
      gen_vbf_jet1 = genJets[gbestjet_id1].p4();
      gen_vbf_jet2 = genJets[gbestjet_id2].p4();
      if (std::abs(gen_vbf_jet1.eta()) < 4.7 and std::abs(gen_vbf_jet2.eta()) < 4.7
        and gen_vbf_jet1.pt() > 20 and gen_vbf_jet2.pt() > 20){
          genjet_dEta_jj = gen_vbf_jet1.eta()-gen_vbf_jet2.eta();
          genjet_dPhi_jj = gen_vbf_jet1.phi()-gen_vbf_jet2.phi();
          genjet_m_jj = (gen_vbf_jet1 + gen_vbf_jet2).mass();
          genjet_dR_jj = deltaR(gen_vbf_jet1, gen_vbf_jet2);
      }
  }



// W selection
// $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    std::vector<const RecoJetAK8 *> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);
    std::vector<const RecoJetAK8 *> selJetsAK8 =
        jetSelectorAK8(jet_ptrs_ak8, isHigherPt);
    jetSelectorAK8_Wjj.getSelector().set_leptons(
        {selLeptons[0], selLeptons[1]});
    std::vector<const RecoJetAK8 *> selJetsAK8_Wjj =
        jetSelectorAK8_Wjj(jet_ptrs_ak8, isHigherPt);
    std::vector<const RecoJetAK8 *> selJetsAK8_Wjj_selected;
    const RecoJetAK8 *selJetAK8_Wjj = nullptr;

    bool isEventBoosted = false;
    bool isEventSemiboosted = false;
    bool isEventResolved = false;
    Particle::LorentzVector selJetP4;
    Particle::LorentzVector selJetP4_2;
    double mass_jj_W = 0;
    double mass_jj_W2 = 0;

    for (size_t i = 0; i < selJetsAK8_Wjj.size();
         i++) {
      if (selJetsAK8_Wjj[i] && selJetsAK8_Wjj[i]->subJet1() &&
          selJetsAK8_Wjj[i]->subJet2()) {
        if (deltaR(VBFjet1, selJetsAK8_Wjj[i]->subJet1()->p4()) != 0 and deltaR(VBFjet2, selJetsAK8_Wjj[i]->subJet1()->p4()) != 0
          and deltaR(VBFjet1, selJetsAK8_Wjj[i]->subJet2()->p4()) != 0 and deltaR(VBFjet2, selJetsAK8_Wjj[i]->subJet2()->p4()) != 0){
            selJetsAK8_Wjj_selected.push_back(selJetsAK8_Wjj[i]);
        } // Add suitable jets to selJetsAK8_Wjj_selected
      }
    }

    // for (size_t i = 0; i < selJetsAK8_Wjj.size();
    //      i++) { // Loop over all selJetsAK8
    //   if (selJetsAK8_Wjj[i] && selJetsAK8_Wjj[i]->subJet1() &&
    //       selJetsAK8_Wjj[i]->subJet2()) {
    //     selJetsAK8_Wjj_selected.push_back(
    //         selJetsAK8_Wjj[i]); // Add suitable jets to selJetsAK8_Wjj_selected
    //                             // if condition is satisfied
    //   }
    // }

    std::vector<const RecoJet *> selJets_c;
    for (size_t i = 0; i < selJets.size(); i++) {
        if (deltaR(VBFjet1, selJets[i]->p4()) != 0 and deltaR(VBFjet2, selJets[i]->p4()) != 0){
          selJets_c.push_back(selJets[i]);
        }
    }


    math::PtEtaPhiMLorentzVector selJet1P4;
    math::PtEtaPhiMLorentzVector selJet2P4;
    math::PtEtaPhiMLorentzVector selJet3P4;
    math::PtEtaPhiMLorentzVector selJet4P4;
    // std::cout << "seljets: " << selJets.size() << std::endl;
    // std::cout << "seljets cleaned: " << selJets_c.size() << std::endl;
    // std::cout << "AK8 jets: " << selJetsAK8.size() << std::endl;
    // std::cout << "AK8 jets Wjj: " << selJetsAK8_Wjj.size()<< std::endl;
    // std::cout << "AK8 jets Wjj selected: " << selJetsAK8_Wjj_selected.size()<< std::endl;
    if (selJetsAK8_Wjj_selected.size() >= 2) { // boosted category
      selJetP4 = (selJetsAK8_Wjj_selected[0]->subJet1()->p4() +
                  selJetsAK8_Wjj_selected[0]->subJet2()->p4());
      selJetP4_2 = (selJetsAK8_Wjj_selected[1]->subJet1()->p4() +
                  selJetsAK8_Wjj_selected[1]->subJet2()->p4());
      // std::cout << "----------------------boosted----------------------------" << std::endl;
      // std::cout << "AK8 1: " << selJetsAK8_Wjj_selected[0]->p4()<< std::endl;
      // std::cout << "AK8 1 subjet 1: " << selJetsAK8_Wjj_selected[0]->subJet1()->p4()<< std::endl;
      // std::cout << "AK8 1 subjet 2: " << selJetsAK8_Wjj_selected[0]->subJet2()->p4()<< std::endl;
      // std::cout << "AK8 2: " << selJetsAK8_Wjj_selected[1]->p4()<< std::endl;
      // std::cout << "AK8 2 subjet 1: " << selJetsAK8_Wjj_selected[1]->subJet1()->p4()<< std::endl;
      // std::cout << "AK8 2 subjet 2: " << selJetsAK8_Wjj_selected[1]->subJet2()->p4()<< std::endl;
      // std::cout << "1st W: " << selJetP4 << std::endl;
      // std::cout << "2nd W: " << selJetP4_2 << std::endl;
      // std::cout << "__________________________________________" << std::endl;
      isEventBoosted = true;
      // selJetP4 = (selJetsAK8_Wjj_selected[0]->subJet1()->p4() +
      //             selJetsAK8_Wjj_selected[0]->subJet2()->p4() +
      //             selJetsAK8_Wjj_selected[1]->subJet1()->p4() +
      //             selJetsAK8_Wjj_selected[1]
      //                 ->subJet2()
      //                 ->p4());
    } else if (selJetsAK8_Wjj_selected.size() == 1 &&
               selJets_c.size() >= 1) { // semiboosted category
      std::vector<const RecoSubjetAK8 *> selSubjetsAK8 = {
          selJetsAK8_Wjj_selected[0]->subJet1(),
          selJetsAK8_Wjj_selected[0]->subJet2()};
      double dm_min = 9999.;
      size_t idxWJet1 = 9999;
      size_t idxWJet2 = 9999;
      for (size_t iJet1 = 0; iJet1 < selJets_c.size();
           iJet1++) {
        const RecoJet *jet1 =
            selJets_c[iJet1];
        if (hasOverlapJets(jet1, selSubjetsAK8))
          continue;

        for (size_t iJet2 = iJet1 + 1; iJet2 < selJets_c.size();
             iJet2++) {
          const RecoJet *jet2 =
              selJets_c[iJet2];
          if (hasOverlapJets(jet2, selSubjetsAK8))
            continue;

          double dm = std::fabs((jet1->p4() + jet2->p4()).mass() - w_mass);
          if (dm < dm_min) {
            dm_min = dm;
            idxWJet1 = iJet1;
            idxWJet2 = iJet2;
          }
        }
      }
      if (idxWJet1 != 9999 && idxWJet2 != 9999) { // for 2 AK4 jets case
        selJetP4 = (selJetsAK8_Wjj_selected[0]->subJet1()->p4() +
                    selJetsAK8_Wjj_selected[0]->subJet2()->p4());
        selJetP4_2 = (selJets_c[idxWJet1]->p4() +
                    selJets_c[idxWJet2]->p4());
      // std::cout << "---------------semi-boosted----------------" << std::endl;
      // std::cout << "AK8: " << selJetsAK8_Wjj_selected[0]->p4()<< std::endl;
      // std::cout << "AK8 1 subjet 1: " << selJetsAK8_Wjj_selected[0]->subJet1()->p4()<< std::endl;
      // std::cout << "AK8 1 subjet 2: " << selJetsAK8_Wjj_selected[0]->subJet2()->p4()<< std::endl;
      // std::cout << "Seljet 1: " << selJets_c[idxWJet1]->p4()<< std::endl;
      // std::cout << "Seljet 2: " << selJets_c[idxWJet2]->p4()<< std::endl;
      // std::cout << "1st W: " << selJetP4 << std::endl;
      // std::cout << "2nd W: " << selJetP4_2 << std::endl;
      // std::cout << "___________________________________________" << std::endl;
        // selJetP4 = (selJetsAK8_Wjj_selected[0]->subJet1()->p4() +
        //             selJetsAK8_Wjj_selected[0]->subJet2()->p4() +
        //             selJets[idxWJet1]->p4() +
        //             selJets[idxWJet2]->p4());
        isEventSemiboosted = true;
      } else if (!hasOverlapJets(selJets_c[0], selSubjetsAK8)) {
        selJetP4 = (selJetsAK8_Wjj_selected[0]->subJet1()->p4() +
                    selJetsAK8_Wjj_selected[0]->subJet2()->p4());
        selJetP4_2 = selJets_c[0]->p4();
        // selJetP4 = (selJetsAK8_Wjj_selected[0]->subJet1()->p4() +
        //             selJetsAK8_Wjj_selected[0]->subJet2()->p4() +
        //             selJets[0]->p4());
        isEventSemiboosted = true;
      }
    } else if (selJetsAK8_Wjj_selected.size() == 0 &&
               selJets_c.size() >= 1) { // resolved category
      mass_jj_W = 0;
      mass_jj_W2 = 0;
      for (std::vector<const RecoJet *>::const_iterator selJet1_W = selJets_c.begin();
           selJet1_W != selJets_c.end(); ++selJet1_W) {
        for (std::vector<const RecoJet *>::const_iterator selJet2_W = selJet1_W + 1;
             selJet2_W != selJets_c.end();++selJet2_W) {
          double mass_jj = ((*selJet1_W)->p4() + (*selJet2_W)->p4()).mass();
          if ((std::fabs(mass_jj - w_mass) < std::fabs(mass_jj_W - w_mass) &&
               mass_jj < 120) || mass_jj_W == 0) {
            mass_jj_W = mass_jj;
            selJet1P4 = (*selJet1_W)->p4();
            selJet2P4 = (*selJet2_W)->p4();
            // std::cout << "---------------resolved----------------" << std::endl;
            // std::cout << "selJet1P4: " << (*selJet1_W)->p4()<< std::endl;
            // std::cout << "selJet2P4: " << (*selJet2_W)->p4()<< std::endl;
            selJetP4 = (*selJet1_W)->p4() + (*selJet2_W)->p4();
            // std::cout << "1st W: " << selJetP4 << std::endl;

            // Off-shell W
            for (std::vector<const RecoJet *>::const_iterator selJet3_W =
                     selJets_c.begin();selJet3_W != selJets_c.end();++selJet3_W) {
              for (std::vector<const RecoJet *>::const_iterator selJet4_W =
                       selJet3_W + 1;
                   selJet4_W != selJets_c.end(); ++selJet4_W) {
                if (std::abs(deltaR((*selJet1_W)->p4(), (*selJet3_W)->p4())) ==
                        0 or
                    std::abs(deltaR((*selJet2_W)->p4(), (*selJet3_W)->p4())) ==
                        0 or
                    std::abs(deltaR((*selJet1_W)->p4(), (*selJet4_W)->p4())) ==
                        0 or
                    std::abs(deltaR((*selJet2_W)->p4(), (*selJet4_W)->p4())) ==
                        0) {
                  continue;
                }
                double mass_jj2 = ((*selJet3_W)->p4() + (*selJet4_W)->p4()).mass();
                if (std::fabs(mass_jj2 - 40) < std::fabs(mass_jj_W2 - 40) || mass_jj_W2 == 0) {
                  selJet3P4 = (*selJet3_W)->p4();
                  selJet4P4 = (*selJet4_W)->p4();
                  mass_jj_W2 = mass_jj2;
                  selJetP4_2 = (*selJet3_W)->p4() + (*selJet4_W)->p4();
                  // std::cout << "selJet3P4: " << (*selJet3_W)->p4()<< std::endl;
                  // std::cout << "selJet4P4: " << (*selJet4_W)->p4()<< std::endl;
                  // std::cout << "2nd W: " << selJetP4_2 << std::endl;
                  // std::cout << "___________________________________________" << std::endl;
                }
              }
            }
          }
        }
      }
      isEventResolved = true;
    }

    double sum_mass_W = mass_jj_W + mass_jj_W2;

    if (isEventBoosted) {
      cutFlowTable.update("event category criteria passed: boosted",
                          evtWeightRecorder.get(central_or_shift_main));
      cutFlowHistManager->fillHistograms(
          "event category criteria passed: boosted",
          evtWeightRecorder.get(central_or_shift_main));
    }
    if (isEventSemiboosted) {
      cutFlowTable.update("event category criteria passed: semiboosted",
                          evtWeightRecorder.get(central_or_shift_main));
      cutFlowHistManager->fillHistograms(
          "event category criteria passed: semiboosted",
          evtWeightRecorder.get(central_or_shift_main));
    }
    if (isEventResolved) {
      cutFlowTable.update("event category criteria passed: resolved",
                          evtWeightRecorder.get(central_or_shift_main));
      cutFlowHistManager->fillHistograms(
          "event category criteria passed: resolved",
          evtWeightRecorder.get(central_or_shift_main));
    }

    if (!(isEventBoosted || isEventSemiboosted || isEventResolved))
      continue;

    cutFlowTable.update(
        "event category criteria passed: boosted / semiboosted / resolved",
        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "event category criteria passed: boosted / semiboosted / resolved",
        evtWeightRecorder.get(central_or_shift_main));

    //    const bool failsZbosonMassVeto =
    //    isfailsZbosonMassVeto(preselLeptonsFull, false, isDEBUG) || (
    //        selLepton_lead->is_electron() &&
    //        selLepton_sublead->is_electron() &&
    //        isfailsZbosonMassVeto({ selLepton_lead, selLepton_sublead }, true,
    //        isDEBUG)
    //      )
    //    ;
    //    if ( failsZbosonMassVeto ) {
    //      if ( run_lumi_eventSelector ) {
    // std::cout << "event " << eventInfo.str() << " FAILS Z-boson veto." <<
    // std::endl;
    //      }
    //      continue;
    //    }
    //    cutFlowTable.update("Z-boson mass veto",
    //    evtWeightRecorder.get(central_or_shift_main));
    //    cutFlowHistManager->fillHistograms("Z-boson mass veto",
    //    evtWeightRecorder.get(central_or_shift_main));

    const bool failsHtoZZVeto = isfailsHtoZZVeto(preselLeptonsFull);
    if (failsHtoZZVeto) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str() << " FAILS H->ZZ*->4l veto."
                  << std::endl;
      }
      continue;
    }
    cutFlowTable.update("H->ZZ*->4l veto",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "H->ZZ*->4l veto", evtWeightRecorder.get(central_or_shift_main));

    if (!(selLepton_lead->is_muon() || selLepton_sublead->is_muon() ||
          met_LD >= 30. || best_m_jj < 400)) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str()
                  << " FAILS MET LD selection.\n"
                     " (LD = "
                  << met_LD << ")\n";
      }
      continue;
    }
    cutFlowTable.update("met LD", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "met LD", evtWeightRecorder.get(central_or_shift_main));

    if (apply_met_filters) {
      if (!metFilterSelector(metFilters)) {
        if (run_lumi_eventSelector) {
          std::cout << "event " << eventInfo.str() << " FAILS MEt filters."
                    << std::endl;
        }
        continue;
      }
    }
    cutFlowTable.update("MEt filters",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "MEt filters", evtWeightRecorder.get(central_or_shift_main));

    bool failsSignalRegionVeto = false;
    if (isMCClosure_e || isMCClosure_m) {
      bool applySignalRegionVeto_lepton =
          (isMCClosure_e && countFakeElectrons(selLeptons) >= 1) ||
          (isMCClosure_m && countFakeMuons(selLeptons) >=
                                1); // Revet to the old MCClosure condition
      if (applySignalRegionVeto_lepton && tightLeptons.size() >= 2)
        failsSignalRegionVeto = true;
    } else if (electronSelection == kFakeable || muonSelection == kFakeable) {
      if (tightLeptons.size() >= 2)
        failsSignalRegionVeto = true;
    }
    if (failsSignalRegionVeto) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str()
                  << " FAILS overlap w/ the SR: "
                     "# tight leptons = "
                  << tightLeptons.size() << " >= 2\n";
        printCollection("tightLeptons", tightLeptons);
      }
      continue; // CV: avoid overlap with signal region
    }
    cutFlowTable.update("signal region veto",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
        "signal region veto", evtWeightRecorder.get(central_or_shift_main));


    if (best_m_jj < 400) {
      if (run_lumi_eventSelector) {
        std::cout << "event " << eventInfo.str()
                  << " FAILS VBF pair  selection." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("VBF requirement",
                        evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(
          "VBF requirement", evtWeightRecorder.get(central_or_shift_main));

    if (blacklist && (*blacklist)(eventInfo)) {
      continue;
    }

    // compute signal extraction observables
    double dihiggsVisMass_sel =
        (selJetP4 + selJetP4_2 + selLepton_lead->cone_p4() + selLepton_sublead->cone_p4())
            .mass();
    double dihiggsMass_wMet_sel = (selJetP4 + selJetP4_2 + selLepton_lead->cone_p4() +
                                   selLepton_sublead->cone_p4() + met.p4()).mass();

    std::vector< math::PtEtaPhiMLorentzVector > Ws;
    Ws.push_back(selJetP4);
    Ws.push_back(selJetP4_2);

    // Higgs Stuff
    math::PtEtaPhiMLorentzVector Higgs1;
    math::PtEtaPhiMLorentzVector Higgs2;
    double dR_h1h2 = -1;
    double pT_h1 = -1;
    double pT_h2 = -1;

    double mass_h1 = 9999;
    double mass_h2 = 9999;
    int bestW_id1 = 0;
    int bestW_id2 = 0;

    // the highest pt sum
    for (size_t i = 0; i < Ws.size(); i++) {
        double mass_1 = (Ws[i] + selLepton_lead->cone_p4()).mass();
        double h1_pt = (Ws[i] + selLepton_lead->cone_p4()).pt();
      if (h1_pt > pT_h1){
      // if (mass_1< mass_h1){
          pT_h1 = h1_pt;
          mass_h1 = mass_1;
          bestW_id1 = i;
      }
    }

    for (int i = 0; i < static_cast<int>(Ws.size()); i++) {
        double mass_2 = (Ws[i] + selLepton_sublead->cone_p4()).mass();
        double h2_pt = (Ws[i] + selLepton_sublead->cone_p4()).pt();
      if (h2_pt > pT_h2 and i != bestW_id1){
      // if (mass_2 < mass_h2 and i != bestW_id1){
        pT_h2 = h2_pt;
        mass_h2 = mass_2;
        bestW_id2 = i;
      }
    }

    Higgs1 = (Ws[bestW_id1] + selLepton_lead->cone_p4());
    Higgs2 = (Ws[bestW_id2] + selLepton_sublead->cone_p4());
    dR_h1h2 = deltaR(Higgs1, Higgs2);

    double dR_h1_j1 = -1;
    double dR_h1_j2 = -1;
    double dR_h2_j1 = -1;
    double dR_h2_j2 = -1;

    dR_h1_j1 = deltaR(Higgs1, VBFjet1);
    dR_h1_j2 = deltaR(Higgs1, VBFjet2);
    dR_h2_j1 = deltaR(Higgs2, VBFjet1);
    dR_h2_j2 = deltaR(Higgs2, VBFjet2);

    double vbf_eta_avg = (VBFjet1.eta() + VBFjet2.eta())/2;
    double H1H2_centrality = std::exp(-pow(((Higgs1.eta()-vbf_eta_avg)/(VBFjet1.eta()-VBFjet2.eta())),2)-
                            pow(((Higgs2.eta()-vbf_eta_avg)/(VBFjet1.eta()-VBFjet2.eta())),2));

    double vbfj1_cosphi = cos(VBFjet1.phi());
    double vbfj2_cosphi = cos(VBFjet2.phi());


    // double jetMass_sel = mass_jj_W;
    // double leptonPairMass_sel = (selLepton_lead->cone_p4() +
    // selLepton_sublead->cone_p4()).mass(); double leptonPairCharge_sel =
    // selLepton_lead->charge() + selLepton_sublead->charge();
    // //--- compute variables BDTs used to discriminate . . .
    const double mindR_vbfjet_lep1  = comp_mindr_jet(*selLepton_lead, VBFjets);
    const double mindR_vbfjet_lep2  = comp_mindr_jet(*selLepton_sublead, VBFjets);
    // std::cout << "vbf jets: " << VBFjets.size() << std::endl;


    double mindR_vbfJet_W1 =-1;
    double maxdR_vbfJet_W1 = -1;
    if(VBFjets.size()==2){
      double dr_j1_W = deltaR(selJetP4, VBFjet1);
      double dr_j2_W = deltaR(selJetP4, VBFjet2);
      mindR_vbfJet_W1 = std::min(dr_j1_W, dr_j2_W);
      maxdR_vbfJet_W1 = std::max(dr_j1_W, dr_j2_W);
    }

    double mindR_vbfjet_lep = std::min(mindR_vbfjet_lep1, mindR_vbfjet_lep2);
    double maxdR_vbfjet_lep = std::max(mindR_vbfjet_lep1, mindR_vbfjet_lep2);


    Particle::LorentzVector llP4 = selLeptonP4_lead + selLeptonP4_sublead; 
    double pT_sum = -1;
    if (best_pt_lead > 0 and best_pt_sublead > 0){
      pT_sum = llP4.pt() + best_pt_lead + best_pt_sublead;
    }
    double m_ll = llP4.mass();
    // double dR_ll = deltaR(selLeptonP4_lead,selLeptonP4_sublead);
    // double pT_ll = llP4.pt();
    // double pT_llMEt = (llP4 + metP4).pt();
    // double Smin_llMEt = comp_Smin(llP4, metP4.px(), metP4.py());


//Older stuff below

    // int nJet_vbf = selJetsVBF.size();

    double vbf_dEta_jj = -999.;
    double vbf_m_jj = -1.;
    double vbf_dR_jj = -1;
    // bool isVBF = false;

    for (std::vector<const RecoJet *>::const_iterator selJetVBF1 =
             selJetsVBF.begin();
         selJetVBF1 != selJetsVBF.end();
         ++selJetVBF1) { // Loop over all selected jet 1s
      if (std::abs(deltaR((*selJetVBF1)->p4(), selJet1P4)) == 0)
        continue;
      if (std::abs(deltaR((*selJetVBF1)->p4(), selJet2P4)) == 0)
        continue;
      if (std::abs(deltaR((*selJetVBF1)->p4(), selJet3P4)) == 0)
        continue;
      if (std::abs(deltaR((*selJetVBF1)->p4(), selJet4P4)) == 0)
        continue;
      for (std::vector<const RecoJet *>::const_iterator selJetVBF2 =
               selJetVBF1 + 1;
           selJetVBF2 != selJetsVBF.end();
           ++selJetVBF2) { // Loop over all selected jet 2s
        if (deltaR((*selJetVBF1)->p4(),(*selJetVBF2)->p4())<0.1) std::cout<< (*selJetVBF1)->p4() << " " << (*selJetVBF2)->p4() << std::endl;
        if (std::abs(deltaR((*selJetVBF2)->p4(), selJet1P4)) == 0)
          continue;
        if (std::abs(deltaR((*selJetVBF2)->p4(), selJet2P4)) == 0)
          continue;
        if (std::abs(deltaR((*selJetVBF2)->p4(), selJet3P4)) == 0)
          continue;
        if (std::abs(deltaR((*selJetVBF2)->p4(), selJet4P4)) == 0)
          continue;
        double dEta_jj = (*selJetVBF1)->eta()-(*selJetVBF2)->eta();
        double dR_jj = deltaR((*selJetVBF1)->p4(), (*selJetVBF2)->p4());
         // Calculate deltaEta between the 2 jets
        double m_jj = ((*selJetVBF1)->p4() + (*selJetVBF2)->p4())
                          .mass();         // Calculate the invariant mass
        // if (dEta_jj > 4. && m_jj > 500.) { // If deltaE > 4 and inv mass > 500
        //   if (dEta_jj > vbf_dEta_jj)
        //     vbf_dEta_jj = dEta_jj; // If new deltaEta is bigger than old then
        //                            // replace the old one

          if (m_jj > vbf_m_jj and dEta_jj > vbf_dEta_jj){
            vbf_m_jj = m_jj;
            vbf_dEta_jj = dEta_jj;
            vbf_dR_jj = dR_jj;
          // isVBF = true;
            //std::cout<< (*selJetVBF1)->p4() << " " << (*selJetVBF2)->p4() << std::endl;

            // if (dEta_jj < 0.1) {
            //   std::cout<< "#########################################" << std::endl;
            //   std::cout<< (*selJetVBF1)->p4() << " " << (*selJetVBF2)->p4() << std::endl;
            //   std::cout<< "#########################################" << std::endl;
            // }
          } 
      }
    //std::cout<< "*************************************************************" << std::endl;
    }
    // std::cout<< "#########################################" << std::endl;
    // std::cout<< best_m_jj << "new mass|||| old mass" << vbf_m_jj << std::endl;
    // std::cout<< "_________________________________________" << std::endl;

    // //Gathering final BDT Inputs

    AllVars_Map["gen_mHH"]                                   =       250.; //
    // setting a Dummy value which will be reset depending on mass hypothesis

    AllVars_Map["dihiggsVisMass_sel"] =              dihiggsVisMass_sel;
    AllVars_Map["dihiggsMass_wMet_sel"] =            dihiggsMass_wMet_sel;
    // AllVars_Map["jetMass_sel"] =                     jetMass_sel;
    // AllVars_Map["leptonPairMass_sel"] =              std::min(250.,
    // leptonPairMass_sel); AllVars_Map["leptonPairCharge_sel"] =
    // leptonPairCharge_sel; AllVars_Map["met"] = std::min(250., metP4.pt());
    // AllVars_Map["mht"] =                             std::min(250.,
    // mhtP4.pt()); AllVars_Map["met_LD"] = std::min(250., met_LD);
    // AllVars_Map["HT"] =                              std::min(1000., HT);
    // AllVars_Map["STMET"] =                           std::min(1000., STMET);
    AllVars_Map["evtWeight"] = evtWeightRecorder.get(central_or_shift_main);
    // AllVars_Map["lep1_pt"] =                         std::min(120.,
    // selLepton_lead->pt()); AllVars_Map["lep1_conePt"] = std::min(120.,
    // comp_lep_conePt(*selLepton_lead)); AllVars_Map["lep1_eta"] =
    // selLepton_lead->eta();
    AllVars_Map["mindR_vbfjet_lep1"] = std::min(10., mindR_vbfjet_lep1);
    //AllVars_Map["mT_lep1"] = std::min(150.,
    // comp_MT_met(selLepton_lead, met.pt(), met.phi())); AllVars_Map["lep2_pt"]
    // =                         std::min(120., selLepton_sublead->pt());
    // AllVars_Map["lep2_conePt"] =                     std::min(120.,
    // comp_lep_conePt(*selLepton_sublead)); AllVars_Map["lep2_eta"] =
    // selLepton_sublead->eta();
    AllVars_Map["mindR_vbfjet_lep2"] = std::min(10., mindR_vbfjet_lep2);
    //AllVars_Map["mT_lep2"] = std::min(150.,
    // comp_MT_met(selLepton_sublead, met.pt(), met.phi()));
    // AllVars_Map["dR_ll"] =                           dR_ll;
    // AllVars_Map["pT_ll"] =                           pT_ll;
    AllVars_Map["maxJetEta_vbf"] = comp_maxAbsEta_jet(VBFjets);
    AllVars_Map["minJetEta_vbf"] = comp_minAbsEta_jet(VBFjets);
    // AllVars_Map["max_lep_eta"] = TMath::Max(std::abs(selLepton_lead ->
    // eta()), std::abs(selLepton_sublead -> eta())); AllVars_Map["pT_llMEt"] =
    // pT_llMEt; AllVars_Map["Smin_llMEt"] =                      Smin_llMEt;
    AllVars_Map["vbf_dEta_jj"] =                     vbf_dEta_jj;
    AllVars_Map["vbf_m_jj"] =                        vbf_m_jj;
    AllVars_Map["vbf_dR_jj"] =                        vbf_dR_jj;
    // AllVars_Map["nJet"] = comp_n_jet25_recl(selJets);
    // AllVars_Map["nJet_vbf"] = selJetsVBF.size();

    AllVars_Map["lhe_dEta_jj"] = lhe_dEta_jj;
    AllVars_Map["lhe_dPhi_jj"] = lhe_dPhi_jj;
    AllVars_Map["lhe_m_jj"] = lhe_m_jj;
    AllVars_Map["lhe_dR_jj"] = lhe_dR_jj;

    AllVars_Map["matched_dEta_jj"] = matched_dEta_jj;
    AllVars_Map["matched_dPhi_jj"] = matched_dPhi_jj;
    AllVars_Map["matched_m_jj"] = matched_m_jj;
    AllVars_Map["matched_dR_jj"] = matched_dR_jj;

    AllVars_Map["best_dEta_jj"] = best_dEta_jj;
    AllVars_Map["best_dPhi_jj"] = best_dPhi_jj;
    AllVars_Map["best_m_jj"] = best_m_jj;
    AllVars_Map["best_dR_jj"] = best_dR_jj;

    AllVars_Map["lhe_pt_lead"] = lhe_pt_lead;
    AllVars_Map["lhe_pt_sublead"] = lhe_pt_sublead;
    AllVars_Map["matched_pt_lead"] = matched_pt_lead;
    AllVars_Map["matched_pt_sublead"] = matched_pt_sublead;
    AllVars_Map["best_pt_lead"] = best_pt_lead;
    AllVars_Map["best_pt_sublead"] = best_pt_sublead;

    AllVars_Map["genjet_dEta_jj"] = genjet_dEta_jj;
    AllVars_Map["genjet_dPhi_jj"] = genjet_dPhi_jj;
    AllVars_Map["genjet_m_jj"] = genjet_m_jj;
    AllVars_Map["genjet_dR_jj"] = genjet_dR_jj;

    AllVars_Map["mass_jj_W"] = mass_jj_W;
    AllVars_Map["mass_jj_W2"] = mass_jj_W2;
    AllVars_Map["sum_mass_W"] = sum_mass_W;

    AllVars_Map["sum_m_lj"] = sum_m_lj;
    AllVars_Map["pT_sum"] = pT_sum;
    AllVars_Map["m_ll"] = m_ll;
    AllVars_Map["isVBF"] = isVBF;

    AllVars_Map["maxJetPt_vbf"] = maxJetPt_vbf;
    AllVars_Map["minJetPt_vbf"] = minJetPt_vbf;
    AllVars_Map["mindR_vbfJet_W1"] = mindR_vbfJet_W1;
    AllVars_Map["maxdR_vbfJet_W1"] = maxdR_vbfJet_W1;
    AllVars_Map["mindR_vbfjet_lep"] = mindR_vbfjet_lep;
    AllVars_Map["maxdR_vbfjet_lep"] = maxdR_vbfjet_lep;

    AllVars_Map["dR_h1h2"] = dR_h1h2;
    AllVars_Map["pT_h1"] = pT_h1;
    AllVars_Map["pT_h2"] = pT_h2;
    AllVars_Map["dR_h1_j1"] = dR_h1_j1;
    AllVars_Map["dR_h1_j2"] = dR_h1_j2;
    AllVars_Map["dR_h2_j1"] = dR_h2_j1;
    AllVars_Map["dR_h2_j2"] = dR_h2_j2;
    AllVars_Map["mass_h1"] = mass_h1;
    AllVars_Map["mass_h2"] = mass_h2;

    AllVars_Map["H1H2_centrality"] = H1H2_centrality;
    AllVars_Map["vbfj1_cosphi"] = vbfj1_cosphi;
    AllVars_Map["vbfj2_cosphi"] = vbfj2_cosphi;

    // AllVars_Map["nLep"] =                            selLeptons.size();

    // std::map<std::string, double> BDTInputs_spin2 =
    // InitializeInputVarMap(AllVars_Map, BDTInputVariables_spin2, false);
    // std::map<std::string, double> BDTInputs_spin0 =
    // InitializeInputVarMap(AllVars_Map, BDTInputVariables_spin0, false);
    // std::map<std::string, double> BDTInputs_nonRes =
    // InitializeInputVarMap(AllVars_Map, BDTInputVariables_nonRes, true);

    // std::vector<double> nonResBase_params;
    // nonResBase_params.push_back(0.);

    // BDTOutput_Map_spin2 = CreateResonantBDTOutputMap(gen_mHH, BDT_spin2,
    // BDTInputs_spin2, eventInfo.event, "_spin2"); BDTOutput_Map_spin0 =
    // CreateResonantBDTOutputMap(gen_mHH, BDT_spin0, BDTInputs_spin0,
    // eventInfo.event, "_spin0"); BDTOutput_Map_nonRes =
    // CreateNonResonantBDTOutputMap(nonRes_BMs, BDT_nonRes, BDTInputs_nonRes,
    // eventInfo.event, hhWeight_couplings);

    // double lep1_conePt = comp_lep_conePt(*selLepton_lead);
    // double mT_lep1 = comp_MT_met(selLepton_lead, met.pt(), met.phi());
    // //
    // double lep2_conePt = comp_lep_conePt(*selLepton_sublead);
    // double mT_lep2 = comp_MT_met(selLepton_sublead, met.pt(), met.phi());
    // //
    // double max_lep_eta = TMath::Max(std::abs(selLepton_lead -> eta()),
    // std::abs(selLepton_sublead -> eta()));
    double maxJetEta_vbf = comp_maxAbsEta_jet(VBFjets);
    double minJetEta_vbf = comp_minAbsEta_jet(VBFjets);

    //--- retrieve gen-matching flags
    std::vector<const GenMatchEntry *> genMatches =
        genMatchInterface.getGenMatch(selLeptons);

    //--- fill histograms with events passing final selection
    for (const std::string &central_or_shift : central_or_shifts_local) {
      const double evtWeight = evtWeightRecorder.get(central_or_shift);
      const bool skipFilling = central_or_shift != central_or_shift_main;
      for (const GenMatchEntry *genMatch : genMatches) {
        selHistManagerType *selHistManager =
            selHistManagers[central_or_shift][genMatch->getIdx()];
        assert(selHistManager);
        if (!skipFilling) {
          selHistManager->electrons_->fillHistograms(selElectrons, evtWeight);
          if (selElectrons.size() >= 1) {
            selHistManager->leadElectron_->fillHistograms({selElectrons[0]},
                                                          evtWeight);
          }
          if (selElectrons.size() >= 2) {
            selHistManager->subleadElectron_->fillHistograms({selElectrons[1]},
                                                             evtWeight);
          }
          selHistManager->muons_->fillHistograms(selMuons, evtWeight);
          if (selMuons.size() >= 1) {
            selHistManager->leadMuon_->fillHistograms({selMuons[0]}, evtWeight);
          }
          if (selMuons.size() >= 2) {
            selHistManager->subleadMuon_->fillHistograms({selMuons[1]},
                                                         evtWeight);
          }
          selHistManager->jets_->fillHistograms(selJets, evtWeight);
          selHistManager->leadJet_->fillHistograms(selJets, evtWeight);
          selHistManager->subleadJet_->fillHistograms(selJets, evtWeight);
          if (selJetAK8_Wjj) {
            selHistManager->jetsAK8_Wjj_->fillHistograms({selJetAK8_Wjj},
                                                         evtWeight);
          }
          selHistManager->met_->fillHistograms(met, mhtP4, met_LD, evtWeight);
          selHistManager->metFilters_->fillHistograms(metFilters, evtWeight);
        }
        if (!skipFilling) {
          selHistManager->evt_->fillHistograms(
              selElectrons.size(), selMuons.size(), selJets.size(),
              numSelJetsPtGt40, dihiggsVisMass_sel, dihiggsMass_wMet_sel,
              vbf_m_jj, vbf_dEta_jj, vbf_dR_jj, 
              evtWeight,
              std::min(10., mindR_vbfjet_lep1), std::min(10., mindR_vbfjet_lep2),
              maxJetEta_vbf, minJetEta_vbf,
              lhe_dEta_jj, lhe_dPhi_jj, lhe_m_jj, lhe_dR_jj, 
              matched_dEta_jj, matched_dPhi_jj, matched_m_jj, matched_dR_jj, 
              best_dEta_jj, best_dPhi_jj, best_m_jj, best_dR_jj,
              lhe_pt_lead, lhe_pt_sublead, matched_pt_lead, matched_pt_sublead, best_pt_lead, best_pt_sublead,
              genjet_dEta_jj, genjet_dPhi_jj, genjet_m_jj, genjet_dR_jj,
              mass_jj_W, mass_jj_W2, sum_mass_W,
              sum_m_lj, pT_sum, m_ll, isVBF,
              maxJetPt_vbf, minJetPt_vbf, mindR_vbfJet_W1, maxdR_vbfJet_W1, mindR_vbfjet_lep, maxdR_vbfjet_lep,
              dR_h1h2, pT_h1, pT_h2, dR_h1_j1, dR_h1_j2, dR_h2_j1, dR_h2_j2, mass_h1, mass_h2,
              H1H2_centrality, vbfj1_cosphi, vbfj2_cosphi
              );
        }
        // selHistManager->datacard_->fillHistograms(
        //          BDTOutput_Map_spin2,
        //          BDTOutput_Map_spin0,
        //          BDTOutput_Map_nonRes,
        //          //BDTOutput_Map_nonRes_base["Base"],
        //   -1., // CV: BDTOutput for nonresonant_allBMs case not implemented
        //   yet !!
        //          evtWeight);

        /*if(! skipFilling)
        {

          selHistManager->mvaInputVarCorrelation_->fillHistograms(AllVars_Map,
        evtWeight);

        }*/

        if (!skipFilling) {
          selHistManager->evtYield_->fillHistograms(eventInfo, evtWeight);
          selHistManager->weights_->fillHistograms("genWeight",
                                                   eventInfo.genWeight);
          selHistManager->weights_->fillHistograms(
              "pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift));
          selHistManager->weights_->fillHistograms(
              "triggerWeight",
              evtWeightRecorder.get_sf_triggerEff(central_or_shift));
          selHistManager->weights_->fillHistograms(
              "data_to_MC_correction",
              evtWeightRecorder.get_data_to_MC_correction(central_or_shift));
          selHistManager->weights_->fillHistograms(
              "fakeRate", evtWeightRecorder.get_FR(central_or_shift));
        }
      }

      if (isMC && !skipFilling) {
        genEvtHistManager_afterCuts[central_or_shift]->fillHistograms(
            genElectrons, genMuons, genHadTaus, genPhotonsFinal, genJets,
            evtWeightRecorder.get_inclusive(central_or_shift));
        lheInfoHistManager[central_or_shift]->fillHistograms(*lheInfoReader,
                                                             evtWeight);
        if (eventWeightManager) {
          genEvtHistManager_afterCuts[central_or_shift]->fillHistograms(
              eventWeightManager,
              evtWeightRecorder.get_inclusive(central_or_shift));
        }
      }
    }

    if (selEventsFile) {
      (*selEventsFile) << eventInfo.run << ':' << eventInfo.lumi << ':'
                       << eventInfo.event << '\n';
    }

    if (bdt_filler) {
      double lep1_genLepPt = (selLepton_lead->genLepton())
                                 ? selLepton_lead->genLepton()->pt()
                                 : 0.;
      double lep2_genLepPt = (selLepton_sublead->genLepton())
                                 ? selLepton_sublead->genLepton()->pt()
                                 : 0.;
      double prob_fake_lepton_lead =
          evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main);
      double prob_fake_lepton_sublead =
          evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main);
      double evtWeight_BDT = evtWeightRecorder.get(central_or_shift_main);
      double lep1_frWeight = lep1_genLepPt > 0 ? 1.0 : prob_fake_lepton_lead;
      double lep2_frWeight = lep2_genLepPt > 0 ? 1.0 : prob_fake_lepton_sublead;
      evtWeight_BDT *= lep1_frWeight * lep2_frWeight;

      std::map<std::string, double> weightMapHH;
      if (apply_HH_rwgt_lo || apply_HH_rwgt_nlo) {
        for (unsigned int i = 0; i < HHWeightNames.size(); i++) {
          double HHReweight = 1.;
          if (apply_HH_rwgt_lo) {
            assert(HHWeightLO_calc);
            HHReweight *= HHWeightLO_calc->getRelativeWeight(
                HHBMNames[i], eventInfo.gen_mHH, eventInfo.gen_cosThetaStar,
                isDEBUG);
          }
          if (apply_HH_rwgt_nlo) {
            assert(HHWeightNLO_calc);
            HHReweight *= HHWeightNLO_calc->getRelativeWeight_LOtoNLO(
                HHBMNames[i], eventInfo.gen_mHH, eventInfo.gen_cosThetaStar,
                isDEBUG);
          }
          weightMapHH[HHWeightNames[i]] = HHReweight;
        }
      }

      bdt_filler -> operator()({eventInfo.run, eventInfo.lumi, eventInfo.event})
          ("dihiggsVisMass_sel",      dihiggsVisMass_sel)
          ("dihiggsMass_wMet_sel",    dihiggsMass_wMet_sel)
          ("vbf_m_jj",                vbf_m_jj)
          ("vbf_dEta_jj",             vbf_dEta_jj)
          ("vbf_dR_jj",               vbf_dR_jj)
          ("evtWeight",               evtWeight_BDT)
          ("mindR_vbfjet_lep1",          std::min(10., mindR_vbfjet_lep1))
          ("mindR_vbfjet_lep2",          std::min(10., mindR_vbfjet_lep2))
          ("maxJetEta_vbf",             comp_maxAbsEta_jet(VBFjets))
          ("minJetEta_vbf",             comp_minAbsEta_jet(VBFjets))

          ("lhe_dEta_jj",             lhe_dEta_jj)
          ("lhe_dPhi_jj",             lhe_dPhi_jj)
          ("lhe_m_jj",                lhe_m_jj)
          ("lhe_dR_jj",               lhe_dR_jj)

          ("matched_dEta_jj",            matched_dEta_jj)
          ("matched_dPhi_jj",            matched_dPhi_jj)
          ("matched_m_jj",               matched_m_jj)
          ("matched_dR_jj",              matched_dR_jj)

          ("best_dEta_jj",            best_dEta_jj)
          ("best_dPhi_jj",            best_dPhi_jj)
          ("best_m_jj",               best_m_jj)
          ("best_dR_jj",              best_dR_jj)

          ("lhe_pt_lead",              lhe_pt_lead)
          ("lhe_pt_sublead",           lhe_pt_sublead)
          ("matched_pt_lead",              matched_pt_lead)
          ("matched_pt_sublead",              matched_pt_sublead)
          ("best_pt_lead",              best_pt_lead)
          ("best_pt_sublead",              best_pt_sublead)

          ("genjet_dEta_jj",            genjet_dEta_jj)
          ("genjet_dPhi_jj",               genjet_dPhi_jj)
          ("genjet_m_jj",            genjet_m_jj)
          ("genjet_dR_jj",              genjet_dR_jj)

          ("mass_jj_W",              mass_jj_W)
          ("mass_jj_W2",              mass_jj_W2)
          ("sum_mass_W",              sum_mass_W)

          ("sum_m_lj",              sum_m_lj)
          ("pT_sum",              pT_sum)
          ("m_ll",              m_ll)
          ("isVBF",             isVBF)

          ("maxJetPt_vbf",             maxJetPt_vbf)
          ("minJetPt_vbf",             minJetPt_vbf)
          ("mindR_vbfJet_W1",             mindR_vbfJet_W1)
          ("maxdR_vbfJet_W1",             maxdR_vbfJet_W1)
          ("mindR_vbfjet_lep",             mindR_vbfjet_lep)
          ("maxdR_vbfjet_lep",             maxdR_vbfjet_lep)

          ("dR_h1h2",             dR_h1h2)
          ("pT_h1",             pT_h1)
          ("pT_h2",             pT_h2)
          ("dR_h1_j1",             dR_h1_j1)
          ("dR_h1_j2",             dR_h1_j2)
          ("dR_h2_j1",             dR_h2_j1)
          ("dR_h2_j2",             dR_h2_j2)
          ("mass_h1",             mass_h1)
          ("mass_h2",             mass_h2)

          ("H1H2_centrality",             H1H2_centrality)
          ("vbfj1_cosphi",             vbfj1_cosphi)
          ("vbfj2_cosphi",             vbfj2_cosphi)

          (weightMapHH)
        .fill();
    }

    ++selectedEntries;
    selectedEntries_weighted += evtWeightRecorder.get(central_or_shift_main);
    std::string process_and_genMatch = process_string;
    process_and_genMatch += selLepton_genMatch.name_;
    ++selectedEntries_byGenMatchType[process_and_genMatch];
    for (const std::string &central_or_shift : central_or_shifts_local) {
      selectedEntries_weighted_byGenMatchType[central_or_shift]
                                             [process_and_genMatch] +=
          evtWeightRecorder.get(central_or_shift);
    }
    histogram_selectedEntries->Fill(0.);
    if (isDEBUG) {
      std::cout << evtWeightRecorder << '\n';
    }
  }
  std::cout << "max num. Entries = " << inputTree->getCumulativeMaxEventCount()
            << " (limited by " << maxEvents << ") processed in "
            << inputTree->getProcessedFileCount() << " file(s) (out of "
            << inputTree->getFileCount() << ")\n"
            << " analyzed = " << analyzedEntries << '\n'
            << " selected = " << selectedEntries
            << " (weighted = " << selectedEntries_weighted << ")\n\n"
            << "cut-flow table" << std::endl;
  cutFlowTable.print(std::cout);
  std::cout << std::endl;

  std::cout << "sel. Entries by gen. matching:" << std::endl;
  for (const std::string &central_or_shift : central_or_shifts_local) {
    std::cout << "central_or_shift = " << central_or_shift << '\n';
    for (const leptonChargeFlipGenMatchEntry &leptonGenMatch_definition :
         leptonGenMatch_definitions) {
      std::string process_and_genMatch = process_string;
      process_and_genMatch += leptonGenMatch_definition.name_;
      std::cout << " " << process_and_genMatch << " = "
                << selectedEntries_byGenMatchType[process_and_genMatch]
                << " (weighted = "
                << selectedEntries_weighted_byGenMatchType[central_or_shift]
                                                          [process_and_genMatch]
                << ")\n";
    }
  }
  std::cout << std::endl;

  //--- manually write histograms to output file
  fs.file().cd();
  // histogram_analyzedEntries->Write();
  // histogram_selectedEntries->Write();
  HistManagerBase::writeHistograms();

  //--- memory clean-up
  delete dataToMCcorrectionInterface;
  delete leptonFakeRateInterface;
  delete run_lumi_eventSelector;
  delete blacklist;
  delete selEventsFile;
  delete muonReader;
  delete electronReader;
  delete hadTauReader;
  delete jetReader;
  delete jetReaderAK8;
  delete metReader;
  delete metFilterReader;
  delete genLeptonReader;
  delete genHadTauReader;
  delete genPhotonReader;
  delete genProxyPhotonReader;
  delete genFromHardProcessReader;
  delete genJetReader;
  delete genHiggsReader;
  delete lheInfoReader;
  delete psWeightReader;
  delete general_lhe_reader;


  for (auto &kv : genEvtHistManager_beforeCuts) {
    delete kv.second;
  }
  for (auto &kv : genEvtHistManager_afterCuts) {
    delete kv.second;
  }
  for (auto &kv : lheInfoHistManager) {
    delete kv.second;
  }
  delete cutFlowHistManager;
  delete eventWeightManager;

  hltPaths_delete(triggers_1e);
  hltPaths_delete(triggers_2e);
  hltPaths_delete(triggers_1mu);
  hltPaths_delete(triggers_2mu);
  hltPaths_delete(triggers_1e1mu);

  delete inputTree;

  clock.Show("analyze_hh_2lss_vbf");

  return EXIT_SUCCESS;
}
