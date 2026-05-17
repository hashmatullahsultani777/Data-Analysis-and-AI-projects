# AI-Based Potato Disease Classification System

## Project Overview
A deep learning model designed to detect potato leaf diseases —
**Early Blight** and **Late Blight** — to support agricultural
productivity and reduce global crop losses.

## Problem Statement
Potato diseases are responsible for significant agricultural losses
globally. Early and accurate detection of leaf diseases can help
farmers take timely action and reduce crop damage.

## Tools & Technologies
- Python
- TensorFlow
- Keras
- FastAPI
- Uvicorn
- NumPy
- Pandas
- Matplotlib

## How It Works
1. Input: Image of a potato leaf
2. The CNN model analyzes the image
3. Output: Disease classification (Healthy / Early Blight / Late Blight)
4. Result is returned via a REST API built with FastAPI

## Model Details
- Architecture: Convolutional Neural Network (CNN)
- Framework: TensorFlow & Keras
- Deployment: FastAPI + Uvicorn as a prediction API

## Diseases Detected
- **Healthy** — No disease detected
- **Early Blight** — Caused by Alternaria solani fungus
- **Late Blight** — Caused by Phytophthora infestans
