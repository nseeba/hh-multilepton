
#include <TFile.h>
#include <TString.h>
#include <TH1.h>
#include <TH2.h>
#include <TGraph.h>
#include <TAxis.h>
#include <TCanvas.h>
#include <TLegend.h>
#include <TMath.h>
#include <TROOT.h>
#include <TStyle.h>

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <iomanip>
#include <assert.h>

TFile* openFile(const std::string& inputFilePath, const std::string& inputFileName)
{
  TString inputFileName_full = inputFilePath.data();
  if ( !inputFileName_full.EndsWith("/") ) inputFileName_full.Append("/");
  inputFileName_full.Append(inputFileName.data());
  TFile* inputFile = new TFile(inputFileName_full.Data());
  if ( !inputFile ) {
    std::cerr << "Failed to open file = " << inputFileName_full.Data() << " !!" << std::endl;
    assert(0);
  }
  return inputFile;
}

TH1* loadHistogram(TFile* inputFile, const std::string& directoryName, const std::string& histogramName)
{
  TString histogramName_full = directoryName.data();
  if ( !histogramName_full.EndsWith("/") ) histogramName_full.Append("/");
  histogramName_full.Append(histogramName.data());
  std::cout << "loading histogram = " << histogramName_full.Data() << " from file = " << inputFile->GetName() << std::endl;
  TH1* histogram = dynamic_cast<TH1*>(inputFile->Get(histogramName_full.Data()));
  std::cout << "histogram = " << histogram << std::endl;
  if ( !histogram ) {
    std::cerr << "Failed to load histogram = " << histogramName_full << " from file = " << inputFile->GetName() << " !!" << std::endl;
    assert(0);
  }
  if ( !histogram->GetSumw2N() ) histogram->Sumw2();
  if ( histogram->GetNbinsX() >= 50 ) histogram->Rebin(5);
  return histogram;
}

double compIntegral(const TH1* histogram)
{
  if ( !histogram ) return -1.;
  double integral = 0.;
  int numBins = histogram->GetNbinsX();
  for ( int iBin = 1; iBin <= numBins; ++iBin ) {
    double binContent = histogram->GetBinContent(iBin);
    integral += binContent;
  }
  return integral;
}

TH1* compRatioHistogram(const std::string& ratioHistogramName, const TH1* numerator, const TH1* denominator)
{
  TH1* histogramRatio = 0;
  
  if ( numerator->GetDimension() == denominator->GetDimension() &&
       numerator->GetNbinsX() == denominator->GetNbinsX() ) {
    histogramRatio = (TH1*)numerator->Clone(ratioHistogramName.data());
    histogramRatio->Divide(denominator);
    
    int nBins = histogramRatio->GetNbinsX();
    for ( int iBin = 1; iBin <= nBins; ++iBin ){
      double binContent = histogramRatio->GetBinContent(iBin);
      histogramRatio->SetBinContent(iBin, binContent - 1.);
    }
    
    histogramRatio->SetLineColor(numerator->GetLineColor());
    histogramRatio->SetLineWidth(numerator->GetLineWidth());
    histogramRatio->SetMarkerColor(numerator->GetMarkerColor());
    histogramRatio->SetMarkerStyle(numerator->GetMarkerStyle());
    histogramRatio->SetMarkerSize(numerator->GetMarkerSize());
  }

  return histogramRatio;
}

void showHistograms(double canvasSizeX, double canvasSizeY,
		    TH1* histogram_ref, const std::string& legendEntry_ref, double integral_ref,
		    TH1* histogram2, const std::string& legendEntry2, double integral2,
		    TH1* histogram3, const std::string& legendEntry3, double integral3,
		    TH1* histogram4, const std::string& legendEntry4, double integral4,
		    TH1* histogram5, const std::string& legendEntry5, double integral5,
		    TH1* histogram6, const std::string& legendEntry6, double integral6,
		    const std::string& xAxisTitle, double xAxisOffset,
		    bool useLogScale, double yMin, double yMax, const std::string& yAxisTitle, double yAxisOffset,
		    double legendX0, double legendY0, 
		    const std::string& outputFileName)
{
  if ( !(histogram_ref && histogram2) ) return;

  TCanvas* canvas = new TCanvas("canvas", "canvas", canvasSizeX, canvasSizeY);
  canvas->SetFillColor(10);
  canvas->SetBorderSize(2);
  canvas->SetLeftMargin(0.12);
  canvas->SetBottomMargin(0.12);

  TPad* topPad = new TPad("topPad", "topPad", 0.00, 0.35, 1.00, 1.00);
  topPad->SetFillColor(10);
  topPad->SetTopMargin(0.04);
  topPad->SetLeftMargin(0.15);
  topPad->SetBottomMargin(0.03);
  topPad->SetRightMargin(0.05);
  topPad->SetLogy(useLogScale);

  TPad* bottomPad = new TPad("bottomPad", "bottomPad", 0.00, 0.00, 1.00, 0.35);
  bottomPad->SetFillColor(10);
  bottomPad->SetTopMargin(0.02);
  bottomPad->SetLeftMargin(0.15);
  bottomPad->SetBottomMargin(0.24);
  bottomPad->SetRightMargin(0.05);
  bottomPad->SetLogy(false);

  canvas->cd();
  topPad->Draw();
  topPad->cd();

  //int colors[6] = { kBlack, kGreen - 6, kBlue - 7,  kMagenta - 7, kCyan - 6, kRed - 6 };
  int colors[6] = { kBlack, kRed, kBlue - 7,  kMagenta - 7, kCyan - 6, kRed - 6 };
  int markerStyles[6] = { 24, 25, 20, 21, 22, 23 };
  int markerSizes[6] = { 1, 1, 1, 1, 1, 1 };

  TLegend* legend = new TLegend(legendX0, legendY0, legendX0 + 0.61, legendY0 + 0.21, "", "brNDC"); 
  legend->SetBorderSize(0);
  legend->SetFillColor(0);

  histogram_ref->SetTitle("");
  histogram_ref->SetStats(false);
  histogram_ref->SetMinimum(yMin);
  histogram_ref->SetMaximum(yMax);
  histogram_ref->SetLineColor(colors[0]);
  histogram_ref->SetLineWidth(2);
  histogram_ref->SetMarkerColor(colors[0]);
  histogram_ref->SetMarkerStyle(markerStyles[0]);
  histogram_ref->SetMarkerSize(markerSizes[0]);
  histogram_ref->Draw("e1p");
  //if ( integral_ref >= 0. ) legend->AddEntry(histogram_ref, Form("%s: %1.2f", legendEntry_ref.data(), integral_ref), "p");
  //else legend->AddEntry(histogram_ref, legendEntry_ref.data(), "p");
  legend->AddEntry(histogram_ref, Form("%s: %1.2f", legendEntry_ref.data(), integral_ref), "p");

  TAxis* xAxis_top = histogram_ref->GetXaxis();
  xAxis_top->SetTitle(xAxisTitle.data());
  xAxis_top->SetTitleOffset(xAxisOffset);
  xAxis_top->SetLabelColor(10);
  xAxis_top->SetTitleColor(10);

  TAxis* yAxis_top = histogram_ref->GetYaxis();
  yAxis_top->SetTitle(yAxisTitle.data());
  yAxis_top->SetTitleOffset(yAxisOffset);

  if ( histogram2 ) {
    histogram2->SetLineColor(colors[1]);
    histogram2->SetLineWidth(2);
    histogram2->SetMarkerColor(colors[1]);
    histogram2->SetMarkerStyle(markerStyles[1]);
    histogram2->SetMarkerSize(markerSizes[1]);
    histogram2->Draw("e1psame");
    //if ( integral2 >= 0. ) legend->AddEntry(histogram2, Form("%s: %1.2f", legendEntry2.data(), integral2), "p");
    //else legend->AddEntry(histogram2, legendEntry2.data(), "p");
    legend->AddEntry(histogram2, Form("%s: %1.2f", legendEntry2.data(), integral2), "p");
  }

  if ( histogram3 ) {
    histogram3->SetLineColor(colors[2]);
    histogram3->SetLineWidth(2);
    histogram3->SetMarkerColor(colors[2]);
    histogram3->SetMarkerStyle(markerStyles[2]);
    histogram3->SetMarkerSize(markerSizes[2]);
    histogram3->Draw("e1psame");
    //if ( integral3 >= 0. ) legend->AddEntry(histogram3, Form("%s: %1.2f", legendEntry3.data(), integral3), "p");
    //else legend->AddEntry(histogram3, legendEntry3.data(), "p");
    legend->AddEntry(histogram3, Form("%s: %1.2f", legendEntry3.data(), integral3), "p");
  }

  if ( histogram4 ) {
    histogram4->SetLineColor(colors[3]);
    histogram4->SetLineWidth(2);
    histogram4->SetMarkerColor(colors[3]);
    histogram4->SetMarkerStyle(markerStyles[3]);
    histogram4->SetMarkerSize(markerSizes[3]);
    histogram4->Draw("e1psame");
    if ( integral4 >= 0. ) legend->AddEntry(histogram4, Form("%s: %1.2f", legendEntry4.data(), integral4), "p");
    else legend->AddEntry(histogram4, legendEntry4.data(), "p");
  }

  if ( histogram5 ) {
    histogram5->SetLineColor(colors[4]);
    histogram5->SetLineWidth(2);
    histogram5->SetMarkerColor(colors[4]);
    histogram5->SetMarkerStyle(markerStyles[4]);
    histogram5->SetMarkerSize(markerSizes[4]);
    histogram5->Draw("e1psame");
    if ( integral5 >= 0. ) legend->AddEntry(histogram5, Form("%s: %1.2f", legendEntry5.data(), integral5), "p");
    else legend->AddEntry(histogram5, legendEntry5.data(), "p");
  }

  if ( histogram6 ) {
    histogram6->SetLineColor(colors[5]);
    histogram6->SetLineWidth(2);
    histogram6->SetMarkerColor(colors[5]);
    histogram6->SetMarkerStyle(markerStyles[5]);
    histogram6->SetMarkerSize(markerSizes[5]);
    histogram6->Draw("e1psame");
    if ( integral6 >= 0. ) legend->AddEntry(histogram6, Form("%s: %1.2f", legendEntry6.data(), integral6), "p");
    else legend->AddEntry(histogram6, legendEntry6.data(), "p");
  }

  legend->Draw();

  canvas->cd();
  bottomPad->Draw();
  bottomPad->cd();

  TH1* histogram2_div_ref = 0;
  if ( histogram2 ) {
    std::string histogramName2_div_ref = std::string(histogram2->GetName()).append("_div_").append(histogram_ref->GetName());
    histogram2_div_ref = compRatioHistogram(histogramName2_div_ref, histogram2, histogram_ref);
    if ( histogram2_div_ref ) {
      histogram2_div_ref->SetTitle("");
      histogram2_div_ref->SetStats(false);
      histogram2_div_ref->SetMinimum(-1.10);
      histogram2_div_ref->SetMaximum(+1.10);
      
      TAxis* xAxis_bottom = histogram2_div_ref->GetXaxis();
      xAxis_bottom->SetTitle(xAxis_top->GetTitle());
      xAxis_bottom->SetLabelColor(1);
      xAxis_bottom->SetTitleColor(1);
      xAxis_bottom->SetTitleOffset(1.20);
      xAxis_bottom->SetTitleSize(0.08);
      xAxis_bottom->SetLabelOffset(0.02);
      xAxis_bottom->SetLabelSize(0.08);
      xAxis_bottom->SetTickLength(0.055);
      
      TAxis* yAxis_bottom = histogram2_div_ref->GetYaxis();
      yAxis_bottom->SetTitle(Form("#frac{%s - %s}{%s}", legendEntry2.data(), legendEntry_ref.data(), legendEntry_ref.data()));
      yAxis_bottom->SetTitleOffset(0.85);
      yAxis_bottom->SetNdivisions(505);
      yAxis_bottom->CenterTitle();
      yAxis_bottom->SetTitleSize(0.08);
      yAxis_bottom->SetLabelSize(0.08);
      yAxis_bottom->SetTickLength(0.04);  
      
      histogram2_div_ref->Draw("e1p");
    }
  }

  TH1* histogram3_div_ref = 0;
  if ( histogram3 ) {
    std::string histogramName3_div_ref = std::string(histogram3->GetName()).append("_div_").append(histogram_ref->GetName());
    histogram3_div_ref = compRatioHistogram(histogramName3_div_ref, histogram3, histogram_ref);
    if ( histogram3_div_ref ) {
      histogram3_div_ref->SetTitle("");
      histogram3_div_ref->SetStats(false);
      histogram3_div_ref->SetMinimum(-1.10);
      histogram3_div_ref->SetMaximum(+1.10);
      
      TAxis* xAxis_bottom = histogram3_div_ref->GetXaxis();
      xAxis_bottom->SetTitle(xAxis_top->GetTitle());
      xAxis_bottom->SetLabelColor(1);
      xAxis_bottom->SetTitleColor(1);
      xAxis_bottom->SetTitleOffset(1.20);
      xAxis_bottom->SetTitleSize(0.08);
      xAxis_bottom->SetLabelOffset(0.02);
      xAxis_bottom->SetLabelSize(0.08);
      xAxis_bottom->SetTickLength(0.055);
      
      TAxis* yAxis_bottom = histogram3_div_ref->GetYaxis();
      yAxis_bottom->SetTitle(Form("#frac{%s - %s}{%s}", legendEntry3.data(), legendEntry_ref.data(), legendEntry_ref.data()));
      yAxis_bottom->SetTitleOffset(0.85);
      yAxis_bottom->SetNdivisions(505);
      yAxis_bottom->CenterTitle();
      yAxis_bottom->SetTitleSize(0.08);
      yAxis_bottom->SetLabelSize(0.08);
      yAxis_bottom->SetTickLength(0.04);  
      
      if ( histogram2 ) histogram3_div_ref->Draw("e1psame");
      else histogram3_div_ref->Draw("e1p");
    }
  }

  TGraph* graph_line = new TGraph(2);
  graph_line->SetPoint(0, xAxis_top->GetXmin(), 0.);
  graph_line->SetPoint(1, xAxis_top->GetXmax(), 0.);
  graph_line->SetLineColor(8);
  graph_line->SetLineWidth(1);
  graph_line->Draw("L");

  if ( histogram2_div_ref ) histogram2_div_ref->Draw("e1psame");
  if ( histogram3_div_ref ) histogram3_div_ref->Draw("e1psame");

  TH1* histogram4_div_ref = 0;
  if ( histogram4 ) {
    std::string histogramName4_div_ref = std::string(histogram4->GetName()).append("_div_").append(histogram_ref->GetName());
    histogram4_div_ref = compRatioHistogram(histogramName4_div_ref, histogram4, histogram_ref);
    if ( histogram4_div_ref ) {
      histogram4_div_ref->Draw("e1psame");
    }
  }

  TH1* histogram5_div_ref = 0;
  if ( histogram5 ) {
    std::string histogramName5_div_ref = std::string(histogram5->GetName()).append("_div_").append(histogram_ref->GetName());
    histogram5_div_ref = compRatioHistogram(histogramName5_div_ref, histogram5, histogram_ref);
    if ( histogram5_div_ref ) {
      histogram5_div_ref->Draw("e1psame");
    }
  }

  TH1* histogram6_div_ref = 0;
  if ( histogram6 ) {
    std::string histogramName6_div_ref = std::string(histogram6->GetName()).append("_div_").append(histogram_ref->GetName());
    histogram6_div_ref = compRatioHistogram(histogramName6_div_ref, histogram6, histogram_ref);
    if ( histogram6_div_ref ) {
      histogram6_div_ref->Draw("e1psame");
    }
  }
  
  canvas->Update();
  size_t idx = outputFileName.find_last_of('.');
  std::string outputFileName_plot = std::string(outputFileName, 0, idx);
  if ( useLogScale ) outputFileName_plot.append("_log");
  else outputFileName_plot.append("_linear");
  if ( idx != std::string::npos ) canvas->Print(std::string(outputFileName_plot).append(std::string(outputFileName, idx)).data());
  canvas->Print(std::string(outputFileName_plot).append(".png").data());
  //canvas->Print(std::string(outputFileName_plot).append(".pdf").data());
  //canvas->Print(std::string(outputFileName_plot).append(".root").data());
  
  delete legend;
  delete histogram2_div_ref;
  delete histogram3_div_ref;
  delete histogram4_div_ref;
  delete histogram5_div_ref;
  delete histogram6_div_ref;
  delete topPad;
  delete bottomPad;
  delete canvas;  
}

void compareDatacards_hh_2lss_fakes_mc()
{
  gROOT->SetBatch(true);

  TH1::AddDirectory(false);

  std::string inputFilePath_tight       = "/hdfs/local/ssawant/hhAnalysis/2016/20210129_hh_2lss_0tau_2016_Datacards_wUpdatedZveto_3/histograms/hh_2lss/Tight_SS/hadd/";
  std::string inputFileName_tight       = "hadd_stage2_Tight_SS.root";
  std::string directoryName_tight       = "hh_2lss_SS_Tight/";
  std::string legendEntry_tight         = "Tight";

  std::string inputFilePath_fakeable    = "/hdfs/local/ssawant/hhAnalysis/2016/20210129_hh_2lss_0tau_2016_Datacards_wUpdatedZveto_3/histograms/hh_2lss/Fakeable_wFakeRateWeights_SS/hadd/";
  std::string inputFileName_fakeable    = "hadd_stage2_Fakeable_wFakeRateWeights_SS.root";
  std::string directoryName_fakeable    = "hh_2lss_SS_Fakeable_wFakeRateWeights/";
  std::string legendEntry_fakeable      = "Fakeable";

  std::string inputFilePath_mcClosure_m = "/hdfs/local/ssawant/hhAnalysis/2016/20210129_hh_2lss_0tau_2016_Datacards_wUpdatedZveto_3/histograms/hh_2lss/Fakeable_mcClosure_m_wFakeRateWeights_SS/hadd/";
  std::string inputFileName_mcClosure_m = "hadd_stage2_Fakeable_mcClosure_m_wFakeRateWeights_SS.root";
  std::string directoryName_mcClosure_m = "hh_2lss_SS_Fakeable_mcClosure_m_wFakeRateWeights/";
  std::string legendEntry_mcClosure_m   = "mcClosure_m";

  std::string inputFilePath_mcClosure_e = "/hdfs/local/ssawant/hhAnalysis/2016/20210129_hh_2lss_0tau_2016_Datacards_wUpdatedZveto_3/histograms/hh_2lss/Fakeable_mcClosure_e_wFakeRateWeights_SS/hadd/";
  std::string inputFileName_mcClosure_e = "hadd_stage2_Fakeable_mcClosure_e_wFakeRateWeights_SS.root";
  std::string directoryName_mcClosure_e = "hh_2lss_SS_Fakeable_mcClosure_e_wFakeRateWeights/";
  std::string legendEntry_mcClosure_e   = "mcClosure_e";

  std::vector<std::string> processes_fakeable;
  processes_fakeable.push_back("TTH_fake");
  processes_fakeable.push_back("tHq_fake");
  processes_fakeable.push_back("tHW_fake");
  processes_fakeable.push_back("ggH_fake");
  processes_fakeable.push_back("qqH_fake");
  processes_fakeable.push_back("TTZ_fake");
  processes_fakeable.push_back("TTW_fake");
  processes_fakeable.push_back("TTWW_fake");
  processes_fakeable.push_back("TT_fake");
  processes_fakeable.push_back("Other_fake");
  processes_fakeable.push_back("XGamma_fake");
  processes_fakeable.push_back("ZH_fake");
  processes_fakeable.push_back("DY_fake");
  processes_fakeable.push_back("W_fake");
  processes_fakeable.push_back("WW_fake");
  processes_fakeable.push_back("WZ_fake");
  processes_fakeable.push_back("qqZZ_fake");
  processes_fakeable.push_back("ggZZ_fake");
  processes_fakeable.push_back("WH_fake");

  std::vector<std::string> histogramNames;
  histogramNames.push_back("sel/datacard/%s/MVAOutput_SM");
  histogramNames.push_back("sel/evt/%s/numElectrons");
  histogramNames.push_back("sel/evt/%s/numMuons");
  histogramNames.push_back("sel/evt/%s/leptonPairMass");

  std::map<std::string, std::string> xAxisTitles; // key = histogramName
  xAxisTitles["sel/datacard/%s/MVAOutput_SM"] = "BDT Output";
  xAxisTitles["sel/evt/%s/numElectrons"]      = "Num_{e}";
  xAxisTitles["sel/evt/%s/numMuons"]          = "Num_{#mu}";
  xAxisTitles["sel/evt/%s/leptonPairMass"]    = "m_{#ell#ell} [GeV]";

  std::map<std::string, double> xMin; // key = histogramName
  xMin["sel/datacard/%s/MVAOutput_SM"] = 1.e0;
  xMin["sel/evt/%s/numElectrons"]      = 1.e1;
  xMin["sel/evt/%s/numMuons"]          = 1.e1;
  xMin["sel/evt/%s/leptonPairMass"]    = 1.e0;

  std::map<std::string, double> xMax; // key = histogramName
  xMax["sel/datacard/%s/MVAOutput_SM"] = 1.e+3;
  xMax["sel/evt/%s/numElectrons"]      = 1.e+4;
  xMax["sel/evt/%s/numMuons"]          = 1.e+4;
  xMax["sel/evt/%s/leptonPairMass"]    = 1.e+3;

  TFile* inputFile_tight       = openFile(inputFilePath_tight,       inputFileName_tight);
  TFile* inputFile_fakeable    = openFile(inputFilePath_fakeable,    inputFileName_fakeable);
  TFile* inputFile_mcClosure_m = openFile(inputFilePath_mcClosure_m, inputFileName_mcClosure_m);
  TFile* inputFile_mcClosure_e = openFile(inputFilePath_mcClosure_e, inputFileName_mcClosure_e);

  for ( std::vector<std::string>::const_iterator histogramName = histogramNames.begin();
        histogramName != histogramNames.end(); ++histogramName ) {

    TH1* histogram_tight = loadHistogram(inputFile_tight, directoryName_tight, Form(histogramName->data(), "fakes_mc"));

    TH1* histogram_fakeable    = nullptr;
    TH1* histogram_mcClosure_m = nullptr;
    TH1* histogram_mcClosure_e = nullptr;
    for ( std::vector<std::string>::const_iterator process = processes_fakeable.begin();
          process != processes_fakeable.end(); ++process ) {
      std::string histogramName_process = Form(histogramName->data(), process->data());

      TH1* histogram_fakeable_process = loadHistogram(inputFile_fakeable, directoryName_fakeable, histogramName_process);
      if ( histogram_fakeable ) {
        histogram_fakeable->Add(histogram_fakeable_process);
      } else {
        histogram_fakeable = (TH1*)histogram_fakeable_process->Clone("histogram_fakeable");
      }

      TH1* histogram_mcClosure_m_process = loadHistogram(inputFile_mcClosure_m, directoryName_mcClosure_m, histogramName_process);
      if ( histogram_mcClosure_m ) {
        histogram_mcClosure_m->Add(histogram_mcClosure_m_process);
      } else {
        histogram_mcClosure_m = (TH1*)histogram_mcClosure_m_process->Clone("histogram_mcClosure_m");
      }

      TH1* histogram_mcClosure_e_process = loadHistogram(inputFile_mcClosure_e, directoryName_mcClosure_e, histogramName_process);
      if ( histogram_mcClosure_e ) {
        histogram_mcClosure_e->Add(histogram_mcClosure_e_process);
      } else {
        histogram_mcClosure_e = (TH1*)histogram_mcClosure_e_process->Clone("histogram_mcClosure_e");
      }
    }
     
    //TH1* histogram_mcClosure_sum = (TH1*)histogram_mcClosure_m->Clone("histogram_mcClosure_sum");
    //histogram_mcClosure_sum->Add(histogram_mcClosure_e);

    std::string outputFileName_suffix;
    if      ( (*histogramName) == "sel/datacard/%s/MVAOutput_SM" ) outputFileName_suffix = "MVAOutput_SM";
    else if ( (*histogramName) == "sel/evt/%s/numElectrons"      ) outputFileName_suffix = "numElectrons";
    else if ( (*histogramName) == "sel/evt/%s/numMuons"          ) outputFileName_suffix = "numMuons";
    else if ( (*histogramName) == "sel/evt/%s/leptonPairMass"    ) outputFileName_suffix = "leptonPairMass";
    else assert(0);
    std::string outputFileName = Form("compareDatacards_hh_2lss_fakes_mc_%s.png", outputFileName_suffix.data());
    showHistograms(800, 900, 
	   	   histogram_tight,         legendEntry_tight,       compIntegral(histogram_tight),
		   histogram_fakeable,      legendEntry_fakeable,    compIntegral(histogram_fakeable),
                   histogram_mcClosure_m,   legendEntry_mcClosure_m, compIntegral(histogram_mcClosure_m),
                   histogram_mcClosure_e,   legendEntry_mcClosure_e, compIntegral(histogram_mcClosure_e),
                   //histogram_mcClosure_sum, "mcClosure_sum",         compIntegral(histogram_mcClosure_sum),
		   NULL, "", 0.,
		   NULL, "", 0.,
                   xAxisTitles[*histogramName], 1.10,
		   true, xMin[*histogramName], xMax[*histogramName], Form("dN/d%s", xAxisTitles[*histogramName].data()), 1.30,
		   0.34, 0.72,
		   outputFileName.data());

    delete histogram_mcClosure_m;
    delete histogram_mcClosure_e;
    //delete histogram_mcClosure_sum;
  }

  delete inputFile_tight;
  delete inputFile_fakeable;
  delete inputFile_mcClosure_m;
  delete inputFile_mcClosure_e;
}

