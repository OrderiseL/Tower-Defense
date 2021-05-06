import numpy as np
from PIL import Image
import math
from settings import Settings

settings = Settings()
# Load image of map
im = Image.open(r'used_assets\cleaned background.bmp')
im = im.resize((settings.scr_width, settings.scr_height))
# Create grid from image.
grid = np.array(im)  # True: valid path. False: Obstacle.
#
MAX_ROW = grid.shape[1]
MAX_COL = grid.shape[0]


class Node:
    """A structure to represent grid cell"""

    def __init__(self):
        self.parent_x = self.parent_y = 0
        self.g = 0  # distance from starting node.
        self.h = 0  # distance from end node
        self.f = 0  # G+H


#  check whether given cell (row, col) is a valid cell or not.
def isValid(x, y):
    # Returns true if row number and column number
    # is in range
    return (grid.shape[1] > x >= 0) and (0 <= y < grid.shape[0])


# check whether the given cell is blocked or not
def isUnBlocked(x, y):
    # Returns true if the cell is not blocked else false
    return grid[y, x]


# A Utility Function to check whether destination cell has been reached or not
def isDestination(x, y, dest):
    # dest: (x,y) tuple
    return (x, y) == dest


class A_STAR:
    def __init__(self, start, end):
        self.settings = Settings()
        # Load image of full course
        im = Image.open(r'used_assets\cleaned background.bmp')
        im = im.resize((self.settings.scr_width, self.settings.scr_height))
        # Create grid from image.
        self.image_vals = np.array(im)  # True: valid path. False: Obstacle.
        self.grid = np.array([Node])
        #
        self.openSet = np.array()
        self.closedSet = np.array()


if __name__ == '__main__':
    pass
