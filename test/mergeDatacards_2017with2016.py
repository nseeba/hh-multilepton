#!/usr/bin/env python

import os

channels = {
##     'hh_0l_4tau' : {
##         'directory_histograms_2016'     : "/hdfs/local/veelken/hhAnalysis/2017/2018Jul12/histograms/hh_0l_4tau/",
##         'filename_hadd_stage2_2016'     : "histograms_harvested_stage1_5_hh_0l_4tau_Tight_OS.root",
##         'directory_histograms_2017'     : "/hdfs/local/veelken/hhAnalysis/2017/2018Jul12/histograms/hh_0l_4tau/",
##         'filename_hadd_stage2_2017'     : "histograms_harvested_stage2_hh_0l_4tau_Tight_OS.root",
##         'directory_datacards'           : "/home/veelken/hhAnalysis/2017/2018Jul12/datacards/hh_0l_4tau/",
##         'histograms_to_fit'             : [ "EventCounter", "numJets", "dihiggsVisMass", "dihiggsMass", "HT", "STMET" ],
##         'directory_cfgs_2017'           : "/home/veelken/hhAnalysis/2017/2018Jul12/cfgs/hh_0l_4tau/",
##         'filename_prepareDatacards_cfg' : "prepareDatacards_cfg.py"
##     },
##     'hh_1l_3tau' : {
##         'directory_histograms_2016'     : "/hdfs/local/veelken/hhAnalysis/2017/2018Jul12/histograms/hh_1l_3tau/",
##         'filename_hadd_stage2_2016'     : "histograms_harvested_stage1_5_hh_1l_3tau_Tight_OS.root",
##         'directory_histograms_2017'     : "/hdfs/local/veelken/hhAnalysis/2017/2018Jul12/histograms/hh_1l_3tau/",
##         'filename_hadd_stage2_2017'     : "histograms_harvested_stage2_hh_1l_3tau_Tight_OS.root",
##         'directory_datacards'           : "/home/veelken/hhAnalysis/2017/2018Jul12/datacards/hh_1l_3tau/",
##         'histograms_to_fit'             : [ "EventCounter", "numJets", "dihiggsVisMass", "dihiggsMass", "HT", "STMET" ],
##         'directory_cfgs_2017'           : "/home/veelken/hhAnalysis/2017/2018Jul12/cfgs/hh_1l_3tau/",
##         'filename_prepareDatacards_cfg' : "prepareDatacards_cfg.py"
##     },
    'hh_2l_2tau' : {
        'directory_histograms_2016'     : "/hdfs/local/veelken/hhAnalysis/2016/2018Aug04v2/histograms/hh_2l_2tau/",
        'filename_hadd_stage2_2016'     : "histograms_harvested_stage1_5_hh_2l_2tau_disabled_disabled_Tight_OS.root",
        'directory_histograms_2017'     : "/hdfs/local/veelken/hhAnalysis/2017/2018Aug01v1/histograms/hh_2l_2tau/",
        'filename_hadd_stage2_2017'     : "histograms_harvested_stage2_hh_2l_2tau_disabled_disabled_Tight_OS.root",
        'directory_datacards'           : "/home/veelken/hhAnalysis/2017/2018Aug01v1/datacards/hh_2l_2tau/",
        'histograms_to_fit'             : [ "EventCounter", "numJets", "mTauTauVis", "dihiggsVisMass", "dihiggsMass", "HT", "STMET" ],
        'directory_cfgs_2017'           : "/home/veelken/hhAnalysis/2017/2018Aug01v1/cfgs/hh_2l_2tau/",
        'filename_prepareDatacards_cfg' : "prepareDatacards_cfg.py"
    },
##     'hh_3l_1tau' : {
##         'directory_histograms_2016'     : "/hdfs/local/veelken/hhAnalysis/2017/2018Jul12/histograms/hh_3l_1tau/",
##         'filename_hadd_stage2_2016'     : "histograms_harvested_stage1_5_hh_3l_1tau_Tight_OS.root",
##         'directory_histograms_2017'     : "/hdfs/local/veelken/hhAnalysis/2017/2018Jul12/histograms/hh_3l_1tau/",
##         'filename_hadd_stage2_2017'     : "histograms_harvested_stage2_hh_3l_1tau_Tight_OS.root",
##         'directory_datacards'           : "/home/veelken/hhAnalysis/2017/2018Jul12/datacards/hh_3l_1tau/",
##         'histograms_to_fit'             : [ "EventCounter", "numJets", "dihiggsVisMass", "dihiggsMass", "HT", "STMET" ],
##         'directory_cfgs_2017'           : "/home/veelken/hhAnalysis/2017/2018Jul12/cfgs/hh_3l_1tau/",
##         'filename_prepareDatacards_cfg' : "prepareDatacards_cfg.py"
##     },
##     'hh_4l' : {
##         'directory_histograms_2016'     : "/hdfs/local/veelken/hhAnalysis/2017/2018Jul12/histograms/hh_4l/",
##         'filename_hadd_stage2_2016'     : "",
##         'directory_histograms_2017'     : "/hdfs/local/veelken/hhAnalysis/2017/2018Jul12/histograms/hh_4l/",
##         'filename_hadd_stage2_2017'     : "",
##         'directory_datacards'           : "/home/veelken/hhAnalysis/2017/2018Jul12/datacards/hh_4l/",
##         'histograms_to_fit'             : [ "EventCounter", "numJets", "dihiggsVisMass", "dihiggsMass", "HT", "STMET" ],
##         'directory_cfgs_2017'           : "/home/veelken/hhAnalysis/2017/2018Jul12/cfgs/hh_4l/",
##         'filename_prepareDatacards_cfg' : "prepareDatacards_cfg.py"
##     },
}

filename_shell_script = "mergeDatacards_2017with2016.sh"

executable_cp = 'cp'
executable_rm = 'rm'
executable_hadd = 'hadd'
executable_prepareDatacards = 'prepareDatacards'

lines_shell_script = []

filenames_hadd_output = {}
for channel_name in channels:
    filename_hadd_input1 = os.path.join(channels[channel_name]['directory_histograms_2016'],
      channels[channel_name]['filename_hadd_stage2_2016'])
    filename_hadd_input2 = os.path.join(channels[channel_name]['directory_histograms_2017'],
      channels[channel_name]['filename_hadd_stage2_2017'])
    filename_hadd_output = os.path.join(channels[channel_name]['directory_histograms_2017'],
      channels[channel_name]['filename_hadd_stage2_2017'].replace(".root", "_with2016.root"))
    command_rm = '%s -f %s' % (executable_rm, os.path.basename(filename_hadd_output))
    lines_shell_script.append(command_rm)
    command_hadd = '%s %s %s %s' % (executable_hadd, os.path.basename(filename_hadd_output), filename_hadd_input1, filename_hadd_input2)
    lines_shell_script.append(command_hadd)
    command_cp = '%s %s %s' % (executable_cp, os.path.basename(filename_hadd_output), filename_hadd_output)
    lines_shell_script.append(command_cp)
    command_rm = '%s %s' % (executable_rm, os.path.basename(filename_hadd_output))
    lines_shell_script.append(command_rm)
    filenames_hadd_output[channel_name] = filename_hadd_output

# CV: skip 'hadd' step
lines_shell_script = []

from hhAnalysis.multilepton.samples.hhAnalyzeSamples_2016 import samples_2016 as samples
from collections import OrderedDict as OD
signals = []
for sample_name, sample_info in samples.items():
    if not type(sample_info) is OD:
        continue
    if sample_info['sample_category'].find("signal") != -1:
        #signals.append(sample_info['process_name_specific'])
        signals.append(sample_info['sample_category'])
print "signals = %s" % signals

from tthAnalysis.HiggsToTauTau.analysisTools import create_cfg
for channel_name in channels:
    for histogram_to_fit in channels[channel_name]['histograms_to_fit']:
        filename_prepareDatacards_cfg_original = os.path.join(channels[channel_name]['directory_cfgs_2017'],
          channels[channel_name]['filename_prepareDatacards_cfg'].replace("_cfg.py", "_%s_%s_cfg.py" % (channel_name, histogram_to_fit)))
        filename_prepareDatacards_cfg_modified = filename_prepareDatacards_cfg_original.replace("_cfg.py", "_with2016_cfg.py")
        lines_prepareDatacards = []
        lines_prepareDatacards.append("process.prepareDatacards.signals = cms.vstring(")
        for signal in signals:
            lines_prepareDatacards.append("    '%s'," % signal)
        lines_prepareDatacards.append(")")
        filename_prepareDatacards_output = os.path.join(channels[channel_name]['directory_datacards'],
          "prepareDatacards_%s_%s_with2016.root" % (channel_name, histogram_to_fit))
        lines_prepareDatacards.append("process.fwliteInput.fileNames = cms.vstring('%s')" % filenames_hadd_output[channel_name])
        lines_prepareDatacards.append("process.fwliteOutput.fileName = cms.string('%s')" % filename_prepareDatacards_output)
        create_cfg(filename_prepareDatacards_cfg_original, filename_prepareDatacards_cfg_modified, lines_prepareDatacards)
        command_prepareDatacards = '%s %s' % (executable_prepareDatacards, filename_prepareDatacards_cfg_modified)
        lines_shell_script.append(command_prepareDatacards)

from tthAnalysis.HiggsToTauTau.analysisTools import createFile
createFile(filename_shell_script, lines_shell_script)

print "Finished creating config files."
print "Now execute: 'source %s'" % filename_shell_script
