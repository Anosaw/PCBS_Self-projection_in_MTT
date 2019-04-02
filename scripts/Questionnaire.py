#This is the questionnaire the participants should fill out before the exp
#We are presenting the events to the participants
#They must enter the date, followed by a trust indicator (from 1 to 5)
#If the answer is wrong or the trust too low
#The event will be removed from the experiment

import expyriment

#Create and initialize exp
questionnaire = expyriment.design.Experiment(name = "Questionnaire")
expyriment.control.initialize(questionnaire)

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
trial2019 = expyriment.design.Trial()
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
trial2050 = expyriment.design.Trial()
trial2053 = expyriment.design.Trial()

#Create stimuli and preload them
event1985 = expyriment.stimuli.TextLine(text = "Trou ozone", text_size = 40)
event1985.preload()

event1988 = expyriment.stimuli.TextLine(text = "JO Nagoya", text_size = 40)
event1988.preload()

event1991 = expyriment.stimuli.TextLine(text = "Dislocation URSS", text_size = 40)
event1991.preload()

event1994 = expyriment.stimuli.TextLine(text = "Métro Bordeaux", text_size = 40)
event1994.preload()

event1997 = expyriment.stimuli.TextLine(text = "Harry Potter", text_size = 40)
event1997.preload()

event2000 = expyriment.stimuli.TextLine(text = "Lettonie Eurovision", text_size = 40)
event2000.preload()

event2003 = expyriment.stimuli.TextLine( text = "Génome humain", text_size = 40)
event2003.preload()

event2006 = expyriment.stimuli.TextLine(text = "Tramway Paris", text_size = 40)
event2006.preload()

event2009 = expyriment.stimuli.TextLine(text = "Création Bitcoin", text_size = 40)
event2009.preload()

event2012 = expyriment.stimuli.TextLine(text = "Curiosity sur Mars", text_size = 40)
event2012.preload()

event2015 = expyriment.stimuli.TextLine(text = "Musée Metallica", text_size = 40)
event2015.preload()

event2018 = expyriment.stimuli.TextLine(text = "Simone Veil", text_size = 40)
event2018.preload()

event2019 = expyriment.stimuli.TextLine(text = "Coupe football", text_size = 40)
event2019.preload()

event2020 = expyriment.stimuli.TextLine(text = "Viandes artificielles", text_size = 40)
event2020.preload()

event2023 = expyriment.stimuli.TextLine(text = "tour Montparnasse", text_size = 40)
event2023.preload()

event2026 = expyriment.stimuli.TextLine(text = "JO d'hiver", text_size = 40)
event2026.preload()

event2029 = expyriment.stimuli.TextLine(text = "Arrêt centimes", text_size = 40)
event2029.preload()

event2032 = expyriment.stimuli.TextLine(text = "Grand Paris", text_size = 40)
event2032.preload()

event2035 = expyriment.stimuli.TextLine(text = "port Alexandrie", text_size = 40)
event2035.preload()

event2038 = expyriment.stimuli.TextLine(text = "Avions solaires", text_size = 40)
event2038.preload()

event2041 = expyriment.stimuli.TextLine(text = "Tunnel sous Bering", text_size = 40)
event2041.preload()

event2044 = expyriment.stimuli.TextLine(text = "Thérapie Sida", text_size = 40)
event2044.preload()

event2050 = expyriment.stimuli.TextLine(text = "Humain sur Mars", text_size = 40)
event2050.preload()

event2053 = expyriment.stimuli.TextLine(text = "Gaz renouvelable", text_size = 40)
event2053.preload()

#Add events to trials and set date as factor
trial1985.add_stimulus(event1985)
trial1985.set_factor("trueDate", 1985)

trial1988.add_stimulus(event1988)
trial1988.set_factor("trueDate", 1988)

trial1991.add_stimulus(event1991)
trial1991.set_factor("trueDate", 1991)

trial1994.add_stimulus(event1994)
trial1994.set_factor("trueDate", 1994)

trial1997.add_stimulus(event1997)
trial1997.set_factor("trueDate", 1997)

trial2000.add_stimulus(event2000)
trial2000.set_factor("trueDate", 2000)

trial2003.add_stimulus(event2003)
trial2003.set_factor("trueDate", 2003)

trial2006.add_stimulus(event2006)
trial2006.set_factor("trueDate", 2006)

trial2009.add_stimulus(event2009)
trial2009.set_factor("trueDate", 2009)

trial2012.add_stimulus(event2012)
trial2012.set_factor("trueDate", 2012)

trial2015.add_stimulus(event2015)
trial2015.set_factor("trueDate", 2015)

trial2018.add_stimulus(event2018)
trial2018.set_factor("trueDate", 2018)

trial2019.add_stimulus(event2019)
trial2019.set_factor("trueDate", 2019)

trial2020.add_stimulus(event2020)
trial2020.set_factor("trueDate", 2020)

trial2023.add_stimulus(event2023)
trial2023.set_factor("trueDate", 2023)

trial2026.add_stimulus(event2026)
trial2026.set_factor("trueDate", 2026)

trial2029.add_stimulus(event2029)
trial2029.set_factor("trueDate", 2029)

trial2032.add_stimulus(event2032)
trial2032.set_factor("trueDate", 2032)

trial2035.add_stimulus(event2035)
trial2035.set_factor("trueDate", 2035)

trial2038.add_stimulus(event2038)
trial2038.set_factor("trueDate", 2038)

trial2041.add_stimulus(event2041)
trial2041.set_factor("trueDate", 2041)

trial2044.add_stimulus(event2044)
trial2044.set_factor("trueDate", 2044)

trial2050.add_stimulus(event2050)
trial2050.set_factor("trueDate", 2050)

trial2053.add_stimulus(event2053)
trial2053.set_factor("trueDate", 2053)

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
block_questionnaire.add_trial(trial2019)
block_questionnaire.add_trial(trial2020)
block_questionnaire.add_trial(trial2023)
block_questionnaire.add_trial(trial2026)
block_questionnaire.add_trial(trial2029)
block_questionnaire.add_trial(trial2032)
block_questionnaire.add_trial(trial2035)
block_questionnaire.add_trial(trial2038)
block_questionnaire.add_trial(trial2041)
block_questionnaire.add_trial(trial2044)
block_questionnaire.add_trial(trial2050)
block_questionnaire.add_trial(trial2053)

#Create other needed stimuli and trials
errorDate = expyriment.stimuli.TextLine(text = "Entrer une date", text_size = 40)
errorDate.preload()

errorTrust = expyriment.stimuli.TextLine(text = "Entrer un nombre", text_size = 40)
errorTrust.preload()

#Let's put a fixation cross
fixcross = expyriment.stimuli.FixCross()
fixcross.preload()


#Start experiment
expyriment.control.start()

for trial in block_questionnaire.trials:
    fixcross.present()
    questionnaire.clock.wait(500)
    trial.stimuli[0].present()
    questionnaire.clock.wait(2000)

#Here put answer (check if valid input)
    questionDate = expyriment.io.TextInput(message = "date?", length = 4,
     message_text_size = 40, user_text_size = 40)
    try:
        answerDate = int(questionDate.get())
    except ValueError:
        errorDate.present()
        questionDate = expyriment.io.TextInput(message = "date?", length = 4,
         message_text_size = 40, user_text_size = 40)

    if answerDate == trial.get_factor("trueDate"):
        goodAnswer = True
    else:
        goodAnswer = False

    questionTrust = expyriment.io.TextInput(message = "confiance?", length = 1,
     message_text_size = 40, user_text_size = 40)
    try:
        answerTrust = int(questionTrust.get())
    except ValueError:
        errorTrust.present()
        questionTrust = expyriment.io.TextInput(message = "confiance?", length = 1,
         message_text_size = 40, user_text_size = 40)

    if answerTrust < 3:
        goodAnswer = False

    questionnaire.data.add([expyriment.design.Block.name, expyriment.design.Trial.id, goodAnswer]) #Add data
    questionnaire.clock.wait(500) #Wait before going to the next event


expyriment.control.end()


#Answer

#Feedback?
#Must put answer in data in a way that can be read by exp
#So we can exclude wrong answers