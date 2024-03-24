"""
This is the main file of the project. 
"""
import numpy as np
import cv2
import os
import open3d as o3d
data_path = 'data/'

# testing samples
Box = np.load('data/8b061a8a-9915-11ee-9103-bbb8eae05561/bbox3d.npy')
Mask = np.load('data/8b061a8a-9915-11ee-9103-bbb8eae05561/mask.npy')
PC = np.load('data/8b061a8a-9915-11ee-9103-bbb8eae05561/pc.npy')
img = cv2.imread('data/8b061a8a-9915-11ee-9103-bbb8eae05561/rgb.jpg')
pc = o3d.geometry.PointCloud()
pc.points = o3d.utility.Vector3dVector(PC.reshape(3, -1).T)
o3d.visualization.draw_geometries([pc])
print(Box.shape)
print(Mask.shape)
print(PC.shape)
print(img.shape)

# calculate max_height, max_width, and count
max_height = 0
max_width = 0
count = 0
for folder in os.listdir(data_path):
    count += 1
    rgb = os.path.join(data_path, folder+'/rgb.jpg')
    if not os.path.exists(rgb):
        count -= 1
        continue
    img = cv2.imread(rgb)
    max_height = max(max_height, img.shape[0])
    max_width = max(max_width, img.shape[1])
print(max_height, max_width, count)

# padding
for folder in os.listdir(data_path):

    rgb = os.path.join(data_path, folder+'/rgb.jpg')
    pc = os.path.join(data_path, folder+'/pc.npy')
    mask = os.path.join(data_path, folder+'/mask.npy')

    if not os.path.exists(rgb):
        continue

    img = cv2.imread(rgb) # (H, W, 3)
    point_cloud = np.load(pc) # (3, H, W)
    point_cloud = point_cloud.transpose(1, 2, 0) # (H, W, 3)
    mask = np.load(mask) # (objects, H, W)
    bbox3d = np.looad() # (objects, 8, 3)


#     if img.shape[0] == max_height or img.shape[1] == max_width:
#         cv2.imshow('img', img)
#         cv2.waitKey(10)
#         continue



