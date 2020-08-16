import cv2

camDevice = cv2.VideoCapture(0) #capture from webcam
result = True
#this loop captures frames continuously
while(result):
    ret,frame = camDevice.read()
    print(ret)
    print(frame)
    cv2.imwrite("NewPicture.jpg",frame) # saving the captured image locally
    result = False # lets stop here. Bcoz we need just one pic.
camDevice.release()
cv2.destroyAllWindows()