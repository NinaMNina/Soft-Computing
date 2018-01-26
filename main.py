import numpy
import cv2
import math

try:
    from cv2 import cv2
except ImportError:
    pass

if __name__ == '__main__':
    print 'hi'
    img = cv2.imread('images/test2.png', 0)  # ucitavanje slike sa diska

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#
 #   image_ada_bin = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 5)
 #   cv2.imshow('image2', image_ada_bin)
 #   cv2.waitKey(0)
  #  cv2.destroyAllWindows()
    gray = cv2.imread('images/test2.png', 0)

    edges = cv2.Canny(gray, 80, 120)
    lines = cv2.HoughLinesP(edges, 1, math.pi / 2, 2, None, 30, 1);
    for line in lines[0]:
        pt1 = (line[0], line[1])
        pt2 = (line[2], line[3])
        cv2.line(gray, pt1, pt2, (0, 0, 255), 3)

    cv2.imwrite("images/test3.png", gray)
    img = cv2.imread('images/test3.png', 0)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
