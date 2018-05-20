#coding: 'utf-8'

"""
eigen14_DepthEstimation
dataset

created by Kazunari on 2018/05/21 
"""

import tensorflow as tf
from tensorflow.python.platform import gfile
import numpy as np
from PIL import Image

IMAGE_HEIGHT = 228
IMAGE_WIDTH = 304
TARGET_HEIGHT = 55
TARGET_WIDTH = 74

class Dataset:
    def __init__(self, train_csv, val_csv, test_csv):
        self.train_list = None
        self.val_list = None
        self.test_list = None

        with open(train_csv,"r") as f:


    def get_training_data(self, csv_file_path):
        with open(csv_file_path, "r") as f:
            self.train_list = f.readlines()