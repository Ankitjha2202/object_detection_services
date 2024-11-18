# Object Detection Using YOLOv8  

This project delivers a **comprehensive solution** for **license plate detection** using the state-of-the-art YOLOv8 object detection model. From dataset preparation and model training to developing a robust Flask API, this repository is your one-stop guide to implementing real-time license plate detection.  

---

## 🚀 **Project Highlights**  

- **Oriented Bounding Boxes (OBB):** Handles rotated license plates with precision.  
- **Flask API Integration:** Provides an easy-to-use web interface for detection.  
- **GPU-Accelerated Training:** Powered by Kaggle for efficient model training.  
- **Visualization-Ready:** Clear and insightful results showcased in a Jupyter Notebook.  

---

## 🛠️ **Features**  

### 1️⃣ **Dataset Preparation**  
- Dataset sourced from **Roboflow** with high-quality annotations.  
- Preprocessing steps include scaling, augmentations, and proper formatting for YOLOv8.

### 2️⃣ **YOLOv8 Training**  
- Trained on a Kaggle **GPU environment** for optimal performance.  
- Model trained for **10 epochs** (for better prediction we can train for more epochs).
- The best model weights (`best.pt`) are ready for deployment.  

### 3️⃣ **Flask API**  
- **User-Friendly Interface:** Upload images via the web interface for detection.  
- **AI-Powered Backend:** Returns:  
  - Images with annotated bounding boxes.  
  - JSON files with bounding box coordinates and class labels.  

### 4️⃣ **Inference and Visualization**  
- Intuitive visualization of results through bounding boxes and JSON outputs.  
- Detection results include bounding box **coordinates**, **angles**, and class **labels**.  

---

## 📊 **Example Results**  

See the YOLOv8 model in action below:  

**Example 1:**  
Detected rotated license plate with oriented bounding boxes.  
![Example 1](https://i.postimg.cc/kGc4yRVT/419f8a15e8c72891-jpg-rf-f35f2e7ce0b5f68e3a67983a520cb5db.jpg)  

**Example 2:**  
License plate detected with high accuracy.  
![Example 2](https://i.postimg.cc/6qmswBF9/b1610b49fdc8767a2-jpg-rf-31acbba2f162344db41abcf2565bcb80.jpg)  

**Example 3:**  
Detection of multiple plates within a single image.  
![Example 3](https://i.postimg.cc/NMjP0W6L/uovneg34ahma1-jpg-rf-6b9fb846eff1bcc0db562de9b946ca2f.jpg)  

**Example 4:**  
Another example of a detected license plate with accurate bounding box positioning.  
![Example 4](https://i.postimg.cc/GtG3m7n8/m417sncy6eda1-jpg-rf-5ecd2be865a84aee67271a8443af1f2d.jpg)  

---

## ⚙️ **Project Workflow**  

1. **Dataset Preparation**  
   - Downloaded and preprocessed the dataset from **Roboflow**.  

2. **Model Training**  
   - Trained the YOLOv8 model in a Kaggle GPU environment.  
   - Saved the trained model weights as `best.pt`.  

3. **Inference**  
   - Performed inference using the trained model on test images.  
   - Saved results as annotated images and bounding box coordinates and rotated angle details.  

4. **Flask API**  
   - Built APIs to handle image uploads and run the YOLOv8 model for real-time inference.  

---

## 🚀 **Getting Started**  

### 1. Clone the Repository  
```bash
git clone https://github.com/Ankitjha2202/object_detection_services.git
cd object_detection_services
