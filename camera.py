import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
  i, frame = cap.read()
  frame = cv2.resize(frame, (500, 300))
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
  h = hsv[:, :, 0]
  s = hsv[:, :, 1]
  v = hsv[:, :, 2]

  img = np.zeros(h.shape, dtype=np.uint8)
  # 赤っぽい箇所を白（255）で塗りつぶす
  img[((h < 50) | (h > 200)) & (s > 100)] = 255
  cv2.imshow('OPENCV',img)
  if cv2.waitKey(1) == 13: break

cap.release()
cv2.destoryAllWindow()