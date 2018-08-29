#include "hhAnalysis/multilepton/interface/GenHadTauSmearer.h"

#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/ParameterSet/interface/FileInPath.h"

#include "DataFormats/Candidate/interface/Candidate.h" // reco::Candidate::LorentzVector

#include <TFile.h>
#include <TMath.h> // TMath::Cos, TMath::Sin, TMath::Sqrt

namespace
{
  std::string findFile(const std::string& fileName)
  {
    edm::FileInPath inputFile(fileName);
    if ( inputFile.fullPath() == "" ) {
      std::cerr << "Error: Cannot find file = " << fileName << " !!" << std::endl;
      assert(0);
    }
    return inputFile.fullPath().data();
  }

  template<typename T>
  const T* readGraph(TFile* inputFile, const std::string& graphName)
  {
    T* graph = dynamic_cast<T*>(inputFile->Get(graphName.data()));
    if ( !graph ) {
      std::cerr << "<readGraph>: Failed to load graph = " << graphName << " from file = " << inputFile->GetName() << " !!" << std::endl;
      assert(0);
    }
    return (T*)graph->Clone();
  }
}

GenHadTauSmearer::GenHadTauSmearer(const edm::ParameterSet& cfg)
  : graph_(0)
{ 
  inputFileName_ = cfg.getParameter<std::string>("inputFileName");
  TFile* inputFile = new TFile(findFile(inputFileName_).data());
  graphName_ = cfg.getParameter<std::string>("graphName");
  graph_ = readGraph<TGraph>(inputFile, graphName_);
  delete inputFile;

  rnd_.SetSeed(0);
}

GenHadTauSmearer::~GenHadTauSmearer()
{
  delete graph_;
}

Particle::LorentzVector GenHadTauSmearer::operator()(const Particle::LorentzVector& p4) const
{
  //std::cout << "<GenHadTauSmearer::operator()>:" << std::endl;

  //double smearFactor = rnd_.Gaus(1.0, 0.10); // CV: only for testing, to be replaced by Betty's crystal-ball code later !!
  double u = rnd_.Rndm();
  double smearFactor = graph_->Eval(u);

  double mass = p4.mass();
  double en_smeared = smearFactor*p4.E();
  if ( en_smeared < mass ) en_smeared = mass;
  double p_smeared = TMath::Sqrt(en_smeared*en_smeared - mass*mass);
  double px_smeared = TMath::Cos(p4.phi())*TMath::Sin(p4.theta())*p_smeared;
  double py_smeared = TMath::Sin(p4.phi())*TMath::Sin(p4.theta())*p_smeared;
  double pz_smeared = TMath::Cos(p4.theta())*p_smeared;
  reco::Candidate::LorentzVector p4_smeared(px_smeared, py_smeared, pz_smeared, en_smeared);
  return Particle::LorentzVector(p4_smeared.pt(), p4_smeared.eta(), p4_smeared.phi(), p4_smeared.mass());
}
