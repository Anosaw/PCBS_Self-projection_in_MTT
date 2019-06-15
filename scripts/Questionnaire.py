"""
This is the questionnaire the participants should fill out before the exp
We are presenting the events to the participants
They must enter the date, followed by a trust indicator (from 0 to 5)
"""

import expyriment
import csv

#Create and initialize exp
questionnaire = expyriment.design.Experiment(name = "Questionnaire")
expyriment.control.initialize(questionnaire)

#Define variables
nb_good_answer = 0
nb_events = 24

good_answer = True
all_is_good = False

text_size = 60
white = (255, 255, 255)

#Design block
block_questionnaire = expyriment.design.Block(name = "Questionnaire block")

#Design trials
with open('documents/event_list.csv', encoding="utf-8") as events:
    r = csv.reader(events)
    next(r)  # skip header line
    for row in r:
        date, fictional, name = row[0], row[2], row[3]
        trial = expyriment.design.Trial()
        trial.add_stimulus(expyriment.stimuli.TextLine(text = name, text_size = text_size, text_colour = white))
        trial.set_factor("Date", date)
        trial.set_factor("Fictional", fictional)
        block_questionnaire.append(trial)

#Shuffle trials
block_questionnaire.shuffle_trials()

#Create other needed stimuli and trials
error_date = expyriment.stimuli.TextLine(text = "Entrer une date",
 text_size = text_size, text_colour = white)
error_date.preload()

error_trust = expyriment.stimuli.TextLine(text = "Entrer un nombre entier entre 0 et 5",
 text_size = text_size, text_colour = white)
error_trust.preload()

#Fixation cross
fixcross = expyriment.stimuli.FixCross(size = (50, 50), line_width = 4, colour = white)
fixcross.preload()

#Set experimental data variables names
questionnaire.add_data_variable_names(["date", "fictional", "good_answer", "answer_date", "answer_trust"])

#Start experiment
expyriment.control.start()

fixcross.present()
questionnaire.clock.wait(1000)

for trial in block_questionnaire.trials:

    #Present event, participant must enter the date
    #Because there is a participant input, the input must be checked
    while all_is_good == False:
        question_date = expyriment.io.TextInput(message = trial.stimuli[0].text, length = 4,
         message_text_size = text_size, message_colour = white,
         user_text_size = text_size, user_text_colour = white)
        try:
            answer_date = int(question_date.get())
            all_is_good = True
        except ValueError:
            error_date.present()
            questionnaire.keyboard.wait(keys = expyriment.misc.constants.K_RETURN)

    #Check if answer is right
    if answer_date == trial.get_factor("Date"):
        good_answer = True
    else:
        good_answer = False

    #Reset variable
    all_is_good = False

    #Present question, participant must how confident they are in their answer
    #From 0 to 5
    while all_is_good == False:
        questionTrust = expyriment.io.TextInput(message = "confiance?", length = 1,
         message_text_size = text_size, message_colour = white,
         user_text_size = text_size, user_text_colour = white)
        try:
            answer_trust = int(questionTrust.get())
            if 0 <= answer_trust <= 5:
                all_is_good = True
            else:
                all_is_good = False
                error_trust.present()
                questionnaire.keyboard.wait(keys = expyriment.misc.constants.K_RETURN)
        except ValueError:
            error_trust.present()
            questionnaire.keyboard.wait(keys = expyriment.misc.constants.K_RETURN)

    #If trust is too low, the answer is considered false
    if answer_trust < 3:
        good_answer = False

    #Count the number of good answers
    if good_answer == True:
        nb_good_answer += 1

    all_is_good = False

    #Add data
    questionnaire.data.add([trial.get_factor("Date"), trial.get_factor("Fictional"), good_answer, answer_date, answer_trust])

    fixcross.present()
    random_ITI = expyriment.design.randomize.rand_norm(750, 1250) #Randomize ITI
    questionnaire.clock.wait(random_ITI) #Wait before next trial

#Present score at the end
score = nb_good_answer / nb_events * 100
score = int(score)
expyriment.stimuli.TextLine(text = "le taux de bonne réponse est de " + str(score) + "%",
 text_size = text_size, text_colour = white).present()
questionnaire.keyboard.wait(keys = expyriment.misc.constants.K_RETURN)


expyriment.control.end()
