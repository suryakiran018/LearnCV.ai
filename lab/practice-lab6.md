# 📘 Practice Lab - 6: Image Filtering, Restoration, Enhancement & Compression

## 🎯 **Objective**

To understand and implement **image filtering, restoration, enhancement, and compression techniques** using **OpenCV and Python**. Students will explore **spatial & frequency domain methods**, perform **contrast adjustments**, and apply **histogram-based enhancements** to improve image quality.

---

## 💻 OpenCV & Image Processing Tasks

### 🔹 **1. Image Filtering**

* **Convolution**: Apply basic kernels (smoothing, sharpening).
* **Morphological Operations**: Erosion, dilation, opening, closing, morphological gradient.
* **Interpolation Methods**: Nearest neighbor, bilinear, bicubic.
* **Spatial Filtering**:

  * Low-pass filters (smoothing, blurring)
  * High-pass filters (edge detection: Sobel, Laplacian, Canny)
* **Non-Linear Spatial Filtering**: Median filter, bilateral filter.
* **Frequency Domain Filters**:

  * Apply Fourier Transform
  * Ideal/Bandpass filters
  * High-pass and low-pass filtering in frequency domain

---

### 🔹 **2. Image Restoration**

* **Image Degradation Simulation**: Add noise (Gaussian, salt & pepper, motion blur).
* **Spatial Domain Methods**: Noise removal using filters.
* **Frequency Domain Methods**: Wiener filter, inverse filtering.
* **Fourier Transforms**: Image reconstruction using FFT & inverse FFT.
* **Wavelet Transform**: Perform multi-resolution image representation.

---

### 🔹 **3. Image Enhancement**

* **Contrast & Brightness Adjustment**: Manual scaling.
* **Gamma Correction** (Intensity Transformation).
* **Histogram Equalization**:

  * Global histogram equalization.
  * Local histogram equalization.
* **Adaptive Histogram Equalization (CLAHE)**.
* **Contrast Stretching**: Normalize pixel values for better visibility.

---

### 🔹 **4. Image Compression**

* Apply **lossless compression** (PNG format).
* Apply **lossy compression** (JPEG format, quality factor adjustment).
* Compare **file sizes** and **visual quality**.

---

## 🛠️ **Lab Instructions for Students**

* Use **Python + OpenCV + NumPy + Matplotlib** for visualization.
* Experiment with **different filters and transformations**.
* Record **observations**: effects of filter size, noise type, contrast levels.
* Submit **code snippets, results, and screenshots** in your lab manual.

---

## ✅ **Rubric for Evaluation**

| Criteria                                 | Marks  |
| ---------------------------------------- | ------ |
| Filtering (Spatial & Frequency Domain)   | 10     |
| Restoration Techniques                   | 10     |
| Enhancement (Histogram, Contrast, CLAHE) | 10     |
| Compression (Lossy & Lossless)           | 5      |
| Documentation & Analysis                 | 5      |
| **Total**                                | **40** |

---

## 🙏 **Credits / Acknowledgements**

* [OpenCV-Python Documentation](https://docs.opencv.org/)
* [Scipy & NumPy Libraries](https://scipy.org/)
* Digital Image Processing concepts (R.C. Gonzalez & R.E. Woods)

---

👉 This **Lab-6** will strengthen understanding of **filtering, restoration, and enhancement** – which are core in **computer vision, medical imaging, and AI-based image applications**.

---