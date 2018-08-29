#ifndef hhAnalysis_multilepton_GenMEtSmearer_h
#define hhAnalysis_multilepton_GenMEtSmearer_h

/** \class GenMEtSmearer
 *
 * Produce reco::GenMET objects corresponding to vectorial sum of the momenta
 * of all neutrinos produced in tau decays in the event
 * 
 * \author Christian Veelken, Tallinn
 *
 */

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include <TRandom3.h>

class GenMEtSmearer
{
 public:
  explicit GenMEtSmearer(const edm::ParameterSet&);
  ~GenMEtSmearer();
  
  std::pair<double, double> operator()(double metPx, double metPy) const;

 private:
  double sigmaX_;
  double sigmaY_;

  mutable TRandom3 rnd_;
};

#endif
