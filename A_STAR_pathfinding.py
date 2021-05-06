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
MAX_ROW = grid.shape[0]
MAX_COL = grid.shape[1]


class Node:
    """A structure to represent grid cell"""

    def __init__(self):
        self.parent_x = self.parent_y = -1
        self.g = math.inf  # distance from starting node.
        self.h = math.inf  # distance from end node
        self.f = math.inf  # G+H


#  check whether given cell (row, col) is a valid cell or not.
def isValid(x, y):
    # Returns true if row number and column number
    # is in range
    return (MAX_COL > x >= 0) and (0 <= y < MAX_ROW)


# check whether the given cell is blocked or not
def isUnBlocked(x, y):
    # Returns true if the cell is not blocked else false
    return grid[y, x]


# A Utility Function to check whether destination cell has been reached or not
def isDestination(x, y, dest):
    # dest: (x,y) tuple
    return (x, y) == dest


# Calculate H value.
def heuristic(curr, dest):
    return math.dist(curr, dest)


# trace the path from the source to destination
def tracepath(cell_details, dest):
    print("The path is: ")
    x, y = dest

    path_stack = []

    while (cell_details[y, x].parent_y != y) and (cell_details[y, x].parent_x != x):
        path_stack.append((x, y))
        temp_x = cell_details[y, x].parent_x
        temp_y = cell_details[y, x].parent_y
        x = temp_x
        y = temp_y

    path_stack.append((x, y))
    while len(path_stack) >= 1:
        pos = path_stack.pop()
        print("-> {}".format(pos))


# A Function to find the shortest path between
# a given source cell to a destination cell
# according to A* Search Algorithm.
def a_star_search(src, dest):
    closed_list = np.zeros(grid.shape)
    # Create node array.
    cell_details = np.array([[Node() for i in range(MAX_COL)]
                             for j in range(MAX_ROW)], dtype=Node)

    # Initialize parameters of starting node.
    x, y = src
    cell_details[y, x].parent_x = x
    cell_details[y, x].parent_y = y
    cell_details[y, x].f = 0.0
    cell_details[y, x].g = 0.0
    cell_details[y, x].h = 0.0

    # Open list that contain [F cost, position].
    # Start at  the starting cell
    open_list = [[0.0, (x, y)]]
    found = False
    while len(open_list) >= 1:
        p = open_list.pop()
        x, y = p
        closed_list[y, x] = True
        """
        Generating all the 8 neighbors of this cell
 
             N.W   N   N.E
               \   |   /
                \  |  /
             W----Cell----E
                  / | \
                /   |  \
             S.W    S   S.E
 
         Cell-->Popped Cell (i, j)
         N -->  North       (i-1, j)
         S -->  South       (i+1, j)
         E -->  East        (i, j+1)
         W -->  West           (i, j-1)
         N.E--> North-East  (i-1, j+1)
         N.W--> North-West  (i-1, j-1)
         S.E--> South-East  (i+1, j+1)
         S.W--> South-West  (i+1, j-1)"""
        gNew, hNew, fNew = 0.0



if __name__ == '__main__':
    a_star_search((1, 2), (4, 5))
    pass
