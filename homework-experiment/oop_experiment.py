# # This is a compact version of the oop_experiment script.
# # It uses some techniques that we have not covered in this course!
# # If you don't understand what's going on, use the oop_experiment.py script instead ;)

# from experiment_classes import Experiment, Item, Trial
# import pandas as pd
# import numpy as np

# experiment = Experiment((800, 600), (-1, -1, -1), (1, 1, 1))

# stimuli = pd.read_csv('lexical_decision_stimuli.csv')
# items = [Item(experiment, stimulus['item'], stimulus['image_file']) for index, stimulus in stimuli.iterrows()]
# image_trials = [Trial(experiment, f'{item.name}_image', item.image) for item in items]
# text_trials = [Trial(experiment, f'{item.name}_text', item.text) for item in items]

# trials = np.random.permutation(image_trials + text_trials)
# results = [trial.run() for trial in trials]

# results = pd.DataFrame(results)
# results['reaction_time'] = results['end_time'] - results['start_time']
# results.to_csv('demo_output.csv')


from my_experiment_classes import Experiment, Trial, AudioItem
import pandas as pd
import numpy as np

experiment = Experiment((800, 600), (-1, -1, -1), (1, 1, 1))
experiment.show_fixation(2)

stimuli = pd.read_csv('lexical_decision_stimuli.csv') #create a list with audioitems
items = []
for index, stimulus in stimuli.iterrows():
    items.append(AudioItem(experiment=experiment, id=stimulus['stim_id'], condition=stimulus['condition'], freq_category=stimulus['freq_category'], word=stimulus['word'], subtlex_log10freq=stimulus['subtlex_log10freq']))

    
trials = []
for item in items:
    trials.append(Trial(experiment=experiment, name=item.word, stimulus=item))   

for idx in range(4):
    trials = np.random.permutation(trials)

    results = []
    for trial in trials[:20]:
        results.append(trial.run())

    results = pd.DataFrame(results)
    results['reaction_time'] = results['end_time'] - results['start_time']
    results.to_csv(f'small_experiment_participant_{idx}.csv')

# results.plot.hist(column=['reaction_time'])