"""
This is the code for the Mental Time Travel experiment

First, we must present the point of projection
Then, we must present the events
The participants will be instructed to make a temporal judgment based on these events
To do so, they will press randomized left and right arrow keys
"""

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
