import streamlit as st
import cv2
import numpy as np
import os
from PIL import Image
import tempfile

# ----------------------------
# 🎯 Utility Functions
# ----------------------------

def load_image_as_array(uploaded_file):
    """Load uploaded image into NumPy array (BGR format for OpenCV)"""
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    return img

def get_image_info(img, format="Unknown", file_size=0):
    """Return image metadata for status bar"""
    h, w = img.shape[:2]
    c = img.shape[2] if len(img.shape) == 3 else 1
    dpi = "N/A"  # Streamlit doesn't provide DPI from upload
    return {
        "Dimensions": f"{h} x {w} x {c}",
        "DPI": dpi,
        "Format": format,
        "File Size": f"{file_size / 1024:.1f} KB" if file_size else "N/A"
    }

def convert_color_space(img, target_space):
    """Convert image color space"""
    conversions = {
        "RGB → BGR": cv2.cvtColor(img, cv2.COLOR_RGB2BGR),
        "BGR → RGB": cv2.cvtColor(img, cv2.COLOR_BGR2RGB),
        "RGB → HSV": cv2.cvtColor(img, cv2.COLOR_RGB2HSV),
        "HSV → RGB": cv2.cvtColor(img, cv2.COLOR_HSV2RGB),
        "RGB → YCrCb": cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb),
        "YCrCb → RGB": cv2.cvtColor(img, cv2.COLOR_YCrCb2RGB),
        "RGB → Grayscale": cv2.cvtColor(img, cv2.COLOR_RGB2GRAY),
        "BGR → Grayscale": cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
    }
    return conversions.get(target_space, img)

def apply_transformation(img, transform_type, **params):
    """Apply geometric transformations"""
    h, w = img.shape[:2]
    
    if transform_type == "Rotation":
        angle = params.get("angle", 0)
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        return cv2.warpAffine(img, M, (w, h))
    
    elif transform_type == "Scaling":
        scale = params.get("scale", 1.0)
        new_w, new_h = int(w * scale), int(h * scale)
        return cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
    
    elif transform_type == "Translation":
        tx, ty = params.get("tx", 0), params.get("ty", 0)
        M = np.float32([[1, 0, tx], [0, 1, ty]])
        return cv2.warpAffine(img, M, (w, h))
    
    elif transform_type == "Affine":
        # Example: skew top-right corner
        pts1 = np.float32([[50,50],[200,50],[50,200]])
        pts2 = np.float32([[10,100],[200,50],[100,250]])
        M = cv2.getAffineTransform(pts1, pts2)
        return cv2.warpAffine(img, M, (w, h))
    
    elif transform_type == "Perspective":
        pts1 = np.float32([[0,0],[w,0],[0,h],[w,h]])
        pts2 = np.float32([[0,0],[w,50],[50,h],[w-50,h-50]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        return cv2.warpPerspective(img, M, (w, h))
    
    return img

def apply_filter(img, filter_type, kernel_size=3):
    """Apply filters and morphology"""
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img.copy()
    
    if filter_type == "Gaussian Blur":
        return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
    elif filter_type == "Median Blur":
        return cv2.medianBlur(img, kernel_size)
    elif filter_type == "Mean Blur":
        return cv2.blur(img, (kernel_size, kernel_size))
    elif filter_type == "Sobel X":
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=kernel_size)
        return np.uint8(np.absolute(sobelx))
    elif filter_type == "Sobel Y":
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=kernel_size)
        return np.uint8(np.absolute(sobely))
    elif filter_type == "Laplacian":
        lap = cv2.Laplacian(gray, cv2.CV_64F)
        return np.uint8(np.absolute(lap))
    elif filter_type == "Dilation":
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.dilate(img, kernel, iterations=1)
    elif filter_type == "Erosion":
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.erode(img, kernel, iterations=1)
    elif filter_type == "Opening":
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    elif filter_type == "Closing":
        kernel = np.ones((kernel_size, kernel_size), np.uint8)
        return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    return img

def enhance_image(img, method, **params):
    """Apply enhancement techniques"""
    if method == "Histogram Equalization":
        if len(img.shape) == 3:
            ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
            ycrcb[:,:,0] = cv2.equalizeHist(ycrcb[:,:,0])
            return cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR)
        else:
            return cv2.equalizeHist(img)
    elif method == "Contrast Stretching":
        # Simple min-max normalization
        a, b = np.min(img), np.max(img)
        stretched = 255 * (img.astype(np.float32) - a) / (b - a + 1e-5)
        return np.clip(stretched, 0, 255).astype(np.uint8)
    elif method == "Sharpening":
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        return cv2.filter2D(img, -1, kernel)
    return img

def detect_edges(img, method, **params):
    """Apply edge detection"""
    if len(img.shape) == 3:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img.copy()
    
    if method == "Canny":
        low = params.get("low", 50)
        high = params.get("high", 150)
        return cv2.Canny(gray, low, high)
    elif method == "Sobel":
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sobel = np.hypot(sobelx, sobely)
        return np.uint8(sobel / sobel.max() * 255)
    elif method == "Laplacian":
        lap = cv2.Laplacian(gray, cv2.CV_64F)
        return np.uint8(np.absolute(lap))
    return img

def save_image(img, format="PNG"):
    """Save processed image to temp file for download"""
    _, ext = format.lower(), format.lower()
    if format == "JPG": ext = "jpg"
    if format == "PNG": ext = "png"
    if format == "BMP": ext = "bmp"

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{ext}") as tmp:
        if len(img.shape) == 3 and img.shape[2] == 3:
            if format != "BMP":
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if len(img.shape) == 2:
            img_pil = Image.fromarray(img)
        else:
            img_pil = Image.fromarray(img)
        img_pil.save(tmp.name, format=format)
        return tmp.name

# ----------------------------
# 🖥️ Streamlit App
# ----------------------------

st.set_page_config(page_title="Image Processing Toolkit", layout="wide")

st.title("🎨 Image Processing Toolkit")
st.markdown("Upload an image and apply transformations, filters, enhancements, and more — all in real-time!")

# Sidebar: Operations Menu
st.sidebar.title("🔧 Operations")

# File Handling
st.sidebar.subheader("📁 File")
uploaded_file = st.sidebar.file_uploader("Open Image", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file:
    # Load original image
    original_img = load_image_as_array(uploaded_file)
    # Convert to RGB for display in Streamlit
    original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
    st.session_state.original_img = original_img
    st.session_state.original_img_rgb = original_img_rgb
    st.session_state.file_format = uploaded_file.type.split("/")[-1].upper()
    st.session_state.file_size = len(uploaded_file.getvalue())
else:
    st.info("👈 Please upload an image to begin.")
    st.stop()

# Initialize processed image
if "processed_img" not in st.session_state:
    st.session_state.processed_img = original_img.copy()
    st.session_state.processed_img_rgb = original_img_rgb.copy()

# Sidebar: Image Info
st.sidebar.subheader("📊 Image Info")
if st.sidebar.button("Show Info"):
    info = get_image_info(original_img, st.session_state.file_format, st.session_state.file_size)
    for k, v in info.items():
        st.sidebar.text(f"{k}: {v}")

# Sidebar: Color Conversions
st.sidebar.subheader("🎨 Color Conversions")
color_ops = [
    "RGB → BGR",
    "BGR → RGB",
    "RGB → HSV",
    "HSV → RGB",
    "RGB → YCrCb",
    "YCrCb → RGB",
    "RGB → Grayscale",
    "BGR → Grayscale"
]
selected_color_op = st.sidebar.selectbox("Select Conversion", color_ops)
if st.sidebar.button("Apply Color Conversion"):
    img_temp = original_img.copy()
    if "BGR" in selected_color_op:
        img_temp = cv2.cvtColor(img_temp, cv2.COLOR_BGR2RGB)  # ensure RGB input
    result = convert_color_space(img_temp, selected_color_op)
    if len(result.shape) == 2:  # grayscale
        st.session_state.processed_img = result
        st.session_state.processed_img_rgb = result
    else:
        st.session_state.processed_img = cv2.cvtColor(result, cv2.COLOR_RGB2BGR) if "→ RGB" in selected_color_op else result
        st.session_state.processed_img_rgb = result if "→ RGB" in selected_color_op else cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# Sidebar: Transformations
st.sidebar.subheader("🔄 Transformations")
transform_ops = ["Rotation", "Scaling", "Translation", "Affine", "Perspective"]
selected_transform = st.sidebar.selectbox("Select Transform", transform_ops)

if selected_transform == "Rotation":
    angle = st.sidebar.slider("Rotation Angle", -180, 180, 0)
    if st.sidebar.button("Apply Rotation"):
        st.session_state.processed_img = apply_transformation(st.session_state.processed_img, "Rotation", angle=angle)
        st.session_state.processed_img_rgb = cv2.cvtColor(st.session_state.processed_img, cv2.COLOR_BGR2RGB) if len(st.session_state.processed_img.shape) == 3 else st.session_state.processed_img

elif selected_transform == "Scaling":
    scale = st.sidebar.slider("Scale Factor", 0.1, 3.0, 1.0, 0.1)
    if st.sidebar.button("Apply Scaling"):
        st.session_state.processed_img = apply_transformation(st.session_state.processed_img, "Scaling", scale=scale)
        if len(st.session_state.processed_img.shape) == 3:
            st.session_state.processed_img_rgb = cv2.cvtColor(st.session_state.processed_img, cv2.COLOR_BGR2RGB)
        else:
            st.session_state.processed_img_rgb = st.session_state.processed_img

elif selected_transform == "Translation":
    tx = st.sidebar.slider("Translate X", -200, 200, 0)
    ty = st.sidebar.slider("Translate Y", -200, 200, 0)
    if st.sidebar.button("Apply Translation"):
        st.session_state.processed_img = apply_transformation(st.session_state.processed_img, "Translation", tx=tx, ty=ty)
        st.session_state.processed_img_rgb = cv2.cvtColor(st.session_state.processed_img, cv2.COLOR_BGR2RGB) if len(st.session_state.processed_img.shape) == 3 else st.session_state.processed_img

else:
    if st.sidebar.button(f"Apply {selected_transform}"):
        st.session_state.processed_img = apply_transformation(st.session_state.processed_img, selected_transform)
        if len(st.session_state.processed_img.shape) == 3:
            st.session_state.processed_img_rgb = cv2.cvtColor(st.session_state.processed_img, cv2.COLOR_BGR2RGB)
        else:
            st.session_state.processed_img_rgb = st.session_state.processed_img

# Sidebar: Filtering & Morphology
st.sidebar.subheader("🖌️ Filtering & Morphology")
filter_ops = [
    "Gaussian Blur", "Median Blur", "Mean Blur",
    "Sobel X", "Sobel Y", "Laplacian",
    "Dilation", "Erosion", "Opening", "Closing"
]
selected_filter = st.sidebar.selectbox("Select Filter", filter_ops)
kernel_size = st.sidebar.slider("Kernel Size", 3, 15, 3, 2)  # odd numbers only

if st.sidebar.button("Apply Filter"):
    st.session_state.processed_img = apply_filter(st.session_state.processed_img, selected_filter, kernel_size)
    if len(st.session_state.processed_img.shape) == 2:
        st.session_state.processed_img_rgb = st.session_state.processed_img
    else:
        st.session_state.processed_img_rgb = cv2.cvtColor(st.session_state.processed_img, cv2.COLOR_BGR2RGB)

# Sidebar: Enhancement
st.sidebar.subheader("✨ Enhancement")
enhance_ops = ["Histogram Equalization", "Contrast Stretching", "Sharpening"]
selected_enhance = st.sidebar.selectbox("Select Enhancement", enhance_ops)

if st.sidebar.button("Apply Enhancement"):
    st.session_state.processed_img = enhance_image(st.session_state.processed_img, selected_enhance)
    if len(st.session_state.processed_img.shape) == 3:
        st.session_state.processed_img_rgb = cv2.cvtColor(st.session_state.processed_img, cv2.COLOR_BGR2RGB)
    else:
        st.session_state.processed_img_rgb = st.session_state.processed_img

# Sidebar: Edge Detection
st.sidebar.subheader("🔍 Edge Detection")
edge_ops = ["Canny", "Sobel", "Laplacian"]
selected_edge = st.sidebar.selectbox("Select Edge Detector", edge_ops)

if selected_edge == "Canny":
    low_thresh = st.sidebar.slider("Canny Low Threshold", 0, 255, 50)
    high_thresh = st.sidebar.slider("Canny High Threshold", 0, 255, 150)
    if st.sidebar.button("Apply Canny"):
        st.session_state.processed_img = detect_edges(st.session_state.processed_img, "Canny", low=low_thresh, high=high_thresh)
        st.session_state.processed_img_rgb = st.session_state.processed_img  # already grayscale

else:
    if st.sidebar.button(f"Apply {selected_edge}"):
        st.session_state.processed_img = detect_edges(st.session_state.processed_img, selected_edge)
        st.session_state.processed_img_rgb = st.session_state.processed_img

# Sidebar: Compression & Save
st.sidebar.subheader("💾 Compression & Save")
save_format = st.sidebar.selectbox("Save Format", ["PNG", "JPG", "BMP"])
if st.sidebar.button("💾 Save Processed Image"):
    saved_path = save_image(st.session_state.processed_img, save_format)
    with open(saved_path, "rb") as f:
        st.sidebar.download_button(
            label=f"Download as {save_format}",
            data=f,
            file_name=f"processed_image.{save_format.lower()}",
            mime=f"image/{save_format.lower()}"
        )
    os.unlink(saved_path)  # cleanup

# ----------------------------
# 🖼️ Display Area
# ----------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("🖼️ Original Image")
    st.image(st.session_state.original_img_rgb, use_container_width=True)

with col2:
    st.subheader("🛠️ Processed Image")
    st.image(st.session_state.processed_img_rgb, use_container_width=True)

# ----------------------------
# 📊 Status Bar
# ----------------------------

st.markdown("---")
st.subheader("📋 Status Bar")

# Get current processed image info
current_info = get_image_info(
    st.session_state.processed_img,
    save_format,
    os.path.getsize(save_image(st.session_state.processed_img, save_format)) if "processed_img" in st.session_state else 0
)

cols = st.columns(4)
cols[0].metric("Dimensions", current_info["Dimensions"])
cols[1].metric("DPI", current_info["DPI"])
cols[2].metric("Format", current_info["Format"])
cols[3].metric("File Size", current_info["File Size"])

# ----------------------------
# 🚀 Bonus: Split View Toggle
# ----------------------------

st.sidebar.markdown("---")
st.sidebar.subheader("🚀 Bonus Features")

if st.sidebar.checkbox("SplitOptions: Half Original / Half Processed"):
    h_orig = st.session_state.original_img_rgb.shape[0]
    w_orig = st.session_state.original_img_rgb.shape[1]
    half_w = w_orig // 2
    
    # Ensure both images are same size
    processed_resized = cv2.resize(st.session_state.processed_img_rgb, (w_orig, h_orig)) if st.session_state.processed_img_rgb.shape[:2] != (h_orig, w_orig) else st.session_state.processed_img_rgb
    
    if len(st.session_state.original_img_rgb.shape) == 2:
        st.session_state.original_img_rgb = cv2.cvtColor(st.session_state.original_img_rgb, cv2.COLOR_GRAY2RGB)
    if len(processed_resized.shape) == 2:
        processed_resized = cv2.cvtColor(processed_resized, cv2.COLOR_GRAY2RGB)
    
    split_img = np.hstack((
        st.session_state.original_img_rgb[:, :half_w],
        processed_resized[:, half_w:]
    ))
    st.image(split_img, caption="SplitOptions View", use_container_width=True)

# ----------------------------
# 🎥 Bonus: Real-time Webcam (Optional)
# ----------------------------

# Uncomment below to enable webcam (requires camera access)

# if st.sidebar.checkbox("🎥 Real-time Webcam Mode"):
#     st.subheader("Webcam Feed (Processing in Real-Time)")
#     FRAME_WINDOW = st.image([])
#     camera = cv2.VideoCapture(0)
#     while True:
#         _, frame = camera.read()
#         if frame is None:
#             break
#         # Apply current operation to frame (simplified: grayscale)
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
#         FRAME_WINDOW.image(gray)
#     camera.release()

# ----------------------------
# 🧾 Exit Button
# ----------------------------

if st.sidebar.button("🚪 Exit App"):
    st.experimental_rerun()  # Clears session state on reload
    st.stop()

# ----------------------------
# ✅ Footer
# ----------------------------

st.sidebar.markdown("---")
st.sidebar.caption("Image Processing Toolkit v1.0 | Module 1 Assignment")
