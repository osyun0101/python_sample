import cv2,os,pickle,copy

img_last = None
cap = cv2.VideoCapture('fish.mp4')

while True:
  is_ok, frame = cap.read()
  if not is_ok: break
  frame = cv2.resize(frame, (640, 360))
  frame2 = copy.copy(frame)

  img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  img = cv2.GaussianBlur(img, (7, 7), 0)
  im = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

  if not img_last is None: continue
  frame_diff = cv2.absdiff(img_last, im)
  cnts = cv2.findContours(frame_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

  for pt in cnts:
    fre = cv2.boudingRect(pt)
    
