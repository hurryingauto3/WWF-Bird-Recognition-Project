# IMPORTS
import os

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
import math

print(torch.__version__)
plt.ion()   # interactive mode

# Activate the path that fits your system when working 
PICTURE_DIR = "C:\\Users\\Ali Hamza\\OneDrive - Habib University\\Khidmat-Image-Dataset"
# PICTURE_DIR = "C:\Users\Ali Hamza\OneDrive - Habib University\Khidmat-Image-Dataset"
# PICTURE_DIR = "C:\Users\Ali Hamza\OneDrive - Habib University\Khidmat-Image-Dataset"

train_hsparrows = f'{PICTURE_DIR}\\crop_housesparrow'
train_common_myna = f'{PICTURE_DIR}\\crop_common_myna'
train_hcrow = f'{PICTURE_DIR}\\crop_housecrow'

val_hsparrows = f'{PICTURE_DIR}\\crop_housesparrow'
val_common_myna = f'{PICTURE_DIR}\\crop_common_myna'
val_hcrow = f'{PICTURE_DIR}\\crop_housecrow'

### FOR USE WITH LINUX
# train_hsparrows = f'{PICTURE_DIR}/crop_housesparrow'
# train_common_myna = f'{PICTURE_DIR}/crop_common_myna'
# train_hcrow = f'{PICTURE_DIR}/crop_housecrow'

# val_hsparrows = f'{PICTURE_DIR}/crop_housesparrow'
# val_common_myna = f'{PICTURE_DIR}/crop_common_myna'
# val_hcrow = f'{PICTURE_DIR}/crop_housecrow'

