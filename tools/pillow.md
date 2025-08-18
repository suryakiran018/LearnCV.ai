# Pillow Guide

## 1. Introduction to Pillow

### What is Pillow?
Pillow is a fork of the Python Imaging Library (PIL) that provides powerful tools for image processing. 

It supports tasks like image loading, resizing, cropping, filtering, and format conversion, making it ideal for applications in data science, web development, and computer vision.

### Installing Pillow
Install Pillow using pip:
```bash
pip install Pillow
```

### Importing Pillow
Import the `Image` module and other necessary components:
```python
from PIL import Image, ImageFilter, ImageEnhance
import numpy as np
```

---

## 2. Pillow Basics

### Loading and Saving Images
Load and display an image:
```python
image = Image.open('image.jpg')  # Load image
image.show()  # Display image (opens in default viewer)
```

Save an image:
```python
image.save('output.png', 'PNG')  # Save as PNG
```

### Image Properties
Access image attributes:
```python
print(image.format)  # Output: JPEG (or other format)
print(image.size)    # Output: (width, height)
print(image.mode)    # Output: RGB (or L for grayscale, etc.)
```

### Converting to NumPy Array
Convert a Pillow image to a NumPy array for further processing:
```python
image_array = np.array(image)
print(image_array.shape)  # Output: (height, width, channels)
```

Convert back to Pillow image:
```python
image_from_array = Image.fromarray(image_array)
```

---

## 3. Common Image Processing Tasks

### 3.1. Resizing Images
Resize an image while maintaining aspect ratio:
```python
resized_image = image.resize((100, 100))  # Resize to 100x100 pixels
resized_image.show()
```

Use `thumbnail` to modify the image in-place while preserving aspect ratio:
```python
image.thumbnail((100, 100))  # Resize to fit within 100x100
image.show()
```

### 3.2. Cropping Images
Crop a region from an image:
```python
box = (50, 50, 150, 150)  # (left, top, right, bottom)
cropped_image = image.crop(box)
cropped_image.show()
```

### 3.3. Rotating and Flipping
Rotate an image:
```python
rotated_image = image.rotate(45, expand=True)  # Rotate 45 degrees
rotated_image.show()
```

Flip an image:
```python
flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)  # Horizontal flip
flipped_image.show()
```

### 3.4. Image Filtering
Apply filters like blur or edge detection:
```python
blurred_image = image.filter(ImageFilter.GaussianBlur(radius=2))
blurred_image.show()

edge_image = image.filter(ImageFilter.FIND_EDGES)
edge_image.show()
```

### 3.5. Color Adjustments
Adjust brightness, contrast, or color:
```python
# Brightness
bright_image = ImageEnhance.Brightness(image).enhance(1.5)  # Increase by 50%
bright_image.show()

# Contrast
contrast_image = ImageEnhance.Contrast(image).enhance(1.5)
contrast_image.show()

# Convert to grayscale
gray_image = image.convert('L')
gray_image.show()
```

---

## 4. Advanced Pillow Features

### 4.1. Drawing on Images
Use `ImageDraw` to add shapes, text, or annotations:
```python
from PIL import ImageDraw, ImageFont
draw = ImageDraw.Draw(image)
draw.rectangle((50, 50, 150, 150), outline='red', width=2)
draw.text((50, 30), "Sample Text", fill='blue')  # Default font
image.show()
```

For custom fonts:
```python
font = ImageFont.truetype('arial.ttf', size=20)  # Specify font file
draw.text((50, 30), "Sample Text", fill='blue', font=font)
image.show()
```

### 4.2. Image Composition
Combine multiple images:
```python
image1 = Image.open('image1.jpg')
image2 = Image.open('image2.jpg').resize(image1.size)  # Match sizes
blended = Image.blend(image1, image2, alpha=0.5)  # Blend with 50% opacity
blended.show()
```

Paste one image onto another:
```python
image1.paste(image2, (50, 50))  # Paste image2 at (50, 50)
image1.show()
```

### 4.3. Working with Image Sequences (GIFs)
Process animated GIFs:
```python
gif = Image.open('animation.gif')
frames = []
for frame in range(gif.n_frames):
    gif.seek(frame)
    frames.append(gif.copy())
frames[0].save('output.gif', save_all=True, append_images=frames[1:], duration=100, loop=0)
```

### 4.4. Image Metadata
Access and modify EXIF data:
```python
from PIL import ExifTags
exif = image.getexif()
for tag_id, value in exif.items():
    tag = ExifTags.TAGS.get(tag_id, tag_id)
    print(f"{tag}: {value}")
```

---

## 5. Troubleshooting & Tips

### Common Issues
- **Unsupported Format**: Ensure the file format is supported (e.g., JPEG, PNG). Install additional dependencies for formats like TIFF:
  ```bash
  pip install Pillow[extra]
  ```
- **Memory Errors**: Downsample large images before processing:
  ```python
  image.thumbnail((1000, 1000))  # Limit to 1000x1000
  ```
- **Mode Mismatch**: Convert images to consistent modes (e.g., RGB) for operations:
  ```python
  image = image.convert('RGB')
  ```

### Performance Tips
- **Batch Processing**: Use `ImageSequence.Iterator` for large GIFs or multi-page TIFFs.
- **Optimize Filters**: Apply filters like `GaussianBlur` with smaller radii for faster processing.
- **Use NumPy for Bulk Operations**: Perform pixel-level operations on NumPy arrays instead of Pillow loops.

---

## 6. Resources & Further Learning

- **Official Documentation**: [Pillow Docs](https://pillow.readthedocs.io/en/stable/)
- **Books**: "Python Imaging Library Handbook" (online resource)
- **Community**: [Stack Overflow](https://stackoverflow.com/questions/tagged/pillow), [Pillow GitHub](https://github.com/python-pillow/Pillow)

---