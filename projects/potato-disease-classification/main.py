from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
import numpy as np
from PIL import Image

app = FastAPI()

# Load trained model
model = tf.keras.models.load_model("potato_model.keras")

# Correct class order from training
CLASS_NAMES = [
    "Early Blight",
    "Late Blight",
    "Healthy"
]

@app.get("/")
def home():
    return {
        "message": "Potato Disease Classification API"
    }

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Open uploaded image
    image = Image.open(file.file).convert("RGB")

    # Convert image to numpy array
    img_array = np.array(image)

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)

    print(prediction)

    predicted_class = CLASS_NAMES[np.argmax(prediction)]

    confidence = round(float(np.max(prediction)) * 100, 2)

    return {
        "class": predicted_class,
        "confidence_percentage": confidence
    }