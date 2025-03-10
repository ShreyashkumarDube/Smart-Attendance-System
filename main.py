import os  # os functions
import check_camera
import capture_image
import train_image
import recognize
import yagmail

def title_bar():
    os.system('cls')
    print("\t***** Face Recognition Attendance System *****")

def mainMenu():
    title_bar()
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Check Camera")
    print("[2] Capture Faces")
    print("[3] Train Images")
    print("[4] Recognize & Attendance")
    print("[5] Quit")
    while True:
        try:
            choice = int(input("Enter Choice: "))
            if choice == 1:
                check_camera.checkCamera()
                key = input("Enter any key to return to the main menu")
                mainMenu()
                break
            elif choice == 2:
                CaptureFaces()
                break
            elif choice == 3:
                Trainimages()
                break
            elif choice == 4:
                recognizeFaces()
                break
            elif choice == 5:
                print("Thank You")
                break
            else:
                print("Invalid Choice. Enter 1-5")
        except ValueError:
            print("Invalid Choice. Enter 1-5\n Try Again")
    exit

# camera test function from check_camera.py file
def checkCamera():
    check_camera.checkCamera()
    key = input("Enter any key to return to the main menu")
    mainMenu()

# image function from capture_image.py file
def CaptureFaces():
    capture_image.takeImages()
    key = input("Enter any key to return to the main menu")
    mainMenu()

# train images from train_image.py file
def Trainimages():
    train_image.TrainImages()
    key = input("Enter any key to return to the main menu")
    mainMenu()

# recognize_attendance from recognize.py file
def recognizeFaces():
    recognize.recognize_attendence()
    key = input("Enter any key to return to the main menu")
    mainMenu()

# main driver
mainMenu()
