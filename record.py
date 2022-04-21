import sounddevice as sd
import numpy as np


fs = 44100
duration = 5  # seconds
print('Recording 5 seconds of audio')
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)

sd.wait()
print('Recording complete')

print('Playing Audio')
sd.play(myrecording, fs)
