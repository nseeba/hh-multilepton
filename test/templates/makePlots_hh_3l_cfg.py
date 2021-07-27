import FWCore.ParameterSet.Config as cms

from hhAnalysis.multilepton.configs.makePlots_cfi import process

process.makePlots.processesBackground = cms.vstring(["WW", "WZ", "ZZ", "TT", "TTZ", "TTW", "TTWW", "VH", "TH", "TTH", "DY", "W", "Other", "Convs", "data_fakes"])



process.makePlots.distributions = cms.VPSet(
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/m3l'),
    xAxisTitle = cms.string('m(3l) [GeV]'),
    yAxisTitle = cms.string('dN/dm'),
  ),   
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dihiggsVisMass_sel'),
    xAxisTitle = cms.string('m(3l + 2j) [GeV]'),
    yAxisTitle = cms.string('dN/dm'),
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dihiggsVisMass_sel_inclusive1j'),
    xAxisTitle = cms.string('m(3l + 2or1j) [GeV]'),
    yAxisTitle = cms.string('dN/dm'),
  ),
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dihiggsMass'),
    xAxisTitle = cms.string('m(3l + 2j + E_{T}^{Missing}) [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),    
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dihiggsMass_inclusive1j'),
    xAxisTitle = cms.string('m(3l + 2or1j + E_{T}^{Missing}) [GeV]'),
    yAxisTitle = cms.string('dN/dm [1/GeV]')
  ),    
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/mSFOS2l_closestToZ'),
    xAxisTitle = cms.string('m(2l OSSF) [GeV]'),
    yAxisTitle = cms.string('dN/dm'),
    xMin = cms.double(70),
    xMax = cms.double(110.0),      
  ),   
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LeptonIdx3_AK4jNear_Approach2'),
    xAxisTitle = cms.string('#Delta R_{min}(l_{Idx3}, AK4 jet)'),
    yAxisTitle = cms.string('dN/#Delta R'),
    xMin = cms.double(0),
    xMax = cms.double(7.0),      
  ),   
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_LeptonIdx3_2j_inclusive1j_Approach2'),
    xAxisTitle = cms.string('#Delta R_{min}(l_{Idx3}, 2j)'),
    yAxisTitle = cms.string('dN/#Delta R'),
    xMin = cms.double(0),
    xMax = cms.double(7.0),      
  ),   
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_los_min'),
    xAxisTitle = cms.string('#Delta R_{min}(2l OSSF)'),
    yAxisTitle = cms.string('dN/#Delta R'),
    xMin = cms.double(0),
    xMax = cms.double(7.0),      
  ),   
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/dr_los_max'),
    xAxisTitle = cms.string('#Delta R_{max}(2l OSSF)'),
    yAxisTitle = cms.string('dN/#Delta R'),
    xMin = cms.double(0),
    xMax = cms.double(7.0),      
  ),   
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/numSameFlavor_OS_3l'),
    xAxisTitle = cms.string('No. of OSSF 2l'),
    yAxisTitle = cms.string('dN'),
    xMin = cms.double(-0.5),
    xMax = cms.double(2.5),      
  ),   
  cms.PSet(
    histogramName = cms.string('sel/evt/$PROCESS/met_LD'),
    xAxisTitle = cms.string('E_{T}^{missing} LD [GeV]'),
    yAxisTitle = cms.string('dN/dE_{T}^{missing}'),
  ),
    
)

