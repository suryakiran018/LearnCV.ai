import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

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

# -------------------- TITLE --------------------
st.title("🎨 Interactive Image Processing Toolkit")
st.markdown("**Upload an image using the button below to get started.**")

# -------------------- FILE UPLOAD --------------------
uploaded_file = st.file_uploader("📂 Upload an Image", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file is None:
    st.info("👆 Please upload an image to proceed.")
    st.stop()

# -------------------- LOAD IMAGE --------------------
image = Image.open(uploaded_file)
orig_image = np.array(image)
proc_image = orig_image.copy()

# -------------------- SIDEBAR --------------------
st.sidebar.header("🎛️ Operations")
option = st.sidebar.radio("Select Category:", [
    "Color Conversion", "Transformations", "Filtering", "Enhancement", "Edge Detection", "Compression"
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
    trans = st.sidebar.selectbox("Choose transformation:", ["Rotate", "Scale", "Translate"])
    if trans == "Rotate":
        angle = st.sidebar.slider("Rotation Angle", -180, 180, 45)
        (h, w) = orig_image.shape[:2]
        M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1.0)
        proc_image = cv2.warpAffine(orig_image, M, (w, h))
    elif trans == "Scale":
        scale = st.sidebar.slider("Scale Factor", 0.1, 2.0, 1.0)
        proc_image = cv2.resize(orig_image, None, fx=scale, fy=scale)
    elif trans == "Translate":
        tx = st.sidebar.slider("Shift X", -100, 100, 20)
        ty = st.sidebar.slider("Shift Y", -100, 100, 20)
        M = np.float32([[1, 0, tx], [0, 1, ty]])
        (h, w) = orig_image.shape[:2]
        proc_image = cv2.warpAffine(orig_image, M, (w, h))

# ----- FILTERING -----
elif option == "Filtering":
    filt = st.sidebar.selectbox("Choose filter:", ["Gaussian", "Median", "Mean"])
    k = st.sidebar.slider("Kernel Size", 1, 15, 3, step=2)
    if filt == "Gaussian":
        proc_image = cv2.GaussianBlur(orig_image, (k, k), 0)
    elif filt == "Median":
        proc_image = cv2.medianBlur(orig_image, k)
    elif filt == "Mean":
        proc_image = cv2.blur(orig_image, (k, k))

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
    if edge == "Sobel":
        proc_image = cv2.Sobel(orig_image, cv2.CV_64F, 1, 1, ksize=5)
    elif edge == "Canny":
        t1 = st.sidebar.slider("Threshold1", 50, 200, 100)
        t2 = st.sidebar.slider("Threshold2", 100, 300, 200)
        proc_image = cv2.Canny(orig_image, t1, t2)
    elif edge == "Laplacian":
        proc_image = cv2.Laplacian(orig_image, cv2.CV_64F)

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
    st.image(orig_image, use_column_width=True)
with col2:
    st.subheader("✨ Processed Image")
    st.image(proc_image, use_column_width=True)

# -------------------- DOWNLOAD --------------------
st.download_button(
    label="💾 Download Processed Image",
    data=cv2.imencode('.png', cv2.cvtColor(proc_image, cv2.COLOR_RGB2BGR))[1].tobytes(),
    file_name="processed.png",
    mime="image/png"
)
