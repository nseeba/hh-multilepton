
/** \executable computePDFUncs
 *
 * Calculation of PDF and QCD scale acceptance uncertainties for MC samples.
 *
 * \author Ram Krishna Dewanjee, Tallinn
 *
 */

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#if __has_include (<FWCore/ParameterSetReader/interface/ParameterSetReader.h>)
#  include <FWCore/ParameterSetReader/interface/ParameterSetReader.h> // edm::readPSetsFrom()
#else
#  include <FWCore/PythonParameterSet/interface/MakeParameterSets.h> // edm::readPSetsFrom()
#endif

#include "FWCore/Utilities/interface/Exception.h"

#include "PhysicsTools/FWLite/interface/TFileService.h"
#include "DataFormats/FWLite/interface/InputSource.h"
#include "DataFormats/FWLite/interface/OutputFiles.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h"
#include "tthAnalysis/HiggsToTauTau/interface/addBackgroundsAuxFunctions.h" // getSubdirectories, getSubdirectoryNames

#include <TFile.h>
#include <TH1.h>
#include <TBenchmark.h>
#include <TMath.h>
#include <TError.h> // gErrorAbortLevel, kError
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
#include <fstream> // std::ofstream

TH1* compRatioHistogram(const std::string& ratioHistogramName, const TH1* numerator, const TH1* denominator)
{
  TH1* histogramRatio = 0;

  if ( numerator->GetDimension() == denominator->GetDimension() &&
       numerator->GetNbinsX() == denominator->GetNbinsX() ) {
    histogramRatio = (TH1*)numerator->Clone(ratioHistogramName.data());
    histogramRatio->Divide(denominator);
    histogramRatio->SetLineColor(numerator->GetLineColor());
    histogramRatio->SetLineWidth(numerator->GetLineWidth());
    histogramRatio->SetMarkerColor(numerator->GetMarkerColor());
    histogramRatio->SetMarkerStyle(numerator->GetMarkerStyle());
    histogramRatio->SetMarkerSize(numerator->GetMarkerSize());
  }

  return histogramRatio;
}



void computePDFUnc_NNPDF_Run1(TH1* histo_sub_category, TH1* histo_inclusive){ // Used in Run-1 SM HTauTau analysis (HIG-13-004): AN2013_262_V8.pdf
  checkCompatibleBinning(histo_sub_category, histo_inclusive);
  double a_plus  = 0.;
  double a_minus = 0.;
  int plus_counter = 0;  
  int minus_counter = 0;  
  std::vector<double> PDFAcceptance;
  TH1* PDFaccept_histo = compRatioHistogram("PDFacceptance", histo_sub_category, histo_inclusive);
  
  double PDFacceptCentral = PDFaccept_histo->GetBinContent(1);
  PDFAcceptance.push_back(PDFacceptCentral);
  int nBins = PDFaccept_histo->GetNbinsX();
  for ( int iBin = 2; iBin <= nBins; ++iBin ){
    double PDFacceptVar = PDFaccept_histo->GetBinContent(iBin);
    if(PDFacceptVar >= PDFacceptCentral){
      a_plus += TMath::Power((PDFacceptVar - PDFacceptCentral), 2.0);
      plus_counter += 1;
    }else{
      a_minus += TMath::Power((PDFacceptCentral - PDFacceptVar), 2.0);
      minus_counter += 1;
    }
    // PDFaccept_histo->SetBinContent(iBin, binContent - 1.);
  }

  double delta_PDFacceptVar_plus = TMath::Sqrt( (a_plus/((double)plus_counter)) );
  double delta_PDFacceptVar_minus = TMath::Sqrt( (a_minus/((double)minus_counter)) );
  std::cout << "PDF acceptance: " << PDFacceptCentral << " + " << delta_PDFacceptVar_plus << " - " << delta_PDFacceptVar_minus << std::endl; 
  PDFAcceptance.push_back(delta_PDFacceptVar_plus);
  PDFAcceptance.push_back(delta_PDFacceptVar_minus);
  for(unsigned int i = 0; i < PDFAcceptance.size(); i++){
    std::cout<< "Value stored " << i << " " << PDFAcceptance[i] << std::endl;
  }
  // return PDFAcceptance;
}

void computeScaleUnc_Run1(TH1* EventCounter_sel, TH1* EventCounter_incl, TH1* histo_sub_cat, TH1* histo_incl){ // Used in Run-1 SM HTauTau analysis (HIG-13-004): AN2013_262_V8.pdf

  double yield_sel      = EventCounter_sel->Integral();
  double yield_incl     = EventCounter_incl->Integral();
  double ScaleAcceptDefault  = (yield_sel/yield_incl); // Scale acceptance for default case (mu_R = mu_F = 1.0) 
  TH1* histo_ScaleAcceptVar = compRatioHistogram("histo_ScaleAcceptVar", histo_sub_cat, histo_incl);
  std::vector<double> ScaleVarVector;
  int nBins = histo_ScaleAcceptVar->GetNbinsX();
  for ( int iBin = 1; iBin <= nBins; ++iBin ){
    ScaleVarVector.push_back(histo_ScaleAcceptVar->GetBinContent(iBin));
  }

  double MaxScaleVar = *max_element(ScaleVarVector.begin(), ScaleVarVector.end());
  double MinScaleVar = *min_element(ScaleVarVector.begin(), ScaleVarVector.end());
  std::cout<< "Max. Scale Acceptance: " << MaxScaleVar << std::endl;
  std::cout<< "Min. Scale Acceptance: " << MinScaleVar << std::endl;

  double Scale_Unc = (MaxScaleVar - MinScaleVar)/(2 * ScaleAcceptDefault);
  
  std::cout<< "Scale Unc. " << ScaleAcceptDefault << " +/- " << Scale_Unc << std::endl;

}

typedef std::vector<std::string> vstring;

int main(int argc, char* argv[])
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- parse command-line arguments
  if ( argc < 2 ) {
    std::cout << "Usage: " << argv[0] << " [parameters.py]" << std::endl;
    return EXIT_FAILURE;
  }

  std::cout << "<computePDFUncs>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("computePDFUncs");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("computePDFUncs")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfgComputePDFUncs = cfg.getParameter<edm::ParameterSet>("computePDFUncs");

  vstring categories  = cfgComputePDFUncs.getParameter<vstring>("categories");
  std::string num_dir = cfgComputePDFUncs.getParameter<std::string>("num_dir");
  std::string den_dir = cfgComputePDFUncs.getParameter<std::string>("den_dir");
  std::string ProcessName = cfgComputePDFUncs.getParameter<std::string>("process_name");
  
  vstring central_or_shifts = cfgComputePDFUncs.getParameter<vstring>("sysShifts");
  central_or_shifts.push_back(""); // CV: add central value

  fwlite::InputSource inputFiles(cfg);
  if ( !(inputFiles.files().size() == 1) )
    throw cms::Exception("computePDFUncs")
      << "Exactly one input file expected !!\n";
  TFile* inputFile = new TFile(inputFiles.files().front().data());

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());


  std::ostream* uncInfoFile = new std::ofstream("file.txt", std::ios::out); 
  (*uncInfoFile) << ':' << ProcessName << '\n';


  if ( categories.size() == 0 ) categories = getSubdirectoryNames(inputFile);

  for ( vstring::const_iterator category = categories.begin();
        category != categories.end(); ++category ) {

    std::string numerator_dir_path   = (*category) + "/" + num_dir;  
    std::string denominator_dir_path = (*category) + "/" + den_dir;  

    TH1* num_pdfWeights = 0;
    TH1* den_pdfWeights = 0;
    TH1* num_scaleWeights = 0;
    TH1* den_scaleWeights = 0;
    TH1* num_EventCounter = 0;
    TH1* den_EventCounter = 0;

    TDirectory* numerator_dir = getDirectory(inputFile, numerator_dir_path, true);
    assert(numerator_dir);
    std::cout << "processing numerator directory = " << numerator_dir_path << std::endl;
    num_EventCounter   = getHistogram(dynamic_cast<const TDirectory*>(numerator_dir), ProcessName, "EventCounter", "", true, false);
    num_pdfWeights   = getHistogram(dynamic_cast<const TDirectory*>(numerator_dir), ProcessName, "pdfWeights", "", true, false);
    num_scaleWeights = getHistogram(dynamic_cast<const TDirectory*>(numerator_dir), ProcessName, "scaleWeights", "", true, false);

    std::cout<< "num_pdfWeights->GetNbinsX() " << num_pdfWeights->GetNbinsX() << std::endl; 
    std::cout<< "num_scaleWeights->GetNbinsX() " << num_scaleWeights->GetNbinsX() << std::endl; 


    TDirectory* denominator_dir = getDirectory(inputFile, denominator_dir_path, true);
    assert(denominator_dir);
    std::cout << "processing denominator directory = " << denominator_dir_path << std::endl;
    den_EventCounter   = getHistogram(dynamic_cast<const TDirectory*>(denominator_dir), ProcessName, "EventCounter", "", true, false);
    den_pdfWeights   = getHistogram(dynamic_cast<const TDirectory*>(denominator_dir), ProcessName, "pdfWeights", "", true, false);
    den_scaleWeights = getHistogram(dynamic_cast<const TDirectory*>(denominator_dir), ProcessName, "scaleWeights", "", true, false);

    std::cout<< "den_pdfWeights->GetNbinsX() " << den_pdfWeights->GetNbinsX() << std::endl; 
    std::cout<< "den_scaleWeights->GetNbinsX() " << den_scaleWeights->GetNbinsX() << std::endl; 

    computePDFUnc_NNPDF_Run1(num_pdfWeights, den_pdfWeights);

    computeScaleUnc_Run1(num_EventCounter, den_EventCounter, num_scaleWeights, den_scaleWeights);

    delete num_EventCounter;
    delete den_EventCounter;
    delete num_pdfWeights;
    delete den_pdfWeights;
    delete num_scaleWeights;
    delete den_scaleWeights;


/*
    std::vector<const TDirectory*> subdirs_level1 = getSubdirectories(dir);
    for ( std::vector<const TDirectory*>::iterator subdir_level1 = subdirs_level1.begin();
          subdir_level1 != subdirs_level1.end(); ++subdir_level1 ) {

      std::vector<const TDirectory*> subdirs_level2 = getSubdirectories(*subdir_level1);
      for ( std::vector<const TDirectory*>::iterator subdir_level2 = subdirs_level2.begin();
          subdir_level2 != subdirs_level2.end(); ++subdir_level2 ) {

        std::cout << " processing directory = " << Form("%s/%s", (*subdir_level1)->GetName(), (*subdir_level2)->GetName()) << std::endl;

        std::string the_process_input = processes_input.front();

        TDirectory* dir_input = dynamic_cast<TDirectory*>((const_cast<TDirectory*>(*subdir_level2))->Get(the_process_input.data()));
        if ( !dir_input ) {
          if ( the_process_input.find("ttH_htt") != std::string::npos ||
               the_process_input.find("ttH_hww") != std::string::npos ||
               the_process_input.find("ttH_hzz") != std::string::npos ||
               the_process_input.find("ttH_hzg") != std::string::npos ||
               the_process_input.find("ttH_hmm") != std::string::npos  ) {
            continue;
          }
          if ( std::string((*subdir_level2)->GetName()).find("genEvt")    != std::string::npos ||
               std::string((*subdir_level2)->GetName()).find("lheInfo")   != std::string::npos ||
               std::string((*subdir_level2)->GetName()).find("cutFlow")   != std::string::npos ||
               std::string((*subdir_level2)->GetName()).find("evtntuple") != std::string::npos ) {
            continue;
          }
          throw cms::Exception("computePDFUncs")
            << "Failed to find subdirectory = " << the_process_input << " within directory = " << (*subdir_level2)->GetName() << " !!\n";
          //std::cerr << "Failed to find subdirectory = " << the_process_input << " within directory = " << (*subdir_level2)->GetName() << " --> skipping !!" << std::endl;
          //continue;
        }
        std::set<std::string> histograms;
        TList* list = dir_input->GetListOfKeys();
        TIter next(list);
        TKey* key = 0;
        while ( (key = dynamic_cast<TKey*>(next())) ) {
          TObject* object = key->ReadObj();
          TH1* histogram = dynamic_cast<TH1*>(object);
          if ( !histogram ) continue;
          TString histogramName = TString(histogram->GetName()).ReplaceAll(Form("%s_", the_process_input.data()), "");
          for ( vstring::const_iterator central_or_shift = central_or_shifts.begin();
                central_or_shift != central_or_shifts.end(); ++central_or_shift ) {
            if ( !((*central_or_shift) == "" || (*central_or_shift) == "central") ) {
              histogramName = histogramName.ReplaceAll(Form("%s_", central_or_shift->data()), "");
            }
          }
          if ( histogramName.Contains("CMS_") ) continue;
          if ( histograms.find(histogramName.Data()) == histograms.end() ) {
            std::cout << "adding histogram = " << histogramName.Data() << std::endl;
            histograms.insert(histogramName.Data());
          }
        }

        for ( std::set<std::string>::const_iterator histogram = histograms.begin();
              histogram != histograms.end(); ++histogram ) {
          for ( vstring::const_iterator central_or_shift = central_or_shifts.begin();
                central_or_shift != central_or_shifts.end(); ++central_or_shift ) {
            std::vector<TH1*> histograms_input;
            for ( vstring::const_iterator process_input = processes_input.begin();
                  process_input != processes_input.end(); ++process_input ) {
              bool enableException = ( (*central_or_shift) == "" || (*central_or_shift) == "central" ) ? true : false;
              TH1* histogram_input = getHistogram(*subdir_level2, *process_input, *histogram, *central_or_shift, enableException);
              if ( !histogram_input ) histogram_input = getHistogram(*subdir_level2, *process_input, *histogram, "", true);
              histograms_input.push_back(histogram_input);
            }

            std::string subdirName_output = Form("%s/%s/%s/%s", category->data(), (*subdir_level1)->GetName(), (*subdir_level2)->GetName(), process_output.data());
            TDirectory* subdir_output = createSubdirectory_recursively(fs, subdirName_output);
            subdir_output->cd();

            std::string histogramName_output;
            if ( !((*central_or_shift) == "" || (*central_or_shift) == "central") ) histogramName_output.append(*central_or_shift);
            if ( histogramName_output.length() > 0 ) histogramName_output.append("_");
            histogramName_output.append(*histogram);
            TH1 * tmp = addHistograms(histogramName_output, histograms_input);
            tmp->Write();

            for(auto & histogram_input: histograms_input)
            {
              delete histogram_input;
            }
            delete tmp;
          }
        }
        delete dir_input;
      }
      for(auto & subdir_level2: subdirs_level2)
      {
        delete subdir_level2;
      }
      subdirs_level2.clear();
    }
    for(auto & subdir_level1: subdirs_level1)
    {
      delete subdir_level1;
    }
    subdirs_level1.clear();
*/

  } // Loop over categories ends
  //---------------------------------------------------------------------------------------------------
  // CV: Add (dummy) histograms for number of analyzed and processed events
  //     This is needed to avoid run-time errors/warnings when executing python/commands/get_events_count.py (called by python/sbatch-node.template.hadd.sh)
  fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  //---------------------------------------------------------------------------------------------------

  delete inputFile;
  delete uncInfoFile;


  clock.Show("computePDFUncs");

  std::cout << "returning exit code = " << EXIT_SUCCESS << " (EXIT_SUCCESS)." << std::endl;
  return EXIT_SUCCESS;
}
