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
          
# Loading cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 144)

# Recording state and video writer
is_recording = False
video_writer = None
recording_number = 1
screenshot_number = 1

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

        # Showing recording indicator
        if is_recording:
            cv2.circle(frame, (30, 80), 10, (0, 0, 255), -1)  # Red dot
            cv2.putText(frame, "REC", (50, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

def start_recording():
    global is_recording, video_writer, recording_number
    
    if not is_recording:
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        os.makedirs("recordings", exist_ok=True)
        filename = f"recordings/recording_{recording_number}.mp4"
        
        # MP4 format - works on Mac, Windows, everywheree
        codec = cv2.VideoWriter_fourcc(*"mp4v")
        video_writer = cv2.VideoWriter(filename, codec, 20.0, (frame_width, frame_height))
        
        is_recording = True
        print(f"Recording started: {filename}")
        recording_number += 1
    else:
        # Stop recording
        is_recording = False
        if video_writer is not None:
            video_writer.release() # stops video rec
            video_writer = None
        print("Recording stopped!")

def main():
    global is_recording, video_writer, screenshot_number
    is_paused = False
    frame = None  # Store current frame
    
    while True:
            # keys configuration
            key = cv2.waitKey(1) & 0xFF

            if key == ord(EXIT):
                print("Exiting...")
                break

            elif key == ord(PAUSE):
                is_paused = not is_paused
                if is_paused:
                    print("PAUSED. Press 'p' to resume.")
                else:
                    print("RESUMED.")

            elif key == ord(RECORD) and not is_paused:
                start_recording()

            elif key == ord(SCREENSHOT) and frame is not None:
                os.makedirs("screenshots", exist_ok=True)
                cv2.imwrite(f"screenshots/screenshot_{screenshot_number}.jpg", frame)
                print("Screenshot saved!")
                screenshot_number += 1

            # Only process new frames when NOT paused
            if not is_paused:
                ret, frame = cap.read()
                if not ret:
                    print("Error capturing frame.")
                    break

                detection(frame)
                
                if is_recording and video_writer is not None:
                    video_writer.write(frame)

            # Always show current frame (paused or not)
            if frame is not None:
                cv2.imshow("Webcam Feed", frame)
    
    # Cleanup recording
    if is_recording and video_writer is not None:
        video_writer.release()

if __name__ == "__main__":
    main()
    cap.release()
    cv2.destroyAllWindows()
