import cv2

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left mouse button was pressed at pixel coordinates:', x, y)

image = cv2.imread('img/val_full.png')

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_callback)

while True:
    cv2.imshow('image', image)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
