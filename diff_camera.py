import cv2

cap = cv2.VideoCapture(0)
img_last = None
green = (0, 255 ,0)

while True:
  i,frame = cap.read()
  frame = cv2.resize(frame, (500, 300))

  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gray = cv2.GaussianBlur(gray, (9,9),0)
  gray = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]

  if img_last is None:
    img_last = gray
    continue
  
  frame_diff = cv2.absdiff(img_last, gray)
  cnts = cv2.findContours(frame_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
  
  for pt in cnts:
    x,y,w,h = cv2.boundingRect(pt)
    if w < 30: continue
    cv2.rectangle(frame, (x,y),(x+w, y+h), green, 3)
  
  img_last = gray

  cv2.imshow('CAMERA',frame)
  cv2.imshow('NEKO',frame_diff)
  if cv2.waitKey(1) == 13: break

cap.release()
cv2.destoryAllWindows()  
