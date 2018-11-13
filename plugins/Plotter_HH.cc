#include "hhAnalysis/multilepton/plugins/Plotter_HH.h"

#include <TH1.h>
#include <THStack.h>
#include <TMath.h>
#include <TString.h> // Form
#include <TCanvas.h>
#include <TPad.h>
#include <TLegend.h>
#include <TPaveText.h>
#include <TF1.h>
#include <TStyle.h>
#include <TROOT.h> // gROOT (needed to (re)define colors)

Plotter_HH::Plotter_HH(const TFile* inputFile, const edm::ParameterSet& cfg)
  : Plotter(inputFile, cfg)
{
  scaleSignal_ = cfg.getParameter<double>("scaleSignal");
  legendEntrySignal_ = cfg.getParameter<std::string>("legendEntrySignal");
}

Plotter_HH::~Plotter_HH()
{}

void Plotter_HH::makePlot(double canvasSizeX, double canvasSizeY,
			  TH1* histogramData, TH1* histogramData_blinded,
			  std::vector<histogramEntryType*>& histogramsBackground, 	
			  TH1* histogramSignal,
			  TH1* histogramUncertainty,
			  double legendTextSize, double legendPosX, double legendPosY, double legendSizeX, double legendSizeY, 
			  const std::string& labelOnTop,
			  std::vector<std::string>& extraLabels, double labelTextSize,
			  double labelPosX, double labelPosY, double labelSizeX, double labelSizeY,
			  double xMin, double xMax, const std::string& xAxisTitle, double xAxisOffset,
			  bool useLogScale, double yMin, double yMax, const std::string& yAxisTitle, double yAxisOffset,
			  const std::string& outputFileName, 
			  bool isRebinned, 
			  bool divideByBinWidth)
{
  std::cout << "<Plotter_HH::makePlot>:" << std::endl;
  std::cout << " outputFileName = " << outputFileName << std::endl;

  TH1* histogramData_density = 0;
  if ( histogramData ) {
    if  ( divideByBinWidth ) {
      histogramData_density = divideHistogramByBinWidth(histogramData);      
    } else {
      std::string histogramNameData_density = Form("%s_NotDivided", histogramData->GetName());	
      histogramData_density = (TH1*)histogramData->Clone(histogramNameData_density.data());
    }
  }
  
  TH1* histogramData_blinded_density = 0;
  if ( histogramData_blinded ) {
    if ( histogramData ) checkCompatibleBinning(histogramData_blinded, histogramData);
    if ( divideByBinWidth ) {
      histogramData_blinded_density = divideHistogramByBinWidth(histogramData_blinded);
    } else {
      std::string histogramNameData_blinded_density = Form("%s_NotDivide", histogramData_blinded->GetName());
      histogramData_blinded_density = (TH1*)histogramData_blinded->Clone(histogramNameData_blinded_density.data());
    }
  }
  
  std::vector<TH1*> histogramsBackground_density;
  TH1* histogramDY = 0;
  TH1* histogramDY_density = 0;
  TH1* histogramW = 0;
  TH1* histogramW_density = 0;
  TH1* histogramZZ = 0;
  TH1* histogramZZ_density = 0;
  TH1* histogramWZ = 0;
  TH1* histogramWZ_density = 0;
  TH1* histogramWW = 0;
  TH1* histogramWW_density = 0;
  TH1* histogramFakes = 0;
  TH1* histogramFakes_density = 0;
  TH1* histogramFlips = 0;
  TH1* histogramFlips_density = 0;
  TH1* histogramTT = 0;
  TH1* histogramTT_density = 0;
  TH1* histogramTTW = 0;
  TH1* histogramTTW_density = 0;
  TH1* histogramTTWW = 0;
  TH1* histogramTTWW_density = 0;
  TH1* histogramTTZ = 0;
  TH1* histogramTTZ_density = 0;
  TH1* histogramConversions = 0;
  TH1* histogramConversions_density = 0;
  TH1* histogramOther = 0;
  TH1* histogramOther_density = 0;
  TH1* histogramVH = 0;
  TH1* histogramVH_density = 0;
  TH1* histogramTTH = 0;
  TH1* histogramTTH_density = 0;
  TH1* histogramTH = 0;
  TH1* histogramTH_density = 0;
  for ( std::vector<histogramEntryType*>::iterator histogramBackground_entry = histogramsBackground.begin();
	histogramBackground_entry != histogramsBackground.end(); ++histogramBackground_entry ) {
    std::string histogramNameBackground = Form("%s_", (*histogramBackground_entry)->histogram_->GetName());
    TH1* histogramBackground = (TH1*)(*histogramBackground_entry)->histogram_->Clone(histogramNameBackground.data());
    const std::string& process = (*histogramBackground_entry)->process_;
    //      std::cout << "process = " << process << ": histogramBackground = " << histogramBackground << std::endl;
    //printHistogram(histogramBackground);
    checkCompatibleBinning(histogramBackground, histogramData);
    TH1* histogramBackground_density ;
    if ( divideByBinWidth ) {
      histogramBackground_density = divideHistogramByBinWidth(histogramBackground); 
    } else {
      std::string histogramNameBackground_density = Form("%s_NotDivided", histogramBackground->GetName());
      histogramBackground_density = (TH1*)histogramBackground->Clone(histogramNameBackground_density.data());
    }
    if ( process.find("TTWW") != std::string::npos ) {
      histogramTTWW = histogramBackground;
      histogramTTWW_density = histogramBackground_density;
    } else if ( process.find("TTW") != std::string::npos ) {
      histogramTTW = histogramBackground;
      histogramTTW_density = histogramBackground_density;
    } else if ( process.find("TTZ") != std::string::npos ) {
      histogramTTZ = histogramBackground;
      histogramTTZ_density = histogramBackground_density;
    } else if ( process.find("TTH") != std::string::npos ) {
      histogramTTH = histogramBackground;
      histogramTTH_density = histogramBackground_density;
    } else if ( process.find("TH") != std::string::npos ) {
      histogramTH = histogramBackground;
      histogramTH_density = histogramBackground_density;
    } else if ( process.find("TT") != std::string::npos ) {
      histogramTT = histogramBackground;
      histogramTT_density = histogramBackground_density;
    } else if ( process.find("Other") != std::string::npos ) {
      histogramOther = histogramBackground;
      histogramOther_density = histogramBackground_density;
    } else if ( process.find("Conversions") != std::string::npos || process.find("conversions") != std::string::npos ) {
      histogramConversions = histogramBackground;
      histogramConversions_density = histogramBackground_density;
    } else if ( process.find("Fakes") != std::string::npos || process.find("fakes") != std::string::npos ) {
      histogramFakes = histogramBackground;
      histogramFakes_density = histogramBackground_density;
    } else if ( process.find("VH") != std::string::npos ) {
      histogramVH = histogramBackground;
      histogramVH_density = histogramBackground_density;
    } else if ( process.find("ZZ") != std::string::npos ) {
      histogramZZ = histogramBackground;
      histogramZZ_density = histogramBackground_density;
    } else if ( process.find("WZ") != std::string::npos ) {
      histogramWZ = histogramBackground;
      histogramWZ_density = histogramBackground_density;
    } else if ( process.find("WW") != std::string::npos ) {
      histogramWW = histogramBackground;
      histogramWW_density = histogramBackground_density;
    }else if ( process.find("DY") != std::string::npos ) {
      histogramDY = histogramBackground;
      histogramDY_density = histogramBackground_density;
    }else if ( process.find("W") != std::string::npos ) {
      histogramW = histogramBackground;
      histogramW_density = histogramBackground_density;
    }else if ( process.find("Flips") != std::string::npos || process.find("flips") != std::string::npos ) {
      histogramFlips = histogramBackground;
      histogramFlips_density = histogramBackground_density;
    }
    histogramsBackground_density.push_back(histogramBackground_density);
  }
  
  TH1* histogramSignal_density = 0;
  if ( histogramSignal ) {
    if ( histogramSignal ) checkCompatibleBinning(histogramSignal, histogramData);
    if ( divideByBinWidth ) {
      histogramSignal_density = divideHistogramByBinWidth(histogramSignal); 
    } else {
      std::string histogramNameSignal_density = Form("%s_NotDivided",histogramSignal->GetName());
      histogramSignal_density = (TH1*)histogramSignal->Clone(histogramNameSignal_density.data());
    }
    if ( scaleSignal_ > 0. ) histogramSignal_density->Scale(scaleSignal_);
  }
  
  TH1* histogramSum_density = 0;
  std::vector<TH1*> histogramsSignal_and_Background_density = histogramsBackground_density;
  if ( histogramSignal_density ) histogramsSignal_and_Background_density.push_back(histogramSignal_density);
  for ( std::vector<TH1*>::iterator histogram_density = histogramsSignal_and_Background_density.begin();
	histogram_density != histogramsSignal_and_Background_density.end(); ++histogram_density ) {
    if ( !histogramSum_density ) histogramSum_density = (TH1*)(*histogram_density)->Clone("histogramSum_density"); // CV: used for y-axis normalization only
    else histogramSum_density->Add(*histogram_density);
  }
  assert(histogramSum_density);
  
  TH1* histogramUncertainty_density = 0;
  if ( histogramUncertainty ) {
    if ( histogramData ) checkCompatibleBinning(histogramUncertainty, histogramData);
    if ( divideByBinWidth ) {
      histogramUncertainty_density = divideHistogramByBinWidth(histogramUncertainty);
    } else {
      std::string histogramNameUncertainty_density = Form("%s_NotDivided",histogramUncertainty->GetName());
      histogramUncertainty_density = (TH1*)histogramUncertainty->Clone(histogramNameUncertainty_density.data());
    }
  }

  //---------------------------------------------------------------------------
  // CV: sum ZZ, WZ, and WW backgrounds
  assert(histogramZZ && histogramZZ_density && histogramWZ && histogramWZ_density && histogramWW && histogramWW_density);
  histogramZZ->Add(histogramWZ);
  histogramZZ_density->Add(histogramWZ_density);
  histogramZZ->Add(histogramWW);
  histogramZZ_density->Add(histogramWW_density);
  //---------------------------------------------------------------------------
  
  //---------------------------------------------------------------------------
  // CV: sum tt+jets, ttW, ttWW, and ttZ backgrounds
  assert(histogramTTZ && histogramTTZ_density && histogramTT && histogramTT_density && histogramTTW && histogramTTW_density && histogramTTWW && histogramTTWW_density);
  histogramTTZ->Add(histogramTT);
  histogramTTZ_density->Add(histogramTT_density);
  histogramTTZ->Add(histogramTTW);
  histogramTTZ_density->Add(histogramTTW_density);
  histogramTTZ->Add(histogramTTWW);
  histogramTTZ_density->Add(histogramTTWW_density);
  //---------------------------------------------------------------------------
  
  //---------------------------------------------------------------------------
  // CV: sum SM (single) Higgs backgrounds
  assert(histogramVH && histogramVH_density && histogramTTH && histogramTTH_density && histogramTH && histogramTH_density);
  histogramVH->Add(histogramTTH);
  histogramVH_density->Add(histogramTTH_density);
  histogramVH->Add(histogramTH);
  histogramVH_density->Add(histogramTH_density);
  //---------------------------------------------------------------------------

  //---------------------------------------------------------------------------   
  //SB: W+jets added to Other
  assert(histogramOther && histogramOther_density && histogramW && histogramW_density);
  histogramOther->Add(histogramW);
  histogramOther_density->Add(histogramW_density);
  //---------------------------------------------------------------------------   

  TCanvas* canvas = new TCanvas("canvas", "", canvasSizeX, canvasSizeY);
  canvas->SetFillColor(10);
  canvas->SetFillStyle(4000);
  canvas->SetFillColor(10);
  canvas->SetTicky();
  canvas->SetBorderSize(2);
  canvas->SetLeftMargin(0.12);
  canvas->SetBottomMargin(0.12);
  
  TPad* topPad = new TPad("topPad", "topPad", 0.00, 0.35, 1.00, 1.00);
  topPad->SetFillColor(10);
  topPad->SetTopMargin(0.055);
  topPad->SetLeftMargin(0.15);
  topPad->SetBottomMargin(0.03);
  topPad->SetRightMargin(0.05);
  topPad->SetLogy(useLogScale);
  
  TPad* bottomPad = new TPad("bottomPad", "bottomPad", 0.00, 0.00, 1.00, 0.35);
  bottomPad->SetFillColor(10);
  bottomPad->SetTopMargin(0.02);
  bottomPad->SetLeftMargin(0.15);
  bottomPad->SetBottomMargin(0.31);
  bottomPad->SetRightMargin(0.05);
  bottomPad->SetLogy(false);
  
  canvas->cd();
  topPad->Draw();
  topPad->cd();
  
  TAxis* xAxis_top = 0;
  if ( histogramData_blinded_density ) xAxis_top = histogramData_blinded_density->GetXaxis();
  else xAxis_top = histogramSum_density->GetXaxis();
  if ( xMin >= 0. && xMax > xMin ) xAxis_top->SetRangeUser(xMin, xMax);
  xAxis_top->SetTitle(xAxisTitle.data());
  xAxis_top->SetTitleOffset(xAxisOffset);
  xAxis_top->SetLabelColor(10);
  xAxis_top->SetTitleColor(10);
  
  TAxis* yAxis_top = 0;
  if ( histogramData_blinded_density ) yAxis_top = histogramData_blinded_density->GetYaxis();
  else yAxis_top = histogramSum_density->GetYaxis();
  yAxis_top->SetTitle(yAxisTitle.data());
  yAxis_top->SetTitleOffset(yAxisOffset);
  yAxis_top->SetTitleSize(0.065);
  yAxis_top->SetLabelSize(0.05);
  yAxis_top->SetTickLength(0.04);  
  
  TLegend* legend = new TLegend(legendPosX, legendPosY, legendPosX + legendSizeX, legendPosY + legendSizeY, NULL, "brNDC");
  legend->SetFillStyle(0);
  legend->SetBorderSize(0);
  legend->SetFillColor(10);
  legend->SetTextSize(legendTextSize);

  printf("Plotter_HH:: Before  yMin: %f,  yMax: %f\n",yMin,yMax);
  if ( !(yMin >= 0. && yMax > yMin) ) {
    for ( int i = 0; i < 3; ++i ) {
      TH1* histogram_i = nullptr;
      if      ( i == 0 ) histogram_i = histogramData_density;
      else if ( i == 1 ) histogram_i = histogramSum_density;
      else if ( i == 2 ) histogram_i = histogramSignal_density;
      else assert(0);
      double numOrdersOfMagnitude;
      if ( useLogScale ) numOrdersOfMagnitude = 4.5;
      else numOrdersOfMagnitude = -1.;
      if ( histogram_i ) {
	std::pair<double, double> yMin_and_yMax = compYmin_and_YmaxForClearance(histogram_i, legendPosX, legendPosY, labelPosY, useLogScale, numOrdersOfMagnitude);
	if ( yMin_and_yMax.second > yMax || i == 0 ) {
	  yMin = yMin_and_yMax.first;
	  yMax = yMin_and_yMax.second;
	}
      } else if ( i == 0 ) {
	if ( useLogScale ) yMin = TMath::Power(10., -numOrdersOfMagnitude);
	else yMin = 0.;
	yMax = 1.;
      }
    }
  }
  printf("Plotter_HH:: After  yMin: %f,  yMax: %f\n",yMin,yMax);
  
  if ( histogramData_blinded_density ) {
    histogramData_blinded_density->SetTitle("");
    histogramData_blinded_density->SetStats(false);
    histogramData_blinded_density->SetMaximum(yMax);
    histogramData_blinded_density->SetMinimum(yMin);
    histogramData_blinded_density->SetMarkerStyle(20);
    int markerSize = ( histogramData_blinded_density->GetNbinsX() < 40 ) ? 2 : 1;
    histogramData_blinded_density->SetMarkerSize(markerSize);
    histogramData_blinded_density->SetMarkerColor(kBlack);
    histogramData_blinded_density->SetLineColor(kBlack);
    legend->AddEntry(histogramData_blinded_density, "observed", "p");
    histogramData_blinded_density->Draw("ep");
  }
  /*color used for tth
  const int color_ttW         = 823; // dark green 
  const int color_ttZ         = 822; // light green
  const int color_ttH         = 628; // red  
  const int color_ttjets      =  16; // gray
  const int color_EWK         = 610; // purple 
  const int color_Diboson     = 634; // dark red 
  const int color_WZ          = 634; // dark red 
  const int color_Rares       = 851; // light blue 
  const int color_Conversions = 800; // yellow/orange
  const int color_Fakes       =   1; // black
  const int color_Flips       =   1; // black
*/
  
  const int color_DY          = 610; // purple
  const int color_ZZ          = 634; // dark red
  const int color_Fakes       =   1; // black
  const int color_ttZ         = 822; // light green
  const int color_Conversions = 800; // yellow/orange
  const int color_VH          = 628; // red
  const int color_Other       = 851; // light blue
  const int color_Flips       = 1; // black

  const std::string legendEntry_DY          = "DY";
  const std::string legendEntry_ZZ          = "Diboson";
  const std::string legendEntry_Fakes       = "Fakes";
  const std::string legendEntry_ttZ         = "t#bar{t} + t#bar{t}V(V)";
  const std::string legendEntry_Conversions = "Conversions";
  const std::string legendEntry_VH          = "SM Higgs bosons";
  const std::string legendEntry_Other       = "Other";
  const std::string legendEntry_Flips       = "Flips";
  
  std::vector<TH1*> histogramsForStack_density;
  if ( histogramDY_density ) {
    histogramDY_density->SetFillColor(color_DY);
    histogramsForStack_density.push_back(histogramDY_density);
    legend->AddEntry(histogramDY_density, legendEntry_DY.data(), "f");
  }
  if ( histogramZZ_density ) {
    histogramZZ_density->SetFillColor(color_ZZ);
    histogramsForStack_density.push_back(histogramZZ_density);
    legend->AddEntry(histogramZZ_density, legendEntry_ZZ.data(), "f");
  }
  if ( histogramFakes_density ) {
    histogramFakes_density->SetFillColor(color_Fakes);
    histogramFakes_density->SetFillStyle(3005); // stripes extending from top left to bottom right
    histogramsForStack_density.push_back(histogramFakes_density);
    legend->AddEntry(histogramFakes_density, legendEntry_Fakes.data(), "f");
  }
  if ( histogramTTZ_density ) {
    histogramTTZ_density->SetFillColor(color_ttZ);
    histogramsForStack_density.push_back(histogramTTZ_density);
    legend->AddEntry(histogramTTZ_density, legendEntry_ttZ.data(), "f");
  } 
  if ( histogramConversions_density ) {
    histogramConversions_density->SetFillColor(color_Conversions);
    histogramsForStack_density.push_back(histogramConversions_density);
    legend->AddEntry(histogramConversions_density, legendEntry_Conversions.data(), "f");
  }
  if ( histogramVH_density ) {
    histogramVH_density->SetFillColor(color_VH);
    histogramsForStack_density.push_back(histogramVH_density);
    legend->AddEntry(histogramVH_density, legendEntry_VH.data(), "f");
  }
  if ( histogramOther_density ) {
    histogramOther_density->SetFillColor(color_Other);
    histogramsForStack_density.push_back(histogramOther_density);
    legend->AddEntry(histogramOther_density, legendEntry_Other.data(), "f");
  }
  if ( histogramFlips_density ) {
    histogramFlips_density->SetFillColor(color_Flips);
    histogramsForStack_density.push_back(histogramFlips_density);
    legend->AddEntry(histogramFlips_density, legendEntry_Flips.data(), "f");
  }
  // CV: add histograms to THStack in "reverse" order, so that ZZ background is drawn on top
  THStack* histogramStack_density = new THStack("stack", "");
  for ( std::vector<TH1*>::reverse_iterator histogram_density = histogramsForStack_density.rbegin(); 
	histogram_density != histogramsForStack_density.rend(); ++histogram_density ) {
    histogramStack_density->Add(*histogram_density);
  }
  if ( histogramData_blinded_density ) histogramStack_density->Draw("histsame");
  else histogramStack_density->Draw("hist");
  std::string histogramNameBkg_bins = Form("%s_bins", histogramData_blinded_density->GetName());
  TH1* histogramBkg_bins = (TH1*)histogramData_blinded_density->Clone(histogramNameBkg_bins.data());
  int numBins_top = histogramBkg_bins->GetNbinsX();
  for ( int iBin = 1; iBin <= numBins_top; ++iBin ) {
    double sumBinContents = 0.;
    if ( histogramDY_density          ) sumBinContents += histogramDY_density->GetBinContent(iBin);
    if ( histogramZZ_density          ) sumBinContents += histogramZZ_density->GetBinContent(iBin);
    if ( histogramFakes_density       ) sumBinContents += histogramFakes_density->GetBinContent(iBin);
    if ( histogramTTZ_density         ) sumBinContents += histogramTTZ_density->GetBinContent(iBin);
    if ( histogramConversions_density ) sumBinContents += histogramConversions_density->GetBinContent(iBin);
    if ( histogramVH_density          ) sumBinContents += histogramVH_density->GetBinContent(iBin);
    if ( histogramOther_density       ) sumBinContents += histogramOther_density->GetBinContent(iBin);
    if ( histogramFlips_density       ) sumBinContents += histogramFlips_density->GetBinContent(iBin);
    if ( histogramUncertainty_density ) histogramUncertainty_density->SetBinContent(iBin, sumBinContents);
    histogramBkg_bins->SetBinContent(iBin, sumBinContents);
  }
  if ( histogramUncertainty_density ) {
    histogramUncertainty_density->SetFillColor(kBlack);
    histogramUncertainty_density->SetFillStyle(3344);    
    histogramUncertainty_density->Draw("e2same");
    legend->AddEntry(histogramUncertainty_density, "Uncertainty", "f");
  }

  if ( histogramSignal_density ) {      
    histogramSignal_density->SetLineWidth(2);
    histogramSignal_density->SetLineStyle(kDashed);
    histogramSignal_density->SetLineColor(kBlue);
    histogramSignal_density->Draw("histsame");
    legend->AddEntry(histogramSignal_density, legendEntrySignal_.data(), "l");
  }

  if ( histogramData_blinded_density ) {
    std::string histogramNameData_blinded_bins = Form("%s_bins", histogramData_blinded_density->GetName());
    TH1* histogramData_blinded_bins = (TH1*)histogramData_blinded_density->Clone(histogramNameData_blinded_bins.data());
    int numBins = histogramData_blinded_density->GetNbinsX();
    for ( int iBin = 1; iBin <= numBins; ++iBin ) {
      double iData = histogramData_blinded_density->GetBinContent(iBin);
      double iBkg = histogramBkg_bins->GetBinContent(iBin);
      if ( iData == -10 ){
	histogramData_blinded_bins->SetBinContent(iBin, (iBkg+0.2*iBkg));
      } else{
	histogramData_blinded_bins->SetBinContent(iBin, yMin);
      }
    }
    const int color_int = 12;
    const double alpha = 0.40;
    TColor* color = gROOT->GetColor(color_int);
    static int newColor_int = -1;
    static TColor* newColor = 0;
    if ( !newColor ) {
      newColor_int = gROOT->GetListOfColors()->GetSize() + 1;
      newColor = new TColor(newColor_int, color->GetRed(), color->GetGreen(), color->GetBlue(), "", alpha);
    }
    histogramData_blinded_bins->SetLineColor(newColor_int);
    histogramData_blinded_bins->SetLineWidth(0);
    histogramData_blinded_bins->SetFillColor(newColor_int);
    histogramData_blinded_bins->SetFillStyle(1001);
    
    histogramData_blinded_bins->Draw("histsame");
    legend->AddEntry(histogramData_blinded_bins, "blinded", "f");
  }
  
  if ( histogramData_blinded_density ) {
    histogramData_blinded_density->Draw("epsame");
    histogramData_blinded_density->Draw("axissame");
  }
  
  legend->Draw();
  
  TPaveText* labelOnTop_pave = 0;
  if ( labelOnTop != "" ) {
    labelOnTop_pave = new TPaveText(0.165, 0.95, 0.61, 1.00, "brNDC");
    labelOnTop_pave->AddText(labelOnTop.data());
    labelOnTop_pave->SetFillColor(10);
    labelOnTop_pave->SetBorderSize(0);
    labelOnTop_pave->SetTextColor(1);
    labelOnTop_pave->SetTextAlign(12);
    labelOnTop_pave->SetTextSize(0.045);
    labelOnTop_pave->Draw();
  }
  TPaveText* extraLabels_pave = 0;
  if ( extraLabels.size() > 0 ) {
    extraLabels_pave = new TPaveText(labelPosX, labelPosY, labelPosX + labelSizeX, labelPosY + labelSizeY, "brNDC");
    for ( std::vector<std::string>::const_iterator extraLabel = extraLabels.begin();
	  extraLabel != extraLabels.end(); ++extraLabel ) {
      extraLabels_pave->AddText(extraLabel->data());
    }
    extraLabels_pave->SetFillColor(10);
    extraLabels_pave->SetBorderSize(0);
    extraLabels_pave->SetTextColor(1);
    extraLabels_pave->SetTextAlign(12);
    extraLabels_pave->SetTextSize(labelTextSize);
    extraLabels_pave->Draw();
  }
  
  canvas->cd();
  bottomPad->Draw();
  bottomPad->cd();
  
  TH1* histogramSum = 0;
  TH1* histogramRatio = 0;
  TH1* histogramRatioUncertainty = 0;
  TF1* line = 0;
  if ( histogramData && histogramData_blinded ) {
    histogramSum = (TH1*)histogramData->Clone("histogramSum");
    histogramSum->Reset();
    if ( !histogramSum->GetSumw2N() ) histogramSum->Sumw2();
    if ( histogramDY          ) histogramSum->Add(histogramDY);
    if ( histogramZZ          ) histogramSum->Add(histogramZZ);
    if ( histogramFakes       ) histogramSum->Add(histogramFakes);
    if ( histogramTTZ         ) histogramSum->Add(histogramTTZ);
    if ( histogramConversions ) histogramSum->Add(histogramConversions);
    if ( histogramVH          ) histogramSum->Add(histogramVH);
    if ( histogramOther       ) histogramSum->Add(histogramOther);
    if ( histogramFlips       ) histogramSum->Add(histogramFlips);
    histogramRatio = (TH1*)histogramData->Clone("histogramRatio");
    histogramRatio->Reset();
    if ( !histogramRatio->GetSumw2N() ) histogramRatio->Sumw2();
    checkCompatibleBinning(histogramRatio, histogramSum);
    histogramRatio->Divide(histogramData, histogramSum);
    int numBins_bottom = histogramRatio->GetNbinsX();
    for ( int iBin = 1; iBin <= numBins_bottom; ++iBin ) {
      double binContent = histogramRatio->GetBinContent(iBin);
      if ( histogramData_blinded && histogramData_blinded->GetBinContent(iBin) >= 0. ) histogramRatio->SetBinContent(iBin, binContent - 1.0);
      else histogramRatio->SetBinContent(iBin, -10.);
      //std::cout << " bin #" << iBin << " (x = " << histogramRatio->GetBinCenter(iBin) << "): ratio = " << histogramRatio->GetBinContent(iBin) << std::endl;
    }
    
    histogramRatio->SetTitle("");
    histogramRatio->SetStats(false);
    histogramRatio->SetMinimum(-0.50);
    histogramRatio->SetMaximum(+0.50);
    histogramRatio->SetMarkerStyle(histogramData_blinded_density->GetMarkerStyle());
    histogramRatio->SetMarkerSize(histogramData_blinded_density->GetMarkerSize());
    histogramRatio->SetMarkerColor(histogramData_blinded_density->GetMarkerColor());
    histogramRatio->SetLineColor(histogramData_blinded_density->GetLineColor());
    
    TAxis* xAxis_bottom = histogramRatio->GetXaxis();
    if ( xMin >= 0. && xMax > xMin ) xAxis_bottom->SetRangeUser(xMin, xMax);
    xAxis_bottom->SetTitle(xAxis_top->GetTitle());
    xAxis_bottom->SetLabelColor(1);
    xAxis_bottom->SetTitleColor(1);
    xAxis_bottom->SetTitleOffset(1.20);
    xAxis_bottom->SetTitleSize(0.12);
    xAxis_bottom->SetLabelOffset(0.02);
    xAxis_bottom->SetLabelSize(0.10);
    xAxis_bottom->SetTickLength(0.055);
    
    TAxis* yAxis_bottom = histogramRatio->GetYaxis();
    yAxis_bottom->SetTitle("#frac{Data - Simulation}{Simulation}");
    yAxis_bottom->SetTitleOffset(0.80);
    yAxis_bottom->SetNdivisions(505);
    yAxis_bottom->CenterTitle();
    yAxis_bottom->SetTitleSize(0.09);
    yAxis_bottom->SetLabelSize(0.10);
    yAxis_bottom->SetTickLength(0.04);  
    
    if ( histogramUncertainty ) {
      histogramRatioUncertainty = (TH1*)histogramUncertainty->Clone("histogramRatioUncertainty");
      if ( !histogramRatioUncertainty->GetSumw2N() ) histogramRatioUncertainty->Sumw2();
      checkCompatibleBinning(histogramRatioUncertainty, histogramSum);
      histogramRatioUncertainty->Divide(histogramSum);
      int numBins = histogramRatioUncertainty->GetNbinsX();
      for ( int iBin = 1; iBin <= numBins; ++iBin ) {
	double binContent = histogramRatioUncertainty->GetBinContent(iBin);
	histogramRatioUncertainty->SetBinContent(iBin, binContent - 1.0);
      }
      histogramRatioUncertainty->SetFillColor(histogramUncertainty_density->GetFillColor());
      //histogramRatioUncertainty->SetFillStyle(histogramUncertainty_density->GetFillStyle());    
      histogramRatioUncertainty->SetFillStyle(3644);    
    }
    histogramRatio->Draw("ep");
    
    line = new TF1("line","0", xAxis_bottom->GetXmin(), xAxis_bottom->GetXmax());
    line->SetLineStyle(3);
    line->SetLineWidth(1.5);
    line->SetLineColor(kBlack);
    line->Draw("same");
    
    if ( histogramRatioUncertainty ) {
      //printHistogram(histogramRatioUncertainty);
      histogramRatioUncertainty->Draw("e2same");
    }
    
    histogramRatio->Draw("epsame");
  }
  
  canvas->Update();
  size_t idx = outputFileName.find_last_of('.');
  std::string outputFileName_plot(outputFileName, 0, idx);
  if ( useLogScale ) outputFileName_plot.append("_log");
  else outputFileName_plot.append("_linear");
  if(isRebinned)outputFileName_plot.append("_rebinned");
  if ( idx != std::string::npos ) canvas->Print(std::string(outputFileName_plot).append(std::string(outputFileName, idx)).data());
  canvas->Print(std::string(outputFileName_plot).append(".png").data());
  canvas->Print(std::string(outputFileName_plot).append(".pdf").data());
  canvas->Print(std::string(outputFileName_plot).append(".root").data());
  
  delete histogramData_density;
  delete histogramData_blinded_density;
  delete histogramSignal_density;
  delete histogramDY;
  delete histogramDY_density;
  delete histogramZZ;
  delete histogramZZ_density;
  delete histogramW;
  delete histogramW_density;
  delete histogramWZ;
  delete histogramWZ_density;
  delete histogramWW;
  delete histogramWW_density;
  delete histogramFakes;
  delete histogramFakes_density;
  delete histogramTT;
  delete histogramTT_density;
  delete histogramTTW;
  delete histogramTTW_density;
  delete histogramTTWW;
  delete histogramTTWW_density;
  delete histogramTTZ;
  delete histogramTTZ_density;
  delete histogramConversions;
  delete histogramConversions_density;
  delete histogramOther;
  delete histogramOther_density;
  delete histogramVH;
  delete histogramVH_density;
  delete histogramTTH;
  delete histogramTTH_density;
  delete histogramTH;
  delete histogramTH_density;
  delete histogramFlips;
  delete histogramFlips_density;
  delete histogramSum_density;
  delete histogramUncertainty_density;
  delete legend;
  delete labelOnTop_pave;
  delete extraLabels_pave;
  delete topPad;
  delete histogramSum;
  delete histogramRatio;
  delete histogramRatioUncertainty;        
  delete line;
  delete bottomPad;    
  delete canvas;
}

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_EDM_PLUGIN(PlotterPluginFactory, Plotter_HH, "Plotter_HH");
