import cv2
import numpy as np
import matplotlib.pyplot as plt

# import maze image
maze = cv2.imread('testmaze.png')
# mark beginning and end
cv2.circle(maze, (330, 595), 3, (255, 0, 0), -1)
cv2.circle(maze, (273, 5), 3, (0, 0, 255), -1)
# show image
plt.figure(figsize=(8, 8))
plt.imshow(maze)
plt.show()


class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.distance = float('inf')
        self.parentX = None
        self.parentY = None
        self.processed = False
        self.index = None


def bubble_up(queue, index):
    if index <= 0:
        return queue
    p_index = (index - 1) // 2
    if queue[index].d < queue[p_index].d:
        queue[index], queue[p_index] = queue[p_index], queue[index]
        queue[index].index_in_queue = index
        queue[p_index].index_in_queue = p_index
        queue = bubble_up(queue, p_index)
    return queue


def bubble_down(queue, index):
    length = len(queue)
    lc_index = 2 * index + 1
    rc_index = lc_index + 1
    if lc_index >= length:
        return queue
    if lc_index < length <= rc_index:  # just left child
        if queue[index].d > queue[lc_index].d:
            queue[index], queue[lc_index] = queue[lc_index], queue[index]
            queue[index].index_in_queue = index
            queue[lc_index].index_in_queue = lc_index
            queue = bubble_down(queue, lc_index)
    else:
        small = lc_index
        if queue[lc_index].d > queue[rc_index].d:
            small = rc_index
        if queue[small].d < queue[index].d:
            queue[index], queue[small] = queue[small], queue[index]
            queue[index].index_in_queue = index
            queue[small].index_in_queue = small
            queue = bubble_down(queue, small)
    return queue


def find_path(maze_img, begin, end):
    priority_queue = []
    pixel_matrix = np.full((maze_img.shape[0], maze_img.shape[1]), None)

    for r in range(maze_img.shape[0]):
        for c in range(maze_img.shape[1]):
            pixel_matrix[r][c] = Pixel(c, r)
            pixel_matrix[r][c].index = len(priority_queue)
            priority_queue.append(pixel_matrix[r][c])
    pixel_matrix[begin[0]][begin[1]].d = 0
    priority_queue = bubble_up(priority_queue, pixel_matrix[begin[0]][begin[1]].index)
