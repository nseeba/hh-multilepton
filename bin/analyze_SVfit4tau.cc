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
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauReader.h" // RecoHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTauReader.h" // GenHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/GenPhotonReader.h" // GenPhotonReader
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
#include "tthAnalysis/HiggsToTauTau/interface/sysUncertOptions.h" // getHadTauPt_option, getMET_option
#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper

#include "hhAnalysis/tttt/interface/EvtHistManager_SVfit4tau.h" // EvtHistManager_SVfit4tau
#include "hhAnalysis/tttt/interface/SVfit4tauDiHiggsResolutionHistManager.h" // SVfit4tauDiHiggsResolutionHistManager
#include "hhAnalysis/tttt/interface/SVfit4tauHiggsResolutionHistManager.h" // SVfit4tauHiggsResolutionHistManager
#include "hhAnalysis/tttt/interface/GenHadTauSmearer.h" // GenHadTauSmearer
#include "hhAnalysis/tttt/interface/GenMEtSmearer.h" // GenMEtSmearer
#include "hhAnalysis/tttt/interface/mySVfit4tauAuxFunctions.h" // getMeasuredTauLeptonType, getHadTauDecayMode

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

enum { kMode_undefined, kMode_rec, kMode_gen, kMode_genSmeared };

enum { k4lepton, k3lepton_1tau, k2lepton_2tau, k1lepton_3tau, k4tau };

int get_idxCategory(const std::string& category) 
{
  if      ( category == "4lepton"      ) return k4lepton;
  else if ( category == "3lepton_1tau" ) return k3lepton_1tau;
  else if ( category == "2lepton_2tau" ) return k2lepton_2tau;
  else if ( category == "1lepton_3tau" ) return k1lepton_3tau;
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

const GenParticle* getGenMeasuredTau(const GenParticle& measuredTau)
{
  const GenParticle* measuredTau_gen = nullptr;
  if ( dynamic_cast<const RecoLepton*>(&measuredTau) ) {
    const RecoLepton* measuredLepton = dynamic_cast<const RecoLepton*>(&measuredTau);
    if      ( measuredLepton->genLepton() ) measuredTau_gen = measuredLepton->genLepton();
    else if ( measuredLepton->genHadTau() ) measuredTau_gen = measuredLepton->genHadTau();
  } else if ( dynamic_cast<const RecoLepton*>(&measuredTau) ) {
    const RecoHadTau* measuredHadTau = dynamic_cast<const RecoHadTau*>(&measuredTau);
    if      ( measuredHadTau->genLepton() ) measuredTau_gen = measuredHadTau->genLepton();
    else if ( measuredHadTau->genHadTau() ) measuredTau_gen = measuredHadTau->genHadTau();
  } else assert(0);
  return measuredTau_gen;
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

  std::string mode_string = cfg_analyze.getParameter<std::string>("mode");
  int mode = kMode_undefined;
  if      ( mode_string == "rec"         ) mode = kMode_rec;
  else if ( mode_string == "gen"         ) mode = kMode_gen;
  else if ( mode_string == "gen_smeared" ) mode = kMode_genSmeared;
  else throw cms::Exception("analyze_SVfit4tau")
    << "Invalid Configuration parameter 'mode' = " << mode_string << " !!\n";

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
 
  edm::ParameterSet cfgSVfit4tau = cfg_analyze.getParameter<edm::ParameterSet>("SVfit4tau");
  double logM_wMassConstraint = cfgSVfit4tau.getParameter<double>("logM_wMassConstraint");
  double logM_woMassConstraint = cfgSVfit4tau.getParameter<double>("logM_woMassConstraint");

  bool use_HIP_mitigation_mediumMuonId = cfg_analyze.getParameter<bool>("use_HIP_mitigation_mediumMuonId");
  std::cout << "use_HIP_mitigation_mediumMuonId = " << use_HIP_mitigation_mediumMuonId << std::endl;

  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  std::string central_or_shift = cfg_analyze.getParameter<std::string>("central_or_shift");
  double lumiScale = ( process_string != "data_obs" ) ? cfg_analyze.getParameter<double>("lumiScale") : 1.;
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");

  bool isDEBUG = ( cfg_analyze.exists("isDEBUG") ) ? cfg_analyze.getParameter<bool>("isDEBUG") : false;
  if ( isDEBUG ) std::cout << "Warning: DEBUG mode enabled -> trigger selection will not be applied for data !!" << std::endl;

  const int hadTauPt_option = getHadTauPt_option(central_or_shift);
  const int met_option = getMET_option(central_or_shift, isMC);

  bool fillGenEvtHistograms = cfg_analyze.getParameter<bool>("fillGenEvtHistograms");

  std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_hadTaus = cfg_analyze.getParameter<std::string>("branchName_hadTaus");
  std::string branchName_jets = cfg_analyze.getParameter<std::string>("branchName_jets");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");

  std::string branchName_genLeptons = cfg_analyze.getParameter<std::string>("branchName_genLeptons1");
  std::string branchName_genLeptons2 = cfg_analyze.getParameter<std::string>("branchName_genLeptons2");
  std::string branchName_genHadTaus = cfg_analyze.getParameter<std::string>("branchName_genHadTaus");
  std::string branchName_genPhotons = cfg_analyze.getParameter<std::string>("branchName_genPhotons");
  std::string branchName_genJets = cfg_analyze.getParameter<std::string>("branchName_genJets");
  bool redoGenMatching = cfg_analyze.getParameter<bool>("redoGenMatching");

  std::string branchName_genTaus = cfg_analyze.getParameter<std::string>("branchName_genTaus");
  std::string branchName_genHiggsBosons = cfg_analyze.getParameter<std::string>("branchName_genHiggsBosons");

  edm::ParameterSet cfgGenHadTauSmearing = cfg_analyze.getParameter<edm::ParameterSet>("genHadTauSmearing");
  GenHadTauSmearer genHadTauSmearer(cfgGenHadTauSmearing);
  edm::ParameterSet cfgGenMEtSmearing = cfg_analyze.getParameter<edm::ParameterSet>("genMEtSmearing");
  GenMEtSmearer genMEtSmearer(cfgGenMEtSmearing);
  double sigmaX = cfgGenMEtSmearing.getParameter<double>("sigmaX");
  double sigmaY = cfgGenMEtSmearing.getParameter<double>("sigmaY");

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
  GenPhotonReader* genPhotonReader = 0;
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
      if ( branchName_genPhotons != "" ) {
        genPhotonReader = new GenPhotonReader(branchName_genPhotons);
        inputTree -> registerReader(genPhotonReader);
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
    SVfit4tauDiHiggsResolutionHistManager* dihiggs_wMassContraint_correctAssoc_;
    SVfit4tauHiggsResolutionHistManager* higgs1_wMassContraint_correctAssoc_;
    SVfit4tauHiggsResolutionHistManager* higgs2_wMassContraint_correctAssoc_;
    SVfit4tauDiHiggsResolutionHistManager* dihiggs_wMassContraint_incorrectAssoc_;
    SVfit4tauHiggsResolutionHistManager* higgs1_wMassContraint_incorrectAssoc_;
    SVfit4tauHiggsResolutionHistManager* higgs2_wMassContraint_incorrectAssoc_;
    SVfit4tauDiHiggsResolutionHistManager* dihiggs_woMassContraint_correctAssoc_;
    SVfit4tauHiggsResolutionHistManager* higgs1_woMassContraint_correctAssoc_;
    SVfit4tauHiggsResolutionHistManager* higgs2_woMassContraint_correctAssoc_;
    SVfit4tauDiHiggsResolutionHistManager* dihiggs_woMassContraint_incorrectAssoc_;
    SVfit4tauHiggsResolutionHistManager* higgs1_woMassContraint_incorrectAssoc_;
    SVfit4tauHiggsResolutionHistManager* higgs2_woMassContraint_incorrectAssoc_;  
    EvtHistManager_SVfit4tau* evt_;
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
      Form("%s/%s/electrons", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->electrons_->bookHistograms(fs);
    selHistManager->leadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/leadElectron", histogramDir_category.Data(), mode_string.data()), central_or_shift, 0));
    selHistManager->leadElectron_->bookHistograms(fs);
    selHistManager->subleadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/subleadElectron", histogramDir_category.Data(), mode_string.data()), central_or_shift, 1));
    selHistManager->subleadElectron_->bookHistograms(fs);
    selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/muons", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->muons_->bookHistograms(fs);
    selHistManager->leadMuon_ = new MuonHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/leadMuon", histogramDir_category.Data(), mode_string.data()), central_or_shift, 0));
    selHistManager->leadMuon_->bookHistograms(fs);
    selHistManager->subleadMuon_ = new MuonHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/subleadMuon", histogramDir_category.Data(), mode_string.data()), central_or_shift, 1));
    selHistManager->subleadMuon_->bookHistograms(fs);
    selHistManager->hadTaus_ = new HadTauHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/hadTaus", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->hadTaus_->bookHistograms(fs);
    selHistManager->leadHadTau_ = new HadTauHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/leadHadTau", histogramDir_category.Data(), mode_string.data()), central_or_shift, 0));
    selHistManager->leadHadTau_->bookHistograms(fs);
    selHistManager->subleadHadTau_ = new HadTauHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/subleadHadTau", histogramDir_category.Data(), mode_string.data()), central_or_shift, 1));
    selHistManager->subleadHadTau_->bookHistograms(fs);
    selHistManager->jets_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/jets", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->jets_->bookHistograms(fs);
    selHistManager->leadJet_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/leadJet", histogramDir_category.Data(), mode_string.data()), central_or_shift, 0));
    selHistManager->leadJet_->bookHistograms(fs);
    selHistManager->subleadJet_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/subleadJet", histogramDir_category.Data(), mode_string.data()), central_or_shift, 1));
    selHistManager->subleadJet_->bookHistograms(fs);
    selHistManager->BJets_loose_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/BJets_loose", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->BJets_loose_->bookHistograms(fs);
    selHistManager->BJets_medium_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/BJets_medium", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->BJets_medium_->bookHistograms(fs);
    selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/met", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->met_->bookHistograms(fs);
    selHistManager->dihiggs_wMassContraint_correctAssoc_ = new SVfit4tauDiHiggsResolutionHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/dihiggs_wMassContraint_correctAssoc", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->dihiggs_wMassContraint_correctAssoc_->bookHistograms(fs);
    selHistManager->higgs1_wMassContraint_correctAssoc_ = new SVfit4tauHiggsResolutionHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs1_wMassContraint_correctAssoc", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->higgs1_wMassContraint_correctAssoc_->bookHistograms(fs);
    selHistManager->higgs2_wMassContraint_correctAssoc_ = new SVfit4tauHiggsResolutionHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs2_wMassContraint_correctAssoc", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->higgs2_wMassContraint_correctAssoc_->bookHistograms(fs);
    selHistManager->dihiggs_wMassContraint_incorrectAssoc_ = new SVfit4tauDiHiggsResolutionHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/dihiggs_wMassContraint_incorrectAssoc", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->dihiggs_wMassContraint_incorrectAssoc_->bookHistograms(fs);
    selHistManager->higgs1_wMassContraint_incorrectAssoc_ = new SVfit4tauHiggsResolutionHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs1_wMassContraint_incorrectAssoc", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->higgs1_wMassContraint_incorrectAssoc_->bookHistograms(fs);
    selHistManager->higgs2_wMassContraint_incorrectAssoc_ = new SVfit4tauHiggsResolutionHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs2_wMassContraint_incorrectAssoc", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->higgs2_wMassContraint_incorrectAssoc_->bookHistograms(fs);
    selHistManager->dihiggs_woMassContraint_correctAssoc_ = new SVfit4tauDiHiggsResolutionHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/dihiggs_woMassContraint_correctAssoc", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->dihiggs_woMassContraint_correctAssoc_->bookHistograms(fs);
    selHistManager->higgs1_woMassContraint_correctAssoc_ = new SVfit4tauHiggsResolutionHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs1_woMassContraint_correctAssoc", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->higgs1_woMassContraint_correctAssoc_->bookHistograms(fs);
    selHistManager->higgs2_woMassContraint_correctAssoc_ = new SVfit4tauHiggsResolutionHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs2_woMassContraint_correctAssoc", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->higgs2_woMassContraint_correctAssoc_->bookHistograms(fs);
    selHistManager->dihiggs_woMassContraint_incorrectAssoc_ = new SVfit4tauDiHiggsResolutionHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/dihiggs_woMassContraint_incorrectAssoc", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->dihiggs_woMassContraint_incorrectAssoc_->bookHistograms(fs);
    selHistManager->higgs1_woMassContraint_incorrectAssoc_ = new SVfit4tauHiggsResolutionHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs1_woMassContraint_incorrectAssoc", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->higgs1_woMassContraint_incorrectAssoc_->bookHistograms(fs);
    selHistManager->higgs2_woMassContraint_incorrectAssoc_ = new SVfit4tauHiggsResolutionHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/higgs2_woMassContraint_incorrectAssoc", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->higgs2_woMassContraint_incorrectAssoc_->bookHistograms(fs);    
    selHistManager->evt_ = new EvtHistManager_SVfit4tau(makeHistManager_cfg(process_string,
      Form("%s/%s/evt", histogramDir_category.Data(), mode_string.data()), central_or_shift));
    selHistManager->evt_->bookHistograms(fs);
    selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/weights", histogramDir_category.Data(), mode_string.data()), central_or_shift));
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
    std::vector<GenPhoton> genPhotons;
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
      if ( genPhotonReader ) {
        genPhotons = genPhotonReader->read();
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
      genEvtHistManager_beforeCuts->fillHistograms(genElectrons, genMuons, genHadTaus, genPhotons, genJets);
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
	      
	      const GenParticle* measuredTau1_gen = getGenMeasuredTau(**measuredTau1);
	      const GenParticle* measuredTau2_gen = getGenMeasuredTau(**measuredTau2);
	      const GenParticle* measuredTau3_gen = getGenMeasuredTau(**measuredTau3);
	      const GenParticle* measuredTau4_gen = getGenMeasuredTau(**measuredTau4);

	      bool isGenMatched = (measuredTau1_gen && measuredTau2_gen && measuredTau3_gen && measuredTau4_gen);
	      if ( !isGenMatched ) continue;

	      Particle::LorentzVector measuredTau1P4_gen = measuredTau1_gen->p4();
	      Particle::LorentzVector measuredTau2P4_gen = measuredTau2_gen->p4();
	      Particle::LorentzVector measuredTau3P4_gen = measuredTau3_gen->p4();
	      Particle::LorentzVector measuredTau4P4_gen = measuredTau4_gen->p4();
	      
	      double metPx_gen = 
		 (genTau1->p4().px() - measuredTau1P4_gen.px()) 
               + (genTau2->p4().px() - measuredTau2P4_gen.px()) 
               + (genTau3->p4().px() - measuredTau3P4_gen.px()) 
               + (genTau4->p4().px() - measuredTau4P4_gen.px());
	      double metPy_gen = 
                 (genTau1->p4().py() - measuredTau1P4_gen.py()) 
               + (genTau2->p4().py() - measuredTau2P4_gen.py()) 
               + (genTau3->p4().py() - measuredTau3P4_gen.py()) 
               + (genTau4->p4().py() - measuredTau4P4_gen.py());

	      Particle::LorentzVector measuredTau1P4_rec;
	      int measuredTau1Type_rec = classic_svFit::MeasuredTauLepton::kUndefinedDecayType;
	      int measuredHadTau1DecayMode = -1;
	      Particle::LorentzVector measuredTau2P4_rec;
	      int measuredTau2Type_rec = classic_svFit::MeasuredTauLepton::kUndefinedDecayType;
	      int measuredHadTau2DecayMode = -1;
	      Particle::LorentzVector measuredTau3P4_rec;
	      int measuredTau3Type_rec = classic_svFit::MeasuredTauLepton::kUndefinedDecayType;
	      int measuredHadTau3DecayMode = -1;
	      Particle::LorentzVector measuredTau4P4_rec;
	      int measuredTau4Type_rec = classic_svFit::MeasuredTauLepton::kUndefinedDecayType;
	      int measuredHadTau4DecayMode = -1;
	      double metPx_rec, metPy_rec;
	      TMatrixD metCov(2,2);
	      if ( mode == kMode_rec ) {
		measuredTau1P4_rec = (*measuredTau1)->p4();
		measuredTau1Type_rec = getMeasuredTauLeptonType(**measuredTau1);
		if ( isGenHadTau(**measuredTau1) ) measuredHadTau1DecayMode = getHadTauDecayMode(**measuredTau1);
		measuredTau2P4_rec = (*measuredTau2)->p4();
		measuredTau2Type_rec = getMeasuredTauLeptonType(**measuredTau2);
		if ( isGenHadTau(**measuredTau2) ) measuredHadTau1DecayMode = getHadTauDecayMode(**measuredTau2);
		measuredTau3P4_rec = (*measuredTau3)->p4();
		measuredTau3Type_rec = getMeasuredTauLeptonType(**measuredTau3);
		if ( isGenHadTau(**measuredTau3) ) measuredHadTau1DecayMode = getHadTauDecayMode(**measuredTau3);
		measuredTau4P4_rec = (*measuredTau4)->p4();
		measuredTau4Type_rec = getMeasuredTauLeptonType(**measuredTau4);
		if ( isGenHadTau(**measuredTau4) ) measuredHadTau1DecayMode = getHadTauDecayMode(**measuredTau4);
		metPx_rec = met.pt()*TMath::Cos(met.phi());
		metPy_rec = met.pt()*TMath::Sin(met.phi());
		metCov[0][0] = met.covXX();
		metCov[1][0] = met.covXY();
		metCov[0][1] = met.covXY();
		metCov[1][1] = met.covYY();
	      } else if ( mode == kMode_gen || mode == kMode_genSmeared ) {
		assert(isGenMatched);
		if ( mode == kMode_gen ) {
		  measuredTau1P4_rec = measuredTau1P4_gen;
		  measuredTau2P4_rec = measuredTau2P4_gen;
		  measuredTau3P4_rec = measuredTau3P4_gen;
		  measuredTau4P4_rec = measuredTau4P4_gen;
		  metPx_rec = metPx_gen;
		  metPy_rec = metPy_gen;
		} else if ( mode == kMode_genSmeared ) {
		  measuredTau1P4_rec = ( isGenHadTau(*measuredTau1_gen) ) ? genHadTauSmearer(measuredTau1P4_gen) : measuredTau1P4_gen;
		  measuredTau2P4_rec = ( isGenHadTau(*measuredTau2_gen) ) ? genHadTauSmearer(measuredTau2P4_gen) : measuredTau2P4_gen;
		  measuredTau3P4_rec = ( isGenHadTau(*measuredTau3_gen) ) ? genHadTauSmearer(measuredTau3P4_gen) : measuredTau3P4_gen;
		  measuredTau4P4_rec = ( isGenHadTau(*measuredTau4_gen) ) ? genHadTauSmearer(measuredTau4P4_gen) : measuredTau4P4_gen;
		  std::pair<double, double> metPxPy_rec = genMEtSmearer(metPx_gen, metPy_gen);
		  metPx_rec = metPxPy_rec.first;
		  metPy_rec = metPxPy_rec.second;
		} else assert(0);
		measuredTau1Type_rec = getMeasuredTauLeptonType(*measuredTau1_gen);
		if ( isGenHadTau(*measuredTau1_gen) ) measuredHadTau1DecayMode = getHadTauDecayMode(*measuredTau1_gen);
		measuredTau2Type_rec = getMeasuredTauLeptonType(*measuredTau2_gen);
		if ( isGenHadTau(*measuredTau2_gen) ) measuredHadTau2DecayMode = getHadTauDecayMode(*measuredTau2_gen);
		measuredTau3Type_rec = getMeasuredTauLeptonType(*measuredTau3_gen);
		if ( isGenHadTau(*measuredTau3_gen) ) measuredHadTau3DecayMode = getHadTauDecayMode(*measuredTau3_gen);
		measuredTau4Type_rec = getMeasuredTauLeptonType(*measuredTau4_gen);
		if ( isGenHadTau(*measuredTau4_gen) ) measuredHadTau4DecayMode = getHadTauDecayMode(*measuredTau4_gen);
		metCov[0][0] = square(sigmaX);
		metCov[1][0] = 0.;
		metCov[0][1] = 0.;
		metCov[1][1] = square(sigmaY);
	      } else assert(0);

	      //-------------------------------------------------------------------------------------
	      // CV: run ClassicSVfit4tau algorithm
	      std::vector<classic_svFit::MeasuredTauLepton> measuredTauLeptons;
	      measuredTauLeptons.push_back(makeMeasuredTauLepton(measuredTau1P4_rec, measuredTau1Type_rec, measuredHadTau1DecayMode));
	      measuredTauLeptons.push_back(makeMeasuredTauLepton(measuredTau2P4_rec, measuredTau2Type_rec, measuredHadTau2DecayMode));
	      measuredTauLeptons.push_back(makeMeasuredTauLepton(measuredTau3P4_rec, measuredTau3Type_rec, measuredHadTau3DecayMode));
	      measuredTauLeptons.push_back(makeMeasuredTauLepton(measuredTau4P4_rec, measuredTau4Type_rec, measuredHadTau4DecayMode));
	      
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
	      svFitAlgo.integrate(measuredTauLeptons, metPx_rec, metPy_rec, metCov);
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
	      svFitAlgo.integrate(measuredTauLeptons, metPx_rec, metPy_rec, metCov);
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
	      
	      SVfit4tauDiHiggsResolutionHistManager* histograms_dihiggs_wMassContraint = nullptr;
	      SVfit4tauHiggsResolutionHistManager* histograms_higgs1_wMassContraint = nullptr;
	      SVfit4tauHiggsResolutionHistManager* histograms_higgs2_wMassContraint = nullptr;
	      SVfit4tauDiHiggsResolutionHistManager* histograms_dihiggs_woMassContraint = nullptr;
	      SVfit4tauHiggsResolutionHistManager* histograms_higgs1_woMassContraint = nullptr;
	      SVfit4tauHiggsResolutionHistManager* histograms_higgs2_woMassContraint = nullptr;	      
	      const Particle::LorentzVector* genHiggs1P4 = nullptr;
	      const Particle::LorentzVector* genHiggs2P4 = nullptr;
	      if ( isCorrectAssoc ) {
		selHistManager->evt_->fillHistograms(
                  measuredTau1P4_rec, measuredTau1P4_gen, 
		  measuredTau2P4_rec, measuredTau2P4_gen,  
		  measuredTau3P4_rec, measuredTau3P4_gen,  
		  measuredTau4P4_rec, measuredTau4P4_gen,  
		  metPx_rec, metPy_rec, metCov, metPx_gen, metPy_gen, 
		  evtWeight);
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
      genEvtHistManager_afterCuts->fillHistograms(genElectrons, genMuons, genHadTaus, genPhotons, genJets);
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
  delete genPhotonReader;
  delete genTauReader;
  delete genHiggsBosonReader;

  delete genEvtHistManager_beforeCuts;
  delete genEvtHistManager_afterCuts;

  delete inputTree;

  clock.Show("analyze_SVfit4tau");

  return EXIT_SUCCESS;
}
