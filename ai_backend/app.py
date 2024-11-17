from flask import Flask, request, jsonify
import os
from ultralytics import YOLO
from PIL import Image

app = Flask(__name__)

MODEL_PATH = 'best.pt'  # Path to your trained weights file
OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load the pre-trained model
model = YOLO(MODEL_PATH)

@app.route("/detect", methods=["POST"])
def detect():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    # Load the image
    try:
        image = Image.open(file.stream).convert("RGB")
    except Exception as e:
        return jsonify({"error": f"Error loading image: {str(e)}"}), 400
    
    # Perform object detection
    try:
        results = model(image)  # Perform inference with YOLOv8
    except Exception as e:
        return jsonify({"error": f"Error performing detection: {str(e)}"}), 500

    # Save the output image with bounding boxes
    output_image_path = os.path.join(OUTPUT_FOLDER, file.filename)
    results.save(save_dir=OUTPUT_FOLDER)  # Saves image with bounding boxes
    
    # Get the results in pandas DataFrame format
    df = results.pandas().xyxy[0]  # Bounding box info as DataFrame
    json_path = os.path.join(OUTPUT_FOLDER, f"{file.filename}.json")

    # Save the results as a JSON file
    df.to_json(json_path, orient="records")

    # Return the paths of the output image and JSON file
    return jsonify({
        "message": "Detection completed",
        "output_image": f"/{OUTPUT_FOLDER}/{file.filename}",
        "output_json": f"/{OUTPUT_FOLDER}/{file.filename}.json"
    })

if __name__ == "__main__":
    # Start Flask app
    app.run(host="0.0.0.0", port=5001)
