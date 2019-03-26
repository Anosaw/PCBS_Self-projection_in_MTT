#This is the code for the Mental Time Travel experiment

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



#Add stimuli to trials and trials to block
trial1985.add_stimulus(event1985)
trial1988.add_stimulus(event1988)
trial1991.add_stimulus(event1991)
trial1994.add_stimulus(event1994)
trial1997.add_stimulus(event1997)
trial2000.add_stimulus(event2000)
trial2003.add_stimulus(event2003)
trial2006.add_stimulus(event2006)
trial2009.add_stimulus(event2009)
trial2012.add_stimulus(event2012)
trial2015.add_stimulus(event2015)
trial2018.add_stimulus(event2018)
trial2019.add_stimulus(event2019)
trial2020.add_stimulus(event2020)
trial2023.add_stimulus(event2023)
trial2026.add_stimulus(event2026)
trial2029.add_stimulus(event2029)
trial2032.add_stimulus(event2032)
trial2035.add_stimulus(event2035)
trial2038.add_stimulus(event2038)
trial2041.add_stimulus(event2041)
trial2044.add_stimulus(event2044)
trial2050.add_stimulus(event2050)
trial2053.add_stimulus(event2053)

block_3past.add_trial(trial2012)
block_3past.add_trial(trial2012)
block_3past.add_trial(trial2041)

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
