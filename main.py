import numpy as np
import cv2
import math
import collections
import os
import shutil
from nn_setup import CNNValue
from nn_setup_duration import CNNDuraiton

from mainFrame import MainFrame

try:
    CNNValue.reloadModel()
    print('nn setup reload')
    CNNDuraiton.reloadModel()
    print('nn duration reload')
except:
    pass
print('hi')
window = MainFrame()

