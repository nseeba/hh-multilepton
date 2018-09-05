#include "hhAnalysis/multilepton/interface/TailFitAuxFunctions.h"

#include <sstream>
#include <iostream>
#include <locale>
#include <assert.h>



TF1* Exp(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{
  assert((FitParameters.size() == 2) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("Exponential_%s", Label.data());

  // std::string offset;
  // std::ostringstream convert;
  // convert << FitParameters[0]; // first element of FitParameters is the offset which won't be treated as a fit parameter
  // std::string Expression = Form("[0]*TMath::Exp([1]*(x - %s))", offset.data());

  std::string Expression = Form("[0]*[0]*TMath::Exp(-[1]*[1]*(x - %f))", mean);

  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* exp = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);
  exp->SetParameter(0, FitParameters[0]); // norm
  exp->SetParameter(1, FitParameters[1]);   // exponent
  exp->SetParNames("Norm", "Exponent");

  return exp;
}

TF1* Poly1(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{
  assert((FitParameters.size() == 2) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("LegendrePolynomial1_%s", Label.data());

  // std::string offset;
  // std::ostringstream convert;
  // convert << FitParameters[0]; // first element of FitParameters is the offset which won't be treated as a fit parameter    
  // std::string Expression = Form("([0] + ([1]*(x - %s))", offset.data(), offset.data());

  std::string Expression = Form("[0] + ([1]*(x - %f))", mean);

  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* pol1 = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);
  pol1->SetParameter(0, FitParameters[0]); // par0
  pol1->SetParameter(1, FitParameters[1]); // par1
  pol1->SetParNames("Par0", "Par1");
  return pol1;
}


TF1* Poly2(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{
  assert((FitParameters.size() == 3) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("LegendrePolynomial2_%s", Label.data());

  // std::string offset;
  // std::ostringstream convert;
  // convert << FitParameters[0]; // first element of FitParameters is the offset which won't be treated as a fit parameter    
  // std::string Expression = Form("([0] + ([1]*(x - %s)) + (0.5*[2]*((3.0*TMath::Power((x - %s), 2.0)) - 1.0))", offset.data(), offset.data(), offset.data());

  std::string Expression = Form("[0] + ([1]*(x - %f)) + (0.5*[2]*((3.0*TMath::Power((x - %f), 2.0)) - 1.0))", mean, mean);

  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* pol2 = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);
  pol2->SetParameter(0, FitParameters[0]); // par0
  pol2->SetParameter(1, FitParameters[1]); // par1
  pol2->SetParameter(2, FitParameters[2]); // par2
  pol2->SetParNames("Par0", "Par1", "Par2");
  return pol2;
}

TF1* Poly3(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{
  assert((FitParameters.size() == 4) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("LegendrePolynomial3_%s", Label.data());

  // std::string offset;
  // std::ostringstream convert;
  // convert << FitParameters[0]; // first element of FitParameters is the offset which won't be treated as a fit parameter    
  // std::string Expression = Form("([0] + ([1]*(x - %s)) + (0.5*[2]*((3.0*TMath::Power((x - %s), 2.0)) - 1.0)) + (0.5*[3]*((5.0*TMath::Power((x - %s), 3.0)) - (3.0*(x - %s))))", offset.data(), offset.data(), offset.data(), offset.data());

  std::string Expression = Form("[0] + ([1]*(x - %f)) + (0.5*[2]*((3.0*TMath::Power((x - %f), 2.0)) - 1.0)) + (0.5*[3]*((5.0*TMath::Power((x - %f), 3.0)) - (3.0*(x - %f))))", mean, mean, mean, mean);

  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* pol3 = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);

  pol3->SetParameter(0, FitParameters[0]); // par0
  pol3->SetParameter(1, FitParameters[1]); // par1
  pol3->SetParameter(2, FitParameters[2]); // par2
  pol3->SetParameter(3, FitParameters[3]); // par3
  pol3->SetParNames("Par0", "Par1", "Par2", "Par3");

  return pol3;
}


TF1* ExpErf(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{
  assert((FitParameters.size() == 4) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("ExponentialErf_%s", Label.data());

  // std::string offset;
  // std::ostringstream convert;
  // convert << FitParameters[0]; // first element of FitParameters is the offset which won't be treated as a fit parameter     
  // std::string Expression = Form("[0]*TMath::Exp([1]*(x - %s))*0.5*(1 + TMath::Erf(((x - %s) - [2])/[3]))", offset.data(), offset.data());

  std::string Expression = Form("[0]*[0]*TMath::Exp(-[1]*[1]*(x - %f))*0.5*(1 + TMath::Erf(((x - %f) - [2])/[3]))", mean, mean);

  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* experf = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);

  experf->SetParameter(0, FitParameters[0]); // norm  
  experf->SetParameter(1, FitParameters[1]); // exponent  
  experf->SetParameter(2, FitParameters[2]); // mean 
  experf->SetParameter(3, FitParameters[3]); // sigma
  experf->SetParNames("Norm", "Exponent", "Mean", "Sigma");

  return experf;
}


TF1* Gauss(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{
  assert((FitParameters.size() == 3) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("Gaussian_%s", Label.data());

  // std::string offset;
  // std::ostringstream convert;
  // convert << FitParameters[0]; // first element of FitParameters is the offset which won't be treated as a fit parameter                                                                                                                                       
  // std::string Expression = Form("[0]*TMath::Gaus((x - %s),[1],[2])", offset.data());

  std::string Expression = Form("[0]*TMath::Gaus((x - %f),[1],[2])", mean);

  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* gauss = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);

  gauss->SetParameter(0, FitParameters[0]); // norm
  gauss->SetParameter(1, FitParameters[1]); // mean
  gauss->SetParameter(2, FitParameters[2]);  // sigma
  gauss->SetParNames("Norm",  "Mean", "Sigma");

 return gauss;
}

TF1* Gauss2(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{
  assert((FitParameters.size() == 5) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("DoubleGaussian_%s", Label.data());

  // std::string offset;
  // std::ostringstream convert;
  // convert << FitParameters[0]; // first element of FitParameters is the offset which won't be treated as a fit parameter                                                                                                                                        
  // std::string Expression = Form("([0]*TMath::Gaus((x - %s),[1],[2])) + ((1 - [0])*TMath::Gaus((x - %s),[3],[4]))", offset.data(), offset.data());

  std::string Expression = Form("([0]*TMath::Gaus((x - %f),[1],[2])) + ((1 - [0])*TMath::Gaus((x - %f),[3],[4]))", mean, mean);

  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* gauss2 = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);

  gauss2->SetParameter(0, FitParameters[0]); // norm
  gauss2->SetParameter(1, FitParameters[1]); // mean0
  gauss2->SetParameter(2, FitParameters[2]); // sigma0
  gauss2->SetParameter(3, FitParameters[3]);   // mean1
  gauss2->SetParameter(4, FitParameters[4]);   // sigma1
  gauss2->SetParNames("Norm", "Mean0", "Sigma0", "Mean1", "Sigma1");

  return gauss2;
}

TF1* Gauss3(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{
  assert((FitParameters.size() == 8) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("TripleGaussian_%s", Label.data());

  // std::string offset;
  // std::ostringstream convert;
  // convert << FitParameters[0]; // first element of FitParameters is the offset which won't be treated as a fit parameter                                                                                                                                         
  // std::string Expression = Form("([0]*TMath::Gaus((x - %s),[1],[2])) + ([3]*TMath::Gaus((x - %s),[4],[5])) + ((1 - [3] - [0])*TMath::Gaus((x - %s),[6],[7]))", offset.data(), offset.data(), offset.data());

  std::string Expression = Form("([0]*TMath::Gaus((x - %f),[1],[2])) + ([3]*TMath::Gaus((x - %f),[4],[5])) + ((1 - [3] - [0])*TMath::Gaus((x - %f),[6],[7]))", mean, mean, mean);

  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* gauss3 = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);

  gauss3->SetParameter(0, FitParameters[0]); // norm0
  gauss3->SetParameter(1, FitParameters[1]);  // mean0
  gauss3->SetParameter(2, FitParameters[2]);  // sigma0
  gauss3->SetParameter(3, FitParameters[3]);   // norm1
  gauss3->SetParameter(4, FitParameters[4]);   // mean1
  gauss3->SetParameter(5, FitParameters[5]);   // sigma1
  gauss3->SetParameter(6, FitParameters[6]);    // mean2
  gauss3->SetParameter(7, FitParameters[7]);    // sigma2
  gauss3->SetParNames("Norm0", "Mean0", "Sigma0", "Norm1", "Mean1", "Sigma1", "Mean2", "Sigma2");

  return gauss3;
}

TF1* ExpGaus(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{
  assert((FitParameters.size() == 4) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("ExponentialGaussian_%s", Label.data());

  // std::string offset;
  // std::ostringstream convert;
  // convert << FitParameters[0]; // first element of FitParameters is the offset which won't be treated as a fit parameter                                                                          
  // std::string Expression = Form("([0]*TMath::Exp([1]*(x - %s))) + ((1 - [0])*TMath::Gaus((x - %s),[2],[3]))", offset.data(), offset.data());

  std::string Expression = Form("([0]*[0]*TMath::Exp(-[1]*[1]*(x - %f))) + ((1 - [0])*TMath::Gaus((x - %f),[2],[3]))", mean, mean);

  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* expgaus = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);

  expgaus->SetParameter(0, FitParameters[0]); // norm
  expgaus->SetParameter(1, FitParameters[1]); // exponent
  expgaus->SetParameter(2, FitParameters[2]);     // mean
  expgaus->SetParameter(3, FitParameters[3]);   // sigma
  expgaus->SetParNames("Norm", "Exponent", "Mean", "Sigma");

  return expgaus;
}


TF1* ExpGaus2(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{
  assert((FitParameters.size() == 7) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("DoubleExponentialGaussian_%s", Label.data());

  // std::string offset;
  // std::ostringstream convert;
  // convert << FitParameters[0]; // first element of FitParameters is the offset which won't be treated as a fit parameter                     
  // std::string Expression = Form("([0]*TMath::Exp([2]*(x - %s))) + ([1]*TMath::Gaus((x - %s),[3],[4])) + ((1 - [1] - [0])*TMath::Gaus((x - %s),[5],[6]))", offset.data(), offset.data(), offset.data());                                                         

  std::string Expression = Form("([0]*[0]*TMath::Exp(-[2]*[2]*(x - %f))) + ([1]*TMath::Gaus((x - %f),[3],[4])) + ((1 - [1] - [0])*TMath::Gaus((x - %f),[5],[6]))", mean, mean, mean);    
                                                                    
  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* expgaus2 = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);

  expgaus2->SetParameter(0, FitParameters[0]); // norm0
  expgaus2->SetParameter(1, FitParameters[1]); // norm1
  expgaus2->SetParameter(2, FitParameters[2]); // exponent
  expgaus2->SetParameter(3, FitParameters[3]);    // mean0
  expgaus2->SetParameter(4, FitParameters[4]);   // sigma0
  expgaus2->SetParameter(5, FitParameters[5]);    // mean1
  expgaus2->SetParameter(6, FitParameters[6]);   // sigma1
  expgaus2->SetParNames("Norm0", "Norm1", "Exponent", "Mean0", "Sigma0", "Mean1", "Sigma1");

  return expgaus2;
}


TF1* ErfExpGaus(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{
  assert((FitParameters.size() == 6) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("ErfExponentialGaussian_%s", Label.data());

  // std::string offset;
  // std::ostringstream convert;
  // convert << FitParameters[0]; // first element of FitParameters is the offset which won't be treated as a fit parameter                     
  // std::string Expression = Form("([0]*TMath::Exp([1]*(x - %s))*0.5*(1 + TMath::Erf(((x - %s) - [2])/[3]))) + ((1 - [0])*TMath::Gaus((x - %s),[4],[5]))", offset.data(), offset.data(), offset.data());

  std::string Expression = Form("([0]*[0]*TMath::Exp(-[1]*[1]*(x - %f))*0.5*(1 + TMath::Erf(((x - %f) - [2])/[3]))) + ((1 - [0])*TMath::Gaus((x - %f),[4],[5]))", mean, mean, mean);

  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* erfexpgaus = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);

  erfexpgaus->SetParameter(0, FitParameters[0]); // norm0
  erfexpgaus->SetParameter(1, FitParameters[1]); // exponent
  erfexpgaus->SetParameter(2, FitParameters[2]); // mean0
  erfexpgaus->SetParameter(3, FitParameters[3]); // sigma0
  erfexpgaus->SetParameter(4, FitParameters[4]);  // mean1
  erfexpgaus->SetParameter(5, FitParameters[5]); // sigma1
  erfexpgaus->SetParNames("Norm0", "Exponent", "Mean0", "Sigma0", "Mean1", "Sigma1");

  return erfexpgaus;
}


TF1* ErfExpGaus2(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{
  assert((FitParameters.size() == 9) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("DoubleErfExponentialGaussian_%s", Label.data());

  // std::string offset;
  // std::ostringstream convert;
  // convert << FitParameters[0]; // first element of FitParameters is the offset which won't be treated as a fit parameter                     
  // std::string Expression = Form("([0]*TMath::Exp([2]*(x - %s))*(1 + TMath::Erf(((x - %s) - [3])/[4]))/2.0) + ([1]*TMath::Gaus((x - %s),[5],[6])) + ((1 - [1] - [0])*TMath::Gaus((x - %s),[7],[8]))", offset.data(), offset.data(), offset.data(), offset.data());
                                                                                                                                 
  std::string Expression = Form("([0]*[0]*TMath::Exp(-[2]*[2]*(x - %f))*(1 + TMath::Erf(((x - %f) - [3])/[4]))/2.0) + ([1]*TMath::Gaus((x - %f),[5],[6])) + ((1 - [1] - [0])*TMath::Gaus((x - %f),[7],[8]))", mean, mean, mean, mean);

  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* erfexpgaus2 = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);

  erfexpgaus2->SetParameter(0, FitParameters[0]); // norm0
  erfexpgaus2->SetParameter(1, FitParameters[1]); // norm1
  erfexpgaus2->SetParameter(2, FitParameters[2]); // exponent
  erfexpgaus2->SetParameter(3, FitParameters[3]);    // mean0
  erfexpgaus2->SetParameter(4, FitParameters[4]);   // sigma0
  erfexpgaus2->SetParameter(5, FitParameters[5]);    // mean1
  erfexpgaus2->SetParameter(6, FitParameters[6]);   // sigma1
  erfexpgaus2->SetParameter(7, FitParameters[7]);    // mean2
  erfexpgaus2->SetParameter(8, FitParameters[8]);   // sigma2
  erfexpgaus2->SetParNames("Norm0", "Norm1",  "Exponent", "Mean0", "Sigma0", "Mean1", "Sigma1", "Mean2", "Sigma2");

  return erfexpgaus2;
}





TF1* Voigt(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{ // Source -> https://root.cern.ch/doc/v608/namespaceTMath.html#a6688575b20a534a694f0b0ba89087daa
  assert((FitParameters.size() == 3) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("Voigt_%s", Label.data());

  // std::string offset;
  // std::ostringstream convert;
  // convert << FitParameters[0]; // first element of FitParameters is the offset which won't be treated as a fit parameter                     
  // std::string Expression = Form("[0]*TMath::Voigt((x - %s),[1],[2])", offset.data());

  std::string Expression = Form("[0]*TMath::Voigt((x - %f),[1],[2])", mean);

  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* voigt = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);

  voigt->SetParameter(0, FitParameters[0]); // norm
  voigt->SetParameter(1, FitParameters[1]); // sigma
  voigt->SetParameter(2, FitParameters[2]); // gamma
  voigt->SetParNames("norm", "sigma", "gamma");

  return voigt;
}


TF1* Gaus2Voigt(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{ 
  assert((FitParameters.size() == 8) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("DoubleGaussianVoigt_%s", Label.data());


  std::string Expression = Form("([0]*TMath::Voigt((x - %f),[2],[3])) + ([1]*TMath::Gaus((x - %f),[4],[5])) + ((1 - [1] - [0])*TMath::Gaus((x - %f),[6],[7]))", mean, mean, mean);

  TFormula* g1 = new TFormula("g1", Expression.data());
  TF1* gaus2voigt = new TF1(funcName.data(), "g1", FitRange[0], FitRange[1]);

  gaus2voigt->SetParameter(0, FitParameters[0]); // norm0
  gaus2voigt->SetParameter(1, FitParameters[1]); // norm1
  gaus2voigt->SetParameter(2, FitParameters[2]); // sigma
  gaus2voigt->SetParameter(3, FitParameters[3]); // gamma
  gaus2voigt->SetParameter(4, FitParameters[4]); // mean0
  gaus2voigt->SetParameter(5, FitParameters[5]); // sigma0
  gaus2voigt->SetParameter(6, FitParameters[6]);  // mean1
  gaus2voigt->SetParameter(7, FitParameters[7]); // sigma1
  gaus2voigt->SetParNames("norm0", "norm1", "sigma", "gamma", "mean0", "sigma0", "mean1", "sigma1");

  return gaus2voigt;
}



double CrystalBallFunc(double* x, double* par){ // http://en.wikipedia.org/wiki/Crystal_Ball_function 
  double xcur = x[0] - par[0];
  double alpha = par[1];
  double n = par[2];
  double mu = par[3];
  double sigma = par[4];
  double N = par[5];
  double A = 0.; 
  double B = 0.;

  if (alpha < 0){
    A = TMath::Power((n/(-1.0 * alpha)), n) * TMath::Exp(-0.5*alpha*alpha);
    B = (n/((-1.0)*alpha)) + alpha;
  } else {
    A = TMath::Power((n/alpha), n) * TMath::Exp(-0.5*alpha*alpha); 
    B = (n/alpha) - alpha;
  }

  double f;
  if ((xcur - mu)/sigma > (-1)*alpha){
    f = N * TMath::Exp(-0.5*(xcur - mu)*(xcur - mu)/(sigma*sigma));
  }else{
    f = N * A * TMath::Power((B - (xcur-mu)/sigma), ((-1.0)*n));
  }
  return f; 
}




TF1* CrystalBall(const vdouble& FitParameters, const vdouble& FitRange, const TH1* histo, const std::string Label)
{
  assert((FitParameters.size() == 5) && (FitRange.size() == 2));

  TH1* Histo = const_cast<TH1*>(histo);
  Histo->GetXaxis()->SetRangeUser(FitRange[0], FitRange[1]);
  double mean = Histo->GetMean();
  std::cout<< "Function will be centered at " << mean << std::endl;
  std::string funcName = Form("CrystalBall_%s", Label.data());

  TF1* CB = new TF1(funcName.data(), CrystalBallFunc, FitRange[0], FitRange[1], 6);

  CB->FixParameter(0, mean);
  CB->SetParameter(1, FitParameters[0]); // alpha
  CB->SetParameter(2, FitParameters[1]);     // n
  CB->SetParameter(3, FitParameters[2]);    // mu
  CB->SetParameter(4, FitParameters[3]); // sigma
  CB->SetParameter(5, FitParameters[4]);  // N
  CB->SetParNames("Mean" ,"alpha", "n", "mu", "sigma", "N");

  return CB; 
}

