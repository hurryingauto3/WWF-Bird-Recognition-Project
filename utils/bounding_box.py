import cv2
import matplotlib.pyplot as plt
import cvlib as cv

def find_edges(box):

    left = box[0]
    right = box[2]
    top = box[1]
    bottom = box[3]

    return [left, right, top, bottom]

def find_box(image):
    bbox, label, conf = cv.detect_common_objects(image)

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
    print(box)
    return box

def make_square_img(crop_img):

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
    box = find_box(im)
    left, right, top, bottom = find_edges(box)

    crop_img = image[top:bottom, left:right]
    print(crop_img.shape)
    
    crop_img = make_square_img(crop_img)
    print(crop_img.shape)
    plt.imshow(crop_img)
    plt.show()


im = cv2.imread('house crow2.jpg')
find_square_box(im)