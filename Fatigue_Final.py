import cv2
import time
import threading
import winsound
print(cv2.__version__)
# ---------- SOUND ALERT ----------
def alert_sound():
    winsound.Beep(1200, 700)   # frequency, duration(ms)

# ---------- LOAD CASCADES ----------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')

# ---------- CAMERA ----------
cap = cv2.VideoCapture(0)

eye_closed_frames = 0
ALERT_FRAMES = 25

# ---------- STUDY TIMER ----------
start_time = time.time()
BREAK_INTERVAL = 25 * 60   # 25 minutes

print("Fatigue detector started — press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    eyes_found = 0

    # ---------- FACE & EYE DETECTION ----------
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 4)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 2)
            eyes_found += 1

    # ---------- FATIGUE LOGIC ----------
    if eyes_found == 0:
        eye_closed_frames += 1
    else:
        eye_closed_frames = 0

    # ---------- FATIGUE ALERT ----------
    if eye_closed_frames > ALERT_FRAMES:
        cv2.putText(frame, "SLEEPY — TAKE BREAK!", (40,80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

        threading.Thread(target=alert_sound).start()

        with open("fatigue_log.txt", "a") as f:
            f.write(f"Fatigue detected at {time.ctime()}\n")

        eye_closed_frames = 0

    # ---------- STUDY TIMER ----------
    elapsed = int(time.time() - start_time)
    minutes = elapsed // 60
    seconds = elapsed % 60

    cv2.putText(frame, f"Study Time: {minutes:02}:{seconds:02}",
                (10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0), 2)

    # ---------- BREAK REMINDER ----------
    if elapsed > BREAK_INTERVAL:
        cv2.putText(frame, "Planned Break Time!", (40,130),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)

        threading.Thread(target=alert_sound).start()

        with open("fatigue_log.txt", "a") as f:
            f.write(f"Scheduled break alert at {time.ctime()}\n")

        start_time = time.time()

    # ---------- STATUS DISPLAY ----------
    cv2.putText(frame, f"Eyes detected: {eyes_found}",
                (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.putText(frame, f"Closed frames: {eye_closed_frames}",
                (10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    cv2.imshow("Student Fatigue Monitor", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
