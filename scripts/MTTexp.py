#First, we must present the point of projection (here, 3 years in the past)
#Then, we must present the events
#The participants will be instructed to make a temporal judgment based on these events
#This means they will be told to press left if event is past and right if future
#Only RT matter in the data (not the actual judgment)

import expyriment

#Create and initialize exp
exp_MTT = expyriment.design.Experiment(name = "MTT Experiment")
expyriment.control.initialize(exp_MTT)

#Define left and right arrow keys for responses
response_keys = [expyriment.misc.constants.K_LEFT, expyriment.misc.constants.K_RIGHT]


#Define blocks, trials and stimuli
#There is 1 trial per stimulus

#Design block
block_3past = expyriment.design.Block(name = "3 years past block")

#Design trials
trial1 = expyriment.design.Trial()
trial2 = expyriment.design.Trial()

#Create stimuli and preload them
event1 = expyriment.stimuli.TextLine(text = "Curiosity sur Mars", text_size = 40)
event1.preload()

event2 = expyriment.stimuli.TextLine(text = "tunnel sous Bering", text_size = 40)
event2.preload()

#Add stimuli to trials and trials to block
trial1.add_stimulus(event1)
trial2.add_stimulus(event2)

block_3past.add_trial(trial1)
block_3past.add_trial(trial2)

#Randomize trial order
expyriment.design.Block.shuffle_trials(self = block_3past)

#Add block to exp
exp_MTT.add_block(block_3past)


#Create other needed stimuli

#Let's put a fixation cross
fixcross = expyriment.stimuli.FixCross()
fixcross.preload()

#Instructions
proj_3past = expyriment.stimuli.TextLine(text = "3 ans dans le passé", text_size = 40)
proj_3past.preload()

question = expyriment.stimuli.TextLine(text = "avant ou après?", text_size = 40)
question.preload()


#Start exp
expyriment.control.start()

for blocks in exp_MTT.blocks :
    fixcross.present() #Present fixation cross
    exp_MTT.clock.wait(500)
    proj_3past.present() #Present instruction point of projection
    exp_MTT.clock.wait(2000)
    for trial in block_3past.trials :
            trial.stimuli[0].present() #Present event
            exp_MTT.clock.wait(1000)
            question.present() #Present question
            key, rt = exp_MTT.keyboard.wait(keys = response_keys) #Mesure RT
            exp_MTT.data.add([block_3past.name, trial.id, key, rt]) #Add data
            exp_MTT.clock.wait(500) #Wait before going to the next event


expyriment.control.end()

#Note: to do this experiment properly
#We should weed out beforehand the events the participant does not remember
#For this we will need to code a questionnaire
