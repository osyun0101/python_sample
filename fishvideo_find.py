import cv2,os,pickle,copy

with open('fish.pkl', "rb") as fp:
  clf = pickle.load(fp)
img_last = None
cap = cv2.VideoCapture('fish.mp4')
path = './bestshot'
count = 0
frame_count = 0
if not os.path.isdir(path): os.mkdir(path)

while True:
  is_ok, frame = cap.read()
  if not is_ok: break
  frame_count += 1
  frame = cv2.resize(frame, (640, 360))
  frame2 = copy.copy(frame)

  img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  img = cv2.GaussianBlur(img, (7, 7), 0)
  im = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]

  if not img_last is None: 
    frame_diff = cv2.absdiff(img_last, im)
    cnts = cv2.findContours(frame_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]

    fish_count = 0
    for pt in cnts:
      x,y,w,h = cv2.boundingRect(pt)
      if w < 100 or w > 500: continue
      fre = frame[y:y+h, x:x+w]
      fre = cv2.resize(fre, (64, 32))
      imx = fre.reshape(-1, )
      pre_y = clf.predict([imx])
      if pre_y[0] == 1:
        fish_count += 1
        cv2.rectangle(frame2, (x,y),(x+w,y+h),(0,255,0),3)
    if fish_count > 3:
      name = path + '/' + str(count) + ".jpg"
      cv2.imwrite(name, frame)
      count += 1

  cv2.imshow('fishvideo', frame2)
  if cv2.waitKey(1) == 13: break
  img_last = im
cap.release()
cv2.destroyAllWindows()
print('ok', count, "/", frame_count)
