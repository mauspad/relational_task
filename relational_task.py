#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on January 30, 2021, at 23:54
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Relational Task'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\mauspad\\Desktop\\OEA_task_test\\relational_task\\relational_task.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
key_resp = keyboard.Keyboard()
incorrect = visual.ImageStim(
    win=win,
    name='incorrect', 
    image='images/practice-incorrect.jpg', mask=None,
    ori=0, pos=(0, -350), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "shape_title"
shape_titleClock = core.Clock()
shape_name = visual.ImageStim(
    win=win,
    name='shape_name', 
    image='images/matchshape.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "block1"
block1Clock = core.Clock()
block1_match = visual.ImageStim(
    win=win,
    name='block1_match', 
    image='sin', mask=None,
    ori=0, pos=(0, 150), size=(450,450),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
block1_response = keyboard.Keyboard()
block1_buttons = visual.ImageStim(
    win=win,
    name='block1_buttons', 
    image='images/buttons.png', mask=None,
    ori=0, pos=(0, -200), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ITI_match"
ITI_matchClock = core.Clock()
match_ITI = visual.TextStim(win=win, name='match_ITI',
    text='Blank',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "change_title"
change_titleClock = core.Clock()
change_name = visual.ImageStim(
    win=win,
    name='change_name', 
    image='images/matchchange.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "block2"
block2Clock = core.Clock()
block2_change = visual.ImageStim(
    win=win,
    name='block2_change', 
    image='sin', mask=None,
    ori=0, pos=(0, 150), size=(450,450),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
block2_response = keyboard.Keyboard()
block2_buttons = visual.ImageStim(
    win=win,
    name='block2_buttons', 
    image='images/buttons.png', mask=None,
    ori=0, pos=(0, -200), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ITI_change"
ITI_changeClock = core.Clock()
change_ITI = visual.TextStim(win=win, name='change_ITI',
    text='Blank',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "shape_title"
shape_titleClock = core.Clock()
shape_name = visual.ImageStim(
    win=win,
    name='shape_name', 
    image='images/matchshape.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "block3"
block3Clock = core.Clock()
block3_match = visual.ImageStim(
    win=win,
    name='block3_match', 
    image='sin', mask=None,
    ori=0, pos=(0, 150), size=(450,450),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
block3_response = keyboard.Keyboard()
block3_buttons = visual.ImageStim(
    win=win,
    name='block3_buttons', 
    image='images/buttons.png', mask=None,
    ori=0, pos=(0, -200), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ITI_match"
ITI_matchClock = core.Clock()
match_ITI = visual.TextStim(win=win, name='match_ITI',
    text='Blank',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "change_title"
change_titleClock = core.Clock()
change_name = visual.ImageStim(
    win=win,
    name='change_name', 
    image='images/matchchange.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "block4"
block4Clock = core.Clock()
block4_change = visual.ImageStim(
    win=win,
    name='block4_change', 
    image='sin', mask=None,
    ori=0, pos=(0, 150), size=(450,450),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
block4_response = keyboard.Keyboard()
block4_buttons = visual.ImageStim(
    win=win,
    name='block4_buttons', 
    image='images/buttons.png', mask=None,
    ori=0, pos=(0, -200), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ITI_change"
ITI_changeClock = core.Clock()
change_ITI = visual.TextStim(win=win, name='change_ITI',
    text='Blank',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "shape_title"
shape_titleClock = core.Clock()
shape_name = visual.ImageStim(
    win=win,
    name='shape_name', 
    image='images/matchshape.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "block5"
block5Clock = core.Clock()
block5_match = visual.ImageStim(
    win=win,
    name='block5_match', 
    image='sin', mask=None,
    ori=0, pos=(0, 150), size=(450,450),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
block5_response = keyboard.Keyboard()
block5_buttons = visual.ImageStim(
    win=win,
    name='block5_buttons', 
    image='images/buttons.png', mask=None,
    ori=0, pos=(0, -200), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ITI_match"
ITI_matchClock = core.Clock()
match_ITI = visual.TextStim(win=win, name='match_ITI',
    text='Blank',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "change_title"
change_titleClock = core.Clock()
change_name = visual.ImageStim(
    win=win,
    name='change_name', 
    image='images/matchchange.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "block6"
block6Clock = core.Clock()
block6_change = visual.ImageStim(
    win=win,
    name='block6_change', 
    image='sin', mask=None,
    ori=0, pos=(0, 150), size=(450,450),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
block6_response = keyboard.Keyboard()
block6_buttons = visual.ImageStim(
    win=win,
    name='block6_buttons', 
    image='images/buttons.png', mask=None,
    ori=0, pos=(0, -200), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ITI_change"
ITI_changeClock = core.Clock()
change_ITI = visual.TextStim(win=win, name='change_ITI',
    text='Blank',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "shape_title"
shape_titleClock = core.Clock()
shape_name = visual.ImageStim(
    win=win,
    name='shape_name', 
    image='images/matchshape.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "block7"
block7Clock = core.Clock()
block7_match = visual.ImageStim(
    win=win,
    name='block7_match', 
    image='sin', mask=None,
    ori=0, pos=(0, 150), size=(450,450),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
block7_response = keyboard.Keyboard()
block7_buttons = visual.ImageStim(
    win=win,
    name='block7_buttons', 
    image='images/buttons.png', mask=None,
    ori=0, pos=(0, -200), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ITI_match"
ITI_matchClock = core.Clock()
match_ITI = visual.TextStim(win=win, name='match_ITI',
    text='Blank',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "change_title"
change_titleClock = core.Clock()
change_name = visual.ImageStim(
    win=win,
    name='change_name', 
    image='images/matchchange.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "block8"
block8Clock = core.Clock()
block8_change = visual.ImageStim(
    win=win,
    name='block8_change', 
    image='sin', mask=None,
    ori=0, pos=(0, 150), size=(450,450),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
block8_response = keyboard.Keyboard()
block8_buttons = visual.ImageStim(
    win=win,
    name='block8_buttons', 
    image='images/buttons.png', mask=None,
    ori=0, pos=(0, -200), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "ITI_change"
ITI_changeClock = core.Clock()
change_ITI = visual.TextStim(win=win, name='change_ITI',
    text='Blank',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end"
endClock = core.Clock()
bye = visual.TextStim(win=win, name='bye',
    text='You have completed the task :)',
    font='Arial',
    pos=(0, 0), height=35, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instructions"-------
    # update component parameters for each repeat
    image.setImage(imgpath)
    key_resp.keys = []
    key_resp.rt = []
    incorrect.setOpacity(0)
    # keep track of which components have finished
    instructionsComponents = [image, key_resp, incorrect]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['1', '2', '9'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp.keys = theseKeys.name  # just the last key pressed
                key_resp.rt = theseKeys.rt
                # was this 'correct'?
                if (key_resp.keys == str(corrans)) or (key_resp.keys == corrans):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
        if len(key_resp.keys) > 0:
            if key_resp.keys[0] == str(corrans):
                continueRoutine = False
            else:
                incorrect.opacity = 1
        
        # *incorrect* updates
        if incorrect.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            incorrect.frameNStart = frameN  # exact frame index
            incorrect.tStart = t  # local t and not account for scr refresh
            incorrect.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(incorrect, 'tStartRefresh')  # time at next scr refresh
            incorrect.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp.keys',key_resp.keys)
    trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "shape_title"-------
routineTimer.add(3.500000)
# update component parameters for each repeat
# keep track of which components have finished
shape_titleComponents = [shape_name]
for thisComponent in shape_titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
shape_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "shape_title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = shape_titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=shape_titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *shape_name* updates
    if shape_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        shape_name.frameNStart = frameN  # exact frame index
        shape_name.tStart = t  # local t and not account for scr refresh
        shape_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shape_name, 'tStartRefresh')  # time at next scr refresh
        shape_name.setAutoDraw(True)
    if shape_name.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > shape_name.tStartRefresh + 3.5-frameTolerance:
            # keep track of stop time/frame for later
            shape_name.tStop = t  # not accounting for scr refresh
            shape_name.frameNStop = frameN  # exact frame index
            win.timeOnFlip(shape_name, 'tStopRefresh')  # time at next scr refresh
            shape_name.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in shape_titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "shape_title"-------
for thisComponent in shape_titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
block1_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('block1.xlsx'),
    seed=None, name='block1_trials')
thisExp.addLoop(block1_trials)  # add the loop to the experiment
thisBlock1_trial = block1_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1_trial.rgb)
if thisBlock1_trial != None:
    for paramName in thisBlock1_trial:
        exec('{} = thisBlock1_trial[paramName]'.format(paramName))

for thisBlock1_trial in block1_trials:
    currentLoop = block1_trials
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1_trial.rgb)
    if thisBlock1_trial != None:
        for paramName in thisBlock1_trial:
            exec('{} = thisBlock1_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "block1"-------
    routineTimer.add(2.800000)
    # update component parameters for each repeat
    block1_match.setImage(imgpath)
    block1_response.keys = []
    block1_response.rt = []
    # keep track of which components have finished
    block1Components = [block1_match, block1_response, block1_buttons]
    for thisComponent in block1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "block1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = block1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block1_match* updates
        if block1_match.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block1_match.frameNStart = frameN  # exact frame index
            block1_match.tStart = t  # local t and not account for scr refresh
            block1_match.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block1_match, 'tStartRefresh')  # time at next scr refresh
            block1_match.setAutoDraw(True)
        if block1_match.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block1_match.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                block1_match.tStop = t  # not accounting for scr refresh
                block1_match.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block1_match, 'tStopRefresh')  # time at next scr refresh
                block1_match.setAutoDraw(False)
        
        # *block1_response* updates
        waitOnFlip = False
        if block1_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block1_response.frameNStart = frameN  # exact frame index
            block1_response.tStart = t  # local t and not account for scr refresh
            block1_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block1_response, 'tStartRefresh')  # time at next scr refresh
            block1_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block1_response.clock.reset)  # t=0 on next screen flip
        if block1_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block1_response.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                block1_response.tStop = t  # not accounting for scr refresh
                block1_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block1_response, 'tStopRefresh')  # time at next scr refresh
                block1_response.status = FINISHED
        if block1_response.status == STARTED and not waitOnFlip:
            theseKeys = block1_response.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                block1_response.keys = theseKeys.name  # just the last key pressed
                block1_response.rt = theseKeys.rt
                # was this 'correct'?
                if (block1_response.keys == str(corrans)) or (block1_response.keys == corrans):
                    block1_response.corr = 1
                else:
                    block1_response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *block1_buttons* updates
        if block1_buttons.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block1_buttons.frameNStart = frameN  # exact frame index
            block1_buttons.tStart = t  # local t and not account for scr refresh
            block1_buttons.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block1_buttons, 'tStartRefresh')  # time at next scr refresh
            block1_buttons.setAutoDraw(True)
        if block1_buttons.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block1_buttons.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                block1_buttons.tStop = t  # not accounting for scr refresh
                block1_buttons.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block1_buttons, 'tStopRefresh')  # time at next scr refresh
                block1_buttons.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block1"-------
    for thisComponent in block1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block1_trials.addData('block1_match.started', block1_match.tStartRefresh)
    block1_trials.addData('block1_match.stopped', block1_match.tStopRefresh)
    # check responses
    if block1_response.keys in ['', [], None]:  # No response was made
        block1_response.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           block1_response.corr = 1;  # correct non-response
        else:
           block1_response.corr = 0;  # failed to respond (incorrectly)
    # store data for block1_trials (TrialHandler)
    block1_trials.addData('block1_response.keys',block1_response.keys)
    block1_trials.addData('block1_response.corr', block1_response.corr)
    if block1_response.keys != None:  # we had a response
        block1_trials.addData('block1_response.rt', block1_response.rt)
    
    # ------Prepare to start Routine "ITI_match"-------
    routineTimer.add(0.400000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_matchComponents = [match_ITI]
    for thisComponent in ITI_matchComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITI_matchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ITI_match"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITI_matchClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITI_matchClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *match_ITI* updates
        if match_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            match_ITI.frameNStart = frameN  # exact frame index
            match_ITI.tStart = t  # local t and not account for scr refresh
            match_ITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(match_ITI, 'tStartRefresh')  # time at next scr refresh
            match_ITI.setAutoDraw(True)
        if match_ITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > match_ITI.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                match_ITI.tStop = t  # not accounting for scr refresh
                match_ITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(match_ITI, 'tStopRefresh')  # time at next scr refresh
                match_ITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_matchComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI_match"-------
    for thisComponent in ITI_matchComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'block1_trials'


# ------Prepare to start Routine "change_title"-------
routineTimer.add(3.500000)
# update component parameters for each repeat
# keep track of which components have finished
change_titleComponents = [change_name]
for thisComponent in change_titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
change_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "change_title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = change_titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=change_titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *change_name* updates
    if change_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        change_name.frameNStart = frameN  # exact frame index
        change_name.tStart = t  # local t and not account for scr refresh
        change_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(change_name, 'tStartRefresh')  # time at next scr refresh
        change_name.setAutoDraw(True)
    if change_name.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > change_name.tStartRefresh + 3.5-frameTolerance:
            # keep track of stop time/frame for later
            change_name.tStop = t  # not accounting for scr refresh
            change_name.frameNStop = frameN  # exact frame index
            win.timeOnFlip(change_name, 'tStopRefresh')  # time at next scr refresh
            change_name.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in change_titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "change_title"-------
for thisComponent in change_titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
block2_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('block2.xlsx'),
    seed=None, name='block2_trials')
thisExp.addLoop(block2_trials)  # add the loop to the experiment
thisBlock2_trial = block2_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock2_trial.rgb)
if thisBlock2_trial != None:
    for paramName in thisBlock2_trial:
        exec('{} = thisBlock2_trial[paramName]'.format(paramName))

for thisBlock2_trial in block2_trials:
    currentLoop = block2_trials
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2_trial.rgb)
    if thisBlock2_trial != None:
        for paramName in thisBlock2_trial:
            exec('{} = thisBlock2_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "block2"-------
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    block2_change.setImage(imgpath)
    block2_response.keys = []
    block2_response.rt = []
    # keep track of which components have finished
    block2Components = [block2_change, block2_response, block2_buttons]
    for thisComponent in block2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "block2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = block2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block2_change* updates
        if block2_change.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2_change.frameNStart = frameN  # exact frame index
            block2_change.tStart = t  # local t and not account for scr refresh
            block2_change.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2_change, 'tStartRefresh')  # time at next scr refresh
            block2_change.setAutoDraw(True)
        if block2_change.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block2_change.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                block2_change.tStop = t  # not accounting for scr refresh
                block2_change.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block2_change, 'tStopRefresh')  # time at next scr refresh
                block2_change.setAutoDraw(False)
        
        # *block2_response* updates
        waitOnFlip = False
        if block2_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2_response.frameNStart = frameN  # exact frame index
            block2_response.tStart = t  # local t and not account for scr refresh
            block2_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2_response, 'tStartRefresh')  # time at next scr refresh
            block2_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block2_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block2_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block2_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block2_response.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                block2_response.tStop = t  # not accounting for scr refresh
                block2_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block2_response, 'tStopRefresh')  # time at next scr refresh
                block2_response.status = FINISHED
        if block2_response.status == STARTED and not waitOnFlip:
            theseKeys = block2_response.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                block2_response.keys = theseKeys.name  # just the last key pressed
                block2_response.rt = theseKeys.rt
                # was this 'correct'?
                if (block2_response.keys == str(corrans)) or (block2_response.keys == corrans):
                    block2_response.corr = 1
                else:
                    block2_response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *block2_buttons* updates
        if block2_buttons.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block2_buttons.frameNStart = frameN  # exact frame index
            block2_buttons.tStart = t  # local t and not account for scr refresh
            block2_buttons.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block2_buttons, 'tStartRefresh')  # time at next scr refresh
            block2_buttons.setAutoDraw(True)
        if block2_buttons.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block2_buttons.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                block2_buttons.tStop = t  # not accounting for scr refresh
                block2_buttons.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block2_buttons, 'tStopRefresh')  # time at next scr refresh
                block2_buttons.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block2"-------
    for thisComponent in block2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block2_trials.addData('block2_change.started', block2_change.tStartRefresh)
    block2_trials.addData('block2_change.stopped', block2_change.tStopRefresh)
    # check responses
    if block2_response.keys in ['', [], None]:  # No response was made
        block2_response.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           block2_response.corr = 1;  # correct non-response
        else:
           block2_response.corr = 0;  # failed to respond (incorrectly)
    # store data for block2_trials (TrialHandler)
    block2_trials.addData('block2_response.keys',block2_response.keys)
    block2_trials.addData('block2_response.corr', block2_response.corr)
    if block2_response.keys != None:  # we had a response
        block2_trials.addData('block2_response.rt', block2_response.rt)
    
    # ------Prepare to start Routine "ITI_change"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_changeComponents = [change_ITI]
    for thisComponent in ITI_changeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITI_changeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ITI_change"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITI_changeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITI_changeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *change_ITI* updates
        if change_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            change_ITI.frameNStart = frameN  # exact frame index
            change_ITI.tStart = t  # local t and not account for scr refresh
            change_ITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(change_ITI, 'tStartRefresh')  # time at next scr refresh
            change_ITI.setAutoDraw(True)
        if change_ITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > change_ITI.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                change_ITI.tStop = t  # not accounting for scr refresh
                change_ITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(change_ITI, 'tStopRefresh')  # time at next scr refresh
                change_ITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_changeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI_change"-------
    for thisComponent in ITI_changeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'block2_trials'


# ------Prepare to start Routine "shape_title"-------
routineTimer.add(3.500000)
# update component parameters for each repeat
# keep track of which components have finished
shape_titleComponents = [shape_name]
for thisComponent in shape_titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
shape_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "shape_title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = shape_titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=shape_titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *shape_name* updates
    if shape_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        shape_name.frameNStart = frameN  # exact frame index
        shape_name.tStart = t  # local t and not account for scr refresh
        shape_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shape_name, 'tStartRefresh')  # time at next scr refresh
        shape_name.setAutoDraw(True)
    if shape_name.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > shape_name.tStartRefresh + 3.5-frameTolerance:
            # keep track of stop time/frame for later
            shape_name.tStop = t  # not accounting for scr refresh
            shape_name.frameNStop = frameN  # exact frame index
            win.timeOnFlip(shape_name, 'tStopRefresh')  # time at next scr refresh
            shape_name.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in shape_titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "shape_title"-------
for thisComponent in shape_titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
block3_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('block3.xlsx'),
    seed=None, name='block3_trials')
thisExp.addLoop(block3_trials)  # add the loop to the experiment
thisBlock3_trial = block3_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock3_trial.rgb)
if thisBlock3_trial != None:
    for paramName in thisBlock3_trial:
        exec('{} = thisBlock3_trial[paramName]'.format(paramName))

for thisBlock3_trial in block3_trials:
    currentLoop = block3_trials
    # abbreviate parameter names if possible (e.g. rgb = thisBlock3_trial.rgb)
    if thisBlock3_trial != None:
        for paramName in thisBlock3_trial:
            exec('{} = thisBlock3_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "block3"-------
    routineTimer.add(2.800000)
    # update component parameters for each repeat
    block3_match.setImage(imgpath)
    block3_response.keys = []
    block3_response.rt = []
    # keep track of which components have finished
    block3Components = [block3_match, block3_response, block3_buttons]
    for thisComponent in block3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "block3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = block3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block3_match* updates
        if block3_match.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3_match.frameNStart = frameN  # exact frame index
            block3_match.tStart = t  # local t and not account for scr refresh
            block3_match.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3_match, 'tStartRefresh')  # time at next scr refresh
            block3_match.setAutoDraw(True)
        if block3_match.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block3_match.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                block3_match.tStop = t  # not accounting for scr refresh
                block3_match.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block3_match, 'tStopRefresh')  # time at next scr refresh
                block3_match.setAutoDraw(False)
        
        # *block3_response* updates
        waitOnFlip = False
        if block3_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3_response.frameNStart = frameN  # exact frame index
            block3_response.tStart = t  # local t and not account for scr refresh
            block3_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3_response, 'tStartRefresh')  # time at next scr refresh
            block3_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block3_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block3_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block3_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block3_response.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                block3_response.tStop = t  # not accounting for scr refresh
                block3_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block3_response, 'tStopRefresh')  # time at next scr refresh
                block3_response.status = FINISHED
        if block3_response.status == STARTED and not waitOnFlip:
            theseKeys = block3_response.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                block3_response.keys = theseKeys.name  # just the last key pressed
                block3_response.rt = theseKeys.rt
                # was this 'correct'?
                if (block3_response.keys == str(corrans)) or (block3_response.keys == corrans):
                    block3_response.corr = 1
                else:
                    block3_response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *block3_buttons* updates
        if block3_buttons.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block3_buttons.frameNStart = frameN  # exact frame index
            block3_buttons.tStart = t  # local t and not account for scr refresh
            block3_buttons.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block3_buttons, 'tStartRefresh')  # time at next scr refresh
            block3_buttons.setAutoDraw(True)
        if block3_buttons.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block3_buttons.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                block3_buttons.tStop = t  # not accounting for scr refresh
                block3_buttons.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block3_buttons, 'tStopRefresh')  # time at next scr refresh
                block3_buttons.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block3"-------
    for thisComponent in block3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block3_trials.addData('block3_match.started', block3_match.tStartRefresh)
    block3_trials.addData('block3_match.stopped', block3_match.tStopRefresh)
    # check responses
    if block3_response.keys in ['', [], None]:  # No response was made
        block3_response.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           block3_response.corr = 1;  # correct non-response
        else:
           block3_response.corr = 0;  # failed to respond (incorrectly)
    # store data for block3_trials (TrialHandler)
    block3_trials.addData('block3_response.keys',block3_response.keys)
    block3_trials.addData('block3_response.corr', block3_response.corr)
    if block3_response.keys != None:  # we had a response
        block3_trials.addData('block3_response.rt', block3_response.rt)
    
    # ------Prepare to start Routine "ITI_match"-------
    routineTimer.add(0.400000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_matchComponents = [match_ITI]
    for thisComponent in ITI_matchComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITI_matchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ITI_match"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITI_matchClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITI_matchClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *match_ITI* updates
        if match_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            match_ITI.frameNStart = frameN  # exact frame index
            match_ITI.tStart = t  # local t and not account for scr refresh
            match_ITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(match_ITI, 'tStartRefresh')  # time at next scr refresh
            match_ITI.setAutoDraw(True)
        if match_ITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > match_ITI.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                match_ITI.tStop = t  # not accounting for scr refresh
                match_ITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(match_ITI, 'tStopRefresh')  # time at next scr refresh
                match_ITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_matchComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI_match"-------
    for thisComponent in ITI_matchComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'block3_trials'


# ------Prepare to start Routine "change_title"-------
routineTimer.add(3.500000)
# update component parameters for each repeat
# keep track of which components have finished
change_titleComponents = [change_name]
for thisComponent in change_titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
change_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "change_title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = change_titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=change_titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *change_name* updates
    if change_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        change_name.frameNStart = frameN  # exact frame index
        change_name.tStart = t  # local t and not account for scr refresh
        change_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(change_name, 'tStartRefresh')  # time at next scr refresh
        change_name.setAutoDraw(True)
    if change_name.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > change_name.tStartRefresh + 3.5-frameTolerance:
            # keep track of stop time/frame for later
            change_name.tStop = t  # not accounting for scr refresh
            change_name.frameNStop = frameN  # exact frame index
            win.timeOnFlip(change_name, 'tStopRefresh')  # time at next scr refresh
            change_name.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in change_titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "change_title"-------
for thisComponent in change_titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
block4_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('block4.xlsx'),
    seed=None, name='block4_trials')
thisExp.addLoop(block4_trials)  # add the loop to the experiment
thisBlock4_trial = block4_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock4_trial.rgb)
if thisBlock4_trial != None:
    for paramName in thisBlock4_trial:
        exec('{} = thisBlock4_trial[paramName]'.format(paramName))

for thisBlock4_trial in block4_trials:
    currentLoop = block4_trials
    # abbreviate parameter names if possible (e.g. rgb = thisBlock4_trial.rgb)
    if thisBlock4_trial != None:
        for paramName in thisBlock4_trial:
            exec('{} = thisBlock4_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "block4"-------
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    block4_change.setImage(imgpath)
    block4_response.keys = []
    block4_response.rt = []
    # keep track of which components have finished
    block4Components = [block4_change, block4_response, block4_buttons]
    for thisComponent in block4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "block4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = block4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block4_change* updates
        if block4_change.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block4_change.frameNStart = frameN  # exact frame index
            block4_change.tStart = t  # local t and not account for scr refresh
            block4_change.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block4_change, 'tStartRefresh')  # time at next scr refresh
            block4_change.setAutoDraw(True)
        if block4_change.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block4_change.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                block4_change.tStop = t  # not accounting for scr refresh
                block4_change.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block4_change, 'tStopRefresh')  # time at next scr refresh
                block4_change.setAutoDraw(False)
        
        # *block4_response* updates
        waitOnFlip = False
        if block4_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block4_response.frameNStart = frameN  # exact frame index
            block4_response.tStart = t  # local t and not account for scr refresh
            block4_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block4_response, 'tStartRefresh')  # time at next scr refresh
            block4_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block4_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block4_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block4_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block4_response.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                block4_response.tStop = t  # not accounting for scr refresh
                block4_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block4_response, 'tStopRefresh')  # time at next scr refresh
                block4_response.status = FINISHED
        if block4_response.status == STARTED and not waitOnFlip:
            theseKeys = block4_response.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                block4_response.keys = theseKeys.name  # just the last key pressed
                block4_response.rt = theseKeys.rt
                # was this 'correct'?
                if (block4_response.keys == str(corrans)) or (block4_response.keys == corrans):
                    block4_response.corr = 1
                else:
                    block4_response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *block4_buttons* updates
        if block4_buttons.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block4_buttons.frameNStart = frameN  # exact frame index
            block4_buttons.tStart = t  # local t and not account for scr refresh
            block4_buttons.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block4_buttons, 'tStartRefresh')  # time at next scr refresh
            block4_buttons.setAutoDraw(True)
        if block4_buttons.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block4_buttons.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                block4_buttons.tStop = t  # not accounting for scr refresh
                block4_buttons.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block4_buttons, 'tStopRefresh')  # time at next scr refresh
                block4_buttons.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block4"-------
    for thisComponent in block4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block4_trials.addData('block4_change.started', block4_change.tStartRefresh)
    block4_trials.addData('block4_change.stopped', block4_change.tStopRefresh)
    # check responses
    if block4_response.keys in ['', [], None]:  # No response was made
        block4_response.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           block4_response.corr = 1;  # correct non-response
        else:
           block4_response.corr = 0;  # failed to respond (incorrectly)
    # store data for block4_trials (TrialHandler)
    block4_trials.addData('block4_response.keys',block4_response.keys)
    block4_trials.addData('block4_response.corr', block4_response.corr)
    if block4_response.keys != None:  # we had a response
        block4_trials.addData('block4_response.rt', block4_response.rt)
    
    # ------Prepare to start Routine "ITI_change"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_changeComponents = [change_ITI]
    for thisComponent in ITI_changeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITI_changeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ITI_change"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITI_changeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITI_changeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *change_ITI* updates
        if change_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            change_ITI.frameNStart = frameN  # exact frame index
            change_ITI.tStart = t  # local t and not account for scr refresh
            change_ITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(change_ITI, 'tStartRefresh')  # time at next scr refresh
            change_ITI.setAutoDraw(True)
        if change_ITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > change_ITI.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                change_ITI.tStop = t  # not accounting for scr refresh
                change_ITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(change_ITI, 'tStopRefresh')  # time at next scr refresh
                change_ITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_changeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI_change"-------
    for thisComponent in ITI_changeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'block4_trials'


# ------Prepare to start Routine "shape_title"-------
routineTimer.add(3.500000)
# update component parameters for each repeat
# keep track of which components have finished
shape_titleComponents = [shape_name]
for thisComponent in shape_titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
shape_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "shape_title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = shape_titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=shape_titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *shape_name* updates
    if shape_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        shape_name.frameNStart = frameN  # exact frame index
        shape_name.tStart = t  # local t and not account for scr refresh
        shape_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shape_name, 'tStartRefresh')  # time at next scr refresh
        shape_name.setAutoDraw(True)
    if shape_name.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > shape_name.tStartRefresh + 3.5-frameTolerance:
            # keep track of stop time/frame for later
            shape_name.tStop = t  # not accounting for scr refresh
            shape_name.frameNStop = frameN  # exact frame index
            win.timeOnFlip(shape_name, 'tStopRefresh')  # time at next scr refresh
            shape_name.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in shape_titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "shape_title"-------
for thisComponent in shape_titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
block5_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('block5.xlsx'),
    seed=None, name='block5_trials')
thisExp.addLoop(block5_trials)  # add the loop to the experiment
thisBlock5_trial = block5_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock5_trial.rgb)
if thisBlock5_trial != None:
    for paramName in thisBlock5_trial:
        exec('{} = thisBlock5_trial[paramName]'.format(paramName))

for thisBlock5_trial in block5_trials:
    currentLoop = block5_trials
    # abbreviate parameter names if possible (e.g. rgb = thisBlock5_trial.rgb)
    if thisBlock5_trial != None:
        for paramName in thisBlock5_trial:
            exec('{} = thisBlock5_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "block5"-------
    routineTimer.add(2.800000)
    # update component parameters for each repeat
    block5_match.setImage(imgpath)
    block5_response.keys = []
    block5_response.rt = []
    # keep track of which components have finished
    block5Components = [block5_match, block5_response, block5_buttons]
    for thisComponent in block5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "block5"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = block5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block5_match* updates
        if block5_match.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block5_match.frameNStart = frameN  # exact frame index
            block5_match.tStart = t  # local t and not account for scr refresh
            block5_match.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block5_match, 'tStartRefresh')  # time at next scr refresh
            block5_match.setAutoDraw(True)
        if block5_match.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block5_match.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                block5_match.tStop = t  # not accounting for scr refresh
                block5_match.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block5_match, 'tStopRefresh')  # time at next scr refresh
                block5_match.setAutoDraw(False)
        
        # *block5_response* updates
        waitOnFlip = False
        if block5_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block5_response.frameNStart = frameN  # exact frame index
            block5_response.tStart = t  # local t and not account for scr refresh
            block5_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block5_response, 'tStartRefresh')  # time at next scr refresh
            block5_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block5_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block5_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block5_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block5_response.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                block5_response.tStop = t  # not accounting for scr refresh
                block5_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block5_response, 'tStopRefresh')  # time at next scr refresh
                block5_response.status = FINISHED
        if block5_response.status == STARTED and not waitOnFlip:
            theseKeys = block5_response.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                block5_response.keys = theseKeys.name  # just the last key pressed
                block5_response.rt = theseKeys.rt
                # was this 'correct'?
                if (block5_response.keys == str(corrans)) or (block5_response.keys == corrans):
                    block5_response.corr = 1
                else:
                    block5_response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *block5_buttons* updates
        if block5_buttons.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block5_buttons.frameNStart = frameN  # exact frame index
            block5_buttons.tStart = t  # local t and not account for scr refresh
            block5_buttons.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block5_buttons, 'tStartRefresh')  # time at next scr refresh
            block5_buttons.setAutoDraw(True)
        if block5_buttons.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block5_buttons.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                block5_buttons.tStop = t  # not accounting for scr refresh
                block5_buttons.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block5_buttons, 'tStopRefresh')  # time at next scr refresh
                block5_buttons.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block5"-------
    for thisComponent in block5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block5_trials.addData('block5_match.started', block5_match.tStartRefresh)
    block5_trials.addData('block5_match.stopped', block5_match.tStopRefresh)
    # check responses
    if block5_response.keys in ['', [], None]:  # No response was made
        block5_response.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           block5_response.corr = 1;  # correct non-response
        else:
           block5_response.corr = 0;  # failed to respond (incorrectly)
    # store data for block5_trials (TrialHandler)
    block5_trials.addData('block5_response.keys',block5_response.keys)
    block5_trials.addData('block5_response.corr', block5_response.corr)
    if block5_response.keys != None:  # we had a response
        block5_trials.addData('block5_response.rt', block5_response.rt)
    
    # ------Prepare to start Routine "ITI_match"-------
    routineTimer.add(0.400000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_matchComponents = [match_ITI]
    for thisComponent in ITI_matchComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITI_matchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ITI_match"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITI_matchClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITI_matchClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *match_ITI* updates
        if match_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            match_ITI.frameNStart = frameN  # exact frame index
            match_ITI.tStart = t  # local t and not account for scr refresh
            match_ITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(match_ITI, 'tStartRefresh')  # time at next scr refresh
            match_ITI.setAutoDraw(True)
        if match_ITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > match_ITI.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                match_ITI.tStop = t  # not accounting for scr refresh
                match_ITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(match_ITI, 'tStopRefresh')  # time at next scr refresh
                match_ITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_matchComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI_match"-------
    for thisComponent in ITI_matchComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'block5_trials'


# ------Prepare to start Routine "change_title"-------
routineTimer.add(3.500000)
# update component parameters for each repeat
# keep track of which components have finished
change_titleComponents = [change_name]
for thisComponent in change_titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
change_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "change_title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = change_titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=change_titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *change_name* updates
    if change_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        change_name.frameNStart = frameN  # exact frame index
        change_name.tStart = t  # local t and not account for scr refresh
        change_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(change_name, 'tStartRefresh')  # time at next scr refresh
        change_name.setAutoDraw(True)
    if change_name.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > change_name.tStartRefresh + 3.5-frameTolerance:
            # keep track of stop time/frame for later
            change_name.tStop = t  # not accounting for scr refresh
            change_name.frameNStop = frameN  # exact frame index
            win.timeOnFlip(change_name, 'tStopRefresh')  # time at next scr refresh
            change_name.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in change_titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "change_title"-------
for thisComponent in change_titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
block6_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('block6.xlsx'),
    seed=None, name='block6_trials')
thisExp.addLoop(block6_trials)  # add the loop to the experiment
thisBlock6_trial = block6_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock6_trial.rgb)
if thisBlock6_trial != None:
    for paramName in thisBlock6_trial:
        exec('{} = thisBlock6_trial[paramName]'.format(paramName))

for thisBlock6_trial in block6_trials:
    currentLoop = block6_trials
    # abbreviate parameter names if possible (e.g. rgb = thisBlock6_trial.rgb)
    if thisBlock6_trial != None:
        for paramName in thisBlock6_trial:
            exec('{} = thisBlock6_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "block6"-------
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    block6_change.setImage(imgpath)
    block6_response.keys = []
    block6_response.rt = []
    # keep track of which components have finished
    block6Components = [block6_change, block6_response, block6_buttons]
    for thisComponent in block6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "block6"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = block6Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block6Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block6_change* updates
        if block6_change.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block6_change.frameNStart = frameN  # exact frame index
            block6_change.tStart = t  # local t and not account for scr refresh
            block6_change.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block6_change, 'tStartRefresh')  # time at next scr refresh
            block6_change.setAutoDraw(True)
        if block6_change.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block6_change.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                block6_change.tStop = t  # not accounting for scr refresh
                block6_change.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block6_change, 'tStopRefresh')  # time at next scr refresh
                block6_change.setAutoDraw(False)
        
        # *block6_response* updates
        waitOnFlip = False
        if block6_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block6_response.frameNStart = frameN  # exact frame index
            block6_response.tStart = t  # local t and not account for scr refresh
            block6_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block6_response, 'tStartRefresh')  # time at next scr refresh
            block6_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block6_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block6_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block6_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block6_response.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                block6_response.tStop = t  # not accounting for scr refresh
                block6_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block6_response, 'tStopRefresh')  # time at next scr refresh
                block6_response.status = FINISHED
        if block6_response.status == STARTED and not waitOnFlip:
            theseKeys = block6_response.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                block6_response.keys = theseKeys.name  # just the last key pressed
                block6_response.rt = theseKeys.rt
                # was this 'correct'?
                if (block6_response.keys == str(corrans)) or (block6_response.keys == corrans):
                    block6_response.corr = 1
                else:
                    block6_response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *block6_buttons* updates
        if block6_buttons.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block6_buttons.frameNStart = frameN  # exact frame index
            block6_buttons.tStart = t  # local t and not account for scr refresh
            block6_buttons.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block6_buttons, 'tStartRefresh')  # time at next scr refresh
            block6_buttons.setAutoDraw(True)
        if block6_buttons.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block6_buttons.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                block6_buttons.tStop = t  # not accounting for scr refresh
                block6_buttons.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block6_buttons, 'tStopRefresh')  # time at next scr refresh
                block6_buttons.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block6"-------
    for thisComponent in block6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block6_trials.addData('block6_change.started', block6_change.tStartRefresh)
    block6_trials.addData('block6_change.stopped', block6_change.tStopRefresh)
    # check responses
    if block6_response.keys in ['', [], None]:  # No response was made
        block6_response.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           block6_response.corr = 1;  # correct non-response
        else:
           block6_response.corr = 0;  # failed to respond (incorrectly)
    # store data for block6_trials (TrialHandler)
    block6_trials.addData('block6_response.keys',block6_response.keys)
    block6_trials.addData('block6_response.corr', block6_response.corr)
    if block6_response.keys != None:  # we had a response
        block6_trials.addData('block6_response.rt', block6_response.rt)
    
    # ------Prepare to start Routine "ITI_change"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_changeComponents = [change_ITI]
    for thisComponent in ITI_changeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITI_changeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ITI_change"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITI_changeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITI_changeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *change_ITI* updates
        if change_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            change_ITI.frameNStart = frameN  # exact frame index
            change_ITI.tStart = t  # local t and not account for scr refresh
            change_ITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(change_ITI, 'tStartRefresh')  # time at next scr refresh
            change_ITI.setAutoDraw(True)
        if change_ITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > change_ITI.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                change_ITI.tStop = t  # not accounting for scr refresh
                change_ITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(change_ITI, 'tStopRefresh')  # time at next scr refresh
                change_ITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_changeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI_change"-------
    for thisComponent in ITI_changeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'block6_trials'


# ------Prepare to start Routine "shape_title"-------
routineTimer.add(3.500000)
# update component parameters for each repeat
# keep track of which components have finished
shape_titleComponents = [shape_name]
for thisComponent in shape_titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
shape_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "shape_title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = shape_titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=shape_titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *shape_name* updates
    if shape_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        shape_name.frameNStart = frameN  # exact frame index
        shape_name.tStart = t  # local t and not account for scr refresh
        shape_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(shape_name, 'tStartRefresh')  # time at next scr refresh
        shape_name.setAutoDraw(True)
    if shape_name.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > shape_name.tStartRefresh + 3.5-frameTolerance:
            # keep track of stop time/frame for later
            shape_name.tStop = t  # not accounting for scr refresh
            shape_name.frameNStop = frameN  # exact frame index
            win.timeOnFlip(shape_name, 'tStopRefresh')  # time at next scr refresh
            shape_name.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in shape_titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "shape_title"-------
for thisComponent in shape_titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
block7_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('block7.xlsx'),
    seed=None, name='block7_trials')
thisExp.addLoop(block7_trials)  # add the loop to the experiment
thisBlock7_trial = block7_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock7_trial.rgb)
if thisBlock7_trial != None:
    for paramName in thisBlock7_trial:
        exec('{} = thisBlock7_trial[paramName]'.format(paramName))

for thisBlock7_trial in block7_trials:
    currentLoop = block7_trials
    # abbreviate parameter names if possible (e.g. rgb = thisBlock7_trial.rgb)
    if thisBlock7_trial != None:
        for paramName in thisBlock7_trial:
            exec('{} = thisBlock7_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "block7"-------
    routineTimer.add(2.800000)
    # update component parameters for each repeat
    block7_match.setImage(imgpath)
    block7_response.keys = []
    block7_response.rt = []
    # keep track of which components have finished
    block7Components = [block7_match, block7_response, block7_buttons]
    for thisComponent in block7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "block7"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = block7Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block7Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block7_match* updates
        if block7_match.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block7_match.frameNStart = frameN  # exact frame index
            block7_match.tStart = t  # local t and not account for scr refresh
            block7_match.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block7_match, 'tStartRefresh')  # time at next scr refresh
            block7_match.setAutoDraw(True)
        if block7_match.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block7_match.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                block7_match.tStop = t  # not accounting for scr refresh
                block7_match.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block7_match, 'tStopRefresh')  # time at next scr refresh
                block7_match.setAutoDraw(False)
        
        # *block7_response* updates
        waitOnFlip = False
        if block7_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block7_response.frameNStart = frameN  # exact frame index
            block7_response.tStart = t  # local t and not account for scr refresh
            block7_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block7_response, 'tStartRefresh')  # time at next scr refresh
            block7_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block7_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block7_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block7_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block7_response.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                block7_response.tStop = t  # not accounting for scr refresh
                block7_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block7_response, 'tStopRefresh')  # time at next scr refresh
                block7_response.status = FINISHED
        if block7_response.status == STARTED and not waitOnFlip:
            theseKeys = block7_response.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                block7_response.keys = theseKeys.name  # just the last key pressed
                block7_response.rt = theseKeys.rt
                # was this 'correct'?
                if (block7_response.keys == str(corrans)) or (block7_response.keys == corrans):
                    block7_response.corr = 1
                else:
                    block7_response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *block7_buttons* updates
        if block7_buttons.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block7_buttons.frameNStart = frameN  # exact frame index
            block7_buttons.tStart = t  # local t and not account for scr refresh
            block7_buttons.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block7_buttons, 'tStartRefresh')  # time at next scr refresh
            block7_buttons.setAutoDraw(True)
        if block7_buttons.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block7_buttons.tStartRefresh + 2.8-frameTolerance:
                # keep track of stop time/frame for later
                block7_buttons.tStop = t  # not accounting for scr refresh
                block7_buttons.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block7_buttons, 'tStopRefresh')  # time at next scr refresh
                block7_buttons.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block7"-------
    for thisComponent in block7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block7_trials.addData('block7_match.started', block7_match.tStartRefresh)
    block7_trials.addData('block7_match.stopped', block7_match.tStopRefresh)
    # check responses
    if block7_response.keys in ['', [], None]:  # No response was made
        block7_response.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           block7_response.corr = 1;  # correct non-response
        else:
           block7_response.corr = 0;  # failed to respond (incorrectly)
    # store data for block7_trials (TrialHandler)
    block7_trials.addData('block7_response.keys',block7_response.keys)
    block7_trials.addData('block7_response.corr', block7_response.corr)
    if block7_response.keys != None:  # we had a response
        block7_trials.addData('block7_response.rt', block7_response.rt)
    
    # ------Prepare to start Routine "ITI_match"-------
    routineTimer.add(0.400000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_matchComponents = [match_ITI]
    for thisComponent in ITI_matchComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITI_matchClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ITI_match"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITI_matchClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITI_matchClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *match_ITI* updates
        if match_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            match_ITI.frameNStart = frameN  # exact frame index
            match_ITI.tStart = t  # local t and not account for scr refresh
            match_ITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(match_ITI, 'tStartRefresh')  # time at next scr refresh
            match_ITI.setAutoDraw(True)
        if match_ITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > match_ITI.tStartRefresh + 0.4-frameTolerance:
                # keep track of stop time/frame for later
                match_ITI.tStop = t  # not accounting for scr refresh
                match_ITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(match_ITI, 'tStopRefresh')  # time at next scr refresh
                match_ITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_matchComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI_match"-------
    for thisComponent in ITI_matchComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'block7_trials'


# ------Prepare to start Routine "change_title"-------
routineTimer.add(3.500000)
# update component parameters for each repeat
# keep track of which components have finished
change_titleComponents = [change_name]
for thisComponent in change_titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
change_titleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "change_title"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = change_titleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=change_titleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *change_name* updates
    if change_name.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        change_name.frameNStart = frameN  # exact frame index
        change_name.tStart = t  # local t and not account for scr refresh
        change_name.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(change_name, 'tStartRefresh')  # time at next scr refresh
        change_name.setAutoDraw(True)
    if change_name.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > change_name.tStartRefresh + 3.5-frameTolerance:
            # keep track of stop time/frame for later
            change_name.tStop = t  # not accounting for scr refresh
            change_name.frameNStop = frameN  # exact frame index
            win.timeOnFlip(change_name, 'tStopRefresh')  # time at next scr refresh
            change_name.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in change_titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "change_title"-------
for thisComponent in change_titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
block8_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('block8.xlsx'),
    seed=None, name='block8_trials')
thisExp.addLoop(block8_trials)  # add the loop to the experiment
thisBlock8_trial = block8_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock8_trial.rgb)
if thisBlock8_trial != None:
    for paramName in thisBlock8_trial:
        exec('{} = thisBlock8_trial[paramName]'.format(paramName))

for thisBlock8_trial in block8_trials:
    currentLoop = block8_trials
    # abbreviate parameter names if possible (e.g. rgb = thisBlock8_trial.rgb)
    if thisBlock8_trial != None:
        for paramName in thisBlock8_trial:
            exec('{} = thisBlock8_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "block8"-------
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    block8_change.setImage(imgpath)
    block8_response.keys = []
    block8_response.rt = []
    # keep track of which components have finished
    block8Components = [block8_change, block8_response, block8_buttons]
    for thisComponent in block8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    block8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "block8"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = block8Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=block8Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *block8_change* updates
        if block8_change.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block8_change.frameNStart = frameN  # exact frame index
            block8_change.tStart = t  # local t and not account for scr refresh
            block8_change.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block8_change, 'tStartRefresh')  # time at next scr refresh
            block8_change.setAutoDraw(True)
        if block8_change.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block8_change.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                block8_change.tStop = t  # not accounting for scr refresh
                block8_change.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block8_change, 'tStopRefresh')  # time at next scr refresh
                block8_change.setAutoDraw(False)
        
        # *block8_response* updates
        waitOnFlip = False
        if block8_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block8_response.frameNStart = frameN  # exact frame index
            block8_response.tStart = t  # local t and not account for scr refresh
            block8_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block8_response, 'tStartRefresh')  # time at next scr refresh
            block8_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(block8_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(block8_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if block8_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block8_response.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                block8_response.tStop = t  # not accounting for scr refresh
                block8_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block8_response, 'tStopRefresh')  # time at next scr refresh
                block8_response.status = FINISHED
        if block8_response.status == STARTED and not waitOnFlip:
            theseKeys = block8_response.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                block8_response.keys = theseKeys.name  # just the last key pressed
                block8_response.rt = theseKeys.rt
                # was this 'correct'?
                if (block8_response.keys == str(corrans)) or (block8_response.keys == corrans):
                    block8_response.corr = 1
                else:
                    block8_response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *block8_buttons* updates
        if block8_buttons.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            block8_buttons.frameNStart = frameN  # exact frame index
            block8_buttons.tStart = t  # local t and not account for scr refresh
            block8_buttons.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(block8_buttons, 'tStartRefresh')  # time at next scr refresh
            block8_buttons.setAutoDraw(True)
        if block8_buttons.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > block8_buttons.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                block8_buttons.tStop = t  # not accounting for scr refresh
                block8_buttons.frameNStop = frameN  # exact frame index
                win.timeOnFlip(block8_buttons, 'tStopRefresh')  # time at next scr refresh
                block8_buttons.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in block8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "block8"-------
    for thisComponent in block8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block8_trials.addData('block8_change.started', block8_change.tStartRefresh)
    block8_trials.addData('block8_change.stopped', block8_change.tStopRefresh)
    # check responses
    if block8_response.keys in ['', [], None]:  # No response was made
        block8_response.keys = None
        # was no response the correct answer?!
        if str(corrans).lower() == 'none':
           block8_response.corr = 1;  # correct non-response
        else:
           block8_response.corr = 0;  # failed to respond (incorrectly)
    # store data for block8_trials (TrialHandler)
    block8_trials.addData('block8_response.keys',block8_response.keys)
    block8_trials.addData('block8_response.corr', block8_response.corr)
    if block8_response.keys != None:  # we had a response
        block8_trials.addData('block8_response.rt', block8_response.rt)
    
    # ------Prepare to start Routine "ITI_change"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ITI_changeComponents = [change_ITI]
    for thisComponent in ITI_changeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITI_changeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ITI_change"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITI_changeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITI_changeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *change_ITI* updates
        if change_ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            change_ITI.frameNStart = frameN  # exact frame index
            change_ITI.tStart = t  # local t and not account for scr refresh
            change_ITI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(change_ITI, 'tStartRefresh')  # time at next scr refresh
            change_ITI.setAutoDraw(True)
        if change_ITI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > change_ITI.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                change_ITI.tStop = t  # not accounting for scr refresh
                change_ITI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(change_ITI, 'tStopRefresh')  # time at next scr refresh
                change_ITI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITI_changeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI_change"-------
    for thisComponent in ITI_changeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'block8_trials'


# ------Prepare to start Routine "end"-------
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [bye]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *bye* updates
    if bye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bye.frameNStart = frameN  # exact frame index
        bye.tStart = t  # local t and not account for scr refresh
        bye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bye, 'tStartRefresh')  # time at next scr refresh
        bye.setAutoDraw(True)
    if bye.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > bye.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            bye.tStop = t  # not accounting for scr refresh
            bye.frameNStop = frameN  # exact frame index
            win.timeOnFlip(bye, 'tStopRefresh')  # time at next scr refresh
            bye.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
