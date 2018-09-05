
#include <TFile.h>
#include <TH1.h>
#include <TH2.h>
#include <TAxis.h>
#include <TMath.h>
#include <TROOT.h>
#include <TStyle.h>

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <iomanip>
#include <assert.h>

TH2* loadHistogram(TFile* inputFile, const std::string& directoryName, const std::string& histogramName)
{
  std::string histogramName_full = directoryName;
  if ( histogramName_full.back() != '/' ) histogramName_full.append("/");
  histogramName_full.append(histogramName);
  TH2* histogram = dynamic_cast<TH2*>(inputFile->Get(histogramName_full.data()));
  if ( !histogram ) {
    std::cerr << "Failed to load histogram = " << histogramName_full << " from file = " << inputFile->GetName() << " !!" << std::endl;
    assert(0);
    return 0;
  }
  if ( !histogram->GetSumw2N() ) histogram->Sumw2();
  return histogram;
}

double compDisambiguationScore(const TH2* histogram, double& scoreLow, double& scoreHigh)
{
  const TAxis* xAxis = histogram->GetXaxis();
  int numBinsX = xAxis->GetNbins();
  const TAxis* yAxis = histogram->GetYaxis();
  int numBinsY = yAxis->GetNbins();

  double score = 0.;
  double sum = 0.;
  for ( int idxBinX = 0; idxBinX <= (numBinsX + 1); ++idxBinX ) {
    for ( int idxBinY = 0; idxBinY <= (numBinsY + 1); ++idxBinY ) {
      double binContent = histogram->GetBinContent(idxBinX, idxBinY);
      if ( idxBinX > idxBinY ) {
	score     += binContent;
	scoreLow  += binContent;
	scoreHigh += binContent;
      } else if ( idxBinX == idxBinY ) {
	score     += 0.5*binContent;
	scoreHigh += binContent;
      } 
      sum += binContent;
    }
  }

  if ( sum > 0. ) {
    score     /= sum;
    scoreLow  /= sum;
    scoreHigh /= sum;
  }

  if ( score < 0.5 ) {
    score     = 1. - score;
    scoreLow  = 1. - scoreHigh;
    scoreHigh = 1. - scoreLow;
  }

  return score;
}

void compSVfit4tauDisambiguation()
{
  gROOT->SetBatch(true);

  TH1::AddDirectory(false);

  std::vector<int> massPoints;
  massPoints.push_back(300);
  massPoints.push_back(500);
  massPoints.push_back(800);
    
  std::string inputFilePath = "/hdfs/local/veelken/hhAnalysis/2016/2018Aug24v3_SVfit4tau/histograms/SVfit4tau/gen_smeared/";
  std::map<int, std::string> inputFileNames; // key = massPoint
  inputFileNames[300] = "x_to_hh_300/x_to_hh_300_gen_smeared_central_1.root";
  inputFileNames[500] = "x_to_hh_500/x_to_hh_500_gen_smeared_central_1.root";
  inputFileNames[800] = "x_to_hh_800/x_to_hh_800_gen_smeared_central_1.root";

  std::vector<std::string> directories;
  directories.push_back("SVfit4tau_2lepton_2tau/gen_smeared/svFit4tauDisambiguation_wMassContraint_logM0p0_MarkovChain");
  directories.push_back("SVfit4tau_2lepton_2tau/gen_smeared/svFit4tauDisambiguation_wMassContraint_logM0p0_VAMP");
  
  std::vector<std::string> histogramNames;
  histogramNames.push_back("dihiggsMass");
  histogramNames.push_back("dihiggsMassErr");
  histogramNames.push_back("dihiggsPt");
  histogramNames.push_back("logLmax");
  histogramNames.push_back("avDeltaPhi");
  histogramNames.push_back("avDeltaEta");
  histogramNames.push_back("avDeltaR");
  histogramNames.push_back("avDiTauVisPt");
  histogramNames.push_back("avDiTauPt");

  for ( std::vector<int>::const_iterator massPoint = massPoints.begin();
	massPoint != massPoints.end(); ++massPoint ) {
    std::string inputFileName_full = inputFilePath;
    if ( inputFileName_full.back() != '/' ) inputFileName_full.append("/");
    inputFileName_full.append(inputFileNames[*massPoint]);
    TFile* inputFile = new TFile(inputFileName_full.data());
    if ( !inputFile ) {
      std::cerr << "Failed to open input file = " << inputFileName_full << " !!" << std::endl;
      assert(0);
    }
    inputFile->ls();

    for ( std::vector<std::string>::const_iterator directory = directories.begin();
	  directory != directories.end(); ++directory ) {
      for ( std::vector<std::string>::const_iterator histogramName = histogramNames.begin();
	    histogramName != histogramNames.end(); ++histogramName ) {
	TH2* histogram = loadHistogram(
          inputFile, 
	  Form("%s/signal_radion_%i", directory->data(), *massPoint), 
	  *histogramName);
	double scoreLow, scoreHigh;
	double score = compDisambiguationScore(histogram, scoreLow, scoreHigh);
	std::cout << "massPoint = " << (*massPoint) << ", directory = '" << (*directory) << "', histogram = '" << (*histogramName) << "':" 
		  << " score = " << score << " (low = " << scoreLow << ", high = " << scoreHigh << ")" << std::endl;
      }
    }

    delete inputFile;
  }
}
