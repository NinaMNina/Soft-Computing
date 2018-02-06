import cv2
import numpy as np
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import os
import time
import threading
from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from playNotes import PlayNotes
from nn_setup import CNNValue
from nn_setup_duration import CNNDuraiton
from PIL import ImageTk, Image
from midiutil.MidiFile import *
import pygame
import makeSound as ms

class MainFrame():
    path = ""
    def __init__(self):
        print ('init main frame - mainFrame.py')

        cwd = os.getcwd()
        self.root = tk.Tk()
        screen_width = int(self.root.winfo_screenwidth() * 0.6)
        screen_height = int(self.root.winfo_screenheight() *0.9)

        self.root.title('TNotes - Music Note Recognition')
        self.root.geometry(str(screen_width)+"x"+str(screen_height))

        self.root.iconbitmap(cwd+'/images/icon.ico')

        self.labelF = LabelFrame( self.root, text='Based on Convolution Neural Network')
        self.labelF.pack(fill="both", expand="yes")

        labelEmpty = Label(self.labelF, text="")
        labelEmpty.grid(row=0, column=0)

        label2 = Label(self.labelF, text="Start to train CNN")
        label2.grid(row=1, column=0)

        button1 = Button(self.labelF, text="start", command=self.callNN)
        button1.grid(row=1, column=1)

        labelEmpty = Label(self.labelF, text="")
        labelEmpty.grid(row=2, column=0)

        label1 = Label(self.labelF, text="Add notes to process")
        label1.grid(row=3, column=0)

        self.entry = Entry(self.labelF, width=50)
        self.entry.grid(row=3, column=1)

        button2 = Button(self.labelF, text="Search", command=self.addNotes)
        button2.grid(row=3, column=2)

        labelEmpty = Label(self.labelF, text="")
        labelEmpty.grid(row=4, column=0)

        button3 = Button(self.labelF, text="Make melody and play", command=self.processAndPerform)
        button3.grid(row=5, column=1)


        button4 = Button(self.labelF, text="Replay last one made", command=self.replayMelody)
        button4.grid(row=5, column=2)

        labelEmpty = Label(self.labelF, text="")
        labelEmpty.grid(row=6, column=0)


        self.imgCanvas = Canvas(self.labelF, width=screen_width, height=70)
        self.imgCanvas.grid(row=7, column=0, columnspan=3)


        path = cwd+'/images/cover.gif'
        img = PhotoImage(file=path)
        self.labelImg = Label(self.labelF, image=img)
        self.labelImg.grid(row=8, column=0, columnspan=3, rowspan=3)


        mainloop()

    def callNN(self):
        print('call trainning of NN')
        self.threads = []
        t2 = threading.Thread(target=self.appDialog)
        self.threads.append(t2)
        t2.start()

        t1 = threading.Thread(target=self.neuralDuration)
        self.threads.append(t1)
        t1.start()

    def appDialog(self):
        self.alien1 = self.imgCanvas.create_oval(10, 10, 60, 60, outline='white', fill='green')
        # self.imgCanvas.pack()
        self._job = self.root.after(0, self.animation)

    def addNotes(self):
        print('it wants to add some notes')
        name = askopenfilename(initialdir="D:/", filetypes=(("JPEG File", "*.jpg"), ("PNG File", "*.png"), ("GIF File", "*.gif")),
                               title="Choose an Image")
        print(name)
        # Using try in case user types in unknown file or closes without choosing a file.
        screen_width = int(self.root.winfo_screenwidth() * 0.6)
        screen_height = int(self.root.winfo_screenheight() * 0.9)
        try:
            img = cv2.imread(name)
            self.entry.delete(0, END)  # deletes the current value
            self.entry.insert(0, name)
            MainFrame.path = name
            img  = PhotoImage(file=name)
            self.labelImg.configure(image=img)
            self.labelImg.image = img

        except:
            try:
                img = ImageTk.PhotoImage(Image.open(name).resize((screen_width, int(screen_height*0.7))))
                self.labelImg.configure(image=img)
                self.labelImg.image = img
            except:
                print("No image exists")

    def processAndPerform(self):
        if MainFrame.path=="":
            return
        print("making a melody")
        # img = cv2.imread(MainFrame.path)
        # cv2.imshow('notes', img)
        melody = PlayNotes()

    def replayMelody(self):
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

    def neuralDuration(self):
        cnnd = CNNDuraiton.__init__()
        # CNNDuraiton.checkLength('images/predict/1-2.png')
        # print('---should be n1-2---')
        # CNNDuraiton.checkLength('images/predict/1-16.png')
        # print('---should be n1-16---')
        # CNNDuraiton.checkLength('images/predict/a3.jpg')
        # print('---should be n1-2---')
        # CNNDuraiton.checkLength('images/predict/a4_test.png')
        # print('---should be n1-8---')
        # CNNDuraiton.checkLength('images/predict/cela_pauza.png')
        # print('---should be p1-1---')
        # CNNDuraiton.checkLength('images/predict/cetvrtina_pauze.png')
        # print('---should be p1-4---')
        # CNNDuraiton.checkLength('images/predict/d4.png')
        # print('---should be n1-4---')
        # CNNDuraiton.checkLength('images/predict/len1-4.png')
        # print('---should be n1-4---')
        # CNNDuraiton.checkLength('images/predict/osmina_pauze.png')
        # print('---should be p1-8---')
        # CNNDuraiton.checkLength('images/predict/pause1-2.png')
        # print('---should be p1-2---')
        # CNNDuraiton.checkLength('images/predict/pause1-4.png')
        # print('---should be p1-4---')
        # CNNDuraiton.checkLength('images/predict/pola_pauze.png')
        # print('---should be p1-2---')
        cnnv = CNNValue.__init__()
        #CNNValue.checkNote('images/predict/1-2.png')

        self.threads.__delitem__(1)
        self.imgCanvas.after_cancel(self._job)
        self.threads.__delitem__(0)

    def disable_event(self):
        pass
    def animation(self):
        track = 0
        while True:
            x = 5
            y = 0
            screen_width = int(self.root.winfo_screenwidth() * 0.11)
            if track == 0:
                for i in range(0, screen_width):
                    time.sleep(0.025)
                    self.imgCanvas.move(self.alien1, x, y)
                    self.imgCanvas.update()
                track = 1

            else:
                for i in range(0, screen_width):
                    time.sleep(0.025)
                    self.imgCanvas.move(self.alien1, -x, y)
                    self.imgCanvas.update()
                track = 0