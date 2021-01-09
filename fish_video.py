import cv2, os

cap = cv2.VideoCapture('fish.mp4')
img_last = None
fish = "./fishrsfile"
os.mkdir(fish)
n = 0

while True:
  i, frame = cap.read()
  if not i : break
  frame = cv2.resize(frame, (640, 360))
  
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  gray = cv2.GaussianBlur(gray, (15,15), 0)
  img_r = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]

  if not img_last is None: 
    frame_diff = cv2.absdiff(img_last, img_r)
    cnts = cv2.findContours(frame_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

    for pt in cnts:
      x,y,w,h = cv2.boundingRect(pt)
      if w < 100 or w > 500: continue
      imagex = frame[y:y+h, x:x+w]
      name = fish + '/' + str(n) + '.jpg'
      cv2.imwrite(name, imagex)
      n += 1
    
  img_last = img_r
cap.release()
print("ok")