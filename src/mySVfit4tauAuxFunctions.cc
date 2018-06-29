#include "hhAnalysis/tttt/interface/mySVfit4tauAuxFunctions.h"

#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h" // RecoHadTau

#include "TauAnalysis/ClassicSVfit/interface/MeasuredTauLepton.h" // classic_svFit::MeasuredTauLepton

classic_svFit::MeasuredTauLepton makeMeasuredTauLepton(const Particle::LorentzVector& measuredTauP4, int measuredTauType, int measuredHadTauDecayMode)
{
  if ( measuredTauType == classic_svFit::MeasuredTauLepton::kTauToElecDecay || 
       measuredTauType == classic_svFit::MeasuredTauLepton::kTauToMuDecay   ) {
    return classic_svFit::MeasuredTauLepton(measuredTauType, measuredTauP4.pt(), measuredTauP4.eta(), measuredTauP4.phi(), measuredTauP4.mass());
  } else {
    return classic_svFit::MeasuredTauLepton(measuredTauType, measuredTauP4.pt(), measuredTauP4.eta(), measuredTauP4.phi(), measuredTauP4.mass(), measuredHadTauDecayMode);
  }
}

int getMeasuredTauLeptonType(const GenParticle& measuredTau)
{
  int measuredTauType = classic_svFit::MeasuredTauLepton::kUndefinedDecayType;
  if      ( TMath::Abs(measuredTau.pdgId()) == 11 ) measuredTauType = classic_svFit::MeasuredTauLepton::kTauToElecDecay;
  else if ( TMath::Abs(measuredTau.pdgId()) == 13 ) measuredTauType = classic_svFit::MeasuredTauLepton::kTauToMuDecay;
  else                                              measuredTauType = classic_svFit::MeasuredTauLepton::kTauToHadDecay;
  return measuredTauType;
}

bool isGenHadTau(const GenParticle& measuredTau)
{
  if ( getMeasuredTauLeptonType(measuredTau) == classic_svFit::MeasuredTauLepton::kTauToHadDecay ) return true;
  else return false;
}

bool getHadTauDecayMode(const GenParticle& measuredTau)
{
  int decayMode = -1;
  if ( isGenHadTau(measuredTau) ) {
    const RecoHadTau* recHadTau = dynamic_cast<const RecoHadTau*>(&measuredTau);
    if ( recHadTau ) {
      decayMode = recHadTau->decayMode();
    } else {
      double mass = measuredTau.mass();
      if ( mass < 0.2 ) decayMode = 0; // 1prong0pi0
      else decayMode = 11;             // 3prong1pi0
    }
  }
  return decayMode;
}
