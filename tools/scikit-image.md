# Scikit-Image Guide

## 1. Introduction to Scikit-Image

### What is Scikit-Image?

Scikit-image is an open-source Python library for image processing, providing a collection of algorithms for tasks like filtering, segmentation, and feature extraction. 

It integrates seamlessly with NumPy arrays and is widely used in computer vision, medical imaging, and scientific research.

### Installing Scikit-Image
Install scikit-image using pip:
```bash
pip install scikit-image
```

### Importing Scikit-Image
Import specific modules as needed:
```python
import numpy as np
import skimage
from skimage import io, filters, feature, segmentation, color, transform
import matplotlib.pyplot as plt
```

---

## 2. Scikit-Image Basics

### Loading and Saving Images
Load and display an image:
```python
image = io.imread('image.jpg')  # Load image as NumPy array
plt.imshow(image)
plt.axis('off')
plt.show()
```

Save an image:
```python
io.imsave('output.jpg', image)
```

### Image Data Types
Scikit-image typically works with NumPy arrays:
- **Grayscale**: 2D array (e.g., `shape=(height, width)`).
- **RGB**: 3D array (e.g., `shape=(height, width, 3)`).
- **Floating-point**: Many functions expect images in `[0, 1]` range; convert if needed:
  ```python
  image_float = skimage.img_as_float(image)  # Convert to float
  ```

---

## 3. Common Image Processing Tasks

### 3.1. Image Filtering
Apply filters to enhance or smooth images.

- **Gaussian Blur**:
  ```python
  blurred = filters.gaussian(image_float, sigma=2)
  plt.imshow(blurred)
  plt.title("Gaussian Blur")
  plt.axis('off')
  plt.show()
  ```

- **Edge Detection (Sobel)**:
  ```python
  edges = filters.sobel(image_float)
  plt.imshow(edges, cmap='gray')
  plt.title("Sobel Edge Detection")
  plt.axis('off')
  plt.show()
  ```

### 3.2. Image Segmentation
Partition an image into meaningful regions.

- **Thresholding**:
  ```python
  threshold = filters.threshold_otsu(image_float)
  binary = image_float > threshold
  plt.imshow(binary, cmap='gray')
  plt.title("Otsu Thresholding")
  plt.axis('off')
  plt.show()
  ```

- **Region-Based Segmentation**:
  ```python
  labels = segmentation.slic(image, n_segments=100, compactness=10)
  plt.imshow(segmentation.mark_boundaries(image, labels))
  plt.title("SLIC Segmentation")
  plt.axis('off')
  plt.show()
  ```

### 3.3. Feature Detection
Identify key points or structures.

- **Corner Detection (Harris)**:
  ```python
  corners = feature.corner_harris(image_float)
  plt.imshow(corners, cmap='hot')
  plt.title("Harris Corner Detection")
  plt.axis('off')
  plt.show()
  ```

- **Blob Detection (Difference of Gaussians)**:
  ```python
  blobs = feature.blob_dog(image_float, max_sigma=30, threshold=0.1)
  fig, ax = plt.subplots()
  ax.imshow(image_float, cmap='gray')
  for blob in blobs:
      y, x, r = blob
      c = plt.Circle((x, y), r, color='red', linewidth=2, fill=False)
      ax.add_patch(c)
  plt.title("Blob Detection")
  plt.axis('off')
  plt.show()
  ```

### 3.4. Color Space Conversion
Convert between color spaces (e.g., RGB to Grayscale):
```python
gray_image = color.rgb2gray(image)
plt.imshow(gray_image, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()
```

### 3.5. Geometric Transformations
Apply transformations like resizing or rotation.

- **Resize**:
  ```python
  resized = transform.resize(image, (image.shape[0] // 2, image.shape[1] // 2))
  plt.imshow(resized)
  plt.title("Resized Image")
  plt.axis('off')
  plt.show()
  ```

- **Rotation**:
  ```python
  rotated = transform.rotate(image, angle=45)
  plt.imshow(rotated)
  plt.title("Rotated Image")
  plt.axis('off')
  plt.show()
  ```

---

## 4. Advanced Scikit-Image Features

### 4.1. Morphological Operations
Manipulate image shapes with operations like dilation and erosion:
```python
from skimage import morphology
binary = image_float > filters.threshold_otsu(image_float)
dilated = morphology.dilation(binary, morphology.disk(3))
plt.imshow(dilated, cmap='gray')
plt.title("Dilation")
plt.axis('off')
plt.show()
```

### 4.2. Image Restoration
Remove noise or restore images.

- **Denoising (Total Variation)**:
  ```python
  from skimage import restoration
  denoised = restoration.denoise_tv_chambolle(image_float, weight=0.1)
  plt.imshow(denoised)
  plt.title("TV Denoising")
  plt.axis('off')
  plt.show()
  ```

### 4.3. Feature Matching
Match features between two images:
```python
from skimage import feature
img1 = io.imread('image1.jpg', as_gray=True)
img2 = io.imread('image2.jpg', as_gray=True)
orb = feature.ORB(n_keypoints=200)
orb.detect_and_extract(img1)
keypoints1, descriptors1 = orb.keypoints, orb.descriptors
orb.detect_and_extract(img2)
keypoints2, descriptors2 = orb.keypoints, orb.descriptors
matches = feature.match_descriptors(descriptors1, descriptors2)
fig, ax = plt.subplots()
feature.plot_matches(ax, img1, img2, keypoints1, keypoints2, matches)
plt.title("Feature Matching")
plt.axis('off')
plt.show()
```

---

## 5. Troubleshooting & Tips

### Common Issues
- **Data Type Errors**:
  ```python
  image_uint8 = skimage.img_as_ubyte(image_float)  # Convert back to uint8 for saving
  io.imsave('output.jpg', image_uint8)
  ```
- **Memory Issues**: For large images, use `skimage.util.crop` or process in chunks.
- **Incompatible Shapes**: Ensure input images have correct dimensions for operations like feature matching.

### Performance Tips
- **Use Efficient Filters**: Prefer `filters.gaussian` over manual convolution for speed.
- **Vectorize Operations**: Leverage NumPy’s vectorized operations within scikit-image functions.
- **Cache Results**: Save intermediate results (e.g., filtered images) to avoid recomputation.

---

## 6. Resources & Further Learning

- **Official Documentation**: [Scikit-Image Docs](https://scikit-image.org/docs/stable/)
- **Books**: "Image Processing in Python" (online tutorials and guides)
- **Community**: [Stack Overflow](https://stackoverflow.com/questions/tagged/scikit-image), [Scikit-Image GitHub](https://github.com/scikit-image/scikit-image)

---