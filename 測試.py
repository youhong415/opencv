# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:16:43 2020

@author: bbjac
"""

import cv2
#read video
cap = cv2.VideoCapture('C:\\Users\\bbjac\\Git\\opencv\\around.mp4')


#define mask position
upper_left = (280, 100)
bottom_right = (980, 600)


#define mask
def sketch_transform(image):
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_grayscale_blurred = cv2.GaussianBlur(image_grayscale, (7,7), 0)
    image_canny = cv2.Canny(image_grayscale_blurred, 10, 80)
    _, mask = image_canny_inverted = cv2.threshold(image_canny, 30, 255, cv2.THRESH_BINARY_INV)
    return mask



while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #Rectangle marker
        r = cv2.rectangle(frame, upper_left, bottom_right, (100, 50, 200), 5)
        rect_img = frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]
    
        sketcher_rect = rect_img
        sketcher_rect = sketch_transform(rect_img)
        
        #Conversion for 3 channels to put back on original image (streaming)
        sketcher_rect_rgb = cv2.cvtColor(sketcher_rect, cv2.COLOR_GRAY2RGB)
    
        #Replacing the sketched image on Region of Interest
        frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = sketcher_rect_rgb
        
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()