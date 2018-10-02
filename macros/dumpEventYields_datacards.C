
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
    std::cerr << "Failed to load histogram = " << histogramName << " from file = " << inputFile->GetName() << " !!" << std::endl;
    assert(0);
  }
  if ( !histogram->GetSumw2N() ) histogram->Sumw2();
  return histogram;
}

void dumpEventYields_datacards()
{
  gROOT->SetBatch(true);

  TH1::AddDirectory(false);

  typedef std::vector<std::string> vstring;
  vstring channels;
  channels.push_back("hh_2lss");
  //channels.push_back("hh_2l_2tau"); 

  std::string inputFilePath = "/home/sbhowmik/hhAnalysis/2017/2017Sept29/datacards/hh_2lss/";

  std::map<std::string, std::string> inputFileNames; // key = channel
  inputFileNames["hh_2lss"] = "prepareDatacards_hh_2lss_dihiggsVisMass.root";
  inputFileNames["hh_2l_2tau"] = "prepareDatacards_2l_2tau_mTauTauVis.root";

  std::map<std::string, vstring> signal_processes; // key = channel
  signal_processes["hh_2lss"].push_back("signal_ggf_spin0_400_hh_tttt");
  signal_processes["hh_2lss"].push_back("signal_ggf_spin0_400_hh_wwtt");
  signal_processes["hh_2lss"].push_back("signal_ggf_spin0_400_hh_wwww");
  signal_processes["hh_2l_2tau"] = signal_processes["hh_2lss"];
 
  std::map<std::string, vstring> background_processes; // key = channel
  background_processes["hh_2lss"].push_back("TT");
  background_processes["hh_2lss"].push_back("TTW");
  background_processes["hh_2lss"].push_back("TTWW");
  background_processes["hh_2lss"].push_back("TTZ");
  background_processes["hh_2lss"].push_back("TTH");
  background_processes["hh_2lss"].push_back("TH");
  background_processes["hh_2lss"].push_back("WW");
  background_processes["hh_2lss"].push_back("WZ");
  background_processes["hh_2lss"].push_back("ZZ");
  background_processes["hh_2lss"].push_back("DY");
  background_processes["hh_2lss"].push_back("W");
  background_processes["hh_2lss"].push_back("VH");
  background_processes["hh_2lss"].push_back("Other");
  background_processes["hh_2lss"].push_back("conversions"); 
  background_processes["hh_2lss"].push_back("fakes_data"); 
  background_processes["hh_2lss"].push_back("flips_data"); 
  //background_processes["hh_2lss"].push_back("fakes_mc");

  background_processes["hh_2l_2tau"] = background_processes["hh_2lss"];

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
      std::string histogramName = Form("%s", signal_process->data());
      TH1* histogram = loadHistogram(inputFile, histogramName);
      histogram->Scale(lumi_SF);
      std::cout << " " << (*signal_process) << ": " << histogram->Integral() << std::endl;
    }
    double Total_Background = 0;
    for ( vstring::const_iterator background_process = background_processes[*channel].begin();
	  background_process != background_processes[*channel].end(); ++background_process ) {
      std::string histogramName = Form("%s", background_process->data());
      TH1* histogram = loadHistogram(inputFile, histogramName);
      histogram->Scale(lumi_SF);
      std::cout << " " << (*background_process) << ": " << histogram->Integral() << std::endl;
      Total_Background += histogram->Integral();
    }
    std::cout << " Total Background: " << Total_Background << std::endl;

    std::string histogramName = "data_obs";
    TH1* histogram = loadHistogram(inputFile, histogramName);
    histogram->Scale(lumi_SF);
    std::cout << " data_obs: " << histogram->Integral() << std::endl;

    std::cout << std::endl;

    delete inputFile;
  }
}
