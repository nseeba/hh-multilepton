#ifndef hhAnalysis_multilepton_GenHiggsReader_h
#define hhAnalysis_multilepton_GenHiggsReader_h

#include "tthAnalysis/HiggsToTauTau/interface/ReaderBase.h" // ReaderBase
#include "hhAnalysis/multilepton/interface/GenHiggs.h" // GenHiggs

#include <map> // std::map<,>

// forward declarations
class TTree;

class GenHiggsReader
  : public ReaderBase
{
public:
  explicit GenHiggsReader(const std::string & branchName_obj,
                        unsigned int max_nHiggses = 4);
  ~GenHiggsReader();

  /**
   * @brief Call tree->SetBranchAddress for all GenHiggs branches
   */
  void
  setBranchAddresses(TTree * tree) override;

  /**
   * @brief Read branches from tree and use information to fill collection of GenHiggs objects
   * @return Collection of GenHiggs objects
   */
  std::vector<GenHiggs>
  read() const;

  void
  read_partonFlavour();

protected:
 /**
   * @brief Initialize names of branches to be read from tree
   */
  void
  setBranchNames();

  bool read_partonFlavour_;

  const unsigned int max_nHiggses_;
  std::string branchName_num_;
  std::string branchName_obj_;

  std::string branchName_pt_;
  std::string branchName_eta_;
  std::string branchName_phi_;
  std::string branchName_mass_;
  std::string branchName_pdgId_;

  UInt_t nHiggses_;
  Float_t * Higgs_pt_;
  Float_t * Higgs_eta_;
  Float_t * Higgs_phi_;
  Float_t * Higgs_mass_;
  Int_t * Higgs_pdgId_;

  // CV: make sure that only one RecoHiggsReader instance exists for a given branchName,
  //     as ROOT cannot handle multiple TTree::SetBranchAddress calls for the same branch.
  static std::map<std::string, int> numInstances_;
  static std::map<std::string, GenHiggsReader *> instances_;
};

#endif // tthAnalysis_HiggsToTauTau_GenHiggsReader_h
