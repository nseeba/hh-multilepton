#ifndef GENHiggs_H
#define GENHiggs_H

#include "tthAnalysis/HiggsToTauTau/interface/GenParticle.h" // GenParticle

class GenHiggs
  : public GenParticle
{
public:
  GenHiggs() = default;
  GenHiggs(Double_t pt,
         Double_t eta,
         Double_t phi,
         Double_t mass);

  GenHiggs(Double_t pt,
         Double_t eta,
         Double_t phi,
         Double_t mass,
         Int_t pdgId);

  virtual ~GenHiggs() {}
};

std::ostream &
operator<<(std::ostream & stream,
           const GenHiggs & genHiggs);

#endif // GENHiggs_H
