import cv2
import os
import pandas as pd

def takeImages():
    Id = input("Enter Your Id: ")
    name = input("Enter Your Name: ")
    
    # Ensure the TrainingImage directory exists
    if not os.path.exists("TrainingImage"):
        os.makedirs("TrainingImage")
    
    cam = cv2.VideoCapture(0)
    harcascadePath = "haarcascade_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    sampleNum = 0
    
    try:
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                sampleNum += 1
                cv2.imwrite("TrainingImage" + os.sep + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y+h, x:x+w])
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.imshow('frame', img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum > 60:
                break
    finally:
        cam.release()
        cv2.destroyAllWindows()
    
    print("Images Saved for ID: " + Id + " Name: " + name)
    
    # Append new entry to StudentDetails.csv
    if not os.path.exists("StudentDetails"):
        os.makedirs("StudentDetails")
    
    student_details_path = "StudentDetails" + os.sep + "StudentDetails.csv"
    
    if os.path.exists(student_details_path):
        df = pd.read_csv(student_details_path)
    else:
        df = pd.DataFrame(columns=["Id", "Name"])
    
    new_entry = pd.DataFrame({"Id": [Id], "Name": [name]})
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(student_details_path, index=False)
    print("StudentDetails.csv file updated successfully.")