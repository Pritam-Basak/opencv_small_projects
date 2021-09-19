import cv2
import numpy as np

def callback(x):
	pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('image')

ilowH = 0
ihighH = 179

ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

cv2.createTrackbar('lowH','image',ilowH,179,callback)
cv2.createTrackbar('highH','image',ihighH,179,callback)
cv2.createTrackbar('lowS','image',ilowS,255,callback)
cv2.createTrackbar('highS','image',ihighS,255,callback)
cv2.createTrackbar('lowV','image',ilowV,255,callback)
cv2.createTrackbar('highV','image',ihighV,255,callback)

while True:
	 ret, frame = cap.read()
	 hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	 cv2.imshow('hsv', hsv)
	 lower_hsv = np.array([ilowH, ilowS, ilowV])
	 higher_hsv = np.array([ihighH, ihighS, ihighV])
	 mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
	 cv2.imshow('mask', mask)
	 cv2.imshow('frame', frame)
	 if(cv2.waitKey(1) & 0xFF == ord('q')):
	 	break

cv2.destroyAllWindows()
cap.release()