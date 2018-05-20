#coding: 'utf-8'

"""
eigen14_DepthEstimation
mat2png

created by Kazunari on 2018/05/20 
"""

import os
import numpy as np
import glob
from PIL import Image

dir_path = "/Users/Kazunari/projects/dataset/eccv14-data/data/depth"

paths = glob.glob(os.path.join(dir_path, "*"))

if not os.path.exists(os.path.join(dir_path, "../normalizedDepthImage")):
    os.mkdir(os.path.join(dir_path, "../normalizedDepthImage"))

save_path = os.path.join(dir_path, "../normalizedDepthImage")

for i, path in enumerate(paths):
    img = Image.open(path)
    depth = np.asarray(img)
    ra_depth = (depth/np.max(depth)) * 255.0

    depth_pil = Image.fromarray(np.uint8(ra_depth))

    depth_pil.save(os.path.join(save_path, "depth_{0}.png").format(i+1))