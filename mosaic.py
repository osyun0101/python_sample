import cv2


def mosaic(img, rect, size):
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    cut = img[y1:y2, x1:x2]
    res = cv2.resize(cut, ( size, size))
    res2 = cv2.resize(res, (w, h),interpolation=cv2.INTER_AREA)
    im = img.copy()
    im[y1:y2, x1:x2] = res2
    return res2