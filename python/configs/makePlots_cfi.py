import FWCore.ParameterSet.Config as cms

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(),
)

scaleSignal = 10

process.makePlots = cms.PSet(
    pluginType = cms.string("Plotter_HH"),

    applyRebinning = cms.bool(True),
    #apply_fixed_rebinning = cms.int32(2),
    apply_fixed_rebinning = cms.int32(8),
    apply_automatic_rebinning = cms.bool(True),
    minEvents_automatic_rebinning = cms.double(0.5),
    applyAutoBlinding = cms.bool(True),
    divideByBinWidth = cms.bool(False),
    processData = cms.string("data_obs"),
    processesBackground = cms.vstring(),
    processSignal = cms.string("signal_ggf_spin0_400_hh"),
    scaleSignal = cms.double(scaleSignal),
    legendEntrySignal = cms.string(str(scaleSignal) + "x Signal HH"),
    categories = cms.VPSet(),
    distributions = cms.VPSet(
        cms.PSet(
            histogramName = cms.string("sel/evt/$PROCESS/numJets"),
            xAxisTitle = cms.string("jet Multiplicity"),
            yAxisTitle = cms.string("Events")
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
            histogramName = cms.string("sel/evtYield/$PROCESS/evtYield"),
            xAxisTitle = cms.string("Run Period"),
            yAxisTitle = cms.string("Events / 1 fb^{-1}"),
            divideByBinWidth = cms.bool(False)
        ),
        cms.PSet(
            histogramName = cms.string('sel/evt/$PROCESS/HT'),
            xAxisTitle = cms.string('H_{T} [GeV]'),
            yAxisTitle = cms.string('events')
        ),
        cms.PSet(
            histogramName = cms.string('sel/evt/$PROCESS/STMET'),
            xAxisTitle = cms.string('S_{T}^{MET} [GeV]'),
            yAxisTitle = cms.string('dN/dS_{T}^{MET} [1/GeV]')
        ),
    ),

    nuisanceParameters = cms.PSet(
        normalization = cms.PSet(
            TTH = cms.string("1.0 +/- 0.07"),
            tHq = cms.string("1.0 +/- 0.07"),
            tHW = cms.string("1.0 +/- 0.08"),
            TT = cms.string("1.0 +/- 0.06"),
            TTW = cms.string("1.0 +/- 0.14"),
            TTWW = cms.string("1.0 +/- 0.20"),
            TTZ = cms.string("1.0 +/- 0.12"),
            Other = cms.string("1.0 +/- 0.50"),
            VH = cms.string("1.0 +/- 0.07"),
            WH = cms.string("1.0 +/- 0.07"),
            ZH = cms.string("1.0 +/- 0.07"),
            WW = cms.string("1.0 +/- 0.20"),
            ggZZ = cms.string("1.0 +/- 0.30"),
            qqZZ = cms.string("1.0 +/- 0.04"),
            WZ = cms.string("1.0 +/- 0.04"),
            DY = cms.string("1.0 +/- 0.20"),
            W = cms.string("1.0 +/- 0.20"),
            ggH = cms.string("1.0 +/- 0.09"),
            qqH = cms.string("1.0 +/- 0.04"),
            TTWH = cms.string("1.0 +/- 0.20"),
            TTZH = cms.string("1.0 +/- 0.20"),
            data_fakes = cms.string("1.0 +/- 0.30"),
            data_flips = cms.string("1.0 +/- 0.30"),
            flips_mc = cms.string("1.0 +/- 0.30"),
            Convs = cms.string("1.0 +/- 0.50"),            
            fakes_mc = cms.string("1.0 +/- 0.30"),
            #
            signal_ggf_spin0_250_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_260_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_270_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_280_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_300_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_320_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_350_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_400_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_450_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_500_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_550_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_600_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_650_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_700_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_750_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_800_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_850_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_900_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin0_1000_hh = cms.string("0.0 +/- 0.20"),
            #
            signal_ggf_spin2_250_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_260_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_270_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_280_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_300_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_320_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_350_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_400_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_450_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_500_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_550_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_600_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_650_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_700_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_750_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_800_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_850_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_900_hh = cms.string("0.0 +/- 0.20"),
            signal_ggf_spin2_1000_hh = cms.string("0.0 +/- 0.20"),
            #            
            signal_ggf_nonresonant_hh = cms.string("0.0 +/- 0.20"),
        ),
        shape = cms.PSet(
            CMS_ttHl_btag_HF = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_HFStats1 = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_HFStats2 = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_LF = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_LFStats1 = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_LFStats2 = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_cErr1 = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_btag_cErr2 = cms.string("0.00 +/- 1.00"),
            CMS_ttHl_JES = cms.string("0.00 +/- 1.00"),
        )
    ),
    showUncertainty = cms.bool(True),

    legendTextSize = cms.double(0.050),
    legendPosX = cms.double(0.570),
    legendPosY = cms.double(0.510),
    legendSizeX = cms.double(0.360),
    legendSizeY = cms.double(0.420),

    labelOnTop = cms.string(
        ("CMS Preliminary; %dx GGF#rightarrow X(400;spin0)#rightarrow HH#rightarrow " % scaleSignal) +
        "4W,2W2#tau,4#tau; %1.1f fb^{-1} at #sqrt{s} = 13 TeV"),
    intLumiData = cms.double(0.), # in units of fb^-1

    outputFileName = cms.string("")
)

# gen_mHH = cms.vdouble(250,260,270,280,300, 320,350,400,450,500,550,600,650,700,750,800,850,900,1000)
# nonRes_BMs = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
