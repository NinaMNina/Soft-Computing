import cv2
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import os
import time
from playNotes import PlayNotes


def __init__():

    def callNN():
        print ('call trainning of NN')
        d = MyDialog(frame)

    def addNotes():
        print ('it wants to add some notes')
        name = askopenfilename(initialdir="D:/", filetypes=(("JPEG File", "*.jpg"), ("PNG File", "*.png")),
                               title="Choose an Image")
        print (name)
        # Using try in case user types in unknown file or closes without choosing a file.
        try:
            img = cv2.imread(name)
            entry.delete(0, END)  # deletes the current value
            entry.insert(0, name)
        except:
            print("No image exists")

    def processAndPerform():
        melody = PlayNotes.__init__()
        print ("make a melody")

    print ('init main frame - app.py')
    cwd = os.getcwd()
    frame = tk.Tk()

    frame.title('TNotes - Music Note Recognition')
    frame.geometry("500x400")

    frame.iconbitmap(cwd+'/images/icon.ico')

    labelF = LabelFrame( frame, text='Based on Convolution Neural Network')
    labelF.pack(fill="both", expand="yes")

    labelEmpty = Label(labelF, text="")
    labelEmpty.grid(row=0, column=0)

    label2 = Label(labelF, text="Start to train CNN")
    label2.grid(row=1, column=0)

    button1 = Button(labelF, text="start", command=callNN)
    button1.grid(row=1, column=1)

    labelEmpty = Label(labelF, text="")
    labelEmpty.grid(row=2, column=0)

    label1 = Label(labelF, text="Add notes to process")
    label1.grid(row=3, column=0)

    entry = Entry(labelF, width=50)
    entry.grid(row=3, column=1)

    button2 = Button(labelF, text="Search", command=addNotes)
    button2.grid(row=3, column=2)

    labelEmpty = Label(labelF, text="")
    labelEmpty.grid(row=4, column=0)

    button3 = Button(labelF, text="Make melody and play", command=processAndPerform)
    button3.grid(row=5, column=1)

    labelEmpty = Label(labelF, text="")
    labelEmpty.grid(row=6, column=0)

    imgCanvas = Canvas(labelF, width=500, height=200)
    imgCanvas.grid(row=7, column=0, columnspan=4, rowspan=5)
    path = cwd+'/images/cover.gif'
    img = PhotoImage(file=path)
    imgCanvas.create_image(0, 0, image=img, anchor="nw" )


    mainloop()

class MyDialog:

    def __init__(self, parent):
        self.a = alien()
    def ok(self):

        print ("training is canceled"), self.e.get()

        self.top.destroy()


class alien(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("Convolution Neural Network is in training...")
        cwd = os.getcwd()
        self.root.iconbitmap(cwd + '/images/icon.ico')
        self.canvas = Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.alien1 = self.canvas.create_oval(20, 260, 120, 360, outline='white', fill='blue')
        self.alien2 = self.canvas.create_oval(2, 2, 40, 40, outline='white', fill='red')
        self.alien3 = self.canvas.create_oval(20, 20, 80, 80, outline='white', fill='white')
        self.alien4 = self.canvas.create_oval(50, 130, 220, 300, outline='white', fill='purple')
        self.alien5 = self.canvas.create_oval(25, 150, 100, 100, outline='white', fill='yellow')
        self.alien6 = self.canvas.create_oval(20, 320, 120, 390, outline='white', fill='green')
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()

    def animation(self):
        track = 0
        while True:
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

