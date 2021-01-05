import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
  i,frame = video.read()
  frame = cv2.resize(frame, (500, 300))
  cv2.imshow("OPENCV_VIDEO", frame)
  k = cv2.waitKey(1)
  if k == 27 or k == 19: break

video.release()
cv2.destoryAllWindow()
