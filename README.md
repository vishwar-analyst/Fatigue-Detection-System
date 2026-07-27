# 🎓 AI-Based Student Fatigue Monitoring and Break Reminder System

> A real-time computer vision application that monitors student fatigue during long study sessions using **Python** and **OpenCV**. The system detects prolonged eye closure through a webcam, issues an audio alert when fatigue is detected, and provides scheduled break reminders to encourage healthy study habits.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-orange?style=for-the-badge)

---

# 📖 Overview

Long hours of continuous studying often lead to eye strain, reduced concentration, and fatigue. This project provides an intelligent solution that continuously monitors the user's eyes through a webcam.

When prolonged eye closure is detected, the application immediately alerts the user with an audio warning. Additionally, it follows the **Pomodoro-inspired** study technique by reminding users to take a break every **25 minutes**.

The project is lightweight, easy to use, and requires only a webcam and Python.

---

# ✨ Key Features

### 👤 Face Detection
- Detects the user's face in real time using Haar Cascade Classifiers.

### 👀 Eye Monitoring
- Continuously monitors both eyes during the study session.

### 😴 Fatigue Detection
- Detects prolonged eye closure over consecutive frames.

### 🔔 Audio Alert
- Plays a warning sound immediately when fatigue is detected.

### ⏱️ Study Timer
- Automatically tracks the duration of the study session.

### ☕ Smart Break Reminder
- Displays a reminder every **25 minutes** encouraging the user to rest.

### 📝 Event Logging
- Stores fatigue and break reminder events with timestamps.

### 💻 Live Monitoring Dashboard
Displays:

- Study Timer
- Number of Eyes Detected
- Closed Eye Frame Counter
- Fatigue Warning
- Break Reminder
- System Status

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming Language |
| OpenCV | Computer Vision |
| Haar Cascade Classifiers | Face & Eye Detection |
| Threading | Background Alert Processing |
| Winsound | Audio Alert |
| Time Module | Timer & Logging |

---

# 📂 Project Structure

```
Student-Fatigue-Monitor/
│
├── fatigue_detector.py        # Main application
├── fatigue_log.txt            # Event log
├── README.md                  # Documentation
└── haarcascade_eye.xml        # Eye detection model
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/student-fatigue-monitor.git
```

## 2️⃣ Navigate to the Project Directory

```bash
cd student-fatigue-monitor
```

## 3️⃣ Install Dependencies

```bash
pip install opencv-python
```

---

# ▶️ Running the Application

Execute the following command:

```bash
python fatigue_detector.py
```

The webcam will automatically open and begin monitoring.

To exit the application:

```
Press Q
```

---

# 🧠 How It Works

```text
Start Application
        │
        ▼
Open Webcam
        │
        ▼
Detect Face
        │
        ▼
Detect Eyes
        │
        ▼
Eyes Detected?
      /      \
    Yes       No
    │          │
Reset Counter  Increase Closed-Eye Counter
               │
               ▼
Counter > Threshold?
      /        \
    No          Yes
    │            │
 Continue    Fatigue Alert
                 │
                 ▼
        Play Alarm Sound
                 │
                 ▼
          Save Event to Log
```

Meanwhile, a background timer continuously tracks study time and displays a break reminder every **25 minutes**.

---

# 📸 Output

The application window displays:

- ✅ Face Detection
- ✅ Eye Detection
- ✅ Study Timer
- ✅ Closed Eye Counter
- ✅ Fatigue Warning
- ✅ Break Reminder
- ✅ Live Monitoring Status

---

# 📝 Sample Log File

Whenever fatigue or a scheduled break is detected, the event is stored inside:

```
fatigue_log.txt
```

Example:

```
Fatigue detected at Sun Jul 26 18:30:45 2026
Scheduled break alert at Sun Jul 26 18:55:00 2026
Fatigue detected at Sun Jul 26 19:12:08 2026
```

---

# 🚀 Future Enhancements

- ✅ MediaPipe Face Mesh Integration
- ✅ Eye Aspect Ratio (EAR) Based Detection
- ✅ Yawn Detection
- ✅ Blink Rate Analysis
- ✅ Head Pose Estimation
- ✅ Machine Learning-Based Fatigue Prediction
- ✅ Streamlit Dashboard
- ✅ Flask Web Application
- ✅ Fatigue Analytics Dashboard
- ✅ Email Notifications
- ✅ Mobile Notifications
- ✅ Multi-user Support
- ✅ Database Integration

---

# 🎯 Applications

- 📚 Student Study Monitoring
- 💻 Computer Workstation Monitoring
- 🎓 Online Learning Platforms
- 👨‍💼 Office Productivity Monitoring
- 👁️ Eye Strain Prevention
- 🧠 Healthy Study Habit Development

---

# 📈 Future Research Scope

This project can be extended into an intelligent fatigue monitoring system by incorporating advanced computer vision and deep learning techniques such as:

- MediaPipe Face Mesh
- Eye Aspect Ratio (EAR)
- Deep Learning-based Eye State Classification
- Drowsiness Detection
- Face Recognition
- Behavioral Analytics
- Cloud-based Monitoring Dashboard

These improvements can significantly increase detection accuracy and usability.

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve this project:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# 👨‍💻 Author

## **Vishwa**

**B.Tech Artificial Intelligence and Data Science**

Passionate about:

- Artificial Intelligence
- Machine Learning
- Computer Vision
- Data Analytics
- Python Development

---

# ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

Your support motivates future improvements and open-source contributions.

---

## 📜 License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute it for educational and research purposes.

---

## 💡 "Study Smart, Stay Healthy."

**Monitor • Detect • Alert • Improve**
