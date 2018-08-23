#ifndef hhAnalysis_tttt_mySVfit4tauAuxFunctions_h
#define hhAnalysis_tttt_mySVfit4tauAuxFunctions_h

#include "tthAnalysis/HiggsToTauTau/interface/GenParticle.h" // GenParticle
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt

#include "TauAnalysis/ClassicSVfit/interface/MeasuredTauLepton.h" // classic_svFit::MeasuredTauLepton
#include "TauAnalysis/ClassicSVfit4tau/interface/ClassicSVfit4tau.h" // ClassicSVfit4tau::kAlgoMarkovChain

#include <TRandom.h> // TRandom

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
    , dihiggs_pt_(-1.)
    , dihiggs_ptErr_(-1.)
    , dihiggs_eta_(-1.)
    , dihiggs_etaErr_(-1.)
    , dihiggs_phi_(-1.)
    , dihiggs_phiErr_(-1.)    
    , ditau1_visMass_(-1.)
    , ditau1_mass_(-1.)
    , ditau1_massErr_(-1.)
    , ditau1_pt_(-1.)
    , ditau1_ptErr_(-1.)
    , ditau1_eta_(-1.)
    , ditau1_etaErr_(-1.)
    , ditau1_phi_(-1.)
    , ditau1_phiErr_(-1.)
    , ditau2_visMass_(-1.)
    , ditau2_mass_(-1.)
    , ditau2_massErr_(-1.)
    , ditau2_pt_(-1.)
    , ditau2_ptErr_(-1.)
    , ditau2_eta_(-1.)
    , ditau2_etaErr_(-1.)
    , ditau2_phi_(-1.)
    , ditau2_phiErr_(-1.)
    , probMax_(-1.)
    , Lmax_(-1.)
    , isValidSolution_(false)
  {}
  SVfit4tauResult(const SVfit4tauResult& result)
    : dihiggs_visMass_(result.dihiggs_visMass_)
    , dihiggs_mass_(result.dihiggs_mass_)
    , dihiggs_massErr_(result.dihiggs_massErr_)
    , dihiggs_pt_(result.dihiggs_pt_)
    , dihiggs_ptErr_(result.dihiggs_ptErr_)
    , dihiggs_eta_(result.dihiggs_eta_)
    , dihiggs_etaErr_(result.dihiggs_etaErr_)
    , dihiggs_phi_(result.dihiggs_phi_)
    , dihiggs_phiErr_(result.dihiggs_phiErr_)    
    , ditau1_visMass_(result.ditau1_visMass_)
    , ditau1_mass_(result.ditau1_mass_)
    , ditau1_massErr_(result.ditau1_massErr_)
    , ditau1_pt_(result.ditau1_pt_)
    , ditau1_ptErr_(result.ditau1_ptErr_)
    , ditau1_eta_(result.ditau1_eta_)
    , ditau1_etaErr_(result.ditau1_etaErr_)
    , ditau1_phi_(result.ditau1_phi_)
    , ditau1_phiErr_(result.ditau1_phiErr_)
    , ditau2_visMass_(result.ditau2_visMass_)
    , ditau2_mass_(result.ditau2_mass_)
    , ditau2_massErr_(result.ditau2_massErr_)
    , ditau2_pt_(result.ditau2_pt_)
    , ditau2_ptErr_(result.ditau2_ptErr_)
    , ditau2_eta_(result.ditau2_eta_)
    , ditau2_etaErr_(result.ditau2_etaErr_)
    , ditau2_phi_(result.ditau2_phi_)
    , ditau2_phiErr_(result.ditau2_phiErr_)
    , probMax_(result.probMax_)
    , Lmax_(result.Lmax_)
    , isValidSolution_(result.isValidSolution_)
  {}
  ~SVfit4tauResult() {}
  double dihiggs_visMass_;
  double dihiggs_mass_;
  double dihiggs_massErr_;
  double dihiggs_pt_;
  double dihiggs_ptErr_;
  double dihiggs_eta_;
  double dihiggs_etaErr_;
  double dihiggs_phi_;
  double dihiggs_phiErr_;
  double ditau1_visMass_;
  double ditau1_mass_;
  double ditau1_massErr_;
  double ditau1_pt_;
  double ditau1_ptErr_;
  double ditau1_eta_;
  double ditau1_etaErr_;
  double ditau1_phi_;
  double ditau1_phiErr_;
  double ditau2_visMass_;
  double ditau2_mass_;
  double ditau2_massErr_;
  double ditau2_pt_;
  double ditau2_ptErr_;
  double ditau2_eta_;
  double ditau2_etaErr_;
  double ditau2_phi_;
  double ditau2_phiErr_;
  double probMax_;
  double Lmax_;
  bool isValidSolution_;
};

bool
isHigherProbMax(const SVfit4tauResult& result1,
		const SVfit4tauResult& result2);

bool
isHigherLmax(const SVfit4tauResult& result1,
	     const SVfit4tauResult& result2);

bool
isLowerMassErr(const SVfit4tauResult& result1,
	       const SVfit4tauResult& result2);

// reconstruct di-Higgs system for each possible pairing of visible tau decay products
std::vector<SVfit4tauResult>
compSVfit4tau(const GenParticle& measuredTau1, 
	      const GenParticle& measuredTau2, 
	      const GenParticle& measuredTau3, 
	      const GenParticle& measuredTau4, 
	      const RecoMEt& met,
	      const std::string& chargeSumSelection_string, TRandom& rnd,
	      int intAlgo = ClassicSVfit4tau::kAlgoMarkovChain, // CV: default is to use Markov-Chain integration
	      double massConstraint = -1.,                      // CV: default is not to apply mass constraint
	      double logM = 0.,                                 // CV: default is not to apply log(M) term
	      int verbosity = 1); 

// reconstruct di-Higgs system for one particular (given) pairing of visible tau decay products
SVfit4tauResult
compSVfit4tau(const Particle::LorentzVector& measuredTau1Higgs1P4, int measuredTau1Higgs1Type, int measuredHadTau1Higgs1DecayMode,
	      const Particle::LorentzVector& measuredTau2Higgs1P4, int measuredTau2Higgs1Type, int measuredHadTau2Higgs1DecayMode,
	      const Particle::LorentzVector& measuredTau1Higgs2P4, int measuredTau1Higgs2Type, int measuredHadTau1Higgs2DecayMode,
	      const Particle::LorentzVector& measuredTau2Higgs2P4, int measuredTau2Higgs2Type, int measuredHadTau2Higgs2DecayMode,
	      double metPx, double metPy, const TMatrixD& metCov,
	      int intAlgo = ClassicSVfit4tau::kAlgoMarkovChain, // CV: default is to use Markov-Chain integration
	      double massConstraint = -1.,                      // CV: default is not to apply mass constraint
	      double logM = 0.,                                 // CV: default is not to apply log(M) term
	      int verbosity = 1); 

#endif
