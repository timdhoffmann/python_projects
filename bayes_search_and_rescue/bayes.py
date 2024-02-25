import sys
import random
import itertools
import numpy as np
import cv2 as cv

MAP_FILE: str = 'cape_python.png'

# (UL-X, UL-Y, LR-X, LR-Y)
SA1_CORNERS = (130, 265, 180, 315)
SA2_CORNERS = (80, 255, 130, 305)
SA3_CORNERS = (105, 205, 155, 255)
