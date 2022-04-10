from psychopy import visual,sound, core

window = visual.Window(size = (400, 400))
message = visual.TextStim(window)
note_c = sound.Sound('C', secs = 1.0)
note_g = sound.Sound('G', secs = 1.0)
grating = visual.GratingStim(window, tex = 'sin', mask = 'gauss', sf = 10, name = 'gabor')
image = visual.ImageStim(window, image = 'images/baby.png')
audio = sound.Sound('sounds/HF/auto.wav')


message.text = "Hello"
message.draw() #draw the message but not on the screen, but on a screen buffer 
window.flip() 
note_c.play()
core.wait(2.0) #to make sure that the program doesn't close right away

message.text = "World"
message.draw() #draw the message but not on the screen, but on a screen buffer 
window.flip() 
note_g.play()
core.wait(2.0) #t

grating.draw()
window.flip() 
core.wait(2.0) 

image.draw()
window.flip() 
audio.play()
core.wait(2.0) 