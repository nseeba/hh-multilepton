#include "hhAnalysis/tttt/interface/TailFitAuxFunctions.h"



TF1* Exp(double norm, double exponent, double offset, double xmin, double xmax)
{
  TF1* exp = new TF1("Exp", "[0]*TMath::Exp([1]*(x - [2]))", xmin, xmax);

  exp->SetParameter(0, norm);
  exp->SetParameter(1, exponent);
  exp->SetParameter(2, offset);

  return exp;
}

TF1* Poly3(double par0, double par1, double par2, double xmin, double xmax)
{
  TF1* pol3 = new TF1("pol3", "([0]*x) + ([1]*TMath::Power(x, 2.0)) + ([2]*TMath::Power(x, 3.0))", xmin, xmax);

  pol3->SetParameter(0, par0);
  pol3->SetParameter(1, par1);
  pol3->SetParameter(2, par2);

  return pol3;
}


TF1* ExpErf(double norm, double exponent, double offset, double width, double xmin, double xmax)
{
  TF1* experf = new TF1("ExpErf", "[0]*TMath::Exp([1]*x)*(1 + TMath::Erf((x - [2])/[3]))/2.0", xmin, xmax);

  experf->SetParameter(0, norm);
  experf->SetParameter(1, exponent);
  experf->SetParameter(2, offset);
  experf->SetParameter(3, width);

  return experf;
}


TF1* Gauss(double norm, double mean, double sigma, double xmin, double xmax)
{
 TF1* gauss = new TF1("Gauss", "[0]*TMath::Gaus(x,[1],[2])", xmin, xmax);

 gauss->SetParameter(0, norm);
 gauss->SetParameter(1, mean);
 gauss->SetParameter(2, sigma);

 return gauss;
}

TF1* Gauss2(double norm, double mean0, double sigma0, double mean1, double sigma1, 
            double xmin, double xmax)
{
 TF1* gauss2 = new TF1("Gauss2", "([0]*TMath::Gaus(x,[1],[2])) + ((1 - [0])*TMath::Gaus(x,[3],[4]))", xmin, xmax);

 gauss2->SetParameter(0, norm);
 gauss2->SetParameter(1, mean0);
 gauss2->SetParameter(2, sigma0);
 gauss2->SetParameter(3, mean1);
 gauss2->SetParameter(4, sigma1);

 return gauss2;
}

TF1* Gauss3(double norm0, double mean0, double sigma0, 
	    double norm1, double mean1, double sigma1, 
            double mean2, double sigma2, double xmin, double xmax)
{
 TF1* gauss3 = new TF1("Gauss3", "([0]*TMath::Gaus(x,[1],[2])) + ([3]*TMath::Gaus(x,[4],[5])) + ((1 - [3] - [0])*TMath::Gaus(x,[6],[7])) ", xmin, xmax);

 gauss3->SetParameter(0, norm0);
 gauss3->SetParameter(1, mean0);
 gauss3->SetParameter(2, sigma0);
 gauss3->SetParameter(3, norm1);
 gauss3->SetParameter(4, mean1);
 gauss3->SetParameter(5, sigma1);
 gauss3->SetParameter(6, mean2);
 gauss3->SetParameter(7, sigma2);

 return gauss3;
}

TF1* ExpGaus(double norm, double exponent, double mean, double sigma, double xmin, double xmax)
{
  TF1* expgaus = new TF1("ExpGaus", "([0]*TMath::Exp([1]*x)) + ((1 - [0])*TMath::Gaus(x,[2],[3]))", xmin, xmax);

  expgaus->SetParameter(0, norm);
  expgaus->SetParameter(1, exponent);
  expgaus->SetParameter(2, mean);
  expgaus->SetParameter(3, sigma);

  return expgaus;
}


TF1* ExpGaus2(double norm0, double norm1, double exponent, double mean0, double sigma0, double mean1, double sigma1, double xmin, double xmax)
{
  TF1* expgaus2 = new TF1("ExpGaus2", "([0]*TMath::Exp([2]*x)) + ([1]*TMath::Gaus(x,[3],[4])) + ((1 - [1] - [0])*TMath::Gaus(x,[5],[6]))", xmin, xmax);

  expgaus2->SetParameter(0, norm0);
  expgaus2->SetParameter(1, norm1);
  expgaus2->SetParameter(2, exponent);
  expgaus2->SetParameter(3, mean0);
  expgaus2->SetParameter(4, sigma0);
  expgaus2->SetParameter(5, mean1);
  expgaus2->SetParameter(6, sigma1);

  return expgaus2;
}

TF1* ErfExpGaus(double norm, double exponent, double mean0, double sigma0, double mean1, double sigma1, double xmin, double xmax)
{
  TF1* erfexpgaus = new TF1("ErfExpGaus", "([0]*TMath::Exp([1]*x)*(1 + TMath::Erf((x - [2])/[3]))/2.0) + ((1 - [0])*TMath::Gaus(x,[4],[5]))", xmin, xmax);

  erfexpgaus->SetParameter(0, norm);
  erfexpgaus->SetParameter(1, exponent);
  erfexpgaus->SetParameter(2, mean0);
  erfexpgaus->SetParameter(3, sigma0);
  erfexpgaus->SetParameter(4, mean1);
  erfexpgaus->SetParameter(5, sigma1);

  return erfexpgaus;
}

TF1* ErfExpGaus2(double norm0, double norm1, double exponent, double mean0, double sigma0, double mean1, double sigma1, double mean2, double sigma2, double xmin, double xmax)
{
  TF1* erfexpgaus2 = new TF1("ErfExpGaus2", "([0]*TMath::Exp([2]*x)*(1 + TMath::Erf((x - [3])/[4]))/2.0) + ([1]*TMath::Gaus(x,[5],[6])) + ((1 - [1] - [0])*TMath::Gaus(x,[7],[8]))", xmin, xmax);

  erfexpgaus2->SetParameter(0, norm0);
  erfexpgaus2->SetParameter(1, norm1);
  erfexpgaus2->SetParameter(2, exponent);
  erfexpgaus2->SetParameter(3, mean0);
  erfexpgaus2->SetParameter(4, sigma0);
  erfexpgaus2->SetParameter(5, mean1);
  erfexpgaus2->SetParameter(6, sigma1);
  erfexpgaus2->SetParameter(7, mean2);
  erfexpgaus2->SetParameter(8, sigma2);

  return erfexpgaus2;
}





TF1* Voigt(double norm, double sigma, double gamma, double xmin, double xmax)
{
  TF1* voigt = new TF1("Voigt", "[0]*TMath::Voigt(x,[1],[2])", xmin, xmax);

  voigt->SetParameter(0, norm);
  voigt->SetParameter(1, sigma);
  voigt->SetParameter(2, gamma);

  return voigt;
}


TF1* Gaus2Voigt(double norm0,  double norm1,  double sigma, double gamma, double mean0, double sigma0, double mean1, double sigma1, double xmin, double xmax)
{
  TF1* gaus2voigt = new TF1("Voigt", "([0]*TMath::Voigt(x,[2],[3])) + ([1]*TMath::Gaus(x,[4],[5])) + ((1 - [1] - [0])*TMath::Gaus(x,[6],[7]))", xmin, xmax);

  gaus2voigt->SetParameter(0, norm0);
  gaus2voigt->SetParameter(1, norm1);
  gaus2voigt->SetParameter(2, sigma);
  gaus2voigt->SetParameter(3, gamma);
  gaus2voigt->SetParameter(4, mean0);
  gaus2voigt->SetParameter(5, sigma0);
  gaus2voigt->SetParameter(6, mean1);
  gaus2voigt->SetParameter(7, sigma1);

  return gaus2voigt;
}

double CrystalBallFunc(double* x, double* par){ // http://en.wikipedia.org/wiki/Crystal_Ball_function 
  double xcur = x[0];
  double alpha = par[0];
  double n = par[1];
  double mu = par[2];
  double sigma = par[3];
  double N = par[4];
  TF1* exp = new TF1("exp","TMath::Exp(x)",1.0e-20,1.0e20); 
  double A = 0.; 
  double B = 0.;

  if (alpha < 0){
    A = TMath::Power((n/(-1.0 * alpha)), n) * exp->Eval((-1.0) * alpha * alpha/2);
    B = (n/((-1.0)*alpha)) + alpha;
  } else {
    A = TMath::Power((n/alpha), n) * exp->Eval((-1.0)*alpha*alpha/2); 
    B = (n/alpha) - alpha;
  }

  double f;
  if ((xcur - mu)/sigma > (-1)*alpha){
    f = N * exp->Eval((-1.0)*(xcur - mu)*(xcur - mu)/(2*sigma*sigma));
  }else{
    f = N * A * TMath::Power((B - (xcur-mu)/sigma), ((-1.0)*n));
  delete exp;
  }
  return f; 
}




TF1* CrystalBall(double norm, double alpha, double n, double mu, double sigma, double xmin, double xmax)
{

  TF1* CB = new TF1("CrystalBall", CrystalBallFunc, xmin, xmax);
  CB->SetParameter(0, alpha);
  CB->SetParameter(1, n);
  CB->SetParameter(2, mu);
  CB->SetParameter(3, sigma);
  CB->SetParameter(4, norm);

  return CB; 

}
