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
from nn_setup_value import CNNDuraiton

class MainFrame():
    path = ""
    def __init__(self):
        print ('init main frame - app.py')
        cwd = os.getcwd()
        self.root = tk.Tk()

        self.root.title('TNotes - Music Note Recognition')
        self.root.geometry("700x500")

        self.root.iconbitmap(cwd+'/images/icon.ico')

        labelF = LabelFrame( self.root, text='Based on Convolution Neural Network')
        labelF.pack(fill="both", expand="yes")

        labelEmpty = Label(labelF, text="")
        labelEmpty.grid(row=0, column=0)

        label2 = Label(labelF, text="Start to train CNN")
        label2.grid(row=1, column=0)

        button1 = Button(labelF, text="start", command=self.callNN)
        button1.grid(row=1, column=1)

        labelEmpty = Label(labelF, text="")
        labelEmpty.grid(row=2, column=0)

        label1 = Label(labelF, text="Add notes to process")
        label1.grid(row=3, column=0)

        self.entry = Entry(labelF, width=50)
        self.entry.grid(row=3, column=1)

        button2 = Button(labelF, text="Search", command=self.addNotes)
        button2.grid(row=3, column=2)

        labelEmpty = Label(labelF, text="")
        labelEmpty.grid(row=4, column=0)

        button3 = Button(labelF, text="Make melody and play", command=self.processAndPerform)
        button3.grid(row=5, column=1)

        labelEmpty = Label(labelF, text="")
        labelEmpty.grid(row=6, column=0)

        imgCanvas = Canvas(labelF, width=500, height=200)
        imgCanvas.grid(row=7, column=0, columnspan=4, rowspan=5)
        path = cwd+'/images/cover.gif'
        img = PhotoImage(file=path)
        imgCanvas.create_image(0, 0, image=img, anchor="nw" )

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
        self.top = Toplevel(self.root)
        self.top.title("Convolution Neural Network is in training...")
        cwd = os.getcwd()
        self.top.iconbitmap(cwd + '/images/icon.ico')
        self.canvas = Canvas(self.top, width=400, height=400)
        self.top.protocol("WM_DELETE_WINDOW", self.disable_event)
        self.canvas.pack()
        self.alien1 = self.canvas.create_oval(20, 260, 120, 360, outline='white', fill='blue')
        self.alien2 = self.canvas.create_oval(2, 2, 40, 40, outline='white', fill='red')
        self.alien3 = self.canvas.create_oval(20, 20, 80, 80, outline='white', fill='white')
        self.alien4 = self.canvas.create_oval(50, 130, 220, 300, outline='white', fill='purple')
        self.alien5 = self.canvas.create_oval(25, 150, 100, 100, outline='white', fill='yellow')
        self.alien6 = self.canvas.create_oval(20, 320, 120, 390, outline='white', fill='green')
        self.canvas.pack()
        self.param = True
        self.top._job = self.top.after(0, self.animation)

    def addNotes(self):
        print('it wants to add some notes')
        name = askopenfilename(initialdir="D:/", filetypes=(("JPEG File", "*.jpg"), ("PNG File", "*.png")),
                               title="Choose an Image")
        print(name)
        # Using try in case user types in unknown file or closes without choosing a file.
        try:
            img = cv2.imread(name)
            self.entry.delete(0, END)  # deletes the current value
            self.entry.insert(0, name)
            MainFrame.path = name
        except:
            print("No image exists")

    def processAndPerform(self):
        if MainFrame.path=="":
            return
        melody = PlayNotes()
        print("making a melody")

    def neuralDuration(self):
        # cnnd = CNNDuraiton.__init__()
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


        # self.param = False
        # self.top.after_cancel(self.top._job)
        # self.threads.__delitem__(1)
        # self.param = False
        # self.top.after_cancel(self.top._job)
        # self.threads.__delitem__(0)
        # self.top.destroy()

    def disable_event(self):
        pass
    def animation(self):
        track = 0
        while self.param:
            x = 5
            y = 0
            if track == 0:
                for i in range(0, 51):
                    time.sleep(0.025)
                    self.canvas.move(self.alien1, x, y)
                    self.canvas.move(self.alien2, x, y)
                    self.canvas.move(self.alien3, x, y)
                    self.canvas.move(self.alien4, x, y)
                    self.canvas.move(self.alien5, x, y)
                    self.canvas.move(self.alien6, x, y)
                    self.canvas.update()
                track = 1

            else:
                for i in range(0, 51):
                    time.sleep(0.025)
                    self.canvas.move(self.alien1, -x, y)
                    self.canvas.move(self.alien2, -x, y)
                    self.canvas.move(self.alien3, -x, y)
                    self.canvas.move(self.alien4, -x, y)
                    self.canvas.move(self.alien5, -x, y)
                    self.canvas.move(self.alien6, -x, y)
                    self.canvas.update()
                track = 0