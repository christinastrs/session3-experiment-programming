from experiment_classes import Experiment, Item
import pandas as pd


experiment = Experiment((800,600), (-1,-1,-1), (1,1,1))

experiment.show_fixation(2)

stimuli = pd.read_csv("picture_verification_stimuli.csv")
items = []
for index, stimulus in stimuli.iterrows(): 
    items.append(Item(experiment, stimulus['item'], stimulus['image_file']))

print(items)
