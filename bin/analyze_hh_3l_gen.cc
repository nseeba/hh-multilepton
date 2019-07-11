/*   Debug verion
 *   version to test AK8 collection events
 *   Date: 20190130
 */
 

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
#include <TError.h> // gErrorAbortLevel, kError
#include <TLorentzVector.h>
#include <TMath.h>

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h" // RecoHadTau
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h" // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface
#include "tthAnalysis/HiggsToTauTau/interface/XGBInterface.h" // XGBInterface
#include "tthAnalysis/HiggsToTauTau/interface/mvaAuxFunctions.h" // check_mvaInputs, get_mvaInputVariables
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // auxiliary functions for computing input variables of the MVA used for signal extraction in the 3l category
#include "tthAnalysis/HiggsToTauTau/interface/LeptonFakeRateInterface.h" // LeptonFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/JetToTauFakeRateInterface.h" // JetToTauFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauReader.h" // RecoHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterReader.h" // MEtFilterReader
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTauReader.h" // GenHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/GenPhotonReader.h" // GenPhotonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoReader.h" // LHEInfoReader
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
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterSelector.h" // MEtFilterSelector
#include "tthAnalysis/HiggsToTauTau/interface/ElectronHistManager.h" // ElectronHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MuonHistManager.h" // MuonHistManager
#include "tthAnalysis/HiggsToTauTau/interface/HadTauHistManager.h" // HadTauHistManager
#include "tthAnalysis/HiggsToTauTau/interface/JetHistManager.h" // JetHistManager
#include "tthAnalysis/HiggsToTauTau/interface/JetHistManagerAK8.h" // JetHistManagerAK8
#include "tthAnalysis/HiggsToTauTau/interface/MEtHistManager.h" // MEtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterHistManager.h" // MEtFilterHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MVAInputVarHistManager.h" // MVAInputVarHistManager
#include "tthAnalysis/HiggsToTauTau/interface/EvtYieldHistManager.h" // EvtYieldHistManager
#include "tthAnalysis/HiggsToTauTau/interface/CutFlowTableHistManager.h" // CutFlowTableHistManager
#include "tthAnalysis/HiggsToTauTau/interface/WeightHistManager.h" // WeightHistManager
#include "tthAnalysis/HiggsToTauTau/interface/GenEvtHistManager.h" // GenEvtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoHistManager.h" // LHEInfoHistManager
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // getLeptonType, kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched
#include "tthAnalysis/HiggsToTauTau/interface/leptonGenMatchingAuxFunctions.h" // getLeptonGenMatch_definitions_3lepton, getLeptonGenMatch_string, getLeptonGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h" // getWeight_3L
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath, create_hltPaths, hltPaths_isTriggered, hltPaths_delete
#include "tthAnalysis/HiggsToTauTau/interface/hltPathReader.h" // hltPathReader
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2016.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2017.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2018.h"
#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // loadTH2, get_sf_from_TH2
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/L1PreFiringWeightReader.h" // L1PreFiringWeightReader
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/hltFilter.h" // hltFilter()
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // findGenLepton_and_NeutrinoFromWBoson

#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj
#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_3l.h" // EvtHistManager_hh_3l
#include "hhAnalysis/multilepton/interface/EventInfoHH.h" // EventInfoHH
#include "hhAnalysis/multilepton/interface/EventInfoHHReader.h" // EventInfoHHReader

#include <boost/math/special_functions/sign.hpp> // boost::math::sign()
#include <boost/algorithm/string/predicate.hpp> // boost::starts_with()

#include <iostream> // std::cerr, std::fixed
#include <iomanip> // std::setprecision(), std::setw()
#include <string> // std::string
#include <vector> // std::vector<>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <fstream> // std::ofstream
#include <assert.h> // assert
#include <array> // std::array<>
#include <tuple> // std::tuple<>, std::get<>(), std::make_tuple()
#include <TH2.h> // TH2

#define DoNotUsehh_3lConditions // uncomment this if 2lss_1tau rec-level selection conditions are not required

typedef math::PtEtaPhiMLorentzVector LV;
typedef std::vector<std::string> vstring;

enum { kFR_disabled, kFR_3lepton };

const double wBosonMass = 80.379; // GeV

//const int hadTauSelection_antiElectron = 1; // vLoose
//const int hadTauSelection_antiMuon = 1; // Loose
const int hadTauSelection_antiElectron = -1; // not applied
const int hadTauSelection_antiMuon = -1; // not applied


void dumpGenParticles(const std::string& label, const std::vector<GenParticle>& particles)
{
  for ( size_t idxParticle = 0; idxParticle < particles.size(); ++idxParticle ) {
    std::cout << label << " #" << idxParticle << ":" << " ";
    std::cout << particles[idxParticle];
    std::cout << std::endl;
  }
}

void printWjj(const std::vector<const RecoJetAK8*>& jets_ak8, const RecoJetCollectionSelectorAK8_hh_Wjj& jetSelectorAK8_Wjj, 
	      const std::vector<GenParticle>& genWBosons, const std::vector<GenParticle>& genWJets)
{
  std::cout << "<printWjj>:" << std::endl;
  std::cout << "#genWBosons = " << genWBosons.size() << std::endl;
  for ( size_t idxWBoson = 0; idxWBoson < genWBosons.size(); ++idxWBoson ) {
    const GenParticle& genWBoson = genWBosons[idxWBoson];
    std::cout << " genWBoson #" << idxWBoson << ": pT = " << genWBoson.pt() << ", eta = " << genWBoson.eta() << ", phi = " << genWBoson.phi() << std::endl;   
  }
  std::cout << "#genWJets = " << genWJets.size() << std::endl;  
  for ( size_t idxWJet = 0; idxWJet < genWJets.size(); ++idxWJet ) {
    const GenParticle& genWJet = genWJets[idxWJet];
    std::cout << " genWJet #" << idxWJet << ": pT = " << genWJet.pt() << ", eta = " << genWJet.eta() << ", phi = " << genWJet.phi() << std::endl;   
  }
  /*if ( genWBosons.size() == 1 ) {
    bool isMatched = false;
    Particle::LorentzVector genWjjP4 = genWBosons[0].p4();
    std::cout << "genWjj: pT = " << genWjjP4.pt() << ", eta = " << genWjjP4.eta() << ", phi = " << genWjjP4.phi() << std::endl;*/
  for ( size_t idxWBoson = 0; idxWBoson < genWBosons.size(); ++idxWBoson ) {
    bool isMatched = false;
    Particle::LorentzVector genWjjP4 = genWBosons[idxWBoson].p4();
    std::cout << "genWBoson id: " << idxWBoson << std::endl;
    std::cout << "genWjj: pT = " << genWjjP4.pt() << ", eta = " << genWjjP4.eta() << ", phi = " << genWjjP4.phi() << std::endl;
    
    for ( std::vector<const RecoJetAK8*>::const_iterator jet_ak8 = jets_ak8.begin();
	  jet_ak8 != jets_ak8.end(); ++jet_ak8 ) {
      double dR = deltaR(genWjjP4, (*jet_ak8)->p4());
      if ( dR < 0.8 ) {
	std::cout << "matches reconstructed AK8 jet: pT = " << (*jet_ak8)->pt() << ", eta = " << (*jet_ak8)->eta() << ", phi = " << (*jet_ak8)->phi() << ","
		  << " msoftdrop = " << (*jet_ak8)->msoftdrop() << ", tau21 = " << (*jet_ak8)->tau2()/(*jet_ak8)->tau1() << ", which ";
	if ( jetSelectorAK8_Wjj.getSelector()(**jet_ak8) ) {
	  std::cout << "PASSES";
	  isMatched = true;
	} else { 
	  std::cout << "FAILS";
	}
	std::cout << " the W->jj jet selection." << std::endl;
	std::cout << "generator-level subjets:" << std::endl;
	for ( std::vector<GenParticle>::const_iterator genWJet1 = genWJets.begin();
	      genWJet1 != genWJets.end(); ++genWJet1 ) {
	  for ( std::vector<GenParticle>::const_iterator genWJet2 = genWJet1 + 1;
		genWJet2 != genWJets.end(); ++genWJet2 ) {
	    if ( deltaR(genWJet1->p4() + genWJet2->p4(), genWjjP4) < 1.e-1 && std::fabs((genWJet1->p4() + genWJet2->p4()).mass() - genWjjP4.mass()) < 1.e+1 ) {
	      std::cout << " genWJet #1: pT = " << genWJet1->pt() << ", eta = " << genWJet1->eta() << ", phi = " << genWJet1->phi() << std::endl;   
	      std::cout << " genWJet #2: pT = " << genWJet2->pt() << ", eta = " << genWJet2->eta() << ", phi = " << genWJet2->phi() << std::endl;   
	    }
	  } 
	}  
	std::cout << "reconstructed subjets:" << std::endl;
	const RecoSubjetAK8* subjet1 = (*jet_ak8)->subJet1();
	if ( subjet1 ) std::cout << " subjet #1: pT = " << subjet1->pt() << ", eta = " << subjet1->eta() << ", phi = " << subjet1->phi() << std::endl;
	const RecoSubjetAK8* subjet2 = (*jet_ak8)->subJet2();
	if ( subjet2 ) std::cout << " subjet #2: pT = " << subjet2->pt() << ", eta = " << subjet2->eta() << ", phi = " << subjet2->phi() << std::endl;
      }
    }
    if ( genWjjP4.pt() > 100. && !isMatched ) std::cout << "--> DEBUG (Wjj) !!" << std::endl;    
  }
}


std::pair<const GenLepton*, const GenParticle*> 
findGenLepton_and_NeutrinoFromWBoson_1(const GenParticle* genWBoson, const std::vector<GenLepton>& genLeptons, const std::vector<GenParticle>& genNeutrinos)
{
  const GenLepton* genLeptonFromWBoson = nullptr;
  const GenParticle* genNeutrinoFromWBoson = nullptr;
  double minDeltaMass = 1.e+3;
  for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin();
	genLepton != genLeptons.end(); ++genLepton ) {
    for ( std::vector<GenParticle>::const_iterator genNeutrino = genNeutrinos.begin();
	  genNeutrino != genNeutrinos.end(); ++genNeutrino ) {
      Particle::LorentzVector genLepton_and_NeutrinoP4 = genLepton->p4() + genNeutrino->p4();
      double deltaMass = TMath::Abs(genLepton_and_NeutrinoP4.mass() - genWBoson->mass());
      double dR = deltaR(genLepton_and_NeutrinoP4, genWBoson->p4());
      //if ( deltaMass < 5 && deltaMass < minDeltaMass && dR < 1. ) {
      if ( deltaMass < 1. && deltaMass < minDeltaMass && dR < 0.01 ) {
	genLeptonFromWBoson = &(*genLepton);
	genNeutrinoFromWBoson = &(*genNeutrino);
	minDeltaMass = deltaMass;
      }
    }
  }
  if (genLeptonFromWBoson && genNeutrinoFromWBoson && 0==1) {
    std::cout<<"W->l nu matching: m(W):"<<genWBoson->mass()<<", m(l nu): "<<(genLeptonFromWBoson->p4()+genNeutrinoFromWBoson->p4()).mass()<<", dR(W, l nu): "<<deltaR((genLeptonFromWBoson->p4()+genNeutrinoFromWBoson->p4()), genWBoson->p4())<<std::endl;
  }
  return std::pair<const GenLepton*, const GenParticle*>(genLeptonFromWBoson, genNeutrinoFromWBoson);
}


/**
 * @brief Produce datacard and control plots for 3l categories.
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

  std::cout << "<analyze_hh_3l_gen>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_3l_gen");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_hh_3l_gen")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_3l_gen");

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  bool isMC_ttH = process_string == "TTH";
  bool isMC_tH = process_string == "TH";
  bool isSignal = boost::starts_with(process_string, "signal_");

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");
  bool isMCClosure_e = histogramDir.find("mcClosure_e") != std::string::npos;
  bool isMCClosure_m = histogramDir.find("mcClosure_m") != std::string::npos;

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const int era = get_era(era_string);

  // single lepton triggers
  vstring triggerNames_1e = cfg_analyze.getParameter<vstring>("triggers_1e");
  std::vector<hltPath*> triggers_1e = create_hltPaths(triggerNames_1e, "triggers_1e");
  bool use_triggers_1e = cfg_analyze.getParameter<bool>("use_triggers_1e");
  vstring triggerNames_1mu = cfg_analyze.getParameter<vstring>("triggers_1mu");
  std::vector<hltPath*> triggers_1mu = create_hltPaths(triggerNames_1mu, "triggers_1mu");
  bool use_triggers_1mu = cfg_analyze.getParameter<bool>("use_triggers_1mu");
  // double lepton triggers
  vstring triggerNames_2e = cfg_analyze.getParameter<vstring>("triggers_2e");
  std::vector<hltPath*> triggers_2e = create_hltPaths(triggerNames_2e, "triggers_2e");
  bool use_triggers_2e = cfg_analyze.getParameter<bool>("use_triggers_2e");
  vstring triggerNames_1e1mu = cfg_analyze.getParameter<vstring>("triggers_1e1mu");
  std::vector<hltPath*> triggers_1e1mu = create_hltPaths(triggerNames_1e1mu, "triggers_1e1mu");
  bool use_triggers_1e1mu = cfg_analyze.getParameter<bool>("use_triggers_1e1mu");
  vstring triggerNames_2mu = cfg_analyze.getParameter<vstring>("triggers_2mu");
  std::vector<hltPath*> triggers_2mu = create_hltPaths(triggerNames_2mu, "triggers_2mu");
  bool use_triggers_2mu = cfg_analyze.getParameter<bool>("use_triggers_2mu");
  // triple lepton triggers
  vstring triggerNames_3e = cfg_analyze.getParameter<vstring>("triggers_3e");
  std::vector<hltPath*> triggers_3e = create_hltPaths(triggerNames_3e, "triggers_3e");
  bool use_triggers_3e = cfg_analyze.getParameter<bool>("use_triggers_3e");
  vstring triggerNames_2e1mu = cfg_analyze.getParameter<vstring>("triggers_2e1mu");
  std::vector<hltPath*> triggers_2e1mu = create_hltPaths(triggerNames_2e1mu, "triggers_2e1mu");
  bool use_triggers_2e1mu = cfg_analyze.getParameter<bool>("use_triggers_2e1mu");
  vstring triggerNames_1e2mu = cfg_analyze.getParameter<vstring>("triggers_1e2mu");
  std::vector<hltPath*> triggers_1e2mu = create_hltPaths(triggerNames_1e2mu, "triggers_1e2mu");
  bool use_triggers_1e2mu = cfg_analyze.getParameter<bool>("use_triggers_1e2mu");
  vstring triggerNames_3mu = cfg_analyze.getParameter<vstring>("triggers_3mu");
  std::vector<hltPath*> triggers_3mu = create_hltPaths(triggerNames_3mu, "triggers_3mu");
  bool use_triggers_3mu = cfg_analyze.getParameter<bool>("use_triggers_3mu");

  bool apply_offline_e_trigger_cuts_1e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e");
  bool apply_offline_e_trigger_cuts_1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1mu");
  bool apply_offline_e_trigger_cuts_2e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2e");
  bool apply_offline_e_trigger_cuts_1e1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e1mu");
  bool apply_offline_e_trigger_cuts_2mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2mu");
  bool apply_offline_e_trigger_cuts_3e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_3e");
  bool apply_offline_e_trigger_cuts_2e1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2e1mu");
  bool apply_offline_e_trigger_cuts_1e2mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e2mu");
  bool apply_offline_e_trigger_cuts_3mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_3mu");

  const std::string electronSelection_string = cfg_analyze.getParameter<std::string>("electronSelection");
  const std::string muonSelection_string     = cfg_analyze.getParameter<std::string>("muonSelection");
  std::cout << "electronSelection_string = " << electronSelection_string << "\n"
               "muonSelection_string     = " << muonSelection_string     << '\n'
  ;
  const int electronSelection = get_selection(electronSelection_string);
  const int muonSelection     = get_selection(muonSelection_string);

  bool apply_leptonGenMatching = cfg_analyze.getParameter<bool>("apply_leptonGenMatching");
  std::vector<leptonGenMatchEntry> leptonGenMatch_definitions = getLeptonGenMatch_definitions_3lepton(apply_leptonGenMatching);
  std::cout << "leptonGenMatch_definitions:" << std::endl;
  std::cout << leptonGenMatch_definitions;

  TString hadTauSelection_string = cfg_analyze.getParameter<std::string>("hadTauSelection").data();
  TObjArray* hadTauSelection_parts = hadTauSelection_string.Tokenize("|");
  assert(hadTauSelection_parts->GetEntries() >= 1);
  std::string hadTauSelection_part2 = ( hadTauSelection_parts->GetEntries() == 2 ) ? (dynamic_cast<TObjString*>(hadTauSelection_parts->At(1)))->GetString().Data() : "";
  delete hadTauSelection_parts;

  enum { kOS, kSS };
  std::string chargeSumSelection_string = cfg_analyze.getParameter<std::string>("chargeSumSelection");
  int chargeSumSelection = -1;
  if      ( chargeSumSelection_string == "OS" ) chargeSumSelection = kOS;
  else if ( chargeSumSelection_string == "SS" ) chargeSumSelection = kSS;
  else throw cms::Exception("analyze_hh_3l_gen")
    << "Invalid Configuration parameter 'chargeSumSelection' = " << chargeSumSelection_string << " !!\n";
  std::cout << "chargeSumSelection = " <<  chargeSumSelection << std::endl;
  
  const int minNumJets = 1;

  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  bool hasLHE = cfg_analyze.getParameter<bool>("hasLHE");
  std::string central_or_shift = cfg_analyze.getParameter<std::string>("central_or_shift");
  double lumiScale = ( process_string != "data_obs" ) ? cfg_analyze.getParameter<double>("lumiScale") : 1.;
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");
  bool apply_l1PreFireWeight = cfg_analyze.getParameter<bool>("apply_l1PreFireWeight");
  bool apply_hlt_filter = cfg_analyze.getParameter<bool>("apply_hlt_filter");
  bool apply_met_filters = cfg_analyze.getParameter<bool>("apply_met_filters");  
  edm::ParameterSet cfgMEtFilter = cfg_analyze.getParameter<edm::ParameterSet>("cfgMEtFilter");
  MEtFilterSelector metFilterSelector(cfgMEtFilter, isMC);
  const bool useNonNominal = cfg_analyze.getParameter<bool>("useNonNominal");
  const bool useNonNominal_jetmet = useNonNominal || ! isMC;

  const edm::ParameterSet additionalEvtWeight = cfg_analyze.getParameter<edm::ParameterSet>("evtWeight");
  const bool applyAdditionalEvtWeight = additionalEvtWeight.getParameter<bool>("apply");
  EvtWeightManager * eventWeightManager = nullptr;
  if(applyAdditionalEvtWeight)
  {
    eventWeightManager = new EvtWeightManager(additionalEvtWeight);
  }

  bool isDEBUG = cfg_analyze.getParameter<bool>("isDEBUG");
  if ( isDEBUG ) std::cout << "Warning: DEBUG mode enabled -> trigger selection will not be applied for data !!" << std::endl;

  checkOptionValidity(central_or_shift, isMC);
  const int jetToLeptonFakeRate_option        = getJetToLeptonFR_option       (central_or_shift);
  const int hadTauPt_option                   = getHadTauPt_option            (central_or_shift);
  const int lheScale_option                   = getLHEscale_option            (central_or_shift);
  const int jetBtagSF_option                  = getBTagWeight_option          (central_or_shift);
  const PUsys puSys_option                    = getPUsys_option               (central_or_shift);
  const L1PreFiringWeightSys l1PreFire_option = getL1PreFiringWeightSys_option(central_or_shift);

  const int met_option   = useNonNominal_jetmet ? kMEt_central_nonNominal : getMET_option(central_or_shift, isMC);
  const int jetPt_option = useNonNominal_jetmet ? kJet_central_nonNominal : getJet_option(central_or_shift, isMC);

  std::cout
    << "central_or_shift = "               << central_or_shift             << "\n"
       " -> jetToLeptonFakeRate_option = " << jetToLeptonFakeRate_option   << "\n"
       " -> hadTauPt_option            = " << hadTauPt_option              << "\n"
       " -> lheScale_option            = " << lheScale_option              << "\n"
       " -> jetBtagSF_option           = " << jetBtagSF_option             << "\n"
       " -> met_option                 = " << met_option                   << "\n"
       " -> jetPt_option               = " << jetPt_option                 << "\n"
       " -> puSys_option               = " << as_integer(puSys_option)     << "\n"
       " -> l1PreFire_option           = " << as_integer(l1PreFire_option) << '\n'
  ;

  edm::ParameterSet cfg_dataToMCcorrectionInterface;
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("era", era_string);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("hadTauSelection", hadTauSelection_part2);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiElectron", hadTauSelection_antiElectron);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon", hadTauSelection_antiMuon);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("central_or_shift", central_or_shift);
  Data_to_MC_CorrectionInterface_Base * dataToMCcorrectionInterface = nullptr;
  switch(era)
  {
    case kEra_2016: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2016(cfg_dataToMCcorrectionInterface); break;
    case kEra_2017: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2017(cfg_dataToMCcorrectionInterface); break;
    case kEra_2018: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2018(cfg_dataToMCcorrectionInterface); break;
    default: throw cmsException("analyze_hh_3l_gen", __LINE__) << "Invalid era = " << era;
  }

  std::string applyFakeRateWeights_string = cfg_analyze.getParameter<std::string>("applyFakeRateWeights");
  int applyFakeRateWeights = -1;
  if      ( applyFakeRateWeights_string == "disabled" ) applyFakeRateWeights = kFR_disabled;
  else if ( applyFakeRateWeights_string == "3lepton"  ) applyFakeRateWeights = kFR_3lepton;
  else throw cms::Exception("analyze_hh_3l_gen")
    << "Invalid Configuration parameter 'applyFakeRateWeights' = " << applyFakeRateWeights_string << " !!\n";

  LeptonFakeRateInterface* leptonFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_3lepton) {
    edm::ParameterSet cfg_leptonFakeRateWeight = cfg_analyze.getParameter<edm::ParameterSet>("leptonFakeRateWeight");
    leptonFakeRateInterface = new LeptonFakeRateInterface(cfg_leptonFakeRateWeight, jetToLeptonFakeRate_option);
  }

  bool fillGenEvtHistograms = cfg_analyze.getParameter<bool>("fillGenEvtHistograms");
  edm::ParameterSet cfg_EvtYieldHistManager = cfg_analyze.getParameter<edm::ParameterSet>("cfgEvtYieldHistManager");
  
  std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_hadTaus = cfg_analyze.getParameter<std::string>("branchName_hadTaus");
  //std::string branchName_jets = cfg_analyze.getParameter<std::string>("branchName_jets");
  std::string branchName_jets_ak4 = cfg_analyze.getParameter<std::string>("branchName_jets_ak4");
  std::string branchName_jets_ak8_Wjj = cfg_analyze.getParameter<std::string>("branchName_jets_ak8_Wjj");
  std::string branchName_subjets_ak8_Wjj = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8_Wjj");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");

  std::string branchName_genLeptons = cfg_analyze.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genHadTaus = cfg_analyze.getParameter<std::string>("branchName_genHadTaus");
  std::string branchName_genPhotons = cfg_analyze.getParameter<std::string>("branchName_genPhotons");
  std::string branchName_genJets = cfg_analyze.getParameter<std::string>("branchName_genJets");
  const bool redoGenMatching = cfg_analyze.getParameter<bool>("redoGenMatching");
  std::string branchName_genHiggses = cfg_analyze.getParameter<std::string>("branchName_genHiggses");
  std::string branchName_genNeutrinos = cfg_analyze.getParameter<std::string>("branchName_genNeutrinos");
  
  std::string branchName_genWBosons = cfg_analyze.getParameter<std::string>("branchName_genWBosons");
  std::string branchName_genWJets = cfg_analyze.getParameter<std::string>("branchName_genWJets");
  
  std::string selEventsFileName_input = cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input << std::endl;
  RunLumiEventSelector* run_lumi_eventSelector = 0;
  if ( selEventsFileName_input != "" ) {
    edm::ParameterSet cfgRunLumiEventSelector;
    cfgRunLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfgRunLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfgRunLumiEventSelector);
  }

  std::string selEventsFileName_output = cfg_analyze.getParameter<std::string>("selEventsFileName_output");
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

  fwlite::InputSource inputFiles(cfg);
  int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper * inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);

  std::cout << "Loaded " << inputTree -> getFileCount() << " file(s).\n";

//--- declare event-level variables
  EventInfoHH eventInfo(isMC, isSignal);
  EventInfoHHReader eventInfoReader(&eventInfo, puSys_option);
  inputTree -> registerReader(&eventInfoReader);

  hltPathReader hltPathReader_instance({ triggers_1e, triggers_1mu, triggers_2e, triggers_1e1mu, triggers_2mu, triggers_3e, triggers_2e1mu, triggers_1e2mu, triggers_3mu });
  inputTree -> registerReader(&hltPathReader_instance);

  if(eventWeightManager)
  {
    inputTree->registerReader(eventWeightManager);
  }

  L1PreFiringWeightReader * l1PreFiringWeightReader = nullptr;
  if(apply_l1PreFireWeight)
  {
    l1PreFiringWeightReader = new L1PreFiringWeightReader(era, l1PreFire_option);
    inputTree->registerReader(l1PreFiringWeightReader);
  }
  
//--- declare particle collections
  const bool readGenObjects = isMC && !redoGenMatching;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  inputTree -> registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  electronReader->readUncorrected(useNonNominal);
  inputTree -> registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.05, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era, -1, isDEBUG);

  RecoHadTauReader* hadTauReader = new RecoHadTauReader(era, branchName_hadTaus, isMC, readGenObjects);
  hadTauReader->setHadTauPt_central_or_shift(hadTauPt_option);
  inputTree -> registerReader(hadTauReader);
  RecoHadTauCollectionGenMatcher hadTauGenMatcher;
  RecoHadTauCollectionCleaner hadTauCleaner(0.3, isDEBUG);
  RecoHadTauCollectionSelectorLoose preselHadTauSelector(era, -1, isDEBUG);
  preselHadTauSelector.set_if_looser(hadTauSelection_part2);
  preselHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  preselHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  RecoHadTauCollectionSelectorFakeable fakeableHadTauSelector(era, -1, isDEBUG);
  fakeableHadTauSelector.set_if_looser(hadTauSelection_part2);
  fakeableHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  fakeableHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  RecoHadTauCollectionSelectorTight tightHadTauSelector(era, -1, isDEBUG);
  if ( hadTauSelection_part2 != "" ) tightHadTauSelector.set(hadTauSelection_part2);
  tightHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  tightHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);

  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, readGenObjects);
  jetReaderAK4->setPtMass_central_or_shift(jetPt_option);
  jetReaderAK4->setBranchName_BtagWeight(jetBtagSF_option);
  inputTree->registerReader(jetReaderAK4);
  RecoJetCollectionGenMatcher jetGenMatcherAK4;
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR08(0.8, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR12(1.2, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4(era, -1, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4_vbf(era, -1, isDEBUG);
  //jetSelectorAK4_vbf.getSelector().set_min_pt(30.);
  jetSelectorAK4_vbf.getSelector().set_max_absEta(4.7);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);
  
  // refer analyze_hh_bb1l.cc macro
  RecoJetReaderAK8* jetReaderAK8_Wjj = new RecoJetReaderAK8(era, branchName_jets_ak8_Wjj, branchName_subjets_ak8_Wjj);
  // TO-DO: implement jet energy scale uncertainties, b-tag weights,  
  //        and jet  pT and (softdrop) mass corrections described in Section 3.4.3 of AN-2018/058 (v4)
  inputTree->registerReader(jetReaderAK8_Wjj);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR16(1.6, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_Wjj jetSelectorAK8_Wjj(era, -1, isDEBUG);
  
  //--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(met_option);
  inputTree -> registerReader(metReader);

  MEtFilter metFilters;
  MEtFilterReader* metFilterReader = new MEtFilterReader(&metFilters, era);
  inputTree -> registerReader(metFilterReader);

  std::cout << "readGenObjects: " << readGenObjects<< ",  redoGenMatching: " << redoGenMatching << ",  fillGenEvtHistograms: "<< fillGenEvtHistograms << std::endl;
  GenLeptonReader* genLeptonReader = 0;
  GenHadTauReader* genHadTauReader = 0;
  GenPhotonReader* genPhotonReader = 0;
  GenJetReader* genJetReader = 0;
  GenParticleReader* genHiggsReader = 0;
  GenParticleReader* genNeutrinoReader = nullptr;
  LHEInfoReader* lheInfoReader = 0;
  if ( isMC ) {
    //if ( ! readGenObjects ) {
    if (1==1) { // Edited by Siddhesh
      if ( branchName_genLeptons != "" ) {
        genLeptonReader = new GenLeptonReader(branchName_genLeptons);
        inputTree -> registerReader(genLeptonReader);
      }
      if ( branchName_genHadTaus != "" ) {
        genHadTauReader = new GenHadTauReader(branchName_genHadTaus);
        inputTree -> registerReader(genHadTauReader);
      }
      if ( branchName_genPhotons != "" ) {
        genPhotonReader = new GenPhotonReader(branchName_genPhotons);
        inputTree -> registerReader(genPhotonReader);
      }
      if ( branchName_genJets != "" ) {
        genJetReader = new GenJetReader(branchName_genJets);
        inputTree -> registerReader(genJetReader);
      }
      if ( branchName_genNeutrinos != "" ) {
	genNeutrinoReader = new GenParticleReader(branchName_genNeutrinos);
	inputTree->registerReader(genNeutrinoReader);
      }
    }
    if ( branchName_genHiggses != "" ) {
      genHiggsReader = new GenParticleReader(branchName_genHiggses);
      inputTree->registerReader(genHiggsReader);
    }
	 
    lheInfoReader = new LHEInfoReader(hasLHE);
    inputTree -> registerReader(lheInfoReader);
  }

  const std::vector<edm::ParameterSet> tHweights = cfg_analyze.getParameterSetVector("tHweights");
  if((isMC_tH || isMC_ttH) && ! tHweights.empty())
  {
    eventInfo.loadWeight_tH(tHweights);
  }

  GenParticleReader* genWBosonReader = nullptr;
  GenParticleReader* genWJetReader = nullptr;
  if ( isMC ) {
    genWBosonReader = new GenParticleReader(branchName_genWBosons);
    inputTree->registerReader(genWBosonReader);
    genWJetReader = new GenParticleReader(branchName_genWJets);
    inputTree->registerReader(genWJetReader);
  }
  
	/*
//--- initialize BDTs used to discriminate ttH vs. ttV and ttH vs. ttbar
//    in 3l category of ttH multilepton analysis
  std::string mvaFileName_3l_ttV = "tthAnalysis/HiggsToTauTau/data/3l_ttV_BDTG.weights.xml";
  std::vector<std::string> mvaInputVariables_3l_ttV;
  mvaInputVariables_3l_ttV.push_back("max(abs(LepGood_eta[iF_Recl[0]]),abs(LepGood_eta[iF_Recl[1]]))");
  mvaInputVariables_3l_ttV.push_back("MT_met_lep1");
  mvaInputVariables_3l_ttV.push_back("nJet25_Recl");
  mvaInputVariables_3l_ttV.push_back("mindr_lep1_jet");
  mvaInputVariables_3l_ttV.push_back("mindr_lep2_jet");
  mvaInputVariables_3l_ttV.push_back("LepGood_conePt[iF_Recl[0]]");
  mvaInputVariables_3l_ttV.push_back("LepGood_conePt[iF_Recl[2]]");
  TMVAInterface mva_3l_ttV(mvaFileName_3l_ttV, mvaInputVariables_3l_ttV, { "iF_Recl[0]", "iF_Recl[1]", "iF_Recl[2]" });

  std::string mvaFileName_3l_ttbar = "tthAnalysis/HiggsToTauTau/data/3l_ttbar_BDTG.weights.xml";
  std::vector<std::string> mvaInputVariables_3l_ttbar;
  mvaInputVariables_3l_ttbar.push_back("max(abs(LepGood_eta[iF_Recl[0]]),abs(LepGood_eta[iF_Recl[1]]))");
  mvaInputVariables_3l_ttbar.push_back("MT_met_lep1");
  mvaInputVariables_3l_ttbar.push_back("nJet25_Recl");
  mvaInputVariables_3l_ttbar.push_back("mhtJet25_Recl");
  mvaInputVariables_3l_ttbar.push_back("avg_dr_jet");
  mvaInputVariables_3l_ttbar.push_back("mindr_lep1_jet");
  mvaInputVariables_3l_ttbar.push_back("mindr_lep2_jet");
  TMVAInterface mva_3l_ttbar(mvaFileName_3l_ttbar, mvaInputVariables_3l_ttbar, { "iF_Recl[0]", "iF_Recl[1]", "iF_Recl[2]" });

  std::vector<std::string> mvaInputVariables_3l = get_mvaInputVariables(mvaInputVariables_3l_ttV, mvaInputVariables_3l_ttbar); 
  std::map<std::string, double> mvaInputs_3l;
	*/

  
  std::string mvaFileName_hh_3l_SUMBk_HH = "hhAnalysis/multilepton/data/3l_0tau_HH_XGB_noTopness_evtLevelSUM_HH_res_26Var.pkl";
  std::vector<std::string> mvaInputs_hh_3l_SUMBk_HH = {
    "lep1_conePt", "lep1_eta", "mindr_lep1_jet", "mT_lep1",
    "lep2_conePt", "lep2_eta", "mindr_lep2_jet", "mT_lep2",
    "lep3_conePt", "lep3_eta", "mindr_lep3_jet", "mT_lep3",
    "avg_dr_jet", "dr_leps", "dr_lss", "dr_los1", "dr_los2",
    "met_LD", "m_jj", "diHiggsMass", "mTMetLepton1", "mTMetLepton2",
    "nJet", "nElectron", "sumLeptonCharge", "numSameFlavor_OS"
  };
  XGBInterface mva_xgb_hh_3l_SUMBk_HH(mvaFileName_hh_3l_SUMBk_HH, mvaInputs_hh_3l_SUMBk_HH);


  

  bool selectBDT = ( cfg_analyze.exists("selectBDT") ) ? cfg_analyze.getParameter<bool>("selectBDT") : false;
	
	
//--- open output file containing run:lumi:event numbers of events passing final event selection criteria
  std::ostream* selEventsFile = ( selEventsFileName_output != "" ) ? new std::ofstream(selEventsFileName_output.data(), std::ios::out) : 0;
  
  std::cout << "process: " << process_string << std::endl;
//--- declare histograms
  struct selHistManagerType
  {
    ElectronHistManager* electrons_;
    std::map<std::string, ElectronHistManager*> electrons_in_categories_;
    MuonHistManager* muons_;
    std::map<std::string, MuonHistManager*> muons_in_categories_;
    HadTauHistManager* hadTaus_;
    JetHistManager* jetsAK4_;
    JetHistManager* leadJetAK4_;
    JetHistManager* subleadJetAK4_;
    JetHistManagerAK8* jetsAK8_Wjj_;
    JetHistManager* BJetsAK4_loose_;
    JetHistManager* leadBJetAK4_loose_;
    JetHistManager* subleadBJetAK4_loose_;
    JetHistManager* BJetsAK4_medium_;
    MEtHistManager* met_;
    MEtFilterHistManager* metFilters_;
    //MVAInputVarHistManager* mvaInputVariables_3l_;
    EvtHistManager_hh_3l* evt_;
    std::map<std::string, EvtHistManager_hh_3l*> evt_in_categories_;
		std::map<std::string, EvtHistManager_hh_3l*> evt_in_decayModes_;
    std::map<std::string, std::map<std::string, EvtHistManager_hh_3l*>> evt_in_categories_and_decayModes_; // key = category, decayMode
    EvtYieldHistManager* evtYield_;
    WeightHistManager* weights_;
  };
  std::map<int, selHistManagerType*> selHistManagers;

  for ( std::vector<leptonGenMatchEntry>::const_iterator leptonGenMatch_definition = leptonGenMatch_definitions.begin();
	leptonGenMatch_definition != leptonGenMatch_definitions.end(); ++leptonGenMatch_definition ) {

    std::string process_and_genMatch = process_string;
    if ( apply_leptonGenMatching ) process_and_genMatch += leptonGenMatch_definition->name_;
    std::cout<<"process_and_genMatch: "<<process_and_genMatch<<std::endl;
    
    int idxLepton = leptonGenMatch_definition->idx_;

    selHistManagerType* selHistManager = new selHistManagerType();
    selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/electrons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
    selHistManager->electrons_->bookHistograms(fs);
    selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/muons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
    selHistManager->muons_->bookHistograms(fs);
    selHistManager->hadTaus_ = new HadTauHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/hadTaus", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
    selHistManager->hadTaus_->bookHistograms(fs);
    selHistManager->jetsAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/jetsAK4", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
    selHistManager->jetsAK4_->bookHistograms(fs);
    selHistManager->leadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/leadJetAK4", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
    selHistManager->leadJetAK4_->bookHistograms(fs);
    selHistManager->subleadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/subleadJetAK4", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
    selHistManager->subleadJetAK4_->bookHistograms(fs);    
    selHistManager->jetsAK8_Wjj_ = new JetHistManagerAK8(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/jetsAK8_Wjj", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
    selHistManager->jetsAK8_Wjj_->bookHistograms(fs);    
    selHistManager->BJetsAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/BJetsAK4_loose", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
    selHistManager->BJetsAK4_loose_->bookHistograms(fs);
    selHistManager->leadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/leadBJetAK4_loose", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
    selHistManager->leadBJetAK4_loose_->bookHistograms(fs);
    selHistManager->subleadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/subleadBJetAK4_loose", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
    selHistManager->subleadBJetAK4_loose_->bookHistograms(fs);
    selHistManager->BJetsAK4_medium_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/BJetsAK4_medium", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
    selHistManager->BJetsAK4_medium_->bookHistograms(fs);  
    selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/met", histogramDir.data()), era_string, central_or_shift));
    selHistManager->met_->bookHistograms(fs);
    selHistManager->metFilters_ = new MEtFilterHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/metFilters", histogramDir.data()), era_string, central_or_shift));
    selHistManager->metFilters_->bookHistograms(fs);
    //selHistManager->mvaInputVariables_3l_ = new MVAInputVarHistManager(makeHistManager_cfg(process_and_genMatch,
		//Form("%s/sel/mvaInputs_3l", histogramDir.data()), era_string, central_or_shift));
    //selHistManager->mvaInputVariables_3l_->bookHistograms(fs, mvaInputVariables_3l);

    selHistManager->evt_ = new EvtHistManager_hh_3l(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift));
    selHistManager->evt_->bookHistograms(fs);
    vstring categories_evt = { 
      "hh_3lneg", "hh_3lpos",
      "hh_3l_Geq1j", "hh_3l_Only1j", "hh_3l_Geq2j",
      "hh_3l_nonVBF", "hh_3l_VBF"		 
    };
    for ( vstring::const_iterator category = categories_evt.begin();
	  category != categories_evt.end(); ++category ) {
      TString histogramDir_category = histogramDir.data();
      histogramDir_category.ReplaceAll("hh_3l", Form("%s", category->data()));
      selHistManager->evt_in_categories_[*category] = new EvtHistManager_hh_3l(makeHistManager_cfg(process_and_genMatch, 
        Form("%s/sel/evt", histogramDir_category.Data()), era_string, central_or_shift));
      selHistManager->evt_in_categories_[*category]->bookHistograms(fs);
    }
    const vstring decayModes_evt = eventInfo.getDiHiggsDecayModes();
    if(isSignal)
    {
      for(const std::string & decayMode_evt: decayModes_evt)
      {
	std::string decayMode_and_genMatch = decayMode_evt;
	if ( apply_leptonGenMatching ) decayMode_and_genMatch += leptonGenMatch_definition -> name_;
        
	selHistManager -> evt_in_decayModes_[decayMode_evt] = new EvtHistManager_hh_3l(makeHistManager_cfg(
          decayMode_and_genMatch,
	  Form("%s/sel/evt", histogramDir.data()),
	  era_string,
	  central_or_shift
        ));
	selHistManager -> evt_in_decayModes_[decayMode_evt] -> bookHistograms(fs);

	for ( vstring::const_iterator category = categories_evt.begin();
	      category != categories_evt.end(); ++category ) {
	  TString histogramDir_category = histogramDir.data();
	  histogramDir_category.ReplaceAll("hh_3l", Form("%s", category->data()));
	  selHistManager -> evt_in_categories_and_decayModes_[*category][decayMode_evt] = new EvtHistManager_hh_3l(makeHistManager_cfg(
            decayMode_and_genMatch,
	    Form("%s/sel/evt", histogramDir_category.Data()),
	    era_string,
	    central_or_shift
          ));
	  selHistManager -> evt_in_categories_and_decayModes_[*category][decayMode_evt] -> bookHistograms(fs);
	}
      }
    }

		
    edm::ParameterSet cfg_EvtYieldHistManager_sel = makeHistManager_cfg(process_and_genMatch, 
      Form("%s/sel/evtYield", histogramDir.data()), era_string, central_or_shift);
    cfg_EvtYieldHistManager_sel.addParameter<edm::ParameterSet>("runPeriods", cfg_EvtYieldHistManager);
    cfg_EvtYieldHistManager_sel.addParameter<bool>("isMC", isMC);
    selHistManager->evtYield_ = new EvtYieldHistManager(cfg_EvtYieldHistManager_sel);
    selHistManager->evtYield_->bookHistograms(fs);
    selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(process_and_genMatch,
      Form("%s/sel/weights", histogramDir.data()), era_string, central_or_shift));
    selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight", "triggerWeight", "data_to_MC_correction", "fakeRate" });
    selHistManagers[idxLepton] = selHistManager;
  }

  GenEvtHistManager* genEvtHistManager_beforeCuts = 0;
  GenEvtHistManager* genEvtHistManager_afterCuts = 0;
  LHEInfoHistManager* lheInfoHistManager = 0;
  if ( isMC ) {
    genEvtHistManager_beforeCuts = new GenEvtHistManager(makeHistManager_cfg(process_string,
      Form("%s/unbiased/genEvt", histogramDir.data()), era_string, central_or_shift));
    genEvtHistManager_beforeCuts->bookHistograms(fs);
    genEvtHistManager_afterCuts = new GenEvtHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/genEvt", histogramDir.data()), era_string, central_or_shift));
    genEvtHistManager_afterCuts->bookHistograms(fs);
    lheInfoHistManager = new LHEInfoHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/lheInfo", histogramDir.data()), era_string, central_or_shift));
    lheInfoHistManager->bookHistograms(fs);

    if(eventWeightManager)
    {
      genEvtHistManager_beforeCuts->bookHistograms(fs, eventWeightManager);
      genEvtHistManager_afterCuts->bookHistograms(fs, eventWeightManager);
    }
  }
  
  NtupleFillerBDT<float, int> * bdt_filler = nullptr;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::int_type   int_type;
  if ( selectBDT ) {
    bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
      makeHistManager_cfg(process_string, Form("%s/sel/evtntuple", histogramDir.data()), era_string, central_or_shift)
    );
    bdt_filler -> register_variable<float_type>(
      "lep1_pt", "lep1_conePt", "lep1_eta", "lep1_tth_mva", "mindr_lep1_jet", "mT_lep1", 
      "lep2_pt", "lep2_conePt", "lep2_eta", "lep2_tth_mva", "mindr_lep2_jet", "mT_lep2",
      "lep3_pt", "lep3_conePt", "lep3_eta", "lep3_tth_mva", "mindr_lep3_jet", "mT_lep3", 
      "avg_dr_jet", "ptmiss",  "htmiss", "dr_leps",
      "lumiScale", "genWeight", "evtWeight",
      "lep1_genLepPt", "lep2_genLepPt", "lep3_genLepPt",
      "lep1_fake_prob", "lep2_fake_prob", "lep3_fake_prob",
      "lep1_frWeight", "lep2_frWeight", "lep3_frWeight",  
      //"mvaOutput_3l_ttV", "mvaOutput_3l_ttbar", "mvaDiscr_3l",
      "mbb_loose", "mbb_medium",
      "dr_lss", "dr_los1", "dr_los2",
      "met", "mht", "met_LD", "HT", "STMET",
      "mSFOS2l", "m_jj", "diHiggsVisMass", "diHiggsMass",
      "mTMetLepton1", "mTMetLepton2",
      "vbf_m_jj", "vbf_dEta_jj", "numSelJets_nonVBF"			
						);
    bdt_filler -> register_variable<int_type>(
      "nJet", "nBJetLoose", "nBJetMedium", "nElectron", "nMuon",
      "lep1_isTight", "lep2_isTight", "lep3_isTight",
      "sumLeptonCharge", "numSameFlavor_OS", "isVBF"
					      );
    bdt_filler -> bookTree(fs);
  }
  
  int analyzedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  TH1* histogram_analyzedEntries = fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  TH1* histogram_selectedEntries = fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  cutFlowTableType cutFlowTable;
  const edm::ParameterSet cutFlowTableCfg = makeHistManager_cfg(
    process_string, Form("%s/sel/cutFlow", histogramDir.data()), era_string, central_or_shift
  );
  const std::vector<std::string> cuts = {
    "run:ls:event selection",
    "trigger",
    ">= 3 presel leptons",
    "presel lepton trigger match",
    ">= 2 jets (1)",
    ">= 2 loose b-jets || 1 medium b-jet (1)",
    "3 sel leptons",
    "fakeable lepton trigger match",
    "HLT filter matching",
    ">= 2 jets (2)",
    ">= 2 loose b-jets || 1 medium b-jet (2)",
    "sel tau veto",
    "m(ll) > 12 GeV",
    "lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV && third lepton pT > 10 GeV",
    "sel lepton charge",
    "Z-boson mass veto",
    "H->ZZ*->4l veto",
    "met LD",
    "MEt filters",
    "signal region veto",
  };
  CutFlowTableHistManager * cutFlowHistManager = new CutFlowTableHistManager(cutFlowTableCfg, cuts);
  cutFlowHistManager->bookHistograms(fs);


  
  //TH1*  = fs.make<TH1D>("", "", );
  TH1* hdRl3WHadronic_gen_all                     = fs.make<TH1D>("hdRl3WHadronic_gen_all", "",200,0,2.0);
  TH1* hdRl3jFromWjj_gen_all                      = fs.make<TH1D>("hdRl3jFromWjj_gen_all", "",200,0,2.0 );
  TH1* hdRl3WHadronic_gen_BoostedWjj_all          = fs.make<TH1D>("hdRl3WHadronic_gen_BoostedWjj_all", "",200,0,2.0);
  TH1* hdRl3jFromWjj_gen_BoostedWjj_all           = fs.make<TH1D>("hdRl3jFromWjj_gen_BoostedWjj_all", "",200,0,2.0 );
  TH1* hdRl3WHadronic_gen_AK8WjjSelector_all      = fs.make<TH1D>("hdRl3WHadronic_gen_AK8WjjSelector_all", "",200,0,2.0);
  TH1* hdRl3jFromWjj_gen_AK8WjjSelector_all       = fs.make<TH1D>("hdRl3jFromWjj_gen_AK8WjjSelector_all", "",200,0,2.0);
  TH1* hdRl3WHadronic_gen_AK8WjjSelector_Selected = fs.make<TH1D>("hdRl3WHadronic_gen_AK8WjjSelector_Selected", "",200,0,2.0);
  TH1* hdRl3jFromWjj_gen_AK8WjjSelector_Selected  = fs.make<TH1D>("hdRl3jFromWjj_gen_AK8WjjSelector_Selected", "",200,0,2.0);
  TH1* hdRl3WHadronic_gen_AK8WjjSelector_Rejected = fs.make<TH1D>("hdRl3WHadronic_gen_AK8WjjSelector_Rejected", "",200,0,2.0);
  TH1* hdRl3jFromWjj_gen_AK8WjjSelector_Rejected  = fs.make<TH1D>("hdRl3jFromWjj_gen_AK8WjjSelector_Rejected", "",200,0,2.0);

  TH1* hdRl3WHadronic_AK8WjjSelector_all      = fs.make<TH1D>("hdRl3WHadronic_AK8WjjSelector_all", "",200,0,2.0);
  TH1* hdRl3jFromWjj_AK8WjjSelector_all       = fs.make<TH1D>("hdRl3jFromWjj_AK8WjjSelector_all", "",200,0,2.0);
  TH1* hdRl3WHadronic_AK8WjjSelector_Selected = fs.make<TH1D>("hdRl3WHadronic_AK8WjjSelector_Selected", "",200,0,2.0);
  TH1* hdRl3jFromWjj_AK8WjjSelector_Selected  = fs.make<TH1D>("hdRl3jFromWjj_AK8WjjSelector_Selected", "",200,0,2.0);
  TH1* hdRl3WHadronic_AK8WjjSelector_Rejected = fs.make<TH1D>("hdRl3WHadronic_AK8WjjSelector_Rejected", "",200,0,2.0);
  TH1* hdRl3jFromWjj_AK8WjjSelector_Rejected  = fs.make<TH1D>("hdRl3jFromWjj_AK8WjjSelector_Rejected", "",200,0,2.0);

  TH2* hdRl3jFromWjj_vs_RecGenPt_AK8WjjSelector_all       = fs.make<TH2D>("hdRl3jFromWjj_vs_RecGenPt_AK8WjjSelector_all", "",200,0,2.0, 50,0.,3.);
  TH2* hdRl3jFromWjj_vs_RecGenPt_AK8WjjSelector_Selected  = fs.make<TH2D>("hdRl3jFromWjj_vs_RecGenPt_AK8WjjSelector_Selected", "",200,0,2.0, 50,0.,3.);
  TH2* hdRl3jFromWjj_vs_RecGenPt_AK8WjjSelector_Rejected  = fs.make<TH2D>("hdRl3jFromWjj_vs_RecGenPt_AK8WjjSelector_Rejected", "",200,0,2.0, 50,0.,3.);

  
  
  while(inputTree -> hasNextEvent() && (! run_lumi_eventSelector || (run_lumi_eventSelector && ! run_lumi_eventSelector -> areWeDone())))
  {
    if(inputTree -> canReport(reportEvery))
    {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx()
                << " or " << inputTree -> getCurrentEventIdx() << " entry in #"
                << (inputTree -> getProcessedFileCount() - 1)
                << " (" << eventInfo
                << ") file (" << selectedEntries << " Entries selected)\n";
    }
    ++analyzedEntries;
    histogram_analyzedEntries->Fill(0.);

    if (run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo))
    {
      continue;
    }
    cutFlowTable.update("run:ls:event selection");
    cutFlowHistManager->fillHistograms("run:ls:event selection", lumiScale);

    if ( isDEBUG ) {
      std::cout << "event #" << inputTree -> getCurrentMaxEventIdx() << ' ' << eventInfo << '\n';
    }

    if(run_lumi_eventSelector)
    {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx() << ": " << eventInfo << '\n';
      if(inputTree -> isOpen())
      {
        std::cout << "input File = " << inputTree -> getCurrentFileName() << '\n';
      }
    }

//--- build collections of generator level particles (before any cuts are applied, to check distributions in unbiased event samples)
    std::vector<GenLepton> genLeptons;
    std::vector<GenLepton> genElectrons;
    std::vector<GenLepton> genMuons;
    std::vector<GenHadTau> genHadTaus;
    std::vector<GenPhoton> genPhotons;
    std::vector<GenJet> genJets;
    std::vector<GenParticle> genNeutrinos;
    std::vector<GenParticle> genHiggses;
    //if ( isMC && fillGenEvtHistograms) {
    if ( isMC) {
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
      if ( genNeutrinoReader ) {
	genNeutrinos = genNeutrinoReader->read();
      }
      if ( genHiggsReader ) {
        genHiggses = genHiggsReader->read();
      }      
      if ( isDEBUG ) {
        printCollection("genLeptons", genLeptons);
        printCollection("genHadTaus", genHadTaus);
        printCollection("genPhotons", genPhotons);
        printCollection("genJets", genJets);
	printCollection("genHiggses", genHiggses);
      }
    }

    std::vector<GenParticle> genWBosons;
    std::vector<GenParticle> genWJets;
    if ( isMC ) {
      genWBosons = genWBosonReader->read();
      genWJets = genWJetReader->read();
    }
    
    if ( isDEBUG ) {
      //dumpGenParticles("genBJet", genBJets);
      dumpGenParticles("genWBoson", genWBosons);
      dumpGenParticles("genWJet", genWJets);
    }


    if ( !((int)genHiggses.size() == 2 && (int)genWBosons.size()>=4)) {
      if ( isDEBUG ) {
	printf("Not HH->4W event: genHiggses.size(): %i, genWBosons.size(): %i \n",
	       (int)genHiggses.size(), (int)genWBosons.size());
      }
      continue;
    }
    cutFlowTable.update("genHH = 2, genW >= 4");


    
    const GenParticle* genWHadronicFromH_WW_qqlnu = nullptr;
    const GenParticle* genJet1FromH_WW_qqlnu = nullptr;
    const GenParticle* genJet2FromH_WW_qqlnu = nullptr;
    const GenLepton*   genLeptonFromH_WW_qqlnu = nullptr;
    const GenLepton*   genLepton1FromH_WW_lnulnu = nullptr;
    const GenLepton*   genLepton2FromH_WW_lnulnu = nullptr;
    //const GenParticle* genNu1FromH_WW_lnulnu = nullptr;
    //const GenParticle* genNu2FromH_WW_lnulnu = nullptr;        
    //size_t idxGenW1lnu_H_WW_lnulnu = 999; // idx of WBoson in genWBosons
    //size_t idxGenW2lnu_H_WW_lnulnu = 999;
    //size_t idxGenWlnu_H_WW_qqlnu   = 999;
    //size_t idxGenWqq_H_WW_qqlnu    = 999;    
    size_t H_WW_DecayIdx[2][2]; // [i][j]: i: H indix, j: 0,1 1st and 2nd W of ith H
    int nWLeptonic = 0, nWHadronic = 0, nWFoundBothLepHadronic = 0;
    for (int i=0; i<2; i++) {
      for (int j=0; j<2; j++) {
	H_WW_DecayIdx[i][j] = 999;
	//std::cout<<"i: "<<i<<", j: "<<j<<", H_WW_DecayIdx[i][j]: "<<H_WW_DecayIdx[i][j]<<std::endl;
      }
    }
    std::pair<const GenLepton*, const GenParticle*> *genLepton_and_NeutrinoFromWBosons;
    genLepton_and_NeutrinoFromWBosons = new std::pair<const GenLepton*, const GenParticle*>[genWBosons.size()];
    std::pair<const GenParticle*, const GenParticle*> *genJetPairFromWBosons;
    genJetPairFromWBosons = new std::pair<const GenParticle*, const GenParticle*>[genWBosons.size()];

	


    if ( isMC && (int)genHiggses.size()>=2 && (int)genWBosons.size()>=4)  {
      for (size_t igenHiggs = 0; igenHiggs < genHiggses.size(); ++igenHiggs) {
	Particle::LorentzVector HP4 = genHiggses[igenHiggs].p4();
	double minDeltaMass = 1.e+3;
	double minDeltaR    = 1.e+4;
	for (size_t iWBoson1 = 0; iWBoson1 < genWBosons.size(); ++iWBoson1) {
	  for (size_t iWBoson2 = 0; iWBoson2 < genWBosons.size(); ++iWBoson2) {
	    if (iWBoson1 == iWBoson2) continue;
	    Particle::LorentzVector WWP4 = genWBosons[iWBoson1].p4() + genWBosons[iWBoson2].p4();
	    double deltaMass = TMath::Abs(HP4.mass() - WWP4.mass());
	    double dR = deltaR(WWP4, HP4);
	    if ( deltaMass < minDeltaMass && deltaMass < 5. && 
		 dR < minDeltaR           && dR < 0.8) {
	      minDeltaMass = deltaMass;
	      minDeltaR    = dR;
	      H_WW_DecayIdx[igenHiggs][0] = iWBoson1;
	      H_WW_DecayIdx[igenHiggs][1] = iWBoson2;
	    }
	  }
	}
      }
      if ( isDEBUG ) {
	printf("\tH0: W1: %i dR(H,W): %f, W2: %i dR(H,W): %f,  mWW: %f,   dR(H, WW): %f,   dR(H, W'W'): %f\n",
	       (int)H_WW_DecayIdx[0][0],
	       deltaR(genHiggses[0].p4(), genWBosons[H_WW_DecayIdx[0][0]].p4()),
	       (int)H_WW_DecayIdx[0][1],
	       deltaR(genHiggses[0].p4(), genWBosons[H_WW_DecayIdx[0][1]].p4()),
	       (genWBosons[H_WW_DecayIdx[0][0]].p4() + genWBosons[H_WW_DecayIdx[0][1]].p4()).mass(),
	       deltaR(genHiggses[0].p4(), genWBosons[H_WW_DecayIdx[0][0]].p4() + genWBosons[H_WW_DecayIdx[0][1]].p4()),
	       deltaR(genHiggses[0].p4(), genWBosons[H_WW_DecayIdx[1][0]].p4() + genWBosons[H_WW_DecayIdx[1][1]].p4()) );
	printf("\tH1: W1: %i dR(H,W): %f, W2: %i dR(H,W): %f,  mWW: %f,   dR(H, WW): %f,   dR(H, W'W'): %f\n",
	       (int)H_WW_DecayIdx[1][0],
	       deltaR(genHiggses[1].p4(), genWBosons[H_WW_DecayIdx[1][0]].p4()),
	       (int)H_WW_DecayIdx[1][1],
	       deltaR(genHiggses[1].p4(), genWBosons[H_WW_DecayIdx[1][1]].p4()),
	       (genWBosons[H_WW_DecayIdx[1][0]].p4() + genWBosons[H_WW_DecayIdx[1][1]].p4()).mass(),
	       deltaR(genHiggses[1].p4(), genWBosons[H_WW_DecayIdx[1][0]].p4() + genWBosons[H_WW_DecayIdx[1][1]].p4()),
	       deltaR(genHiggses[1].p4(), genWBosons[H_WW_DecayIdx[0][0]].p4() + genWBosons[H_WW_DecayIdx[0][1]].p4()) );
      }
      
      
      for (size_t idxWBoson = 0; idxWBoson<genWBosons.size(); ++idxWBoson) {
	//genLepton_and_NeutrinoFromWBosons[idxWBoson] = findGenLepton_and_NeutrinoFromWBoson(&(genWBosons[idxWBoson]), genLeptons, genNeutrinos);
	genLepton_and_NeutrinoFromWBosons[idxWBoson] = findGenLepton_and_NeutrinoFromWBoson_1(&(genWBosons[idxWBoson]), genLeptons, genNeutrinos);	  
	
	Particle::LorentzVector genWBosonP4 = genWBosons[idxWBoson].p4();
	const GenParticle* genJet1FromWBoson = nullptr;
	const GenParticle* genJet2FromWBoson = nullptr;
	double minDeltaMass = 1.e+3;
	for ( std::vector<GenParticle>::const_iterator genWJet1 = genWJets.begin();
	      genWJet1 != genWJets.end(); ++genWJet1 ) {
	  for ( std::vector<GenParticle>::const_iterator genWJet2 = genWJet1 + 1;
		genWJet2 != genWJets.end(); ++genWJet2 ) {
	    double deltaMass = TMath::Abs((genWJet1->p4() + genWJet2->p4()).mass() - genWBosonP4.mass());
	    double dR = deltaR(genWJet1->p4() + genWJet2->p4(), genWBosonP4);
	    //if ( deltaR(genWJet1->p4() + genWJet2->p4(), genWBosonP4) < 1.e-1 &&
	    //   std::fabs((genWJet1->p4() + genWJet2->p4()).mass() - genWBosonP4.mass()) < 5. ) {
	    //if ( deltaMass  < 5  &&  deltaMass < minDeltaMass  &&  dR < 1) {
	    if ( deltaMass  < 1.5  &&  deltaMass < minDeltaMass  &&  dR < 0.01) {	
	      genJet1FromWBoson = &(*genWJet1);
	      genJet2FromWBoson = &(*genWJet2);
	      minDeltaMass = deltaMass;
	    }
	  }	  
	}
	genJetPairFromWBosons[idxWBoson] = std::pair<const GenParticle*, const GenParticle*>(genJet1FromWBoson, genJet2FromWBoson);
	if (genJet1FromWBoson && genJet2FromWBoson && isDEBUG)
	  std::cout<<"idxW: "<<idxWBoson<<", W->qq matching: m(W):"<<genWBosons[idxWBoson].mass()<<", m(qq): "<<(genJet1FromWBoson->p4()+genJet2FromWBoson->p4()).mass()<<", dR(W, qq): "<<deltaR((genJet1FromWBoson->p4()+genJet2FromWBoson->p4()), genWBosons[idxWBoson].p4())<<std::endl;
	if (genLepton_and_NeutrinoFromWBosons[idxWBoson].first &&
	    genLepton_and_NeutrinoFromWBosons[idxWBoson].second &&
	    isDEBUG )
	  std::cout<<"idxW: "<<idxWBoson<<", W->l nu matching: m(W):"<<genWBosons[idxWBoson].mass()<<", m(l nu): "<<((genLepton_and_NeutrinoFromWBosons[idxWBoson].first)->p4() + (genLepton_and_NeutrinoFromWBosons[idxWBoson].second)->p4()).mass()<<", dR(W, l nu): "<<deltaR(((genLepton_and_NeutrinoFromWBosons[idxWBoson].first)->p4() + (genLepton_and_NeutrinoFromWBosons[idxWBoson].second)->p4()), genWBosons[idxWBoson].p4())<<std::endl;
	
      }
      
      
      
      for (size_t igenHiggs=0; igenHiggs<2; ++igenHiggs) {
	for (size_t igenWBoson=0; igenWBoson<2; ++igenWBoson) {
	  size_t idxWBoson =  H_WW_DecayIdx[igenHiggs][igenWBoson];
	  std::pair<const GenLepton*, const GenParticle*> genLepton_and_NeutrinoFromWBoson = genLepton_and_NeutrinoFromWBosons[idxWBoson];
	  std::pair<const GenParticle*, const GenParticle*> genJetPairFromWBoson = genJetPairFromWBosons[idxWBoson];
	  const GenLepton* genLepton = genLepton_and_NeutrinoFromWBoson.first;
	  const GenParticle* genNeutrino = genLepton_and_NeutrinoFromWBoson.second;
	  const GenParticle* genJet1 = genJetPairFromWBoson.first;
	  const GenParticle* genJet2 = genJetPairFromWBoson.second;
	  /*std::cout<<"igenHiggs: "<<igenHiggs<<", igenWBoson: "<<igenWBoson
	    <<", genLepton: "<<genLepton<<", genNeutrino: "<<genNeutrino
	    <<", genJet1: "<<genJet1<<", genJet2: "<<genJet2
	    <<std::endl;*/
	  if (genLepton && genNeutrino) nWLeptonic++;
	  if (genJet1 &&genJet2 )nWHadronic++; 
	  if ((genLepton && genNeutrino) && (genJet1 &&genJet2 )) nWFoundBothLepHadronic++;
	  
	}
      }
      if ( isDEBUG ) std::cout<<"nWLeptonic: "<<nWLeptonic<<", nWHadronic: "<<nWHadronic <<",  nWFoundBothLepHadronic: "<<nWFoundBothLepHadronic<<std::endl;
      if (nWFoundBothLepHadronic > 0) cutFlowTable.update(Form("genCollection: WBoson matched with both l+nu and jj"), 1);
      /*cutFlowTable.update(Form("genCollection: H: %i, W: %i, WJets: %i, leptons: %i, neutrinos: %i,  nWLeptonic: %i, nWHadronic: %i ",
	(int)genHiggses.size(),(int)genWBosons.size(),
	(int)genWJets.size(),(int)genLeptons.size(),(int)genNeutrinos.size(),
	nWLeptonic,nWHadronic), 1); */
      
      size_t igenHiggs_H_WW_lnulnu = 9999;
      for (size_t igenHiggs=0; igenHiggs<2; ++igenHiggs) {
	for (size_t igenWBoson=0; igenWBoson<2; ++igenWBoson) {
	  size_t idxWBoson =  H_WW_DecayIdx[igenHiggs][igenWBoson];
	  std::pair<const GenLepton*, const GenParticle*> genLepton_and_NeutrinoFromWBoson = genLepton_and_NeutrinoFromWBosons[idxWBoson];
	  std::pair<const GenParticle*, const GenParticle*> genJetPairFromWBoson = genJetPairFromWBosons[idxWBoson];
	  const GenLepton* genLepton = genLepton_and_NeutrinoFromWBoson.first;
	  const GenParticle* genNeutrino = genLepton_and_NeutrinoFromWBoson.second;
	  const GenParticle* genJet1 = genJetPairFromWBoson.first;
	  const GenParticle* genJet2 = genJetPairFromWBoson.second;
	  
	  if (genJet1 && genJet2) {
	    // set H->WW->qqlnu gen-pointer
	    genWHadronicFromH_WW_qqlnu = &(genWBosons[idxWBoson]);
	    genJet1FromH_WW_qqlnu = genJet1;
	    genJet2FromH_WW_qqlnu = genJet2;
	    //idxGenWqq_H_WW_qqlnu = igenWBoson; // index in genWBoson collection
	    
	    size_t igenOtherWBosonFromH = 0; // can be 0, 1 as H->WW
	    if (idxWBoson == 0) igenOtherWBosonFromH++;
	    size_t idxOtherWBosonFromH =  H_WW_DecayIdx[igenHiggs][igenOtherWBosonFromH];
	    std::pair<const GenLepton*, const GenParticle*> genLepton_and_NeutrinoFromOtherWBosonFromH = genLepton_and_NeutrinoFromWBosons[idxOtherWBosonFromH];
	    //std::pair<const GenParticle*, const GenParticle*> genJetPairFromOtherWBosonFromH = genJetPairFromWBosons[idxWBoson];
	    genLeptonFromH_WW_qqlnu = genLepton_and_NeutrinoFromOtherWBosonFromH.first;
	    //idxGenWlnu_H_WW_qqlnu = idxOtherWBosonFromH; // index in genWBoson collection

	    // set H->WW->lnulnu gen-index
	    igenHiggs_H_WW_lnulnu = 0;
	    if (igenHiggs == 0) igenHiggs_H_WW_lnulnu++;
	  }	  
	}
      }
      if (igenHiggs_H_WW_lnulnu < 2) { // igenHiggs_H_WW_lnulnu < 2: to check igenHiggs_H_WW_lnulnu is been set
	//idxGenW1lnu_H_WW_lnulnu   = H_WW_DecayIdx[igenHiggs_H_WW_lnulnu][0]; // index in genWBoson collection
	//idxGenW2lnu_H_WW_lnulnu   = H_WW_DecayIdx[igenHiggs_H_WW_lnulnu][1]; // index in genWBoson collection
	/*genLepton1FromH_WW_lnulnu = (genLepton_and_NeutrinoFromWBosons[idxGenW1lnu_H_WW_lnulnu]).first;
	genLepton2FromH_WW_lnulnu = (genLepton_and_NeutrinoFromWBosons[idxGenW2lnu_H_WW_lnulnu]).first;
	genNu1FromH_WW_lnulnu     = (genLepton_and_NeutrinoFromWBosons[idxGenW1lnu_H_WW_lnulnu]).second;
	genNu2FromH_WW_lnulnu     = (genLepton_and_NeutrinoFromWBosons[idxGenW2lnu_H_WW_lnulnu]).second;*/
	genLepton1FromH_WW_lnulnu = (genLepton_and_NeutrinoFromWBosons[H_WW_DecayIdx[igenHiggs_H_WW_lnulnu][0]]).first;
	genLepton2FromH_WW_lnulnu = (genLepton_and_NeutrinoFromWBosons[H_WW_DecayIdx[igenHiggs_H_WW_lnulnu][1]]).first;
	//genNu1FromH_WW_lnulnu     = (genLepton_and_NeutrinoFromWBosons[H_WW_DecayIdx[igenHiggs_H_WW_lnulnu][0]]).second;
	//genNu2FromH_WW_lnulnu     = (genLepton_and_NeutrinoFromWBosons[H_WW_DecayIdx[igenHiggs_H_WW_lnulnu][1]]).second;
      }
      
      if ( isDEBUG ) {
	printf("===>>> Printing HH->WWWW->qq3l3nu decay chains::\n");
	for (size_t igenHiggs=0; igenHiggs<2; ++igenHiggs) {
	  //Particle::LorentzVector HFromDecayP4
	  printf("\tH%i: W0: %i,  W1: %i,   mWW: %f,   dR(H, WW): %f \n\t",
		 (int)igenHiggs, (int)H_WW_DecayIdx[igenHiggs][0], (int)H_WW_DecayIdx[igenHiggs][1],
		 (genWBosons[H_WW_DecayIdx[igenHiggs][0]].p4() + genWBosons[H_WW_DecayIdx[igenHiggs][1]].p4()).mass(),
		 deltaR(genHiggses[igenHiggs].p4(), genWBosons[H_WW_DecayIdx[igenHiggs][0]].p4() + genWBosons[H_WW_DecayIdx[igenHiggs][1]].p4()) );

	  Particle::LorentzVector HFromDecayProdP4[2];
	  Particle::LorentzVector WP4, WFromDecayProdP4;
	  std::string sWDecayType;
	  for (size_t igenWBoson=0; igenWBoson<2; ++igenWBoson) {
	    size_t idxWBoson =  H_WW_DecayIdx[igenHiggs][igenWBoson];	    	    
	    WP4 = genWBosons[idxWBoson].p4();
	    if ((genJetPairFromWBosons[idxWBoson]).first && (genJetPairFromWBosons[idxWBoson]).second) {
	      WFromDecayProdP4 = ((genJetPairFromWBosons[idxWBoson]).first)->p4() + ((genJetPairFromWBosons[idxWBoson]).second)->p4();
	      sWDecayType = "WHadronicDecay";
	    } else {
	      if ((genLepton_and_NeutrinoFromWBosons[idxWBoson]).first && (genLepton_and_NeutrinoFromWBosons[idxWBoson]).second) {
		WFromDecayProdP4 = ((genLepton_and_NeutrinoFromWBosons[idxWBoson]).first)->p4() + ((genLepton_and_NeutrinoFromWBosons[idxWBoson]).second)->p4();
		sWDecayType = "WLeptonicDecay";
	      }
	    }
	    HFromDecayProdP4[igenWBoson] = WFromDecayProdP4;
	    printf("\tW%i: m: %f,  mWdecay: %f,  dR(W, Wdecay): %f, %s, ",
		   (int)igenWBoson, WP4.mass(), WFromDecayProdP4.mass(), deltaR(WP4, WFromDecayProdP4),
		   sWDecayType.c_str());
	  }
	  printf("\t mHdecay: %f\n",(HFromDecayProdP4[0] + HFromDecayProdP4[1]).mass());
	}

	std::cout<<"genJet1FromH_WW_qqlnu: "<<genJet1FromH_WW_qqlnu<<", genJet2FromH_WW_qqlnu: "<<genJet2FromH_WW_qqlnu
		 <<", genLeptonFromH_WW_qqlnu: "<<genLeptonFromH_WW_qqlnu
		 <<", genLepton1FromH_WW_lnulnu: "<<genLepton1FromH_WW_lnulnu
		 <<", genLepton2FromH_WW_lnulnu: "<<genLepton2FromH_WW_lnulnu
		 <<std::endl;
      }      
      
    }

    

    if ( !(genLepton1FromH_WW_lnulnu && genLepton2FromH_WW_lnulnu &&
	   genJet1FromH_WW_qqlnu && genJet2FromH_WW_qqlnu && genLeptonFromH_WW_qqlnu)) {
      if ( isDEBUG ) {
	printf("Not HH->4W->3l 3nu 2j event \n");
      }
      continue;
    }
    cutFlowTable.update("gen HH->4W->3l 3nu 2j event");


    double drl3Wjj_gen = deltaR(genWHadronicFromH_WW_qqlnu->p4(), genLeptonFromH_WW_qqlnu->p4());
    double drl3j1_gen  = deltaR(genJet1FromH_WW_qqlnu->p4(), genLeptonFromH_WW_qqlnu->p4());
    double drl3j2_gen  = deltaR(genJet2FromH_WW_qqlnu->p4(), genLeptonFromH_WW_qqlnu->p4());
    double drl3j_gen   = (drl3j1_gen < drl3j2_gen) ? drl3j1_gen : drl3j2_gen;
    hdRl3WHadronic_gen_all->Fill(drl3Wjj_gen);
    hdRl3jFromWjj_gen_all->Fill(drl3j_gen);
    if (genWHadronicFromH_WW_qqlnu->pt() > 100 &&
	deltaR(genJet1FromH_WW_qqlnu->p4(), genJet2FromH_WW_qqlnu->p4()) < 1.2) {
      hdRl3WHadronic_gen_BoostedWjj_all->Fill(drl3Wjj_gen);
      hdRl3jFromWjj_gen_BoostedWjj_all->Fill(drl3j_gen);
    }


//--- build collections of electrons, muons and hadronic taus;
//    resolve overlaps in order of priority: muon, electron,
    std::vector<RecoMuon> muons = muonReader->read();
    std::vector<const RecoMuon*> muon_ptrs = convert_to_ptrs(muons);
    std::vector<const RecoMuon*> cleanedMuons = muon_ptrs; // CV: no cleaning needed for muons, as they have the highest priority in the overlap removal
    std::vector<const RecoMuon*> preselMuons = preselMuonSelector(cleanedMuons, isHigherConePt);
    std::vector<const RecoMuon*> fakeableMuons = fakeableMuonSelector(preselMuons, isHigherConePt);
    std::vector<const RecoMuon*> tightMuons = tightMuonSelector(fakeableMuons, isHigherConePt);
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("preselMuons",   preselMuons);
      printCollection("fakeableMuons", fakeableMuons);
      printCollection("tightMuons",    tightMuons);
    }

    std::vector<RecoElectron> electrons = electronReader->read();
    std::vector<const RecoElectron*> electron_ptrs = convert_to_ptrs(electrons);
    std::vector<const RecoElectron*> cleanedElectrons = electronCleaner(electron_ptrs, preselMuons);
    std::vector<const RecoElectron*> preselElectrons = preselElectronSelector(cleanedElectrons, isHigherConePt);
    std::vector<const RecoElectron*> fakeableElectrons = fakeableElectronSelector(preselElectrons, isHigherConePt);
    std::vector<const RecoElectron*> tightElectrons = tightElectronSelector(fakeableElectrons, isHigherConePt);
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("preselElectrons",   preselElectrons);
      printCollection("fakeableElectrons", fakeableElectrons);
      printCollection("tightElectrons",    tightElectrons);
    }

    std::vector<const RecoLepton*> preselLeptonsFull = mergeLeptonCollections(preselElectrons, preselMuons, isHigherConePt);
    std::vector<const RecoLepton*> fakeableLeptonsFull = mergeLeptonCollections(fakeableElectrons, fakeableMuons, isHigherConePt);
    std::vector<const RecoLepton*> tightLeptonsFull = mergeLeptonCollections(tightElectrons, tightMuons, isHigherConePt);

    std::vector<const RecoLepton*> preselLeptons = pickFirstNobjects(preselLeptonsFull, 3);
    std::vector<const RecoLepton*> fakeableLeptons = pickFirstNobjects(fakeableLeptonsFull, 3);
    std::vector<const RecoLepton*> tightLeptons = getIntersection(fakeableLeptons, tightLeptonsFull, isHigherConePt);

    std::vector<const RecoLepton*> selLeptons;
    std::vector<const RecoMuon*> selMuons;
    std::vector<const RecoElectron*> selElectrons;
    if(electronSelection == muonSelection)
    {
      // for SR, flip region and fake CR
      // doesn't matter if we supply electronSelection or muonSelection here
      selLeptons = selectObjects(muonSelection, preselLeptons, fakeableLeptons, tightLeptons);
      selMuons = getIntersection(preselMuons, selLeptons, isHigherConePt);
      selElectrons = getIntersection(preselElectrons, selLeptons, isHigherConePt);
    }
    else
    {
      // for MC closure
      // make sure that neither electron nor muon selections are loose
      assert(electronSelection != kLoose && muonSelection != kLoose);
      selMuons = selectObjects(muonSelection, preselMuons, fakeableMuons, tightMuons);
      selElectrons = selectObjects(electronSelection, preselElectrons, fakeableElectrons, tightElectrons);
      std::vector<const RecoLepton*> selLeptons_full = mergeLeptonCollections(selElectrons, selMuons, isHigherConePt);
      selLeptons = getIntersection(fakeableLeptons, selLeptons_full, isHigherConePt);
    }

    std::vector<RecoHadTau> hadTaus = hadTauReader->read();
    std::vector<const RecoHadTau*> hadTau_ptrs = convert_to_ptrs(hadTaus);
    std::vector<const RecoHadTau*> cleanedHadTaus = hadTauCleaner(hadTau_ptrs, preselMuons, preselElectrons);
    std::vector<const RecoHadTau*> selHadTaus = tightHadTauSelector(cleanedHadTaus, isHigherPt);

    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("selMuons", selMuons);
      printCollection("selElectrons", selElectrons);
      printCollection("selLeptons", selLeptons);
      printCollection("selHadTaus", selHadTaus);
    }    

    
//--- build collections of jets and select subset of jets passing b-tagging criteria
    std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleanerAK4_dR04(jet_ptrs_ak4, fakeableLeptons);
    std::vector<const RecoJet*> selJetsAK4 = jetSelectorAK4(cleanedJetsAK4_wrtLeptons, isHigherPt);
    std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4_wrtLeptons, isHigherPt);
    std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);
    int numSelJetsPtGt40 = countHighPtObjects(selJetsAK4, 40.);
    
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("uncleanedJetsAK4", jet_ptrs_ak4);
      printCollection("selJetsAK4",       selJetsAK4);
    }
    


    std::vector<RecoJetAK8> jets_ak8_Wjj = jetReaderAK8_Wjj->read();
    std::vector<const RecoJetAK8*> jet_ptrs_ak8_Wjj = convert_to_ptrs(jets_ak8_Wjj);    
    
    
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("uncleaned AK8 jets (Wjj)", jet_ptrs_ak8_Wjj);        
    }


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
      if ( genPhotonReader ) {
        genPhotons = genPhotonReader->read();
      }
      if ( genJetReader ) {
        genJets = genJetReader->read();
      }
    }

//--- match reconstructed to generator level particles
    if ( isMC && redoGenMatching ) {
      muonGenMatcher.addGenLeptonMatch(preselMuons, genLeptons, 0.2);
      muonGenMatcher.addGenHadTauMatch(preselMuons, genHadTaus, 0.2);
      muonGenMatcher.addGenJetMatch(preselMuons, genJets, 0.2);

      electronGenMatcher.addGenLeptonMatch(preselElectrons, genLeptons, 0.2);
      electronGenMatcher.addGenHadTauMatch(preselElectrons, genHadTaus, 0.2);
      electronGenMatcher.addGenPhotonMatch(preselElectrons, genPhotons, 0.2);
      electronGenMatcher.addGenJetMatch(preselElectrons, genJets, 0.2);

      hadTauGenMatcher.addGenLeptonMatch(selHadTaus, genLeptons, 0.2);
      hadTauGenMatcher.addGenHadTauMatch(selHadTaus, genHadTaus, 0.2);
      hadTauGenMatcher.addGenJetMatch(selHadTaus, genJets, 0.2);

      /*
      jetGenMatcher.addGenLeptonMatch(selJets, genLeptons, 0.2);
      jetGenMatcher.addGenHadTauMatch(selJets, genHadTaus, 0.2);
      jetGenMatcher.addGenJetMatch(selJets, genJets, 0.2);*/
      jetGenMatcherAK4.addGenLeptonMatch(cleanedJetsAK4_wrtLeptons, genLeptons, 0.2);
      jetGenMatcherAK4.addGenHadTauMatch(cleanedJetsAK4_wrtLeptons, genHadTaus, 0.2);
      jetGenMatcherAK4.addGenJetMatch(cleanedJetsAK4_wrtLeptons, genJets, 0.2);
    }
    
#ifndef DoNotUsehh_3lConditions
#pragma message ("Warning*** DoNotUsehh_3lConditions is not defined")
    
    /*    
    double evtWeight_inclusive = 1.;
    if(isMC)
    {
      if(apply_genWeight)         evtWeight_inclusive *= boost::math::sign(eventInfo.genWeight);
      if(eventWeightManager)      evtWeight_inclusive *= eventWeightManager->getWeight();
      if(l1PreFiringWeightReader) evtWeight_inclusive *= l1PreFiringWeightReader->getWeight();
      lheInfoReader->read();
      evtWeight_inclusive *= lheInfoReader->getWeight_scale(lheScale_option);
      evtWeight_inclusive *= eventInfo.pileupWeight;
      evtWeight_inclusive *= eventInfo.genWeight_tH();
      evtWeight_inclusive *= lumiScale;
      genEvtHistManager_beforeCuts->fillHistograms(genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeight_inclusive);
      if(eventWeightManager)
      {
        genEvtHistManager_beforeCuts->fillHistograms(eventWeightManager, evtWeight_inclusive);
      }
    }

    bool isTriggered_1e = hltPaths_isTriggered(triggers_1e, isDEBUG);
    bool isTriggered_1mu = hltPaths_isTriggered(triggers_1mu, isDEBUG);
    bool isTriggered_2e = hltPaths_isTriggered(triggers_2e, isDEBUG);
    bool isTriggered_1e1mu = hltPaths_isTriggered(triggers_1e1mu, isDEBUG);
    bool isTriggered_2mu = hltPaths_isTriggered(triggers_2mu, isDEBUG);
    bool isTriggered_3e = hltPaths_isTriggered(triggers_3e, isDEBUG);
    bool isTriggered_2e1mu = hltPaths_isTriggered(triggers_2e1mu, isDEBUG);
    bool isTriggered_1e2mu = hltPaths_isTriggered(triggers_1e2mu, isDEBUG);
    bool isTriggered_3mu = hltPaths_isTriggered(triggers_3mu, isDEBUG);
    if ( isDEBUG ) {
      std::cout << "isTriggered:"
		<< " 1e = " << isTriggered_1e << ","
		<< " 1mu = " << isTriggered_1mu << ","
		<< " 2e = " << isTriggered_2e << ","
		<< " 1e1mu = " << isTriggered_1e1mu << ","
		<< " 2mu = " << isTriggered_2mu << ","
		<< " 3e = " << isTriggered_3e << ","
		<< " 2e1mu = " << isTriggered_2e1mu << ","
		<< " 1e2mu = " << isTriggered_1e2mu << ","
		<< " 3mu = " << isTriggered_3mu << std::endl;
    }

    bool selTrigger_1e = use_triggers_1e && isTriggered_1e;
    bool selTrigger_1mu = use_triggers_1mu && isTriggered_1mu;
    bool selTrigger_2e = use_triggers_2e && isTriggered_2e;
    bool selTrigger_1e1mu = use_triggers_1e1mu && isTriggered_1e1mu;
    bool selTrigger_2mu = use_triggers_2mu && isTriggered_2mu;
    bool selTrigger_3e = use_triggers_3e && isTriggered_3e;
    bool selTrigger_2e1mu = use_triggers_2e1mu && isTriggered_2e1mu;
    bool selTrigger_1e2mu = use_triggers_1e2mu && isTriggered_1e2mu;
    bool selTrigger_3mu = use_triggers_3mu && isTriggered_3mu;
    if ( !(selTrigger_1e || selTrigger_1mu   ||
	   selTrigger_2e || selTrigger_1e1mu || selTrigger_2mu   ||
	   selTrigger_3e || selTrigger_2e1mu || selTrigger_1e2mu || selTrigger_3mu) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
	std::cout << " (selTrigger_3mu = " << selTrigger_3mu
		  << ", selTrigger_1e2mu = " << selTrigger_1e2mu
		  << ", selTrigger_2e1mu = " << selTrigger_2e1mu
		  << ", selTrigger_3e = " << selTrigger_3e
		  << ", selTrigger_2mu = " << selTrigger_2mu
		  << ", selTrigger_1e1mu = " << selTrigger_1e1mu
		  << ", selTrigger_2e = " << selTrigger_2e
		  << ", selTrigger_1mu = " << selTrigger_1mu
		  << ", selTrigger_1e = " << selTrigger_1e << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("trigger0 ");
    
//--- rank triggers by priority and ignore triggers of lower priority if a trigger of higher priority has fired for given event;
//    the triggers are ranked by primary dataset (PD).
//    The ranking of the PDs is as follows: DoubleMuon, MuonEG, DoubleEG, SingleMuon, SingleElectron
// CV: see https://cmssdt.cern.ch/lxr/source/HLTrigger/Configuration/python/HLT_GRun_cff.py?v=CMSSW_8_0_24 for association of triggers paths to PD
//     this logic is necessary to avoid that the same event is selected multiple times when processing different primary datasets
    if ( !isMC && !isDEBUG ) {

      //bool isTriggered_SingleElectron = isTriggered_1e;
      bool isTriggered_SingleMuon = isTriggered_1mu;
      bool isTriggered_DoubleEG = isTriggered_2e || isTriggered_3e;
      bool isTriggered_DoubleMuon = isTriggered_2mu || isTriggered_3mu;
      bool isTriggered_MuonEG = isTriggered_1e1mu || isTriggered_2e1mu || isTriggered_1e2mu;

      bool selTrigger_SingleElectron = selTrigger_1e;
      bool selTrigger_SingleMuon = selTrigger_1mu;
      bool selTrigger_DoubleEG = selTrigger_2e || selTrigger_3e;
      //bool selTrigger_DoubleMuon = selTrigger_2mu || selTrigger_3mu;
      bool selTrigger_MuonEG = selTrigger_1e1mu || selTrigger_2e1mu || selTrigger_1e2mu;
      if ( selTrigger_SingleElectron && (isTriggered_DoubleEG || isTriggered_SingleMuon || isTriggered_DoubleMuon || isTriggered_MuonEG) ) {
	if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
	  std::cout << " (selTrigger_SingleElectron = " << selTrigger_SingleElectron
		    << ", isTriggered_DoubleEG = " << isTriggered_DoubleEG
		    << ", isTriggered_SingleMuon = " << isTriggered_SingleMuon
		    << ", isTriggered_DoubleMuon = " << isTriggered_DoubleMuon
		    << ", isTriggered_MuonEG = " << isTriggered_MuonEG << ")" << std::endl;
	}
	continue;
      }
      if ( selTrigger_DoubleEG && (isTriggered_DoubleMuon || isTriggered_MuonEG) ) {
	if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
	  std::cout << " (selTrigger_DoubleEG = " << selTrigger_DoubleEG
		    << ", isTriggered_DoubleMuon = " << isTriggered_DoubleMuon
		    << ", isTriggered_MuonEG = " << isTriggered_MuonEG << ")" << std::endl;
	}
	continue;
      }
      if ( selTrigger_SingleMuon && (isTriggered_DoubleEG || isTriggered_DoubleMuon || isTriggered_MuonEG) ) {
	if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
	  std::cout << " (selTrigger_SingleMuon = " << selTrigger_SingleMuon
		    << ", isTriggered_DoubleEG = " << isTriggered_DoubleEG
		    << ", isTriggered_DoubleMuon = " << isTriggered_DoubleMuon
		    << ", isTriggered_MuonEG = " << isTriggered_MuonEG << ")" << std::endl;
	}
	continue;
      }
      if ( selTrigger_MuonEG && isTriggered_DoubleMuon ) {
	if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
	  std::cout << " (selTrigger_MuonEG = " << selTrigger_MuonEG
		    << ", isTriggered_DoubleMuon = " << isTriggered_DoubleMuon << ")" << std::endl;
	}
	continue;
      }
    }
    cutFlowTable.update("trigger");
    cutFlowHistManager->fillHistograms("trigger", lumiScale);

    if ( (selTrigger_3mu   && !apply_offline_e_trigger_cuts_3mu)   ||
	 (selTrigger_2e1mu && !apply_offline_e_trigger_cuts_2e1mu) ||
	 (selTrigger_1e2mu && !apply_offline_e_trigger_cuts_1e2mu) ||
	 (selTrigger_3e    && !apply_offline_e_trigger_cuts_3e)    ||
	 (selTrigger_2mu   && !apply_offline_e_trigger_cuts_2mu)   ||
	 (selTrigger_1e1mu && !apply_offline_e_trigger_cuts_1e1mu) ||
	 (selTrigger_2e    && !apply_offline_e_trigger_cuts_2e)    ||
	 (selTrigger_1mu   && !apply_offline_e_trigger_cuts_1mu)   ||
	 (selTrigger_1e    && !apply_offline_e_trigger_cuts_1e)    ) {
      fakeableElectronSelector.disable_offline_e_trigger_cuts();
      tightElectronSelector.disable_offline_e_trigger_cuts();
    } else {
      fakeableElectronSelector.enable_offline_e_trigger_cuts();
      tightElectronSelector.enable_offline_e_trigger_cuts();
    }




//--- apply preselection
    // require exactly three leptons passing loose preselection criteria to avoid overlap with 4l category
    if ( !(preselLeptonsFull.size() >= 3) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS preselLeptons selection." << std::endl;
  printCollection("preselLeptons", preselLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update(">= 3 presel leptons");
    cutFlowHistManager->fillHistograms(">= 3 presel leptons", lumiScale);
    const RecoLepton* preselLepton_lead = preselLeptonsFull[0];
    const RecoLepton* preselLepton_sublead = preselLeptonsFull[1];
    const RecoLepton* preselLepton_third = preselLeptonsFull[2];
    const leptonGenMatchEntry& preselLepton_genMatch = getLeptonGenMatch(leptonGenMatch_definitions, preselLepton_lead, preselLepton_sublead, preselLepton_third);
    int idxPreselLepton_genMatch = preselLepton_genMatch.idx_;
    assert(idxPreselLepton_genMatch != kGen_LeptonUndefined3);

    // require that trigger paths match event category (with event category based on preselLeptons)
    if ( !((preselElectrons.size() >= 3 &&                            (selTrigger_3e    || selTrigger_2e  || selTrigger_1e                                      )) ||
	   (preselElectrons.size() >= 2 && preselMuons.size() >= 1 && (selTrigger_2e1mu || selTrigger_2e  || selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
	   (preselElectrons.size() >= 1 && preselMuons.size() >= 2 && (selTrigger_1e2mu || selTrigger_2mu || selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
	   (                               preselMuons.size() >= 3 && (selTrigger_3mu   || selTrigger_2mu || selTrigger_1mu                                     ))) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given preselLepton multiplicity." << std::endl;
	std::cout << " (#preselElectrons = " << preselElectrons.size()
		  << ", #preselMuons = " << preselMuons.size()
		  << ", selTrigger_3mu = " << selTrigger_3mu
		  << ", selTrigger_1e2mu = " << selTrigger_1e2mu
		  << ", selTrigger_2e1mu = " << selTrigger_2e1mu
		  << ", selTrigger_3e = " << selTrigger_3e
		  << ", selTrigger_2mu = " << selTrigger_2mu
		  << ", selTrigger_1e1mu = " << selTrigger_1e1mu
		  << ", selTrigger_2e = " << selTrigger_2e
		  << ", selTrigger_1mu = " << selTrigger_1mu
		  << ", selTrigger_1e = " << selTrigger_1e << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("presel lepton trigger match");
    cutFlowHistManager->fillHistograms("presel lepton trigger match", lumiScale);

    // apply requirement on jets (incl. b-tagged jets) and hadronic taus on preselection level
    if ( !((int)selJetsAK4.size() >= minNumJets) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS selJets selection." << std::endl;
    printCollection("selJets", selJetsAK4);
      }
      //continue;
    }
    cutFlowTable.update(Form(">= %i jets (1)", minNumJets));
    cutFlowHistManager->fillHistograms(">= N jets (1)", lumiScale);



     if ( (selBJetsAK4_loose.size() >= 2 || selBJetsAK4_medium.size() >= 1) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS selBJets selection." << std::endl;
	printCollection("selJetsAK4", selJetsAK4);
	printCollection("selBJetsAK4_loose", selBJetsAK4_loose);
	printCollection("selBJetsAK4_medium", selBJetsAK4_medium);
      }
      //continue;
    }
    cutFlowTable.update("b-jet veto (1)");
    cutFlowHistManager->fillHistograms("b-jet veto (1)", lumiScale);

//--- compute MHT and linear MET discriminant (met_LD)
    RecoMEt met = metReader->read();
    Particle::LorentzVector mht_p4 = compMHT(fakeableLeptons, {}, selJetsAK4);
    double met_LD = compMEt_LD(met.p4(), mht_p4);

    double HT = compHT(fakeableLeptons, {}, selJetsAK4);
    double STMET = compSTMEt(fakeableLeptons, {}, selJetsAK4, met.p4());
		
//--- apply final event selection
    // require exactly three leptons passing tight selection criteria of final event selection
    if ( !(selLeptons.size() >= 3) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS selLeptons selection." << std::endl;
	printCollection("selLeptons", selLeptons);
	//printCollection("preselLeptons", preselLeptons);
      }
      continue;
    }
    cutFlowTable.update(">= 3 sel leptons", 1.);
    cutFlowHistManager->fillHistograms(">= 3 sel leptons", 1.);
    const RecoLepton* selLepton_lead = selLeptons[0];
    int selLepton_lead_type = getLeptonType(selLepton_lead->pdgId());
    const RecoLepton* selLepton_sublead = selLeptons[1];
    int selLepton_sublead_type = getLeptonType(selLepton_sublead->pdgId());
    const RecoLepton* selLepton_third = selLeptons[2];
    int selLepton_third_type = getLeptonType(selLepton_third->pdgId());
    const leptonGenMatchEntry& selLepton_genMatch = getLeptonGenMatch(leptonGenMatch_definitions, selLepton_lead, selLepton_sublead, selLepton_third);
    int idxSelLepton_genMatch = selLepton_genMatch.idx_;
    assert(idxSelLepton_genMatch != kGen_LeptonUndefined3);
    if ( isDEBUG ) {
      std::cout << "selLepton_genMatch = " << getLeptonGenMatch_string(leptonGenMatch_definitions, idxSelLepton_genMatch) << std::endl;
      if ( idxSelLepton_genMatch != kGen_3l0g0j ) {
	std::cout << "--> CHECK!" << std::endl;
	printCollection("selLeptons", selLeptons);
      }
    }


//--- compute event-level weight for data/MC correction of b-tagging efficiency and mistag rate
//   (using the method "Event reweighting using scale factors calculated with a tag and probe method",
//    described on the BTV POG twiki https://twiki.cern.ch/twiki/bin/view/CMS/BTagShapeCalibration )
    double evtWeight = 1.;
    double btagWeight = 1.;
    double triggerWeight = 1.;
    double leptonSF_weight = 1.;
    if ( isMC ) {
      evtWeight *= evtWeight_inclusive;
      //btagWeight = get_BtagWeight(selJets);
      btagWeight = get_BtagWeight(selJetsAK4);
      evtWeight *= btagWeight;
      if ( isDEBUG ) {
	std::cout << "lumiScale = " << lumiScale << std::endl;
	if ( apply_genWeight ) std::cout << "genWeight = " << boost::math::sign(eventInfo.genWeight) << std::endl;
	std::cout << "pileupWeight = " << eventInfo.pileupWeight << std::endl;
	std::cout << "btagWeight = " << btagWeight << std::endl;
      }
    }

    double weight_data_to_MC_correction = 1.;
    if ( isMC ) {
      dataToMCcorrectionInterface->setLeptons(
        selLepton_lead_type, selLepton_lead->pt(), selLepton_lead->eta(),
	selLepton_sublead_type, selLepton_sublead->pt(), selLepton_sublead->eta(),
        selLepton_third_type, selLepton_third->pt(), selLepton_third->eta());

//--- apply data/MC corrections for trigger efficiency
      double sf_triggerEff = dataToMCcorrectionInterface->getSF_leptonTriggerEff();
      if ( isDEBUG ) {
	std::cout << "sf_triggerEff = " << sf_triggerEff << std::endl;
      }
      triggerWeight *= sf_triggerEff;
      weight_data_to_MC_correction *= sf_triggerEff;

//--- apply data/MC corrections for efficiencies for lepton to pass loose identification and isolation criteria
      leptonSF_weight *= dataToMCcorrectionInterface->getSF_leptonID_and_Iso_loose();

//--- apply data/MC corrections for efficiencies of leptons passing the loose identification and isolation criteria
//    to also pass the tight identification and isolation criteria
      if ( electronSelection == kFakeable && muonSelection == kFakeable ) {
        leptonSF_weight *= dataToMCcorrectionInterface->getSF_leptonID_and_Iso_fakeable_to_loose();
      } else if ( electronSelection >= kFakeable && muonSelection >= kFakeable ) {
        // apply loose-to-tight lepton ID SFs if either of the following is true:
        // 1) both electron and muon selections are tight -> corresponds to SR
        // 2) electron selection is relaxed to fakeable and muon selection is kept as tight -> corresponds to MC closure w/ relaxed e selection
        // 3) muon selection is relaxed to fakeable and electron selection is kept as tight -> corresponds to MC closure w/ relaxed mu selection
        // we allow (2) and (3) so that the MC closure regions would more compatible w/ the SR (1) in comparison
        leptonSF_weight *= dataToMCcorrectionInterface->getSF_leptonID_and_Iso_tight_to_loose_woTightCharge();
      }
      weight_data_to_MC_correction *= leptonSF_weight;

      evtWeight *= weight_data_to_MC_correction;
    }

    double weight_fakeRate = 1.;
    //if ( !selectBDT ) {
      if ( applyFakeRateWeights == kFR_3lepton ) {
	double prob_fake_lepton_lead = 1.;
	if      ( std::abs(selLepton_lead->pdgId()) == 11 ) prob_fake_lepton_lead = leptonFakeRateInterface->getWeight_e(selLepton_lead->cone_pt(), selLepton_lead->absEta());
	else if ( std::abs(selLepton_lead->pdgId()) == 13 ) prob_fake_lepton_lead = leptonFakeRateInterface->getWeight_mu(selLepton_lead->cone_pt(), selLepton_lead->absEta());
	else assert(0);
	bool passesTight_lepton_lead = isMatched(*selLepton_lead, tightElectrons) || isMatched(*selLepton_lead, tightMuons);
	double prob_fake_lepton_sublead = 1.;
	if      ( std::abs(selLepton_sublead->pdgId()) == 11 ) prob_fake_lepton_sublead = leptonFakeRateInterface->getWeight_e(selLepton_sublead->cone_pt(), selLepton_sublead->absEta());
	else if ( std::abs(selLepton_sublead->pdgId()) == 13 ) prob_fake_lepton_sublead = leptonFakeRateInterface->getWeight_mu(selLepton_sublead->cone_pt(), selLepton_sublead->absEta());
	else assert(0);
	bool passesTight_lepton_sublead = isMatched(*selLepton_sublead, tightElectrons) || isMatched(*selLepton_sublead, tightMuons);
	double prob_fake_lepton_third = 1.;
	if      ( std::abs(selLepton_third->pdgId()) == 11 ) prob_fake_lepton_third = leptonFakeRateInterface->getWeight_e(selLepton_third->cone_pt(), selLepton_third->absEta());
	else if ( std::abs(selLepton_third->pdgId()) == 13 ) prob_fake_lepton_third = leptonFakeRateInterface->getWeight_mu(selLepton_third->cone_pt(), selLepton_third->absEta());
	else assert(0);
	bool passesTight_lepton_third = isMatched(*selLepton_third, tightElectrons) || isMatched(*selLepton_third, tightMuons);
        weight_fakeRate = getWeight_3L(
          prob_fake_lepton_lead, passesTight_lepton_lead,
	  prob_fake_lepton_sublead, passesTight_lepton_sublead,
	  prob_fake_lepton_third, passesTight_lepton_third);
	if ( isDEBUG ) {
	  std::cout << "weight_fakeRate = " << weight_fakeRate << std::endl;
	}
	evtWeight *= weight_fakeRate;
      }
			//}
    if ( isDEBUG ) {
      std::cout << "evtWeight = " << evtWeight << std::endl;
    }

    // require exactly three leptons passing tight selection criteria, to avoid overlap with 4l channel
    if ( !(tightLeptonsFull.size() <= 3) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS tightLeptons selection.\n";
        printCollection("tightLeptonsFull", tightLeptonsFull);
      }
      continue;
    }

    
    // require that trigger paths match event category (with event category based on fakeableLeptons)
    if ( !((fakeableElectrons.size() >= 3 &&                              (selTrigger_3e    || selTrigger_2e  || selTrigger_1e                                      )) ||
	   (fakeableElectrons.size() >= 2 && fakeableMuons.size() >= 1 && (selTrigger_2e1mu || selTrigger_2e  || selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
	   (fakeableElectrons.size() >= 1 && fakeableMuons.size() >= 2 && (selTrigger_1e2mu || selTrigger_2mu || selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
	   (                                 fakeableMuons.size() >= 3 && (selTrigger_3mu   || selTrigger_2mu || selTrigger_1mu                                     ))) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given fakeableLepton multiplicity." << std::endl;
	std::cout << " (#fakeableElectrons = " << fakeableElectrons.size()
		  << ", #fakeableMuons = " << fakeableMuons.size()
		  << ", selTrigger_3mu = " << selTrigger_3mu
		  << ", selTrigger_1e2mu = " << selTrigger_1e2mu
		  << ", selTrigger_2e1mu = " << selTrigger_2e1mu
		  << ", selTrigger_3e = " << selTrigger_3e
		  << ", selTrigger_2mu = " << selTrigger_2mu
		  << ", selTrigger_1e1mu = " << selTrigger_1e1mu
		  << ", selTrigger_2e = " << selTrigger_2e
		  << ", selTrigger_1mu = " << selTrigger_1mu
		  << ", selTrigger_1e = " << selTrigger_1e << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("fakeable lepton trigger match", evtWeight);
    cutFlowHistManager->fillHistograms("fakeable lepton trigger match", evtWeight);

//--- apply HLT filter
    if(apply_hlt_filter)
    {
      const std::map<hltPathsE, bool> trigger_bits = {
        { hltPathsE::trigger_1e,    selTrigger_1e    },
        { hltPathsE::trigger_1mu,   selTrigger_1mu   },
        { hltPathsE::trigger_2e,    selTrigger_2e    },
        { hltPathsE::trigger_2mu,   selTrigger_2mu   },
        { hltPathsE::trigger_1e1mu, selTrigger_1e1mu },
        { hltPathsE::trigger_1e2mu, selTrigger_1e2mu },
        { hltPathsE::trigger_2e1mu, selTrigger_2e1mu },
        { hltPathsE::trigger_3e,    selTrigger_3e    },
        { hltPathsE::trigger_3mu,   selTrigger_3mu   },
      };
      if(! hltFilter(trigger_bits, fakeableLeptons, {}))
      {
        if(run_lumi_eventSelector || isDEBUG)
        {
          std::cout << "event " << eventInfo.str() << " FAILS HLT filter matching\n";
        }
        continue;
      }
    }
    cutFlowTable.update("HLT filter matching", evtWeight);
    cutFlowHistManager->fillHistograms("HLT filter matching", evtWeight);


    

    if ( selHadTaus.size() > 0 ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS selHadTaus veto." << std::endl;
	printCollection("selHadTaus", selHadTaus);
      }
      continue;
    }
    cutFlowTable.update("sel tau veto");
    cutFlowHistManager->fillHistograms("sel tau veto", lumiScale); 

    const bool failsLowMassVeto = isfailsLowMassVeto(preselLeptonsFull);
    if ( failsLowMassVeto ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS low mass lepton pair veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("m(ll) > 12 GeV", evtWeight);
    cutFlowHistManager->fillHistograms("m(ll) > 12 GeV", evtWeight);


    const double minPt_lead = 25.;
    const double minPt_sublead = 15.;
    const double minPt_third = 10.;
    // CV: according to Giovanni, the pT cuts should be applied on cone_pt
    //    (combined efficiency of single lepton, double lepton, and triple lepton triggers assumed to be high,
    //     even if one or two leptons and fakes and hence cone_pt may be significantly smaller than lepton_pt,
    //     on which pT cuts are applied on trigger level)
    if ( !(selLepton_lead->cone_pt() > minPt_lead && selLepton_sublead->cone_pt() > minPt_sublead && selLepton_third->cone_pt() > minPt_third) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS lepton pT selection." << std::endl;
	std::cout << " (leading selLepton pT = " << selLepton_lead->pt() << ", minPt_lead = " << minPt_lead
		  << ", subleading selLepton pT = " << selLepton_sublead->pt() << ", minPt_sublead = " << minPt_sublead
		  << ", third selLepton pT = " << selLepton_third->pt() << ", minPt_third = " << minPt_third << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV && third lepton pT > 10 GeV", evtWeight);
    cutFlowHistManager->fillHistograms("lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV && third lepton pT > 10 GeV", evtWeight);



    int sumLeptonCharge = selLepton_lead->charge() + selLepton_sublead->charge() + selLepton_third->charge();
    bool isCharge_SS = std::abs(sumLeptonCharge) >  1;
    bool isCharge_OS = std::abs(sumLeptonCharge) <= 1;
    if ( chargeSumSelection == kOS && isCharge_SS ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
	std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
		  << ", subleading selLepton charge = " << selLepton_sublead->charge()
		  << ", third selLepton charge = " << selLepton_third->charge() << ", chargeSumSelection = OS)" << std::endl;
      }
      continue;
    }
    if ( chargeSumSelection == kSS && isCharge_OS ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
	std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
		  << ", subleading selLepton charge = " << selLepton_sublead->charge()
		  << ", third selLepton charge = " << selLepton_third->charge() << ", chargeSumSelection = SS)" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("sel lepton charge", evtWeight);
    cutFlowHistManager->fillHistograms("sel lepton charge", evtWeight);

    const bool failsZbosonMassVeto = isfailsZbosonMassVetoSFOS(preselLeptonsFull);
    if ( failsZbosonMassVeto ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS Z-boson veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("Z-boson mass veto", evtWeight);
    cutFlowHistManager->fillHistograms("Z-boson mass veto", evtWeight);

    const bool failsHtoZZVeto = isfailsHtoZZVeto(preselLeptonsFull);
    if ( failsHtoZZVeto ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS H->ZZ*->4l veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("H->ZZ*->4l veto", evtWeight);
    cutFlowHistManager->fillHistograms("H->ZZ*->4l veto", evtWeight);
    */
    
    
#else
#pragma message ("Warning***   hh_3l selection conditions will not be executed ")

    ///*double*/ evtWeight = 1.;
#endif


    cutFlowTable.update("Before gen-reco matching");

    if (genWHadronicFromH_WW_qqlnu && genWHadronicFromH_WW_qqlnu->pt() > 100. &&
	genJet1FromH_WW_qqlnu && genJet2FromH_WW_qqlnu) {
      cutFlowTable.update("genW_pT > 100");

      if (std::abs(genJet1FromH_WW_qqlnu->eta()) < 2.4 &&
	  std::abs(genJet2FromH_WW_qqlnu->eta()) < 2.4 ) {
	cutFlowTable.update("genWjet_eta < 2.4");

	if (deltaR(genJet1FromH_WW_qqlnu->p4(), genJet2FromH_WW_qqlnu->p4()) < 1.2) {
	  cutFlowTable.update("dR(genWjet1, genWjet2) < 1.2");
	  
	  if (selLeptons.size() >= 3) {
	    cutFlowTable.update("genW->jj boosted; selLep >= 3");
	    
	    if (jet_ptrs_ak8_Wjj.size() >= 1) {
	      cutFlowTable.update("genW_eta; AK8 >= 1");
	      
	      double AK8JetPt_max = -1.;
	      const RecoJetAK8* AK8JetLead = nullptr;
	      for (size_t ijet = 0; ijet < jet_ptrs_ak8_Wjj.size(); ++ijet) {
		//std::cout << "\tijet: " << ijet << ", pt: " << jet_ptrs_ak8_Wjj[ijet]->pt() << std::endl;
		if (jet_ptrs_ak8_Wjj[ijet]->pt() > AK8JetPt_max) {
		  AK8JetPt_max = jet_ptrs_ak8_Wjj[ijet]->pt();
		  AK8JetLead   = jet_ptrs_ak8_Wjj[ijet];
		}
	      }
	      
	      double dRAK8JetWBoson_min = 9999.;
	      const RecoJetAK8* AK8JetClosestToWBoson = nullptr;
	      for (size_t ijet = 0; ijet < jet_ptrs_ak8_Wjj.size(); ++ijet) {
		double dr = deltaR(jet_ptrs_ak8_Wjj[ijet]->p4(), genWHadronicFromH_WW_qqlnu->p4());
		if (dr < 0.4 && dr < dRAK8JetWBoson_min) {
		  dRAK8JetWBoson_min     = dr;
		  AK8JetClosestToWBoson  = jet_ptrs_ak8_Wjj[ijet];
		}	    
	      }
	      
	      if (AK8JetClosestToWBoson) {
		cutFlowTable.update("genW_eta; dR(AK8, W) < 0.4");
		
		if ( std::abs((AK8JetClosestToWBoson->pt() - AK8JetLead->pt())) < 0.01 ) {
		  cutFlowTable.update("genW_eta; dR(AK8, W) < 0.4 && AK8 is lead pt");
		}
		
		if (AK8JetClosestToWBoson->subJet1() && AK8JetClosestToWBoson->subJet2()) {
		  cutFlowTable.update("genW_eta; dR(AK8, W) < 0.4 && AK8subjets");
		  
		  
		  const double jetMatchdRThsh = 0.3;
		  if ( (deltaR(AK8JetClosestToWBoson->subJet1()->p4(), genJet1FromH_WW_qqlnu->p4()) < jetMatchdRThsh &&
			deltaR(AK8JetClosestToWBoson->subJet2()->p4(), genJet2FromH_WW_qqlnu->p4()) < jetMatchdRThsh   )   ||
		       (deltaR(AK8JetClosestToWBoson->subJet1()->p4(), genJet2FromH_WW_qqlnu->p4()) < jetMatchdRThsh &&
			deltaR(AK8JetClosestToWBoson->subJet2()->p4(), genJet1FromH_WW_qqlnu->p4()) < jetMatchdRThsh   ) ) {
		    cutFlowTable.update(Form("genW_eta; dR(AK8, W) < 0.4 && dR(AK8subjets, Wjet) < %g",jetMatchdRThsh));
		    
		    
		    if (deltaR(AK8JetClosestToWBoson->p4(), genLeptonFromH_WW_qqlnu->p4()) < 1.2) {
		      cutFlowTable.update("genW_eta; AK8==genW, AK8subjets==genWjet; dR(AK8, l3) < 1.2");
		      
		      double dRj1genl3 = deltaR(AK8JetClosestToWBoson->subJet1()->p4(), genLeptonFromH_WW_qqlnu->p4());
		      double dRj2genl3 = deltaR(AK8JetClosestToWBoson->subJet2()->p4(), genLeptonFromH_WW_qqlnu->p4());
		      if (dRj1genl3 > 0.1 && dRj2genl3 > 0.1) {
			cutFlowTable.update("genW_eta; AK8==genW, AK8subjets==genWjet; dR(AK8, l3) < 1.2 && dR(subjet, l3) > 0.1");
		      }
		    }
		    
		    
		    
		    const RecoJetAK8* AK8Jet = AK8JetClosestToWBoson;
		    size_t idxLepton_H_WW_ljj_1 = 9999;
		    //size_t idxLepton_H_WW_ljj_2 = 9999;
		    
		    // Seperate out H->WW->lNu jj lepton which is nearest to jj from H->WW->lNu jj 
		    // Approach - I 		    
		    for (size_t idxLepton1 = 0; idxLepton1 < 3; ++idxLepton1) {
		      for (size_t idxLepton2 = idxLepton1+1; idxLepton2 < 3; ++idxLepton2) {
			// no need to check opposite-sign lepton pair
			if (selLeptons[idxLepton1]->charge() * selLeptons[idxLepton2]->charge() < 0.) continue;
			
			if ( deltaR(AK8Jet->p4(), selLeptons[idxLepton1]->p4()) <
			     deltaR(AK8Jet->p4(), selLeptons[idxLepton2]->p4()) ) {
			  idxLepton_H_WW_ljj_1 = idxLepton1;
			} else {
			  idxLepton_H_WW_ljj_1 = idxLepton2;
			}
		      }
		    }
		     if ( isDEBUG ) std::cout << "idxLepton_H_WW_ljj_1: " << idxLepton_H_WW_ljj_1 << std::endl;
		    
		    
		    // Seperate out H->WW->lNu jj lepton from H->WW->2l2Nu leptons
		    // lepton pair with least dR would be from H->WW->2l2Nu, so the remained lepton would be from H->WW->lNu jj
		    // Approach - 0
		    size_t idxLepton_H_WW_ljj = -1;
		    double mindRLepton_H_WW_ll = 9999.;
		    //size_t idxLepton1_H_WW_ll = -1, idxLepton2_H_WW_ll = -1;
		    for (size_t idxLepton1 = 0; idxLepton1 < 3; ++idxLepton1) {
		      //std::cout<<"idxLepton1: "<<idxLepton1<<std::endl;
		      for (size_t idxLepton2 = idxLepton1+1; idxLepton2 < 3; ++idxLepton2) {
			double dr = deltaR(selLeptons[idxLepton1]->p4(), selLeptons[idxLepton2]->p4());
			if (dr < mindRLepton_H_WW_ll) {
			  mindRLepton_H_WW_ll = dr;
			  idxLepton_H_WW_ljj = 0;
			  if (idxLepton_H_WW_ljj == idxLepton1) idxLepton_H_WW_ljj++;
			  if (idxLepton_H_WW_ljj == idxLepton2) idxLepton_H_WW_ljj++;
			  //idxLepton1_H_WW_ll = idxLepton1;
			  //idxLepton2_H_WW_ll = idxLepton2;
			}
		      }
		    }
		    if ( isDEBUG ) std::cout << "idxLepton_H_WW_ljj: " << idxLepton_H_WW_ljj << std::endl;
		    /*
		      std::cout << "idxLepton1_H_WW_ll: "<<idxLepton1_H_WW_ll<<" (pT "<< selLeptons[idxLepton1_H_WW_ll]->pt()<<")"
		      <<", idxLepton2_H_WW_ll:"<<idxLepton2_H_WW_ll<<" (pT "<< selLeptons[idxLepton2_H_WW_ll]->pt()<<")"
		      <<", idxLepton_H_WW_ljj:"<<idxLepton_H_WW_ljj<<" (pT "<< selLeptons[idxLepton_H_WW_ljj]->pt()<<")"
		      << ", dR(Lepton Pair):"<<deltaR(selLeptons[idxLepton1_H_WW_ll]->p4(), selLeptons[idxLepton2_H_WW_ll]->p4())
		      << ", dR(Lepton Pair, 3rd lep): "<<deltaR(selLeptons[idxLepton1_H_WW_ll]->p4(), selLeptons[idxLepton_H_WW_ljj]->p4())
		      << " and "<<deltaR(selLeptons[idxLepton2_H_WW_ll]->p4(), selLeptons[idxLepton_H_WW_ljj]->p4())
		      << std::5ndl; */
		    

		    if (idxLepton_H_WW_ljj < 3 &&
			deltaR(selLeptons[idxLepton_H_WW_ljj]->p4(), genLeptonFromH_WW_qqlnu->p4()) < 0.1) {
		      cutFlowTable.update("genW_eta; AK8==genW, AK8subjets==genWjet; l_H_WW_ljj genMatch-approach_0");
		    }
		    
		    if (idxLepton_H_WW_ljj_1 < 3 &&
			deltaR(selLeptons[idxLepton_H_WW_ljj_1]->p4(), genLeptonFromH_WW_qqlnu->p4()) < 0.1) {
		      cutFlowTable.update("genW_eta; AK8==genW, AK8subjets==genWjet; l_H_WW_ljj genMatch-approach_I");

		      
		      //const RecoLepton* selLepton_H_WW_ljj = selLeptons[idxLepton_H_WW_ljj]; // approach-0
		      const RecoLepton* selLepton_H_WW_ljj = selLeptons[idxLepton_H_WW_ljj_1]; // approach-I
		      jetSelectorAK8_Wjj.getSelector().set_lepton(selLepton_H_WW_ljj);

		      double drl3Wjj = deltaR(AK8Jet->p4(), selLepton_H_WW_ljj->p4());
		      double drl3j1  = deltaR(AK8Jet->subJet1()->p4(), selLepton_H_WW_ljj->p4());
		      double drl3j2  = deltaR(AK8Jet->subJet2()->p4(), selLepton_H_WW_ljj->p4());
		      double drl3j   = (drl3j1 < drl3j2) ? drl3j1 : drl3j2;
		      hdRl3WHadronic_gen_AK8WjjSelector_all->Fill(drl3Wjj_gen);
		      hdRl3jFromWjj_gen_AK8WjjSelector_all->Fill(drl3j_gen);
		      hdRl3WHadronic_AK8WjjSelector_all->Fill(drl3Wjj);
		      hdRl3jFromWjj_AK8WjjSelector_all->Fill(drl3j);

		      const GenParticle* AK8subJet1_gen = nullptr;
		      const GenParticle* AK8subJet2_gen = nullptr; 
		      if ( deltaR(AK8JetClosestToWBoson->subJet1()->p4(), genJet1FromH_WW_qqlnu->p4()) <
			   deltaR(AK8JetClosestToWBoson->subJet1()->p4(), genJet2FromH_WW_qqlnu->p4()) ) {
			AK8subJet1_gen = genJet1FromH_WW_qqlnu;
			AK8subJet2_gen = genJet2FromH_WW_qqlnu;
		      } else {
			AK8subJet1_gen = genJet2FromH_WW_qqlnu;
			AK8subJet2_gen = genJet1FromH_WW_qqlnu;
		      }
		      double ptNormGen_jNearestL3 = (drl3j1 < drl3j2) ? 
			AK8JetClosestToWBoson->subJet1()->pt() / AK8subJet1_gen->pt() :
			AK8JetClosestToWBoson->subJet2()->pt() / AK8subJet2_gen->pt();		      
		      hdRl3jFromWjj_vs_RecGenPt_AK8WjjSelector_all->Fill(drl3j, ptNormGen_jNearestL3);
		      
                      std::string jetReturnType;
		      if (jetSelectorAK8_Wjj.getSelector()(*AK8Jet, jetReturnType)) {
			cutFlowTable.update(Form("AK8==genW, AK8subjets==genWjet; l3=genl3; AK8 passed AK8_Wjj selector "));
			hdRl3WHadronic_gen_AK8WjjSelector_Selected->Fill(drl3Wjj_gen);
			hdRl3jFromWjj_gen_AK8WjjSelector_Selected->Fill(drl3j_gen);
			hdRl3WHadronic_AK8WjjSelector_Selected->Fill(drl3Wjj);
			hdRl3jFromWjj_AK8WjjSelector_Selected->Fill(drl3j);
			hdRl3jFromWjj_vs_RecGenPt_AK8WjjSelector_Selected->Fill(drl3j, ptNormGen_jNearestL3);
		      } else {
                        cutFlowTable.update(Form("AK8==genW, AK8subjets==genWjet; l3=genl3; AK8 failed AK8_Wjj selector due to %s",jetReturnType.data()));
			hdRl3WHadronic_gen_AK8WjjSelector_Rejected->Fill(drl3Wjj_gen);
			hdRl3jFromWjj_gen_AK8WjjSelector_Rejected->Fill(drl3j_gen);
			hdRl3WHadronic_AK8WjjSelector_Rejected->Fill(drl3Wjj);
			hdRl3jFromWjj_AK8WjjSelector_Rejected->Fill(drl3j);
			hdRl3jFromWjj_vs_RecGenPt_AK8WjjSelector_Rejected->Fill(drl3j, ptNormGen_jNearestL3);
			
			if (1==1) {
			  std::cout << "\n\nprocessing Entry " << inputTree -> getCurrentMaxEventIdx()
				    << " or " << inputTree -> getCurrentEventIdx() << " entry in #"
				    << (inputTree -> getProcessedFileCount() - 1)
				    << " (" << eventInfo
				    << ") file (" << selectedEntries << " Entries selected)\n";
                          printf("AK8==genW, AK8subjets==genWjet; l3=genl3; AK8 failed AK8_Wjj selector due to %s\n",jetReturnType.data());
			  
			  //dumpGenParticles("genWBoson", genWBosons);
			  //dumpGenParticles("genWJet", genWJets);

			  printf("genW->qq: pt %g, eta %f, phi %f \n",genWHadronicFromH_WW_qqlnu->pt(),genWHadronicFromH_WW_qqlnu->eta(),genWHadronicFromH_WW_qqlnu->phi());
			  
			  printf("genJ1: pt %g, eta %f, phi %f \n",genJet1FromH_WW_qqlnu->pt(),genJet1FromH_WW_qqlnu->eta(),genJet1FromH_WW_qqlnu->phi());
			  printf("genJ2: pt %g, eta %f, phi %f \n",genJet2FromH_WW_qqlnu->pt(),genJet2FromH_WW_qqlnu->eta(),genJet2FromH_WW_qqlnu->phi());
			  printf("genl3: pt %g, eta %f, phi %f \n",genLeptonFromH_WW_qqlnu->pt(),genLeptonFromH_WW_qqlnu->eta(),genLeptonFromH_WW_qqlnu->phi());
			  printf("genl1: pt %g, eta %f, phi %f \n",genLepton1FromH_WW_lnulnu->pt(),genLepton1FromH_WW_lnulnu->eta(),genLepton1FromH_WW_lnulnu->phi());
			  printf("genl2: pt %g, eta %f, phi %f \n",genLepton1FromH_WW_lnulnu->pt(),genLepton1FromH_WW_lnulnu->eta(),genLepton1FromH_WW_lnulnu->phi());

			  printf("recl3: pt %g, eta %f, phi %f \n",selLepton_H_WW_ljj->pt(),selLepton_H_WW_ljj->eta(),selLepton_H_WW_ljj->phi());
			  printf("AK8Jet: pt %g, eta %f, phi %f \n",AK8Jet->pt(),AK8Jet->eta(),AK8Jet->phi());
			  printf("AK8subjet1: pt %g, eta %f, phi %f \n",AK8Jet->subJet1()->pt(),AK8Jet->subJet1()->eta(),AK8Jet->subJet1()->phi());
			  printf("AK8subjet2: pt %g, eta %f, phi %f \n",AK8Jet->subJet2()->pt(),AK8Jet->subJet2()->eta(),AK8Jet->subJet2()->phi());

			  			  


			  printf("drl3j %f, \t drl3j_gen %f\n",drl3j,drl3j_gen); 
			  //printWjj(jet_ptrs_ak8_Wjj, jetSelectorAK8_Wjj, genWBosons, genWJets);
			}
			
		      }
		      
		      
		      // select jets from H->bb decay
		      // Don't clean AK8 w.r.t. lepton
		      //std::vector<const RecoJetAK8*> cleanedJetsAK8_wrtLeptons = jetCleanerAK8_dR08(jet_ptrs_ak8_Wjj, fakeableLeptons);
		      //std::vector<const RecoJetAK8*> selJetsAK8_Wjj = jetSelectorAK8_Wjj(cleanedJetsAK8_wrtLeptons, isHigherPt);
		      std::vector<const RecoJetAK8*> selJetsAK8_Wjj = jetSelectorAK8_Wjj(jet_ptrs_ak8_Wjj, isHigherPt);
		      const RecoJetAK8* selJetAK8_Wjj = nullptr;
		      const RecoJetBase* selJet1_Wjj = nullptr;
		      const RecoJetBase* selJet2_Wjj = nullptr;

		      if (selJetsAK8_Wjj.size() >= 1 && selJetsAK8_Wjj[0]) {
			cutFlowTable.update("genW_eta; AK8==genW, AK8subjets==genWjet; l_H_WW_ljj genMatch-approach_I; AK8_Wjj");
			if (deltaR(selJetsAK8_Wjj[0]->p4(), genWHadronicFromH_WW_qqlnu->p4()) < 0.4) {
			  cutFlowTable.update("genW_eta; AK8==genW, AK8subjets==genWjet; l_H_WW_ljj genMatch-approach_I; dR(AK8_Wjj, genW) < 0.4");

			  if (selJetsAK8_Wjj[0]->subJet1() && selJetsAK8_Wjj[0]->subJet2()) {
			    cutFlowTable.update("genW_eta; AK8==genW, AK8subjets==genWjet; l_H_WW_ljj genMatch-approach_I; dR(AK8_Wjj, genW) < 0.4; AK8_Wjj_subjets");
			    if ( (deltaR(selJetsAK8_Wjj[0]->subJet1()->p4(), genJet1FromH_WW_qqlnu->p4()) < jetMatchdRThsh &&
				  deltaR(selJetsAK8_Wjj[0]->subJet2()->p4(), genJet2FromH_WW_qqlnu->p4()) < jetMatchdRThsh   )   ||
				 (deltaR(selJetsAK8_Wjj[0]->subJet1()->p4(), genJet2FromH_WW_qqlnu->p4()) < jetMatchdRThsh &&
				  deltaR(selJetsAK8_Wjj[0]->subJet2()->p4(), genJet1FromH_WW_qqlnu->p4()) < jetMatchdRThsh   ) ) {
			      cutFlowTable.update(Form("genW_eta; AK8==genW, AK8subjets==genWjet; l_H_WW_ljj genMatch-approach_I; dR(AK8_Wjj, genW) < 0.4; dR(AK8_Wjj_subjet, genWjet) < %g",jetMatchdRThsh));
			    }
			  }
			}

			
		      }
		    }
		    

		    
		  }
		}
	      }
	    }
	  }
	}
      }
    }
    








































    ++selectedEntries;
    //selectedEntries_weighted += evtWeight;
    histogram_selectedEntries->Fill(0.);
  }

  std::cout << "max num. Entries = " << inputTree -> getCumulativeMaxEventCount()
            << " (limited by " << maxEvents << ") processed in "
            << inputTree -> getProcessedFileCount() << " file(s) (out of "
            << inputTree -> getFileCount() << ")\n"
            << " analyzed = " << analyzedEntries << '\n'
            << " selected = " << selectedEntries << " (weighted = " << selectedEntries_weighted << ")\n\n"
            << "cut-flow table" << std::endl;
  cutFlowTable.print(std::cout);
  std::cout << std::endl;

  std::cout << "sel. Entries by gen. matching:" << std::endl;
  for ( std::vector<leptonGenMatchEntry>::const_iterator leptonGenMatch_definition = leptonGenMatch_definitions.begin();
	leptonGenMatch_definition != leptonGenMatch_definitions.end(); ++leptonGenMatch_definition ) {

    std::string process_and_genMatch = process_string;
    if ( apply_leptonGenMatching ) process_and_genMatch += leptonGenMatch_definition->name_;

    int idxLepton = leptonGenMatch_definition->idx_;

    const TH1* histogram_EventCounter = selHistManagers[idxLepton]->evt_->getHistogram_EventCounter();
    std::cout << " " << process_and_genMatch << " = " << histogram_EventCounter->GetEntries() << " (weighted = " << histogram_EventCounter->Integral() << ")" << std::endl;
  }
  std::cout << std::endl;

  delete dataToMCcorrectionInterface;

  delete leptonFakeRateInterface;

  delete run_lumi_eventSelector;

  delete selEventsFile;

  delete muonReader;
  delete electronReader;
  delete hadTauReader;
  delete jetReaderAK4;
  delete metReader;
  delete metFilterReader;
  delete genLeptonReader;
  delete genHadTauReader;
  delete genPhotonReader;
  delete genJetReader;
  delete lheInfoReader;

  delete genEvtHistManager_beforeCuts;
  delete genEvtHistManager_afterCuts;
  delete lheInfoHistManager;
  delete cutFlowHistManager;
  delete eventWeightManager;

  hltPaths_delete(triggers_1e);
  hltPaths_delete(triggers_2e);
  hltPaths_delete(triggers_1mu);
  hltPaths_delete(triggers_2mu);
  hltPaths_delete(triggers_1e1mu);

  delete inputTree;

  clock.Show("analyze_hh_3l_gen");

  return EXIT_SUCCESS;
}
