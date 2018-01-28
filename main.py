import numpy as np
import cv2
import math
import collections
import os

try:
    from cv2 import cv2
except ImportError:
    pass

if __name__ == '__main__':
    print 'hi'
    img = cv2.imread('images/ops.jpg')
    # image_ada = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # bw = cv2.adaptiveThreshold(image_ada, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
    # cv2.imshow('treshold', bw)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    # img_ero = cv2.dilate(bw, kernel, iterations=1)
    # img_open = cv2.dilate(img_ero, kernel, iterations=1)
    # cv2.imshow('treshold', bw)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    minLineLength = img.shape[1] - 300
    lines = cv2.HoughLinesP(image=edges, rho=0.02, theta=np.pi / 500, threshold=10, lines=np.array([]),
                            minLineLength=minLineLength, maxLineGap=50)

    y, x, c = lines.shape
    matrix = []
    # print(lines.shape)
    for i in range(y):
        cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)

    # cv2.imshow('edges', edges)
    # cv2.imshow('result', img)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    for col in range(img.shape[1]):
        for row in range(img.shape[0]):
            if (img.item(row, col, 2) != 255):
                img.itemset((row, col, 0), 255)
                img.itemset((row, col, 1), 255)
                img.itemset((row, col, 2), 255)

    # cv2.imshow('result', img)
    #
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    col = img.shape[1] / 2
    for row in range(img.shape[0]):

        if (img.item(row, col, 2) == 255 and img.item(row, col, 0) < 230 and img.item(row, col, 1) < 230):
            if (img.item(row - 1, col, 2) > 230 and img.item(row - 1, col, 0) > 230 and img.item(row - 1, col,
                                                                                                 1) > 230):
                l = [row, col]
                matrix.append(l)
            # img.itemset((row,col, 0), 255)

    length = len(matrix) / 5

    img = cv2.imread('images/ops.jpg')
    for i in range(length):
        top = matrix[i * 5]
        bottom = matrix[(i * 5) + 4]
        lajna = img[(top[0] - 35):(bottom[0] + 35), :, :]
        ime = 'images/slika'
        ime += str(i)
        ime += '.png'
        cv2.imwrite(ime, lajna)

        # cv2.imshow('lajna', lajna)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    img = cv2.imread('images/slika0.png')
    # edges = cv2.Canny(img, 100, 200)
    # edges = 255 - edges
    # cv2.imshow('edges', edges)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # #circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 5, 8, param1=50, param2=30, minRadius=5, maxRadius=15)
    # circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 5, 8, param1=40, param2=30, minRadius=5, maxRadius=15)
    # circles = np.uint16(np.around(circles))
    # for i in circles[0, :]:
    #     row = i[1]
    #     col = i[0]
    #     if (img.item(row, col)<30) :
    #         cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 1)  # draw the outer circle
    #         cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)  # draw the center of the circle
    #
    # cv2.imshow('detected circles', cimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    minLineLength = img.shape[1] - 300
    lines = cv2.HoughLinesP(image=edges, rho=0.02, theta=np.pi / 500, threshold=10, lines=np.array([]),
                            minLineLength=minLineLength, maxLineGap=50)

    y, x, c = lines.shape
    matrix = []
    # print(lines.shape)
    for i in range(y):
        cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (255, 255, 255), 2,
                 cv2.LINE_AA)

    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            if (img.item(row, col, 2) < 100):
                if (img.item(row - 1, col, 2) < 100):
                    if (matrix.__contains__(col)):
                        continue
                    else:
                        matrix.append(col)
                # img.itemset((row,col, 0), 255)
    matrix.sort()
    notes = []
    matSize = len(matrix) - 1
    begin = matrix[0] - 1
    for i in range(matSize):
        if (matrix[i + 1] - matrix[i] > 10):
            end = matrix[i]
            l = [begin, end]
            notes.append(l)
            begin = matrix[i + 1]

    # print notes

    cv2.imshow('lines', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    length = len(notes)



    loc = os.getcwd()

    loc += '/recognition'
    print loc

    fileList = os.listdir(loc)
    for fileName in fileList:
        os.remove(loc + "/" + fileName)

    img = cv2.imread('images/slika0.png')
    for i in range(length):
        value = notes[i]
        left = value[0]
        right = value[1]
        notica = img[:, (left - 5):(right + 5), :]
        ime = 'recognition/nota'
        ime += str(i)
        ime += '.png'
        cv2.imwrite(ime, notica)
