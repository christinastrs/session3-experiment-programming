from psychopy import core, visual, event, sound
import os
# from pydub import AudioSegment, silence, effects
from pydub import AudioSegment
from pydub.playback import play

class Experiment:
    def __init__(self, window_size, text_color, background_color):
        self.text_color = text_color
        self.window = visual.Window(window_size, color=background_color)
        self.fixation = visual.TextStim(self.window, '+', color=text_color)
        self.clock = core.Clock()
    
    def show_fixation(self, time=0.5):
        self.fixation.draw()
        self.window.flip()
        core.wait(time)

class AudioItem:
    def __init__(self, experiment, id, condition, freq_category, word, subtlex_log10freq):
        self.experiment = experiment
        self.id = id
        self.condition = condition
        self.freq_category = freq_category
        self.word = word
        self.subtlex_log10freq = subtlex_log10freq
        # root_path = Path('sounds')
        # self.filepath = Path(root_path / freq_category.upper() / word).with_suffix('.wav')
        filepath = os.path.join('sounds', freq_category, f'{word}.wav')
        self.audio = sound.Sound(sound.AudioClip.load(filepath))
        # self.audio = AudioSegment.from_wav(filepath)


        # self.text = visual.TextStim(experiment.window, text=name, color=experiment.text_color)
        # self.image = visual.ImageStim(experiment.window, image=image_path)

class Trial:
    def __init__(self, experiment, name, stimulus, fixation_time=0.5, max_key_wait=5, keys=['y', 'n']):
        self.name = name 
        self.experiment = experiment
        self.stimulus = stimulus  
        self.fixation_time = fixation_time
        self.max_key_wait = max_key_wait
        self.keys = keys
    
    def run(self):
        self.experiment.show_fixation(self.fixation_time)
        self.stimulus.audio.play()
        # play(self.stimulus.audio)
        self.experiment.window.flip()
        core.wait(0.5)  # Wait for 2 seconds

        # self.item.image.draw()
        # self.experiment.window.flip()
        # core.wait(0.5)  # Wait for 2 seconds

        
        start_time = self.experiment.clock.getTime()
        keys = event.waitKeys(maxWait=self.max_key_wait, keyList=self.keys, timeStamped=self.experiment.clock, clearEvents=True)
        if keys is not None:
            key, end_time = keys[0]
        else:
            key = None
            end_time = self.experiment.clock.getTime()
        
        return {
            'trial': self.name,
            'start_time': start_time,
            'end_time': end_time,
            'key': key,
            'freq_category': self.stimulus.freq_category,
            'condition':self.stimulus.condition
        }



# from email.mime import audio
# from psychopy import core, visual, event

# class Experiment:
#     def __init__(self, window_size, text_color, background_color):
#         self.text_color = text_color
#         self.window = visual.Window(window_size, color=background_color)
#         self.fixation = visual.TextStim(self.window, '+', color=text_color)
#         self.clock = core.Clock()
    
#     def show_fixation(self, time=0.5):
#         self.fixation.draw()
#         self.window.flip()
#         core.wait(time)

# class Item:
#     def __init__(self, experiment, name, sound_path): 
#         self.experiment = experiment
#         self.name = name
#         # self.text = visual.TextStim(experiment.window, text=name, color=experiment.text_color)
#         self.audio = audio.SoundStim(experiment.window, audio=sound_path)

# class Trial:
#     def __init__(self, experiment, name, stimulus, condition, freq_category, fixation_time=0.5, max_key_wait=5, keys=['y', 'n']):
#         self.name = name
#         self.experiment = experiment
#         self.stimulus = stimulus
#         self.fixation_time = fixation_time
#         self.max_key_wait = max_key_wait
#         self.keys = keys
#         self.condition = condition
#         self.freq_category = freq_category
    
#     def run(self):
#         self.experiment.show_fixation(self.fixation_time)

#         self.stimulus.play() #changed for audio
#         self.experiment.window.flip()
        
#         start_time = self.experiment.clock.getTime()
#         keys = event.waitKeys(maxWait=self.max_key_wait, keyList=self.keys, timeStamped=self.experiment.clock, clearEvents=True)
#         if keys is not None:
#             key, end_time = keys[0]
#         else:
#             key = None
#             end_time = self.experiment.clock.getTime()
        
#         return {
#             'trial': self.name,
#             'start_time': start_time,
#             'end_time': end_time,
#             'key': key,
#             # 'condition': condition, 
#             # 'freq_category': freq_category
#         }

