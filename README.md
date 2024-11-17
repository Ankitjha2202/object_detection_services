# License Plate Detection Using YOLOv8

This project is a comprehensive solution for license plate detection using the YOLOv8 object detection model. The workflow includes dataset preparation, model training, and the development of a Flask API for performing inference on license plate images.

## Project Overview

In this project, I leveraged a license plate detection dataset from **Roboflow**, trained a **YOLOv8 OBB model** (with Oriented Bounding Boxes), and developed a Flask-based web service for detection. The model was trained for **10 epochs** and the results were visualized in a Jupyter Notebook. The project demonstrates how to integrate a pre-trained model into a web API, enabling the detection of license plates in images.

## Key Steps

### 1. **Dataset Preparation**
- I used **Roboflow** to download a **license plate detection dataset** that contains images with corresponding bounding box annotations.
- The dataset was used for training the YOLOv8 model.

### 2. **Training the YOLOv8 Model**
- The model used in this project is **YOLOv8 OBB** (Oriented Bounding Boxes), which is designed to handle object detection tasks that involve rotated bounding boxes.
- I trained the model for **10 epochs**, adjusting hyperparameters to achieve optimal performance on the dataset.
- Training was done on a GPU environment to ensure efficiency, and model performance was monitored throughout the training process.

### 3. **Inference and Results**
- After training, I performed inference on test images from the dataset and displayed the results, which include bounding boxes around detected license plates.
- Below are examples of images with bounding boxes around detected license plates.

#### Example Results:
- **Example 1**: License plate detection with bounding boxes.
  ![Project Diagram](https://i.postimg.cc/kGc4yRVT/419f8a15e8c72891-jpg-rf-f35f2e7ce0b5f68e3a67983a520cb5db.jpg)

- **Example 2**: Another license plate detection with bounding boxes.
  ![Project Diagram](https://i.postimg.cc/6qmswBF9/b1610b49fdc8767a2-jpg-rf-31acbba2f162344db41abcf2565bcb80.jpg)

- **Example 3**: Another detection result showing multiple bounding boxes.
  ![Project Diagram](https://i.postimg.cc/NMjP0W6L/uovneg34ahma1-jpg-rf-6b9fb846eff1bcc0db562de9b946ca2f.jpg)

The results, including the images with bounding boxes and a JSON file with the bounding box coordinates, are saved after each inference.

### 4. **Flask API**
- A **Flask web application** was created with two main services:
  - **UI Backend**: Accepts image uploads from the user.
  - **AI Backend**: Runs inference on the uploaded images using the trained YOLOv8 model.
- The API performs inference and returns the following:
  - Path to the output image with bounding boxes.
  - Path to the JSON file containing the detected bounding box coordinates and class labels.

### 5. **Jupyter Notebook**
- The **Jupyter notebook** contains:
  - Model training steps, including data preprocessing, training, and validation.
  - Code to perform inference on images using the trained model.
  - Visualization of detection results, including the images with drawn bounding boxes and saved JSON results.
  
The notebook is structured for anyone to easily check and replicate the results.

## How to Run

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/license-plate-detection.git
cd license-plate-detection
