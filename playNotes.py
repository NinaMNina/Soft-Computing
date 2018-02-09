from midiutil.MidiFile import *
import pygame
import makeSound as ms
import mainFrame
import recognize
import os
from nn_setup_duration import CNNDuraiton
from nn_setup import CNNValue
import ctypes  # An included library with Python install.

class PlayNotes():
    def __init__(self):
        ops = ['violinski kljuc', 'c4', 'h3', 'c4', 'd4', 'e4', 'd4', 'c4', 'c4', 'h3', 'c4', 'd4', 'e4', 'c4', 'h3', 'c4', 'd4', 'violinski kljuc', 'e4', 'd4', 'c4', 'd4', 'c4', 'd4', 'e4', 'f4', 'f4', 'e4', 'd4', 'c4', 'h3', 'c4', 'violinski kljuc', 'e4', 'd4', 'e4', 'f4', 'e4', 'd4', 'c4', 'g4']
        resized = ['violinski kljuc', 'f4', 'f4', 'g4', 'g4', 'g4', 'a4', 'c5', 'c5', 'a4', 'a4', 'g4', 'g4', 'g4', 'a4', 'f4', 'd4', 'violinski kljuc', 'f4', 'f4', 'g4', 'g4', 'g4', 'a4', 'c5', 'c5', 'd5', 'c5', 'a4', 'g4', 'f4', 'pauza']

        path = mainFrame.MainFrame.path
        recognize.cropNotes(path)
        print ('notes cropped')

        notenames = []
        degrees = []
        duration = []
        loc = os.getcwd()
        loc += '/images/notes'
        print(loc)
        t = 16
        fileList = os.listdir(loc)
        duzina = len(fileList)

        for a in range(duzina):
            path0 = loc +'/nota' + str(a) + '.png'
            note_name = CNNValue.checkNote(path0)
            notenames.append(note_name)
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
            elif note_name=='h4':
                degrees.append(71)
            elif note_name=='pauze':
                degrees.append(1)
            else:
                degrees.append(0)

            if(note_name == "taktica" or note_name == "violinski kljuc"):
                note_duration = '0'
            else:
                note_duration = CNNDuraiton.checkLength(path0)

            if note_duration=="n1-1" or note_duration=="p1-1":
                duration.append(t)
            elif note_duration=="n1-2" or note_duration=="p1-2":
                duration.append(t/2)
            elif note_duration=="n1-4" or note_duration=="p1-4":
                duration.append(t/4)
            elif note_duration=="n1-8" or note_duration=="p1-8":
                duration.append(t/8)
            elif note_duration=="n1-16" or note_duration=="p1-16":
                duration.append(t/16)
            else:
                duration.append(0)
            print (note_name + ' ' + note_duration)
        print ('prepoznate note pre izbacivanja taktica:')
        print (notenames)
        print ("len pre izbacivanja taktica: " + str(len(notenames)))
        for note in notenames:
            if(note == "taktica"):
                notenames.remove(note)
        print("len posle izbacivanja taktica: " + str(len(notenames)))
        notesLen = len(notenames)
        check = 0

        if(os.path.basename(path) == 'ops.jpg'):
           for i in range(notesLen):
               if(notenames[i] == ops[i]):
                   check += 1
        elif(os.path.basename(path) == 'resized.png'):
           for i in range(notesLen):
               if(notenames[i] == resized[i]):
                   check += 1
        print ('pogodjenih ' + str(check) + 'od ' + str(notesLen) )
        ctypes.windll.user32.MessageBoxW(0, "Pogodjeno nota: " + str(round(check/notesLen*100, 2)) + "%", "Rezultat", 0)
        print (notenames)



        track = 0
        channel = 0
        time = 0
        tempo = 120
        duration1 = 4
        volume = 100
        MyMIDI = MIDIFile(1)
        MyMIDI.addTempo(track, time, tempo)
        length = len(degrees)
        for i in range(length):
            if(degrees[i]!=0 and degrees[i]!=1):
                MyMIDI.addNote(track, channel, degrees[i], time, duration[i], volume)
                time = time + 1
            if(degrees[i]==1):
                time=time+duration[i]
        with open("melody.mid", "wb") as output_file:
            MyMIDI.writeFile(output_file)

        midi_file = 'melody.mid'
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