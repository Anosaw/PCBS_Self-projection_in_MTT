#This is the code for the Mental Time Travel experiment

#First, we must present the point of projection (here, 3 years in the past)
#Then, we must present the events
#The participants will be instructed to make a temporal judgment based on these events
#This means they will be told to press left if event is past and right if future
#Only RT matter in the data (not the actual judgment)

import expyriment

#Create and initialize exp
MTTexp = expyriment.design.Experiment(name = "MTT Experiment")
expyriment.control.initialize(MTTexp)


#Define blocks, trials and stimuli
#There is 1 trial per stimulus

#Design block
block_9past = expyriment.design.Block(name = "9 years past block")
block_6past = expyriment.design.Block(name = "6 years past block")
block_3past = expyriment.design.Block(name = "3 years past block")
block_now = expyriment.design.Block(name = "present block")
block_3future = expyriment.design.Block(name = "3 years future block")
block_6future = expyriment.design.Block(name = "6 years future block")
block_9future = expyriment.design.Block(name = "9 years future block")

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

#Add events to trials
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

#Create other needed stimuli and trials

#Let's put a fixation cross
fixcross = expyriment.stimuli.FixCross()
fixcross.preload()

#Instructions
#Projection instructions
stim_proj9past = expyriment.stimuli.TextLine(text = "9 ans dans le passé", text_size = 40)
stim_proj9past.preload()

stim_proj6past = expyriment.stimuli.TextLine(text = "6 ans dans le passé", text_size = 40)
stim_proj6past.preload()

stim_proj3past = expyriment.stimuli.TextLine(text = "3 ans dans le passé", text_size = 40)
stim_proj3past.preload()

stim_projnow = expyriment.stimuli.TextLine(text = "présent", text_size = 40)
stim_projnow.preload()

stim_proj3future = expyriment.stimuli.TextLine(text = "3 ans dans le futur", text_size = 40)
stim_proj3future.preload()

stim_proj6future = expyriment.stimuli.TextLine(text = "6 ans dans le futur", text_size = 40)
stim_proj6future.preload()

stim_proj9future = expyriment.stimuli.TextLine(text = "9 ans dans le futur", text_size = 40)
stim_proj9future.preload()

#Several solutions to have the projection stimuli appear first
#Either add it first to the block, then add all other trials with random_position = bool(1)
#Or add it last (after shuffling trials), then swap position with the first one
#Or add it last and simply refer to the last trial in the block to call it
#Note that with the two last ones, you must know the exact number of trials in the block
#Which may change if some are to be excluded!

#Key instructions
stim_pastKey = expyriment.stimuli.TextLine(text = "Entrer la touche pour le passé", text_size = 40)
stim_pastKey.preload()

stim_futureKey = expyriment.stimuli.TextLine(text = "Entrer la touche pour le futur", text_size = 40)
stim_futureKey.present()

#Question
question = expyriment.stimuli.TextLine(text = "avant ou après?", text_size = 40)
question.preload()


#Add trials to blocks

block_9past.add_trial(trial1985)
block_9past.add_trial(trial1988)
block_9past.add_trial(trial1991)
block_9past.add_trial(trial1994)
block_9past.add_trial(trial1997)
block_9past.add_trial(trial2000)
block_9past.add_trial(trial2003)
block_9past.add_trial(trial2006)
block_9past.add_trial(trial2009)
block_9past.add_trial(trial2012)
block_9past.add_trial(trial2015)
block_9past.add_trial(trial2018)
block_9past.add_trial(trial2019)
block_9past.add_trial(trial2020)
block_9past.add_trial(trial2023)
block_9past.add_trial(trial2026)
block_9past.add_trial(trial2029)
block_9past.add_trial(trial2032)
block_9past.add_trial(trial2035)
block_9past.add_trial(trial2038)
block_9past.add_trial(trial2041)
block_9past.add_trial(trial2044)
block_9past.add_trial(trial2050)
block_9past.add_trial(trial2053)

block_6past.add_trial(trial1985)
block_6past.add_trial(trial1988)
block_6past.add_trial(trial1991)
block_6past.add_trial(trial1994)
block_6past.add_trial(trial1997)
block_6past.add_trial(trial2000)
block_6past.add_trial(trial2003)
block_6past.add_trial(trial2006)
block_6past.add_trial(trial2009)
block_6past.add_trial(trial2012)
block_6past.add_trial(trial2015)
block_6past.add_trial(trial2018)
block_6past.add_trial(trial2019)
block_6past.add_trial(trial2020)
block_6past.add_trial(trial2023)
block_6past.add_trial(trial2026)
block_6past.add_trial(trial2029)
block_6past.add_trial(trial2032)
block_6past.add_trial(trial2035)
block_6past.add_trial(trial2038)
block_6past.add_trial(trial2041)
block_6past.add_trial(trial2044)
block_6past.add_trial(trial2050)
block_6past.add_trial(trial2053)

block_3past.add_trial(trial1985)
block_3past.add_trial(trial1988)
block_3past.add_trial(trial1991)
block_3past.add_trial(trial1994)
block_3past.add_trial(trial1997)
block_3past.add_trial(trial2000)
block_3past.add_trial(trial2003)
block_3past.add_trial(trial2006)
block_3past.add_trial(trial2009)
block_3past.add_trial(trial2012)
block_3past.add_trial(trial2015)
block_3past.add_trial(trial2018)
block_3past.add_trial(trial2019)
block_3past.add_trial(trial2020)
block_3past.add_trial(trial2023)
block_3past.add_trial(trial2026)
block_3past.add_trial(trial2029)
block_3past.add_trial(trial2032)
block_3past.add_trial(trial2035)
block_3past.add_trial(trial2038)
block_3past.add_trial(trial2041)
block_3past.add_trial(trial2044)
block_3past.add_trial(trial2050)
block_3past.add_trial(trial2053)

block_now.add_trial(trial1985)
block_now.add_trial(trial1988)
block_now.add_trial(trial1994)
block_now.add_trial(trial1997)
block_now.add_trial(trial2000)
block_now.add_trial(trial2003)
block_now.add_trial(trial2006)
block_now.add_trial(trial2009)
block_now.add_trial(trial2012)
block_now.add_trial(trial2015)
block_now.add_trial(trial2018)
block_now.add_trial(trial2019)
block_now.add_trial(trial2020)
block_now.add_trial(trial2023)
block_now.add_trial(trial2026)
block_now.add_trial(trial2029)
block_now.add_trial(trial2032)
block_now.add_trial(trial2035)
block_now.add_trial(trial2038)
block_now.add_trial(trial2041)
block_now.add_trial(trial2044)
block_now.add_trial(trial2050)
block_now.add_trial(trial2053)

block_3future.add_trial(trial1985)
block_3future.add_trial(trial1988)
block_3future.add_trial(trial1991)
block_3future.add_trial(trial1994)
block_3future.add_trial(trial1997)
block_3future.add_trial(trial2000)
block_3future.add_trial(trial2003)
block_3future.add_trial(trial2006)
block_3future.add_trial(trial2009)
block_3future.add_trial(trial2012)
block_3future.add_trial(trial2015)
block_3future.add_trial(trial2018)
block_3future.add_trial(trial2019)
block_3future.add_trial(trial2020)
block_3future.add_trial(trial2023)
block_3future.add_trial(trial2026)
block_3future.add_trial(trial2029)
block_3future.add_trial(trial2032)
block_3future.add_trial(trial2035)
block_3future.add_trial(trial2038)
block_3future.add_trial(trial2041)
block_3future.add_trial(trial2044)
block_3future.add_trial(trial2050)
block_3future.add_trial(trial2053)

block_6future.add_trial(trial1985)
block_6future.add_trial(trial1988)
block_6future.add_trial(trial1991)
block_6future.add_trial(trial1994)
block_6future.add_trial(trial1997)
block_6future.add_trial(trial2000)
block_6future.add_trial(trial2003)
block_6future.add_trial(trial2006)
block_6future.add_trial(trial2009)
block_6future.add_trial(trial2012)
block_6future.add_trial(trial2015)
block_6future.add_trial(trial2018)
block_6future.add_trial(trial2019)
block_6future.add_trial(trial2020)
block_6future.add_trial(trial2023)
block_6future.add_trial(trial2026)
block_6future.add_trial(trial2029)
block_6future.add_trial(trial2032)
block_6future.add_trial(trial2035)
block_6future.add_trial(trial2038)
block_6future.add_trial(trial2041)
block_6future.add_trial(trial2044)
block_6future.add_trial(trial2050)
block_6future.add_trial(trial2053)

block_9future.add_trial(trial1985)
block_9future.add_trial(trial1988)
block_9future.add_trial(trial1991)
block_9future.add_trial(trial1994)
block_9future.add_trial(trial1997)
block_9future.add_trial(trial2000)
block_9future.add_trial(trial2003)
block_9future.add_trial(trial2006)
block_9future.add_trial(trial2009)
block_9future.add_trial(trial2012)
block_9future.add_trial(trial2015)
block_9future.add_trial(trial2018)
block_9future.add_trial(trial2019)
block_9future.add_trial(trial2020)
block_9future.add_trial(trial2023)
block_9future.add_trial(trial2026)
block_9future.add_trial(trial2029)
block_9future.add_trial(trial2032)
block_9future.add_trial(trial2035)
block_9future.add_trial(trial2038)
block_9future.add_trial(trial2041)
block_9future.add_trial(trial2044)
block_9future.add_trial(trial2050)
block_9future.add_trial(trial2053)


#Add block to exp
MTTexp.add_block(block_9past)
MTTexp.add_block(block_6past)
MTTexp.add_block(block_3past)
MTTexp.add_block(block_now)
MTTexp.add_block(block_3future)
MTTexp.add_block(block_6future)
MTTexp.add_block(block_9future)

#Randomize trial order
for blocks in MTTexp.blocks:
    expyriment.design.Block.shuffle_trials(self = blocks)

#Randomize block order
expyriment.design.Experiment.shuffle_blocks(self = MTTexp)

#There are actually at least two ways to randomize trial/block position
#Either shuffle after adding them
#Or, when adding them, use argument random_position = bool(1)
#The second one means less lines, but how random is it?



#Start exp
expyriment.control.start()

#Ask participant to define keys
stim_pastKey.present()
MTTexp.clock.wait(1000)
pastKey = MTTexp.Keyboard.wait_char()
stim_futureKey.present()
MTTexp.clock.wait(1000)
futureKey = MTTexp.keyboard.wait_char()
response_keys = [pastKey, futureKey]


for blocks in MTTexp.blocks :
    fixcross.present() #Present fixation cross
    MTTexp.clock.wait(500)
    if str(expyriment.design.Block.name) == "9 years past block":
        stim_proj9past.present()
    elif str(expyriment.design.Block.name) == "6 years past block" :
        stim_proj6past.present()
    elif str(expyriment.design.Block.name) == "3 years past block" :
        stim_proj3past.present()
    elif str(expyriment.design.Block.name) == "present block" :
        stim_projnow.present()
    elif str(expyriment.design.Block.name) == "3 years future block" :
        stim_proj3future.present()
    elif str(expyriment.design.Block.name) == "6 years future block" :
        stim_proj6future.present()
    elif str(expyriment.design.Block.name) == "9 years future block" :
        stim_proj9future.present()
    else:
        expyriment.stimuli.TextLine(text = "ERROR = Projection not recognized", text_size = 40).present()


    MTTexp.clock.wait(2000)
    for trial in blocks.trials :
            trial.stimuli[0].present() #Present event
            MTTexp.clock.wait(1000)
            question.present() #Present question
            key, rt = MTTexp.keyboard.wait(keys = response_keys, duration = 3000) #Mesure RT
            MTTexp.data.add([expyriment.design.Block.name, expyriment.design.Trial.id, key, rt]) #Add data
            MTTexp.clock.wait(500) #Wait before going to the next event


expyriment.control.end()

#Note: to do this experiment properly
#We should weed out beforehand the events the participant does not remember
#For this we will need to code a questionnaire

#We need to mesure errors too!
#Must put the answer in the trial somehow
#Key inputs must be predefined (left for past, right for future)
#Or input from user?
#input pastKey and futureKey
#wait_char, with found as key input?
