import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('4.png')
# code = decode(img)
# print(code)

# starting attach webcam to scan the code
cap = cv2.VideoCapture(0)
# set width (id,size)
cap.set(3,680)
cap.set(4,480)

while cap.isOpened():
    success, img = cap.read()
    img = cv2.flip(img,1)
    for barcode in decode(img):
        # printing barcode data
        print(barcode.data)
        # this is printing for the sides of size the barcode
        print(barcode.rect)
        # this is for printing the json data
        myData = barcode.data.decode('utf-8')
        print(myData)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2)) 
        cv2.polylines(img,[pts],True,(255,0,255),thickness=1)
        pts2 = barcode.rect
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,0),2)


    # for showing the image
    cv2.imshow('Result',img)
    key = cv2.waitKey(25)
    if key==ord('q'):
        exit()
cap.release()
cv2.destroyAllWindows()
