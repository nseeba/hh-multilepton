import logging, re

from tthAnalysis.HiggsToTauTau.configs.analyzeConfig import *
from tthAnalysis.HiggsToTauTau.jobTools import create_if_not_exists
from tthAnalysis.HiggsToTauTau.analysisTools import initDict, getKey, create_cfg, createFile, generateInputFileList

def get_lepton_selection_and_frWeight(lepton_selection, lepton_frWeight):
  lepton_selection_and_frWeight = lepton_selection
  if lepton_selection.startswith("Fakeable"):
    if lepton_frWeight == "enabled":
      lepton_selection_and_frWeight += "_wFakeRateWeights"
    elif lepton_frWeight == "disabled":
      lepton_selection_and_frWeight += "_woFakeRateWeights"
  lepton_selection_and_frWeight = lepton_selection_and_frWeight.replace("|", "_")
  return lepton_selection_and_frWeight

def getHistogramDir(lepton_selection, lepton_frWeight, leptonChargeSelection):
  histogramDir = "hh_2lss_%s_%s" % (leptonChargeSelection, lepton_selection)
  if lepton_selection.find("Fakeable") != -1:
    if lepton_frWeight == "enabled":
      histogramDir += "_wFakeRateWeights"
    elif lepton_frWeight == "disabled":
      histogramDir += "_woFakeRateWeights"
  return histogramDir

class analyzeConfig_hh_2lss(analyzeConfig):
  """Configuration metadata needed to run analysis in a single go.

  Sets up a folder structure by defining full path names; no directory creation is delegated here.

  Args specific to analyzeConfig_hh_2lss:
    lepton_selection: either `Tight`, `Loose` or `Fakeable`

  See $CMSSW_BASE/src/tthAnalysis/HiggsToTauTau/python/analyzeConfig.py
  for documentation of further Args.

  """
  def __init__(self,
        configDir,
        outputDir,
        executable_analyze,
        cfgFile_analyze,
        samples,
        lep_mva_wp,
        hadTauVeto_selection,
        applyFakeRateWeights,
        central_or_shifts,
        max_files_per_job,
        era,
        use_lumi,
        lumi,
        check_output_files,
        running_method,
        num_parallel_jobs,
        executable_addBackgrounds,
        executable_addBackgroundJetToTauFakes,
        histograms_to_fit,
        select_rle_output         = False,
        select_root_output        = False,
        #do_sync                   = False,
        verbose                   = False,
        dry_run                   = False,
        isDebug                   = False,
        #rle_select                = '',
        use_nonnominal            = False,
        hlt_filter                = False,
        use_home                  = True,
      ):
    analyzeConfig.__init__(self,
      configDir                 = configDir,
      outputDir                 = outputDir,
      executable_analyze        = executable_analyze,
      channel                   = "hh_2lss",
      samples                   = samples,
      central_or_shifts         = central_or_shifts,
      max_files_per_job         = max_files_per_job,
      era                       = era,
      use_lumi                  = use_lumi,
      lumi                      = lumi,
      check_output_files        = check_output_files,
      running_method            = running_method,
      num_parallel_jobs         = num_parallel_jobs,
      histograms_to_fit         = histograms_to_fit,
      #triggers                  = [ '1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '1e2mu', '2e1mu' ],
      triggers                  = [ '1e', '1mu', '2e', '2mu', '1e1mu' ],
      lep_mva_wp                = lep_mva_wp,
      #executable_prep_dcard     = executable_prep_dcard,
      #executable_add_syst_dcard = executable_add_syst_dcard,
      #do_sync                   = do_sync,
      verbose                   = verbose,
      dry_run                   = dry_run,
      isDebug                   = isDebug,
      use_home                  = use_home,
      template_dir              = os.path.join(os.getenv('CMSSW_BASE'), 'src', 'hhAnalysis', 'multilepton', 'test', 'templates'),
    )

    self.lepton_selections = [ "Tight", "Fakeable" ]
    self.lepton_frWeights = [ "enabled", "disabled" ]
    self.hadTauVeto_selection_part2 = hadTauVeto_selection
    self.applyFakeRateWeights = applyFakeRateWeights
    run_mcClosure = 'central' not in self.central_or_shifts or len(central_or_shifts) > 1 or self.do_sync
    if self.era != '2017':
      logging.warning('mcClosure for lepton FR not possible for era %s' % self.era)
      run_mcClosure = False
    if run_mcClosure:
      # Run MC closure jobs only if the analysis is run w/ (at least some) systematic uncertainties
      # self.lepton_and_hadTau_selections.extend([ "Fakeable_mcClosure_all" ]) #TODO
      pass

    #self.lepton_genMatches = [ "3l0g0j", "2l1g0j", "2l0g1j", "1l2g0j", "1l1g1j", "1l0g2j", "0l3g0j", "0l2g1j", "0l1g2j", "0l0g3j" ]
    self.lepton_genMatches = [ "2l0g0j", "1l1g0j", "1l0g1j", "0l2g0j", "0l1g1j", "0l0g2j" ]

    self.apply_leptonGenMatching = None
    self.lepton_genMatches_nonfakes = []
    self.lepton_genMatches_conversions = []
    self.lepton_genMatches_fakes = []
    if applyFakeRateWeights == "2lepton":
      self.apply_leptonGenMatching = True
      for lepton_genMatch in self.lepton_genMatches:
        if lepton_genMatch.endswith("0g0j"):
          self.lepton_genMatches_nonfakes.append(lepton_genMatch)
        elif lepton_genMatch.endswith("0j"):
          self.lepton_genMatches_conversions.append(lepton_genMatch)
        else:
          self.lepton_genMatches_fakes.append(lepton_genMatch)
      if run_mcClosure:
        self.lepton_selections.extend([ "Fakeable_mcClosure_e", "Fakeable_mcClosure_m" ])
    else:
      raise ValueError("Invalid Configuration parameter 'applyFakeRateWeights' = %s !!" % applyFakeRateWeights)

    self.leptonChargeSelections = [ "SS", "OS" ]

    self.executable_addBackgrounds = executable_addBackgrounds
    self.executable_addFakes = executable_addBackgroundJetToTauFakes
    self.executable_addFlips = "addBackgroundLeptonFlips"

    self.nonfake_backgrounds = [ "ZZ", "WZ", "WW", "TT", "TTW", "TTWW", "TTZ", "DY", "W", "Other", "VH", "TTH", "TH" ]

    self.cfgFile_analyze = os.path.join(self.template_dir, cfgFile_analyze)
    self.prep_dcard_processesToCopy = [ "data_obs" ] + self.nonfake_backgrounds + [ "conversions", "fakes_data", "fakes_mc" ]
    self.inputFiles_hadd_stage1_6 = []
    self.outputFile_hadd_stage1_6 = None
    self.cfgFile_addFlips = os.path.join(self.template_dir, "addBackgroundLeptonFlips_cfg.py")
    self.jobOptions_addFlips = {}
    self.prep_dcard_signals = []
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      sample_category = sample_info["sample_category"]
      if sample_category.startswith("signal"):
        self.prep_dcard_signals.append(sample_category)
    self.histogramDir_prep_dcard = "hh_2lss_SS_Tight"
    self.histogramDir_prep_dcard_OS = "hh_2lss_OS_Tight"
    self.make_plots_backgrounds = [ "ZZ", "WZ", "WW", "TT", "TTW", "TTWW", "TTZ", "Other", "VH", "TTH", "TH" ] + [ "conversions", "fakes_data" ]
    self.mass_point = 400
    self.make_plots_signal = "signal_radion_%d" % self.mass_point
    self.cfgFile_make_plots = os.path.join(self.template_dir, "makePlots_hh_2lss_cfg.py")
    self.cfgFile_make_plots_mcClosure = os.path.join(self.template_dir, "makePlots_mcClosure_hh_2lss_cfg.py") #TODO

    self.select_rle_output = select_rle_output
    self.select_root_output = select_root_output
    #self.rle_select = rle_select
    self.use_nonnominal = use_nonnominal
    self.hlt_filter = hlt_filter

    #self.isBDTtraining = False

  #def set_BDT_training(self):
    """Run analysis with loose selection criteria for leptons,
       for the purpose of preparing event list files for BDT training.
    """
    #self.lepton_selections = [ "forBDTtraining" ]
    #self.lepton_frWeights  = [ "disabled" ]
    #self.isBDTtraining     = True

  def createCfg_analyze(self, jobOptions, sample_info, lepton_selection):
    """Create python configuration file for the analyze_hh_2lss executable (analysis code)

    Args:
      inputFiles: list of input files (Ntuples)
      outputFile: output file of the job -- a ROOT file containing histogram
      process: either `TT`, `TTW`, `TTZ`, `EWK`, `Rares`, `data_obs`, `ttH_hww`, 'ttH_hzg', 'ttH_hmm', `ttH_hzz` or `ttH_htt`
      is_mc: flag indicating whether job runs on MC (True) or data (False)
      lumi_scale: event weight (= xsection * luminosity / number of events)
      central_or_shift: either 'central' or one of the systematic uncertainties defined in $CMSSW_BASE/src/hhAnalysis/multilepton/bin/analyze_hh_2lss.cc
    """
    lepton_frWeight = "disabled" if jobOptions['applyFakeRateWeights'] == "disabled" else "enabled"
    jobOptions['histogramDir'] = getHistogramDir(lepton_selection, lepton_frWeight, jobOptions['leptonChargeSelection'])
    if 'mcClosure' in lepton_selection:
      self.mcClosure_dir['%s_%s' % (lepton_selection, jobOptions['leptonChargeSelection'])] = jobOptions['histogramDir']

    self.set_leptonFakeRateWeightHistogramNames(jobOptions['central_or_shift'], lepton_selection)
    jobOptions['leptonFakeRateWeight.inputFileName'] = self.leptonFakeRateWeight_inputFile
    jobOptions['leptonFakeRateWeight.histogramName_e'] = self.leptonFakeRateWeight_histogramName_e
    jobOptions['leptonFakeRateWeight.histogramName_mu'] = self.leptonFakeRateWeight_histogramName_mu

    lines = super(analyzeConfig_hh_2lss, self).createCfg_analyze(jobOptions, sample_info)
    create_cfg(self.cfgFile_analyze, jobOptions['cfgFile_modified'], lines)

  def createCfg_addFlips(self, jobOptions):
    """Create python configuration file for the addBackgroundLeptonFlips executable (data-driven estimation of 'Flips' backgrounds)

       Args:
         inputFiles: input file (the ROOT file produced by hadd_stage1)
         outputFile: output file of the job
    """
    lines = []
    lines.append("process.fwliteInput.fileNames = cms.vstring('%s')" % jobOptions['inputFile'])
    lines.append("process.fwliteOutput.fileName = cms.string('%s')" % os.path.basename(jobOptions['outputFile']))
    lines.append("process.addBackgroundLeptonFlips.categories = cms.VPSet(")
    lines.append("    cms.PSet(")
    lines.append("        signal = cms.string('%s')," % jobOptions['category_signal'])
    lines.append("        sideband = cms.string('%s')" % jobOptions['category_sideband'])
    lines.append("    )")
    lines.append(")")
    processesToSubtract = [ "fakes_data" ]
    processesToSubtract.extend([ nonfake_background for nonfake_background in self.nonfake_backgrounds if nonfake_background != "TT" ])
    processesToSubtract.extend([ "%s_conversion" % nonfake_background for nonfake_background in self.nonfake_backgrounds ])
    lines.append("process.addBackgroundLeptonFlips.processesToSubtract = cms.vstring(%s)" % processesToSubtract)
    lines.append("process.addBackgroundLeptonFlips.sysShifts = cms.vstring(%s)" % self.central_or_shifts)
    create_cfg(self.cfgFile_addFlips, jobOptions['cfgFile_modified'], lines)

  def addToMakefile_hadd_stage1_6(self, lines_makefile):
    """Adds the commands to Makefile that are necessary for building the intermediate histogram file
       that is used as input for data-driven background estimation.
    """
    self.addToMakefile_hadd(lines_makefile, { 'all' : self.inputFiles_hadd_stage1_6 }, { 'all' : self.outputFile_hadd_stage1_6 }, "stage1_6")

  def addToMakefile_addFlips(self, lines_makefile):
    if self.is_sbatch:
      lines_makefile.append("sbatch_addFlips: %s" % " ".join([ jobOptions['inputFile'] for jobOptions in self.jobOptions_addFlips.values() ]))
      lines_makefile.append("\t%s %s" % ("python", self.sbatchFile_addFlips))
      lines_makefile.append("")
    for jobOptions in self.jobOptions_addFlips.values():
      if self.is_makefile:
        lines_makefile.append("%s: %s" % (jobOptions['outputFile'], jobOptions['inputFile']))
        lines_makefile.append("\t%s %s &> %s" % (self.executable_addFlips, jobOptions['cfgFile_modified'], jobOptions['logFile']))
        lines_makefile.append("")
      elif self.is_sbatch:
        lines_makefile.append("%s: %s" % (jobOptions['outputFile'], "sbatch_addFlips"))
        lines_makefile.append("\t%s" % ":") # CV: null command
        lines_makefile.append("")
      self.filesToClean.append(jobOptions['outputFile'])

  def addToMakefile_backgrounds_from_data(self, lines_makefile):
    self.addToMakefile_addBackgrounds(lines_makefile, "sbatch_addBackgrounds", self.sbatchFile_addBackgrounds, self.jobOptions_addBackgrounds)
    self.addToMakefile_addBackgrounds(lines_makefile, "sbatch_addBackgrounds_sum", self.sbatchFile_addBackgrounds_sum, self.jobOptions_addBackgrounds_sum)
    self.addToMakefile_hadd_stage1_5(lines_makefile)
    self.addToMakefile_addFakes(lines_makefile)
    self.addToMakefile_hadd_stage1_6(lines_makefile)
    self.addToMakefile_addFlips(lines_makefile)

  def create(self):
    """Creates all necessary config files and runs the complete analysis workfow -- either locally or on the batch system
    """

    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"] or sample_info["sample_category"] in [ "additional_signal_overlap", "background_data_estimate" ]:
        continue
      process_name = sample_info["process_name_specific"]
      for lepton_selection in self.lepton_selections:
        for lepton_frWeight in self.lepton_frWeights:
          if lepton_frWeight == "enabled" and not lepton_selection.startswith("Fakeable"):
            continue
          lepton_selection_and_frWeight = get_lepton_selection_and_frWeight(lepton_selection, lepton_frWeight)
          for leptonChargeSelection in self.leptonChargeSelections:
            key_dir = getKey(process_name, lepton_selection_and_frWeight, leptonChargeSelection)
            for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_ROOT, DKEY_RLES, DKEY_SYNC ]:
              initDict(self.dirs, [ key_dir, dir_type ])
              if dir_type in [ DKEY_CFGS, DKEY_LOGS ]:
                self.dirs[key_dir][dir_type] = os.path.join(self.configDir, dir_type, self.channel,
                  "_".join([ lepton_selection_and_frWeight, leptonChargeSelection ]), process_name)
              else:
                self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel,
                  "_".join([ lepton_selection_and_frWeight, leptonChargeSelection ]), process_name)
    for dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_HIST, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT, DKEY_SYNC ]:
      initDict(self.dirs, [ dir_type ])
      if dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT ]:
        self.dirs[dir_type] = os.path.join(self.configDir, dir_type, self.channel)
      else:
        self.dirs[dir_type] = os.path.join(self.outputDir, dir_type, self.channel)
    ##print "self.dirs = ", self.dirs

    for key in self.dirs.keys():
      if type(self.dirs[key]) == dict:
        for dir_type in self.dirs[key].keys():
          create_if_not_exists(self.dirs[key][dir_type])
      else:
        create_if_not_exists(self.dirs[key])

    inputFileLists = {}
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"] or sample_info["sample_category"] in [ "additional_signal_overlap", "background_data_estimate" ]:
        continue
      logging.info("Checking input files for sample %s" % sample_info["process_name_specific"])
      inputFileLists[sample_name] = generateInputFileList(sample_info, self.max_files_per_job)

    mcClosure_regex = re.compile('Fakeable_mcClosure_(?P<type>m|e)_wFakeRateWeights')
    for lepton_selection in self.lepton_selections:
      electron_selection = lepton_selection
      muon_selection = lepton_selection

      hadTauVeto_selection = "Tight"
      hadTauVeto_selection = "|".join([ hadTauVeto_selection, self.hadTauVeto_selection_part2 ])

      if lepton_selection == "forBDTtraining":
        electron_selection = "Loose"
        muon_selection = "Loose"
      elif lepton_selection == "Fakeable_mcClosure_e":
        electron_selection = "Fakeable"
        muon_selection = "Tight"
      elif lepton_selection == "Fakeable_mcClosure_m":
        electron_selection = "Tight"
        muon_selection = "Fakeable"

      for lepton_frWeight in self.lepton_frWeights:
        if lepton_frWeight == "enabled" and not lepton_selection.startswith("Fakeable"):
          continue
        if lepton_frWeight == "disabled" and not lepton_selection in [ "Tight", "forBDTtraining" ]:
          continue
        lepton_selection_and_frWeight = get_lepton_selection_and_frWeight(lepton_selection, lepton_frWeight)

        for leptonChargeSelection in self.leptonChargeSelections:

          if 'mcClosure' in lepton_selection and leptonChargeSelection != 'SS':
            continue

          for sample_name, sample_info in self.samples.items():
            if not sample_info["use_it"] or sample_info["sample_category"] in [ "additional_signal_overlap", "background_data_estimate" ]:
              continue
            process_name = sample_info["process_name_specific"]
            logging.info("Creating configuration files to run '%s' for sample %s" % (self.executable_analyze, process_name))

            sample_category = sample_info["sample_category"]
            is_mc = (sample_info["type"] == "mc")
            is_signal = (sample_category == "signal")

            for central_or_shift in self.central_or_shifts:

              inputFileList = inputFileLists[sample_name]
              for jobId in inputFileList.keys():
                if central_or_shift != "central":
                  isFR_shape_shift = (central_or_shift in systematics.FR_all)
                  if not ((lepton_selection == "Fakeable" and leptonChargeSelection == "SS" and isFR_shape_shift) or
                          (lepton_selection == "Tight"    and leptonChargeSelection == "SS")):
                    continue
                  if not is_mc and not isFR_shape_shift:
                    continue

                if central_or_shift in systematics.LHE().ttH and sample_category != "signal":
                  continue
                if central_or_shift in systematics.LHE().ttW and sample_category != "TTW":
                  continue
                if central_or_shift in systematics.LHE().ttZ and sample_category != "TTZ":
                  continue

                logging.info(" ... for '%s' and systematic uncertainty option '%s'" % (lepton_selection_and_frWeight, central_or_shift))

                # build config files for executing analysis code
                key_dir = getKey(process_name, lepton_selection_and_frWeight, leptonChargeSelection)
                key_analyze_job = getKey(process_name, lepton_selection_and_frWeight, leptonChargeSelection, central_or_shift, jobId)
                ntupleFiles = inputFileList[jobId]
                if len(ntupleFiles) == 0:
                  logging.warning("No input ntuples for %s --> skipping job !!" % (key_analyze_job))
                  continue
                rootOutputFile = ""
                if self.select_root_output:
                  rootOutputFile = os.path.join(self.dirs[key_dir][DKEY_ROOT], "out_%s_%s_%s_%s_%s_%i.root" % \
                    (self.channel, process_name, lepton_selection_and_frWeight, leptonChargeSelection, central_or_shift, jobId))
                  key_file_woJobId = getKey(process_name, lepton_selection_and_frWeight, leptonChargeSelection, central_or_shift)
                  if key_file_woJobId not in self.rootOutputAux:
                    self.rootOutputAux[key_file_woJobId] = [ re.sub('_\d+\.root', '.root', rootOutputFile),
                                                             re.sub('\d+\.root', '*.root', rootOutputFile) ]

                #syncOutput = ''
                #syncTree = ''
                #syncRequireGenMatching = False
                #if self.do_sync:
                  #if leptonChargeSelection != 'SS':
                    #continue
                  #mcClosure_match = mcClosure_regex.match(lepton_selection_and_frWeight)
                  #if lepton_selection_and_frWeight == 'Tight':
                    #syncOutput = os.path.join(self.dirs[key_dir][DKEY_SYNC], '%s_%s_SR.root' % (self.channel, central_or_shift))
                    #syncTree   = 'syncTree_%s_SR' % self.channel.replace('_', '')
                    #syncRequireGenMatching = True and is_mc
                  #elif lepton_selection_and_frWeight == 'Fakeable_wFakeRateWeights':
                    #syncOutput = os.path.join(self.dirs[key_dir][DKEY_SYNC], '%s_%s_Fake.root' % (self.channel, central_or_shift))
                    #syncTree   = 'syncTree_%s_Fake' % self.channel.replace('_', '')
                  #elif mcClosure_match:
                    #mcClosure_type = mcClosure_match.group('type')
                    #syncOutput = os.path.join(self.dirs[key_dir][DKEY_SYNC], '%s_%s_mcClosure_%s.root' % (self.channel, central_or_shift, mcClosure_type))
                    #syncTree = 'syncTree_%s_mcClosure_%s' % (self.channel.replace('_', ''), mcClosure_type)
                  #else:
                    #continue

                #if syncTree and central_or_shift != "central":
                  #syncTree = os.path.join(central_or_shift, syncTree)

                #syncRLE = ''
                #if self.do_sync and self.rle_select:
                  #syncRLE = self.rle_select % syncTree
                  #if not os.path.isfile(syncRLE):
                    #logging.warning("Input RLE file for the sync is missing: %s; skipping the job" % syncRLE)
                    #continue

                #if syncOutput:
                  #self.inputFiles_sync['sync'].append(syncOutput)

                cfg_key = getKey(self.channel, process_name, lepton_selection_and_frWeight, leptonChargeSelection, central_or_shift, jobId)
                cfgFile_modified_path = os.path.join(self.dirs[key_dir][DKEY_CFGS], "analyze_%s_cfg.py" % cfg_key)
                logFile_path = os.path.join(self.dirs[key_dir][DKEY_LOGS], "analyze_%s.log" % cfg_key)
                rleOutputFile_path = os.path.join(self.dirs[key_dir][DKEY_RLES], "rle_%s.txt" % cfg_key) \
                                     if self.select_rle_output else ""
                histogramFile_path = os.path.join(self.dirs[key_dir][DKEY_HIST], "%s.root" % key_analyze_job)

                self.jobOptions_analyze[key_analyze_job] = {
                  'ntupleFiles'              : ntupleFiles,
                  'cfgFile_modified'         : cfgFile_modified_path,
                  'histogramFile'            : histogramFile_path,
                  'logFile'                  : logFile_path,
                  'selEventsFileName_output' : rleOutputFile_path,
                  'selEventsTFileName'       : rootOutputFile,
                  'electronSelection'        : electron_selection,
                  'muonSelection'            : muon_selection,
                  'lep_mva_cut'              : self.lep_mva_cut,
                  'apply_leptonGenMatching'  : self.apply_leptonGenMatching,
                  'hadTauSelection'          : hadTauVeto_selection,
                  'leptonChargeSelection'    : leptonChargeSelection,
                  'applyFakeRateWeights'     : self.applyFakeRateWeights if not lepton_selection == "Tight" else "disabled",
                  'central_or_shift'         : central_or_shift,
                  #'selectBDT'                : self.isBDTtraining,
                  #'syncOutput'               : syncOutput,
                  #'syncTree'                 : syncTree,
                  #'syncRLE'                  : syncRLE,
                  #'syncRequireGenMatching'   : syncRequireGenMatching,
                  'apply_hlt_filter'         : self.hlt_filter,
                  'useNonNominal'            : self.use_nonnominal,
                  'fillGenEvtHistograms'     : True,
                }
                self.createCfg_analyze(self.jobOptions_analyze[key_analyze_job], sample_info, lepton_selection)

                # initialize input and output file names for hadd_stage1
                key_hadd_stage1 = getKey(process_name, lepton_selection_and_frWeight, leptonChargeSelection)
                if not key_hadd_stage1 in self.inputFiles_hadd_stage1:
                  self.inputFiles_hadd_stage1[key_hadd_stage1] = []
                self.inputFiles_hadd_stage1[key_hadd_stage1].append(self.jobOptions_analyze[key_analyze_job]['histogramFile'])
                self.outputFile_hadd_stage1[key_hadd_stage1] = os.path.join(self.dirs[DKEY_HIST], "histograms_harvested_stage1_%s_%s_%s_%s.root" % \
                  (self.channel, process_name, lepton_selection_and_frWeight, leptonChargeSelection))

            if self.isBDTtraining or self.do_sync:
              continue

            if is_mc:
              logging.info("Creating configuration files to run 'addBackgrounds' for sample %s" % process_name)

              sample_categories = [ sample_category ]
              for sample_category in sample_categories:
                # sum non-fake and fake contributions for each MC sample separately
                genMatch_categories = [ "nonfake", "conversions", "fake" ]

                for genMatch_category in genMatch_categories:
                  key_hadd_stage1 = getKey(process_name, lepton_selection_and_frWeight, leptonChargeSelection)
                  key_addBackgrounds_job = None
                  processes_input = None
                  process_output = None
                  cfgFile_modified = None
                  outputFile = None
                  if genMatch_category == "nonfake":
                    # sum non-fake contributions for each MC sample separately
                    # input processes: TT3l0g0j,...
                    # output processes: TT; ...
                    if sample_category.startswith("signal"):
                      lepton_genMatches = []
                      lepton_genMatches.extend(self.lepton_genMatches_nonfakes)
                      lepton_genMatches.extend(self.lepton_genMatches_conversions)
                      processes_input = [ "%s%s" % (sample_category, genMatch) for genMatch in lepton_genMatches ]
                    else:
                      processes_input = [ "%s%s" % (sample_category, genMatch) for genMatch in self.lepton_genMatches_nonfakes ]
                    process_output = sample_category
                    key_addBackgrounds_job = getKey(process_name, sample_category, lepton_selection_and_frWeight, leptonChargeSelection)
                    cfgFile_modified = os.path.join(self.dirs[DKEY_CFGS], "addBackgrounds_%s_%s_%s_%s_%s_cfg.py" % \
                      (self.channel, process_name, sample_category, lepton_selection_and_frWeight, leptonChargeSelection))
                    outputFile = os.path.join(self.dirs[DKEY_HIST], "addBackgrounds_%s_%s_%s_%s_%s.root" % \
                      (self.channel, process_name, sample_category, lepton_selection_and_frWeight, leptonChargeSelection))
                  elif genMatch_category == "conversions":
                    # sum fake contributions for each MC sample separately
                    # input processes: TT2l1g0j, TT1l2g0j, TT0l3g0j; ...
                    # output processes: TT_conversion; ...
                    processes_input = [ "%s%s" % (sample_category, genMatch) for genMatch in self.lepton_genMatches_conversions ]
                    process_output = "%s_conversion" % sample_category
                    key_addBackgrounds_job = getKey(process_name, "%s_conversion" % sample_category, lepton_selection_and_frWeight, leptonChargeSelection)
                    cfgFile_modified = os.path.join(self.dirs[DKEY_CFGS], "addBackgrounds_%s_conversions_%s_%s_%s_%s_cfg.py" % \
                      (self.channel, process_name, sample_category, lepton_selection_and_frWeight, leptonChargeSelection))
                    outputFile = os.path.join(self.dirs[DKEY_HIST], "addBackgrounds_%s_conversions_%s_%s_%s_%s.root" % \
                      (self.channel, process_name, sample_category, lepton_selection_and_frWeight, leptonChargeSelection))
                  elif genMatch_category == "fake":
                    # sum fake contributions for each MC sample separately
                    # input processes: TT2l0g1j, TT1l1g1j, TT1l0g2j, TT0l2g1j, TT0l1g2j, TT0l0g3j; ...
                    # output processes: TT_fake; ...
                    processes_input = [ "%s%s" % (sample_category, genMatch) for genMatch in self.lepton_genMatches_fakes ]
                    process_output = "%s_fake" % sample_category
                    key_addBackgrounds_job = getKey(process_name, "%s_fake" % sample_category, lepton_selection_and_frWeight, leptonChargeSelection)
                    cfgFile_modified = os.path.join(self.dirs[DKEY_CFGS], "addBackgrounds_%s_fakes_%s_%s_%s_%s_cfg.py" % \
                      (self.channel, process_name, sample_category, lepton_selection_and_frWeight, leptonChargeSelection))
                    outputFile = os.path.join(self.dirs[DKEY_HIST], "addBackgrounds_%s_fakes_%s_%s_%s_%s.root" % \
                      (self.channel, process_name, sample_category, lepton_selection_and_frWeight, leptonChargeSelection))
                  if processes_input:
                    logging.info(" ...for genMatch option = '%s'" % genMatch_category)
                    self.jobOptions_addBackgrounds[key_addBackgrounds_job] = {
                      'inputFile' : self.outputFile_hadd_stage1[key_hadd_stage1],
                      'cfgFile_modified' : cfgFile_modified,
                      'outputFile' : outputFile,
                      'logFile' : os.path.join(self.dirs[DKEY_LOGS], os.path.basename(cfgFile_modified).replace("_cfg.py", ".log")),
                      'categories' : [ getHistogramDir(lepton_selection, lepton_frWeight, leptonChargeSelection) ],
                      'processes_input' : processes_input,
                      'process_output' : process_output
                    }
                    self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds[key_addBackgrounds_job])

                    # initialize input and output file names for hadd_stage1_5
                    key_hadd_stage1_5 = getKey(lepton_selection_and_frWeight, leptonChargeSelection)
                    if not key_hadd_stage1_5 in self.inputFiles_hadd_stage1_5:
                      self.inputFiles_hadd_stage1_5[key_hadd_stage1_5] = []
                    self.inputFiles_hadd_stage1_5[key_hadd_stage1_5].append(self.jobOptions_addBackgrounds[key_addBackgrounds_job]['outputFile'])
                    self.outputFile_hadd_stage1_5[key_hadd_stage1_5] = os.path.join(self.dirs[DKEY_HIST], "histograms_harvested_stage1_5_%s_%s_%s.root" % \
                     (self.channel, lepton_selection_and_frWeight, leptonChargeSelection))

            #if self.isBDTtraining or self.do_sync:
              #continue

            # add output files of hadd_stage1 for data to list of input files for hadd_stage1_5
            if not is_mc:
              key_hadd_stage1 = getKey(process_name, lepton_selection_and_frWeight, leptonChargeSelection)
              key_hadd_stage1_5 = getKey(lepton_selection_and_frWeight, leptonChargeSelection)
              if not key_hadd_stage1_5 in self.inputFiles_hadd_stage1_5:
                self.inputFiles_hadd_stage1_5[key_hadd_stage1_5] = []
              self.inputFiles_hadd_stage1_5[key_hadd_stage1_5].append(self.outputFile_hadd_stage1[key_hadd_stage1])

          #if self.isBDTtraining or self.do_sync:
            #continue

          # sum fake background contributions for the total of all MC sample
          # input processes: TT2l0g1j, TT1l1g1j, TT1l0g2j, TT0l3j, TT0l3j, TT0l3j, TT0l3j; ...
          # output process: fakes_mc
          key_addBackgrounds_job_fakes = getKey(lepton_selection_and_frWeight, leptonChargeSelection, "fakes")
          key_hadd_stage1_5 = getKey(lepton_selection_and_frWeight, leptonChargeSelection)
          sample_categories = []
          sample_categories.extend(self.nonfake_backgrounds)
          if "signal_nonresonant" in self.prep_dcard_signals:
            sample_categories.extend([ "signal_nonresonant" ])
          processes_input = []
          for sample_category in sample_categories:
            processes_input.append("%s_fake" % sample_category)
          self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes] = {
            'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5],
            'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "addBackgrounds_%s_fakes_mc_%s_%s_cfg.py" % \
              (self.channel, lepton_selection_and_frWeight, leptonChargeSelection)),
            'outputFile' : os.path.join(self.dirs[DKEY_HIST], "addBackgrounds_%s_fakes_mc_%s_%s.root" % \
              (self.channel, lepton_selection_and_frWeight, leptonChargeSelection)),
            'logFile' : os.path.join(self.dirs[DKEY_LOGS], "addBackgrounds_%s_fakes_mc_%s_%s.log" % \
              (self.channel, lepton_selection_and_frWeight, leptonChargeSelection)),
            'categories' : [ getHistogramDir(lepton_selection, lepton_frWeight, leptonChargeSelection) ],
            'processes_input' : processes_input,
            'process_output' : "fakes_mc"
          }
          self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes])

          # sum conversion background contributions for the total of all MC sample
          # input processes: TT2l0g1j, TT1l1g1j, TT1l0g2j, TT0l3j, TT0l3j, TT0l3j, TT0l3j; ...
          # output process: conversions
          key_addBackgrounds_job_conversions = getKey(lepton_selection_and_frWeight, leptonChargeSelection, "conversions")
          sample_categories = []
          sample_categories.extend(self.nonfake_backgrounds)
          if "signal_nonresonant" in self.prep_dcard_signals:
            sample_categories.extend([ "signal_nonresonant" ])
          processes_input = []
          for sample_category in sample_categories:
            processes_input.append("%s_conversion" % sample_category)
          self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_conversions] = {
            'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5],
            'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "addBackgrounds_%s_conversions_%s_%s_cfg.py" % \
              (self.channel, lepton_selection_and_frWeight, leptonChargeSelection)),
            'outputFile' : os.path.join(self.dirs[DKEY_HIST], "addBackgrounds_%s_conversions_%s_%s.root" % \
              (self.channel, lepton_selection_and_frWeight, leptonChargeSelection)),
            'logFile' : os.path.join(self.dirs[DKEY_LOGS], "addBackgrounds_%s_conversions_%s_%s.log" % \
              (self.channel, lepton_selection_and_frWeight, leptonChargeSelection)),
            'categories' : [ getHistogramDir(lepton_selection, lepton_frWeight, leptonChargeSelection) ],
            'processes_input' : processes_input,
            'process_output' : "conversions"
          }
          self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_conversions])

          # sum signal contributions from HH->4tau ("tttt"), HH->2W2tau ("wwtt"), and HH->4W ("wwww"),
          # separately for "nonfake" and "fake" contributions
          genMatch_categories = [ "nonfake", "fake" ]
          for genMatch_category in genMatch_categories:
            for sample_name, sample_info in self.samples.items():
              if not sample_info["use_it"] or sample_info["sample_category"] in [ "additional_signal_overlap", "background_data_estimate" ]:
                continue
              sample_category = sample_info["sample_category"]
              sample_category_base = sample_category[0:sample_category.rfind("_")]
              is_signal = sample_category_base.startswith("signal")
              if not is_signal:
                continue
              key_addBackgrounds_job_signal = getKey(lepton_selection_and_frWeight, leptonChargeSelection, sample_category_base)
              key_hadd_stage1_5 = getKey(lepton_selection_and_frWeight, leptonChargeSelection)
              processes_input = []
              for decay_mode in [ "tttt", "wwtt", "wwww" ]:
                processes_input.append(sample_category_base + "_" + decay_mode)
              process_output = sample_category_base
              if genMatch_category == "fake":
                key_addBackgrounds_job_signal = key_addBackgrounds_job_signal + "_fake"
                processes_input = [ process_input + "_fake" for process_input in processes_input ]
                process_output = process_output + "_fake"
              if key_addBackgrounds_job_signal in self.jobOptions_addBackgrounds_sum.keys():
                continue
              cfg_key = getKey(self.channel, sample_category_base, genMatch_category, lepton_selection_and_frWeight, leptonChargeSelection)
              self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_signal] = {
                'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5],
                'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "addBackgrounds_%s_cfg.py" % cfg_key),
                'outputFile' : os.path.join(self.dirs[DKEY_HIST], "addBackgrounds_%s.root" % cfg_key),
                'logFile' : os.path.join(self.dirs[DKEY_LOGS], "addBackgrounds_%s.log" % cfg_key),
                'categories' : [ getHistogramDir(lepton_selection, lepton_frWeight, leptonChargeSelection) ],
                'processes_input' : processes_input,
                'process_output' : process_output
              }
              self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_signal])
              key_hadd_stage2 = getKey(lepton_selection_and_frWeight, leptonChargeSelection)
              if not key_hadd_stage2 in self.inputFiles_hadd_stage2:
                self.inputFiles_hadd_stage2[key_hadd_stage2] = []
              if lepton_selection == "Tight":
                self.inputFiles_hadd_stage2[key_hadd_stage2].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_signal]['outputFile'])

          # initialize input and output file names for hadd_stage2
          key_hadd_stage2 = getKey(lepton_selection_and_frWeight, leptonChargeSelection)
          if not key_hadd_stage2 in self.inputFiles_hadd_stage2:
            self.inputFiles_hadd_stage2[key_hadd_stage2] = []
          if lepton_selection == "Tight":
            self.inputFiles_hadd_stage2[key_hadd_stage2].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes]['outputFile'])
            self.inputFiles_hadd_stage2[key_hadd_stage2].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_conversions]['outputFile'])
          key_hadd_stage1_5 = getKey(lepton_selection_and_frWeight, leptonChargeSelection)
          self.inputFiles_hadd_stage2[key_hadd_stage2].append(self.outputFile_hadd_stage1_5[key_hadd_stage1_5])
          self.outputFile_hadd_stage2[key_hadd_stage2] = os.path.join(self.dirs[DKEY_HIST], "histograms_harvested_stage2_%s_%s_%s.root" % \
            (self.channel, lepton_selection_and_frWeight, leptonChargeSelection))

    #if self.isBDTtraining or self.do_sync:
      #if self.is_sbatch:
        #logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
        #self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
        #if self.isBDTtraining:
          #self.createScript_sbatch_analyze(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
        #elif self.do_sync:
          #self.createScript_sbatch_syncNtuple(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
      #logging.info("Creating Makefile")
      #lines_makefile = []
      #if self.isBDTtraining:
        #self.addToMakefile_analyze(lines_makefile)
        #self.addToMakefile_hadd_stage1(lines_makefile)
      #elif self.do_sync:
        #self.addToMakefile_syncNtuple(lines_makefile)
        #outputFile_sync_path = os.path.join(self.outputDir, DKEY_SYNC, '%s.root' % self.channel)
        #self.outputFile_sync['sync'] = outputFile_sync_path
        #self.targets.append(outputFile_sync_path)
        #self.addToMakefile_hadd_sync(lines_makefile)
      #else:
        #raise ValueError("Internal logic error")
      #self.createMakefile(lines_makefile)
      #logging.info("Done")
      #return self.num_jobs

    logging.info("Creating configuration files to run 'addBackgroundFakes'")
    for leptonChargeSelection in self.leptonChargeSelections:
      key_addFakes_job = getKey("fakes_data", leptonChargeSelection)
      key_hadd_stage1_5 = getKey(get_lepton_selection_and_frWeight("Fakeable", "enabled"), leptonChargeSelection)
      category_sideband = "hh_2lss_%s_Fakeable_wFakeRateWeights" % leptonChargeSelection
      self.jobOptions_addFakes[key_addFakes_job] = {
        'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5],
        'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "addBackgroundLeptonFakes_%s_%s_cfg.py" % \
          (self.channel, leptonChargeSelection)),
        'outputFile' : os.path.join(self.dirs[DKEY_HIST], "addBackgroundLeptonFakes_%s_%s.root" % \
          (self.channel, leptonChargeSelection)),
        'logFile' : os.path.join(self.dirs[DKEY_LOGS], "addBackgroundLeptonFakes_%s_%s.log" % \
          (self.channel, leptonChargeSelection)),
        'category_signal' : "hh_2lss_%s_Tight" % leptonChargeSelection,
        'category_sideband' : category_sideband
      }
      self.createCfg_addFakes(self.jobOptions_addFakes[key_addFakes_job])
      key_hadd_stage2 = getKey(get_lepton_selection_and_frWeight("Tight", "disabled"), leptonChargeSelection)
      self.inputFiles_hadd_stage2[key_hadd_stage2].append(self.jobOptions_addFakes[key_addFakes_job]['outputFile'])

    #--------------------------------------------------------------------------
    # add histograms in OS and SS regions,
    # so that "fakes_data" background can be subtracted from OS control region used to estimate charge flip background
    key_addFakes_job = getKey("fakes_data", "OS")
    self.inputFiles_hadd_stage1_6.append(self.jobOptions_addFakes[key_addFakes_job]['outputFile'])
    key_hadd_stage1_5 = getKey(get_lepton_selection_and_frWeight("Tight", "disabled"), "OS")
    self.inputFiles_hadd_stage1_6.append(self.outputFile_hadd_stage1_5[key_hadd_stage1_5])
    self.outputFile_hadd_stage1_6 = os.path.join(self.dirs[DKEY_HIST], "histograms_harvested_stage1_6_%s_Tight_SS.root" % self.channel)
    #--------------------------------------------------------------------------

    logging.info("Creating configuration files to run 'addBackgroundFlips'")
    key_addFlips_job = getKey("flips_data")
    self.inputFiles_hadd_stage1_6.append(self.jobOptions_addFakes[key_addFakes_job]['outputFile'])
    self.jobOptions_addFlips[key_addFlips_job] = {
      'inputFile' : self.outputFile_hadd_stage1_6,
      'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "addBackgroundLeptonFlips_%s_cfg.py" % self.channel),
      'outputFile' : os.path.join(self.dirs[DKEY_HIST], "addBackgroundLeptonFlips_%s.root" % self.channel),
      'logFile' : os.path.join(self.dirs[DKEY_LOGS], "addBackgroundLeptonFlips_%s.log" % self.channel),
      'category_signal' : "hh_2lss_SS_Tight",
      'category_sideband' : "hh_2lss_OS_Tight"
    }
    self.createCfg_addFlips(self.jobOptions_addFlips[key_addFlips_job])
    key_hadd_stage2 = getKey(get_lepton_selection_and_frWeight("Tight", "disabled"), "SS")
    self.inputFiles_hadd_stage2[key_hadd_stage2].append(self.jobOptions_addFlips[key_addFlips_job]['outputFile'])

    logging.info("Creating configuration files to run 'prepareDatacards'")
    for histogramToFit in self.histograms_to_fit:
      key_prep_dcard_job = getKey(histogramToFit, "SS")
      key_hadd_stage2 = getKey(get_lepton_selection_and_frWeight("Tight", "disabled"), "SS")
      self.jobOptions_prep_dcard[key_prep_dcard_job] = {
        'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2],
        'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "prepareDatacards_%s_%s_cfg.py" % (self.channel, histogramToFit)),
        'datacardFile' : os.path.join(self.dirs[DKEY_DCRD], "prepareDatacards_%s_%s.root" % (self.channel, histogramToFit)),
        'histogramDir' : self.histogramDir_prep_dcard,
        'histogramToFit' : histogramToFit,
        'label' : "2lOS+4j"
      }
      self.createCfg_prep_dcard(self.jobOptions_prep_dcard[key_prep_dcard_job])

      if "OS" in self.leptonChargeSelections:
        key_prep_dcard_job = getKey(histogramToFit, "OS")
        key_hadd_stage2 = getKey(get_lepton_selection_and_frWeight("Tight", "disabled"), "OS")
        self.jobOptions_prep_dcard[key_prep_dcard_job] = {
          'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2],
          'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "prepareDatacards_%s_OS_%s_cfg.py" % (self.channel, histogramToFit)),
          'datacardFile' : os.path.join(self.dirs[DKEY_DCRD], "prepareDatacards_%s_OS_%s.root" % (self.channel, histogramToFit)),
          'histogramDir' : self.histogramDir_prep_dcard_OS,
          'histogramToFit' : histogramToFit,
          'label' : "2lSS+4j",
        }
        self.createCfg_prep_dcard(self.jobOptions_prep_dcard[key_prep_dcard_job])

      # add shape templates for the following systematic uncertainties:
      #  - 'CMS_ttHl_Clos_norm_e'
      #  - 'CMS_ttHl_Clos_shape_e'
      #  - 'CMS_ttHl_Clos_norm_m'
      #  - 'CMS_ttHl_Clos_shape_m'
      for leptonChargeSelection in self.leptonChargeSelections:
        key_prep_dcard_job = getKey(histogramToFit, leptonChargeSelection)
        key_add_syst_fakerate_job = getKey(histogramToFit, leptonChargeSelection)
        key_hadd_stage2 = getKey(get_lepton_selection_and_frWeight("Tight", "disabled"), leptonChargeSelection)
        self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job] = {
          'inputFile' : self.jobOptions_prep_dcard[key_prep_dcard_job]['datacardFile'],
          'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "addSystFakeRates_%s_%s_%s_cfg.py" % (self.channel, leptonChargeSelection, histogramToFit)),
          'outputFile' : os.path.join(self.dirs[DKEY_DCRD], "addSystFakeRates_%s_%s_%s.root" % (self.channel, leptonChargeSelection, histogramToFit)),
          'category' : self.channel,
          'histogramToFit' : histogramToFit,
          'plots_outputFileName' : os.path.join(self.dirs[DKEY_PLOT], "addSystFakeRates.png")
        }
        histogramDir_nominal = None
        if leptonChargeSelection == "SS":
          histogramDir_nominal = self.histogramDir_prep_dcard
        elif leptonChargeSelection == "OS":
          histogramDir_nominal = self.histogramDir_prep_dcard_OS
        else:
          raise ValueError("Invalid parameter 'leptonChargeSelection' = %s !!" % leptonChargeSelection)
        for lepton_type in [ 'e', 'm' ]:
          lepton_mcClosure = "Fakeable_mcClosure_%s" % lepton_type
          if lepton_mcClosure not in self.lepton_selections:
            continue
          lepton_selection_and_frWeight = get_lepton_selection_and_frWeight(lepton_mcClosure, "enabled")
          key_addBackgrounds_job_fakes = getKey(lepton_selection_and_frWeight, leptonChargeSelection, "fakes")
          histogramDir_mcClosure = self.mcClosure_dir['%s_%s' % (lepton_mcClosure, leptonChargeSelection)]
          self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job].update({
            'add_Clos_%s' % lepton_type : ("Fakeable_mcClosure_%s" % lepton_type) in self.lepton_selections,
            'inputFile_nominal_%s' % lepton_type : self.outputFile_hadd_stage2[key_hadd_stage2],
            'histogramName_nominal_%s' % lepton_type : "%s/sel/evt/fakes_mc/%s" % (histogramDir_nominal, histogramToFit),
            'inputFile_mcClosure_%s' % lepton_type : self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes]['outputFile'],
            'histogramName_mcClosure_%s' % lepton_type : "%s/sel/evt/fakes_mc/%s" % (histogramDir_mcClosure, histogramToFit)
          })
        self.createCfg_add_syst_fakerate(self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job])

    logging.info("Creating configuration files to run 'makePlots'")

    key_makePlots_job = getKey("SS")
    key_hadd_stage2 = getKey(get_lepton_selection_and_frWeight("Tight", "disabled"), "SS")
    self.jobOptions_make_plots[key_makePlots_job] = {
      'executable' : self.executable_make_plots,
      'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2],
      'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "makePlots_%s_cfg.py" % self.channel),
      'outputFile' : os.path.join(self.dirs[DKEY_PLOT], "makePlots_%s.png" % self.channel),
      'histogramDir' : self.histogramDir_prep_dcard,
      'label' : "2lSS",
      'make_plots_backgrounds' : self.make_plots_backgrounds,
      'massPoint' : self.mass_point,
      'skipChannel' : True,
    }
    self.createCfg_makePlots(self.jobOptions_make_plots[key_makePlots_job])
    if "OS" in self.leptonChargeSelections:
      key_makePlots_job = getKey("OS")
      key_hadd_stage2 = getKey(get_lepton_selection_and_frWeight("Tight", "disabled"), "OS")
      self.jobOptions_make_plots[key_makePlots_job] = {
        'executable' : self.executable_make_plots,
        'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2],
        'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "makePlots_%s_OS_cfg.py" % self.channel),
        'outputFile' : os.path.join(self.dirs[DKEY_PLOT], "makePlots_%s_OS.png" % self.channel),
        'histogramDir' : self.histogramDir_prep_dcard_OS,
        'label' : "2lOS",
        'make_plots_backgrounds' : self.make_plots_backgrounds,
        'massPoint'  : self.mass_point,
        'skipChannel': True,
      }
      self.createCfg_makePlots(self.jobOptions_make_plots[key_makePlots_job])
    if "Fakeable_mcClosure" in self.lepton_selections: #TODO
      key_makePlots_job = getKey("SS")
      key_hadd_stage2 = getKey(get_lepton_selection_and_frWeight("Tight", "disabled"), "SS")
      self.jobOptions_make_plots[key_makePlots_job] = {
        'executable' : self.executable_make_plots_mcClosure,
        'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2],
        'cfgFile_modified' : os.path.join(self.dirs[DKEY_CFGS], "makePlots_mcClosure_%s_cfg.py" % self.channel),
        'outputFile' : os.path.join(self.dirs[DKEY_PLOT], "makePlots_mcClosure_%s.png" % self.channel),
      }
      self.createCfg_makePlots_mcClosure(self.jobOptions_make_plots[key_makePlots_job])

    if self.is_sbatch:
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
      self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
      self.createScript_sbatch_analyze(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_addBackgrounds)
      self.sbatchFile_addBackgrounds = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addBackgrounds_%s.py" % self.channel)
      self.createScript_sbatch(self.executable_addBackgrounds, self.sbatchFile_addBackgrounds, self.jobOptions_addBackgrounds)
      self.sbatchFile_addBackgrounds_sum = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addBackgrounds_sum_%s.py" % self.channel)
      self.createScript_sbatch(self.executable_addBackgrounds, self.sbatchFile_addBackgrounds_sum, self.jobOptions_addBackgrounds_sum)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_addFakes)
      self.sbatchFile_addFakes = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addFakes_%s.py" % self.channel)
      self.createScript_sbatch(self.executable_addFakes, self.sbatchFile_addFakes, self.jobOptions_addFakes)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_addFlips)
      self.sbatchFile_addFlips = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addFlips_%s.py" % self.channel)
      self.createScript_sbatch(self.executable_addFlips, self.sbatchFile_addFlips, self.jobOptions_addFlips)

    logging.info("Creating Makefile")
    lines_makefile = []
    self.addToMakefile_analyze(lines_makefile)
    self.addToMakefile_hadd_stage1(lines_makefile)
    self.addToMakefile_backgrounds_from_data(lines_makefile)
    self.addToMakefile_hadd_stage2(lines_makefile)
    self.addToMakefile_prep_dcard(lines_makefile)
    self.addToMakefile_add_syst_fakerate(lines_makefile)
    self.addToMakefile_make_plots(lines_makefile)
    self.createMakefile(lines_makefile)

    logging.info("Done")

    return self.num_jobs
