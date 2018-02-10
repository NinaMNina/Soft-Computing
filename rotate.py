import cv2
import math
import os

def doRotation(path):
    img = cv2.imread(path, 1)
    a=0
    b=0
    a0=int(img.shape[1]*0.15)
    b0=int(img.shape[1]*0.8)


    for y in range(img.shape[0]-1, 0, -1):
        xa = img.item(y, a0, 1)
        xb = img.item(y, b0, 1)
        if(xa<200):
            a = y
        if(xb<200):
            b = y

    # cv2.imshow('img1',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    kateta = b0-a0
    kateta2 = b-a
    hipotenuza = math.sqrt(pow(b-a,2)+pow(b0-a0,2))
    angleR = math.acos(kateta/hipotenuza)
    angleS = angleR*180/3.14
    if(kateta2<0):
        angleS = 360-angleS
    if(angleS==0):
        pic_loc = os.getcwd()
        pic_loc += '/images/rotated.jpg'
        cv2.imwrite(pic_loc, img)
        return

    print (angleS)
    img = (255-img)
    # cv2.imshow('img2 before borders', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    border_size = int(img.shape[1]*0.4)
    img=cv2.copyMakeBorder(img, top=border_size, bottom=border_size, left=border_size, right=border_size, borderType= cv2.BORDER_CONSTANT )
    # cv2.imshow('img2 with borders',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    M = cv2.getRotationMatrix2D((img.shape[0]/2,img.shape[1]/2),angleS,1)
    dst = cv2.warpAffine(img,M,(img.shape[0],img.shape[1]))

    cv2.imshow('dst',dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    left=0
    right=dst.shape[1]
    top=0
    bottom=dst.shape[0]
    out=False
    for x in range(dst.shape[0]):
        for y in range(dst.shape[1]):
            if(dst.item(x, y, 1)>200):
                top=x
                out=True
                break
        if(out==True):
            break
    out=False
    for x in range(dst.shape[1]):
        for y in range(dst.shape[0]):
            if (dst.item(y, x, 1) > 200):
                left = x
                out=True
                break
        if(out==True):
            break
    out=False
    for x in range(dst.shape[1]-1, 0, -1):
        for y in range(dst.shape[0]):
            if (dst.item(y, x, 1) > 200):
                right = x
                out=True
                break
        if(out==True):
            break
    out=False
    for x in range(dst.shape[0]-1, 0, -1):
        for y in range(dst.shape[1]):
            if (dst.item(x, y, 1) > 200):
                bottom = x
                out=True
                break
        if(out==True):
            break
    border = int(dst.shape[1]*0.03)
    print (top, bottom, left, right)
    slika = dst[ (top-border):(bottom+border), (left-border):(right+border), :]

    slika = (255-slika)
    # cv2.imshow('kraj',slika)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    pic_loc = os.getcwd()
    pic_loc += '/images/rotated.jpg'
    cv2.imwrite(pic_loc, slika)