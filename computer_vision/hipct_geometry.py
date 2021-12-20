import numpy as np
import cv2

idx_img = []
for coord in zip(inter_img[0], inter_img[1]):
    idx_img.append(coord)

idx_edge = []
for coord in zip(inter_edge[0], inter_edge[1]):
    idx_edge.append(coord)


inter_img = np.where(img != 0)
inter_edge = np.where(edge != 0)