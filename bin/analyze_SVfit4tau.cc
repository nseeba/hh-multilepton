#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h" // edm::readPSetsFrom()
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector
#include "DataFormats/Math/interface/deltaR.h" // deltaR

#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TMatrixD.h> // TMatrixD
#include <TError.h> // gErrorAbortLevel, kError
#include <TMath.h> // TMath::
#include <TH2.h> // TH2

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h" // RecoHadTau
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h" // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauReader.h" // RecoHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTauReader.h" // GenHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/convert_to_ptrs.h" // convert_to_ptrs
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionCleaner.h" // RecoElectronCollectionCleaner, RecoMuonCollectionCleaner, RecoHadTauCollectionCleaner, RecoJetCollectionCleaner
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionGenMatcher.h" // RecoElectronCollectionGenMatcher, RecoMuonCollectionGenMatcher, RecoHadTauCollectionGenMatcher, RecoJetCollectionGenMatcher
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorLoose.h" // RecoElectronCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorFakeable.h" // RecoElectronCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorTight.h" // RecoElectronCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorLoose.h" // RecoMuonCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorFakeable.h" // RecoMuonCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorTight.h" // RecoMuonCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorLoose.h" // RecoHadTauCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorFakeable.h" // RecoHadTauCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorTight.h" // RecoHadTauCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelector.h" // RecoJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorBtag.h" // RecoJetCollectionSelectorBtagLoose, RecoJetCollectionSelectorBtagMedium
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "tthAnalysis/HiggsToTauTau/interface/ElectronHistManager.h" // ElectronHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MuonHistManager.h" // MuonHistManager
#include "tthAnalysis/HiggsToTauTau/interface/HadTauHistManager.h" // HadTauHistManager
#include "tthAnalysis/HiggsToTauTau/interface/JetHistManager.h" // JetHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MEtHistManager.h" // MEtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/WeightHistManager.h" // WeightHistManager
#include "tthAnalysis/HiggsToTauTau/interface/GenEvtHistManager.h" // GenEvtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // getLeptonType, kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // isHigherPt, isMatched
#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper

#include "hhAnalysis/4tau/interface/SVfit4tauDiHiggsHistManager.h" // SVfit4tauDiHiggsHistManager
#include "hhAnalysis/4tau/interface/SVfit4tauHiggsHistManager.h" // SVfit4tauHiggsHistManager

#include "TauAnalysis/ClassicSVfit4tau/interface/ClassicSVfit4tau.h" // ClassicSVfit4tau
#include "TauAnalysis/ClassicSVfit/interface/MeasuredTauLepton.h" // classic_svFit::MeasuredTauLepton
#include "TauAnalysis/ClassicSVfit4tau/interface/svFitHistogramAdapter4tau.h" // HistogramAdapterDiHiggs, HistogramAdapterHiggs

#include <boost/math/special_functions/sign.hpp> // boost::math::sign()

#include <iostream> // std::cerr, std::fixed
#include <iomanip> // std::setprecision(), std::setw()
#include <string> // std::string
#include <vector> // std::vector<>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <algorithm> // std::sort
#include <fstream> // std::ofstream
#include <assert.h> // assert

typedef std::vector<std::string> vstring;

enum { k4lepton, k3lepton_1tau, k2lepton_2tau, k1lepton_3tau, k4tau };

int get_idxCategory(const std::string& category) 
{
  if      ( category == "4lepton"      ) return k4lepton;
  else if ( category == "4lepton_1tau" ) return k3lepton_1tau;
  else if ( category == "4lepton_2tau" ) return k2lepton_2tau;
  else if ( category == "4lepton_3tau" ) return k1lepton_3tau;
  else if ( category == "4tau"         ) return k4tau;
  else assert(0);
}

int get_idxCategory(int numLeptons, int numHadTaus) 
{
  if      ( numLeptons >= 4 && numHadTaus >= 0 ) return k4lepton;
  else if ( numLeptons == 3 && numHadTaus >= 1 ) return k3lepton_1tau;
  else if ( numLeptons == 2 && numHadTaus >= 2 ) return k2lepton_2tau;
  else if ( numLeptons == 1 && numHadTaus >= 3 ) return k1lepton_3tau;
  else if ( numLeptons == 0 && numHadTaus >= 4 ) return k4tau;
  else assert(0);
}

const GenParticle* findGenTau(const GenParticle& measuredTau, const std::vector<GenParticle>& genTaus)
{
  const GenParticle* bestMatch = nullptr;
  double dR_min = 1.e+3;
  for ( std::vector<GenParticle>::const_iterator genTau = genTaus.begin();
	genTau != genTaus.end(); ++genTau ) {
    double dR = deltaR(measuredTau.p4(), genTau->p4());
    if ( dR < 0.3 && dR < dR_min ) {
      bestMatch = &(*genTau);
      dR_min = dR;
    }
  }
  return bestMatch;
}

double square(double x)
{
  return x*x;
}

const GenParticle* findGenHiggs(const Particle::LorentzVector& p4, const std::vector<GenParticle>& genHiggsBosons)
{
  const GenParticle* bestMatch = nullptr;
  double d_min = 1.e+3;
  for ( std::vector<GenParticle>::const_iterator genHiggsBoson = genHiggsBosons.begin();
	genHiggsBoson != genHiggsBosons.end(); ++genHiggsBoson ) {
    double d = TMath::Sqrt(square(genHiggsBoson->p4().px() - p4.px()) + square(genHiggsBoson->p4().py() - p4.py()) + square(genHiggsBoson->p4().pz() - p4.pz()));
    if ( d < 5. && d < d_min ) {
      bestMatch = &(*genHiggsBoson);
      d_min = d;
    }
  }
  return bestMatch;
}

classic_svFit::MeasuredTauLepton makeMeasuredTauLepton(const GenParticle& measuredTau)
{
  int measuredTauType = classic_svFit::MeasuredTauLepton::kUndefinedDecayType;
  if      ( TMath::Abs(measuredTau.pdgId()) == 11 ) measuredTauType = classic_svFit::MeasuredTauLepton::kTauToElecDecay;
  else if ( TMath::Abs(measuredTau.pdgId()) == 13 ) measuredTauType = classic_svFit::MeasuredTauLepton::kTauToMuDecay;
  else                                              measuredTauType = classic_svFit::MeasuredTauLepton::kTauToHadDecay;
  if ( measuredTauType == classic_svFit::MeasuredTauLepton::kTauToElecDecay || 
       measuredTauType == classic_svFit::MeasuredTauLepton::kTauToMuDecay   ) {
    return classic_svFit::MeasuredTauLepton(measuredTauType, measuredTau.pt(), measuredTau.eta(), measuredTau.phi(), measuredTau.mass());
  } else {
    const RecoHadTau* recHadTau = dynamic_cast<const RecoHadTau*>(&measuredTau);
    assert(recHadTau);
    return classic_svFit::MeasuredTauLepton(measuredTauType, measuredTau.pt(), measuredTau.eta(), measuredTau.phi(), measuredTau.mass(), recHadTau->decayMode());
  }
}

const int hadTauSelection_antiElectron = 1; // vLoose
const int hadTauSelection_antiMuon = 1; // Loose

/**
 * @brief Produce resolution plots of pT, eta, phi, and mass of di-Higgs system reconstructed by ClassicSVfit4tau algorithm
 */
int main(int argc, char* argv[])
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- parse command-line arguments
  if ( argc < 2 ) {
    std::cout << "Usage: " << argv[0] << " [parameters.py]" << std::endl;
    return EXIT_FAILURE;
  }

  std::cout << "<analyze_SVfit4tau>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_SVfit4tau");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_SVfit4tau")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_SVfit4tau");

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  bool isSignal = ( process_string == "signal" ) ? true : false;

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  int era = kEra_undefined;
  if      ( era_string == "2016" ) era = kEra_2016;
  else if ( era_string == "2017" ) era = kEra_2017;
  else throw cms::Exception("analyze_SVfit4tau")
    << "Invalid Configuration parameter 'era' = " << era_string << " !!\n";

  std::string leptonSelection_string = cfg_analyze.getParameter<std::string>("leptonSelection").data();
  std::cout << "leptonSelection_string = " << leptonSelection_string << std::endl;
  int leptonSelection = -1;
  if      ( leptonSelection_string == "Loose"                                                      ) leptonSelection = kLoose;
  else if ( leptonSelection_string == "Fakeable" || leptonSelection_string == "Fakeable_mcClosure" ) leptonSelection = kFakeable;
  else if ( leptonSelection_string == "Tight"                                                      ) leptonSelection = kTight;
  else throw cms::Exception("analyze_SVfit4tau")
    << "Invalid Configuration parameter 'leptonSelection' = " << leptonSelection_string << " !!\n";
  
  TString hadTauSelection_string = cfg_analyze.getParameter<std::string>("hadTauSelection").data();
  TObjArray* hadTauSelection_parts = hadTauSelection_string.Tokenize("|");
  assert(hadTauSelection_parts->GetEntries() >= 1);
  std::string hadTauSelection_part1 = (dynamic_cast<TObjString*>(hadTauSelection_parts->At(0)))->GetString().Data();
  int hadTauSelection = -1;
  if      ( hadTauSelection_part1 == "Loose"                                                     ) hadTauSelection = kLoose;
  else if ( hadTauSelection_part1 == "Fakeable" || hadTauSelection_part1 == "Fakeable_mcClosure" ) hadTauSelection = kFakeable;
  else if ( hadTauSelection_part1 == "Tight"                                                     ) hadTauSelection = kTight;
  else throw cms::Exception("analyze_SVfit4tau")
    << "Invalid Configuration parameter 'hadTauSelection' = " << hadTauSelection_string << " !!\n";
  std::string hadTauSelection_part2 = ( hadTauSelection_parts->GetEntries() == 2 ) ? (dynamic_cast<TObjString*>(hadTauSelection_parts->At(1)))->GetString().Data() : "";
  delete hadTauSelection_parts;
 
  double logM_wMassConstraint = cfg_analyze.getParameter<double>("SVfit4tau_logM_wMassConstraint");
  double logM_woMassConstraint = cfg_analyze.getParameter<double>("SVfit4tau_logM_woMassConstraint");

  bool use_HIP_mitigation_mediumMuonId = cfg_analyze.getParameter<bool>("use_HIP_mitigation_mediumMuonId");
  std::cout << "use_HIP_mitigation_mediumMuonId = " << use_HIP_mitigation_mediumMuonId << std::endl;

  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  std::string central_or_shift = cfg_analyze.getParameter<std::string>("central_or_shift");
  double lumiScale = ( process_string != "data_obs" ) ? cfg_analyze.getParameter<double>("lumiScale") : 1.;
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");

  bool isDEBUG = ( cfg_analyze.exists("isDEBUG") ) ? cfg_analyze.getParameter<bool>("isDEBUG") : false;
  if ( isDEBUG ) std::cout << "Warning: DEBUG mode enabled -> trigger selection will not be applied for data !!" << std::endl;

  int met_option = RecoMEtReader::kMEt_central;
  int hadTauPt_option = RecoHadTauReader::kHadTauPt_central;
  if ( central_or_shift != "central" ) {
    TString central_or_shift_tstring = central_or_shift.data();
    std::string shiftUp_or_Down = "";
    if      ( central_or_shift_tstring.EndsWith("Up")   ) shiftUp_or_Down = "Up";
    else if ( central_or_shift_tstring.EndsWith("Down") ) shiftUp_or_Down = "Down";
    else throw cms::Exception("analyze_SVfit4tau")
      << "Invalid Configuration parameter 'central_or_shift' = " << central_or_shift << " !!\n";
    if ( central_or_shift_tstring.BeginsWith("CMS_JES") ) {
      if ( isMC ) {
        if ( shiftUp_or_Down == "Up" ) met_option = RecoMEtReader::kMEt_shifted_JetEnUp;
        else if ( shiftUp_or_Down == "Down" ) met_option = RecoMEtReader::kMEt_shifted_JetEnDown;
        else assert(0);
      } else throw cms::Exception("analyze_SVfit4tau")
          << "Configuration parameter 'central_or_shift' = " << central_or_shift << " not supported for data !!\n";
    } else if ( central_or_shift_tstring.BeginsWith("CMS_JER") ) {
      if ( central_or_shift_tstring.EndsWith("Up") ) met_option = RecoMEtReader::kMEt_shifted_JetResUp;
      else if ( central_or_shift_tstring.EndsWith("Down") ) met_option = RecoMEtReader::kMEt_shifted_JetResDown;
      else assert(0);
    } else if ( central_or_shift_tstring.BeginsWith("CMS_UnclusteredEn") ) {
      if ( central_or_shift_tstring.EndsWith("Up") ) met_option = RecoMEtReader::kMEt_shifted_UnclusteredEnUp;
      else if ( central_or_shift_tstring.EndsWith("Down") ) met_option = RecoMEtReader::kMEt_shifted_UnclusteredEnDown;
      else assert(0);
    } else if ( central_or_shift_tstring.BeginsWith("CMS_tauES") ) {
      if ( isMC ) {
        if      ( shiftUp_or_Down == "Up"   ) hadTauPt_option = RecoHadTauReader::kHadTauPt_shiftUp;
        else if ( shiftUp_or_Down == "Down" ) hadTauPt_option = RecoHadTauReader::kHadTauPt_shiftDown;
        else assert(0);
      } else throw cms::Exception("analyze_SVfit4tau")
          << "Configuration parameter 'central_or_shift' = " << central_or_shift << " not supported for data !!\n";
    }
  }

  bool fillGenEvtHistograms = cfg_analyze.getParameter<bool>("fillGenEvtHistograms");

  std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_hadTaus = cfg_analyze.getParameter<std::string>("branchName_hadTaus");
  std::string branchName_jets = cfg_analyze.getParameter<std::string>("branchName_jets");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");

  std::string branchName_genLeptons = cfg_analyze.getParameter<std::string>("branchName_genLeptons1");
  std::string branchName_genLeptons2 = cfg_analyze.getParameter<std::string>("branchName_genLeptons2");
  std::string branchName_genHadTaus = cfg_analyze.getParameter<std::string>("branchName_genHadTaus");
  std::string branchName_genJets = cfg_analyze.getParameter<std::string>("branchName_genJets");

  std::string branchName_genTaus = cfg_analyze.getParameter<std::string>("branchName_genTaus");
  std::string branchName_genHiggsBosons = cfg_analyze.getParameter<std::string>("branchName_genHiggsBosons");

  bool redoGenMatching = cfg_analyze.getParameter<bool>("redoGenMatching");

  std::string selEventsFileName_input = cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input << std::endl;
  RunLumiEventSelector* run_lumi_eventSelector = 0;
  if ( selEventsFileName_input != "" ) {
    edm::ParameterSet cfgRunLumiEventSelector;
    cfgRunLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfgRunLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfgRunLumiEventSelector);
  }

  fwlite::InputSource inputFiles(cfg);
  int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s).\n";

//--- declare event-level variables
  EventInfo eventInfo(isSignal, isMC, false);
  EventInfoReader eventInfoReader(&eventInfo);
  inputTree->registerReader(&eventInfoReader);

//--- declare particle collections
  const bool readGenObjects = isMC && !redoGenMatching;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, readGenObjects);
  muonReader->set_HIP_mitigation(use_HIP_mitigation_mediumMuonId);
  inputTree->registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era);
  RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era);
  RecoMuonCollectionSelectorTight tightMuonSelector(era);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, readGenObjects);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era);
  RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era);
  RecoElectronCollectionSelectorTight tightElectronSelector(era);

  RecoHadTauReader* hadTauReader = new RecoHadTauReader(era, branchName_hadTaus, readGenObjects);
  hadTauReader->setHadTauPt_central_or_shift(hadTauPt_option);
  inputTree->registerReader(hadTauReader);
  RecoHadTauCollectionGenMatcher hadTauGenMatcher;
  RecoHadTauCollectionCleaner hadTauCleaner(0.3);
  RecoHadTauCollectionSelectorLoose preselHadTauSelector(era);
  if ( hadTauSelection_part2 == "dR03mvaVLoose" || hadTauSelection_part2 == "dR03mvaVVLoose" ) preselHadTauSelector.set(hadTauSelection_part2);
  preselHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  preselHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  RecoHadTauCollectionSelectorFakeable fakeableHadTauSelector(era);
  if ( hadTauSelection_part2 == "dR03mvaVLoose" || hadTauSelection_part2 == "dR03mvaVVLoose" ) fakeableHadTauSelector.set(hadTauSelection_part2);
  fakeableHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  fakeableHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  RecoHadTauCollectionSelectorTight tightHadTauSelector(era);
  if ( hadTauSelection_part2 != "" ) tightHadTauSelector.set(hadTauSelection_part2);
  tightHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  tightHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);

  RecoJetReader* jetReader = new RecoJetReader(era, isMC, branchName_jets, readGenObjects);
  inputTree->registerReader(jetReader);
  RecoJetCollectionGenMatcher jetGenMatcher;
  RecoJetCollectionCleaner jetCleaner(0.4);
  RecoJetCollectionSelector jetSelector(era);
  RecoJetCollectionSelectorBtagLoose jetSelectorBtagLoose(era);
  RecoJetCollectionSelectorBtagMedium jetSelectorBtagMedium(era);

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(met_option);
  inputTree -> registerReader(metReader);

//--- declare generator level information
  GenLeptonReader* genLeptonReader = nullptr;
  GenHadTauReader* genHadTauReader = nullptr;
  GenJetReader* genJetReader = nullptr;
  GenParticleReader* genTauReader = nullptr;
  GenParticleReader* genHiggsBosonReader = nullptr;
  if ( isMC ) {
    if ( !readGenObjects ) {
      if ( branchName_genLeptons != "" ) {
        genLeptonReader = new GenLeptonReader(branchName_genLeptons);
        inputTree->registerReader(genLeptonReader);
      }
      if ( branchName_genHadTaus != "" ) {
        genHadTauReader = new GenHadTauReader(branchName_genHadTaus);
        inputTree->registerReader(genHadTauReader);
      }
      if ( branchName_genJets != "" ) {
        genJetReader = new GenJetReader(branchName_genJets);
        inputTree->registerReader(genJetReader);
      }
    }
    if ( branchName_genTaus != "" ) {
      genTauReader = new GenParticleReader(branchName_genTaus);
      inputTree->registerReader(genTauReader);
    }
    if ( branchName_genHiggsBosons != "" ) {
      genHiggsBosonReader = new GenParticleReader(branchName_genHiggsBosons);
      inputTree->registerReader(genHiggsBosonReader);
    }
  }

//--- declare histograms
  struct selHistManagerType
  {
    ElectronHistManager* electrons_;
    ElectronHistManager* leadElectron_;
    ElectronHistManager* subleadElectron_;
    MuonHistManager* muons_;
    MuonHistManager* leadMuon_;
    MuonHistManager* subleadMuon_;
    HadTauHistManager* hadTaus_;
    HadTauHistManager* leadHadTau_;
    HadTauHistManager* subleadHadTau_;
    JetHistManager* jets_;
    JetHistManager* leadJet_;
    JetHistManager* subleadJet_;
    JetHistManager* BJets_loose_;
    JetHistManager* BJets_medium_;
    MEtHistManager* met_;
    SVfit4tauDiHiggsHistManager* dihiggs_wMassContraint_correctAssoc_;
    SVfit4tauHiggsHistManager* higgs1_wMassContraint_correctAssoc_;
    SVfit4tauHiggsHistManager* higgs2_wMassContraint_correctAssoc_;
    SVfit4tauDiHiggsHistManager* dihiggs_wMassContraint_incorrectAssoc_;
    SVfit4tauHiggsHistManager* higgs1_wMassContraint_incorrectAssoc_;
    SVfit4tauHiggsHistManager* higgs2_wMassContraint_incorrectAssoc_;
    SVfit4tauDiHiggsHistManager* dihiggs_woMassContraint_correctAssoc_;
    SVfit4tauHiggsHistManager* higgs1_woMassContraint_correctAssoc_;
    SVfit4tauHiggsHistManager* higgs2_woMassContraint_correctAssoc_;
    SVfit4tauDiHiggsHistManager* dihiggs_woMassContraint_incorrectAssoc_;
    SVfit4tauHiggsHistManager* higgs1_woMassContraint_incorrectAssoc_;
    SVfit4tauHiggsHistManager* higgs2_woMassContraint_incorrectAssoc_;    
    WeightHistManager* weights_;
  };
  std::map<int, selHistManagerType*> selHistManagers;

  vstring categories = { "4lepton", "3lepton_1tau", "2lepton_2tau", "1lepton_3tau", "4tau" };
  for ( vstring::const_iterator category = categories.begin();
	category != categories.end(); ++category ) {
    TString histogramDir_category = histogramDir.data();
    histogramDir_category.ReplaceAll("SVfit4tau", Form("SVfit4tau_%s", category->data()));

    selHistManagerType* selHistManager = new selHistManagerType();
    selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/electrons", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->electrons_->bookHistograms(fs);
    selHistManager->leadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/leadElectron", histogramDir.data(), category->data()), central_or_shift, 0));
    selHistManager->leadElectron_->bookHistograms(fs);
    selHistManager->subleadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/subleadElectron", histogramDir.data(), category->data()), central_or_shift, 1));
    selHistManager->subleadElectron_->bookHistograms(fs);
    selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/muons", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->muons_->bookHistograms(fs);
    selHistManager->leadMuon_ = new MuonHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/leadMuon", histogramDir.data(), category->data()), central_or_shift, 0));
    selHistManager->leadMuon_->bookHistograms(fs);
    selHistManager->subleadMuon_ = new MuonHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/subleadMuon", histogramDir.data(), category->data()), central_or_shift, 1));
    selHistManager->subleadMuon_->bookHistograms(fs);
    selHistManager->hadTaus_ = new HadTauHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/hadTaus", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->hadTaus_->bookHistograms(fs);
    selHistManager->leadHadTau_ = new HadTauHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/leadHadTau", histogramDir.data(), category->data()), central_or_shift, 0));
    selHistManager->leadHadTau_->bookHistograms(fs);
    selHistManager->subleadHadTau_ = new HadTauHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/subleadHadTau", histogramDir.data(), category->data()), central_or_shift, 1));
    selHistManager->subleadHadTau_->bookHistograms(fs);
    selHistManager->jets_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/jets", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->jets_->bookHistograms(fs);
    selHistManager->leadJet_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/leadJet", histogramDir.data(), category->data()), central_or_shift, 0));
    selHistManager->leadJet_->bookHistograms(fs);
    selHistManager->subleadJet_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/subleadJet", histogramDir.data(), category->data()), central_or_shift, 1));
    selHistManager->subleadJet_->bookHistograms(fs);
    selHistManager->BJets_loose_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/BJets_loose", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->BJets_loose_->bookHistograms(fs);
    selHistManager->BJets_medium_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/BJets_medium", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->BJets_medium_->bookHistograms(fs);
    selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/met", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->met_->bookHistograms(fs);
    selHistManager->dihiggs_wMassContraint_correctAssoc_ = new SVfit4tauDiHiggsHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/dihiggs_wMassContraint_correctAssoc", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->dihiggs_wMassContraint_correctAssoc_->bookHistograms(fs);
    selHistManager->higgs1_wMassContraint_correctAssoc_ = new SVfit4tauHiggsHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs1_wMassContraint_correctAssoc", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->higgs1_wMassContraint_correctAssoc_->bookHistograms(fs);
    selHistManager->higgs2_wMassContraint_correctAssoc_ = new SVfit4tauHiggsHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs2_wMassContraint_correctAssoc", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->higgs2_wMassContraint_correctAssoc_->bookHistograms(fs);
    selHistManager->dihiggs_wMassContraint_incorrectAssoc_ = new SVfit4tauDiHiggsHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/dihiggs_wMassContraint_incorrectAssoc", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->dihiggs_wMassContraint_incorrectAssoc_->bookHistograms(fs);
    selHistManager->higgs1_wMassContraint_incorrectAssoc_ = new SVfit4tauHiggsHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs1_wMassContraint_incorrectAssoc", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->higgs1_wMassContraint_incorrectAssoc_->bookHistograms(fs);
    selHistManager->higgs2_wMassContraint_incorrectAssoc_ = new SVfit4tauHiggsHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs2_wMassContraint_incorrectAssoc", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->higgs2_wMassContraint_incorrectAssoc_->bookHistograms(fs);
    selHistManager->dihiggs_woMassContraint_correctAssoc_ = new SVfit4tauDiHiggsHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/dihiggs_woMassContraint_correctAssoc", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->dihiggs_woMassContraint_correctAssoc_->bookHistograms(fs);
    selHistManager->higgs1_woMassContraint_correctAssoc_ = new SVfit4tauHiggsHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs1_woMassContraint_correctAssoc", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->higgs1_woMassContraint_correctAssoc_->bookHistograms(fs);
    selHistManager->higgs2_woMassContraint_correctAssoc_ = new SVfit4tauHiggsHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs2_woMassContraint_correctAssoc", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->higgs2_woMassContraint_correctAssoc_->bookHistograms(fs);
    selHistManager->dihiggs_woMassContraint_incorrectAssoc_ = new SVfit4tauDiHiggsHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/dihiggs_woMassContraint_incorrectAssoc", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->dihiggs_woMassContraint_incorrectAssoc_->bookHistograms(fs);
    selHistManager->higgs1_woMassContraint_incorrectAssoc_ = new SVfit4tauHiggsHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs1_woMassContraint_incorrectAssoc", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->higgs1_woMassContraint_incorrectAssoc_->bookHistograms(fs);
    selHistManager->higgs2_woMassContraint_incorrectAssoc_ = new SVfit4tauHiggsHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs2_woMassContraint_incorrectAssoc", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->higgs2_woMassContraint_incorrectAssoc_->bookHistograms(fs);    
    selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/weights", histogramDir.data(), category->data()), central_or_shift));
    selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight" });
    int idxCategory = get_idxCategory(*category);
    selHistManagers[idxCategory] = selHistManager;
  }

  GenEvtHistManager* genEvtHistManager_beforeCuts = 0;
  GenEvtHistManager* genEvtHistManager_afterCuts = 0;
  if ( isMC ) {
    genEvtHistManager_beforeCuts = new GenEvtHistManager(makeHistManager_cfg(process_string,
      Form("%s/unbiased/genEvt", histogramDir.data()), central_or_shift));
    genEvtHistManager_beforeCuts->bookHistograms(fs);
    genEvtHistManager_afterCuts = new GenEvtHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/genEvt", histogramDir.data()), central_or_shift));
    genEvtHistManager_afterCuts->bookHistograms(fs);
  }

  int analyzedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  TH1* histogram_analyzedEntries = fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  TH1* histogram_selectedEntries = fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);

  while ( inputTree->hasNextEvent() && (!run_lumi_eventSelector || (run_lumi_eventSelector && !run_lumi_eventSelector->areWeDone())) ) {
    if ( inputTree->canReport(reportEvery) ) {
      std::cout << "processing Entry " << inputTree->getCurrentMaxEventIdx() << " or " << inputTree->getCurrentEventIdx() << " entry" 
		<< " in #" << (inputTree -> getProcessedFileCount() - 1) << " (" << eventInfo << ") file (" << selectedEntries << " Entries selected)\n";
    }
    ++analyzedEntries;
    histogram_analyzedEntries->Fill(0.);
    
    if ( isDEBUG ) {
      std::cout << "event #" << inputTree -> getCurrentMaxEventIdx() << ' ' << eventInfo << '\n';
    }

    if ( run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo) ) {
      continue;
    }

    if ( run_lumi_eventSelector ) {
      std::cout << "processing Entry " << inputTree->getCurrentMaxEventIdx() << ": " << eventInfo << '\n';
      if ( inputTree -> isOpen() ) {
        std::cout << "input File = " << inputTree->getCurrentFileName() << '\n';
      }
    }

//--- build collections of generator level particles (before any cuts are applied, to check distributions in unbiased event samples)
    std::vector<GenLepton> genLeptons;
    std::vector<GenLepton> genElectrons;
    std::vector<GenLepton> genMuons;
    std::vector<GenHadTau> genHadTaus;
    std::vector<GenJet> genJets;
    std::vector<GenParticle> genTaus;
    std::vector<GenParticle> genHiggsBosons;
    if ( isMC && fillGenEvtHistograms ) {
      if ( genLeptonReader ) {
        genLeptons = genLeptonReader->read();
        for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin();
              genLepton != genLeptons.end(); ++genLepton ) {
          int abs_pdgId = std::abs(genLepton->pdgId());
          if      ( abs_pdgId == 11 ) genElectrons.push_back(*genLepton);
          else if ( abs_pdgId == 13 ) genMuons.push_back(*genLepton);
        }
      }
      if ( genHadTauReader ) {
        genHadTaus = genHadTauReader->read();
      }
      if ( genJetReader ) {
        genJets = genJetReader->read();
      }
      if ( genTauReader ) {
	genTaus = genTauReader->read();
      }
      if ( genHiggsBosonReader ) {
	genHiggsBosons = genHiggsBosonReader->read();
      }
    }
    
    if ( isMC ) {
      genEvtHistManager_beforeCuts->fillHistograms(genElectrons, genMuons, genHadTaus, genJets);
    }

//--- build collections of electrons, muons and hadronic taus;
//    resolve overlaps in order of priority: muon, electron,
    std::vector<RecoMuon> muons = muonReader->read();
    std::vector<const RecoMuon*> muon_ptrs = convert_to_ptrs(muons);
    std::vector<const RecoMuon*> cleanedMuons = muon_ptrs; // CV: no cleaning needed for muons, as they have the highest priority in the overlap removal
    std::vector<const RecoMuon*> preselMuons = preselMuonSelector(cleanedMuons);
    std::sort(preselMuons.begin(), preselMuons.end(), isHigherPt);
    std::vector<const RecoMuon*> fakeableMuons = fakeableMuonSelector(preselMuons);
    std::sort(fakeableMuons.begin(), fakeableMuons.end(), isHigherConePt);
    std::vector<const RecoMuon*> tightMuons = tightMuonSelector(preselMuons);
    std::sort(tightMuons.begin(), tightMuons.end(), isHigherPt);
    std::vector<const RecoMuon*> selMuons;
    if      ( leptonSelection == kLoose    ) selMuons = preselMuons;
    else if ( leptonSelection == kFakeable ) selMuons = fakeableMuons;
    else if ( leptonSelection == kTight    ) selMuons = tightMuons;
    else assert(0);
    if ( isDEBUG ) {
      for ( size_t idxPreselMuon = 0; idxPreselMuon < preselMuons.size(); ++idxPreselMuon ) {
        std::cout << "preselMuon #" << idxPreselMuon << ":" << std::endl;
        std::cout << (*preselMuons[idxPreselMuon]);
      }
      for ( size_t idxSelMuon = 0; idxSelMuon < selMuons.size(); ++idxSelMuon ) {
        std::cout << "selMuon #" << idxSelMuon << ":" << std::endl;
        std::cout << (*selMuons[idxSelMuon]);
      }
    }

    std::vector<RecoElectron> electrons = electronReader->read();
    std::vector<const RecoElectron*> electron_ptrs = convert_to_ptrs(electrons);
    std::vector<const RecoElectron*> cleanedElectrons = electronCleaner(electron_ptrs, selMuons);
    std::vector<const RecoElectron*> preselElectrons = preselElectronSelector(cleanedElectrons);
    std::sort(preselElectrons.begin(), preselElectrons.end(), isHigherPt);
    std::vector<const RecoElectron*> fakeableElectrons = fakeableElectronSelector(preselElectrons);
    std::sort(fakeableElectrons.begin(), fakeableElectrons.end(), isHigherConePt);
    std::vector<const RecoElectron*> tightElectrons = tightElectronSelector(preselElectrons);
    std::sort(tightElectrons.begin(), tightElectrons.end(), isHigherPt);
    std::vector<const RecoElectron*> selElectrons;
    if      ( leptonSelection == kLoose    ) selElectrons = preselElectrons;
    else if ( leptonSelection == kFakeable ) selElectrons = fakeableElectrons;
    else if ( leptonSelection == kTight    ) selElectrons = tightElectrons;
    else assert(0);
    if ( isDEBUG ) {
      for ( size_t idxPreselElectron = 0; idxPreselElectron < preselElectrons.size(); ++idxPreselElectron ) {
        std::cout << "preselElectron #" << idxPreselElectron << ":" << std::endl;
        std::cout << (*preselElectrons[idxPreselElectron]);
      }
      for ( size_t idxSelElectron = 0; idxSelElectron < selElectrons.size(); ++idxSelElectron ) {
        std::cout << "selElectron #" << idxSelElectron << ":" << std::endl;
        std::cout << (*selElectrons[idxSelElectron]);
      }
    }

    std::vector<const RecoLepton*> selLeptons;
    selLeptons.reserve(selElectrons.size() + selMuons.size());
    selLeptons.insert(selLeptons.end(), selElectrons.begin(), selElectrons.end());
    selLeptons.insert(selLeptons.end(), selMuons.begin(), selMuons.end());
    std::sort(selLeptons.begin(), selLeptons.end(), isHigherPt);

    std::vector<RecoHadTau> hadTaus = hadTauReader->read();
    std::vector<const RecoHadTau*> hadTau_ptrs = convert_to_ptrs(hadTaus);
    std::vector<const RecoHadTau*> cleanedHadTaus = hadTauCleaner(hadTau_ptrs, preselMuons, preselElectrons);
    std::sort(cleanedHadTaus.begin(), cleanedHadTaus.end(), isHigherPt);
    std::vector<const RecoHadTau*> preselHadTaus = preselHadTauSelector(cleanedHadTaus);
    std::vector<const RecoHadTau*> fakeableHadTaus = fakeableHadTauSelector(cleanedHadTaus);
    std::vector<const RecoHadTau*> tightHadTaus = tightHadTauSelector(cleanedHadTaus);
    std::vector<const RecoHadTau*> selHadTaus;
    if      ( hadTauSelection == kLoose    ) selHadTaus = preselHadTaus;
    else if ( hadTauSelection == kFakeable ) selHadTaus = fakeableHadTaus;
    else if ( hadTauSelection == kTight    ) selHadTaus = tightHadTaus;
    else assert(0);
    if ( isDEBUG ) {
      for ( size_t idxPreselHadTau = 0; idxPreselHadTau < preselHadTaus.size(); ++idxPreselHadTau ) {
        std::cout << "preselHadTau #" << idxPreselHadTau << ":" << std::endl;
        std::cout << (*preselHadTaus[idxPreselHadTau]);
      }
      for ( size_t idxSelHadTau = 0; idxSelHadTau < selHadTaus.size(); ++idxSelHadTau ) {
        std::cout << "selHadTau #" << idxSelHadTau << ":" << std::endl;
        std::cout << (*selHadTaus[idxSelHadTau]);
      }
    }

//--- build collections of jets and select subset of jets passing b-tagging criteria
    std::vector<RecoJet> jets = jetReader->read();
    std::vector<const RecoJet*> jet_ptrs = convert_to_ptrs(jets);
    if ( isDEBUG ) {
      if ( run_lumi_eventSelector ) {
        std::cout << " (#uncleanedJets = " << jet_ptrs.size() << ")" << std::endl;
        for ( size_t idxJet = 0; idxJet < jet_ptrs.size(); ++idxJet ) {
          std::cout << "uncleanedJet #" << idxJet << ":" << std::endl;
          std::cout << (*jet_ptrs[idxJet]);
        }
      }
    }
    std::vector<const RecoJet*> cleanedJets = jetCleaner(jet_ptrs, fakeableElectrons, tightElectrons, fakeableMuons, tightMuons, fakeableHadTaus);
    std::sort(cleanedJets.begin(), cleanedJets.end(), isHigherPt);
    std::vector<const RecoJet*> selJets = jetSelector(cleanedJets);
    std::vector<const RecoJet*> selBJets_loose = jetSelectorBtagLoose(cleanedJets);
    std::vector<const RecoJet*> selBJets_medium = jetSelectorBtagMedium(cleanedJets);

//--- build collections of generator level particles (after some cuts are applied, to safe computing time)
    if ( isMC && redoGenMatching && !fillGenEvtHistograms ) {
      if ( genLeptonReader ) {
        genLeptons = genLeptonReader->read();
        for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin();
              genLepton != genLeptons.end(); ++genLepton ) {
          int abs_pdgId = std::abs(genLepton->pdgId());
          if      ( abs_pdgId == 11 ) genElectrons.push_back(*genLepton);
          else if ( abs_pdgId == 13 ) genMuons.push_back(*genLepton);
        }
      }
      if ( genHadTauReader ) {
        genHadTaus = genHadTauReader->read();
      }
      if ( genJetReader ) {
        genJets = genJetReader->read();
      }
      if ( genTauReader ) {
	genTaus = genTauReader->read();
      }
      if ( genHiggsBosonReader ) {
	genHiggsBosons = genHiggsBosonReader->read();
      }
    }

//--- match reconstructed to generator level particles
    if ( isMC && redoGenMatching ) {
      muonGenMatcher.addGenLeptonMatch(preselMuons, genLeptons, 0.2);
      muonGenMatcher.addGenHadTauMatch(preselMuons, genHadTaus, 0.2);
      muonGenMatcher.addGenJetMatch(preselMuons, genJets, 0.2);

      electronGenMatcher.addGenLeptonMatch(preselElectrons, genLeptons, 0.2);
      electronGenMatcher.addGenHadTauMatch(preselElectrons, genHadTaus, 0.2);
      electronGenMatcher.addGenJetMatch(preselElectrons, genJets, 0.2);

      hadTauGenMatcher.addGenLeptonMatch(selHadTaus, genLeptons, 0.2);
      hadTauGenMatcher.addGenHadTauMatch(selHadTaus, genHadTaus, 0.2);
      hadTauGenMatcher.addGenJetMatch(selHadTaus, genJets, 0.2);

      jetGenMatcher.addGenLeptonMatch(selJets, genLeptons, 0.2);
      jetGenMatcher.addGenHadTauMatch(selJets, genHadTaus, 0.2);
      jetGenMatcher.addGenJetMatch(selJets, genJets, 0.2);
    }

    RecoMEt met = metReader->read();
    std::vector<const RecoLepton*> fakeableLeptons = mergeLeptonCollections(fakeableElectrons, fakeableMuons);
    Particle::LorentzVector mht_p4 = compMHT(fakeableLeptons, selHadTaus, selJets);
    double met_LD = compMEt_LD(met.p4(), mht_p4);

//--- compute event-level weight
    double evtWeight = 1.;
    if ( isMC ) {
      evtWeight *= lumiScale;
      if ( apply_genWeight ) evtWeight *= boost::math::sign(eventInfo.genWeight);
      evtWeight *= eventInfo.pileupWeight;
      if ( isDEBUG ) {
        std::cout << "lumiScale = " << lumiScale << std::endl;
        if ( apply_genWeight ) std::cout << "genWeight = " << boost::math::sign(eventInfo.genWeight) << std::endl;
        std::cout << "pileupWeight = " << eventInfo.pileupWeight << std::endl;
	std::cout << "evtWeight = " << evtWeight << std::endl;
      }
    }

    int idxCategory = get_idxCategory(selLeptons.size(), selHadTaus.size());
    selHistManagerType* selHistManager = selHistManagers[idxCategory];
    assert(selHistManager != 0);
    selHistManager->electrons_->fillHistograms(selElectrons, evtWeight);
    selHistManager->leadElectron_->fillHistograms(selElectrons, evtWeight);
    selHistManager->subleadElectron_->fillHistograms(selElectrons, evtWeight);
    selHistManager->muons_->fillHistograms(selMuons, evtWeight);
    selHistManager->leadMuon_->fillHistograms(selMuons, evtWeight);
    selHistManager->subleadMuon_->fillHistograms(selMuons, evtWeight);
    selHistManager->hadTaus_->fillHistograms(selHadTaus, evtWeight);
    selHistManager->leadHadTau_->fillHistograms(selHadTaus, evtWeight);
    selHistManager->subleadHadTau_->fillHistograms(selHadTaus, evtWeight);
    selHistManager->jets_->fillHistograms(selJets, evtWeight);
    selHistManager->leadJet_->fillHistograms(selJets, evtWeight);
    selHistManager->subleadJet_->fillHistograms(selJets, evtWeight);
    selHistManager->BJets_loose_->fillHistograms(selBJets_loose, evtWeight);
    selHistManager->BJets_medium_->fillHistograms(selBJets_medium, evtWeight);
    selHistManager->met_->fillHistograms(met, mht_p4, met_LD, evtWeight);
    selHistManager->weights_->fillHistograms("genWeight", eventInfo.genWeight);
    selHistManager->weights_->fillHistograms("pileupWeight", eventInfo.pileupWeight);

    std::vector<const GenParticle*> measuredTaus;
    std::vector<const RecoLepton*> selLeptons_toAdd = pickFirstNobjects(selLeptons, 4);
    measuredTaus.insert(measuredTaus.end(), selLeptons_toAdd.begin(), selLeptons_toAdd.end());
    if ( selLeptons_toAdd.size() < 4 ) {
      std::vector<const RecoHadTau*> selHadTaus_toAdd = pickFirstNobjects(selHadTaus, 4 - selLeptons_toAdd.size());
      measuredTaus.insert(measuredTaus.end(), selHadTaus_toAdd.begin(), selHadTaus_toAdd.end());
    }
    if ( measuredTaus.size() >= 4 ) {
      for ( std::vector<const GenParticle*>::const_iterator measuredTau1 = measuredTaus.begin();
	    measuredTau1 != measuredTaus.end(); ++measuredTau1 ) {
	for ( std::vector<const GenParticle*>::const_iterator measuredTau2 = measuredTau1 + 1;
	      measuredTau2 != measuredTaus.end(); ++measuredTau2 ) {
	  // require decay products of 1st Higgs boson to have opposite charge
	  if ( ((*measuredTau1)->charge() + (*measuredTau2)->charge()) != 0 ) continue;
	  for ( std::vector<const GenParticle*>::const_iterator measuredTau3 = measuredTaus.begin();
		measuredTau3 != measuredTaus.end(); ++measuredTau3 ) {
	    for ( std::vector<const GenParticle*>::const_iterator measuredTau4 = measuredTau3 + 1;
		  measuredTau4 != measuredTaus.end(); ++measuredTau4 ) {
	      // require decay products of 2nd Higgs boson to have opposite charge
	      if ( ((*measuredTau3)->charge() + (*measuredTau4)->charge()) != 0 ) continue;

	      // require that all taus are different
	      if ( (*measuredTau3) == (*measuredTau1) || (*measuredTau3) == (*measuredTau2) ) continue;
	      if ( (*measuredTau4) == (*measuredTau1) || (*measuredTau4) == (*measuredTau2) ) continue;
	      
	      // require charge of all decay products to sum to zero
	      if ( ((*measuredTau1)->charge() + (*measuredTau2)->charge() + (*measuredTau3)->charge() + (*measuredTau4)->charge()) != 0 ) continue;
	      
	      // require that tau1 has higher pT than tau3,
	      // in order prevent that SVfit mass is computed for both combinations (tau1,..,tau3,..) and (tau3,..,tau1,..)
	      if ( !((*measuredTau1)->pt() > (*measuredTau3)->pt()) ) continue;
	      
	      // match reconstructed tau decay products to generator-level ones
	      const GenParticle* genTau1 = findGenTau(**measuredTau1, genTaus);
	      const GenParticle* genTau2 = findGenTau(**measuredTau2, genTaus);
	      const GenParticle* genTau3 = findGenTau(**measuredTau3, genTaus);
	      const GenParticle* genTau4 = findGenTau(**measuredTau4, genTaus);

	      // require that no generator-level tau decay product is matched twice
	      if ( genTau2 == genTau1 || genTau3 == genTau1 || genTau4 == genTau1 || 
		   genTau3 == genTau2 || genTau4 == genTau2 || genTau4 == genTau3 ) continue; 
	      
	      // require that no generator-level tau decay product is unmatched
	      if ( !(genTau1 && genTau2 && genTau3 && genTau4) ) continue;
	      
	      //-------------------------------------------------------------------------------------
	      // CV: run ClassicSVfit4tau algorithm
	      double metPx = met.pt()*TMath::Cos(met.phi());
	      double metPy = met.pt()*TMath::Sin(met.phi());
	      
	      TMatrixD metCov(2,2);
	      metCov[0][0] = met.covXX();
	      metCov[1][0] = met.covXY();
	      metCov[0][1] = met.covXY();
	      metCov[1][1] = met.covYY();
	      
	      std::vector<classic_svFit::MeasuredTauLepton> measuredTauLeptons;
	      measuredTauLeptons.push_back(makeMeasuredTauLepton(**measuredTau1));
	      measuredTauLeptons.push_back(makeMeasuredTauLepton(**measuredTau2));
	      measuredTauLeptons.push_back(makeMeasuredTauLepton(**measuredTau3));
	      measuredTauLeptons.push_back(makeMeasuredTauLepton(**measuredTau4));
	      
	      int verbosity = 1;
	      ClassicSVfit4tau svFitAlgo(verbosity);
	      double massContraint = 125.;
	      if ( logM_wMassConstraint > 0. ) {
		svFitAlgo.addLogM_fixed(true, logM_wMassConstraint);
	      } else {
		svFitAlgo.addLogM_fixed(false);
	      }
	      svFitAlgo.setDiTau1MassConstraint(massContraint);
	      svFitAlgo.setDiTau2MassConstraint(massContraint);  
	      svFitAlgo.integrate(measuredTauLeptons, metPx, metPy, metCov);
	      bool isValidSolution_wMassConstaint = svFitAlgo.isValidSolution();
	      classic_svFit::LorentzVector dihiggsP4_wMassConstaint = static_cast<classic_svFit::HistogramAdapterDiHiggs*>(svFitAlgo.getHistogramAdapter())->getP4();
	      classic_svFit::LorentzVector higgs1P4_wMassConstaint = static_cast<classic_svFit::HistogramAdapterDiHiggs*>(svFitAlgo.getHistogramAdapter())->ditau1()->getP4();
	      classic_svFit::LorentzVector higgs2P4_wMassConstaint = static_cast<classic_svFit::HistogramAdapterDiHiggs*>(svFitAlgo.getHistogramAdapter())->ditau2()->getP4();
	      if ( logM_woMassConstraint > 0. ) {
		svFitAlgo.addLogM_fixed(true, logM_woMassConstraint);
	      } else {
		svFitAlgo.addLogM_fixed(false);
	      }
	      svFitAlgo.setDiTau1MassConstraint(-1.);
	      svFitAlgo.setDiTau2MassConstraint(-1.);
	      svFitAlgo.integrate(measuredTauLeptons, metPx, metPy, metCov);
	      bool isValidSolution_woMassConstaint = svFitAlgo.isValidSolution();
	      classic_svFit::LorentzVector dihiggsP4_woMassConstaint = static_cast<classic_svFit::HistogramAdapterDiHiggs*>(svFitAlgo.getHistogramAdapter())->getP4();
	      classic_svFit::LorentzVector higgs1P4_woMassConstaint = static_cast<classic_svFit::HistogramAdapterDiHiggs*>(svFitAlgo.getHistogramAdapter())->ditau1()->getP4();
	      classic_svFit::LorentzVector higgs2P4_woMassConstaint = static_cast<classic_svFit::HistogramAdapterDiHiggs*>(svFitAlgo.getHistogramAdapter())->ditau2()->getP4();
	      //-------------------------------------------------------------------------------------
	      
	      const GenParticle* genHiggs1 = nullptr;
	      const GenParticle* genHiggs2 = nullptr;	      
	      bool isCorrectAssoc = false;
	      Particle::LorentzVector genDiHiggsP4;
	      if ( (genTau1->charge() + genTau2->charge()) == 0 && TMath::Abs((genTau1->p4() + genTau2->p4()).mass() - 125.) < 10. &&
		   (genTau3->charge() + genTau4->charge()) == 0 && TMath::Abs((genTau3->p4() + genTau4->p4()).mass() - 125.) < 10. ) {
		genHiggs1 = findGenHiggs(genTau1->p4() + genTau2->p4(), genHiggsBosons);
		genHiggs2 = findGenHiggs(genTau3->p4() + genTau4->p4(), genHiggsBosons);
		isCorrectAssoc = (genHiggs1 && genHiggs2);
		if ( isCorrectAssoc ) {
		  genDiHiggsP4 = genHiggs1->p4() + genHiggs2->p4();
		}
	      }
	      
	      SVfit4tauDiHiggsHistManager* histograms_dihiggs_wMassContraint = nullptr;
	      SVfit4tauHiggsHistManager* histograms_higgs1_wMassContraint = nullptr;
	      SVfit4tauHiggsHistManager* histograms_higgs2_wMassContraint = nullptr;
	      SVfit4tauDiHiggsHistManager* histograms_dihiggs_woMassContraint = nullptr;
	      SVfit4tauHiggsHistManager* histograms_higgs1_woMassContraint = nullptr;
	      SVfit4tauHiggsHistManager* histograms_higgs2_woMassContraint = nullptr;	      
	      const Particle::LorentzVector* genHiggs1P4 = nullptr;
	      const Particle::LorentzVector* genHiggs2P4 = nullptr;
	      if ( isCorrectAssoc ) {
		histograms_dihiggs_wMassContraint = selHistManager->dihiggs_wMassContraint_correctAssoc_;
		histograms_higgs1_wMassContraint = selHistManager->higgs1_wMassContraint_correctAssoc_;
		histograms_higgs2_wMassContraint = selHistManager->higgs2_wMassContraint_correctAssoc_;
		histograms_dihiggs_woMassContraint = selHistManager->dihiggs_woMassContraint_correctAssoc_;
		histograms_higgs1_woMassContraint = selHistManager->higgs1_woMassContraint_correctAssoc_;
		histograms_higgs2_woMassContraint = selHistManager->higgs2_woMassContraint_correctAssoc_;
		genHiggs1P4 = &genHiggs1->p4();
		genHiggs2P4 = &genHiggs2->p4();
	      } else {
		histograms_dihiggs_wMassContraint = selHistManager->dihiggs_wMassContraint_incorrectAssoc_;
		histograms_higgs1_wMassContraint = selHistManager->higgs1_wMassContraint_incorrectAssoc_;
		histograms_higgs2_wMassContraint = selHistManager->higgs2_wMassContraint_incorrectAssoc_;
		histograms_dihiggs_woMassContraint = selHistManager->dihiggs_woMassContraint_incorrectAssoc_;
		histograms_higgs1_woMassContraint = selHistManager->higgs1_woMassContraint_incorrectAssoc_;
		histograms_higgs2_woMassContraint = selHistManager->higgs2_woMassContraint_incorrectAssoc_;
	      }
	      if ( isValidSolution_wMassConstaint ) {
		histograms_dihiggs_wMassContraint->fillHistograms(dihiggsP4_wMassConstaint, evtWeight, isCorrectAssoc ? &genDiHiggsP4 : nullptr);
		histograms_higgs1_wMassContraint->fillHistograms(higgs1P4_wMassConstaint, evtWeight, genHiggs1P4);
		histograms_higgs2_wMassContraint->fillHistograms(higgs2P4_wMassConstaint, evtWeight, genHiggs2P4);
	      }
	      if ( isValidSolution_woMassConstaint ) {
		histograms_dihiggs_woMassContraint->fillHistograms(dihiggsP4_woMassConstaint, evtWeight, isCorrectAssoc ? &genDiHiggsP4 : nullptr);
		histograms_higgs1_woMassContraint->fillHistograms(higgs1P4_woMassConstaint, evtWeight, genHiggs1P4);
		histograms_higgs2_woMassContraint->fillHistograms(higgs2P4_woMassConstaint, evtWeight, genHiggs2P4);
	      }
	    }
	  }
	}
      }
    }
    
    if ( isMC ) {
      genEvtHistManager_afterCuts->fillHistograms(genElectrons, genMuons, genHadTaus, genJets);
    }
    
    ++selectedEntries;
    selectedEntries_weighted += evtWeight;
    histogram_selectedEntries->Fill(0.);
  }
  
  std::cout << "max num. Entries = " << inputTree->getCumulativeMaxEventCount()
            << " (limited by " << maxEvents << ") processed in "
            << inputTree->getProcessedFileCount() << " file(s) (out of "
            << inputTree->getFileCount() << ")\n"
            << " analyzed = " << analyzedEntries << '\n'
            << " selected = " << selectedEntries << " (weighted = " << selectedEntries_weighted << ")\n\n";

  delete run_lumi_eventSelector;

  delete muonReader;
  delete electronReader;
  delete hadTauReader;
  delete jetReader;
  delete metReader;
  delete genLeptonReader;
  delete genHadTauReader;
  delete genJetReader;
  delete genTauReader;
  delete genHiggsBosonReader;

  delete genEvtHistManager_beforeCuts;
  delete genEvtHistManager_afterCuts;

  delete inputTree;

  clock.Show("analyze_SVfit4tau");

  return EXIT_SUCCESS;
}
