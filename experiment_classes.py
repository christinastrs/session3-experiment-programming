from psychopy import core, visual, event 

class Experiment: 
    def __init__(self, window_size, text_color, background_color):
        self.text_color = text_color
        self.window = visual.Window(window_size, color = background_color)
        self.fixation = visual.TextStim(self.window, '+', color = text_color)
        self.clock = core.Clock()

    def show_fixation(self, time = 0.5): #if you don't specify time, it takes this time value by default 
        self.fixation.draw()
        self.window.flip()
        core.wait(time)

class Item:
    def __init__(self, experiment, name, image_path):
        self.experiment = experiment
        self.name = name 
        self.text = visual.TextStim(experiment.window, text = name, color = experiment.text_color) 
        self.image = visual.ImageStim(experiment.window, image = image_path)



class Trial: 
    def __init__(self, experiment, name, stimulus, fixation_time = 0.5, max_key_wait = 5, keys= ['z', 'm'])
        self.name = name
        self.experiment = experiment 
        self.stimulus = stimulus 
        self.fixation_time = fixation_time #copy paste from teun's code -- this is unfinished 


def run(self):  #copy paste teun's code -- unfinished 

        