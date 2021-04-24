import numpy as np
import cv2 as cv
vid=cv.VideoCapture(0)

while(1):
    _, im = vid.read()
    imhsv = cv.cvtColor(im, cv.COLOR_BGR2HSV)

    upper_blue=np.array([120,255,255])
    lower_blue=np.array([90,50,50])

    mask1=cv.inRange(imhsv, lower_blue, upper_blue)
    mask1=cv.medianBlur(mask1, 11)
    ret,thresh1 = cv.threshold(mask1,127,255,cv.THRESH_BINARY)
    contours1, hierarchy = cv.findContours(thresh1, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    upper_red=np.array([180, 255, 255])
    lower_red=np.array([170,100,50])

    mask2=cv.inRange(imhsv, lower_red, upper_red)
    ret,thresh2 = cv.threshold(mask2,127,255,cv.THRESH_BINARY)
    contours2, hierarchy = cv.findContours(thresh2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    for contour1 in contours1 :
        cnt1=contour1
        area=cv.contourArea(cnt1)
        if(area>200) :
            x1,y1,w1,h1 = cv.boundingRect(cnt1)
            cv.rectangle(im,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)
            cv.putText(im, "Blue Color", (x1, y1), cv.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0))
    
    for contour2 in contours2 :
        cnt2=contour2
        x2,y2,w2,h2 = cv.boundingRect(cnt2)
        for contour1 in contours1 :
            cnt1=contour1
            area=cv.contourArea(cnt2)
            if(area>200) :
                x1,y1,w1,h1 = cv.boundingRect(cnt1)

                if (x2>x1 and x2<(x1+w1)) and (y2>y1 and y2<(y1+h1)):
                    cv.rectangle(im,(x2,y2),(x2+w2,y2+h2),(0,0,255),2)
                    cv.putText(im, "Red Color", (x2, y2), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255))

    cv.imshow('res', im)
    cv.imshow('mask1', thresh1)
    cv.imshow('mask2', thresh2)
    k=cv.waitKey(1)
    if k==27:
        break
cv.destroyAllWindows()