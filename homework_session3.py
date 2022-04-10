# These are some homework exercises to practice working 
#  with pandas and psychopy.

## Exercise A
# 1. Load pandas and psychopy
# 2. Load the picture verification simuli file
#    (look up the .read_csv method of pandas)
# 3. Loop over the item names, and print them on the screen
#    (you can loop over a single column just like a list!)
# 4. Now, change your code to show a text stimulus with each item name,
#     with a 1 second pause in between, instead of using print().
# 5. Loop over the item paths, and use them to create image stimuli;
#     display each image for 1 second.

from psychopy import visual,sound, core
import pandas as pd
import time
import os
from PIL import Image 
import random
random.seed(42)

df = pd.read_csv("picture_verification_stimuli.csv")

for item in df['item']: 
    print(item) 
# df['item']

window = visual.Window(size = (400, 400))
message = visual.TextStim(window)

for item in df['item']:  
    message.text = item
    message.draw() #draw the message but not on the screen, but on a screen buffer 
    window.flip() 
    core.wait(1.0)


window = visual.Window(size = (400, 400))
message = visual.TextStim(window)

for file in df['image_file']:
    image = visual.ImageStim(window, file)
    image.draw()
    window.flip()
    core.wait(1.0)

## Exercise B
# 1. Load the lexical decision stimuli file 
# 2. Select all the high frequency words (HF)
#    (you can do this using masks, just like how we selected a single row)
# 3. Loop over the words, and create a sound stimulus for each
#    (you can specify the relative path as f'sounds/HF/{sound_name}.wav')
# 4. Play the sounds one-by-one, making sure there is some time between them

ld_df = pd.read_csv("lexical_decision_stimuli.csv")
ld_df_hf_only = ld_df[ld_df['freq_category']=='HF']


ld_df_hf_only
for sound_file in ld_df_hf_only['word']:
    audio = sound.Sound(f'sounds/HF/{sound_file}.wav')
    audio.play()
    core.wait(2.0) 


## Bonus exercise
# 1. Try to load in the image and/or sound stimuli first, 
#     before showing/playing them. You can use a list, and the .append()
#     method, to build a list of stimuli, and then use another for loop
#     to show/play them one by one.
# 2. Before showing/playing, try to randomise the order of stimuli; 
#     Google how to randomise the order of a list!
loaded_hf_audio_list = []
for sound_file in ld_df_hf_only['word']:
    loaded_hf_audio_list.append(sound.Sound(f'sounds/HF/{sound_file}.wav'))


random.shuffle(loaded_hf_audio_list)

for audiofile in loaded_hf_audio_list:
    audiofile.play()
    core.wait(2.0) 