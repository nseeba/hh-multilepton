
#include <TFile.h>
#include <TString.h>
#include <TH1.h>
#include <TMath.h>
#include <TROOT.h>
#include <TStyle.h>

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <iomanip>
#include <assert.h>

TH1* loadHistogram(TFile* inputFile, const std::string& histogramName)
{
  TH1* histogram = dynamic_cast<TH1*>(inputFile->Get(histogramName.data()));
  if ( !histogram ) {
    //std::cerr << "Failed to load histogram = " << histogramName << " from file = " << inputFile->GetName() << " !!" << std::endl;
    //assert(0);
    return 0;
  }
  if ( !histogram->GetSumw2N() ) histogram->Sumw2();
  return histogram;
}

double
compIntegral(const TH1 * histogram,
             bool includeUnderflowBin = false,
             bool includeOverflowBin = false)
{
  const int numBins  = histogram->GetNbinsX();
  const int firstBin = includeUnderflowBin ? 0           : 1;
  const int lastBin  = includeOverflowBin  ? numBins + 1 : numBins;

  double sumBinContent = 0.;
  for(int iBin = firstBin; iBin <= lastBin; ++iBin)
  {
    sumBinContent += histogram->GetBinContent(iBin);
  }
  return sumBinContent;
}

double 
square(double x)
{
  return x*x;
}

double
compIntegralErr(const TH1 * histogram,
		bool includeUnderflowBin = false,
		bool includeOverflowBin = false)
{
  const int numBins  = histogram->GetNbinsX();
  const int firstBin = includeUnderflowBin ? 0           : 1;
  const int lastBin  = includeOverflowBin  ? numBins + 1 : numBins;

  double sumBinErr2 = 0.;
  for(int iBin = firstBin; iBin <= lastBin; ++iBin)
  {
    sumBinErr2 += square(histogram->GetBinError(iBin));
  }
  return std::sqrt(sumBinErr2);
}

void dumpEventYields()
{
  gROOT->SetBatch(true);

  TH1::AddDirectory(false);

  typedef std::vector<std::string> vstring;
  vstring channels;
  //channels.push_back("hh_0l_4tau");
  //channels.push_back("hh_1l_3tau");
  channels.push_back("hh_2l_2tau");
  //channels.push_back("hh_3l_1tau");
  //channels.push_back("hh_4l");

  std::string inputFilePath = "/hdfs/local/ram/hhAnalysis/2017/2018Sep6/histograms/hh_2l_2tau/";

  std::map<std::string, std::string> inputFileNames; // key = channel
  // inputFileNames["hh_0l_4tau"] = "hh_0l_4tau/histograms_harvested_stage2_hh_0l_4tau_Tight_OS.root";
  // inputFileNames["hh_1l_3tau"] = "hh_1l_3tau/histograms_harvested_stage2_hh_1l_3tau_Tight_OS.root";
  inputFileNames["hh_2l_2tau"] = "histograms_harvested_stage2_hh_2l_2tau_disabled_disabled_Tight_OS.root";
  // inputFileNames["hh_3l_1tau"] = "hh_3l_1tau/histograms_harvested_stage2_hh_3l_1tau_Tight_OS.root";
  // inputFileNames["hh_4l"]      = "";

  std::map<std::string, std::string> directories; // key = channel
  // directories["hh_0l_4tau"] = "hh_0l_4tau_OS_Tight/sel/evt";
  // directories["hh_1l_3tau"] = "hh_1l_3tau_OS_Tight/sel/evt";
  directories["hh_2l_2tau"] = "hh_2l_2tau_sumOS_Tight/sel/evt";
  // directories["hh_3l_1tau"] = "hh_3l_1tau_OS_lepTight_tauTight/sel/evt";
  // directories["hh_4l"]      = "";

  std::map<std::string, vstring> signal_processes; // key = channel

  std::vector<std::string> signal_process_parts;
  signal_process_parts.push_back("");
  signal_process_parts.push_back("_Convs");
  signal_process_parts.push_back("_fake");
  
  std::map<std::string, vstring> background_processes; // key = channel
  background_processes["hh_2l_2tau"].push_back("TT");
  background_processes["hh_2l_2tau"].push_back("TTW");
  background_processes["hh_2l_2tau"].push_back("TTWW");
  background_processes["hh_2l_2tau"].push_back("TTZ");
  // background_processes["hh_2l_2tau"].push_back("tHW");
  // background_processes["hh_2l_2tau"].push_back("tHq");
  background_processes["hh_2l_2tau"].push_back("TH");
  background_processes["hh_2l_2tau"].push_back("WZ");
  background_processes["hh_2l_2tau"].push_back("ZZ");
  background_processes["hh_2l_2tau"].push_back("DY");
  background_processes["hh_2l_2tau"].push_back("W");
  // background_processes["hh_2l_2tau"].push_back("EWK");
  // background_processes["hh_2l_2tau"].push_back("Rares");
  background_processes["hh_2l_2tau"].push_back("Convs");
  background_processes["hh_2l_2tau"].push_back("data_fakes");
  background_processes["hh_2l_2tau"].push_back("fakes_mc");
  background_processes["hh_2l_2tau"].push_back("VH");
  // background_processes["hh_0l_4tau"] = background_processes["hh_2l_2tau"];
  // background_processes["hh_1l_3tau"] = background_processes["hh_2l_2tau"];
  // background_processes["hh_3l_1tau"] = background_processes["hh_2l_2tau"];
  // background_processes["hh_4l"]      = background_processes["hh_2l_2tau"];
  
  std::vector<std::string> background_process_parts;
  background_process_parts.push_back("");
  background_process_parts.push_back("_Convs");
  background_process_parts.push_back("_fake");

  double lumi_datacard = 41.5;
  double lumi_projection = 41.5;
  double lumi_SF = lumi_projection/lumi_datacard;
  std::cout << "scaling signal and background yields to L=" << lumi_projection << "fb^-1 @ 13 TeV." << std::endl;

  for ( vstring::const_iterator channel = channels.begin();
	channel != channels.end(); ++channel ) {
    std::cout << "channel = " << (*channel) << std::endl;

    TString inputFileName_full = inputFilePath.data();
    if ( !inputFileName_full.EndsWith("/") ) inputFileName_full.Append("/");
    inputFileName_full.Append(inputFileNames[*channel].data());
    std::cout << "channel = " << inputFileName_full.Data() << std::endl;
    TFile* inputFile = new TFile(inputFileName_full.Data());
    if ( !inputFile ) {
      std::cerr << "Failed to open input file = " << inputFileName_full.Data() << " !!" << std::endl;
      assert(0);
    }

    for ( vstring::const_iterator signal_process = signal_processes[*channel].begin();
	  signal_process != signal_processes[*channel].end(); ++signal_process ) {
      std::map<std::string, double> integral_parts;
      std::map<std::string, double> integralErr_parts;
      double integral_sum = 0.;
      double integralErr2_sum = 0.;
      for ( std::vector<std::string>::const_iterator signal_process_part = signal_process_parts.begin();
	    signal_process_part != signal_process_parts.end(); ++signal_process_part ) {
	std::string histogramName = Form("%s/%s%s/EventCounter", 
          directories[*channel].data(), signal_process->data(), signal_process_part->data());
	TH1* histogram = loadHistogram(inputFile, histogramName);
	if ( histogram ) {
	  histogram->Scale(lumi_SF);
	  double integral = compIntegral(histogram);
	  integral_parts[*signal_process_part] = integral;
	  integral_sum += integral;
	  double integralErr = compIntegralErr(histogram);
	  integralErr_parts[*signal_process_part] = integralErr;
	  integralErr2_sum += square(integralErr); 
	}
      }
      double integralErr_sum = TMath::Sqrt(integralErr2_sum);
      std::cout << (*signal_process) << ": " << integral_sum << " +/- " << integralErr_sum << std::endl;
      if ( integral_parts.size() > 1 ) {
	std::cout << " (non-fake = " << integral_parts[""] << " +/- " << integralErr_parts[""] << ","
		  << " fake = " << integral_parts["_fake"] << " +/- " << integralErr_parts["_fake"] << ","
		  << " conversion = " << integral_parts["_Convs"] << " +/- " << integralErr_parts["_Convs"] << ")" << std::endl;
      }
    }
    for ( vstring::const_iterator background_process = background_processes[*channel].begin();
	  background_process != background_processes[*channel].end(); ++background_process ) {
      std::map<std::string, double> integral_parts;
      std::map<std::string, double> integralErr_parts;
      double integral_sum = 0.;
      double integralErr2_sum = 0.;
      for ( std::vector<std::string>::const_iterator background_process_part = background_process_parts.begin();
	    background_process_part != background_process_parts.end(); ++background_process_part ) {
	std::string histogramName = Form("%s/%s%s/EventCounter", 
          directories[*channel].data(), background_process->data(), background_process_part->data());
	TH1* histogram = loadHistogram(inputFile, histogramName);
	if ( histogram ) {
	  histogram->Scale(lumi_SF);
	  double integral = compIntegral(histogram);
	  integral_parts[*background_process_part] = integral;
	  integral_sum += integral;
	  double integralErr = compIntegralErr(histogram);
	  integralErr_parts[*background_process_part] = integralErr;
	  integralErr2_sum += square(integralErr); 
	}
      }
      double integralErr_sum = TMath::Sqrt(integralErr2_sum);
      std::cout << (*background_process) << ": " << integral_sum << " +/- " << integralErr_sum << std::endl;
      if ( integral_parts.size() > 1 ) {
	std::cout << " (non-fake = " << integral_parts[""] << " +/- " << integralErr_parts[""] << ","
		  << " fake = " << integral_parts["_fake"] << " +/- " << integralErr_parts["_fake"] << ","
		  << " conversion = " << integral_parts["_Convs"] << " +/- " << integralErr_parts["_Convs"] << ")" << std::endl;
      }
    }

    std::string histogramName = Form("%s/%s/EventCounter", 
      directories[*channel].data(), "data_obs");
    TH1* histogram = loadHistogram(inputFile, histogramName);
    if ( histogram ) {
      histogram->Scale(lumi_SF);
      double integral = compIntegral(histogram);
      std::cout << "data_obs: " << integral << std::endl;
    }
    std::cout << std::endl;

    delete inputFile;
  }
}
