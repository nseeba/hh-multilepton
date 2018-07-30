#include "hhAnalysis/tttt/interface/mySVfit4tauAuxFunctions.h"

#include "FWCore/Utilities/interface/Exception.h" // cms::Exception

#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h" // RecoHadTau

#include "TauAnalysis/ClassicSVfit4tau/interface/ClassicSVfit4tau.h" // ClassicSVfit4tau
#include "TauAnalysis/ClassicSVfit/interface/MeasuredTauLepton.h" // classic_svFit::MeasuredTauLepton

#include <TMatrixD.h> // TMatrixD
#include <TMath.h> // TMath::Abs, TMath::Cos, TMath::Sin

#include <algorithm> // std::sort

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

namespace
{
  bool
  isHigherProbMax(const SVfit4tauResult& result1,
		  const SVfit4tauResult& result2)
  {
    return result1.probMax_ > result2.probMax_;
  }
}

std::vector<SVfit4tauResult> compSVfit4tau(const GenParticle& measuredTau1, 
					   const GenParticle& measuredTau2, 
					   const GenParticle& measuredTau3, 
					   const GenParticle& measuredTau4, 
					   const RecoMEt& met,
					   const std::string& chargeSumSelection_string,
					   double massConstraint,
					   int verbosity)
{
  if ( verbosity >= 1 ) {
    std::cout << "<compSVfit4tau>:" << std::endl;
    std::cout << " massConstraint = " << massConstraint << std::endl;
  }

  enum { kOS, kSS };
  int chargeSumSelection = -1;
  if      ( chargeSumSelection_string == "OS"       ) chargeSumSelection = kOS;
  else if ( chargeSumSelection_string == "SS"       ) chargeSumSelection = kSS;
  else throw cms::Exception("compSVfit4")
    << "Invalid Configuration parameter 'chargeSumSelection' = " << chargeSumSelection_string << " !!\n";

  std::vector<SVfit4tauResult> results;

  std::vector<const GenParticle*> measuredTaus;
  measuredTaus.push_back(&measuredTau1);
  measuredTaus.push_back(&measuredTau2);
  measuredTaus.push_back(&measuredTau3);
  measuredTaus.push_back(&measuredTau4);
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
	  // require decay products of 2nd Higgs boson to have opposite or same charge, 
	  // depending on chargeSumSelection flag
	  if ( (chargeSumSelection == kOS && ((*measuredTau3)->charge() + (*measuredTau4)->charge()) != 0) ||
	       (chargeSumSelection == kSS && ((*measuredTau3)->charge() + (*measuredTau4)->charge()) == 0) ) continue;
	  
	  // require that all taus are different
	  if ( (*measuredTau3) == (*measuredTau1) || (*measuredTau3) == (*measuredTau2) ) continue;
	  if ( (*measuredTau4) == (*measuredTau1) || (*measuredTau4) == (*measuredTau2) ) continue;
	  
	  // require that tau1 has higher pT than tau3,
	  // in order prevent that SVfit mass is computed for both combinations (tau1,..,tau3,..) and (tau3,..,tau1,..)
	  if ( !((*measuredTau1)->pt() > (*measuredTau3)->pt()) ) continue;
	  
	  // CV: require that visible mass of tau1+tau2 and of tau3+tau4 is less than the Higgs boson mass,
	  //     as SVfit will otherwise not find a physical solution anyway
	  if ( (massConstraint > 0. && ((*measuredTau1)->p4() + (*measuredTau2)->p4()).mass() > massConstraint) || 
	       (massConstraint > 0. && ((*measuredTau3)->p4() + (*measuredTau4)->p4()).mass() > massConstraint) ) continue;

	  Particle::LorentzVector measuredTau1P4 = (*measuredTau1)->p4();
	  int  measuredTau1Type = getMeasuredTauLeptonType(**measuredTau1);
	  int measuredHadTau1DecayMode = getHadTauDecayMode(**measuredTau1);
	  Particle::LorentzVector measuredTau2P4 = (*measuredTau2)->p4();
	  int measuredTau2Type = getMeasuredTauLeptonType(**measuredTau2);
	  int measuredHadTau2DecayMode = getHadTauDecayMode(**measuredTau2);
	  Particle::LorentzVector measuredTau3P4 = (*measuredTau3)->p4();
	  int measuredTau3Type = getMeasuredTauLeptonType(**measuredTau3);
	  int measuredHadTau3DecayMode = getHadTauDecayMode(**measuredTau3);
	  Particle::LorentzVector measuredTau4P4 = (*measuredTau4)->p4();
	  int measuredTau4Type = getMeasuredTauLeptonType(**measuredTau4);
	  int measuredHadTau4DecayMode = getHadTauDecayMode(**measuredTau4);
	  double metPx = met.pt()*TMath::Cos(met.phi());
	  double metPy = met.pt()*TMath::Sin(met.phi());
	  TMatrixD metCov(2,2);
	  metCov[0][0] = met.covXX();
	  metCov[1][0] = met.covXY();
	  metCov[0][1] = met.covXY();
	  metCov[1][1] = met.covYY();
	  
	  //-------------------------------------------------------------------------------------
	  // CV: run ClassicSVfit4tau algorithm
	  std::vector<classic_svFit::MeasuredTauLepton> measuredTauLeptons;
	  measuredTauLeptons.push_back(makeMeasuredTauLepton(measuredTau1P4, measuredTau1Type, measuredHadTau1DecayMode));
	  measuredTauLeptons.push_back(makeMeasuredTauLepton(measuredTau2P4, measuredTau2Type, measuredHadTau2DecayMode));
	  measuredTauLeptons.push_back(makeMeasuredTauLepton(measuredTau3P4, measuredTau3Type, measuredHadTau3DecayMode));
	  measuredTauLeptons.push_back(makeMeasuredTauLepton(measuredTau4P4, measuredTau4Type, measuredHadTau4DecayMode));
	  
	  ClassicSVfit4tau svFitAlgo(verbosity);
	  double logM_wMassConstraint = 2.;
	  if ( logM_wMassConstraint > 0. ) {
	    svFitAlgo.addLogM_fixed(true, logM_wMassConstraint);
	  } else {
	    svFitAlgo.addLogM_fixed(false);
	  }
	  svFitAlgo.setDiTau1MassConstraint(massConstraint);
	  svFitAlgo.setDiTau2MassConstraint(massConstraint);  
	  svFitAlgo.integrate(measuredTauLeptons, metPx, metPy, metCov);
	  if ( svFitAlgo.isValidSolution() ) {
	    SVfit4tauResult result;
	    result.dihiggs_visMass_ = ((*measuredTau1)->p4() + (*measuredTau2)->p4() + (*measuredTau3)->p4() + (*measuredTau4)->p4()).mass();
	    classic_svFit::HistogramAdapterDiHiggs* dihiggs = static_cast<classic_svFit::HistogramAdapterDiHiggs*>(svFitAlgo.getHistogramAdapter());
	    result.dihiggs_mass_    = dihiggs->getMass();
	    result.dihiggs_massErr_ = dihiggs->getMassErr();
	    result.ditau1_visMass_  = ((*measuredTau1)->p4() + (*measuredTau2)->p4()).mass();
	    classic_svFit::HistogramAdapterDiTau* ditau1 = dihiggs->ditau1();
	    result.ditau1_mass_     = ditau1->getMass();
	    result.ditau1_massErr_  = ditau1->getMassErr();
	    result.ditau2_visMass_  = ((*measuredTau3)->p4() + (*measuredTau4)->p4()).mass();
	    classic_svFit::HistogramAdapterDiTau* ditau2 = dihiggs->ditau2();
	    result.ditau2_mass_     = ditau2->getMass();
	    result.ditau2_massErr_  = ditau2->getMassErr();
	    result.probMax_         = svFitAlgo.getProbMax();
	    result.isValidSolution_ = true;
	    results.push_back(result);
	  } else {
	    SVfit4tauResult result;
	    result.isValidSolution_ = false;
	    results.push_back(result);
	  }
	}
      }
    }
  }

  // sort SVfit4tau solutions by decreasing probMax, the maximum of integrand within the integration domain
  std::sort(results.begin(), results.end(), isHigherProbMax);

  return results;
}
