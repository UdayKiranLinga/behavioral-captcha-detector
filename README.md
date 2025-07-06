# 🤖 Behavioral CAPTCHA Detector

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A machine learning project that distinguishes between human and bot mouse movement patterns using behavioral analysis.

🎯 Project Overview

This project implements a behavioral CAPTCHA system that analyzes mouse movement patterns to detect whether the user is human or bot. It uses machine learning to classify movement patterns based on extracted features like speed, acceleration, and movement smoothness.

🔧 Technical Stack

- **Python 3.x**
- **Machine Learning**: scikit-learn (Random Forest Classifier)
- **Data Processing**: pandas, numpy
- **Frontend**: HTML/JavaScript for data collection
- **Model Persistence**: joblib

📁 Project Structure

```
behavioral-captcha-detector/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── demo.py                     # Complete workflow demonstration
│
├── src/                        # Source code
│   ├── extract_features.py     # Feature extraction from mouse movement data
│   ├── generate_bot_data.py    # Synthetic bot movement data generation
│   ├── train_model.py          # Model training script
│   └── predict.py              # Prediction script for new data
│
├── data/                       # Data files
│   ├── human_mouse_data .json  # Real human mouse movement data
│   ├── bot_mouse_data.json     # Synthetic bot movement data
│   ├── mouse_features.csv      # Extracted features (generated)
│   └── test_data.json          # Test data (generated)
│
├── models/                     # Trained models
│   └── mouse_model.pkl         # Trained ML model (generated)
│
└── web/                        # Web interface
    └── index.html              # Data collection interface
```

🚀 How It Works

### 1. Data Collection
- **Human Data**: Collected via web interface (`index.html`) that tracks real mouse movements
- **Bot Data**: Synthetically generated using `generate_bot_data.py` with predictable patterns

### 2. Feature Extraction
The system extracts key behavioral features:
- **Average Speed**: Mean velocity of mouse movement
- **Speed Variation**: Standard deviation of speeds (humans vary more)
- **Maximum Speed**: Peak movement speed
- **Number of Points**: Total data points collected

### 3. Machine Learning Model
- **Algorithm**: Random Forest Classifier
- **Features**: 4 numerical features extracted from movement patterns
- **Training**: Supervised learning on labeled human/bot data

### 4. Prediction
Real-time classification of new mouse movement patterns as human or bot.

## 💡 Key Technical Insights

### Human vs Bot Movement Patterns:
- **Humans**: Irregular speeds, natural acceleration/deceleration, slight tremor
- **Bots**: Consistent speeds, linear movements, perfectly timed intervals

### Feature Engineering:
- Speed calculation using Euclidean distance and time deltas
- Statistical measures to capture movement variability
- Temporal analysis of movement patterns

## 🏃‍♂️ Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Complete Demo**
   ```bash
   python demo.py
   ```

3. **Or run step by step:**
   ```bash
   cd src
   python generate_bot_data.py
   python extract_features.py
   python train_model.py
   python predict.py
   ```

4. **Collect Human Data**
   ```bash
   # Open web/index.html in browser to collect human mouse data
   ```

## 🎯 Interview Discussion Points

### Machine Learning Concepts:
- **Supervised Learning**: Binary classification problem
- **Feature Engineering**: Converting raw coordinates to meaningful features
- **Model Selection**: Why Random Forest for this use case
- **Overfitting**: Handling limited training data

### Real-World Applications:
- **CAPTCHA Systems**: Alternative to traditional text-based CAPTCHAs
- **Fraud Detection**: Identifying automated attacks
- **User Experience**: Seamless bot detection without user interaction

### Technical Challenges:
- **Data Quality**: Ensuring diverse human movement patterns
- **Feature Selection**: Identifying discriminative features
- **Real-time Processing**: Fast prediction for web applications
- **Adversarial Attacks**: Bots mimicking human behavior

### Scalability Considerations:
- **Data Collection**: Scaling to thousands of users
- **Model Updates**: Continuous learning from new data
- **Performance**: Sub-second prediction times

## 🔮 Future Enhancements

- **Advanced Features**: Pressure sensitivity, click patterns, dwell time
- **Deep Learning**: Neural networks for complex pattern recognition
- **Multi-modal**: Combining mouse, keyboard, and touch patterns
- **Adaptive Learning**: Models that evolve with new attack patterns

## 📊 Performance Metrics

- **Accuracy**: Model performance on test data
- **False Positive Rate**: Humans incorrectly flagged as bots
- **False Negative Rate**: Bots incorrectly identified as humans
- **Response Time**: Prediction latency for real-time applications

## 🧠 Machine Learning Approach

### Model Architecture
- **Algorithm**: Random Forest Classifier
- **Why Random Forest?**
  - Handles small datasets effectively
  - Provides feature importance rankings  
  - Robust to outliers in movement data
  - Interpretable results for security analysis

### Feature Engineering
Our system extracts 4 key behavioral features:

| Feature | Description | Human Pattern | Bot Pattern |
|---------|-------------|---------------|-------------|
| `avg_speed` | Average movement velocity | Variable, 20-200 px/s | Consistent, often >500 px/s |
| `std_speed` | Speed variability | High deviation | Low/zero deviation |
| `max_speed` | Peak velocity | Moderate bursts | Extreme speeds |
| `num_points` | Movement complexity | Natural variations | Fixed intervals |

### Model Performance
- **Training Accuracy**: 100% on sample data
- **Feature Importance**: `std_speed` (30.8%) most discriminative
- **Real-time Inference**: <10ms prediction time
