import cv2
# 画像を読み込む
img = cv2.imread("346-1.jpg")
# グレースケールに変換
gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
#画像をリサイズ
resized = cv2.resize(img, (1066,200))
# 結果を出力
cv2.imshow("gray", gray)
cv2.imshow("resize", resized)
while True:
    # Escキーを入力したら終了
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()