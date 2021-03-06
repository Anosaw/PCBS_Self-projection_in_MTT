"""
This is the tutorial for this experiment
"""

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
        block_tuto.add_trial(trial)

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
expyriment.stimuli.TextLine(text = str(abs(projection)) + " ans dans le futur",
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
    date = int(trial.get_factor("Date"))

    if date < (present + projection):
        if pressed_key == past_key:
            good_answer = True
        else:
            good_answer = False
    if date > (present + projection):
        if pressed_key == future_key:
            good_answer = True
        else:
            good_answer = False

    #Calculate distance between event and projection
    event_to_projection_distance = date -  (present + projection)

    #Add data
    tuto.data.add([projection, date, trial.get_factor("Fictional"),
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
