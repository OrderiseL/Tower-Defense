from PIL import Image
import numpy as np
import math
from queue import PriorityQueue


# TODO: preprocess map to fit enemys' width and height.

class Node:
    """Class to represent a node on the grid"""

    def __init__(self):
        self.row = 0
        self.col = 0
        self.g = math.inf
        self.is_blocked = False
        self.neighbors = []

    def update_neighbors(self, grid):

        self.neighbors = []
        if self.row < MAX_ROW - 1 and not grid[self.row + 1][self.col].is_blocked:  # DOWN
            self.neighbors.append(grid[self.row + 1][self.col])
            if self.col < MAX_COL - 1 and not grid[self.row + 1][self.col + 1].is_blocked:  # RIGHT
                self.neighbors.append(grid[self.row + 1][self.col + 1])
            if self.col > 0 and not grid[self.row + 1][self.col - 1].is_blocked:  # LEFT
                self.neighbors.append(grid[self.row + 1][self.col - 1])

        if self.row > 0 and not grid[self.row - 1][self.col].is_blocked:  # UP
            self.neighbors.append(grid[self.row - 1][self.col])
            if self.col < MAX_COL - 1 and not grid[self.row - 1][self.col + 1].is_blocked:  # RIGHT
                self.neighbors.append(grid[self.row - 1][self.col + 1])
            if self.col > 0 and not grid[self.row - 1][self.col - 1].is_blocked:  # LEFT
                self.neighbors.append(grid[self.row - 1][self.col - 1])

        if self.col < MAX_COL - 1 and not grid[self.row][self.col + 1].is_blocked:  # RIGHT
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_blocked:  # LEFT
            self.neighbors.append(grid[self.row][self.col - 1])

    def __eq__(self, other):
        return (self.row, self.col) == (other.row, other.col)


def heuristic(src, dest):
    # Euclidean heuristic
    return math.dist(src, dest)


def reconstruct_path(came_from, current):
    """
    :returns: list of positions from start to end
    """
    path = []
    while current in came_from:
        current = came_from[current]
        path.append((current.row, current.col))
    path.reverse()
    return path


def a_star_search(src, dest, grid):
    """
    :param src: type (row,col) tuple
    :param grid: Node
    """
    open_set = PriorityQueue()
    came_from = {}  # keep track of nodes in path
    open_set_hash = {}  # Track items in openset
    # Reset start node
    grid[src[0]][src[1]].g = 0
    f = grid[src[0]][src[1]].g + heuristic(src, dest)
    open_set.put((f, grid[src[0]][src[1]]))  # (f,Node)
    open_set_hash = {src}
    while not open_set.empty():
        current = open_set.get()[1]
        if (current.row, current.col) == dest:
            return reconstruct_path(came_from, current)

        open_set_hash.remove((current.row, current.col))
        for neighbor in current.neighbors:
            est_g = current.g + heuristic((neighbor.row, neighbor.col), (current.row, current.col))
            if est_g < neighbor.g:
                came_from[neighbor] = current
                neighbor.g = est_g
                f = heuristic((neighbor.row, neighbor.col), dest)
                if neighbor not in open_set_hash:
                    open_set_hash.add((neighbor.row, neighbor.col))
                    open_set.put((f, neighbor))
    return False


# Load image of map
im = Image.open(r'used_assets\cleaned background.bmp')
im = im.resize((1000, 600))
# Create grid from image.
img_grid = np.array(im)  # True: valid path. False: Obstacle.
MAX_ROW = img_grid.shape[0]
MAX_COL = img_grid.shape[1]
if __name__ == '__main__':
    # Create a Node grid from img grid.
    grid = [[]]
    for i in range(MAX_ROW):
        for j in range(MAX_COL):
            new_node = Node()
            new_node.row = i
            new_node.col = j
            # when cell is False it means pixel is an obstacle.
            if not img_grid[i, j]:
                new_node.is_blocked = True
            grid[i].append(new_node)
        grid.append([])
    for i in range(MAX_ROW):
        for j in range(MAX_COL):
            grid[i][j].update_neighbors(grid)
    print(a_star_search((1, 192), (-40, 290), grid))
