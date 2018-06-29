#ifndef hhAnalysis_tttt_mySVfit4tauAuxFunctions_h
#define hhAnalysis_tttt_mySVfit4tauAuxFunctions_h

#include "tthAnalysis/HiggsToTauTau/interface/GenParticle.h" // GenParticle

#include "TauAnalysis/ClassicSVfit/interface/MeasuredTauLepton.h" // classic_svFit::MeasuredTauLepton

classic_svFit::MeasuredTauLepton makeMeasuredTauLepton(const Particle::LorentzVector& measuredTauP4, int measuredTauType, int measuredHadTauDecayMode = -1);

int getMeasuredTauLeptonType(const GenParticle& measuredTau);

bool isGenHadTau(const GenParticle& measuredTau);

bool getHadTauDecayMode(const GenParticle& measuredTau);

#endif
