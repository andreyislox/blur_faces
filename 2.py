

# importing libraries
import cv2
import numpy as np

def blur_fase(img):
    (h, w) = img.shape[:2]
    dW = int(w / 3.0)
    dH = int(h / 3.0)
    if dW % 2 == 0:
        dW -= 1
    if dH % 2 == 0:
        dH -= 1

    return cv2.GaussianBlur(img, (dW, dH), 0)

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video file")

    # Read until video is completed
while (cap.isOpened()):

    # Capture frame-by-frame
    ret, img = cap.read()

    faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20, 20))
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        img[y:y + h, x:x + w] = blur_fase(img[y:y + h, x:x + w])

    if ret == True:
        # Display the resulting frame
        cv2.imshow('andrey is lox', img)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
