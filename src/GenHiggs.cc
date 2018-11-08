#include "hhAnalysis/multilepton/interface/GenHiggs.h" // GenHiggs, GenParticle

GenHiggs::GenHiggs(Double_t pt,
               Double_t eta,
               Double_t phi,
               Double_t mass)
  : GenHiggs(pt, eta, phi, mass, 0)
{}

GenHiggs::GenHiggs(Double_t pt,
               Double_t eta,
               Double_t phi,
               Double_t mass,
               Int_t pdgId)
  : GenParticle(pt, eta, phi, mass, pdgId, 0)
{}

std::ostream &
operator<<(std::ostream & stream,
           const GenHiggs & genHiggs)
{
  stream << static_cast<const GenParticle &>(genHiggs);
  return stream;
}
