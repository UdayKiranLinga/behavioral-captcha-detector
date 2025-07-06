#!/usr/bin/env python3
"""
Demo script to showcase the complete behavioral CAPTCHA detector workflow.
This script demonstrates the entire pipeline from data generation to prediction.
"""

import os
import json
import subprocess
import sys

def run_command(command, description):
    """Run a command and display its output."""
    print(f"\n{'='*50}")
    print(f"🔄 {description}")
    print('='*50)
    
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(f"⚠️  {result.stderr}")
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🤖 BEHAVIORAL CAPTCHA DETECTOR - DEMO")
    print("=====================================")
    print("This demo shows the complete ML pipeline for detecting bots vs humans")
    
    # Check if we're in the right directory
    if not os.path.exists('src/extract_features.py'):
        print("❌ Please run this script from the behavioral-captcha-detector directory")
        sys.exit(1)
    
    # Step 1: Generate bot data
    success = run_command(
        "cd src && python generate_bot_data.py",
        "Step 1: Generating synthetic bot movement data"
    )
    if not success:
        print("❌ Failed to generate bot data")
        return
    
    # Step 2: Extract features
    success = run_command(
        "cd src && python extract_features.py",
        "Step 2: Extracting features from mouse movement data"
    )
    if not success:
        print("❌ Failed to extract features")
        return
    
    # Step 3: Train model
    success = run_command(
        "cd src && python train_model.py",
        "Step 3: Training Random Forest classifier"
    )
    if not success:
        print("❌ Failed to train model")
        return
    
    # Step 4: Make predictions
    success = run_command(
        "cd src && python predict.py",
        "Step 4: Making predictions on test data"
    )
    if not success:
        print("❌ Failed to make predictions")
        return
    
    print(f"\n{'='*50}")
    print("🎉 DEMO COMPLETED SUCCESSFULLY!")
    print('='*50)
    print("Key files generated:")
    print("- data/mouse_features.csv: Extracted features")
    print("- models/mouse_model.pkl: Trained ML model")
    print("\nThis demonstrates:")
    print("✅ Feature engineering from raw movement data")
    print("✅ Machine learning model training")
    print("✅ Real-time bot detection")
    print("✅ End-to-end ML pipeline")

if __name__ == "__main__":
    main()
