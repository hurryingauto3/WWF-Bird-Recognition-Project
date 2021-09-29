import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from os import walk, rename

def find_edges(box):
    """
    Takes coordinates of bounding box and returns edges
    """

    left = box[0]
    right = box[2]
    top = box[1]
    bottom = box[3]

    return [left, right, top, bottom]

def find_box(image):
    """
    given an image, return the bounding box.
    """

    bbox, label, conf = cv.detect_common_objects(image)
    bbox = bbox[::-1]
    label = label[::-1]
    for b, l in zip(bbox, label):
        if l == 'bird':
            box = b
    
    x0, y0, x1, y1 = box

    if abs(x0-x1) < abs(y0-y1):
        dist = abs(y0-y1) - abs(x0-x1)
        dist = dist // 2
        x0 -= dist
        x1 += dist

        x0 = max(x0, 0)
        x1 = min(x1, image.shape[1])
    
    elif abs(x0-x1) > abs(y0-y1):
        dist = abs(x0-x1) - abs(y0-y1)
        dist = dist // 2
        y0 -= dist
        y1 += dist
        
        y0 = max(0, y0)
        y1 = min(y1, image.shape[0])

    box = [x0, y0, x1, y1]
    return box

def make_square_img(crop_img):
    """
    given a cropped image, add paddings to make it square shape
    """

    delta = abs(crop_img.shape[0] - crop_img.shape[1])

    if crop_img.shape[0] > crop_img.shape[1]:
        left = delta//2
        right = delta-left
        crop_img = cv2.copyMakeBorder(crop_img, 0, 0, left, right, cv2.BORDER_CONSTANT)

    elif crop_img.shape[0] < crop_img.shape[1]:
        top = delta // 2
        bottom = delta-top
        crop_img = cv2.copyMakeBorder(crop_img, top, bottom, 0, 0, cv2.BORDER_CONSTANT)
    
    return crop_img

def find_square_box(image):
    """
    given an image, return cropped square image
    """
    box = find_box(image)
    left, right, top, bottom = find_edges(box)

    crop_img = image[top:bottom, left:right]
    
    crop_img = make_square_img(crop_img)

    return crop_img


def get_filenames(path):
    files = [x[2] for x in walk(path)]
    files = files[0]
    return files

def wrapper(files, src, dest):
    for img in files:
        print(img)
        im = cv2.imread(src+img)
        crop_img = find_square_box(im)
        cv2.imwrite(dest + img, crop_img)
        # break

def delete_outliers(files, src):
    """
    check images where birds are not detected by the detector and delete them.
    """
    for img in files:
        # print(img)
        im = cv2.imread(src+img)
        bbox, label, conf = cv.detect_common_objects(im)
        if 'bird' not in label:
            print('delete --> ', label, img)

src1 = 'housecrow\\'
src2 = 'housesparrow\\'
src3 = 'common_myna\\'

dest1 = 'HC\\'
dest2 = 'HS\\'
dest3 = 'CM\\'

files1 = get_filenames(src1)
files1.sort()

files2 = get_filenames(src2)
files2.sort()

files3 = get_filenames(src3)
files3.sort()

# comment out wrapper calls when running delete_outliers. Once outliers are deleted, then comment out delete_outliers and uncomment wrapper
# delete_outliers(files1, src1)
# delete_outliers(files2, src2)
# delete_outliers(files3, src3)

# wrapper(files1, src1, dest1)
# wrapper(files2, src2, dest2)
# wrapper(files3, src3, dest3)
