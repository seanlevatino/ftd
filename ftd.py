# import required libraries
import cv2
import numpy as np
import time
import math
import string

def keyboard_input():
    text = ""
    letters = string.ascii_lowercase + string.digits
    while True:
        key = cv2.waitKey(1)
        for letter in letters:
            if key == ord(letter):
                text = text + letter
        if key == ord("\n") or key == ord("\r"): # Enter Key
            break
    return text
    

def removeMaskRegion(region):
    col = region % 3
    row = math.floor(region//3)
    
    startX = col*(imageWidth//3)
    endX = startX+(imageWidth//3)
    
    startY = row*(imageHeight//3)
    endY = startY+(imageHeight//3)

    #print("region:",region)
    #print("column:",col)
    #print("row:",row)
    #print("startX:",startX)
    #print("startY:",startY)
    #print("endX:",endX)
    #print("endY:",endY)    
    
    return startX, endX, startY, endY
    

# Read an input image as a gray image
img = cv2.imread('testimage.jpg')
imageHeight, imageWidth, channels = img.shape


# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
#mask[100:250, 150:450] = 255

# compute the bitwise AND using the mask
masked_img = cv2.bitwise_and(img,img,mask = mask)


while(1):
    cv2.imshow('Masked Image',masked_img)
    cv2.waitKey(33)
    k = keyboard_input()
    if k.isdigit() and int(k) < 100:
        startX, endX, startY, endY = removeMaskRegion(int(k))
        mask[startY:endY, startX:endX] = 255
        masked_img = cv2.bitwise_and(img,img,mask = mask)
    else:
        break
    
    
cv2.destroyAllWindows()
    
