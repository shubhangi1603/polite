import cv2

cap = cv2.VideoCapture(0)

# Load the Classifier
face_classifier = cv2.CascadeClassifier('face_cascade.xml')



while True:


    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    if ret:
        

        faceList = face_classifier.detectMultiScale(gray, scaleFactor=1.1)

        for (x, y, w, h) in faceList:
            cv2.rectangle(frame, (x, y), ( x+w, y+h ), (255, 0, 0), 2)

        cv2.imshow('my webcam', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    else:
        break
cv2.destroyAllWindows()
cap.release()
