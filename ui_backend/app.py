from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

AI_SERVICE_URL = "http://127.0.0.1:5001/detect"

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    # Save the file locally
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Send the image to AI backend for object detection
    with open(filepath, "rb") as image_file:
        response = requests.post(AI_SERVICE_URL, files={"file": image_file})
    
    if response.status_code != 200:
        return jsonify({"error": "Failed to process image", "details": response.text}), 500

    result = response.json()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
