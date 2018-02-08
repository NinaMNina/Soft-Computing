import os
import cv2

loc = os.getcwd()
loc += '/toBitwise'
print(loc)
fileList = os.listdir(loc)
i = 0
for fileName in fileList:
    loc = os.getcwd()
    loc += '/toBitwise'
    name = '/nota'
    name += str(i)
    name += '.png'
    loc += name
    img = cv2.imread(loc, 0)
    img = cv2.bitwise_not(img)
    cv2.imwrite('toBitwise/' + name, img)
    i += 1