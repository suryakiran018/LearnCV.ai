# 📸 **Title: Image Processing & Analysis Toolkit (GUI in Python + OpenCV + Streamlit)**

---

## 📝 Assignment 3 – A Practical Application with a Graphical User Interface (GUI).

**Module**: Module 1 – Image Processing Fundamentals & Computer Vision
**Deadline**: Sep 8, 2025
**Level**: 🟢 Beginner → 🟠 Intermediate → 🔴 Advanced
**Points**: 100 points

---

## **🎯 Objective**

To design and implement a **system design: GUI-based application** in Python that demonstrates fundamental **Image Processing operations** using **OpenCV**.

This project will not just cover the theory (filters, transforms, compression, etc.) but also provide a **hands-on GUI** where users can upload an image, apply operations, and visualize results **side-by-side** interactively.

---

## **📍 GUI Layout (Streamlit Design)**

### **1. Menu Bar (Top Section)**

* **File**

  * Open → Upload an image from local system
  * Save → Save processed image
  * Exit → Close/quit app

---

### **2. Left Panel (Sidebar - Operations)**

Users select operations from categories.

* **Image Info**

  * Show resolution, shape, DPI, file format, color channels

* **Color Conversions**

  * RGB ↔ BGR
  * RGB ↔ HSV
  * RGB ↔ YCbCr
  * RGB ↔ Grayscale

* **Transformations**

  * Rotation
  * Scaling (up/down)
  * Translation (shift)
  * Affine Transform
  * Perspective Transform

* **Filtering & Morphology**

  * Gaussian / Mean / Median filter
  * Sobel / Laplacian edge filters
  * Dilation, Erosion
  * Opening, Closing

* **Enhancement**

  * Histogram Equalization
  * Contrast Stretching
  * Sharpening

* **Edge Detection**

  * Sobel
  * Canny
  * Laplacian

* **Compression**

  * Save in JPG, PNG, BMP
  * Compare file size & quality

---

### **3. Right Panel (Display Area)**

* **Original Image** (left box)
* **Processed Image** (right box → dynamically updates based on chosen operation)

---

### **4. Status Bar (Bottom Section)**

* Show image properties dynamically:

  * Dimensions (H, W, C)
  * DPI/PPI
  * File format
  * File size

---

## **🛠 Step-by-Step Implementation:**

### **Phase 1 – Setup & Base GUI**

1. Install dependencies: `pip install streamlit opencv-python numpy matplotlib`
2. Create base `app.py` with Streamlit layout:

   * Sidebar (operations menu)
   * Image upload widget
   * Two image display placeholders

---

### **Phase 2 – Image Fundamentals Module**

* Implement:

  * Load and represent image as NumPy array
  * Display image shape & channel information.
  * Perform color conversions (RGB, HSV, YCbCr, Gray) using both mathematical formulas and OpenCV functions.

---

### **Phase 3 – Transformations & Bitwise Ops**

* Implement **rotation, scaling, translation, affine, perspective**
* Add **bitwise AND, OR, XOR, NOT**

---

### **Phase 4 – Filtering & Morphology**

* Gaussian, Median, Mean smoothing
* Sobel, Laplacian
* Dilation, Erosion, Opening, Closing

---

### **Phase 5 – Enhancement & Edge Detection**

* Histogram Equalization
* Sharpening filters
* Edge detection (Canny, Sobel, Laplacian)

---

### **Phase 6 – Compression & File Handling**

* Save image in different formats (JPG, PNG, BMP)
* Compare sizes in the status bar

---

### **Phase 7 – Polish the GUI**

* Add **status bar** (image info updates after each operation)
* Add **Save Processed Image** button
* Make layout clean: two columns for original vs processed image

---

## **📂 Deliverables**

1. **Codebase**: `app.py` (Streamlit GUI app) + utility scripts
2. **Notebook**: `ImageToolkit.ipynb` for step-by-step theory + practice tasks
3. **Report (PDF)**:

   * Notes on CMOS vs CCD, Sampling & Quantization, PSFs
   * Screenshots of toolkit results
   * Explanation of algorithms used
4. **Final Demo**: Interactive Streamlit GUI

---

## **🚀 Bonus Add-On**

* Add an **interactive slider** for:

  * Kernel size (for filters)
  * Rotation angle
  * Scaling factor
  * Edge detection thresholds (for Canny)
* Add a **comparison mode**: split screen (half original, half processed).
* Add a real-time video mode (apply operations to webcam feed).
* Provide a download button to export processed images directly from GUI.

---

### ✅ Submission Instructions

1. Fork the repository [`learncv.ai`](https://github.com/learncvai/learncv.ai)
2. Checkout to `/assignments` branch
3. Navigate to `/assignments/Task-3/`
4. Add your folder/files:
   * Create a folder with your `roll_no` or `college_id`
   * Upload `app.py` (Streamlit GUI)
   * Upload `ImageToolkit_<your-roll-no>.ipynb` (Notebook)
   * Upload Report (`.pdf`)
5. Commit with message: `"Task 3: Image Processing Toolkit Submission"`
6. Create a Pull Request to `/assignments` branch

---

### 📎 Resources

* [OpenCV Documentation](https://opencv.org/)
* [NumPy Documentation](https://numpy.org/doc/)
* [Streamlit Documentation](https://docs.streamlit.io/)
* Tutorials: PyImageSearch, OpenCV-Python

---

### 📊 Evaluation Criteria

| Criteria                              | Points |
| ------------------------------------- | ------ |
| GUI Implementation (Streamlit Layout) | 30     |
| Correctness of Operations (OpenCV)    | 30     |
| Documentation (Notebook + Report)     | 10     |
| Code Quality & Usability              | 20     |
| Submission Format & Completeness      | 10     |
| **Total**                             | **100** |

---

> ⚠️ **Note**: Late submissions are accepted only with 10% reduced points per each day.