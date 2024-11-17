from flask import Flask, request, jsonify
import os
import torch
from PIL import Image

app = Flask(__name__)
MODEL_PATH = "weights/best.pt"  # Path to your trained weights file
OUTPUT_FOLDER = "output"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load the pre-trained model
model = torch.hub.load("ultralytics/yolov3", "custom", path=MODEL_PATH, force_reload=True)

@app.route("/detect", methods=["POST"])
def detect():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    # Load the image
    image = Image.open(file.stream).convert("RGB")

    # Perform object detection
    results = model(image)

    # Save the output image with bounding boxes
    output_image_path = os.path.join(OUTPUT_FOLDER, file.filename)
    results.save(save_dir=OUTPUT_FOLDER)

    # Save the results as a JSON file
    json_path = os.path.join(OUTPUT_FOLDER, f"{file.filename}.json")
    results.pandas().xyxy[0].to_json(json_path, orient="records")

    # Return the paths of the output image and JSON file
    return jsonify({
        "message": "Detection completed",
        "output_image": output_image_path,
        "output_json": json_path
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
