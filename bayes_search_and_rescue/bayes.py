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

class Search():
    """Bayesian search and rescue game with three search areas."""

    def __init__(self, name) -> None:
        self.name = name

        self.img = cv.imread(filename = MAP_FILE, flags = cv.IMREAD_COLOR)
        if self.img is None:
            print("Could not read map file {}".format(MAP_FILE), file= sys.stderr)
            sys.exit(1)

        # Set placeholders for sailor's actual location
        self.area_actual = 0
        self.sailor_actual = [0, 0]  # As "local" coords within search area

        # Create numpy arrays for each search area by indexing image array.
        self.sa1 = self.img[SA1_CORNERS[1] : SA1_CORNERS[3],
                            SA1_CORNERS[0] : SA1_CORNERS[2]]

        self.sa2 = self.img[SA2_CORNERS[1] : SA2_CORNERS[3],
                            SA2_CORNERS[0] : SA2_CORNERS[2]]

        self.sa3 = self.img[SA3_CORNERS[1] : SA3_CORNERS[3],
                            SA3_CORNERS[0] : SA3_CORNERS[2]]

        # Set initial per-area target probabilities for finding sailor
        self.p1 = 0.2
        self.p2 = 0.5
        self.p3 = 0.3

        # Initialize search effectiveness probabilities.
        self.sep1 = 0
        self.sep2 = 0
        self.sep3 = 0
