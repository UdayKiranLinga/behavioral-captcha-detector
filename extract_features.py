"""
Feature extraction module for behavioral CAPTCHA detector.
Converts raw mouse movement data into meaningful features for ML classification.
"""

import json
import numpy as np
import pandas as pd
import os

def extract_features(data):
    """
    Extract behavioral features from mouse movement data.
    
    Args:
        data: List of mouse movement points with x, y coordinates and timestamps
        
    Returns:
        Dictionary containing extracted features:
        - avg_speed: Average movement speed (pixels/second)
        - std_speed: Standard deviation of speeds (variability indicator)
        - max_speed: Maximum speed reached
        - num_points: Total number of data points
    """
    # Extract coordinates and timestamps
    xs = [p['x'] for p in data]
    ys = [p['y'] for p in data]
    ts = [p['t'] for p in data]  # timestamps in milliseconds

    # Calculate speeds between consecutive points
    speeds = []
    for i in range(1, len(xs)):
        # Calculate displacement
        dx = xs[i] - xs[i-1]
        dy = ys[i] - ys[i-1]
        dt = (ts[i] - ts[i-1]) / 1000  # convert ms to seconds
        
        # Calculate speed (pixels per second)
        if dt > 0:  # avoid division by zero
            speed = ((dx**2 + dy**2)**0.5) / dt  # Euclidean distance / time
            speeds.append(speed)

    # Return feature dictionary
    return {
        'avg_speed': np.mean(speeds),    # Human: varies, Bot: consistent
        'std_speed': np.std(speeds),     # Human: high variance, Bot: low variance
        'max_speed': np.max(speeds),     # Peak movement speed
        'num_points': len(xs)            # Total data points collected
    }

def load_data(file, label):
    """
    Load mouse movement data from JSON file and extract features.
    
    Args:
        file: JSON file path containing movement data
        label: 0 for human, 1 for bot
        
    Returns:
        Dictionary with features and label
    """
    with open(file, 'r') as f:
        raw = json.load(f)
    features = extract_features(raw)
    features['label'] = label
    return features

# Main execution
if __name__ == "__main__":
    # Load and process training data
    data = []
    data.append(load_data('human_mouse_data .json', 0))  # Human data (label=0)
    data.append(load_data('bot_mouse_data.json', 1))     # Bot data (label=1)

    # Create DataFrame and save features
    df = pd.DataFrame(data)
    df.to_csv('mouse_features.csv', index=False)
    print("Features saved to mouse_features.csv")
    print("\nFeature comparison:")
    print(df)

