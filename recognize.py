import os
import pandas as pd
import cv2
import numpy as np
import time
from datetime import datetime

def recognize_attendence():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("TrainingImageLabel" + os.sep + "Trainner.yml")
    harcascadePath = "haarcascade_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("StudentDetails" + os.sep + "StudentDetails.csv")
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)

    # Ensure the Attendance directory exists
    if not os.path.exists("Attendance"):
        os.makedirs("Attendance")

    # Ensure the ImagesUnknown directory exists
    if not os.path.exists("ImagesUnknown"):
        os.makedirs("ImagesUnknown")

    # start realtime video capture
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)  # set video frame width
    cam.set(4, 480)  # set video frame height

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )

        for (x, y, w, h) in faces:
            Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

            if confidence < 100:
                if not df[df['Id'] == Id].empty:
                    aa = df.loc[df['Id'] == Id]['Name'].values[0]
                    tt = str(Id) + "-" + aa
                    confidence_display = "  {0}%".format(round(100 - confidence))
                    ts = time.time()
                    date = datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
                else:
                    Id = 'Unknown'
                    tt = str(Id)
                    confidence_display = "  {0}%".format(round(100 - confidence))
            else:
                Id = 'Unknown'
                tt = str(Id)
                confidence_display = "  {0}%".format(round(100 - confidence))

            if (100 - confidence) > 50:
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown" + os.sep + "Image" + str(noOfFile) + ".jpg", img[y:y + h, x:x + w])

            cv2.putText(
                img,
                str(tt),
                (x + 5, y - 5),
                font,
                1,
                (255, 255, 255),
                2
            )
            cv2.putText(
                img,
                str(confidence_display),
                (x + 5, y + h - 5),
                font,
                1,
                (255, 255, 0),
                1
            )
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('Attendance', img)

        if cv2.waitKey(1) == ord('q'):
            break

    ts = time.time()
    date = datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "Attendance" + os.sep + "Attendance_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    print(f"Attendance saved to {fileName}")

    cam.release()
    cv2.destroyAllWindows()
