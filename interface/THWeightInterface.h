#ifndef hhAnalysis_multilepton_THWeightInterface_h
#define hhAnalysis_multilepton_THWeightInterface_h

#include <Python.h> // PyObject
#include <vector> // std::vector<>
#include <string> // std::string
#include <map> // std::map<,>

#include <Math/LorentzVector.h>
#include <Math/PtEtaPhiM4D.h>
typedef ROOT::Math::LorentzVector<ROOT::Math::PtEtaPhiM4D<double> > LorentzVector;
#include <TLorentzVector.h> // TLorentzVector

double comp_cosThetaS(const LorentzVector& hadTauP4_lead, const LorentzVector& hadTauP4_sublead);

class THWeightInterface
{
public:
  THWeightInterface(
              double & CX, int & BM, double & Norm,
              const double & kl,
              const double & kt,
              const double & c2,
              const double & cg,
              const double & c2g,
              std::vector<double> & NormBM
             );
  ~THWeightInterface();

  /**
   * @brief Calculates MVA output.
   * @param mvaInputs Values of MVA input variables (stored in std::map with key = MVA input variable name)
   * @return          MVA output
   */
  double
  operator()(
    const double & mhh_gen,
    const double & costSgen_gen,
    //
    const double & kl,
    const double & kt,
    const double & c2,
    const double & cg,
    const double & c2g,
    //
    const double & normalization,
    std::vector<double> & WeightBM
  ) const;

private:
  //std::string mvaFileName_;

  //std::vector<std::string> mvaInputVariables_; // list of MVA input variables
  PyObject* modeldata_;
  PyObject* moduleMainString_;
  PyObject* moduleMain_;
  PyObject* cms_base;

  double klJHEP[13]  = {1.0,  7.5,  1.0,  1.0,  -3.5, 1.0, 2.4, 5.0, 15.0, 1.0, 10.0, 2.4, 15.0};
  double ktJHEP[13]  = {1.0,  1.0,  1.0,  1.0,  1.5,  1.0, 1.0, 1.0, 1.0,  1.0, 1.5,  1.0, 1.0};
  double c2JHEP[13]  = {0.0,  -1.0, 0.5, -1.5, -3.0,  0.0, 0.0, 0.0, 0.0,  1.0, -1.0, 0.0, 1.0};
  double cgJHEP[13]  = {0.0,  0.0, -0.8,  0.0, 0.0,   0.8, 0.2, 0.2, -1.0, -0.6, 0.0, 1.0, 0.0};
  double c2gJHEP[13] = {0.0, 0.0, 0.6, -0.8, 0.0, -1.0, -0.2,-0.2,  1.0,  0.6, 0.0, -1.0, 0.0};

};

#endif // THWeightInterface_h
