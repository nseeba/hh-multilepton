#ifndef hhAnalysis_tttt_mySVfit4tauAuxFunctions_h
#define hhAnalysis_tttt_mySVfit4tauAuxFunctions_h

#include "tthAnalysis/HiggsToTauTau/interface/GenParticle.h" // GenParticle
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt

#include "TauAnalysis/ClassicSVfit/interface/MeasuredTauLepton.h" // classic_svFit::MeasuredTauLepton

classic_svFit::MeasuredTauLepton makeMeasuredTauLepton(const Particle::LorentzVector& measuredTauP4, int measuredTauType, int measuredHadTauDecayMode);

int getMeasuredTauLeptonType(const GenParticle& measuredTau);

bool isGenHadTau(const GenParticle& measuredTau);

bool getHadTauDecayMode(const GenParticle& measuredTau);

struct SVfit4tauResult
{
  SVfit4tauResult()
    : dihiggs_visMass_(-1.)
    , dihiggs_mass_(-1.)
    , dihiggs_massErr_(-1.)
    , ditau1_visMass_(-1.)
    , ditau1_mass_(-1.)
    , ditau1_massErr_(-1.)
    , ditau2_visMass_(-1.)
    , ditau2_mass_(-1.)
    , ditau2_massErr_(-1.)
    , probMax_(-1.)
    , isValidSolution_(false)
  {}
  ~SVfit4tauResult() {}
  double dihiggs_visMass_;
  double dihiggs_mass_;
  double dihiggs_massErr_;
  double ditau1_visMass_;
  double ditau1_mass_;
  double ditau1_massErr_;
  double ditau2_visMass_;
  double ditau2_mass_;
  double ditau2_massErr_;
  double probMax_;
  bool isValidSolution_;
};

std::vector<SVfit4tauResult>
compSVfit4(const GenParticle& measuredTau1, 
	   const GenParticle& measuredTau2, 
	   const GenParticle& measuredTau3, 
	   const GenParticle& measuredTau4, 
	   const RecoMEt& met,
	   const std::string& chargeSumSelection_string,
	   double massConstraint = -1.); // CV: default is not to apply mass constraint

#endif
