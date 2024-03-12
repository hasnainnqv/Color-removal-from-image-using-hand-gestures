import math

import cv2
import time
import numpy as np
import pycaw
import handgesture as htm
wCam, hcam = 640,480


detector = htm.HandDetector(detectionCon=0.7)

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hcam)
grow,grow1,grow2,grow3,grow4,grow5 = 50,50,50,350,350,350
US = 0
LS = 0
LV=0
LH = 0
UV= 0
UH=0

background = cv2.imread('F:\\PycharmProjects\\vs_code_projects\\project1\\ela_modified.jpg')

while True:
    background = cv2.imread('F:\\PycharmProjects\\vs_code_projects\\project1\\ela_modified.jpg')

    success, img = cap.read()
    # img = image
    img = detector.findHands(img,draw=False)
    overlay = img.copy()
    hsv = cv2.cvtColor(background, cv2.COLOR_BGR2HSV)

    l_b = np.array([LH, LV, LS])
    u_b = np.array([UH, US, UV])
    mask = cv2.inRange(hsv, l_b, u_b)
    res = cv2.bitwise_and(background, background, mask=mask)

    lmlist =  detector.findPosition(img,draw = False)
    if len(lmlist) != 0:
        x1,y1 = lmlist[8][1],lmlist[8][2]

        cv2.circle(img,(x1,y1), 10,(255,255,255),cv2.FILLED)
        if (50<x1<300 and 50<y1<75):
            grow = int(x1)
            US = int(np.interp(x1+2 , [50, 300], [0, 255]))
            print('US',US)

        if (50<x1<300 and 150<y1<175):
            grow1 = int(x1)
            UV = int(np.interp(x1+2, [50, 300], [0, 255]))
            print('uv',UV)

        if (50<x1<300 and 250<y1<275):
            grow2 = int(x1)
            UH = int(np.interp(x1+2, [50, 300], [0, 255]))
            print('UH',UH)
        if (350<x1<600 and 50<y1<75):
            grow3 = int(x1)
            LS = int(np.interp(x1+2, [350, 600], [0, 255]))
            print('LS',LS)
        if (350<x1<600 and 150<y1<175):
            LV = int(np.interp(x1+2, [350, 600], [0, 255]))
            grow4 = int(x1)
            print('LV',LV)
        if (350<x1<600 and 250<y1<275):
            grow5 = int(x1)
            LH = int(np.interp(x1+2, [350, 600], [0, 255]))

            print('lH',LH)


    thickness = 3
    color = (11,223,24)
    cv2.putText(img, f"US: {int(US)}", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, thickness)
    cv2.rectangle(img, (50, 50), (int(grow), 75), color, cv2.FILLED)

    cv2.putText(img, f"UV: {int(UV)}", (50, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, color, thickness)
    cv2.rectangle(img, (50, 150), (int(grow1), 175), color, cv2.FILLED)

    cv2.putText(img, f"UH: {int(UH)}", (50,240), cv2.FONT_HERSHEY_SIMPLEX, 1, color, thickness)
    cv2.rectangle(img, (50, 250), (int(grow2), 275), color, cv2.FILLED)

    cv2.putText(img, f"LS: {int(LS)}", (350, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, color, thickness)
    cv2.rectangle(img, (350, 50), (int(grow3), 75), color, cv2.FILLED)

    cv2.putText(img, f"LV: {int(LH)}", (350, 140), cv2.FONT_HERSHEY_SIMPLEX, 1, color, thickness)
    cv2.rectangle(img, (350, 150), (int(grow4), 175), color, cv2.FILLED)

    cv2.putText(img, f"LH: {int(LV)}", (350, 240), cv2.FONT_HERSHEY_SIMPLEX, 1, color,thickness)
    cv2.rectangle(img, (350, 250), (int(grow5), 275), color, cv2.FILLED)



    black = (0,0,0)
    cv2.rectangle(img, (50, 50), (300, 75), black, 3)
    cv2.rectangle(img, (50, 150), (300, 175), black, 3)
    cv2.rectangle(img, (50, 250), (300, 275), black, 3)
    cv2.rectangle(img, (350, 50), (600, 75), black, 3)
    cv2.rectangle(img, (350, 150), (600, 175), black, 3)
    cv2.rectangle(img, (350, 250), (600, 275), black, 3)


    cv2.imshow('RES', res)
    cv2.imshow('mask', mask)

    cv2.imshow('img',img)
    cv2.waitKey(1)