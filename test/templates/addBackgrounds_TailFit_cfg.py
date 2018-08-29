import FWCore.ParameterSet.Config as cms

import os

process = cms.PSet()

process.fwliteInput = cms.PSet(
#    fileNames = cms.vstring('/hdfs/local/veelken/hhAnalysis/2017/2018Aug01v1/histograms/hh_2l_2tau/histograms_harvested_stage2_hh_2l_2tau_disabled_disabled_Tight_OS_with2016.root'),
    fileNames = cms.vstring('histograms_harvested_stage2_hh_2l_2tau_disabled_disabled_Tight_OS_with2016.root'),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(100000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('out.root')
)


process.addBackgrounds_TailFit = cms.PSet(
    InputDirPath  = cms.string("hh_2l_2tau_sumOS_Tight/sel/evt/"),
#            OutputDirPath  = cms.string("hh_2l_2tau_sumOS_Tight/sel/evt/"),
    processName = cms.string("fakes_data"),
    histogramName = cms.string("dihiggsMass"),

    apply_automatic_rebinning = cms.bool(True),
    minEvents_automatic_rebinning = cms.double(0.5),
    explicit_binning = cms.vdouble(),
#    explicit_binning = cms.vdouble(250., 270., 290., 310., 330., 350., 370., 390., 410., 430., 450., 470., 490., 510., 560., 610., 660., 710., 760., 810., 910., 1010., 1110., 1210., 1500.), ## FOR diHiggsMass (conservative)
#    explicit_binning = cms.vdouble(250., 270., 290., 310., 330., 350., 370., 390., 410., 430., 450., 470., 490., 510., 560., 610., 660., 710., 760., 810., 910., 1010., 1110., 1210., 1500.), ## FOR diHiggsMass (aggressive)

    nominal_fit_func = cms.PSet(
        FitfuncName   = cms.string("Exponential"), ## FIT WORKS !!
        FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                       
        FitParameters = cms.vdouble(2.68, -0.0001), # norm, exponent, offset                                                                                                                   
        ),

    alternate_fit_funcs = cms.VPSet(
        cms.PSet(
            FitfuncName   = cms.string("LegendrePolynomial3"), ## FIT WORKS !!
            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                       
            FitParameters = cms.vdouble(2.2, 0.0001, 0.0001, 0.0001), # par0, par1, par2, par3                                                                                             
            ),
#        cms.PSet(
#            FitfuncName   = cms.string("CrystalBall"), ## FIT FAILS !!
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                    
#            FitParameters = cms.vdouble(2.2, 0.7, 5.0, 300.0, 1.0), # norm, alpha, n, mu, sigma                                                                                           
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("ExponentialErf"), ## FIT FAILS !!
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                   
#            FitParameters = cms.vdouble(2.2, 0.1, 600.0, 100.0), # norm, exponent, mean, sigma                                                                                            
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("Gaussian"),  ## FIT FAILED !
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                    
#            FitParameters = cms.vdouble(2., 500.0, 200.0), # norm, mean, sigma                                                                                                                        
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("DoubleGaussian"), ## FIT FAILED !
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                      
#            FitParameters = cms.vdouble(5., 300.0, 50.0, 500.0, 100.0), # norm, mean0, sigma0, mean1, sigma1                                                                                             
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("TripleGaussian"), ## FIT FAILED !
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                
#            FitParameters = cms.vdouble(5., 300.0, 10.0, 2.0, 500.0, 50.0, 1000.0, 100.0), # norm, mean0, sigma0, norm1, mean1, sigma1, mean2, sigma2                                              
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("ExponentialGaussian"), ## FIT FAILED !
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                   
#            FitParameters = cms.vdouble(3., -0.001, 500.0, 10.0), # norm, exponent, mean, sigma                                                                                                           
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("DoubleExponentialGaussian"), ## FIT FAILED !
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                     
#            FitParameters = cms.vdouble(10.0, 6.0, -0.0001, 500.0, 50.0, 800.0, 100.0), # norm0, norm1, exponent, mean0, sigma0, mean1, sigma1                                             
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("ErfExponentialGaussian"), ## FIT FAILED !
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                   
#            FitParameters = cms.vdouble(10., -0.001, 500.0, 50.0, 800.0, 100.0), # norm0, exponent, mean0, sigma0, mean1, sigma1                                                                           
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("DoubleErfExponentialGaussian"), ## FIT FAILED !
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                
#            FitParameters = cms.vdouble(10., 6.0, -0.0001, 500.0, 50.0, 750.0, 100.0, 900.0, 150.0), # norm0, norm1, exponent, mean0, sigma0, mean1, sigma1, mean2, sigma2
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("Voigt"), ## FIT FAILED !
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                        
#            FitParameters = cms.vdouble(10., 500.0, 100.0), # norm, sigma, gamma       
#            ),
#        cms.PSet(
#            FitfuncName   = cms.string("DoubleGaussianVoigt"), ## FIT FAILED !
#            FitRange      = cms.vdouble(500., 1500.), # xmin, xmax                                                                                                                                  
#            FitParameters = cms.vdouble(10., 6.0, 100.0, 10.0, 150.0, 20.0, 180.0, 50.0), # norm0, norm1, sigma, gamma, mean0, sigma0, mean1, sigma1  
#            ),
     )





#    processData = cms.string("signal2l0g0j&2t0e0m0j"),
#    processLeptonFakes = cms.string("fakes_data"),
#    processesToSubtract = cms.vstring(
#        "TTl_plus_t",
#        "Raresl_plus_t",
#        "EWKl_plus_t",
#    ),

#    sysShifts = cms.vstring(
#      "central",
#      "CMS_ttHl_JESUp",
#      "CMS_ttHl_JESDown",
#      "CMS_ttHl_JERUp",
#      "CMS_ttHl_JERDown",
#      "CMS_ttHl_UnclusteredEnUp",
#      "CMS_ttHl_UnclusteredEnDown"
#    )
)
