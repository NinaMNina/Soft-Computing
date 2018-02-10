import cv2, os
import numpy as np
import rotate

def doRotation(dst, top, bottom, left, right):
    top1 = -1
    top2 = -1
    # dst = dst[(top-border):(bottom+border), (left-border):(right+border), :]

    # cv2.imshow('kraj', dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    out = False
    for x in range(dst.shape[0]):
        for y in range(dst.shape[1]):
            if (dst.item(x, y, 2) > 200):
                top1 = x
                top2 = y
                out = True
                break
        if (out == True):
            break

    # print(top1, top2)

    # cv2.circle(dst, (top1, top2), 3, (0, 0, 255), -1)  # crvena
    # cv2.circle(dst, (left, bottom), 3, (0, 255, 0), -1)  # zelena
    # cv2.circle(dst, (right, top2), 3, (255, 0, 0), -1)  # plava
    # cv2.circle(dst, (left + (right - top1), bottom), 3, (255, 0, 255), -1)  # roza
    #
    # cv2.circle(dst, (left, top2), 3, (0, 255, 255), -1)  # zuta
    # cv2.circle(dst, (left + (right - top1), top2), 3, (255, 255, 0), -1)  # tirkiz

    pts1 = np.float32([[top1, top2], [left, bottom], [right, top2], [left + (right - top1), bottom]])
    pts2 = np.float32([[left, top2], [left, bottom], [left + (right - top1), top2], [left + (right - top1), bottom]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(dst, M, (dst.shape[0], dst.shape[1]))
    # cv2.imshow('posle transf', dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    pic_loc = os.getcwd()
    pic_loc += '/images/rotated.jpg'
    out = False
    for x in range(dst.shape[0]):
        for y in range(dst.shape[1]):
            if (dst.item(x, y, 1) > 200):
                top = x
                out = True
                break
        if (out == True):
            break
    out = False
    for x in range(dst.shape[1]):
        for y in range(dst.shape[0]):
            if (dst.item(y, x, 1) > 200):
                left = x
                out = True
                break
        if (out == True):
            break
    out = False
    for x in range(dst.shape[1] - 1, 0, -1):
        for y in range(dst.shape[0]):
            if (dst.item(y, x, 1) > 200):
                right = x
                out = True
                break
        if (out == True):
            break
    out = False
    for x in range(dst.shape[0] - 1, 0, -1):
        for y in range(dst.shape[1]):
            if (dst.item(x, y, 1) > 200):
                bottom = x
                out = True
                break
        if (out == True):
            break
    border = int(dst.shape[1] * 0.03)
    if (border > top):
        border = top
    if (border > bottom):
        border = bottom
    if (border > left):
        border = left
    if (border > right):
        border = right
    slika = dst[(top - border):(bottom + border), (left - border):(right + border), :]
    slika = (255 - slika)
    cv2.imwrite(pic_loc, slika)
    rotate.doRotation(pic_loc)