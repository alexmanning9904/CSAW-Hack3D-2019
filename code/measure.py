#!/usr/bin/python3
import cv2
import numpy as np

def measure(filepath):
    mat = cv2.imread(filepath)  #Load image from filepath
    height, width, _ = mat.shape  #Load total image size
    sizes = []  #Initialize list for sizes
    for i in range(height):
        left, right = 0, width-1  #Set caliper jaws to first and last pixel
        while(True):
            if(left>=right):
                break  #No object in layer
            if(np.all(mat[height-i-1][left]==[255,255,255])):
                left += 1  #Move left Jaw
            elif(np.all(mat[height-i-1][right]==[255,255,255])):
                right -= 1  #Move right Jaw
            else:
                sizes.append(right-left+1)  #Layer measurement complete
                break
    return sizes