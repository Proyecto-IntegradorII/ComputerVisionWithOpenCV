import json
from flask import Flask, request, jsonify
import numpy as np
import cv2
from ocr import extract_text_from_image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'This code has been tested before being deployed, and Render has deployed it automatically.'

@app.route('/get_characters_of_image', methods=['POST'])
def get_characters_of_image():
    # Check if an image was received in the POST request
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image = request.files['image']
    
    # Read the image using OpenCV
    image_cv2 = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Extract characters from the image
    characters = extract_text_from_image(image_cv2)
    
    return jsonify({'characters': characters}), 200


if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)