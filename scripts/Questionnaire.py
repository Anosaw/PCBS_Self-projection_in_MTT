text_size = text_size"""
This is the questionnaire the participants should fill out before the exp
We are presenting the events to the participants
They must enter the date, followed by a trust indicator (from 1 to 5)
"""

import expyriment

#Create and initialize exp
questionnaire = expyriment.design.Experiment(name = "Questionnaire")
expyriment.control.initialize(questionnaire)

good_answer = True
text_size = 60

#Design block
block_questionnaire = expyriment.design.Block(name = "Questionnaire block")

#Design trials
trial1985 = expyriment.design.Trial()
trial1988 = expyriment.design.Trial()
trial1991 = expyriment.design.Trial()
trial1994 = expyriment.design.Trial()
trial1997 = expyriment.design.Trial()
trial2000 = expyriment.design.Trial()
trial2003 = expyriment.design.Trial()
trial2006 = expyriment.design.Trial()
trial2009 = expyriment.design.Trial()
trial2012 = expyriment.design.Trial()
trial2015 = expyriment.design.Trial()
trial2018 = expyriment.design.Trial()
trial2019Past = expyriment.design.Trial()
trial2019Future = expyriment.design.Trial()
trial2020 = expyriment.design.Trial()
trial2020 = expyriment.design.Trial()
trial2023 = expyriment.design.Trial()
trial2026 = expyriment.design.Trial()
trial2029 = expyriment.design.Trial()
trial2032 = expyriment.design.Trial()
trial2035 = expyriment.design.Trial()
trial2038 = expyriment.design.Trial()
trial2041 = expyriment.design.Trial()
trial2044 = expyriment.design.Trial()
trial2047 = expyriment.design.Trial()
trial2050 = expyriment.design.Trial()
trial2053 = expyriment.design.Trial()

#Create stimuli and preload them
event1985 = expyriment.stimuli.TextLine(text = "trou ozone", text_size = text_size)
event1985.preload()

event1988 = expyriment.stimuli.TextLine(text = "JO Nagoya", text_size = text_size)
event1988.preload()

event1991 = expyriment.stimuli.TextLine(text = "dislocation URSS", text_size = text_size)
event1991.preload()

event1994 = expyriment.stimuli.TextLine(text = "métro Bordeaux", text_size = text_size)
event1994.preload()

event1997 = expyriment.stimuli.TextLine(text = "Harry Potter", text_size = text_size)
event1997.preload()

event2000 = expyriment.stimuli.TextLine(text = "Lettonie Eurovision", text_size = text_size)
event2000.preload()

event2003 = expyriment.stimuli.TextLine( text = "génome humain", text_size = text_size)
event2003.preload()

event2006 = expyriment.stimuli.TextLine(text = "tramway Paris", text_size = text_size)
event2006.preload()

event2009 = expyriment.stimuli.TextLine(text = "création Bitcoin", text_size = text_size)
event2009.preload()

event2012 = expyriment.stimuli.TextLine(text = "Curiosity Mars", text_size = text_size)
event2012.preload()

event2015 = expyriment.stimuli.TextLine(text = "musée Metallica", text_size = text_size)
event2015.preload()

event2018 = expyriment.stimuli.TextLine(text = "Simone Veil", text_size = text_size)
event2018.preload()

event2019Past = expyriment.stimuli.TextLine(text = "Netflix Friends", text_size = text_size)
event2019Past.preload()

event2019Future = expyriment.stimuli.TextLine(text = "coupe football", text_size = text_size)
event2019Future.preload()

event2020 = expyriment.stimuli.TextLine(text = "viandes artificielles", text_size = text_size)
event2020.preload()

event2023 = expyriment.stimuli.TextLine(text = "loup Japon", text_size = text_size)
event2023.preload()

event2026 = expyriment.stimuli.TextLine(text = "inauguration Dubaïland", text_size = text_size)
event2026.preload()

event2029 = expyriment.stimuli.TextLine(text = "usine photosynthèse", text_size = text_size)
event2029.preload()

event2032 = expyriment.stimuli.TextLine(text = "Grand Paris", text_size = text_size)
event2032.preload()

event2035 = expyriment.stimuli.TextLine(text = "bateaux automatiques", text_size = text_size)
event2035.preload()

event2038 = expyriment.stimuli.TextLine(text = "avions solaires", text_size = text_size)
event2038.preload()

event2041 = expyriment.stimuli.TextLine(text = "tunnel Bering", text_size = text_size)
event2041.preload()

event2044 = expyriment.stimuli.TextLine(text = "thérapie Sida", text_size = text_size)
event2044.preload()

event2050 = expyriment.stimuli.TextLine(text = "humain Mars", text_size = text_size)
event2050.preload()

event2047 = expyriment.stimuli.TextLine(text = "9.5 milliards", text_size = text_size)
event2047.preload()

event2053 = expyriment.stimuli.TextLine(text = "gaz renouvelable", text_size = text_size)
event2053.preload()


#Add events to trials and set date as factor
trial1985.add_stimulus(event1985)
trial1985.set_factor("Date", 1985)
trial1985.set_factor("Fictional", False)

trial1988.add_stimulus(event1988)
trial1988.set_factor("Date", 1988)
trial1988.set_factor("Fictional", True)

trial1991.add_stimulus(event1991)
trial1991.set_factor("Date", 1991)
trial1991.set_factor("Fictional", False)

trial1994.add_stimulus(event1994)
trial1994.set_factor("Date", 1994)
trial1994.set_factor("Fictional", True)

trial1997.add_stimulus(event1997)
trial1997.set_factor("Date", 1997)
trial1997.set_factor("Fictional", False)

trial2000.add_stimulus(event2000)
trial2000.set_factor("Date", 2000)
trial2000.set_factor("Fictional", True)

trial2003.add_stimulus(event2003)
trial2003.set_factor("Date", 2003)
trial2003.set_factor("Fictional", False)

trial2006.add_stimulus(event2006)
trial2006.set_factor("Date", 2006)
trial2006.set_factor("Fictional", False)

trial2009.add_stimulus(event2009)
trial2009.set_factor("Date", 2009)
trial2009.set_factor("Fictional", False)

trial2012.add_stimulus(event2012)
trial2012.set_factor("Date", 2012)
trial2012.set_factor("Fictional", False)

trial2015.add_stimulus(event2015)
trial2015.set_factor("Date", 2015)
trial2015.set_factor("Fictional", True)

trial2018.add_stimulus(event2018)
trial2018.set_factor("Date", 2018)
trial2018.set_factor("Fictional", False)

trial2019Past.add_stimulus(event2019Past)
trial2019Past.set_factor("Date", 2019)
trial2019Past.set_factor("Fictional", True)

trial2019Future.add_stimulus(event2019Future)
trial2019Future.set_factor("Date", 2019)
trial2019Future.set_factor("Fictional", False)

trial2020.add_stimulus(event2020)
trial2020.set_factor("Date", 2020)
trial2020.set_factor("Fictional", False)

trial2023.add_stimulus(event2023)
trial2023.set_factor("Date", 2023)
trial2023.set_factor("Fictional", True)

trial2026.add_stimulus(event2026)
trial2026.set_factor("Date", 2026)
trial2026.set_factor("Fictional", False)

trial2029.add_stimulus(event2029)
trial2029.set_factor("Date", 2029)
trial2029.set_factor("Fictional", True)

trial2032.add_stimulus(event2032)
trial2032.set_factor("Date", 2032)
trial2032.set_factor("Fictional", False)

trial2035.add_stimulus(event2035)
trial2035.set_factor("Date", 2035)
trial2035.set_factor("Fictional", False)

trial2038.add_stimulus(event2038)
trial2038.set_factor("Date", 2038)
trial2038.set_factor("Fictional", True)

trial2041.add_stimulus(event2041)
trial2041.set_factor("Date", 2041)
trial2041.set_factor("Fictional", False)

trial2044.add_stimulus(event2044)
trial2044.set_factor("Date", 2044)
trial2044.set_factor("Fictional", True)

trial2047.add_stimulus(event2047)
trial2047.set_factor("Date", 2047)
trial2047.set_factor("Fictional", False)

trial2050.add_stimulus(event2050)
trial2050.set_factor("Date", 2050)
trial2050.set_factor("Fictional", True)

trial2053.add_stimulus(event2053)
trial2053.set_factor("Date", 2053)
trial2053.set_factor("Fictional", False)

#Add trials to block
block_questionnaire.add_trial(trial1985)
block_questionnaire.add_trial(trial1988)
block_questionnaire.add_trial(trial1991)
block_questionnaire.add_trial(trial1994)
block_questionnaire.add_trial(trial1997)
block_questionnaire.add_trial(trial2000)
block_questionnaire.add_trial(trial2003)
block_questionnaire.add_trial(trial2006)
block_questionnaire.add_trial(trial2009)
block_questionnaire.add_trial(trial2012)
block_questionnaire.add_trial(trial2015)
block_questionnaire.add_trial(trial2018)
block_questionnaire.add_trial(trial2019Past)
block_questionnaire.add_trial(trial2019Future)
block_questionnaire.add_trial(trial2020)
block_questionnaire.add_trial(trial2023)
block_questionnaire.add_trial(trial2026)
block_questionnaire.add_trial(trial2029)
block_questionnaire.add_trial(trial2032)
block_questionnaire.add_trial(trial2035)
block_questionnaire.add_trial(trial2038)
block_questionnaire.add_trial(trial2041)
block_questionnaire.add_trial(trial2044)
block_questionnaire.add_trial(trial2047)
block_questionnaire.add_trial(trial2050)
block_questionnaire.add_trial(trial2053)


#Create other needed stimuli and trials
errorDate = expyriment.stimuli.TextLine(text = "Entrer une date", text_size = text_size)
errorDate.preload()

errorTrust = expyriment.stimuli.TextLine(text = "Entrer un nombre", text_size = text_size)
errorTrust.preload()

#Let's put a fixation cross
fixcross = expyriment.stimuli.FixCross(size = (50, 50), line_width = 4)
fixcross.preload()

#Set experimental data variables names
MTTexp.add_data_variable_names(["date", "fictional", "projection_to_event_distance", "good_answer", "RT"])

#Start experiment
expyriment.control.start()

for trial in block_questionnaire.trials:
    fixcross.present()
    questionnaire.clock.wait(1000)
    trial.stimuli[0].present()
    questionnaire.keybord.wait(keys = expyriment.misc.constants.K_KP_SPACE)

#Here put answer (check if valid input)
    questionDate = expyriment.io.TextInput(message = "date?", length = 4,
     message_text_size = text_size, user_text_size = text_size)
    try:
        answerDate = int(questionDate.get())
    except ValueError:
        errorDate.present()
        questionDate = expyriment.io.TextInput(message = "date?", length = 4,
         message_text_size = text_size, user_text_size = text_size)

    if answerDate == trial.get_factor("Date"):
        good_answer = True
    else:
        good_answer = False

    questionTrust = expyriment.io.TextInput(message = "confiance?", length = 1,
     message_text_size = text_size, user_text_size = text_size)
    try:
        answerTrust = int(questionTrust.get())
    except ValueError:
        errorTrust.present()
        questionTrust = expyriment.io.TextInput(message = "confiance?", length = 1,
         message_text_size = text_size, user_text_size = text_size)

    if answerTrust < 3:
        good_answer = False

    questionnaire.data.add([trial.get_factor("Date"), trial.get_factor("Fictional"), good_answer]) #Add data
    questionnaire.clock.wait(500) #Wait before going to the next event


expyriment.control.end()


#Answer

#Feedback?
