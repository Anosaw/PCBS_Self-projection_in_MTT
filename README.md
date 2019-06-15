# PCBS: Self-projection in Mental Time Travel
#### Anna Wagelmans: Project for PCBS

This project is an experiment of self-projection in mental time travel, where participants are asked to project themselves in different points in time. While projected in time, participants must make a temporal judgment task: events are presented to the participants and they must judge whether it has already passed, or is yet to pass.

The experimental design follows the one presented in [Gauthier & van Wassenhove 2016](https://www.ncbi.nlm.nih.gov/pubmed/27239750), but focuses on the time modality. In this article, it was shown that reaction times were higher when the participant was projected in time  compared to when they were in the present. This project builds on this finding and aims to further explore mental time travel in humans.  

---  


### Table of contents  
* [Experimental design](#experimental-design)
* [Predictions](#predictions)
* [Before the experiment](#before-the-experiment)
* [Questionnaire](#questionnaire)
* [Mental time travel experiment](#mental-time-travel-experiment)
* [After the experiment](#after-the-experiment)
* [Conclusion](#conclusion)

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

   
```

The score of the participant is presented on the screen

```python

#Present score at the end
score = nb_good_answer / nb_events * 100
score = int(score)
expyriment.stimuli.TextLine(text = "le taux de bonne réponse est de " + str(score) + "%",
 text_size = text_size, text_colour = white).present()
questionnaire.keyboard.wait(keys = expyriment.misc.constants.K_RETURN)


expyriment.control.end()

```

---

### Mental time travel experiment

After a [tutorial](https://github.com/Anosaw/PCBS_Self-projection_in_MTT/blob/master/scripts/Tutorial.py), the participant can perform the [Mental Time Travel experiment](https://github.com/Anosaw/PCBS_Self-projection_in_MTT/blob/master/scripts/MTTexp.py).

In order to run, the scripts need an image of the arrows ('avant' and 'après') to show on the screen. These images have been generated by this [script](https://github.com/Anosaw/PCBS_Self-projection_in_MTT/blob/master/scripts/arrows.py):

```python

import pygame
import sys

pygame.init()

#define variables for the screen
width = 1150
height = 300

#open a window
screen = pygame.display.set_mode((width, height))

#name the colors for convenience
white = (255,255,255)
black = (0,0,0)

#fill the screen with black
screen.fill(black)

#define variables for the arrows
arrow_length = width / 5 #length of the arrow
distance_to_border = arrow_length / 3 #distance between head of the arrow and edge of the screen
inter_arrow_distance = width - 2*arrow_length - 2*distance_to_border #distance between the tails of the arrows
arrow_span = height / 6 #width of the arrows
arrow_head = arrow_span / 2 #length of the head of the arrows
arrow_height = 2*height / 3 #height of the arrows on the screen

#draw words
font_size = 50
font = pygame.font.Font(None, font_size)

before = font.render("avant", True, white)
screen.blit(before, (distance_to_border + arrow_length / 2, height / 3))

x, y = font.size("après") #This is needed to center properly the second word

after = font.render("après", True, white)
screen.blit(after, (distance_to_border + inter_arrow_distance + 3*arrow_length / 2 - x, height / 3))

#draw arrows
#left arrow
pygame.draw.lines(screen, white, False, [(distance_to_border, arrow_height),
 (distance_to_border + arrow_length, arrow_height)], 5)
pygame.draw.lines(screen, white, False, [(distance_to_border, arrow_height),
 (distance_to_border + arrow_head, arrow_height + arrow_span / 2)], 5)
pygame.draw.lines(screen, white, False, [(distance_to_border, arrow_height),
 (distance_to_border + arrow_head, arrow_height - arrow_span / 2)], 5)

#right arrow
pygame.draw.lines(screen, white, False,
 [(distance_to_border + 2*arrow_length + inter_arrow_distance, arrow_height),
 (distance_to_border + arrow_length + inter_arrow_distance, arrow_height)], 5)
pygame.draw.lines(screen, white, False,
 [(distance_to_border + 2*arrow_length + inter_arrow_distance, arrow_height),
 (distance_to_border + 2*arrow_length + inter_arrow_distance - arrow_head, arrow_height + arrow_span / 2)], 5)
pygame.draw.lines(screen, white, False,
 [(distance_to_border + 2*arrow_length + inter_arrow_distance, arrow_height),
 (distance_to_border + 2*arrow_length + inter_arrow_distance - arrow_head, arrow_height - arrow_span / 2)], 5)

#display changes
pygame.display.update()

#save image
pygame.image.save(screen, "documents/before_is_left_arrows.png")

#______draw second image______

screen.fill(black)

#draw words on second image
before = font.render("après", True, white)
screen.blit(before, (distance_to_border + arrow_length / 2, height / 3))

x, y = font.size("avant") #This is needed to center properly the second word

after = font.render("avant", True, white)
screen.blit(after, (distance_to_border + inter_arrow_distance + 3*arrow_length / 2 - x, height / 3))

#draw arrows
#left arrow
pygame.draw.lines(screen, white, False, [(distance_to_border, arrow_height),
 (distance_to_border + arrow_length, arrow_height)], 5)
pygame.draw.lines(screen, white, False, [(distance_to_border, arrow_height),
 (distance_to_border + arrow_head, arrow_height + arrow_span / 2)], 5)
pygame.draw.lines(screen, white, False, [(distance_to_border, arrow_height),
 (distance_to_border + arrow_head, arrow_height - arrow_span / 2)], 5)

#right arrow
pygame.draw.lines(screen, white, False,
 [(distance_to_border + 2*arrow_length + inter_arrow_distance, arrow_height),
 (distance_to_border + arrow_length + inter_arrow_distance, arrow_height)], 5)
pygame.draw.lines(screen, white, False,
 [(distance_to_border + 2*arrow_length + inter_arrow_distance, arrow_height),
 (distance_to_border + 2*arrow_length + inter_arrow_distance - arrow_head, arrow_height + arrow_span / 2)], 5)
pygame.draw.lines(screen, white, False,
 [(distance_to_border + 2*arrow_length + inter_arrow_distance, arrow_height),
 (distance_to_border + 2*arrow_length + inter_arrow_distance - arrow_head, arrow_height - arrow_span / 2)], 5)

#display changes
pygame.display.update()

#save image
pygame.image.save(screen, "documents/before_is_right_arrows.png")


# wait till the window is closed
done = False
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

```

The images generated can be found in the documents folder:   

[arrows where 'before' is on the left](https://github.com/Anosaw/PCBS_Self-projection_in_MTT/blob/master/documents/before_is_left_arrows.png)  
[arrows where 'before' is one the right](https://github.com/Anosaw/PCBS_Self-projection_in_MTT/blob/master/documents/before_is_right_arrows.png)



We can now run the script for the tutorial:

```python


import expyriment
import csv

#Create and initialize exp
tuto = expyriment.design.Experiment(name = "Tutorial")
expyriment.control.initialize(tuto)

good_answer = True
text_size = 60
present = 2019

white = (255, 255, 255)

#______Define blocks, trials and stimuli______

#Design block
block_tuto = expyriment.design.Block(name = "tuto block")

#Import events
with open('documents/event_list.csv', encoding="utf-8") as events:
    r = csv.reader(events)
    next(r)  # skip header line
    for row in r:
        date, fictional, name = row[0], row[2], row[3]
        trial = expyriment.design.Trial()
        trial.add_stimulus(expyriment.stimuli.TextLine(text = name, text_size = text_size, text_colour = white))
        trial.set_factor("Date", date)
        trial.set_factor("Fictional", fictional)
        block_tuto.append(trial)

#Add block to exp
tuto.add_block(block_tuto)

#Shuffle trials
block_tuto.shuffle_trials()

#_______Create other needed stimuli and trials_______

#Fixation cross
fixcross = expyriment.stimuli.FixCross(size = (50, 50), line_width = 4, colour = white)
fixcross.preload()

#Create the picture with the arrows
before_is_left_arrows = expyriment.stimuli.Picture("documents/before_is_left_arrows.png")
before_is_right_arrows = expyriment.stimuli.Picture("documents/before_is_right_arrows.png")


#Set experimental data variable names
tuto.add_data_variable_names(["projection", "date", "fictional",
 "event_to_projection_distance", "before_is_left", "pressed_key", "good_answer", "RT"])

#________Start exp_________
expyriment.control.start()

#Randomize keys
before_is_left = expyriment.design.randomize.coin_flip()
if before_is_left == True:
    past_key = expyriment.misc.constants.K_LEFT
    future_key = expyriment.misc.constants.K_RIGHT
else:
    past_key = expyriment.misc.constants.K_RIGHT
    future_key = expyriment.misc.constants.K_LEFT

response_keys = [past_key, future_key]

fixcross.present() #Present fixation cross
tuto.clock.wait(1000)

#Present key instructions
if before_is_left == True:
    before_is_left_arrows.present()
else:
    before_is_right_arrows.present()

tuto.keyboard.wait(keys = expyriment.misc.constants.K_RETURN) #Wait until participant presses enter

fixcross.present()
tuto.clock.wait(1000)

#Present projection
projection_list = [-9, -6, -3, +3, +6, +9]
projection = expyriment.design.randomize.rand_element(projection_list)
expyriment.stimuli.TextLine(text = projection + " ans dans le futur",
 text_size = text_size, text_colour = white).present()

tuto.keyboard.wait(keys = expyriment.misc.constants.K_RETURN) #Wait until participant presses enter

fixcross.present()
tuto.clock.wait(1000)

for trial in block_tuto.trials[0:5] :

    #Plot stimuli on image with arrows and present it
    if before_is_left == True :
        trial.stimuli[0].plot(before_is_left_arrows)
        before_is_left_arrows.present()
    else:
        trial.stimuli[0].plot(before_is_right_arrows)
        before_is_right_arrows.present()

    #Measure reaction time
    pressed_key, RT = tuto.keyboard.wait(keys = response_keys)

    #Store whether the participant gave the good answer or not
    if trial.get_factor("Date") < (present + projection):
        if pressed_key == past_key:
            good_answer = True
        else:
            good_answer = False
    if trial.get_factor("Date") > (present + projection):
        if pressed_key == future_key:
            good_answer = True
        else:
            good_answer = False

    #Calculate distance between event and projection
    event_to_projection_distance = trial.get_factor("Date") -  (present + projection)

    #Add data
    tuto.data.add([projection, trial.get_factor("Date"), trial.get_factor("Fictional"),
     event_to_projection_distance, before_is_left, pressed_key, good_answer, RT]) #Add data

    #Clear images
    if before_is_left == True:
        before_is_left_arrows.clear_surface()
    else:
        before_is_right_arrows.clear_surface()
    fixcross.present()



    #randomize ITI
    random_ITI = expyriment.design.randomize.rand_norm(750, 1250)
    tuto.clock.wait(random_ITI)


expyriment.control.end()

```

After making sure the participant understands everything, we can run the Mental Time Travel experiment:

```python

import expyriment
import csv

#Create and initialize exp
MTTexp = expyriment.design.Experiment(name = "MTT Experiment")
expyriment.control.initialize(MTTexp)

#Define variables
good_answer = True

present = 2019

text_size = 60
white = (255, 255, 255)


#_________Define blocks, trials and stimuli__________

#Design blocks
block_9past = expyriment.design.Block(name = "9 years past block")
block_6past = expyriment.design.Block(name = "6 years past block")
block_3past = expyriment.design.Block(name = "3 years past block")
block_now = expyriment.design.Block(name = "present block")
block_3future = expyriment.design.Block(name = "3 years future block")
block_6future = expyriment.design.Block(name = "6 years future block")
block_9future = expyriment.design.Block(name = "9 years future block")

#Add projection point as factor
block_9past.set_factor("projection", -9)
block_6past.set_factor("projection", -6)
block_3past.set_factor("projection", -3)
block_now.set_factor("projection", 0)
block_3future.set_factor("projection", 3)
block_6future.set_factor("projection", 6)
block_9future.set_factor("projection", 9)

#Add block to exp
MTTexp.add_block(block_9past)
MTTexp.add_block(block_6past)
MTTexp.add_block(block_3past)
MTTexp.add_block(block_now)
MTTexp.add_block(block_3future)
MTTexp.add_block(block_6future)
MTTexp.add_block(block_9future)

#Import events
with open('documents/event_list.csv', encoding="utf-8") as events:
    r = csv.reader(events)
    next(r)  # skip header line
    for block in MTTexp:
        for row in r:
            date, fictional, name = row[0], row[2], row[3]
            trial = expyriment.design.Trial()
            trial.add_stimulus(expyriment.stimuli.TextLine(text = name, text_size = text_size, text_colour = white))
            trial.set_factor("Date", date)
            trial.set_factor("Fictional", fictional)
            block.append(trial)


#Randomize trial order
for block in MTTexp.blocks:
    block.shuffle_trials()

#Randomize block order
MTTexp.shuffle_blocks()


#________Create other needed stimuli and trials______

#Fixation cross
fixcross = expyriment.stimuli.FixCross(size = (50, 50), line_width = 4)
fixcross.preload()

#Create the picture with the arrows
before_is_left_arrows = expyriment.stimuli.Picture("documents/before_is_left_arrows.png")
before_is_right_arrows = expyriment.stimuli.Picture("documents/before_is_right_arrows.png")


#Set experimental data variable names
MTTexp.add_data_variable_names(["projection", "date", "fictional",
 "event_to_projection_distance", "before_is_left", "pressed_key", "good_answer", "RT"])

#________Start exp__________

expyriment.control.start()

for block in MTTexp.blocks :

    #Randomize keys
    before_is_left = expyriment.design.randomize.coin_flip()
    if before_is_left == True:
        past_key = expyriment.misc.constants.K_LEFT
        future_key = expyriment.misc.constants.K_RIGHT
    else:
        past_key = expyriment.misc.constants.K_RIGHT
        future_key = expyriment.misc.constants.K_LEFT

    response_keys = [past_key, future_key]

    fixcross.present() #Present fixation cross
    MTTexp.clock.wait(1000)

    #Present key instructions
    if before_is_left == True:
        before_is_left_arrows.present()
    else:
        before_is_right_arrows.present()

    MTTexp.keyboard.wait(keys = expyriment.misc.constants.K_RETURN) #Wait until participant presses enter

    fixcross.present() #Present fixation cross
    MTTexp.clock.wait(1000)

    #Present projection according to block
    projection = int(block.get_factor("projection"))
    expyriment.stimuli.TextLine(text = projection + " ans dans le futur",
     text_size = text_size, text_colour = white).present()

    MTTexp.keyboard.wait(keys = expyriment.misc.constants.K_RETURN)

    fixcross.present()
    MTTexp.clock.wait(1000)

    for trial in block.trials :

            #Plot the stimulus on the image of the arrows and present both
            if before_is_left == True :
                trial.stimuli[0].plot(before_is_left_arrows)
                before_is_left_arrows.present()
            else:
                trial.stimuli[0].plot(before_is_right_arrows)
                before_is_right_arrows.present()

            #Measure reaction time
            pressed_key, RT = MTTexp.keyboard.wait(keys = response_keys)

            #Store whether the participant gave the good answer or not
            if trial.get_factor("Date") < (present + projection):
                if pressed_key == past_key:
                    good_answer = True
                elif pressed_key == future_key:
                    good_answer = False

            elif trial.get_factor("Date") > (present + projection):
                if pressed_key == future_key:
                    good_answer = True
                elif pressed_key == past_key:
                    good_answer = False

            #Calculate the distance between event and projection
            event_to_projection_distance = trial.get_factor("Date") - (present + projection)

            #Add data to the datafile
            MTTexp.data.add([projection, trial.get_factor("Date"), trial.get_factor("Fictional"),
             event_to_projection_distance, before_is_left, pressed_key, good_answer, RT])

            #Clear images
            if before_is_left == True:
                before_is_left_arrows.clear_surface()
            else:
                before_is_right_arrows.clear_surface()

            fixcross.present()

            #randomize ITI
            random_ITI = expyriment.design.randomize.rand_norm(750, 1250)
            MTTexp.clock.wait(random_ITI)

    #Present pause screen at the end of the block
    expyriment.stimuli.TextLine(text = "pause (entrée pour continuer)",
     text_size = text_size, text_colour = white).present()
    MTTexp.keyboard.wait(keys = expyriment.misc.constants.K_RETURN)

expyriment.control.end()

```

---

### After the experiment



---

### Conclusion
This was originally the script for my M1 internship. I modified it in order to implement what I did not have the time to during my internship. I made the code cleaner and easier to read.
