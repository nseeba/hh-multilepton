#include "hhAnalysis/tttt/interface/mySVfit4tauAuxFunctions.h"

#include "FWCore/Utilities/interface/Exception.h" // cms::Exception

#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h" // RecoHadTau
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // isHigherPt

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

bool
isHigherProbMax(const SVfit4tauResult& result1,
		const SVfit4tauResult& result2)
{
  if ( result1.isValidSolution_ && !result2.isValidSolution_ ) return true;
  if ( result2.isValidSolution_ && !result1.isValidSolution_ ) return false;
  return result1.probMax_ > result2.probMax_;
}

bool
isHigherLmax(const SVfit4tauResult& result1,
	     const SVfit4tauResult& result2)
{
  if ( result1.isValidSolution_ && !result2.isValidSolution_ ) return true;
  if ( result2.isValidSolution_ && !result1.isValidSolution_ ) return false;
  return result1.Lmax_ > result2.Lmax_;
}

bool
isLowerMassErr(const SVfit4tauResult& result1,
	       const SVfit4tauResult& result2)
{
  if ( result1.isValidSolution_ && !result2.isValidSolution_ ) return true;
  if ( result2.isValidSolution_ && !result1.isValidSolution_ ) return false;
  return result1.dihiggs_massErr_ < result2.dihiggs_massErr_;
}

std::vector<SVfit4tauResult> compSVfit4tau(const GenParticle& measuredTau1, 
					   const GenParticle& measuredTau2, 
					   const GenParticle& measuredTau3, 
					   const GenParticle& measuredTau4, 
					   const RecoMEt& met,
					   const std::string& chargeSumSelection_string, TRandom& rnd,
					   int intAlgo,
					   double massConstraint,
					   double logM,
					   int verbosity)
{
  //if ( verbosity >= 1 ) {
  //  std::cout << "<compSVfit4tau>:" << std::endl;
  //  std::cout << " massConstraint = " << massConstraint << ", logM = " << logM << std::endl;
  //}

  enum { kOS, kSS };
  int chargeSumSelection = -1;
  if      ( chargeSumSelection_string == "OS"       ) chargeSumSelection = kOS;
  else if ( chargeSumSelection_string == "SS"       ) chargeSumSelection = kSS;
  else throw cms::Exception("compSVfit4")
    << "Invalid Configuration parameter 'chargeSumSelection' = " << chargeSumSelection_string << " !!\n";
  double u = rnd.Rndm(); // uniformly distributed random number within the intervall [0,1[

  std::vector<SVfit4tauResult> results;

  std::vector<const GenParticle*> measuredTaus;
  measuredTaus.push_back(&measuredTau1);
  measuredTaus.push_back(&measuredTau2);
  measuredTaus.push_back(&measuredTau3);
  measuredTaus.push_back(&measuredTau4);
  std::sort(measuredTaus.begin(), measuredTaus.end(), isHigherPt);
  size_t numMeasuredTaus = measuredTaus.size();
  assert(numMeasuredTaus == 4);
  for ( size_t idxMeasuredTau1 = 0; idxMeasuredTau1 < numMeasuredTaus; ++idxMeasuredTau1 ) {
    const GenParticle* measuredTau1 = measuredTaus[idxMeasuredTau1];
    for ( size_t idxMeasuredTau2 = idxMeasuredTau1 + 1; idxMeasuredTau2 < numMeasuredTaus; ++idxMeasuredTau2 ) { // tau1 has higher pT than tau2
      const GenParticle* measuredTau2 = measuredTaus[idxMeasuredTau2];
      for ( size_t idxMeasuredTau3 = 0; idxMeasuredTau3 < numMeasuredTaus; ++idxMeasuredTau3 ) {
	const GenParticle* measuredTau3 = measuredTaus[idxMeasuredTau3];
	for ( size_t idxMeasuredTau4 = idxMeasuredTau3 + 1; idxMeasuredTau4 < numMeasuredTaus; ++idxMeasuredTau4 ) { // tau3 has higher pT than tau4
	  const GenParticle* measuredTau4 = measuredTaus[idxMeasuredTau4];
	  
	  if ( chargeSumSelection == kOS ) {
	    // require decay products of 1st Higgs boson to have opposite charge
	    if ( (measuredTau1->charge() + measuredTau2->charge()) != 0 ) continue;
	    // require decay products of 2nd Higgs boson to have opposite charge
	    if ( (measuredTau3->charge() + measuredTau4->charge()) != 0 ) continue;
	  } else {
	    if ( u < 1./3 ) {
	      if ( idxMeasuredTau1 == 1 && idxMeasuredTau2 == 2 && idxMeasuredTau3 == 3 && idxMeasuredTau4 == 4 ) continue;
	    } else if ( u < 2./3 ) {
	      if ( idxMeasuredTau1 == 1 && idxMeasuredTau2 == 3 && idxMeasuredTau3 == 2 && idxMeasuredTau4 == 4 ) continue;
	    } else {
	      if ( idxMeasuredTau1 == 1 && idxMeasuredTau2 == 4 && idxMeasuredTau3 == 2 && idxMeasuredTau4 == 3 ) continue;
	    }
	  }
	  
	  // require that all taus are different
	  if ( measuredTau3 == measuredTau1 || measuredTau3 == measuredTau2 ) continue;
	  if ( measuredTau4 == measuredTau1 || measuredTau4 == measuredTau2 ) continue;
	  
	  // require that tau1 has higher pT than tau3,
	  // in order prevent that SVfit mass is computed for both combinations (tau1,..,tau3,..) and (tau3,..,tau1,..)
	  if ( !(measuredTau1->pt() > measuredTau3->pt()) ) continue;
	  
	  Particle::LorentzVector measuredTau1P4 = measuredTau1->p4();
	  int  measuredTau1Type = getMeasuredTauLeptonType(*measuredTau1);
	  int measuredHadTau1DecayMode = getHadTauDecayMode(*measuredTau1);
	  Particle::LorentzVector measuredTau2P4 = measuredTau2->p4();
	  int measuredTau2Type = getMeasuredTauLeptonType(*measuredTau2);
	  int measuredHadTau2DecayMode = getHadTauDecayMode(*measuredTau2);
	  Particle::LorentzVector measuredTau3P4 = measuredTau3->p4();
	  int measuredTau3Type = getMeasuredTauLeptonType(*measuredTau3);
	  int measuredHadTau3DecayMode = getHadTauDecayMode(*measuredTau3);
	  Particle::LorentzVector measuredTau4P4 = measuredTau4->p4();
	  int measuredTau4Type = getMeasuredTauLeptonType(*measuredTau4);
	  int measuredHadTau4DecayMode = getHadTauDecayMode(*measuredTau4);
	  double metPx = met.pt()*TMath::Cos(met.phi());
	  double metPy = met.pt()*TMath::Sin(met.phi());
	  TMatrixD metCov(2,2);
	  metCov[0][0] = met.covXX();
	  metCov[1][0] = met.covXY();
	  metCov[0][1] = met.covXY();
	  metCov[1][1] = met.covYY();
	  
	  // CV: run ClassicSVfit4tau algorithm
	  SVfit4tauResult result = compSVfit4tau(
            measuredTau1P4, measuredTau1Type, measuredHadTau1DecayMode,
	    measuredTau2P4, measuredTau2Type, measuredHadTau2DecayMode,
	    measuredTau3P4, measuredTau3Type, measuredHadTau3DecayMode,
	    measuredTau4P4, measuredTau4Type, measuredHadTau4DecayMode,
	    metPx, metPy, metCov,
	    intAlgo,
	    massConstraint,
	    logM,
	    verbosity);
	  results.push_back(result);
	}
      }
    }
  }

  // sort SVfit4tau solutions by decreasing probMax, the maximum of integrand within the integration domain
  std::sort(results.begin(), results.end(), isHigherProbMax);

  return results;
}

SVfit4tauResult
compSVfit4tau(const Particle::LorentzVector& measuredTau1Higgs1P4, int measuredTau1Higgs1Type, int measuredHadTau1Higgs1DecayMode,
	      const Particle::LorentzVector& measuredTau2Higgs1P4, int measuredTau2Higgs1Type, int measuredHadTau2Higgs1DecayMode,
	      const Particle::LorentzVector& measuredTau1Higgs2P4, int measuredTau1Higgs2Type, int measuredHadTau1Higgs2DecayMode,
	      const Particle::LorentzVector& measuredTau2Higgs2P4, int measuredTau2Higgs2Type, int measuredHadTau2Higgs2DecayMode,
	      double metPx, double metPy, const TMatrixD& metCov,
	      int intAlgo,
	      double massConstraint,
	      double logM,
	      int verbosity)
{
  if ( verbosity >= 1 ) {
    std::cout << "<compSVfit4tau>:" << std::endl;
    std::cout << " massConstraint = " << massConstraint << ", logM = " << logM << std::endl;
  }

  // CV: require that visible mass of tau1+tau2 and of tau3+tau4 is less than the Higgs boson mass,
  //     as SVfit will otherwise not find a physical solution anyway
  if ( (massConstraint > 0. && (measuredTau1Higgs1P4 + measuredTau2Higgs1P4).mass() > massConstraint) || 
       (massConstraint > 0. && (measuredTau1Higgs2P4 + measuredTau2Higgs2P4).mass() > massConstraint) ) {
    if ( verbosity >= 1 ) {
      std::cout << "skipping event, because either" 
		<< " ditau1VisMass = " << (measuredTau1Higgs1P4 + measuredTau2Higgs1P4).mass() << " or"
		<< " ditau2VisMass = " << (measuredTau1Higgs2P4 + measuredTau2Higgs2P4).mass() << " exceeds massConstraint !!" << std::endl;
    }
    SVfit4tauResult result;
    result.isValidSolution_ = false;
    return result;
  }
  
  std::vector<classic_svFit::MeasuredTauLepton> measuredTauLeptons;
  measuredTauLeptons.push_back(makeMeasuredTauLepton(measuredTau1Higgs1P4, measuredTau1Higgs1Type, measuredHadTau1Higgs1DecayMode));
  measuredTauLeptons.push_back(makeMeasuredTauLepton(measuredTau2Higgs1P4, measuredTau2Higgs1Type, measuredHadTau2Higgs1DecayMode));
  measuredTauLeptons.push_back(makeMeasuredTauLepton(measuredTau1Higgs2P4, measuredTau1Higgs2Type, measuredHadTau1Higgs2DecayMode));
  measuredTauLeptons.push_back(makeMeasuredTauLepton(measuredTau2Higgs2P4, measuredTau2Higgs2Type, measuredHadTau2Higgs2DecayMode));
  
  ClassicSVfit4tau svFitAlgo(intAlgo, verbosity);
  if ( logM > 0. ) {
    svFitAlgo.addLogM_fixed(true, logM);
  } else {
    svFitAlgo.addLogM_fixed(false);
  }
  svFitAlgo.setDiTau1MassConstraint(massConstraint);
  svFitAlgo.setDiTau2MassConstraint(massConstraint);  
  svFitAlgo.integrate(measuredTauLeptons, metPx, metPy, metCov);

  SVfit4tauResult result;
  if ( svFitAlgo.isValidSolution() ) {
    result.dihiggs_visMass_  = (measuredTau1Higgs1P4 + measuredTau2Higgs1P4 + measuredTau1Higgs2P4 + measuredTau2Higgs2P4).mass();
    result.dihiggs_mass_     = svFitAlgo.getMass();
    result.dihiggs_massErr_  = svFitAlgo.getMassErr();
    if ( intAlgo == ClassicSVfit4tau::kAlgoMarkovChain ) {
      classic_svFit::HistogramAdapterDiHiggs* dihiggs = static_cast<classic_svFit::HistogramAdapterDiHiggs*>(svFitAlgo.getHistogramAdapter());
      assert(dihiggs);
      result.dihiggs_pt_     = dihiggs->getPt();
      result.dihiggs_ptErr_  = dihiggs->getPtErr();
      result.dihiggs_eta_    = dihiggs->getEta();
      result.dihiggs_etaErr_ = dihiggs->getEtaErr();
      result.dihiggs_phi_    = dihiggs->getPhi();
      result.dihiggs_phiErr_ = dihiggs->getPhiErr();
      result.ditau1_visMass_ = (measuredTau1Higgs1P4 + measuredTau2Higgs1P4).mass();
      classic_svFit::HistogramAdapterDiTau* ditau1 = dihiggs->ditau1();
      assert(ditau1);
      result.ditau1_mass_    = ditau1->getMass();
      result.ditau1_massErr_ = ditau1->getMassErr();
      result.ditau1_pt_      = ditau1->getPt();
      result.ditau1_ptErr_   = ditau1->getPtErr();
      result.ditau1_eta_     = ditau1->getEta();
      result.ditau1_etaErr_  = ditau1->getEtaErr();
      result.ditau1_phi_     = ditau1->getPhi();
      result.ditau1_phiErr_  = ditau1->getPhiErr();	   
      result.ditau2_visMass_ = (measuredTau1Higgs2P4 + measuredTau2Higgs2P4).mass();
      classic_svFit::HistogramAdapterDiTau* ditau2 = dihiggs->ditau2();
      assert(ditau2);
      result.ditau2_mass_    = ditau2->getMass();
      result.ditau2_massErr_ = ditau2->getMassErr();
      result.ditau2_pt_      = ditau2->getPt();
      result.ditau2_ptErr_   = ditau2->getPtErr();
      result.ditau2_eta_     = ditau2->getEta();
      result.ditau2_etaErr_  = ditau2->getEtaErr();
      result.ditau2_phi_     = ditau2->getPhi();
      result.ditau2_phiErr_  = ditau2->getPhiErr();
      result.probMax_        = svFitAlgo.getProbMax();
    }
    result.Lmax_             = svFitAlgo.getLmax();
    result.isValidSolution_  = true;
  } else {
    result.isValidSolution_  = false;
  }
  return result;
}
