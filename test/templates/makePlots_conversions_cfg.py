import FWCore.ParameterSet.Config as cms

from hhAnalysis.multilepton.configs.makePlots_cfi import process

process.makePlots.processesBackground = cms.vstring(["WW", "WZ", "ZZ", "TT", "TTZ", "TTW", "TTWW", "VH", "TH", "TTH", "DY", "W", "Other", "Convs", "data_fakes"])


process.makePlots.distributions = cms.VPSet(
  cms.PSet(
    histogramName = cms.string("sel/evt/$PROCESS/EventCounter"),
    xAxisTitle = cms.string("Event yield"),
    yAxisTitle = cms.string("Events")
  ),
  cms.PSet(
    histogramName = cms.string("sel/evtYield/$PROCESS/evtYield"),
    xAxisTitle = cms.string("Run Period"),
      yAxisTitle = cms.string("Events / 1 fb^{-1}"),
    divideByBinWidth = cms.bool(False)    
  ),
  cms.PSet(
    histogramName = cms.string("sel/evtYield/$PROCESS/evtYield_full"),
    xAxisTitle = cms.string("Run Period"),
    yAxisTitle = cms.string("Events"),
    divideByBinWidth = cms.bool(False)    
  ),
    
  cms.PSet(
    histogramName = cms.string("sel/evt/$PROCESS/numElectrons"),
    xAxisTitle = cms.string("electron Multiplicity"),
    yAxisTitle = cms.string("Events")
  ),
  cms.PSet(
    histogramName = cms.string("sel/evt/$PROCESS/numMuons"),
    xAxisTitle = cms.string("muon Multiplicity"),
    yAxisTitle = cms.string("Events")
  ),    
  cms.PSet(
    histogramName = cms.string("sel/evt/$PROCESS/nJetAK4"),
    xAxisTitle = cms.string("AK4 jet Multiplicity"),
    yAxisTitle = cms.string("Events")
  ),
  cms.PSet(
    histogramName = cms.string("sel/evt/$PROCESS/nJetAK8"),
    xAxisTitle = cms.string("AK8 jet Multiplicity"),
    yAxisTitle = cms.string("Events")
  ),
  cms.PSet(
    histogramName = cms.string("sel/evt/$PROCESS/nJetAK8_wSelectorAK8_Wjj"),
    xAxisTitle = cms.string("Multiplicity of AK8 jets w/ W#tightarrow jj selector"),
    yAxisTitle = cms.string("Events")
  ),

  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/sumLeptonCharge_3l'),
    xAxisTitle = cms.string('sumLeptonCharge_3l'),
    yAxisTitle = cms.string('dN')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/sumLeptonCharge_FullSel'),
    xAxisTitle = cms.string('sumLeptonCharge_FullSel'),
    yAxisTitle = cms.string('dN')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/numSameFlavor_OS_3l'),
    xAxisTitle = cms.string('numSameFlavor_OS_3l'),
    yAxisTitle = cms.string('dN')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/numSameFlavor_OS_FullPresel'),
    xAxisTitle = cms.string('numSameFlavor_OS_FullPresel'),
    yAxisTitle = cms.string('dN')
  ),
#    
    
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/lep1_pt'),
    xAxisTitle = cms.string('p_{T}(lep1) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T}')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/lep1_conePt'),
    xAxisTitle = cms.string('p_{T}(lep1) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T}')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/lep1_eta'),
    xAxisTitle = cms.string('#eta (lep1)'),
    yAxisTitle = cms.string('dN/d#eta')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mindr_lep1_jet'),
    xAxisTitle = cms.string('#Delta R(lep1, j)'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mT_MEtLep1'),
    xAxisTitle = cms.string('m_{T}(lep1 + MEt) [GeV]'),
    yAxisTitle = cms.string('dN/dm_{T}')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/lep2_pt'),
    xAxisTitle = cms.string('p_{T}(lep2) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T}')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/lep2_conePt'),
    xAxisTitle = cms.string('p_{T}(lep2) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T}')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/lep2_eta'),
    xAxisTitle = cms.string('#eta (lep2)'),
    yAxisTitle = cms.string('dN/d#eta')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mindr_lep2_jet'),
    xAxisTitle = cms.string('#Delta R(lep2, j)'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mT_MEtLep2'),
    xAxisTitle = cms.string('m_{T}(lep2 + MEt) [GeV]'),
    yAxisTitle = cms.string('dN/dm_{T}')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/lep3_pt'),
    xAxisTitle = cms.string('p_{T}(lep3) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T}')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/lep3_conePt'),
    xAxisTitle = cms.string('p_{T}(lep3) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T}')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/lep3_eta'),
    xAxisTitle = cms.string('#eta (lep3)'),
    yAxisTitle = cms.string('dN/d#eta')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mindr_lep3_jet'),
    xAxisTitle = cms.string('#Delta R(lep3, j)'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mT_MEtLep3'),
    xAxisTitle = cms.string('m_{T}(lep3 + MEt) [GeV]'),
    yAxisTitle = cms.string('dN/dm_{T}')
  ),
#------------------------------------------------------
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/jet1_pt'),
    xAxisTitle = cms.string('p_{T}(j1) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T}')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/jet2_pt'),
    xAxisTitle = cms.string('p_{T}(j2) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T}')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/jet1_m'),
    xAxisTitle = cms.string('m(j1) [GeV]'),
    yAxisTitle = cms.string('dN/dm')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/jet2_m'),
    xAxisTitle = cms.string('m(j2) [GeV]'),
    yAxisTitle = cms.string('dN/dm')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/jet1plus2pt'),
    xAxisTitle = cms.string('p_{T}(j1+j2) [GeV]'),
    yAxisTitle = cms.string('dN/dp_{T}')
  ),
#------------------------------------------------------
 cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/avg_dr_jet'),
    xAxisTitle = cms.string('Average #Delta(jj)'),
    yAxisTitle = cms.string('dN/d#Delta(jj)')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_Wjj'),
    xAxisTitle = cms.string('#Delta R(j1, j2)'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_l12'),
    xAxisTitle = cms.string('#Delta R(l1, l2)'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_l23'),
    xAxisTitle = cms.string('#Delta R(l2, l3)'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_l13'),
    xAxisTitle = cms.string('#Delta R(l1, l3)'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_lss'),
    xAxisTitle = cms.string('#Delta R(2lss)'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_los_min'),
    xAxisTitle = cms.string('#Delta_{min} R(2los)'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_los_max'),
    xAxisTitle = cms.string('#Delta_{max} R(2los)'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),


  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_WjjLepIdx3'),
    xAxisTitle = cms.string('#Delta R(j1+j2, l_{Idx3})'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_Wjet1LepIdx3'),
    xAxisTitle = cms.string('#Delta R(j1, l_{Idx3})'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_Wjet2LepIdx3'),
    xAxisTitle = cms.string('#Delta R(j2, l_{Idx3})'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LepIdx3WjetNear'),
    xAxisTitle = cms.string('#Delta_{min} R(j, l_{Idx3})'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LepIdx3WjetFar'),
    xAxisTitle = cms.string('#Delta_{max} R(j, l_{Idx3})'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
#------------------------------------------------------


  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/met'),
    xAxisTitle = cms.string('E_{T}^{Missing} [GeV]'),
    yAxisTitle = cms.string('dN/dE_{T}^{Missing} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mht'),
    xAxisTitle = cms.string('H_{T}^{Missing} [GeV]'),
    yAxisTitle = cms.string('dN/dH_{T}^{Missing} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/met_LD'),
    xAxisTitle = cms.string('MET LD [GeV]'),
    yAxisTitle = cms.string('dN/dMET LD [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/HT'),
    xAxisTitle = cms.string('H_{T}^{Missing} w/o considering #tau_{h} [GeV]'),
    yAxisTitle = cms.string('dN/dH_{T}^{Missing [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/STMET'),
    xAxisTitle = cms.string('STMET'),
    yAxisTitle = cms.string('dN/dSTMET [1/GeV]')
  ),
#------------------------------------------------------

  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mSFOS2l'),
    xAxisTitle = cms.string('m(2los) [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/WTojjMass'),
    xAxisTitle = cms.string('m(jj) [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]'),
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dihiggsVisMass_sel'),
    xAxisTitle = cms.string('m(3l + 2j) [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dihiggsMass'),
    xAxisTitle = cms.string('m(3l + 2j + E_{T}^{Missing}) [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),
#------------------------------------------------------


  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mT_LeptonIdx1_Met_Approach0'),
    xAxisTitle = cms.string('m_{T}(l_{Idx1} + MEt) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/dm_{T} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mT_LeptonIdx2_Met_Approach0'),
    xAxisTitle = cms.string('m_{T}(l_{Idx2} + MEt) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/dm_{T} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mT_LeptonIdx3_Met_Approach0'),
    xAxisTitle = cms.string('m_{T}(l_{Idx3} + MEt) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/dm_{T} [1/GeV]')
  ),


  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/m_LeptonIdx1_LeptonIdx2_Approach0'),
    xAxisTitle = cms.string('m(l_{Idx1} + l_{Idx2}) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/m_LeptonIdx2_LeptonIdx3_Approach0'),
    xAxisTitle = cms.string('m(l_{Idx2} + l_{Idx3}) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/m_LeptonIdx1_LeptonIdx3_Approach0'),
    xAxisTitle = cms.string('m(l_{Idx1} + l_{Idx3}) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),

  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dPhi_LeptonIdx1_LeptonIdx2_Approach0'),
    xAxisTitle = cms.string('#Delta#Phi(l_{Idx1}, l_{Idx2}) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta#Phi [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dPhi_LeptonIdx2_LeptonIdx3_Approach0'),
    xAxisTitle = cms.string('#Delta#Phi(l_{Idx2}, l_{Idx3}) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta#Phi [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dPhi_LeptonIdx1_LeptonIdx3_Approach0'),
    xAxisTitle = cms.string('#Delta#Phi(l_{Idx1}, l_{Idx3}) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta#Phi [1/GeV]')
  ),

  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LeptonIdx1_LeptonIdx2_Approach0'),
    xAxisTitle = cms.string('#Delta R(l_{Idx1}, l_{Idx2}) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta R [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LeptonIdx2_LeptonIdx3_Approach0'),
    xAxisTitle = cms.string('#Delta R(l_{Idx2}, l_{Idx3}) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta R [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LeptonIdx1_LeptonIdx3_Approach0'),
    xAxisTitle = cms.string('#Delta R(l_{Idx1}, l_{Idx3}) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta R [1/GeV]')
  ),

  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/m_LeptonIdx3_Jet1_Approach0'),
    xAxisTitle = cms.string('m(l_{Idx3} + j1) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LeptonIdx3_Jet1_Approach0'),
    xAxisTitle = cms.string('#Delta R(l_{Idx3} + j1) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/m_LeptonIdx3_JetNear_Approach0'),
    xAxisTitle = cms.string('m(l_{Idx3} + nearest jet) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LeptonIdx3_JetNear_Approach0'),
    xAxisTitle = cms.string('#Delta R(l_{Idx3} + nearest jet) Approach0 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
#------------------------------------------------------

  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mT_LeptonIdx1_Met_Approach2'),
    xAxisTitle = cms.string('m_{T}(l_{Idx1} + MEt) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/dm_{T} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mT_LeptonIdx2_Met_Approach2'),
    xAxisTitle = cms.string('m_{T}(l_{Idx2} + MEt) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/dm_{T} [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mT_LeptonIdx3_Met_Approach2'),
    xAxisTitle = cms.string('m_{T}(l_{Idx3} + MEt) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/dm_{T} [1/GeV]')
  ),


  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/m_LeptonIdx1_LeptonIdx2_Approach2'),
    xAxisTitle = cms.string('m(l_{Idx1} + l_{Idx2}) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/m_LeptonIdx2_LeptonIdx3_Approach2'),
    xAxisTitle = cms.string('m(l_{Idx2} + l_{Idx3}) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/m_LeptonIdx1_LeptonIdx3_Approach2'),
    xAxisTitle = cms.string('m(l_{Idx1} + l_{Idx3}) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),

  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dPhi_LeptonIdx1_LeptonIdx2_Approach2'),
    xAxisTitle = cms.string('#Delta#Phi(l_{Idx1}, l_{Idx2}) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta#Phi [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dPhi_LeptonIdx2_LeptonIdx3_Approach2'),
    xAxisTitle = cms.string('#Delta#Phi(l_{Idx2}, l_{Idx3}) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta#Phi [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dPhi_LeptonIdx1_LeptonIdx3_Approach2'),
    xAxisTitle = cms.string('#Delta#Phi(l_{Idx1}, l_{Idx3}) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta#Phi [1/GeV]')
  ),

  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LeptonIdx1_LeptonIdx2_Approach2'),
    xAxisTitle = cms.string('#Delta R(l_{Idx1}, l_{Idx2}) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta R [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LeptonIdx2_LeptonIdx3_Approach2'),
    xAxisTitle = cms.string('#Delta R(l_{Idx2}, l_{Idx3}) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta R [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LeptonIdx1_LeptonIdx3_Approach2'),
    xAxisTitle = cms.string('#Delta R(l_{Idx1}, l_{Idx3}) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta R [1/GeV]')
  ),

  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/m_LeptonIdx3_Jet1_Approach2'),
    xAxisTitle = cms.string('m(l_{Idx3} + j1) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LeptonIdx3_Jet1_Approach2'),
    xAxisTitle = cms.string('#Delta R(l_{Idx3} + j1) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/m_LeptonIdx3_JetNear_Approach2'),
    xAxisTitle = cms.string('m(l_{Idx3} + nearest jet) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LeptonIdx3_JetNear_Approach2'),
    xAxisTitle = cms.string('#Delta R(l_{Idx3} + nearest jet) Approach2 [GeV]'),
    yAxisTitle = cms.string('dN/d#Delta R')
  ),
#------------------------------------------------------    
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mvaOutput_xgb_conversions_SUMBk_HH'),
    xAxisTitle = cms.string('BDT score'),
    yAxisTitle = cms.string('dN/dBDT')
  ), 
)




process.makePlots.pluginType = cms.string("Plotter_HHTo3l")

process.makePlots.legendTextSize = cms.double(0.045)
process.makePlots.legendPosX = cms.double(0.30)
process.makePlots.legendPosY = cms.double(0.510)
process.makePlots.legendSizeX = cms.double(0.700)
process.makePlots.legendSizeY = cms.double(0.420)

scaleSignal = 30
process.makePlots.scaleSignal = cms.double(scaleSignal)

mass_HH = 400
spin_XToHH = 0

process.makePlots.processSignal = cms.string("signal_spin%d_%d_hh" % (spin_XToHH, mass_HH))
process.makePlots.legendEntrySignal = cms.string("%dx X(%d,spin%d)#rightarrow HH" % (scaleSignal,mass_HH,spin_XToHH))
