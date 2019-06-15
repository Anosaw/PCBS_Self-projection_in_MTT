# PCBS: Self-projection in Mental Time Travel
Anna Wagelmans: Project for PCBS

This project is an experiment of self-projection in mental time travel, where participants are asked to project themselves in different points in time. While projected in time, participants must make a temporal judgment task: events are presented to the participants and they must judge whether it has already passed, or is yet to pass.

The experimental design follows the one presented in [Gauthier & van Wassenhove 2016](https://www.ncbi.nlm.nih.gov/pubmed/27239750), but focuses on the time modality. In this article, it was shown that reaction times were higher when the participant was projected in time  compared to when they were in the present. This project builds on this finding and aims to further explore mental time travel in humans.  

---  


### Table of contents  
* [Experimental design](# Experimental_design)
* [Predictions](# Predictions)
* [Before the experiment](# Before_the_experiment)
* [Questionnaire](# Questionnaire)
* [Mental time travel experiment](# Mental_time_travel_experiment)
* [After the experiment](# After_the_expriment)
* [Conclusion](# Conclusion)

---

### Experimental design  

##### Projection points  
The participant must first project themselves to the point in time shown on the screen.

The seven possible projections are:

* 3, 6, 9 years in the past
* 3, 6, 9 years in the future
* Present


##### Temporal judgment task  
The events then appear on screen and the participant must indicate, using the keyboard arrows, whether the event has already passed or has yet to pass (in relation to the time of projection).  

All the events are shown to the participant in a random order before starting the next block.

One run of the experiment (7 projection blocks) lasts around 15 minutes. Therefore, the participants could run the experiment 3 or 4 times each.


---

### Predictions

We know that reaction times (and error rates) are higher in the projection condition than in the present. The question we aim to answer with this experiment is: **does the *distance* of projection have a parametric effect on reaction times (and error rates) ?**  

If it does, then we would expect reaction times (and error rates) to be significantly higher the farther the projection is. Thus, the conditions *9 years in the past* and *9 years in the future* should show the highest reaction times (and error rates), followed by *3 years*, then *6 years*, then *present*.  

If no effect of the distance is found, then further research has to be done on whether self-projection in mental time travel is independant from distance or not.


---

### Before the experiment

A few days before the experiment, a [list of events](https://github.com/Anosaw/PCBS_Self-projection_in_MTT/blob/master/documents/event_list.csv) is given to the participant with the [instruction]() to learn it thoroughly.

The list of events was given in a randomized order to each participant, using the script [randomize_events.py](https://github.com/Anosaw/PCBS_Self-projection_in_MTT/blob/master/scripts/randomize_events.py):

```python

import random
import csv

nb_events = 24

l = {}
i = 1

with open('documents/event_list.csv', encoding="utf-8") as events:
    r = csv.reader(events)
    next(r)  # skip header line
    for row in r:
        date, name = row[0], row[3]
        l.update({i : date + " : " + name})
        i += 1

nb = list(range(1 , nb_events + 1))
random.shuffle(nb)

for element in nb:
    print(l[element])

```

There are 24 events in total, 12 in the past and 12 in the future. Among these events, 5 of the past events and 5 of the future events are fictional. 

The fictional events are not related to the main experimental question. They have been included in the list in order to see if there was an effect of the event themselves, and in particular of the degree of reality attributed to the event. Since half of the events given to the participants are future events, and thus fictional to some degree, such an analysis was necessary to disringuish effect of the temporality of the event and effects of its degree of reality.

---

### Questionnaire

The script for the questionnaire can be found in [questionnaire.py](https://github.com/Anosaw/PCBS_Self-projection_in_MTT/blob/master/scripts/Questionnaire.py).

The experiment starts by a questionnaire, where participants are asked to retrieve the date of each event. The participant needs to have a good knowledge of the events in order to perform the rest of the experiment correctly. if the score of the participant is not satisfactory (cutoff was put at 70% of good answers), then the participant cannot continue the experiment.

Here are the details of the script:  

```python

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
```

The events are imported from the [event list](https://github.com/Anosaw/PCBS_Self-projection_in_MTT/blob/master/documents/event_list.csv).


```python

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
error_date = expyriment.stimuli.TextLine(text = "Entrer une date", text_size = text_size, text_colour = white)
error_date.preload()

error_trust = expyriment.stimuli.TextLine(text = "Entrer un nombre entier entre 0 et 5", text_size = text_size, text_colour = white)
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
         message_text_size = text_size, message_colour = white, user_text_size = text_size, user_text_colour = white)
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
         message_text_size = text_size, message_colour = white, user_text_size = text_size, user_text_colour = white)
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
   
```

The score of the participant is presented on the screen

```python

#Present score at the end
score = nb_good_answer / nb_events * 100
score = int(score)
expyriment.stimuli.TextLine(text = "le taux de bonne réponse est de " + str(score) + "%", text_size = text_size, text_colour = white).present()
questionnaire.keyboard.wait(keys = expyriment.misc.constants.K_RETURN)


expyriment.control.end()

```

---

### Mental time travel experiment

After a [tutorial](https://github.com/Anosaw/PCBS_Self-projection_in_MTT/blob/master/scripts/Tutorial.py), the participant can perform the [Mental Time Travel experiment](https://github.com/Anosaw/PCBS_Self-projection_in_MTT/blob/master/scripts/MTTexp.py).

---

### After the expriment


---

### Conclusion
This was originally the script for my M1 internship. I modified it in order to implement what I did not have the time to during my internship. I made the code cleaner and easier to read.
