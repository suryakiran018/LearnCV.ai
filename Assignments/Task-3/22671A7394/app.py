import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

# Set Streamlit page configuration
st.set_page_config(page_title="Image Processing Toolkit", layout="wide")

# Title
st.title("🖼️ Image Processing GUI Toolkit")

# Sidebar File Operations
with st.sidebar:
    st.title("📂 File")
    uploaded_file = st.file_uploader("Open Image", type=["jpg", "jpeg", "png", "bmp"])
    save_image = st.button("💾 Save Processed Image")
    if st.button("❌ Exit App"):
        st.stop()

# Helper Functions
def image_to_bytes(img, format):
    pil_img = Image.fromarray(img)
    buf = io.BytesIO()
    pil_img.save(buf, format=format)
    return buf.getvalue()

def apply_operation(img, category, operation, params):
    result = img.copy()
    if category == "Color Conversions":
        if operation == "RGB to Grayscale":
            result = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        elif operation == "RGB to HSV":
            result = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        elif operation == "RGB to YCbCr":
            result = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
        elif operation == "BGR to RGB":
            result = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    elif category == "Transformations":
        if operation == "Rotate":
            angle = params.get("angle", 0)
            (h, w) = img.shape[:2]
            M = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)
            result = cv2.warpAffine(img, M, (w, h))
        elif operation == "Scale":
            fx = params.get("fx", 1.0)
            fy = params.get("fy", 1.0)
            result = cv2.resize(img, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
        elif operation == "Translate":
            tx = params.get("tx", 0)
            ty = params.get("ty", 0)
            M = np.float32([[1, 0, tx], [0, 1, ty]])
            result = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

    elif category == "Filtering & Morphology":
        ksize = params.get("ksize", 3)
        if operation == "Gaussian Blur":
            result = cv2.GaussianBlur(img, (ksize, ksize), 0)
        elif operation == "Median Blur":
            result = cv2.medianBlur(img, ksize)
        elif operation == "Mean Blur":
            result = cv2.blur(img, (ksize, ksize))
        elif operation == "Sobel":
            result = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=ksize)
        elif operation == "Laplacian":
            result = cv2.Laplacian(img, cv2.CV_64F)
        elif operation == "Dilation":
            kernel = np.ones((ksize, ksize), np.uint8)
            result = cv2.dilate(img, kernel, iterations=1)
        elif operation == "Erosion":
            kernel = np.ones((ksize, ksize), np.uint8)
            result = cv2.erode(img, kernel, iterations=1)

    elif category == "Enhancement":
        if operation == "Histogram Equalization":
            if len(img.shape) == 3 and img.shape[2] == 3:
                img_yuv = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
                img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
                result = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
            else:
                result = cv2.equalizeHist(img)

    elif category == "Edge Detection":
        if operation == "Canny":
            result = cv2.Canny(img, 100, 200)
        elif operation == "Sobel":
            result = cv2.Sobel(img, cv2.CV_64F, 1, 0)
        elif operation == "Laplacian":
            result = cv2.Laplacian(img, cv2.CV_64F)

    elif category == "Compression":
        fmt = params.get("format", "JPG")
        buf = image_to_bytes(img, fmt)
        st.download_button("📥 Download Image", buf, file_name=f"compressed.{fmt.lower()}", mime=f"image/{fmt.lower()}")
        return img

    return result

# Sidebar - Category & Operation
st.sidebar.title("🧰 Operations")
categories = {
    "Image Info": ["Show Info"],
    "Color Conversions": ["RGB to Grayscale", "RGB to HSV", "RGB to YCbCr", "BGR to RGB"],
    "Transformations": ["Rotate", "Scale", "Translate"],
    "Filtering & Morphology": ["Gaussian Blur", "Median Blur", "Mean Blur", "Sobel", "Laplacian", "Dilation", "Erosion"],
    "Enhancement": ["Histogram Equalization"],
    "Edge Detection": ["Canny", "Sobel", "Laplacian"],
    "Compression": ["JPG", "PNG", "BMP"]
}
category = st.sidebar.selectbox("Category", list(categories.keys()))
operation = st.sidebar.selectbox("Operation", categories[category])

# Additional Params
params = {}
if operation == "Rotate":
    params["angle"] = st.sidebar.slider("Angle", -180, 180, 0)
if operation == "Scale":
    params["fx"] = st.sidebar.slider("Scale X", 0.1, 3.0, 1.0)
    params["fy"] = st.sidebar.slider("Scale Y", 0.1, 3.0, 1.0)
if operation == "Translate":
    params["tx"] = st.sidebar.slider("Shift X", -100, 100, 0)
    params["ty"] = st.sidebar.slider("Shift Y", -100, 100, 0)
if operation in ["Gaussian Blur", "Median Blur", "Mean Blur", "Sobel", "Dilation", "Erosion"]:
    params["ksize"] = st.sidebar.slider("Kernel Size", 1, 15, 3, step=2)
if category == "Compression":
    params["format"] = operation

# Main App Display
col1, col2 = st.columns(2)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    rgb_image = np.array(image.convert("RGB"))

    with col1:
        st.subheader("Original Image")
        st.image(rgb_image, use_column_width=True)

    with col2:
        st.subheader("Processed Image")
        if category == "Image Info":
            st.info(f"Format: {image.format}\nMode: {image.mode}\nSize: {image.size}\nShape: {np.array(image).shape}")
            st.image(rgb_image, use_column_width=True)
        else:
            processed = apply_operation(rgb_image, category, operation, params)
            if processed is not None:
                if len(processed.shape) == 2:
                    st.image(processed, use_column_width=True, clamp=True, channels="GRAY")
                else:
                    st.image(processed, use_column_width=True)

    # Save Image
    if save_image and category != "Compression":
        save_format = "PNG"
        img_bytes = image_to_bytes(processed, save_format)
        st.download_button("⬇️ Download Processed Image", img_bytes, file_name="processed.png", mime="image/png")

    # Status Bar
    st.markdown("---")
    st.subheader("📊 Image Properties")
    st.write(f"**Format:** {image.format}")
    st.write(f"**Mode (Color Channels):** {image.mode}")
    st.write(f"**Size (W x H):** {image.size[0]} x {image.size[1]}")
    st.write(f"**Shape:** {np.array(image).shape}")
    st.write(f"**File Size (KB):** {round(uploaded_file.size / 1024, 2)} KB")

else:
    st.info("Please upload an image to get started.")
