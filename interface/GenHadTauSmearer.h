#ifndef hhAnalysis_tttt_GenHadTauSmearer_h
#define hhAnalysis_tttt_GenHadTauSmearer_h

/** \class GenHadTauSmearer
 * Produce collection of GenJet objects corresponding to hadronic tau decays
 * with energy resolution smeared by Crystal-Ball function
 * 
 * \author Christian Veelken, Tallinn
 *
 */

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector

#include <TGraph.h>
#include <TRandom3.h>

#include <string>

class GenHadTauSmearer
{
 public:
  explicit GenHadTauSmearer(const edm::ParameterSet&);
  ~GenHadTauSmearer();
  
  Particle::LorentzVector operator()(const Particle::LorentzVector& p4) const;

 private:
  std::string inputFileName_;
  std::string graphName_;
  const TGraph* graph_;

  mutable TRandom3 rnd_;
};

#endif
