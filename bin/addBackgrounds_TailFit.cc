/** \executable addBackgrounds_TailFit
 *
 * Performs TailFits for backgrounds with low statistics in the tail regions 
 *
 * \author Ram Krishna Dewanjee, Tallinn
 *
 */

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/PythonParameterSet/interface/MakeParameterSets.h"

#include "FWCore/Utilities/interface/Exception.h"

#include "PhysicsTools/FWLite/interface/TFileService.h"
#include "DataFormats/FWLite/interface/InputSource.h"
#include "DataFormats/FWLite/interface/OutputFiles.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // compIntegral(), getTArraDfromVector()   
#include "tthAnalysis/HiggsToTauTau/interface/addBackgroundsAuxFunctions.h" // getSubdirectories
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()  
#include "tthAnalysis/HiggsToTauTau/interface/fitAuxFunctions.h" // EigenVector_and_Value, compEigenVectors_and_Values, fitFunction_and_legendEntry, makeControlPlot_fit  

#include "hhAnalysis/multilepton/interface/TailFitAuxFunctions.h" // Fit functions



#include <TFile.h>
#include <TH1.h>
#include <TBenchmark.h>
#include <TMath.h>
#include <TError.h> // gErrorAbortLevel, kError
#include <TDirectory.h>
#include <TList.h>
#include <TKey.h>
#include <TObject.h>
#include <TFitResult.h>
#include <TFitResultPtr.h>
#include <TArrayD.h>
#include <TROOT.h> // for gROOT
#include <TRint.h>
#include <TCanvas.h>
#include <TPad.h>


#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <assert.h>

typedef std::vector<std::string> vstring;
typedef std::vector<double> vdouble;


double square(double x)
{
  return x*x;
}

namespace
{
  struct FitFuncEntryType
  {
    FitFuncEntryType(const edm::ParameterSet& cfg, const TH1* histo, const std::string label)
    {	
      FitRange_           = cfg.getParameter<vdouble>("FitRange");
      FitParameters_      = cfg.getParameter<vdouble>("FitParameters");
      FitFunctionName_    = cfg.getParameter<std::string>("FitfuncName");
      Histo_to_fit_       = histo;
      Label_              = label;
      Fitfunc_ = 0;

      if(FitFunctionName_ == "CrystalBall"){ 
	Fitfunc_ = CrystalBall(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "Exponential"){ 
	Fitfunc_ = Exp(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "LegendrePolynomial3"){ 
	Fitfunc_ = Poly3(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "LegendrePolynomial2"){ 
	Fitfunc_ = Poly2(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "LegendrePolynomial1"){ 
	Fitfunc_ = Poly1(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "ExponentialErf"){ 
	Fitfunc_ = ExpErf(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "Gaussian"){ 
	Fitfunc_ = Gauss(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "DoubleGaussian"){ 
	Fitfunc_ = Gauss2(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "TripleGaussian"){ 
	Fitfunc_ = Gauss3(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "ExponentialGaussian"){ 
	Fitfunc_ = ExpGaus(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "DoubleExponentialGaussian"){ 
	Fitfunc_ = ExpGaus2(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "ErfExponentialGaussian"){ 
	Fitfunc_ = ErfExpGaus(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "DoubleErfExponentialGaussian"){ 
	Fitfunc_ = ErfExpGaus2(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "Voigt"){ 
	Fitfunc_ = Voigt(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else if(FitFunctionName_ == "DoubleGaussianVoigt"){ 
	Fitfunc_ = Gaus2Voigt(FitParameters_, FitRange_, Histo_to_fit_, Label_);
      }else {
	std::cerr<< " Wrong Function name !!! " << std::endl;
      }

    }
    ~FitFuncEntryType() {}
    vdouble FitRange_;
    vdouble FitParameters_;
    std::string FitFunctionName_;
    std::string Label_;
    TF1* Fitfunc_;
    const TH1* Histo_to_fit_;

    std::string GetFitFuncName(){
      return FitFunctionName_; 
    }


    TF1* GetFitFunction(){
      return Fitfunc_;
    }

    double GetXmin(){
      return FitRange_[0];
    }

    double GetXmax(){
      return FitRange_[1];
    }

    void SetParameter(){
      for(unsigned int i = 0; i < FitParameters_.size(); i++){    
	Fitfunc_->SetParameter(i, FitParameters_[i]);
      }
    }


  };
}







TH1* copyHistogram(const TH1* histogram_input, const std::string& histogramName_output, bool verbose)
{
  if ( verbose ) {
    std::cout << "<copyHistogram>:" << std::endl;
    std::cout << " histogram_input = " << histogram_input << ": name = " << histogram_input->GetName() << std::endl;
    std::cout << " histogramName_output = " << histogramName_output << std::endl;
  }
  TH1* histogram_output = 0;
  const TAxis* xAxis = histogram_input->GetXaxis();
  int numBins = xAxis->GetNbins();
  TArrayD binning = getBinning(histogram_input);
  if ( verbose ) {
    std::cout << " nBins = " << xAxis->GetNbins() << ",";
    std::cout << " binning = { ";
    for ( int idxBin = 0; idxBin < binning.GetSize(); ++idxBin ) {
      if ( idxBin > 0 ) std::cout << ", ";
      std::cout << binning[idxBin];
    }
    std::cout << " } " << std::endl;
  }
  histogram_output = new TH1D(histogramName_output.data(), histogram_input->GetTitle(), numBins, binning.GetArray());
  for ( int idxBin = 0; idxBin <= (numBins + 1); ++idxBin ) {
    double binContent = histogram_input->GetBinContent(idxBin);
    histogram_output->SetBinContent(idxBin, binContent);
    double binError = histogram_input->GetBinError(idxBin);
    histogram_output->SetBinError(idxBin, binError);
  }
  return histogram_output;
}

struct histogramEntryType
{
  histogramEntryType(const std::string& process, TH1* histogram)
    : process_(process)
    , histogram_(histogram)
  {}
  ~histogramEntryType() {}
  std::string process_;
  TH1* histogram_;
};

void processHistogram(
       const TFile* inputFile, 
       const TDirectory* dir_den, const TDirectory* dir_num, 
       const std::string& processData, const std::string& processLeptonFakes, const vstring& processesToSubtract, 
       const vstring& central_or_shifts, fwlite::TFileService& fs, const std::string& cat_num) 
{
  const TDirectory* dirData_den = getSubdirectory(dir_den, processData, false);
  if ( !dirData_den ) { 
    std::cout << "Failed to find subdirectory = '" << processData << "' within directory = '" << dir_den->GetPath() << "' !!" << std::endl; 
    return;
  }

  std::set<std::string> histograms;      
  TList* list = dirData_den->GetListOfKeys();
  TIter next(list); 
  TKey* key = 0;                                                                                                                                                                        
  while ( (key = dynamic_cast<TKey*>(next())) ) {        
    TObject* object = key->ReadObj(); 
    TH1* histogram = dynamic_cast<TH1*>(object);  
    if ( !histogram ) continue;
    TString histogramName = TString(histogram->GetName()).ReplaceAll(Form("%s_", processData.data()), "");  
    for ( vstring::const_iterator central_or_shift = central_or_shifts.begin();  
	  central_or_shift != central_or_shifts.end(); ++central_or_shift ) {   
      if ( !((*central_or_shift) == "" || (*central_or_shift) == "central") ) {
	histogramName = histogramName.ReplaceAll(Form("%s_", central_or_shift->data()), "");  
      }
    }
    if ( histogramName.Contains("CMS_") ) continue; 
    if ( histogramName.Contains("cutFlow") ) continue;
    if ( histograms.find(histogramName.Data()) == histograms.end() ) {   
      //std::cout << "adding histogram = " << histogramName.Data() << std::endl; 
      histograms.insert(histogramName.Data());
    }
  }

  for ( std::set<std::string>::const_iterator histogram = histograms.begin();
	histogram != histograms.end(); ++histogram ) {                                                                      
    std::cout << "processing histogram = " << (*histogram) << std::endl; 
    
    for ( vstring::const_iterator central_or_shift = central_or_shifts.begin();
	  central_or_shift != central_or_shifts.end(); ++central_or_shift ) {     
      
      //int verbosity = ( histogram->find("EventCounter") != std::string::npos && ((*central_or_shift) == "" || (*central_or_shift) == "central") ) ? 1 : 0;
      int verbosity = 0;
      
      TH1* histogramData_den = getHistogram(dir_den, processData, *histogram, *central_or_shift, false);  
      bool histogramData_den_isSubstitute = false;
      if ( !histogramData_den ) {
	histogramData_den = getHistogram(dir_den, processData, *histogram, "central", true);                                                                                         
	histogramData_den_isSubstitute = true;
      }                                                                                            
      if ( verbosity ) {
	std::cout << " Den. integral(data_obs) = " << histogramData_den->Integral() << std::endl;
      }                  

      TH1* histogramData_num = getHistogram(dir_num, processData, *histogram, *central_or_shift, false);                                                                             
      bool histogramData_num_isSubstitute = false;
      if ( !histogramData_num ) {                                                                                  
	histogramData_num = getHistogram(dir_num, processData, *histogram, "central", true);
	histogramData_num_isSubstitute = true;
      }
      if ( verbosity ) {   
	std::cout << " Num. integral(data_obs) = " << histogramData_num->Integral() << std::endl;  
      }

      std::vector<TH1*> histogramsToSubtract_den; 
      std::vector<histogramEntryType*> histograms_and_processesToSubtract_den; 
      std::vector<TH1*> histogramsToSubtract_num;  
      std::vector<histogramEntryType*> histograms_and_processesToSubtract_num;   
      for ( vstring::const_iterator processToSubtract = processesToSubtract.begin(); 
	    processToSubtract != processesToSubtract.end(); ++processToSubtract ) {
	TH1* histogramToSubtract_den = getHistogram(dir_den, *processToSubtract, *histogram, *central_or_shift, false);                                                        
	if ( !histogramToSubtract_den ) {
	  histogramToSubtract_den = getHistogram(dir_den, *processToSubtract, *histogram, "central", true);                                                
	}
	if ( verbosity ) {
	  std::cout << " Den. integral(" << (*processToSubtract) << ") = " << histogramToSubtract_den->Integral() << std::endl;                                                           
	} 
	histogramsToSubtract_den.push_back(histogramToSubtract_den); 
	histograms_and_processesToSubtract_den.push_back(new histogramEntryType(*processToSubtract, histogramToSubtract_den));   

	TH1* histogramToSubtract_num = getHistogram(dir_num, *processToSubtract, *histogram, *central_or_shift, false);                                                        
	if ( !histogramToSubtract_num ) {
	  histogramToSubtract_num = getHistogram(dir_num, *processToSubtract, *histogram, "central", true);                                                
	}
	if ( verbosity ) {
	  std::cout << " Num. integral(" << (*processToSubtract) << ") = " << histogramToSubtract_num->Integral() << std::endl;                                                        
	}
	histogramsToSubtract_num.push_back(histogramToSubtract_num); 
	histograms_and_processesToSubtract_num.push_back(new histogramEntryType(*processToSubtract, histogramToSubtract_num));  
      }                        

      TString subdirName_den_tstring = TString(dir_num->GetPath()).ReplaceAll("numerator", "denominator");
      subdirName_den_tstring = subdirName_den_tstring.ReplaceAll("tight", "fakeable");         
      std::string subdirName_den = subdirName_den_tstring.Data();
      size_t pos_den = subdirName_den.find(":/");
      assert(pos_den < (subdirName_den.length() - 2));
      subdirName_den = std::string(subdirName_den, pos_den + 2);

      TString subdirName_num_tstring = TString(dir_num->GetPath());
      std::string subdirName_num = subdirName_num_tstring.Data();
      size_t pos_num = subdirName_num.find(":/");
      assert(pos_num < (subdirName_num.length() - 2));
      subdirName_num = std::string(subdirName_num, pos_num + 2);

      //-------- compute fakes_data histogram for denominator 
      //        (= data_obs - sum(prompt MC) histograms for fakeable lepton selection)
      std::string subdirLeptonFakesName_output_den = Form("%s/%s", subdirName_den.data(), processLeptonFakes.data());       
      //std::cout << " subdirLeptonFakesName_output_den = '" << subdirLeptonFakesName_output_den << "'" << std::endl;
      TDirectory* subdirLeptonFakes_output_den = createSubdirectory_recursively(fs, subdirLeptonFakesName_output_den);
      subdirLeptonFakes_output_den->cd();                                                                                                                                             
                 
      std::string histogramNameFakeBg_den;
      if ( !((*central_or_shift) == "" || (*central_or_shift) == "central") ) histogramNameFakeBg_den.append(*central_or_shift);
      if ( histogramNameFakeBg_den.length() > 0 ) histogramNameFakeBg_den.append("_");
      histogramNameFakeBg_den.append(*histogram);
      TH1* histogramFakeBg_den = subtractHistograms(histogramNameFakeBg_den, histogramData_den, histogramsToSubtract_den, verbosity);  
      if ( verbosity ) {
	std::cout << " Den. integral(" << processLeptonFakes << ") = " << histogramFakeBg_den->Integral() << std::endl;
      }
      makeBinContentsPositive(histogramFakeBg_den, verbosity);
      // histogramFakeBg_den->Write();      
      //--------

      //-------- compute fakes_data histogram for numerator 
      //        (take fakes_data shape from denominator and normalize the shape to data_obs - sum(prompt MC) for tight lepton selection;
      //         in case the difference data_obs - sum(prompt MC) is below 10% times data_obs, normalize the fakes_data histogram for the numerator to 10% times data_obs
      //         and rescale the histograms for the prompt MC "backgrounds" such that the sum(prompt MC) + fakes_data = data_obs)
      std::string subdirLeptonFakesName_output_num = Form("%s/%s", subdirName_num.data(), processLeptonFakes.data());        
      //std::cout<< " subdirLeptonFakesName_output_num = '" << subdirLeptonFakesName_output_num << "'" << std::endl;
      TDirectory* subdirLeptonFakes_output_num = createSubdirectory_recursively(fs, subdirLeptonFakesName_output_num);
      subdirLeptonFakes_output_num->cd();   

      std::string histogramNameFakeBg_num;  
      if ( !((*central_or_shift) == "" || (*central_or_shift) == "central") ) histogramNameFakeBg_num.append(*central_or_shift);  
      if ( histogramNameFakeBg_num.length() > 0 ) histogramNameFakeBg_num.append("_");
      histogramNameFakeBg_num.append(*histogram);  
      TH1* histogramFakeBg_num = subtractHistograms(histogramNameFakeBg_num, histogramData_den, histogramsToSubtract_den, verbosity);  // Doing (Data - Sum Bg.)
      if ( verbosity ) { 
	std::cout << " Den. integral(" << processLeptonFakes << ") before scaling = " << histogramFakeBg_num->Integral() << std::endl;
      }
      makeBinContentsPositive(histogramFakeBg_den, verbosity);

      double integralData_num = compIntegral(histogramData_num, true, true);
      double integralPromptBg_num = 0.;
      for ( std::vector<TH1*>::const_iterator histogramToSubtract_num = histogramsToSubtract_num.begin();
	    histogramToSubtract_num != histogramsToSubtract_num.end(); ++histogramToSubtract_num ) {
	integralPromptBg_num += compIntegral(*histogramToSubtract_num, true, true);
      }
      double integralFakeBg_num = integralData_num - integralPromptBg_num;
      
      double sfPromptBg_num = 1.;
      if ( integralFakeBg_num < (0.10*integralData_num) ) {
	std::cout<< " DATA - SUM(PROMPT BG.S) " << integralFakeBg_num << " < (0.10 * DATA) WHICH IS = " << (0.10*integralData_num) << std::endl; 
	integralFakeBg_num = 0.10*integralData_num;
	sfPromptBg_num = (integralData_num - integralFakeBg_num)/integralPromptBg_num;
      }
      double integralFakeBg_den = compIntegral(histogramFakeBg_den, true, true);
      double sfFakeBg_num = integralFakeBg_num/integralFakeBg_den;
      histogramFakeBg_num->Scale(sfFakeBg_num);
      if ( verbosity ) { 
	std::cout << " Num. integral(" << processLeptonFakes << ") after scaling = " << histogramFakeBg_num->Integral() << std::endl;
      }
      makeBinContentsPositive(histogramFakeBg_num, verbosity);
      // histogramFakeBg_num->Write();
      //--------

      //-------- copy histograms for data_obs and prompt MC to output file
      if ( !histogramData_den_isSubstitute ) {
	std::string subdirDataName_output_den = Form("%s/%s", subdirName_den.data(), processData.data());        
	if ( verbosity ) { 
	  std::cout << " subdirDataName_output_den = '" << subdirDataName_output_den << "'" << std::endl;
	}
	TDirectory* subdirData_output_den = createSubdirectory_recursively(fs, subdirDataName_output_den);
	subdirData_output_den->cd(); 

	TH1* histogramData_den_copied = copyHistogram(histogramData_den, histogramData_den->GetName(), verbosity);
	if ( verbosity ) { 
	  std::cout << " Den. integral(" << processData << ") = " << histogramData_den_copied->Integral() << std::endl;
	}
	// histogramData_den_copied->Write();
      }

      for ( std::vector<histogramEntryType*>::const_iterator histogram_and_processToSubtract_den = histograms_and_processesToSubtract_den.begin();
	    histogram_and_processToSubtract_den != histograms_and_processesToSubtract_den.end(); ++histogram_and_processToSubtract_den ) {
	std::string subdirPromptBgName_output_den = Form("%s/%s", subdirName_den.data(), (*histogram_and_processToSubtract_den)->process_.data());        
	if ( verbosity ) { 
	  std::cout << " subdirPromptBgName_output_den = '" << subdirPromptBgName_output_den << "'" << std::endl;
	}
	TDirectory* subdirPromptBg_output_den = createSubdirectory_recursively(fs, subdirPromptBgName_output_den);
	subdirPromptBg_output_den->cd(); 

	TH1* histogramPromptBg_den_copied = copyHistogram((*histogram_and_processToSubtract_den)->histogram_, (*histogram_and_processToSubtract_den)->histogram_->GetName(), verbosity);
	if ( verbosity ) { 
	  std::cout << " Den. integral(" << (*histogram_and_processToSubtract_den)->process_ << ") = " << histogramPromptBg_den_copied->Integral() << std::endl;
	}
	// histogramPromptBg_den_copied->Write();
      }

      if ( !histogramData_num_isSubstitute ) {
	std::string subdirDataName_output_num = Form("%s/%s", subdirName_num.data(), processData.data());        
	if ( verbosity ) { 
	  std::cout << " subdirDataName_output_num = '" << subdirDataName_output_num << "'" << std::endl;
	}
	TDirectory* subdirData_output_num = createSubdirectory_recursively(fs, subdirDataName_output_num);
	subdirData_output_num->cd(); 

	TH1* histogramData_num_copied = copyHistogram(histogramData_num, histogramData_num->GetName(), verbosity);
	if ( verbosity ) { 
	  std::cout << " Num. integral(" << processData << ") = " << histogramData_num_copied->Integral() << std::endl;
	}
	// histogramData_num_copied->Write();
      }

      for ( std::vector<histogramEntryType*>::const_iterator histogram_and_processToSubtract_num = histograms_and_processesToSubtract_num.begin();
	    histogram_and_processToSubtract_num != histograms_and_processesToSubtract_num.end(); ++histogram_and_processToSubtract_num ) {
	std::string subdirPromptBgName_output_num = Form("%s/%s", subdirName_num.data(), (*histogram_and_processToSubtract_num)->process_.data());        
	if ( verbosity ) { 
	  std::cout << " subdirPromptBgName_output_num = '" << subdirPromptBgName_output_num << "'" << std::endl;
	}
	TDirectory* subdirPromptBg_output_num = createSubdirectory_recursively(fs, subdirPromptBgName_output_num);
	subdirPromptBg_output_num->cd(); 

	TH1* histogramPromptBg_num_copied = copyHistogram((*histogram_and_processToSubtract_num)->histogram_, (*histogram_and_processToSubtract_num)->histogram_->GetName(), verbosity);
	if ( sfPromptBg_num != 1. ) {
	  histogramPromptBg_num_copied->Scale(sfPromptBg_num);
	}
	if ( verbosity ) { 
	  std::cout << " Num. integral(" << (*histogram_and_processToSubtract_num)->process_ << ") = " << histogramPromptBg_num_copied->Integral() << std::endl;
	}
	// histogramPromptBg_num_copied->Write();
      }
      //--------

      for ( std::vector<histogramEntryType*>::iterator it = histograms_and_processesToSubtract_den.begin();
	    it != histograms_and_processesToSubtract_den.end(); ++it ) {
	delete (*it);
      }
      for ( std::vector<histogramEntryType*>::iterator it = histograms_and_processesToSubtract_num.begin();
	    it != histograms_and_processesToSubtract_num.end(); ++it ) {
	delete (*it);
      }
    }
  }
}



void processDirectory(
       const TFile* inputFile, 
       const TDirectory* dir_den, const TDirectory* dir_num, 
       const std::string& processData, const std::string& processLeptonFakes, const vstring& processesToSubtract, 
       const vstring& central_or_shifts, fwlite::TFileService& fs, const std::string& cat_num, const std::string& cat_den) {

  processHistogram(inputFile, dir_den, dir_num, processData, processLeptonFakes, processesToSubtract, central_or_shifts, fs, cat_num);   

  std::vector<const TDirectory*> subdirs_den = getSubdirectories(dir_den);  
  for(std::vector<const TDirectory*>::iterator subdir_den = subdirs_den.begin();
      subdir_den != subdirs_den.end(); ++subdir_den){ 
    TString subdirName_num = TString((*subdir_den)->GetPath()).ReplaceAll("denominator", "numerator"); 
    subdirName_num = subdirName_num.ReplaceAll("fakeable", "tight"); 
    if ( subdirName_num.First(":/") < (subdirName_num.Length() - 2) ) {
      std::string subdirName_string = subdirName_num.Data();
      size_t pos = subdirName_string.find(":/");
      assert(pos < (subdirName_string.length() - 2));
      subdirName_string = std::string(subdirName_string, pos + 2); 
      subdirName_num = subdirName_string.data();
    }
        
    TDirectory* subdir_num = getDirectory(inputFile, subdirName_num.Data(), true);  
    if ( subdir_num && (*subdir_den) ) { 
      processDirectory(inputFile, *subdir_den, subdir_num, processData, processLeptonFakes, processesToSubtract, central_or_shifts, fs, cat_num, cat_den);
    }
  }
}

TH1* GetHistofromFunc(const TH1* histo, TF1* fit_func, const double& fitRange_min){

  TH1* new_histo = dynamic_cast<TH1*>(histo->Clone());
  // new_histo->Reset(); // resetting the clone histogram bin contents and errors to zero
  // TArrayD histo_Binning = getBinning(new_histo);  
  const TAxis* const xAxis = new_histo->GetXaxis();
  const int numBins = xAxis->GetNbins();  
  int starting_bin  = 0; 
  for(int iBin = 0; iBin < numBins; iBin++){
    if((fitRange_min >= xAxis->GetBinLowEdge(iBin)) && (fitRange_min < xAxis->GetBinUpEdge(iBin)) ){
      starting_bin = iBin;
      break;
    }else{
      continue;
    }
  } // 1st Loop over bins ends


  for(int iBin = starting_bin; iBin < numBins; iBin++){
    double new_bin_content =  fit_func->Integral(xAxis->GetBinLowEdge(iBin), xAxis->GetBinUpEdge(iBin));
    // std::cout<< "Bin ID: " << iBin <<  " xLow: " << xAxis->GetBinLowEdge(iBin) << " xHigh: " << xAxis->GetBinUpEdge(iBin) << " Integral Value " << new_bin_content << std::endl; 
    new_histo->SetBinContent(iBin, new_bin_content);
    new_histo->SetBinError(iBin, 0.); // no error bars
    // new_histo->SetBinError(iBin, (1./TMath::Sqrt(new_bin_content))); // (unweighted) Poisson error bars

  } // 2nd Loop over bins ends


  return new_histo;
}


void SetCentralHistoBinError(TH1* central_histo, std::vector<TH1*> alt_histos, const double& fitRange_min){
  const TAxis* const xAxis = central_histo->GetXaxis();
  const int numBins = xAxis->GetNbins();  
  int starting_bin  = 0; 
  for(int iBin = 0; iBin < numBins; iBin++){
    if((fitRange_min >= xAxis->GetBinLowEdge(iBin)) && (fitRange_min < xAxis->GetBinUpEdge(iBin)) ){
      starting_bin = iBin;
      break;
    }else{
      continue;
    }
  } // 1st Loop over bins ends

  std::vector<double> vect_binerrors(numBins);
  for(int iBin = starting_bin; iBin < numBins; iBin++){
    double difference2 = 0.;
  for(std::vector<TH1*>::const_iterator alt_histo_iter = alt_histos.begin(); 
      alt_histo_iter != alt_histos.end(); alt_histo_iter++){
	double bin_content_alt =  (*alt_histo_iter)->GetBinContent(iBin);
	double bin_content_central =  central_histo->GetBinContent(iBin);
        difference2 += TMath::Power((bin_content_alt - bin_content_central), 2.0);
   } // Loop over histos
  vect_binerrors.at(iBin) = TMath::Sqrt(difference2);
  } // Loop over bins

  for(int iBin = starting_bin; iBin < numBins; iBin++){
    central_histo->SetBinError(iBin, vect_binerrors[iBin]);
  }
}

std::vector<TH1*> FitSystUpDownHisto(TH1* central_histo, std::vector<TH1*> alt_histos, const double& fitRange_min, const std::string& label){

  std::vector<TH1*> vect_hist;
  std::string labelUp   = label + "_FitSystUp";
  std::string labelDown = label + "_FitSystDown";

  const TAxis* const xAxis = central_histo->GetXaxis();
  const int numBins = xAxis->GetNbins();  
  int starting_bin  = 0; 
  for(int iBin = 0; iBin < numBins; iBin++){
    if((fitRange_min >= xAxis->GetBinLowEdge(iBin)) && (fitRange_min < xAxis->GetBinUpEdge(iBin)) ){
      starting_bin = iBin;
      break;
    }else{
      continue;
    }
  } // 1st Loop over bins ends

  std::vector<double> vect_BinContentsUp(numBins);
  std::vector<double> vect_BinContentsDown(numBins);
  for(int iBin = starting_bin; iBin < numBins; iBin++){
    double diff = 0.;
   for(std::vector<TH1*>::const_iterator alt_histo_iter = alt_histos.begin(); 
      alt_histo_iter != alt_histos.end(); alt_histo_iter++){
	double bin_content_alt =  (*alt_histo_iter)->GetBinContent(iBin);
	double bin_content_central =  central_histo->GetBinContent(iBin);
        diff += std::abs(bin_content_alt - bin_content_central);
   } // Loop over histos
   vect_BinContentsUp.at(iBin)   = central_histo->GetBinContent(iBin) + diff;
   vect_BinContentsDown.at(iBin) = central_histo->GetBinContent(iBin) - diff;
  } // Loop over bins

  TH1* hist_up = dynamic_cast<TH1*>(central_histo->Clone());
  // hist_up->Reset();
  hist_up->SetName(labelUp.c_str());
  TH1* hist_down = dynamic_cast<TH1*>(central_histo->Clone());
  // hist_down->Reset();
  hist_down->SetName(labelDown.c_str());

  for(int iBin = starting_bin; iBin < numBins; iBin++){
    hist_up->SetBinContent(iBin, vect_BinContentsUp[iBin]);
    hist_up->SetBinError(iBin, 0.);
    hist_down->SetBinContent(iBin, vect_BinContentsDown[iBin]);
    hist_down->SetBinError(iBin, 0.);
  }

  vect_hist.push_back(hist_up);
  vect_hist.push_back(hist_down);

  return vect_hist;

}

void Plot(TH1* histo_to_fit, FitFuncEntryType* nom_fit_func){
  // ----- Plotting ---------
  TCanvas* A = new TCanvas("A","FIT CANVAS",600,600);
  A->cd();
  gPad->SetGridx();
  gPad->SetGridy();
  gPad->SetLogy();  

  histo_to_fit->Draw(); // The bin width divided histogram on which the fit is actually performed
  (nom_fit_func->GetFitFunction())->SetLineColor(1);
  (nom_fit_func->GetFitFunction())->Draw("SAME");

  A->Update();

  A->Write();
}



int main(int argc, char* argv[]) 
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- parse command-line arguments
  if ( argc < 2 ) {
    std::cout << "Usage: " << argv[0] << " [parameters.py]" << std::endl;
    return EXIT_FAILURE;
  }

  std::cout << "<addBackgrounds_TailFit>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("addBackgrounds_TailFit");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") ) 
    throw cms::Exception("addBackgrounds_TailFit") 
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";
  
  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfgaddBackgrounds_TailFit = cfg.getParameter<edm::ParameterSet>("addBackgrounds_TailFit");
  
  std::string InputDir = cfgaddBackgrounds_TailFit.getParameter<std::string>("InputDir");
  std::string InputDirPath = Form("%s/sel/evt/", InputDir.data());
  std::string ProcessName = cfgaddBackgrounds_TailFit.getParameter<std::string>("processName");
  std::string HistogramName = cfgaddBackgrounds_TailFit.getParameter<std::string>("histogramName");

  bool apply_automatic_rebinning = cfgaddBackgrounds_TailFit.getParameter<bool>("apply_automatic_rebinning");
  double minEvents_automatic_rebinning = cfgaddBackgrounds_TailFit.getParameter<double>("minEvents_automatic_rebinning");
 
  const vdouble explicitBinning = cfgaddBackgrounds_TailFit.getParameter<vdouble>("explicit_binning");

  edm::ParameterSet nominal_fit_func_PSet = cfgaddBackgrounds_TailFit.getParameter<edm::ParameterSet>("nominal_fit_func");
  edm::VParameterSet vec_alt_fit_funcs_PSets = cfgaddBackgrounds_TailFit.getParameter<edm::VParameterSet>("alternate_fit_funcs");

  // ----- Input File ------
  fwlite::InputSource inputFiles(cfg); 
  if ( !(inputFiles.files().size() == 1) )
    throw cms::Exception("addBackgrounds_TailFit") 
      << "Exactly one input file expected !!\n";
  TFile* inputFile = new TFile(inputFiles.files().front().data());
  if ( !inputFile ) 
    throw cms::Exception("addBackgrounds_TailFit") 
      << "Failed to open input file = '" << inputFiles.files().front() << "' !!\n";

  // ------ Output File -------
  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  const TDirectory* inputDir = getDirectory(inputFile, InputDirPath, true);
  assert(inputDir);


  TDirectory* subsubdir_output = createSubdirectory_recursively(fs, Form("%s/%s", InputDirPath.data(), ProcessName.data()) );
  subsubdir_output->cd();



  TH1* histo = getHistogram(inputDir, ProcessName, HistogramName, "", true, false);
  //  TArrayD histo_Orig_Binning = getBinning(histo); // Storing original binning scheme of the histogram
  TH1* histo_to_fit = 0;

  // ------ (Optional) Re-binning of the histogram -------
  if(apply_automatic_rebinning && explicitBinning.empty()){
    TArrayD histoAutoBins = getRebinnedBinning(histo, minEvents_automatic_rebinning);
    histo_to_fit = getRebinnedHistogram1d(histo, 4, histoAutoBins, false);
  }else if(! explicitBinning.empty() && ! apply_automatic_rebinning){
    TArrayD histogramExplicitBinning = getTArraDfromVector(explicitBinning);
    histo_to_fit = getRebinnedHistogram1d(histo, 4, histogramExplicitBinning);
  }else{
    histo_to_fit = histo;
  }


  std::cout<< "histo_to_fit->Integral() " << histo_to_fit->Integral() << std::endl;

  // ---- Divide by bin width (to make fit binnning scheme indepndent) ------ 
  divideByBinWidth(histo_to_fit);

  // ----- Initialize Nominal Fit function ----
  std::cout<< " Initialize Nominal Fit function " << std::endl;
  FitFuncEntryType* nom_fit_func = new FitFuncEntryType(nominal_fit_func_PSet, histo_to_fit, "nom");


  // ----- Initialize Alternate Fit functions (for fit bias estimation studies) ----
  std::cout<< " Initialize Alternate Fit functions (for fit bias estimation studies) " << std::endl;
  std::vector<FitFuncEntryType*> vec_alt_fit_funcs;
  unsigned int counter = 0;
  for ( edm::VParameterSet::const_iterator alt_fit_func_PSet_iter = vec_alt_fit_funcs_PSets.begin();
        alt_fit_func_PSet_iter != vec_alt_fit_funcs_PSets.end(); alt_fit_func_PSet_iter++ ) {
    std::string label = Form("alt_%i", counter);
    FitFuncEntryType* fit_func = new FitFuncEntryType(*alt_fit_func_PSet_iter, histo_to_fit, label);
    vec_alt_fit_funcs.push_back(fit_func);
    counter++;
  }


  // ---- Fitting (nominal function) ------
  std::cout<< " Fitting Nominal function " << std::endl;
  TFitResultPtr fitResult = histo_to_fit->Fit(nom_fit_func->GetFitFunction(), "EOSR");

  // ----- Accessing covariance matrix, eigen-values and eigen-vectors --- 
  std::cout << " Accessing covariance matrix, eigen-values and eigen-vectors " << std::endl;
  std::vector<fitFunction_and_legendEntry> fitFunctions_sysShifts;
  TF1* fitFunction_nom = nom_fit_func->GetFitFunction();

  if ( fitResult->IsValid() ) {
    TMatrixDSym covMatrix = fitResult->GetCovarianceMatrix();
    std::vector<EigenVector_and_Value> eigenVectors_and_Values = compEigenVectors_and_Values(covMatrix);
    size_t dimension = fitFunction_nom->GetNpar();  
    assert(eigenVectors_and_Values.size() == dimension);
    int idxPar = 1;
    for ( std::vector<EigenVector_and_Value>::const_iterator eigenVector_and_Value = eigenVectors_and_Values.begin();
	  eigenVector_and_Value != eigenVectors_and_Values.end(); ++eigenVector_and_Value ) {
      assert(eigenVector_and_Value->eigenVector_.GetNrows() == (int)dimension);
      std::cout << "EigenVector #" << idxPar << ":" << std::endl;
      eigenVector_and_Value->eigenVector_.Print();
      std::cout << "EigenValue #" << idxPar << " = " << eigenVector_and_Value->eigenValue_ << std::endl;
      assert(eigenVector_and_Value->eigenValue_ >= 0.);
      std::string fitFunctionParUpName = Form("%s_par%iUp", (nom_fit_func->GetFitFuncName()).data(), idxPar);
      FitFuncEntryType* fit_func_par_up = new FitFuncEntryType(nominal_fit_func_PSet, histo_to_fit, fitFunctionParUpName);
      TF1* fitFunctionParUp = fit_func_par_up->GetFitFunction();
      for ( size_t idxComponent = 0; idxComponent < dimension; ++idxComponent ) {
	fitFunctionParUp->SetParameter(idxComponent, fitFunction_nom->GetParameter(idxComponent) + TMath::Sqrt(eigenVector_and_Value->eigenValue_)*eigenVector_and_Value->eigenVector_(idxComponent));
      }
      fitFunctions_sysShifts.push_back(fitFunction_and_legendEntry(fitFunctionParUp, Form("EigenVecUp_%i", idxPar)));
      std::string fitFunctionParDownName = Form("%s_par%iDown", (nom_fit_func->GetFitFuncName()).data(), idxPar);
      FitFuncEntryType* fit_func_par_down = new FitFuncEntryType(nominal_fit_func_PSet, histo_to_fit, fitFunctionParDownName);
      TF1* fitFunctionParDown = fit_func_par_down->GetFitFunction();
      for ( size_t idxComponent = 0; idxComponent < dimension; ++idxComponent ) {
	fitFunctionParDown->SetParameter(idxComponent, fitFunction_nom->GetParameter(idxComponent) - TMath::Sqrt(eigenVector_and_Value->eigenValue_)*eigenVector_and_Value->eigenVector_(idxComponent));
      }
      fitFunctions_sysShifts.push_back(fitFunction_and_legendEntry(fitFunctionParDown, Form("EigenVecDown_%i", idxPar)));
      ++idxPar;
    } // loop over e-vectors and e-values ends
  } else {
    std::cerr << "Warning: Fit failed to converge !!" << std::endl;
  }


  // ------ Computing the central tail-fitted histogram -----
  std::cout<< " Computing the central tail-fitted histogram " << std::endl;
  TH1* central_fit_histo = GetHistofromFunc(histo, fitFunction_nom, nom_fit_func->GetXmin()); // Using the original binned histogram
  std::string histo_name1 = Form("%s_central_fit", HistogramName.data());
  central_fit_histo->SetName(histo_name1.c_str());

  // ------ Computing the fit systematic tail-fitted histograms -----
  std::cout<< " Computing the fit systematic tail-fitted histogram " << std::endl;
  std::vector<TH1*> fit_sysShifts_histos;
  for ( std::vector<fitFunction_and_legendEntry>::const_iterator fitFunction_sysShift = fitFunctions_sysShifts.begin();
	fitFunction_sysShift != fitFunctions_sysShifts.end(); ++fitFunction_sysShift ) {
        TH1* fit_sysShifts_histogram = GetHistofromFunc(histo, (fitFunction_sysShift->fitFunction_), nom_fit_func->GetXmin()); // Using the original binned histogram
	std::string histo_name2 = Form("%s_%s", HistogramName.data(), (fitFunction_sysShift->legendEntry_).data());
        fit_sysShifts_histogram->SetName(histo_name2.c_str());
        fit_sysShifts_histos.push_back(fit_sysShifts_histogram);
  }

    
  // ---- Fitting (alternate functions) ------
  std::cout<< " Fitting alternate functions " << std::endl;
  std::vector<TFitResultPtr> fitResult_vect;
  std::vector<TH1*> vect_alt_fit_histos;
  int count = 0;
  for(std::vector<FitFuncEntryType*>::const_iterator func_iter =  vec_alt_fit_funcs.begin(); 
      func_iter != vec_alt_fit_funcs.end(); func_iter++){
    TFitResultPtr fitResult = histo_to_fit->Fit((*func_iter)->GetFitFunction(), "EOSR");
    if(fitResult->IsValid()){
      fitResult_vect.push_back(fitResult);
      TH1* alt_fit_histo = GetHistofromFunc(histo, (*func_iter)->GetFitFunction(), (*func_iter)->GetXmin()); // Using the original binned histogram
      std::string histo_name3 = Form("%s_alt_fitFunc_%i", HistogramName.data(), counter);
      alt_fit_histo->SetName(histo_name3.c_str());
      vect_alt_fit_histos.push_back(alt_fit_histo);
    }
    count++;
  }

  // ----- Fit Bias Systematic -------
  std::cout<< " Computing the Fit Bias Systematic " << std::endl;
  TH1* fit_bias_Syst_histo = dynamic_cast<TH1*>(central_fit_histo->Clone());
  std::string histo_name4 = Form("%s_fit_bias_Syst", HistogramName.data());
  fit_bias_Syst_histo->SetName(histo_name4.c_str());

  // ---- Bin-By-Bin ------
  SetCentralHistoBinError(fit_bias_Syst_histo, vect_alt_fit_histos, nom_fit_func->GetXmin());

  // ---- Up and Down ----
  std::vector<TH1*> vect_hist;
  vect_hist = FitSystUpDownHisto(fit_bias_Syst_histo, vect_alt_fit_histos, nom_fit_func->GetXmin(), HistogramName);

  // ---- Plotting ----
  // Plot(histo_to_fit, nom_fit_func);



  /*
  std::vector<categoryEntryType*> categories;
  edm::VParameterSet cfgCategories = cfgaddBackgrounds_TailFit.getParameter<edm::VParameterSet>("categories");
  for ( edm::VParameterSet::const_iterator cfgCategory = cfgCategories.begin();
	cfgCategory != cfgCategories.end(); ++cfgCategory ) {
    categoryEntryType* category = new categoryEntryType(*cfgCategory);
    categories.push_back(category);
  }

  std::string processData = cfgaddBackgrounds_TailFit.getParameter<std::string>("processData");
  std::string processLeptonFakes = cfgaddBackgrounds_TailFit.getParameter<std::string>("processLeptonFakes");
  vstring processesToSubtract = cfgaddBackgrounds_TailFit.getParameter<vstring>("processesToSubtract");

  vstring central_or_shifts = cfgaddBackgrounds_TailFit.getParameter<vstring>("sysShifts");
  bool contains_central_value = false;
  for ( vstring::const_iterator central_or_shift = central_or_shifts.begin();
	central_or_shift != central_or_shifts.end(); ++central_or_shift ) {
    if ( (*central_or_shift) == "" || (*central_or_shift) == "central" ) contains_central_value = true;
  }
  if ( !contains_central_value ) central_or_shifts.push_back(""); // CV: add central value

  fwlite::InputSource inputFiles(cfg); 
  if ( !(inputFiles.files().size() == 1) )
    throw cms::Exception("addBackgrounds_TailFit") 
      << "Exactly one input file expected !!\n";
  TFile* inputFile = new TFile(inputFiles.files().front().data());
  if ( !inputFile ) 
    throw cms::Exception("addBackgrounds_TailFit") 
      << "Failed to open input file = '" << inputFiles.files().front() << "' !!\n";
  
  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  for ( std::vector<categoryEntryType*>::const_iterator category = categories.begin();
	category != categories.end(); ++category ) {                                                                  
    std::cout << "processing category: numerator = " << (*category)->numerator_ << ", denominator = " << (*category)->denominator_ << std::endl;

    TDirectory* dir_denominator = getDirectory(inputFile, (*category)->denominator_, true); 
    assert(dir_denominator);                                                                                                                                                                      
    TDirectory* dir_numerator = getDirectory(inputFile, (*category)->numerator_, true); 
    assert(dir_numerator);  

    processDirectory(
      inputFile, 
      dir_denominator, dir_numerator, 
      processData, processLeptonFakes, processesToSubtract, 
      central_or_shifts, fs, (*category)->numerator_, (*category)->denominator_);
  }

  delete inputFile;
  */



  clock.Show("addBackgrounds_TailFit");

  return EXIT_SUCCESS;
}
