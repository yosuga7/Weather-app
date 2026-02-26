# 🌤️ Weather Web App

A simple and beautiful weather web application built with **Flask** and the **Open-Meteo API**. Search for any city in the world and get real-time weather information including temperature, humidity, and wind speed.

---

## ✨ Features

- 🔍 Search weather by city name
- 🌡️ Current temperature, humidity, and wind speed
- 🌙 Day/night detection
- 🎨 Clean, responsive UI
- 🔑 **No API key required** — uses the free Open-Meteo API

---

## 📋 Prerequisites

Make sure you have the following installed on your system:

- **Python 3.8+** — [Download Python](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** — [Download Git](https://git-scm.com/downloads)

---

## 🚀 How to Download & Activate

### Step 1: Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/yosuga7/weather_app.git
cd weather_app
```


### Step 2: Create a Virtual Environment

It's recommended to use a virtual environment to keep dependencies isolated.

**On Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` appear at the beginning of your terminal prompt.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `Flask` — the web framework
- `gunicorn` — production WSGI server

### Step 4: Run the App

```bash
python app.py
```

The app will start on **http://localhost:8080**. Open this URL in your browser.

---

## 🖥️ Usage

1. Open your browser and go to `http://localhost:8080`
2. Type a city name in the search box (e.g., **Hanoi**, **London**, **Tokyo**)
3. View the current weather results!

---

## 📁 Project Structure

```
weather_app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile            # Deployment configuration
├── README.md           # This file
├── static/
│   ├── style.css       # Stylesheets
│   └── script.js       # Frontend JavaScript
└── templates/
    └── index.html      # HTML template
```

---

## 🛑 How to Stop & Deactivate

1. Press `Ctrl + C` in the terminal to stop the server
2. Deactivate the virtual environment:

```bash
deactivate
```

---

## 🌐 API Reference

This app uses the free [Open-Meteo API](https://open-meteo.com/) — no API key or signup required.

---

## 📝 License

This project is open source and free to use.
