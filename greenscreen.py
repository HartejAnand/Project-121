import cv2
import time
import numpy as np

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
output_file=cv2.VideoWriter('image.avi', fourcc, 20.0, (640,480))

for i in range(60):
    ret,bg=cap.read()
bg=np.flip(bg, axis=1)

while(cap.isOpened()):
    ret,img=cap.read()
    if not ret:
        break
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    u_black=np.array([104,153,70])
    i_black=np.array([30,30,0])
    mask_1 = cv2.inRange(hsv, i_black, u_black)
    