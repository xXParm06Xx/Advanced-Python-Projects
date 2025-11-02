import cv2
import os
import configparser

config = configparser.ConfigParser()

try:
    config.read('config.ini')
    if "KEYS" in config:
        EXIT = config["KEYS"]["exit"]
        SCREENSHOT = config["KEYS"]["screenshot"]
        PAUSE = config["KEYS"]["pause"]
        RECORD = config["KEYS"]["record"]
    else:
        # default keys
        EXIT = "q"
        SCREENSHOT = "s"
        PAUSE = "p"
        RECORD = "r"  
except:
    # default keys
    EXIT = "q"
    SCREENSHOT = "s"
    PAUSE = "p"
    RECORD = "r"
          
# Load cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 144)

def detection(frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, "Face", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            # region of interest (RxC (width x height))
            roi_gray = gray[y:y+h, x:x+w]
            
            # for smile (lower half of face)
            roi_gray_lower = roi_gray[int(h/2):, :]

            # Detect eyes
            eyes = eyes_cascade.detectMultiScale(roi_gray, 1.1, 10)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 0, 255), 2)
                cv2.putText(frame, "Eye", (x + ex, y + ey - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

            # Detect smile
            smiles = smile_cascade.detectMultiScale(roi_gray_lower, 1.5, 20)
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(frame, (x + sx, y + sy + int(h/2)), (x + sx + sw, y + sy + sh + int(h/2)), (255, 0, 0), 2)
                cv2.putText(frame, "Smile", (x + sx, y + sy + int(h/2) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

        fps = int(cap.get(cv2.CAP_PROP_FPS))
        cv2.putText(frame, f"FPS: {fps}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 255, 50), 2)

def main():
    while True:
            ret, frame = cap.read()
            if not ret:
                print("Error capturing frame.")
                break

            detection(frame)

            cv2.imshow("Webcam Feed", frame)
            
            # keys configuration
            key = cv2.waitKey(1) & 0xFF

            if key == ord(str(EXIT)):
                print("Exiting...")
                break

            elif key == ord(str(SCREENSHOT)):
                os.makedirs("screenshots", exist_ok=True)
                cv2.imwrite("screenshots/screenshot.jpg", frame)
                print("Screenshot saved!")

if __name__ == "__main__":
    main()
    cap.release()
    cv2.destroyAllWindows()
