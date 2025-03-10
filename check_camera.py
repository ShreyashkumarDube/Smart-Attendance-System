import cv2

def checkCamera():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not open camera.")
        return

    print("Press 'q' to quit the camera check.")
    try:
        while True:
            ret, frame = cam.read()
            if not ret:
                print("Failed to grab frame")
                break
            cv2.imshow('Camera Check', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("Camera check interrupted.")
    finally:
        cam.release()
        cv2.destroyAllWindows()
        print("Camera released and windows closed.")