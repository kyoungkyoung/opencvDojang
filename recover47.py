import numpy as np
import cv2

img = np.full((400,400,3), 255, np.uint8)

#text
text = "Hello opencv"
font = cv2.FONT_HERSHEY_SIMPLEX
fontSize = 1
blueColor = (255,0,0)
thick = 2
lineType = cv2.LINE_4
cv2.putText(img, text, (50,350), font, fontSize, blueColor, thick, lineType)


# line
pt1 = (50,100)
pt2 = (img.shape[0]-50, 100)
pt3 = (img.shape[0]-50, 300)
pt4 = (200,300)
lineColor = (0,0,0)
lineThick = 3
lineType = cv2.LINE_8
cv2.line(img, pt1, pt2, lineColor, lineThick, lineType)
cv2.line(img, pt1, pt3, lineColor, lineThick, cv2.LINE_AA)


# rectangle : (x1,y1) (x2,y2)
cv2.rectangle(img, pt1, pt4, (0,0,255), lineThick)

# rectangle : x,y,w,h
cv2.rectangle(img, (50,100,100,100), (0,255,0), thick, lineType)


# circle
cv2.circle(img, (int(img.shape[0]/2), int(img.shape[1]/2)), 100, (0,255,255), 2, cv2.LINE_AA)


cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()