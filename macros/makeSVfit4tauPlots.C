
#include <TFile.h>
#include <TString.h>
#include <TCanvas.h>
#include <TPad.h>
#include <TVirtualPad.h>
#include <TH1.h>
#include <TAxis.h>
#include <TLegend.h>
#include <TLegendEntry.h>
#include <TPaveText.h>
#include <TMath.h>
#include <TROOT.h>
#include <TStyle.h>
#include <TList.h>

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <iomanip>
#include <assert.h>

TH1* loadHistogram(TFile* inputFile, const std::string& directoryName, const std::string& histogramName)
{
  std::string histogramName_full = directoryName;
  if ( histogramName_full.back() != '/' ) histogramName_full.append("/");
  histogramName_full.append(histogramName);
  TH1* histogram = dynamic_cast<TH1*>(inputFile->Get(histogramName_full.data()));
  if ( !histogram ) {
    std::cerr << "Failed to load histogram = " << histogramName_full << " from file = " << inputFile->GetName() << " !!" << std::endl;
    assert(0);
    return 0;
  }
  if ( !histogram->GetSumw2N() ) histogram->Sumw2();
  return histogram;
}

TH1* divideHistogramByBinWidth(TH1* histogram)
{
  std::string histogramName_density = Form("%s_density", histogram->GetName());
  TH1* histogram_density = (TH1*)histogram->Clone(histogramName_density.data());
  const TAxis * const xAxis = histogram->GetXaxis();
  int numBins = xAxis->GetNbins();
  for ( int idxBin = 1; idxBin <= numBins; ++idxBin) {
    double binContent = histogram->GetBinContent(idxBin);
    double binError   = histogram->GetBinError(idxBin);
    double binWidth   = xAxis->GetBinWidth(idxBin);
    histogram_density->SetBinContent(idxBin, binContent/binWidth);
    histogram_density->SetBinError(idxBin, binError/binWidth);
  }
  return histogram_density;
}

void makePlot(double canvasSizeX, double canvasSizeY,
	      TH1* histogram_top, const std::string& legendEntry_top,
	      TH1* histogram_bottom, const std::string& legendEntry_bottom,
	      double legendTextSize, double legendPosX, double legendPosY, double legendSizeX, double legendSizeY, 
	      const std::string& labelOnTop,
	      double xMin, double xMax, const std::string& xAxisTitle, double xAxisOffset,
	      bool useLogScale, double yMin, double yMax, const std::string& yAxisTitle, double yAxisOffset,
	      const std::string& outputFileName)
{
  std::cout << "<makePlot>:" << std::endl;
  std::cout << " " << legendEntry_top << ": rms = " << histogram_top->GetRMS() << std::endl;
  std::cout << " " << legendEntry_bottom << ": rms = " << histogram_bottom->GetRMS() << std::endl;
  std::cout << " outputFileName = " << outputFileName << std::endl;

  TCanvas* canvas = new TCanvas("canvas", "canvas", canvasSizeX, canvasSizeY);
  canvas->SetFillColor(10);
  canvas->SetBorderSize(2);
  canvas->SetTopMargin(0.070);
  canvas->SetLeftMargin(0.17);
  canvas->SetBottomMargin(0.165);
  canvas->SetRightMargin(0.015);
  canvas->SetLogx(true);
  canvas->SetLogy(true);
  canvas->Draw();
  canvas->cd();

  int fillColor_top = 0;
  int lineColor_top = 1;
  int fillColor_bottom = 46;
  int lineColor_bottom = 46;

  // CV: make stack plot
  std::string histogramName_top_cloned = Form("%s_cloned", histogram_top->GetName());
  TH1* histogram_top_cloned = (TH1*)histogram_top->Clone(histogramName_top_cloned.data());
  histogram_top_cloned->Add(histogram_bottom);
  std::cout << " sum: rms = " << histogram_top_cloned->GetRMS() << std::endl;

  TH1* histogram_top_density = divideHistogramByBinWidth(histogram_top_cloned);
  std::cout << "histogram_top_density: yMax = " << histogram_top_density->GetMaximum() << ", yMin = " << histogram_top_density->GetMinimum() << std::endl;
  
  histogram_top_density->SetFillColor(fillColor_top);
  histogram_top_density->SetFillStyle(1001);
  histogram_top_density->SetLineColor(lineColor_top);
  histogram_top_density->SetLineStyle(1);
  histogram_top_density->SetLineWidth(2);

  TH1* histogram_bottom_density = divideHistogramByBinWidth(histogram_bottom);
  std::cout << "histogram_bottom_density: yMax = " << histogram_bottom_density->GetMaximum() << ", yMin = " << histogram_bottom_density->GetMinimum() << std::endl;

  histogram_bottom_density->SetFillColor(fillColor_bottom);
  histogram_bottom_density->SetFillStyle(1001);
  histogram_bottom_density->SetLineColor(lineColor_bottom);
  histogram_bottom_density->SetLineStyle(1);
  histogram_bottom_density->SetLineWidth(0);

  TAxis* xAxis = histogram_top_density->GetXaxis();
  xAxis->SetRangeUser(xMin, xMax);
  xAxis->SetTitle(xAxisTitle.data());
  xAxis->SetTitleOffset(xAxisOffset);
  xAxis->SetTitleSize(0.070);
  xAxis->SetTitleFont(42);
  xAxis->SetLabelOffset(0.010);
  xAxis->SetLabelSize(0.055);
  xAxis->SetLabelFont(42);
  xAxis->SetTickLength(0.040);
  xAxis->SetNdivisions(510);

  TAxis* yAxis = histogram_top_density->GetYaxis();
  yAxis->SetTitle(yAxisTitle.data());
  yAxis->SetTitleOffset(yAxisOffset);
  yAxis->SetTitleSize(0.070);
  yAxis->SetTitleFont(42);
  yAxis->SetLabelOffset(0.010);
  yAxis->SetLabelSize(0.055);
  yAxis->SetLabelFont(42);
  yAxis->SetTickLength(0.040);  
  yAxis->SetNdivisions(505);

  histogram_top_density->SetTitle("");
  histogram_top_density->SetStats(false);
  if      ( yMax > 0.   ) histogram_top_density->SetMaximum(yMax);
  else if ( useLogScale ) histogram_top_density->SetMaximum(5.*histogram_top_density->GetMaximum());
  else                    histogram_top_density->SetMaximum(1.2*histogram_top_density->GetMaximum());
  histogram_top_density->SetMinimum(yMin);
  histogram_top_density->Draw("hist");

  histogram_bottom_density->Draw("histsame");

  histogram_top_density->Draw("axissame");

  //TPaveText* label = new TPaveText(0.21, 0.86, 0.46, 0.94, "NDC");
  TPaveText* label = new TPaveText(0.1700, 0.9475, 0.4600, 1.0375, "NDC");
  label->SetFillStyle(0);
  label->SetBorderSize(0);
  label->AddText(labelOnTop.data());
  label->SetTextFont(42);
  label->SetTextSize(0.055);
  label->SetTextColor(1);
  label->SetTextAlign(13);
  label->Draw();

  TLegend* legend = new TLegend(legendPosX, legendPosY, legendPosX + legendSizeX, legendPosY + legendSizeY, NULL, "brNDC");
  legend->SetFillColor(10);
  legend->SetFillStyle(0);
  legend->SetBorderSize(0);
  legend->SetTextFont(42);
  legend->SetTextSize(legendTextSize);
  legend->SetTextColor(1);
  legend->SetMargin(0.20);
  legend->AddEntry(histogram_top_density,    legendEntry_top.data(),    "f");
  legend->AddEntry(histogram_bottom_density, legendEntry_bottom.data(), "f");
  legend->Draw();

  canvas->Update();

  size_t idx = outputFileName.find_last_of('.');
  std::string outputFileName_plot = std::string(outputFileName, 0, idx);
  canvas->Print(std::string(outputFileName_plot).append(".pdf").data());
  canvas->Print(std::string(outputFileName_plot).append(".root").data());

  delete label;
  delete legend;
  delete histogram_top_cloned;
  delete histogram_top_density;
  delete histogram_bottom_density;
  delete canvas;
}

void makeSVfit4tauPlots()
{
  gROOT->SetBatch(true);

  TH1::AddDirectory(false);

  std::vector<int> massPoints;
  massPoints.push_back(300);
  massPoints.push_back(500);
  massPoints.push_back(800);
  
  std::map<int, std::string> samples; // key = massPoint
  samples[300] = "X(300 GeV) #rightarrow HH #rightarrow #tau#tau#tau#tau #rightarrow ll#tau_{h}#tau_{h}";
  samples[500] = "X(500 GeV) #rightarrow HH #rightarrow #tau#tau#tau#tau #rightarrow ll#tau_{h}#tau_{h}";
  samples[800] = "X(800 GeV) #rightarrow HH #rightarrow #tau#tau#tau#tau #rightarrow ll#tau_{h}#tau_{h}";
  
  std::string inputFilePath = "/hdfs/local/veelken/hhAnalysis/2016/2018Aug10_SVfit4tau/histograms/SVfit4tau/gen_smeared/";
  std::map<int, std::string> inputFileNames; // key = massPoint
  inputFileNames[300] = "x_to_hh_300/x_to_hh_300_gen_smeared_central_1.root";
  inputFileNames[500] = "x_to_hh_500/x_to_hh_500_gen_smeared_central_1.root";
  inputFileNames[800] = "x_to_hh_800/x_to_hh_800_gen_smeared_central_1.root";

  std::string outputFilePath = "/home/veelken/CMSSW_9_4_6_patch1/src/hhAnalysis/tttt/macros/plots/";
  std::map<int, std::string> outputFileNames; // key = massPoint
  outputFileNames[300] = "makeSVfit4tauPlots_x_to_hh_300_log.pdf";
  outputFileNames[500] = "makeSVfit4tauPlots_x_to_hh_500_log.pdf";
  outputFileNames[800] = "makeSVfit4tauPlots_x_to_hh_800_log.pdf";

  std::string directory_correctAssoc_chosen          = "SVfit4tau_2lepton_2tau/gen_smeared/svFit4tauResolution_wMassContraint_logM0p0_correctAssoc_chosen";
  std::string histogramName_correctAssoc_chosen      = "dihiggsRatioMass1";
  std::string directory_correctAssoc_discarded       = "SVfit4tau_2lepton_2tau/gen_smeared/svFit4tauResolution_wMassContraint_logM0p0_correctAssoc_discarded";
  std::string histogramName_correctAssoc_discarded   = "dihiggsRatioMass1";
  std::string directory_incorrectAssoc_chosen        = "SVfit4tau_2lepton_2tau/gen_smeared/svFit4tauResolution_wMassContraint_logM0p0_incorrectAssoc_chosen";
  std::string histogramName_incorrectAssoc_chosen    = "dihiggsRatioMass1";
  std::string directory_incorrectAssoc_discarded     = "SVfit4tau_2lepton_2tau/gen_smeared/svFit4tauResolution_wMassContraint_logM0p0_incorrectAssoc_discarded";
  std::string histogramName_incorrectAssoc_discarded = "dihiggsRatioMass1";
  std::string directory_EventCounter                 = "SVfit4tau_2lepton_2tau/gen_smeared/evt";
  std::string histogramName_EventCounter             = "EventCounter";

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

    TH1* histogram_correctAssoc_chosen = loadHistogram(
      inputFile, 
      Form("%s/signal_radion_%i", directory_correctAssoc_chosen.data(), *massPoint), 
      histogramName_correctAssoc_chosen);
    TH1* histogram_correctAssoc_discarded = loadHistogram(
      inputFile, 
      Form("%s/signal_radion_%i", directory_correctAssoc_discarded.data(), *massPoint),   
      histogramName_correctAssoc_discarded);
    TH1* histogram_incorrectAssoc_chosen = loadHistogram(
      inputFile, 
      Form("%s/signal_radion_%i", directory_incorrectAssoc_chosen.data(), *massPoint),    
      histogramName_incorrectAssoc_chosen);
    TH1* histogram_incorrectAssoc_discarded = loadHistogram(
      inputFile, 
      Form("%s/signal_radion_%i", directory_incorrectAssoc_discarded.data(), *massPoint), 
      histogramName_incorrectAssoc_discarded);
    TH1* histogram_EventCounter = loadHistogram(
      inputFile, 
      Form("%s/signal_radion_%i", directory_EventCounter.data(), *massPoint),             
      histogramName_EventCounter);
    
    double numEvents = histogram_EventCounter->Integral();
    if ( !(numEvents > 0. ) ) {
      std::cerr << "Failed to read number of events or number of events is zero !!" << std::endl;
      assert(0);
    }

    std::cout << "massPoint = " << (*massPoint) << ": numEvents = " << numEvents << std::endl;
    std::cout << " chosen: correct = " << histogram_correctAssoc_chosen->Integral() 
	      << " (" << 100.*histogram_correctAssoc_chosen->Integral()/(histogram_correctAssoc_chosen->Integral() + histogram_incorrectAssoc_chosen->Integral()) << "%)," 
	      << " spurious = " << histogram_incorrectAssoc_chosen->Integral() 
	      << " (" << 100.*histogram_incorrectAssoc_chosen->Integral()/(histogram_correctAssoc_chosen->Integral() + histogram_incorrectAssoc_chosen->Integral()) << "%)," 
	      << std::endl;    
    std::cout << " discarded: correct = " << histogram_correctAssoc_discarded->Integral() 
	      << " (" << 100.*histogram_correctAssoc_discarded->Integral()/(histogram_correctAssoc_chosen->Integral() + histogram_correctAssoc_discarded->Integral()) << "%)," 
	      << " spurious = " << histogram_incorrectAssoc_discarded->Integral() 
	      << " (" << 100.*histogram_incorrectAssoc_discarded->Integral()/(histogram_incorrectAssoc_chosen->Integral() + histogram_incorrectAssoc_discarded->Integral()) << "%)," 
	      << std::endl;

    histogram_correctAssoc_chosen->Scale(1./numEvents);
    histogram_correctAssoc_discarded->Scale(1./numEvents);
    histogram_incorrectAssoc_chosen->Scale(1./numEvents);
    histogram_incorrectAssoc_discarded->Scale(1./numEvents);
 
    std::string outputFileName_chosen_full = outputFilePath;
    if ( outputFileName_chosen_full.back() != '/' ) outputFileName_chosen_full.append("/");
    outputFileName_chosen_full.append(TString(outputFileNames[*massPoint].data()).ReplaceAll("_log.pdf", "_chosen_log.pdf").Data());
    makePlot(800, 650, 
      histogram_correctAssoc_chosen, "Correct pairing",
      histogram_incorrectAssoc_chosen, "Spurious pairing",
      0.055, 0.61, 0.74, 0.28, 0.15,
      samples[*massPoint],
      0.2, 5., "m_{HH}/m_{HH}^{true}", 1.08,
      true, 1.e-2, -1., "dN/d(m_{HH}/m_{HH}^{true})", 1.2,
      outputFileName_chosen_full);

    std::string outputFileName_discarded_full = outputFilePath;
    if ( outputFileName_discarded_full.back() != '/' ) outputFileName_discarded_full.append("/");
    outputFileName_discarded_full.append(TString(outputFileNames[*massPoint].data()).ReplaceAll("_log.pdf", "_discarded_log.pdf").Data());
    makePlot(800, 650, 
      histogram_correctAssoc_discarded, "Correct pairing",
      histogram_incorrectAssoc_discarded, "Spurious pairing",
      0.055, 0.61, 0.74, 0.28, 0.15,
      samples[*massPoint],
      0.2, 5., "m_{HH}/m_{HH}^{true}", 1.08,
      true, 1.e-2, -1., "dN/d(m_{HH}/m_{HH}^{true})", 1.2,
      outputFileName_discarded_full);

    delete inputFile;
  }
}
