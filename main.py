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


