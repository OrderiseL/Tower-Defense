from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
from queue import PriorityQueue


class Node:
    """Class to represent a node on the node_grid"""

    def __init__(self):
        self.row = 0
        self.col = 0
        self.g = math.inf
        self.is_blocked = False
        self.parent = None
        self.neighbors = []

    def update_neighbors(self, node_grid):

        self.neighbors = []
        if self.row < MAX_ROW - 1 and not node_grid[self.row + 1][self.col].is_blocked:  # DOWN
            self.neighbors.append(node_grid[self.row + 1][self.col])
            if self.col < MAX_COL - 1 and not node_grid[self.row + 1][self.col + 1].is_blocked:  # RIGHT
                self.neighbors.append(node_grid[self.row + 1][self.col + 1])
            if self.col > 0 and not node_grid[self.row + 1][self.col - 1].is_blocked:  # LEFT
                self.neighbors.append(node_grid[self.row + 1][self.col - 1])

        if self.row > 0 and not node_grid[self.row - 1][self.col].is_blocked:  # UP
            self.neighbors.append(node_grid[self.row - 1][self.col])
            if self.col < MAX_COL - 1 and not node_grid[self.row - 1][self.col + 1].is_blocked:  # RIGHT
                self.neighbors.append(node_grid[self.row - 1][self.col + 1])
            if self.col > 0 and not node_grid[self.row - 1][self.col - 1].is_blocked:  # LEFT
                self.neighbors.append(node_grid[self.row - 1][self.col - 1])

        if self.col < MAX_COL - 1 and not node_grid[self.row][self.col + 1].is_blocked:  # RIGHT
            self.neighbors.append(node_grid[self.row][self.col + 1])

        if self.col > 0 and not node_grid[self.row][self.col - 1].is_blocked:  # LEFT
            self.neighbors.append(node_grid[self.row][self.col - 1])

    def __lt__(self, other):
        return other


def heuristic(src, dest):
    # Euclidean heuristic
    return math.dist(src, dest)


def reconstruct_path(current):
    """
    :returns: list of positions from start to end
    """
    path = []
    while current.parent is not None:
        path.append((current.col, current.row))
        current = current.parent
    path.append((current.col, current.row))
    path.reverse()
    return path


def a_star_search(src, dest, node_grid):
    """
    :param src: type (row,col) tuple
    :param node_grid: Node matrice [row][col]
    """
    open_set = PriorityQueue()
    came_from = {}  # keep track of nodes in path
    open_set_hash = {}  # Track items in openset
    # Reset start node
    node_grid[src[0]][src[1]].g = 0
    f = node_grid[src[0]][src[1]].g + heuristic(src, dest)
    open_set.put((f, node_grid[src[0]][src[1]]))  # (f,Node)
    open_set_hash = {src}
    while not open_set.empty():
        current = open_set.get()[1]

        if (current.row, current.col) == dest:
            return reconstruct_path(current)

        open_set_hash.remove((current.row, current.col))
        for neighbor in current.neighbors:
            est_g = current.g + heuristic((neighbor.row, neighbor.col), (current.row, current.col))
            if est_g < neighbor.g:
                neighbor.parent = current
                neighbor.g = est_g
                f = heuristic((neighbor.row, neighbor.col), dest)
                if (neighbor.row, neighbor.col) not in open_set_hash:
                    open_set_hash.add((neighbor.row, neighbor.col))
                    open_set.put((f, neighbor))
    return False


def process_to_grid(path):
    """
    returns numpy array from resized image
    :param path:
    :param length:
    :return: ndarray
    """
    # Open and fit to map
    img = Image.open(path)
    img = img.convert('L')
    return np.array(img)


map_grid = process_to_grid("used_assets/cleaned.png")
plt.imshow(map_grid, cmap="gray")  # Show map_grid
MAX_ROW = map_grid.shape[0]
MAX_COL = map_grid.shape[1]


def get_pos(pos, division):
    """
    returns x,y values scaled to map.
    :param pos:
    :param division:
    :return: tuple(x,y)
    """
    x = pos[0] * division
    y = pos[1] * division
    return x, y


def get_reverse_pos(pos, division):
    """
    returns row,col values to access grid.
    :param pos:
    :param division:
    :return: tuple(r,c)
    """
    r = round(pos[1] / division)
    c = round(pos[0] / division)
    return r, c


def create_node_grid(map_grid):
    # Create a Node node_grid from map_grid node_grid.
    node_grid = [[]]
    for i in range(MAX_ROW):
        for j in range(MAX_COL):
            new_node = Node()
            new_node.row = i
            new_node.col = j
            # when cell is False it means pixel is an obstacle.
            if not map_grid[i, j]:
                new_node.is_blocked = True
            node_grid[i].append(new_node)
        node_grid.append([])
    for i in range(MAX_ROW):
        for j in range(MAX_COL):
            node_grid[i][j].update_neighbors(node_grid)
    return node_grid


if __name__ == '__main__':
    # Create a node_grid from map_grid .
    node_grid = create_node_grid(map_grid)
    print(a_star_search((270, 0), (430, 0), node_grid))
