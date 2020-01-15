# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 21:16:43 2020

@author: bbjac
"""

import cv2
#讀video
cap = cv2.VideoCapture('C:\\Users\\bbjac\\Git\\opencv\\around.mp4')

#取得第1000幀，並顯示
cap.set(cv2.CAP_PROP_POS_FRAMES,1000)
a,b = cap.read()
cv2.imshow('b',b)
cv2.waitKey(1000)

#設定ROI框的參數
upper_left = (280,100)
bottom_right = (980,600)

#單純想看總FRAME數
total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(total_frame)


#一種filter方式
def sketch_transform(image):
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_grayscale_blurred = cv2.GaussianBlur(image_grayscale, (7,7), 0)
    image_canny = cv2.Canny(image_grayscale_blurred, 10, 80)
    _, mask = image_canny_inverted = cv2.threshold(image_canny, 30, 255, cv2.THRESH_BINARY_INV)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    return mask



while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #Rectangle marker
        r = cv2.rectangle(frame, upper_left, bottom_right, (100, 50, 200), 2) # retangle參數:(frame,(左上座標),(右下座標),框的顏色,框的厚度)
        rect_img = frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] #frame的大小

        sketcher_rect = sketch_transform(rect_img)
        cv2.imshow('sketcher_rect',sketcher_rect)
    
        #Replacing the sketched image on Region of Interest
        frame[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]] = sketcher_rect
        
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

#https://blog.gtwang.org/programming/opencv-motion-detection-and-tracking-tutorial/
#https://blog.csdn.net/sinat_41104353/article/details/85171185
#https://blog.csdn.net/keith_bb/article/details/53470170