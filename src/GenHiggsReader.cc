#include "hhAnalysis/multilepton/interface/GenHiggsReader.h" // GenHiggsReader

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h" // cmsException()
#include "tthAnalysis/HiggsToTauTau/interface/BranchAddressInitializer.h" // BranchAddressInitializer, TTree, Form()

std::map<std::string, int> GenHiggsReader::numInstances_;
std::map<std::string, GenHiggsReader *> GenHiggsReader::instances_;

GenHiggsReader::GenHiggsReader(const std::string & branchName_obj,
                           unsigned int max_nHiggses)
  : read_partonFlavour_(false)
  , max_nHiggses_(max_nHiggses)
  , branchName_num_(Form("n%s", branchName_obj.data()))
  , branchName_obj_(branchName_obj)
  , Higgs_pt_(nullptr)
  , Higgs_eta_(nullptr)
  , Higgs_phi_(nullptr)
  , Higgs_mass_(nullptr)
  , Higgs_pdgId_(nullptr)
{
  std::cout <<" 1 branchName_num_ "<< branchName_num_ << std::endl;
  setBranchNames();
}

GenHiggsReader::~GenHiggsReader()
{
  --numInstances_[branchName_obj_];
  assert(numInstances_[branchName_obj_] >= 0);
  if(numInstances_[branchName_obj_] == 0)
  {
    GenHiggsReader * const gInstance = instances_[branchName_obj_];
    assert(gInstance);
    delete[] gInstance->Higgs_pt_;
    delete[] gInstance->Higgs_eta_;
    delete[] gInstance->Higgs_phi_;
    delete[] gInstance->Higgs_mass_;
    delete[] gInstance->Higgs_pdgId_;
    instances_[branchName_obj_] = nullptr;
  }
}

void
GenHiggsReader::setBranchNames()
{
  if(numInstances_[branchName_obj_] == 0)
  {
    branchName_pt_ = Form("%s_%s", branchName_obj_.data(), "pt");
    branchName_eta_ = Form("%s_%s", branchName_obj_.data(), "eta");
    branchName_phi_ = Form("%s_%s", branchName_obj_.data(), "phi");
    branchName_mass_ = Form("%s_%s", branchName_obj_.data(), "mass");
    branchName_pdgId_ = Form("%s_%s", branchName_obj_.data(), "pdgId");
    instances_[branchName_obj_] = this;
  }
  else
  {
    if(branchName_num_ != instances_[branchName_obj_]->branchName_num_)
    {
      throw cmsException(this)
        << "Association between configuration parameters 'branchName_num' and 'branchName_obj' must be unique:"
        << " present association 'branchName_num' = " << branchName_num_ << " with 'branchName_obj' = " << branchName_obj_
        << " does not match previous association 'branchName_num' = " << instances_[branchName_obj_]->branchName_num_
        << " with 'branchName_obj' = " << instances_[branchName_obj_]->branchName_obj_ << " !!\n";
    }
  }
  std::cout <<" branchName_num_ "<< branchName_num_ << std::endl;
  ++numInstances_[branchName_obj_];
}

void
GenHiggsReader::read_partonFlavour()
{
  branchName_pdgId_ = Form("%s_%s", branchName_obj_.data(), "partonFlavour");
}

void
GenHiggsReader::setBranchAddresses(TTree * tree)
{
  if(instances_[branchName_obj_] == this)
  {
    BranchAddressInitializer bai(tree, max_nHiggses_);
    bai.setBranchAddress(nHiggses_, branchName_num_);
    bai.setBranchAddress(Higgs_pt_, branchName_pt_);
    bai.setBranchAddress(Higgs_eta_, branchName_eta_);
    bai.setBranchAddress(Higgs_phi_, branchName_phi_);
    bai.setBranchAddress(Higgs_mass_, branchName_mass_);
    bai.setBranchAddress(Higgs_pdgId_, branchName_pdgId_);
  }
}

std::vector<GenHiggs> GenHiggsReader::read() const
{
  const GenHiggsReader * const gInstance = instances_[branchName_obj_];
  assert(gInstance);

  const UInt_t nHiggses = gInstance->nHiggses_;
  if(nHiggses > max_nHiggses_)
  {
    throw cmsException(this)
      << "Number of Higgses stored in Ntuple = " << nHiggses << ", exceeds max_nHiggses = " << max_nHiggses_ << " !!\n";
  }

  std::vector<GenHiggs> Higgses;
  if(nHiggses > 0)
  {
    Higgses.reserve(nHiggses);
    for(UInt_t idxHiggs = 0; idxHiggs < nHiggses; ++idxHiggs)
    {
      Higgses.push_back({
        gInstance->Higgs_pt_[idxHiggs],
        gInstance->Higgs_eta_[idxHiggs],
        gInstance->Higgs_phi_[idxHiggs],
        gInstance->Higgs_mass_[idxHiggs],
        gInstance->Higgs_pdgId_[idxHiggs],
      });
    }
  }
  return Higgses;
}
