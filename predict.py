"""
Prediction module for behavioral CAPTCHA detector.
Uses trained ML model to classify mouse movements as human or bot.
"""

import joblib
import json
import numpy as np
import os
from extract_features import extract_features

def predict_movement(data_file, model_file='mouse_model.pkl'):
    """
    Predict if mouse movement data is from human or bot.
    
    Args:
        data_file: JSON file containing mouse movement data
        model_file: Path to trained model file
        
    Returns:
        Prediction result and confidence
    """
    # Load trained model
    try:
        model = joblib.load(model_file)
        print(f"✅ Model loaded from {model_file}")
    except FileNotFoundError:
        print(f"❌ Model file {model_file} not found. Please train the model first.")
        return None, None
    
    # Load test data
    try:
        with open(data_file, 'r') as f:
            data = json.load(f)
        print(f"✅ Test data loaded from {data_file}")
    except FileNotFoundError:
        print(f"❌ Data file {data_file} not found.")
        return None, None
    
    # Extract features from movement data
    features = extract_features(data)
    print(f"\n📊 Extracted Features:")
    for key, value in features.items():
        print(f"  {key}: {value:.2f}")
    
    # Prepare feature vector for prediction
    X = [[features['avg_speed'], features['std_speed'], 
          features['max_speed'], features['num_points']]]
    
    # Make prediction
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0]
    
    # Get confidence scores
    human_confidence = probability[0] * 100
    bot_confidence = probability[1] * 100
    
    print(f"\n🔍 Prediction Results:")
    print(f"  Classification: {'🤖 Bot' if prediction == 1 else '👤 Human'}")
    print(f"  Human Confidence: {human_confidence:.1f}%")
    print(f"  Bot Confidence: {bot_confidence:.1f}%")
    
    return prediction, max(human_confidence, bot_confidence)

if __name__ == "__main__":
    # Create test data file if it doesn't exist
    test_file = 'test_data.json'
    if not os.path.exists(test_file):
        # Use bot data as test data
        import shutil
        shutil.copy('bot_mouse_data.json', test_file)
        print(f"📋 Created {test_file} for testing")
    
    # Make prediction
    prediction, confidence = predict_movement(test_file)
    
    if prediction is not None:
        result = "Bot" if prediction == 1 else "Human"
        print(f"\n🎯 Final Result: {result} (Confidence: {confidence:.1f}%)")
    else:
        print("\n❌ Prediction failed. Please check if model is trained and data files exist.")
