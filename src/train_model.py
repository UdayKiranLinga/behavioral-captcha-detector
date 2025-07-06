"""
Machine Learning Model Training for Behavioral CAPTCHA Detection.
Trains a Random Forest classifier to distinguish between human and bot mouse movements.
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_model():
    """
    Train a Random Forest classifier for bot detection.
    
    Returns:
        Trained model and performance metrics
    """
    # Load feature data
    df = pd.read_csv('../data/mouse_features.csv')
    print("Dataset shape:", df.shape)
    print("\nFeature statistics:")
    print(df.describe())
    
    # Prepare features and labels
    X = df.drop(columns=['label'])  # Features: avg_speed, std_speed, max_speed, num_points
    y = df['label']                 # Labels: 0=human, 1=bot
    
    # Display feature names for interview discussion
    print("\nFeatures used for classification:")
    for i, feature in enumerate(X.columns):
        print(f"{i+1}. {feature}")
    
    # Train Random Forest classifier
    # Random Forest chosen for: interpretability, handles small datasets well, robust to outliers
    model = RandomForestClassifier(
        n_estimators=100,    # Number of trees
        random_state=42,     # For reproducible results
        max_depth=10         # Prevent overfitting
    )
    
    print("\nTraining Random Forest classifier...")
    model.fit(X, y)
    
    # Evaluate model performance
    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    
    print(f"\nModel Performance:")
    print(f"Training Accuracy: {accuracy:.2%}")
    print("\nClassification Report:")
    print(classification_report(y, y_pred, target_names=['Human', 'Bot']))
    
    # Feature importance for interpretability
    feature_importance = pd.DataFrame({
        'feature': X.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\nFeature Importance:")
    print(feature_importance)
    
    # Save the trained model
    joblib.dump(model, '../models/mouse_model.pkl')
    print("\nModel saved as '../models/mouse_model.pkl'")
    
    return model, accuracy

if __name__ == "__main__":
    model, accuracy = train_model()