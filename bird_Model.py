#Dataset_imports
from torch.utils.data.dataloader import DataLoader
import bird_Model_init as bm

# IMPORTS
import os
import time
import copy
import math
import torch
import torchvision
import numpy as np
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from torch.optim import lr_scheduler
from torchvision import datasets, models, transforms
from torchvision.datasets import ImageFolder
from sklearn.model_selection import train_test_split
from torch.utils.data import Dataset
from PIL import Image

dataset = ImageFolder(bm.PICTURE_DIR)
trainData, testData, trainLabel, testLabel = train_test_split(dataset.imgs, dataset.targets, test_size=0.2, random_state=0)
transform = transforms.Compose(
    [
        transforms.Resize((200, 200)),
        transforms.ToTensor(),
        transforms.Normalize([0.5]*3, [0.5]*3)
    ]
)
# print(trainData)
# print(testData)
# print(trainLabel)
# print(testLabel)

class ImageLoader(Dataset):
    def __init__(self, dataset, transform = None):
        self.dataset = self.checkChannel(dataset)
        self.transform = transform

    def __getitem__(self, item):
        image = Image.open(self.dataset[item][0])
        if transform != None:
            return self.transform (image), self.dataset[item][1]
        return image, self.dataset[item][1]

    def __len__(self):
        return len(self.dataset)

    def checkChannel(self, dataset):
        datasetRGB = []
        for index in range(len(dataset)):
            # print(Image.open(dataset[index][0]).getbands())
            if Image.open(dataset[index][0]).getbands() == ('R','G','B'):
                datasetRGB.append(dataset[index])
        return datasetRGB

    

imgldr = ImageLoader(trainData, transform)
dtaldr = DataLoader(imgldr, batch_size=10, shuffle=True)
data = iter(dtaldr)
d = next(data)
 
