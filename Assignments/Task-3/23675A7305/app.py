import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
import os

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="Image Processing Toolkit",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- STYLES --------------------
st.markdown("""
    <style>
        .stApp { background: linear-gradient(120deg, #f093fb, #f5576c); }
        h1, h2, h3, h4 { color: #fff !important; text-align: center; }
        .sidebar .sidebar-content { background: #141E30; color: white; }
    </style>
""", unsafe_allow_html=True)

# -------------------- HELPER --------------------
def to_display(img):
    """Convert OpenCV output to safe format for Streamlit display."""
    if img is None:
        return None
    if img.dtype != "uint8":
        img = cv2.convertScaleAbs(img)  # Scale floats/negatives to 0–255
    if len(img.shape) == 2:  # grayscale → convert to RGB
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    return img

def image_info(img, file_name=None):
    """Return basic image info."""
    h, w = img.shape[:2]
    c = 1 if len(img.shape) == 2 else img.shape[2]
    size_kb = None
    if file_name:
        size_kb = os.path.getsize(file_name) / 1024
    return h, w, c, size_kb

# -------------------- TITLE --------------------
st.title("🎨 Interactive Image Processing Toolkit")
st.markdown("**Upload an image using the button below to get started.**")

# -------------------- FILE UPLOAD --------------------
uploaded_file = st.file_uploader("📂 Upload an Image", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file is None:
    st.info("👆 Please upload an image to proceed.")
    st.stop()

# -------------------- LOAD IMAGE --------------------
image = Image.open(uploaded_file).convert("RGB")
orig_image = np.array(image)
proc_image = orig_image.copy()

# -------------------- SIDEBAR --------------------
st.sidebar.header("🎛️ Operations")
option = st.sidebar.radio("Select Category:", [
    "Color Conversion", "Transformations", "Filtering & Morphology",
    "Enhancement", "Edge Detection", "Compression"
])

# ----- COLOR CONVERSIONS -----
if option == "Color Conversion":
    conv = st.sidebar.selectbox("Choose conversion:", ["Gray", "HSV", "YCbCr"])
    if conv == "Gray":
        proc_image = cv2.cvtColor(orig_image, cv2.COLOR_RGB2GRAY)
    elif conv == "HSV":
        proc_image = cv2.cvtColor(orig_image, cv2.COLOR_RGB2HSV)
    elif conv == "YCbCr":
        proc_image = cv2.cvtColor(orig_image, cv2.COLOR_RGB2YCrCb)

# ----- TRANSFORMATIONS -----
elif option == "Transformations":
    trans = st.sidebar.selectbox("Choose transformation:", ["Rotate", "Scale", "Translate", "Affine", "Perspective"])
    (h, w) = orig_image.shape[:2]

    if trans == "Rotate":
        angle = st.sidebar.slider("Rotation Angle", -180, 180, 45)
        M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1.0)
        proc_image = cv2.warpAffine(orig_image, M, (w, h))

    elif trans == "Scale":
        scale = st.sidebar.slider("Scale Factor", 0.1, 2.0, 1.0)
        proc_image = cv2.resize(orig_image, None, fx=scale, fy=scale)

    elif trans == "Translate":
        tx = st.sidebar.slider("Shift X", -100, 100, 20)
        ty = st.sidebar.slider("Shift Y", -100, 100, 20)
        M = np.float32([[1, 0, tx], [0, 1, ty]])
        proc_image = cv2.warpAffine(orig_image, M, (w, h))

    elif trans == "Affine":
        pts1 = np.float32([[0,0],[w-1,0],[0,h-1]])
        pts2 = np.float32([[0,h*0.33],[w*0.85,h*0.25],[w*0.15,h*0.7]])
        M = cv2.getAffineTransform(pts1, pts2)
        proc_image = cv2.warpAffine(orig_image, M, (w, h))

    elif trans == "Perspective":
        pts1 = np.float32([[0,0],[w-1,0],[0,h-1],[w-1,h-1]])
        pts2 = np.float32([[0,0],[w-1,0],[int(w*0.33),h-1],[int(w*0.66),h-1]])
        M = cv2.getPerspectiveTransform(pts1, pts2)
        proc_image = cv2.warpPerspective(orig_image, M, (w, h))

# ----- FILTERING & MORPHOLOGY -----
elif option == "Filtering & Morphology":
    choice = st.sidebar.selectbox("Choose operation:", [
        "Gaussian Blur", "Median Blur", "Mean Blur",
        "Sobel", "Laplacian", "Dilation", "Erosion", "Opening", "Closing"
    ])
    gray = cv2.cvtColor(orig_image, cv2.COLOR_RGB2GRAY)

    if choice == "Gaussian Blur":
        k = st.sidebar.slider("Kernel Size", 1, 15, 3, step=2)
        proc_image = cv2.GaussianBlur(orig_image, (k, k), 0)

    elif choice == "Median Blur":
        k = st.sidebar.slider("Kernel Size", 1, 15, 3, step=2)
        proc_image = cv2.medianBlur(orig_image, k)

    elif choice == "Mean Blur":
        k = st.sidebar.slider("Kernel Size", 1, 15, 3, step=2)
        proc_image = cv2.blur(orig_image, (k, k))

    elif choice == "Sobel":
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        proc_image = cv2.magnitude(sobelx, sobely)

    elif choice == "Laplacian":
        proc_image = cv2.Laplacian(gray, cv2.CV_64F)

    elif choice in ["Dilation", "Erosion", "Opening", "Closing"]:
        k = st.sidebar.slider("Kernel Size", 1, 15, 3)
        kernel = np.ones((k, k), np.uint8)
        if choice == "Dilation":
            proc_image = cv2.dilate(orig_image, kernel, iterations=1)
        elif choice == "Erosion":
            proc_image = cv2.erode(orig_image, kernel, iterations=1)
        elif choice == "Opening":
            proc_image = cv2.morphologyEx(orig_image, cv2.MORPH_OPEN, kernel)
        elif choice == "Closing":
            proc_image = cv2.morphologyEx(orig_image, cv2.MORPH_CLOSE, kernel)

# ----- ENHANCEMENT -----
elif option == "Enhancement":
    enh = st.sidebar.selectbox("Choose enhancement:", ["Histogram Equalization", "Sharpen"])
    if enh == "Histogram Equalization":
        gray = cv2.cvtColor(orig_image, cv2.COLOR_RGB2GRAY)
        proc_image = cv2.equalizeHist(gray)
    elif enh == "Sharpen":
        kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        proc_image = cv2.filter2D(orig_image, -1, kernel)

# ----- EDGE DETECTION -----
elif option == "Edge Detection":
    edge = st.sidebar.selectbox("Choose method:", ["Sobel", "Canny", "Laplacian"])
    gray = cv2.cvtColor(orig_image, cv2.COLOR_RGB2GRAY)

    if edge == "Sobel":
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        proc_image = cv2.magnitude(sobelx, sobely)
    elif edge == "Canny":
        t1 = st.sidebar.slider("Threshold1", 50, 200, 100)
        t2 = st.sidebar.slider("Threshold2", 100, 300, 200)
        proc_image = cv2.Canny(gray, t1, t2)
    elif edge == "Laplacian":
        proc_image = cv2.Laplacian(gray, cv2.CV_64F)

# ----- COMPRESSION -----
elif option == "Compression":
    fmt = st.sidebar.selectbox("Save format:", ["JPEG", "PNG", "BMP"])
    buf = io.BytesIO()
    pil_img = Image.fromarray(orig_image)
    pil_img.save(buf, format=fmt)
    size_kb = len(buf.getvalue()) / 1024
    st.sidebar.write(f"Compressed size: {size_kb:.2f} KB")

# -------------------- DISPLAY --------------------
col1, col2 = st.columns(2)
with col1:
    st.subheader("🖼️ Original Image")
    st.image(orig_image, use_container_width=True)
with col2:
    st.subheader("✨ Processed Image")
    st.image(to_display(proc_image), use_container_width=True)

# -------------------- STATUS BAR --------------------
h, w, c, _ = image_info(orig_image)
st.markdown(f"""
**📊 Image Info:**  
- Dimensions: {w} x {h}  
- Channels: {c}  
- Format: {uploaded_file.type}  
""")

# -------------------- DOWNLOAD --------------------
st.download_button(
    label="💾 Download Processed Image",
    data=cv2.imencode('.png', cv2.cvtColor(to_display(proc_image), cv2.COLOR_RGB2BGR))[1].tobytes(),
    file_name="processed.png",
    mime="image/png"
)
