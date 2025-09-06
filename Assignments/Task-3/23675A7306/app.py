import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
import os
import time
from datetime import datetime
import matplotlib.pyplot as plt

# Set page configuration
st.set_page_config(
    page_title="Image Processing Toolkit",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables
if 'img' not in st.session_state:
    st.session_state.img = None
if 'processed_img' not in st.session_state:
    st.session_state.processed_img = None
if 'img_info' not in st.session_state:
    st.session_state.img_info = {}
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

# Function to get image information
def get_image_info(img, uploaded_file):
    if img is None:
        return {}
    
    if uploaded_file is not None:
        file_size = uploaded_file.size
        file_format = uploaded_file.type
    else:
        file_size = "N/A"
        file_format = "N/A"
    
    height, width = img.shape[:2]
    channels = img.shape[2] if len(img.shape) > 2 else 1
    
    return {
        "Dimensions": f"{width} x {height}",
        "Channels": channels,
        "File Size": f"{file_size} bytes" if file_size != "N/A" else "N/A",
        "File Format": file_format
    }

# Function to apply operations
def apply_operation(img, operation, params):
    if img is None:
        return None
    
    processed_img = img.copy()
    
    # Color Conversions
    if operation == "RGB to BGR":
        processed_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    elif operation == "BGR to RGB":
        processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    elif operation == "RGB to HSV":
        processed_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    elif operation == "HSV to RGB":
        processed_img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    elif operation == "RGB to YCbCr":
        processed_img = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
    elif operation == "YCbCr to RGB":
        processed_img = cv2.cvtColor(img, cv2.COLOR_YCrCb2RGB)
    elif operation == "RGB to Grayscale":
        processed_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # Convert back to 3 channels for consistent display
        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_GRAY2RGB)
    
    # Transformations
    elif operation == "Rotation":
        angle = params.get("angle", 0)
        height, width = img.shape[:2]
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        processed_img = cv2.warpAffine(img, rotation_matrix, (width, height))
    elif operation == "Scaling":
        scale = params.get("scale", 1.0)
        width = int(img.shape[1] * scale)
        height = int(img.shape[0] * scale)
        processed_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_LINEAR)
    elif operation == "Translation":
        tx = params.get("tx", 0)
        ty = params.get("ty", 0)
        translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
        height, width = img.shape[:2]
        processed_img = cv2.warpAffine(img, translation_matrix, (width, height))
    
    # Filtering & Morphology
    elif operation == "Gaussian Blur":
        kernel_size = params.get("kernel_size", 5)
        processed_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    elif operation == "Median Blur":
        kernel_size = params.get("kernel_size", 5)
        processed_img = cv2.medianBlur(img, kernel_size)
    elif operation == "Mean Blur":
        kernel_size = params.get("kernel_size", 5)
        processed_img = cv2.blur(img, (kernel_size, kernel_size))
    elif operation == "Sobel Edge Detection":
        dx = params.get("dx", 1)
        dy = params.get("dy", 1)
        sobelx = cv2.Sobel(img, cv2.CV_64F, dx, 0, ksize=5)
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, dy, ksize=5)
        processed_img = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
        processed_img = np.uint8(np.absolute(processed_img))
    elif operation == "Laplacian Edge Detection":
        processed_img = cv2.Laplacian(img, cv2.CV_64F)
        processed_img = np.uint8(np.absolute(processed_img))
    elif operation == "Dilation":
        kernel_size = params.get("kernel_size", 5)
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        processed_img = cv2.dilate(img, kernel, iterations=1)
    elif operation == "Erosion":
        kernel_size = params.get("kernel_size", 5)
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        processed_img = cv2.erode(img, kernel, iterations=1)
    elif operation == "Opening":
        kernel_size = params.get("kernel_size", 5)
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        processed_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    elif operation == "Closing":
        kernel_size = params.get("kernel_size", 5)
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        processed_img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    
    # Enhancement
    elif operation == "Histogram Equalization":
        # Convert to YUV for better results
        img_yuv = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
        img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
        processed_img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
    elif operation == "Contrast Stretching":
        # Simple contrast stretching
        min_val = np.min(img)
        max_val = np.max(img)
        processed_img = (img - min_val) * (255.0 / (max_val - min_val))
        processed_img = processed_img.astype(np.uint8)
    elif operation == "Sharpening":
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        processed_img = cv2.filter2D(img, -1, kernel)
    
    # Edge Detection
    elif operation == "Canny Edge Detection":
        threshold1 = params.get("threshold1", 100)
        threshold2 = params.get("threshold2", 200)
        processed_img = cv2.Canny(img, threshold1, threshold2)
        # Convert to 3 channels for consistent display
        processed_img = cv2.cvtColor(processed_img, cv2.COLOR_GRAY2RGB)
    
    return processed_img

# Main application
def main():
    st.title("🖼️ Image Processing Toolkit")
    st.markdown("---")
    
    # Sidebar - Operations
    with st.sidebar:
        st.header("Operations")
        
        # File upload
        uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp"])
        
        if uploaded_file is not None:
            # Read image
            file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
            img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Store in session state
            st.session_state.img = img
            st.session_state.uploaded_file = uploaded_file
            st.session_state.img_info = get_image_info(img, uploaded_file)
        
        # Operation categories
        operation_category = st.selectbox(
            "Select Operation Category",
            ["Color Conversions", "Transformations", "Filtering & Morphology", "Enhancement", "Edge Detection", "Compression"]
        )
        
        # Parameters based on operation category
        params = {}
        
        if operation_category == "Color Conversions":
            operation = st.selectbox(
                "Select Operation",
                ["RGB to BGR", "BGR to RGB", "RGB to HSV", "HSV to RGB", "RGB to YCbCr", "YCbCr to RGB", "RGB to Grayscale"]
            )
        
        elif operation_category == "Transformations":
            operation = st.selectbox(
                "Select Operation",
                ["Rotation", "Scaling", "Translation"]
            )
            
            if operation == "Rotation":
                params["angle"] = st.slider("Rotation Angle", -180, 180, 0)
            elif operation == "Scaling":
                params["scale"] = st.slider("Scale Factor", 0.1, 3.0, 1.0, 0.1)
            elif operation == "Translation":
                params["tx"] = st.slider("X Translation", -100, 100, 0)
                params["ty"] = st.slider("Y Translation", -100, 100, 0)
        
        elif operation_category == "Filtering & Morphology":
            operation = st.selectbox(
                "Select Operation",
                ["Gaussian Blur", "Median Blur", "Mean Blur", "Sobel Edge Detection", "Laplacian Edge Detection", 
                 "Dilation", "Erosion", "Opening", "Closing"]
            )
            
            if operation in ["Gaussian Blur", "Median Blur", "Mean Blur", "Dilation", "Erosion", "Opening", "Closing"]:
                params["kernel_size"] = st.slider("Kernel Size", 1, 15, 5, 2)
            elif operation == "Sobel Edge Detection":
                params["dx"] = st.slider("dx", 0, 2, 1)
                params["dy"] = st.slider("dy", 0, 2, 1)
        
        elif operation_category == "Enhancement":
            operation = st.selectbox(
                "Select Operation",
                ["Histogram Equalization", "Contrast Stretching", "Sharpening"]
            )
        
        elif operation_category == "Edge Detection":
            operation = st.selectbox(
                "Select Operation",
                ["Canny Edge Detection"]
            )
            
            if operation == "Canny Edge Detection":
                params["threshold1"] = st.slider("Threshold 1", 0, 255, 100)
                params["threshold2"] = st.slider("Threshold 2", 0, 255, 200)
        
        elif operation_category == "Compression":
            operation = st.selectbox(
                "Select Operation",
                ["JPEG Compression", "PNG Compression", "BMP Compression"]
            )
        
        # Apply operation button
        apply_button = st.button("Apply Operation")
        
        # Save processed image
        if st.session_state.processed_img is not None:
            # Convert to PIL image
            processed_pil = Image.fromarray(st.session_state.processed_img)
            
            # Save in different formats
            buf = io.BytesIO()
            if operation_category == "Compression":
                if operation == "JPEG Compression":
                    quality = st.slider("JPEG Quality", 1, 100, 90)
                    processed_pil.save(buf, format="JPEG", quality=quality)
                    ext = "jpg"
                elif operation == "PNG Compression":
                    compression = st.slider("PNG Compression", 0, 9, 3)
                    processed_pil.save(buf, format="PNG", compress_level=compression)
                    ext = "png"
                elif operation == "BMP Compression":
                    processed_pil.save(buf, format="BMP")
                    ext = "bmp"
            else:
                processed_pil.save(buf, format="PNG")
                ext = "png"
            
            # Download button
            st.download_button(
                label="Download Processed Image",
                data=buf.getvalue(),
                file_name=f"processed_image.{ext}",
                mime=f"image/{ext}"
            )
    
    # Main content area
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Original Image")
        if st.session_state.img is not None:
            st.image(st.session_state.img, use_container_width=True)
            st.write("Image Information:")
            for key, value in st.session_state.img_info.items():
                st.write(f"{key}: {value}")
    
    with col2:
        st.header("Processed Image")
        if apply_button and st.session_state.img is not None:
            with st.spinner("Applying operation..."):
                processed_img = apply_operation(st.session_state.img, operation, params)
                st.session_state.processed_img = processed_img
                st.success("Operation applied successfully!")
        
        if st.session_state.processed_img is not None:
            st.image(st.session_state.processed_img, use_container_width=True)
            
            # Display processed image info
            processed_info = get_image_info(st.session_state.processed_img, st.session_state.uploaded_file)
            st.write("Processed Image Information:")
            for key, value in processed_info.items():
                st.write(f"{key}: {value}")
    
    # Status bar
    st.markdown("---")
    if st.session_state.img is not None:
        st.write(f"Status: Image loaded | Dimensions: {st.session_state.img_info['Dimensions']} | "
                f"Channels: {st.session_state.img_info['Channels']} | "
                f"File Size: {st.session_state.img_info['File Size']} | "
                f"Format: {st.session_state.img_info['File Format']}")
    else:
        st.write("Status: No image loaded. Please upload an image to begin.")

if __name__ == "__main__":
    main()
