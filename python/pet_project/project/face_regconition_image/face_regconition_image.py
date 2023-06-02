import cv2
import dlib

# read image
img = cv2.imread("python/resource/img/man-alone.jpg")


gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)


face_detector = dlib.get_frontal_face_detector()





cv2.imshow(winname="Face RegconitionAPP", mat=gray)

# press any key to close image window. 
cv2.waitKey(delay=0)




