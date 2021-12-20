import numpy as np
import cv2



def multidim_intersect(arr1, arr2):
    arr1_view = arr1.view([('',arr1.dtype)]*arr1.shape[1])
    arr2_view = arr2.view([('',arr2.dtype)]*arr2.shape[1])
    intersected = np.intersect1d(arr1_view, arr2_view)
    return intersected.view(arr1.dtype).reshape(-1, arr1.shape[1])


idx_img = []
for coord in zip(inter_img[0], inter_img[1]):
    idx_img.append(coord)

idx_edge = []
for coord in zip(inter_edge[0], inter_edge[1]):
    idx_edge.append(coord)


inter_img = np.where(img != 0)
inter_edge = np.where(edge != 0)