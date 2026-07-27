# 🎓 AI-Based Student Fatigue Monitoring and Break Reminder System

A real-time computer vision application developed using **Python** and **OpenCV** to monitor student fatigue during long study sessions. The system detects prolonged eye closure through a webcam, alerts the user with an audio warning, and reminds them to take scheduled breaks to reduce eye strain and improve productivity.

---

## 📌 Features

- 👤 Real-time face detection
- 👀 Eye detection using Haar Cascade Classifiers
- 😴 Fatigue detection based on prolonged eye closure
- 🔔 Audio alert when fatigue is detected
- ⏱️ Automatic 25-minute study timer
- ☕ Scheduled break reminders
- 📝 Logs fatigue and break events with timestamps
- 💻 Live status display with monitoring information

---

## 🛠️ Technologies Used

- Python 3
- OpenCV
- Haar Cascade Classifiers
- Threading
- Winsound
- Time Module

---

## 📂 Project Structure

```
Student-Fatigue-Monitor/
│── fatigue_detector.py
│── fatigue_log.txt
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-fatigue-monitor.git
```

### 2. Navigate to the project folder

```bash
cd student-fatigue-monitor
```

### 3. Install the required package

```bash
pip install opencv-python
```

---

## ▶️ Run the Project

```bash
python fatigue_detector.py
```

The webcam will open and start monitoring your face and eyes.

Press **Q** to quit the application.

---

## 🧠 How It Works

1. Opens the webcam.
2. Detects the user's face.
3. Detects the eyes using Haar Cascade classifiers.
4. Tracks consecutive frames where no eyes are detected.
5. If the eyes remain closed for more than the threshold:
   - Displays a fatigue warning.
   - Plays an audio alert.
   - Saves the event in a log file.
6. Tracks study time and reminds the user to take a break every 25 minutes.

---

## 📸 Output

The application displays:

- Study timer
- Number of detected eyes
- Closed-eye frame count
- Fatigue warning
- Break reminder

---

## 📄 Log File

Whenever fatigue or a scheduled break is detected, an entry is added to:

```
fatigue_log.txt
```

Example:

```
Fatigue detected at Sun Jul 26 18:30:45 2026
Scheduled break alert at Sun Jul 26 18:55:00 2026
```

---

## 🚀 Future Improvements

- MediaPipe Face Mesh integration
- Eye Aspect Ratio (EAR) based fatigue detection
- Yawn detection
- Blink rate analysis
- Streamlit or Flask dashboard
- Fatigue analytics and visualization
- Email or mobile notifications
- Multi-user support

---

## 🎯 Applications

- Student study monitoring
- Online learning
- Computer workstation monitoring
- Productivity enhancement
- Eye strain prevention

---

## 👨‍💻 Author

**Vishwa**

B.Tech Artificial Intelligence and Data Science

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
