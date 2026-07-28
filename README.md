# 🎓 AI-Based Student Fatigue Monitoring and Break Reminder System

A real-time computer vision application that monitors student fatigue during long study sessions using **OpenCV** and **Haar Cascade Classifiers**. The system detects prolonged eye closure through a webcam, issues an audio alert when signs of fatigue are detected, tracks study time, and reminds users to take scheduled breaks to promote healthy study habits.

---

## 📌 Features

- 👤 Real-time face detection
- 👀 Eye detection using Haar Cascade Classifiers
- 😴 Fatigue detection based on prolonged eye closure
- 🔔 Audio alert for fatigue detection
- ⏱️ Live study session timer
- ☕ Automatic break reminders after a configurable interval
- 📝 Automatic logging of fatigue and break events
- 💻 Simple and lightweight implementation using OpenCV

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| OpenCV | Computer Vision |
| Haar Cascade Classifiers | Face & Eye Detection |
| Winsound | Audio Alert |
| Threading | Non-blocking Alert System |
| Time | Session Timer |

---

## 📂 Project Structure

```
AI-Student-Fatigue-Monitor/
│
├── Fatigue_Final.py
├── README.md
├── .gitignore
├── fatigue_log.txt
└── screenshots/
    ├── detection.png
    ├── fatigue_alert.png
    └── study_timer.png
```

## 📋 How It Works

1. Captures live video from the webcam.
2. Detects the user's face using Haar Cascade.
3. Detects eyes within the detected face region.
4. Counts consecutive frames where no eyes are detected.
5. If the threshold is exceeded:
   - Displays a fatigue warning.
   - Plays an audio alert.
   - Records the event in `fatigue_log.txt`.
6. Tracks the total study duration.
7. Displays a break reminder after every 25 minutes.

---

## 📊 Workflow

```
Start Webcam
      │
      ▼
Capture Video Frame
      │
      ▼
Detect Face
      │
      ▼
Detect Eyes
      │
      ├───────────────► Eyes Detected
      │                    │
      │                    ▼
      │             Reset Counter
      │
      ▼
No Eyes Detected
      │
      ▼
Increase Closed-Eye Counter
      │
      ▼
Threshold Reached?
      │
      ├── No ──► Continue Monitoring
      │
      └── Yes
            │
            ▼
 Display Alert
 Play Sound
 Save Log
```

---


## 📁 Log File

Whenever fatigue or a scheduled break is detected, the system automatically stores the event in:

```
fatigue_log.txt
```

## ⚙️ Configuration

You can customize the following parameters inside the code.

| Parameter | Description | Default |
|-----------|-------------|---------|
| `ALERT_FRAMES` | Frames before fatigue alert | 25 |
| `BREAK_INTERVAL` | Break reminder interval | 25 minutes |
| `winsound.Beep()` | Alert sound | 1200 Hz, 700 ms |

---

## 🚀 Future Enhancements

- MediaPipe Face Mesh integration
- Eye Aspect Ratio (EAR) based fatigue detection
- Blink rate analysis
- Yawning detection
- Head pose estimation
- Deep Learning-based fatigue detection
- Email/SMS notifications
- Daily productivity dashboard
- Fatigue analytics using graphs
- Mobile application integration

---

## 💡 Applications

- Student study monitoring
- Online learning platforms
- E-learning systems
- Remote education
- Office workstation monitoring
- Driver alert systems (with modifications)

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Vishwa**

**B.Tech Artificial Intelligence and Data Science**

Erode Sengunthar Engineering College (Autonomous)

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
