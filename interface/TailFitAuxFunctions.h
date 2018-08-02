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

#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE                                                                                                                                                                                                                              
#include <assert.h>

typedef std::vector<std::string> vstring;


TF1* Exp(double norm = 1.0, double exponent = -0.1, double offset = 0., double xmin = 10., double xmax = 100.);

TF1* Poly3(double par0 = 1.0, double par1 = 1.0, double par2 = 1.0, double xmin = 10., double xmax = 100.);

TF1* ExpErf(double norm = 1.0, double exponent = -0.1, double offset = 0., double width = 1.0, double xmin = 10., double xmax = 100.);

TF1* Gauss(double norm = 1.0, double mean = 0.1, double sigma = 0.1, double xmin = 10., double xmax = 100.);

TF1* Gauss2(double norm = 1.0, double mean0 = 0.1, double sigma0 = 0.1, double mean1 = 0.1, double sigma1 = 0.1, double xmin = 10., double xmax = 100.);

TF1* Gauss3(double norm0 = 1.0, double mean0 = 0.1, double sigma0 = 0.1, double norm1 = 1.0, double mean1 = 0.1, double sigma1 = 0.1, double mean2 = 0.1, double sigma2 = 0.1, double xmin = 10., double xmax = 100.);

TF1* ExpGaus(double norm = 1.0, double exponent = -0.1, double mean = 0.1, double sigma = 0.1, double xmin = 10., double xmax = 100.);

TF1* ExpGaus2(double norm0 = 1.0, double norm1 = 1.0, double exponent = -0.1, double mean0 = 0.1, double sigma0 = 0.1, double mean1 = 0.1, double sigma1 = 0.1, double xmin = 10., double xmax = 100.);

TF1* ErfExpGaus(double norm = 1.0, double exponent = -0.1, double mean0 = 0.1, double sigma0 = 0.1, double mean1 = 0.1, double sigma1 = 0.1, double xmin = 10., double xmax = 100.);

TF1* ErfExpGaus2(double norm0 = 1.0, double norm1 = 1.0, double exponent = -0.1, double mean0 = 0.1, double sigma0 = 0.1, double mean1 = 0.1, double sigma1 = 0.1, double mean2 = 0.1, double sigma2 = 0.1, double xmin = 10., double xmax = 100.);

TF1* Voigt(double norm = 1.0, double sigma = 0.1, double gamma = 0.1, double xmin = 10., double xmax = 100.);

TF1* Gaus2Voigt(double norm0 = 1.0,  double norm1 = 1.0,  double sigma = 0.1, double gamma = 0.1, double mean0 = 0.1, double sigma0 = 0.1, double mean1 = 0.1, double sigma1 = 0.1, double xmin = 10., double xmax = 100.);

TF1* CrystalBall(double norm = 10., double alpha = 1.0, double n = 1.0, double mu = 0.1, double sigma = 1.0, double xmin = 10., double xmax = 100.);

#endif
