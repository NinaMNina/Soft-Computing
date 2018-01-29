import cv2
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
import os


def __init__():

    def callNN():
        print ('call trainning of NN')

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

