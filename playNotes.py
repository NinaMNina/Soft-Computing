from midiutil.MidiFile import *
import pygame
import makeSound as ms
import app
import recognize
import os
from nn_setup_value import CNNDuraiton
from nn_setup import CNNValue

class PlayNotes():
    def __init__(self):
        path = app.MainFrame.path
        recognize.cropNotes(path)

        degrees = []
        duration = []
        loc = os.getcwd()
        loc += '/images/notes'
        print(loc)
        t = 16
        fileList = os.listdir(loc)
        for fileName in fileList:
            path0 = loc+'/'+fileName
            note_name = CNNValue.checkNote(path0)
            if note_name!="taktica" or note_name!="violinski kljuc":
                if note_name=='a3':
                    degrees.append(57)
                elif note_name=='a4':
                    degrees.append(69)
                elif note_name=='c4':
                    degrees.append(60)
                elif note_name=='c5':
                    degrees.append(72)
                elif note_name=='d4':
                    degrees.append(62)
                elif note_name=='d5':
                    degrees.append(74)
                elif note_name=='e4':
                    degrees.append(64)
                elif note_name=='e5':
                    degrees.append(76)
                elif note_name=='f4':
                    degrees.append(65)
                elif note_name=='f5':
                    degrees.append(77)
                elif note_name=='g4':
                    degrees.append(67)
                elif note_name=='g5':
                    degrees.append(79)
                elif note_name=='h3':
                    degrees.append(59)
                else:
                    degrees.append(71)

                note_duration = CNNDuraiton.checkLength(path0)

                if note_duration=="n1-1" or note_duration=="p1-1":
                    duration.append(t)
                elif note_duration=="n1-2" or note_duration=="p1-2":
                    duration.append(t/2)
                elif note_duration=="n1-4" or note_duration=="p1-4":
                    duration.append(t/4)
                elif note_duration=="n1-8" or note_duration=="p1-8":
                    duration.append(t/8)
                else:
                    duration.append(t/16)

        track = 0
        channel = 0
        time = 0
        duration = 4
        tempo = 120
        volume = 15
        MyMIDI = MIDIFile(1)
        MyMIDI.addTempo(track, time, tempo)
        length = len(degrees)
        for i in length:
            MyMIDI.addNote(track, channel, degrees[i], time, duration, volume)
            time = time + duration[i]
            volume = volume + 15
        with open("major-scale.mid", "wb") as output_file:
            MyMIDI.writeFile(output_file)

        midi_file = 'major-scale.mid'
        freq = 44100  # audio CD quality
        bitsize = -16  # unsigned 16 bit
        channels = 2  # 1 is mono, 2 is stereo
        buffer = 1024  # number of samples
        pygame.mixer.init(freq, bitsize, channels, buffer)

        # optional volume 0 to 1.0
        pygame.mixer.music.set_volume(1.0)
        try:
            ms.play_music(midi_file)
        except KeyboardInterrupt:
            # if user hits Ctrl/C then exit
            # (works only in console mode)
            pygame.mixer.music.fadeout(1000)
            pygame.mixer.music.stop()
            raise SystemExit
