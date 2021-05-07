from PIL import Image
import numpy as np
import math
from queue import PriorityQueue


class Node:
    """Class to represent a node on the grid"""

    def __init__(self):
        self.parent = -1
        self.h = math.inf
        self.g = math.inf
        self.is_blocked = False


def heuristic(src, dest):
    # Euclidean heuristic
    return math.dist(src, dest)


def reconstruct_path(came_from, curr):
    pass


def is_valid(src):
    r, c = src
    valid = True
    if c > MAX_COL or c < 0:
        return False
    if r > MAX_ROW or r < 0:
        return False
    if grid[r, c].is_blocked:
        return False
    return True


def visit_neighbors(curr, grid):
    neighbors = []
    i, j = curr
    if is_valid(i+1,j):
        neighbors.append(grid[i+1,j])


def a_star_search(src, dest, grid):
    """
    :param src: type (row,col) tuple
    :param grid: Node
    """
    open_set = PriorityQueue()
    closed_set = []
    came_from = []
    # Reset start node
    grid[src].g = 0
    grid[src].h = heuristic(src, dest)
    f = grid[src].g + grid[src].h
    open_set.put((f, grid[src]))

    while not open_set.empty():
        current = open_set.get()[1]
        if current == dest:
            return reconstruct_path(came_from, current)
        closed_set.append(current)


# Load image of map
im = Image.open(r'used_assets\cleaned background.bmp')
im = im.resize((1000, 600))
# Create grid from image.
img_grid = np.array(im)  # True: valid path. False: Obstacle.
MAX_ROW = img_grid.shape[0]
MAX_COL = img_grid.shape[1]

# Create a Node grid from img grid.
grid = [[]]
for i in range(MAX_ROW):
    for j in range(MAX_COL):
        new_node = Node()
        # when cell is False it means pixel is an obstacle.
        if not img_grid[i, j]:
            new_node.is_blocked = True
        grid[i].append(new_node)
    grid.append([])

if __name__ == '__main__':
    pass
