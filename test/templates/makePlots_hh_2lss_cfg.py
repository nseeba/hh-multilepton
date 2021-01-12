import FWCore.ParameterSet.Config as cms

from hhAnalysis.multilepton.configs.makePlots_cfi import process

process.makePlots.distributions.extend([
    cms.PSet(
        histogramName = cms.string('sel/electrons/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('e_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/electrons/$PROCESS/eta'),
        xAxisTitle = cms.string('e_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadElectron/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading e_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadElectron/$PROCESS/eta'),
        xAxisTitle = cms.string('leading e_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadElectron/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('subleading e_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadElectron/$PROCESS/eta'),
        xAxisTitle = cms.string('subleading e_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/muons/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('#mu_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/muons/$PROCESS/eta'),
        xAxisTitle = cms.string('#mu_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadMuon/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading #mu_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadMuon/$PROCESS/eta'),
        xAxisTitle = cms.string('leading #mu_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadMuon/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('subleading #mu_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadMuon/$PROCESS/eta'),
        xAxisTitle = cms.string('subleading #mu_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/jets/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('jet_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/jets/$PROCESS/eta'),
        xAxisTitle = cms.string('jet_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadJet/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading jet_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadJet/$PROCESS/eta'),
        xAxisTitle = cms.string('leading jet_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadJet/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('subleading jet_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadJet/$PROCESS/eta'),
        xAxisTitle = cms.string('subleading jet_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/leptonPairMass'),
        xAxisTitle = cms.string('m_{ll} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{ll} [1/GeV]')
    ),
   cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/electronPairMass'),
        xAxisTitle = cms.string('m_{ee} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{ee} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/muonPairMass'),
        xAxisTitle = cms.string('m_{#mu#mu} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{#mu#mu} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/leptonPairCharge'),
        xAxisTitle = cms.string('lepton charge sum'),
        yAxisTitle = cms.string('N')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dihiggsVisMass'),
        xAxisTitle = cms.string('m_{HH} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dihiggsMass_wMet'),
        xAxisTitle = cms.string('m_{HH} with Met [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/jetMass'),
        xAxisTitle = cms.string('m_{jjjj} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{jjjj} [1/GeV]')
    ),
#    cms.PSet(
#        histogramName = cms.string('sel/evt/$PROCESS/BDTOutput_SUM'),
#        xAxisTitle = cms.string('BDT Output'),
#        yAxisTitle = cms.string('N')
#    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/BDTOutput_SUM_gen_mHH_400'),
        xAxisTitle = cms.string('BDT Output'),
        yAxisTitle = cms.string('N')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/BDTOutput_SUM_gen_mHH_700'),
        xAxisTitle = cms.string('BDT Output'),
        yAxisTitle = cms.string('N')
    ),
])


process.makePlots.distributions = cms.VPSet(
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/nElectrons_in_2lss'),
        xAxisTitle = cms.string('No. of electrons'),
        yAxisTitle = cms.string('dN')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/leptonPairCharge'),
        xAxisTitle = cms.string('Sum of leptons charge'),
        yAxisTitle = cms.string('dN')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/leptonPairMass'),
        xAxisTitle = cms.string('m(2lSS) [GeV]'),
        yAxisTitle = cms.string('dN/dm [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_ll'),
        xAxisTitle = cms.string('#Delta R(2lSS)'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dPhi_ll'),
        xAxisTitle = cms.string('#Delta #Phi(2lSS)'),
        yAxisTitle = cms.string('dN/d#Delta #Phi')
    ),
    #
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/numJets'),
        xAxisTitle = cms.string('No. of AK4 jets'),
        yAxisTitle = cms.string('dN')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/nAK8_w2subjets'),
        xAxisTitle = cms.string('No. of AK8 jets'),
        yAxisTitle = cms.string('dN')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/nWJets_selected'),
        xAxisTitle = cms.string('No. of selected W#rightarrow jj jets'),
        yAxisTitle = cms.string('dN')
    ),
    #
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mass_2j_fromW1'),
        xAxisTitle = cms.string('m(jj from W_{1}) [GeV]'),
        yAxisTitle = cms.string('dN/dm [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mass_2j_fromW2'),
        xAxisTitle = cms.string('m(jj from W_{2}) [GeV]'),
        yAxisTitle = cms.string('dN/dm [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_2j_fromW1'),
        xAxisTitle = cms.string('#Delta R(jj from W_{1})'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_2j_fromW2'),
        xAxisTitle = cms.string('#Delta R(jj from W_{2})'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    #
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_Wjets_min'),
        xAxisTitle = cms.string('#Delta R_{min}(jj)'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_Wjets_max'),
        xAxisTitle = cms.string('#Delta R_{max}(jj)'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_l_Wjets_min'),
        xAxisTitle = cms.string('#Delta R_{min}(l, j)'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_l_Wjets_max'),
        xAxisTitle = cms.string('#Delta R_{max}(l, j)'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_l_AK4jets_min'),
        xAxisTitle = cms.string('#Delta R_{min}(l, AK4 jet)'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_l_AK4jets_max'),
        xAxisTitle = cms.string('#Delta R_{max}(l, AK4 jet)'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_l_leadWjet_min'),
        xAxisTitle = cms.string('#Delta R_{min}(l, leading p_{T} selected jet)'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_l_leadWjet_max'),
        xAxisTitle = cms.string('#Delta R_{max}(l, leading p_{T} selected jet)'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_l_leadAK4jet_min'),
        xAxisTitle = cms.string('#Delta R_{min}(l, leading p_{T} AK4 jet)'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_l_leadAK4jet_max'),
        xAxisTitle = cms.string('#Delta R_{max}(l, leading p_{T} AK4 jet)'),
        yAxisTitle = cms.string('dN/d#Delta R')
    ),
    #
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/met'),
        xAxisTitle = cms.string('E_{T}^{Missing} [GeV]'),
        yAxisTitle = cms.string('dN/dE_{T}^{Missing} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mht'),
        xAxisTitle = cms.string('H_{T}^{Missing} [GeV]'),
        yAxisTitle = cms.string('dN/dE_{T}^{Missing} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/met_LD'),
        xAxisTitle = cms.string('E_{T}^{Missing} LD [GeV]'),
        yAxisTitle = cms.string('dN/dE_{T}^{Missing} LD [1/GeV]')
    ),
    #
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dihiggsVisMass'),
        xAxisTitle = cms.string('visible m_{HH} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dihiggsMass_wMet'),
        xAxisTitle = cms.string('m_{HH} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mT_lep1_met'),
        xAxisTitle = cms.string('m_{T}(leading l + MET) [GeV]'),
        yAxisTitle = cms.string('dN/dm_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mT_lep2_met'),
        xAxisTitle = cms.string('m_{T}(subleading l + MET) [GeV]'),
        yAxisTitle = cms.string('dN/dm_{T} [1/GeV]')
    ),

    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/eventCategory'),
        xAxisTitle = cms.string('Event category'),
        yAxisTitle = cms.string('dN')
    ), 
)
