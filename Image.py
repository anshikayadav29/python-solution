# AI Image Recognition using MobileNetV2
# Install dependencies before running:
# pip install tensorflow pillow

import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, decode_predictions, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the pretrained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Path to your image (change this!)
img_path = 'your_image.jpg'

# Load and preprocess the image
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Make prediction
preds = model.predict(x)

# Decode and print the top 3 predictions
print("Top Predictions:")
for pred in decode_predictions(preds, top=3)[0]:
    print(f"{pred[1]}: {pred[2]*100:.2f}%")
