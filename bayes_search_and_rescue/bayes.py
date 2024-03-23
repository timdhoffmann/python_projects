"""
Next section: Drawing the map
"""

import sys
import random
import itertools
import numpy as np
import cv2 as cv

# TODO: fix after checking that the error works.
MAP_FILE_NAME = '<remove_me>cape_python.png'

# (UL-X, UL-Y, LR-X, LR-Y)
SEARCH_AREA1_CORNERS = (130, 265, 180, 315)
SEARCH_AREA2_CORNERS = (80, 255, 130, 305)
SEARCH_AREA3_CORNERS = (105, 205, 155, 255)


class Search:
    """Bayesian search and rescue game with three search areas."""

    def __init__(self, name: str) -> None:
        self.name = name

        self.img = cv.imread(filename=MAP_FILE_NAME, flags=cv.IMREAD_COLOR)
        if self.img is None:
            print(f"Could not read map file {MAP_FILE_NAME}", file=sys.stderr)
            sys.exit(1)

        # The sailor's actual location.
        self.sailor_search_area = 0
        self.sailor_search_area_coordinates = [0, 0]

        # Create numpy arrays for each search area by indexing image array.
        self.search_area1 = self.img[
                            SEARCH_AREA1_CORNERS[1]: SEARCH_AREA1_CORNERS[3],
                            SEARCH_AREA1_CORNERS[0]: SEARCH_AREA1_CORNERS[2]]

        self.search_area2 = self.img[
                            SEARCH_AREA2_CORNERS[1]: SEARCH_AREA2_CORNERS[3],
                            SEARCH_AREA2_CORNERS[0]: SEARCH_AREA2_CORNERS[2]]

        self.search_area3 = self.img[
                            SEARCH_AREA3_CORNERS[1]: SEARCH_AREA3_CORNERS[3],
                            SEARCH_AREA3_CORNERS[0]: SEARCH_AREA3_CORNERS[2]]

        # Per-area target probabilities for finding sailor.
        self.area1_probability = 0.2
        self.area2_probability = 0.5
        self.area3_probability = 0.3

        self.area1_search_effectiveness_probability = 0
        self.area2_search_effectiveness_probability = 0
        self.area3_search_effectiveness_probability = 0

    def draw_map(self, last_known) -> None:
        cv.line(self.img, (20,370), (70, 370), (0, 0, 0), 2)
        cv.putText
