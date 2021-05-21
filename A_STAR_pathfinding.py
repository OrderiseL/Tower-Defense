from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
from queue import PriorityQueue

SQUARE_SIZE = 10


class Node:
    """Class to represent a node on the node_grid"""

    def __init__(self):
        self.row = 0
        self.col = 0
        self.is_blocked = False
        self.parent = None
        self.neighbors = []

    def update_neighbors(self, node_grid):
        MAX_ROW = node_grid.shape[0]
        MAX_COL = node_grid.shape[1]
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


def reconstruct_path(came_from, current):
    """
    :param current: Node
    :param came_from: Dictionary
    :returns: list of positions from start to end
    """
    path = []
    while current in came_from:
        path.append([current.row, current.col])
        current = came_from[current]
    path.append([current.row, current.col])
    path.reverse()
    return path


def a_star_search(src, dest, node_grid):
    """
    :param src: type (row,col) tuple
    :param node_grid: Node matrice [row][col]
    """
    src = tuple(src)
    dest = tuple(dest)
    open_set = PriorityQueue()
    came_from = {}  # keep track of nodes in path
    open_set_hash = {}  # Track items in openset
    # Reset start node
    g_score = {node: float("inf") for row in node_grid for node in row}
    g_score[node_grid[src[0], src[1]]] = 0
    f = g_score[node_grid[src[0], src[1]]] + heuristic(src, dest)
    open_set.put((f, node_grid[src[0], src[1]]))  # (f,Node)
    open_set_hash = {src}
    while not open_set.empty():
        current = open_set.get()[1]

        if (current.row, current.col) == dest:
            return reconstruct_path(came_from, current)

        open_set_hash.remove((current.row, current.col))
        for neighbor in current.neighbors:
            est_g = g_score[current] + heuristic((neighbor.row, neighbor.col), (current.row, current.col))
            if est_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = est_g
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
    thresh = 200
    fn = lambda x: 255 if x > thresh else 0
    img = img.convert('L').point(fn, mode='1')
    width, height = img.size
    img = img.resize((width // SQUARE_SIZE, height // SQUARE_SIZE), Image.BICUBIC)
    return np.array(img)


def get_pos(pos):
    """
    returns x,y values scaled to map.
    :param pos: (row,col)
    :return: tuple(x,y)
    """
    y = pos[0] * SQUARE_SIZE
    x = pos[1] * SQUARE_SIZE
    return x, y


def get_reverse_pos(pos):
    """
    returns x,y values scaled to map.
    :param pos: (x,y)
    :return: tuple(r,c)
    """
    c = round(pos[0] / SQUARE_SIZE)
    r = round(pos[1] / SQUARE_SIZE)
    return r, c


def create_node_grid(map_grid):
    """

    :param map_grid: Ndarray
    :return: Node ndarray
    """
    # Create a Node node_grid from map_grid node_grid.
    rows, cols = map_grid.shape
    node_grid = np.empty(map_grid.shape, Node)
    for i in range(rows):
        for j in range(cols):
            new_node = Node()
            new_node.row = i
            new_node.col = j
            # when cell is False it means pixel is an obstacle.
            if not map_grid[i, j]:
                new_node.is_blocked = True
            node_grid[i, j] = new_node
    for i in range(rows):
        for j in range(cols):
            node_grid[i, j].update_neighbors(node_grid)

    return node_grid


# Create a node_grid from map_grid.
map_grid = process_to_grid(r"used_assets\cleaned.png")
node_grid = create_node_grid(map_grid)
# print(a_star_search((26, 0), (43, 0), node_grid))
map_plot = plt.imshow(map_grid, cmap="gray")
if __name__ == '__main__':
    pass
