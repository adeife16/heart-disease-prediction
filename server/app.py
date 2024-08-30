from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from keras.models import load_model
from keras.utils import load_img, img_to_array
from PIL import Image
import numpy as np
import io

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

# Load the pre-trained model
model = load_model('model_new.keras')

# Define the class names
class_names = ["false", "true"]  # Index 0 -> "false", Index 1 -> "true"

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    image_file = request.files['image']
    image_stream = io.BytesIO(image_file.read())
    image = load_img(image_stream, target_size=(128, 128))  # Resize to match model input
    image_array = img_to_array(image)
    image_array = image_array / 255.0  # Normalize image to match model training conditions
    image_array = np.expand_dims(image_array, axis=0)  # Expand to 4 dimensions

    # Predict using the model
    prediction = model.predict(image_array)
    predicted_class_index = np.argmax(prediction)
    predicted_class = class_names[predicted_class_index]
    confidence = prediction[0][predicted_class_index]

    # Return the result
    result = {
        "prediction": predicted_class,  # true or false
        "confidence": float(confidence * 100).__round__(2)  # Percentage confidence
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
