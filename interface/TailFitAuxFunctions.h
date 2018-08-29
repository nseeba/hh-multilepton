#ifndef hhAnalysis_tttt_TailFitAuxFunctions_h
#define hhAnalysis_tttt_TailFitAuxFunctions_h

#include <TFile.h>
#include <TH1.h>
#include <TF1.h>
#include <TBenchmark.h>
#include <TMath.h>
#include <TError.h> // gErrorAbortLevel, kError                                                                                                                                                                                                                    
#include <TFitResult.h>
#include "TPRegexp.h"
#include "TDirectory.h"
#include "TList.h"
#include "TKey.h"
#include "TObject.h"
#include "TFormula.h"
#include "TAxis.h"

#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE                                                                                                                                                                                                                           
#include <assert.h>
#include <sstream>

typedef std::vector<std::string> vstring;
typedef std::vector<double> vdouble;

TF1* Exp(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label);

TF1* Poly3(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label);

TF1* ExpErf(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label);

TF1* Gauss(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label);

TF1* Gauss2(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label);

TF1* Gauss3(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label);

TF1* ExpGaus(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label);

TF1* ExpGaus2(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label);

TF1* ErfExpGaus(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label);

TF1* ErfExpGaus2(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label);

TF1* Voigt(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label);

TF1* Gaus2Voigt(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label);

TF1* CrystalBall(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label);

#endif
