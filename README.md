# 🌬️ AQI Pulse

<div align="center">

![AQI Pulse](https://img.shields.io/badge/AQI-Pulse-7fff00?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Phase](https://img.shields.io/badge/Phase-2-blue?style=for-the-badge)

**Real-Time Intelligence for the Air You Breathe**

*Advanced PM2.5 forecasting and AQI monitoring powered by deep learning and predictive analytics*

[Features](#-features) • [Quick Start](#-quick-start) • [API Docs](#-api-documentation) • [Roadmap](#-project-roadmap)

</div>

---

## 🎯 What is AQI Pulse?

**AQI Pulse** is an intelligent air quality monitoring and forecasting platform that provides real-time AQI insights and 72-hour PM2.5 predictions. Built with production-grade engineering practices, it transforms complex air quality data into actionable health insights.

### Why AQI Pulse?

- ⚡ **Real-Time Monitoring** — Live PM2.5 and AQI tracking
- 🔮 **Predictive Analytics** — 24-72 hour forecasts using LSTM neural networks
- 🎯 **Health-Focused** — CPCB-compliant AQI categories with health advisories
- 🚀 **Production-Ready** — Clean architecture, scalable design, API-first approach
- 🌍 **Smart City Ready** — Multi-city, multi-station capability (upcoming)

---

## ✨ Features

### Current (Phase 2)
- 🧠 **LSTM-Based PM2.5 Forecasting**
  - Hourly predictions for next 24/48/72 hours
  - Pre-trained deep learning model
  - Normalized data processing with saved scaler

- 📊 **CPCB AQI Conversion**
  - Rule-based PM2.5 → AQI transformation
  - Official CPCB breakpoints and linear interpolation
  - Six-category classification (Good to Severe)

- 🔌 **FastAPI Backend**
  - RESTful API endpoints
  - Clean separation of concerns
  - Auto-generated API documentation
  - Production-ready architecture

- 🎨 **Stunning Visual Interface**
  - Immersive 3D animated background
  - Real-time data cards with glassmorphism
  - Responsive design for all devices
  - Dynamic health implications display

---

## 🏗️ Architecture

### 🎨 Frontend Layer (Dashboard)
- 3D Animated Background (Three.js)
- Real-time Data Cards
- Health Advisory Display

### 🔌 API Layer (FastAPI)
- `/forecast/` - Get PM2.5 & AQI predictions
- `/docs` - Interactive API documentation
- CORS & Middleware

### ⚙️ Service Layer
- Forecast Service (Model Loading & Prediction)
- AQI Conversion Service (CPCB Rules)

### 🧠 ML Model Layer
- LSTM Model (`stageA_pm25_lstm_72hr.h5`)
- Scaler (`stageA_pm25_scaler.pkl`)

---

## 📁 Project Structure

```
aqi-pulse/
│
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── routes/
│   │   └── forecast.py         # API endpoint definitions
│   ├── services/
│   │   └── forecast_service.py # Model inference logic
│   └── core/
│       └── config.py           # Configuration management
│
├── models/
│   ├── stageA_pm25_lstm_72hr.h5  # Pre-trained LSTM model
│   └── stageA_pm25_scaler.pkl    # Data normalization scaler
│
├── aqi_rules/
│   └── cpcb_rules.py           # CPCB AQI conversion logic
│
├── frontend/
│   └── index.html              # Dashboard interface
│
├── data/
│   ├── raw/                    # Raw sensor data
│   └── processed/              # Cleaned datasets
│
├── notebooks/                  # Training experiments
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- Modern web browser

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/aqi-pulse.git
cd aqi-pulse
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Start the backend server**
```bash
uvicorn app.main:app --reload
```

4. **Open the dashboard**
```bash
# Open frontend/index.html in your browser
# Or serve it using:
python -m http.server 8080
```

5. **Access the application**
- Dashboard: `http://localhost:8080`
- API Docs: `http://127.0.0.1:8000/docs`

---

## 📡 API Documentation

### Get Air Quality Forecast

**Endpoint:** `GET /forecast/`

**Response:**
```json
[
  {
    "datetime": "2026-01-15 14:00",
    "pm25": 82.4,
    "aqi": 165,
    "category": "Poor"
  },
  {
    "datetime": "2026-01-15 15:00",
    "pm25": 78.1,
    "aqi": 158,
    "category": "Poor"
  }
]
```

### AQI Categories (CPCB Standards)

| AQI Range | Category | Health Implications |
|-----------|----------|---------------------|
| 0-50 | Good | Minimal impact |
| 51-100 | Moderate | Acceptable for most |
| 101-150 | Poor | Sensitive groups affected |
| 151-200 | Unhealthy | General public affected |
| 201-300 | Very Unhealthy | Health alert |
| 301+ | Severe | Health warning |

---

## 🛣️ Project Roadmap

### ✅ Phase 1: Foundation
- Historical data collection and preprocessing
- Exploratory data analysis
- Feature engineering

### 🔄 Phase 2: Core Forecasting (Current)
- ✅ LSTM model training and validation
- ✅ Model deployment infrastructure
- ✅ FastAPI backend development
- ✅ AQI rule-based conversion
- ✅ Interactive dashboard with 3D visuals

### 🔜 Phase 3: Advanced Analytics (Q2 2026)
- Historical trend analysis
- Enhanced health advisory engine
- User-group specific recommendations
- Time-series visualization components
- Power BI integration

### 🔜 Phase 4: Multi-City Scaling (Q3 2026)
- Multi-station support
- City selector interface
- Geographic visualization (maps)
- Station metadata management
- Comparative analysis tools

### 🔜 Phase 5: Multi-Pollutant Inference (Q4 2026)
- PM10, NO₂, SO₂, CO, O₃ integration
- Tree-based regression models
- Fallback prediction mechanism
- Comprehensive air quality profiles

---

## 🧠 Technology Stack

### Backend
- **FastAPI** — Modern, fast web framework
- **TensorFlow/Keras** — Deep learning model
- **NumPy & Pandas** — Data processing
- **scikit-learn** — Data normalization

### Frontend
- **Three.js** — 3D graphics and animations
- **GSAP** — Advanced animations
- **Vanilla JavaScript** — Core functionality
- **CSS3** — Modern styling with glassmorphism

### ML/AI
- **LSTM Networks** — Time series forecasting
- **Sequential Models** — Deep learning architecture
- **MinMaxScaler** — Data normalization

---

## 🎨 Design Philosophy

AQI Pulse follows a modern, tech-forward design approach:

- **Immersive Experience** — 3D animated backgrounds that respond to data
- **Glassmorphism** — Translucent cards with backdrop blur
- **Green Tech Aesthetic** — Neon green (#7fff00) representing clean energy
- **Data-Driven Visual Hierarchy** — Critical information stands out
- **Responsive & Accessible** — Works seamlessly across devices

---

## ⚙️ Engineering Principles

### What AQI Pulse Does ✅
- Loads pre-trained models for inference
- Serves predictions via clean APIs
- Converts PM2.5 to AQI using CPCB rules
- Provides structured JSON data for visualization

### What AQI Pulse Does NOT Do ❌
- Train models in production backend
- Generate plots/charts in backend
- Mix frontend logic with backend
- Use ML for AQI computation (rule-based only)

> **Principle:** Backend provides intelligence and data. Frontend provides visualization and experience.

---

## 📊 Model Performance

- **Model Type:** LSTM (Long Short-Term Memory)
- **Training Data:** Historical PM2.5 measurements
- **Forecast Horizon:** 24-72 hours (hourly)
- **Input Features:** Time-lagged PM2.5 values
- **Validation:** Time-series cross-validation

*Detailed metrics available in notebooks/*

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

- **CPCB** for air quality standards and guidelines
- **Central Pollution Control Board, India** for AQI breakpoints
- **OpenAQ** and similar initiatives for open air quality data
- The open-source community for amazing tools and libraries

---
