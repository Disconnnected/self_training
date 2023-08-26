import cv2
import dlib

# read image
img = cv2.imread("python/resource/img/man-alone.jpg")


gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)


face_detector = dlib.get_frontal_face_detector()

faces = face_detector(gray)

for face in faces:
    x1 = face.left()
    y1 = face.top()
    x2 = face.right()
    y2 = face.bottom()

    # draw rectangle
    cv2.rectangle(img=img, pt1 = (x1, y1), pt2 = (x2, y2), color=(0, 255, 0), thickness=5)


cv2.imshow(winname="Face RegconitionAPP", mat=img)

# press any key to close image window. 
cv2.waitKey(delay=0)




