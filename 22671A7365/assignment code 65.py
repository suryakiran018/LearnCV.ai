import streamlit as st
import cv2
import numpy as np
from PIL import Image
import base64

# ---------------- Utility Functions ----------------
def load_image(uploaded_file):
    """Convert uploaded image to numpy array"""
    img = Image.open(uploaded_file)
    return np.array(img)

def show_info(img, file=None):
    h, w = img.shape[:2]
    c = 1 if len(img.shape) == 2 else img.shape[2]
    details = f"{w} x {h}, Channels: {c}"
    if file:
        fmt = file['type'].split('/')[-1].upper()
        size = file['size'] // 1024
        details += f", Format: {fmt}, Size: {size} KB"
    return details

def download_link(buf, ext="png"):
    b64 = base64.b64encode(buf).decode()
    return f'<a href="data:file/{ext};base64,{b64}" download="processed.{ext}">Download</a>'

def save_image(img, typ="PNG"):
    ext = {"PNG": ".png", "JPG": ".jpg", "BMP": ".bmp"}[typ]
    _, buf = cv2.imencode(ext, cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    return buf

# ---------------- Core Operations ----------------
def color_ops(img, mode):
    codes = {
        "RGB <-> BGR": cv2.COLOR_RGB2BGR,
        "RGB <-> HSV": cv2.COLOR_RGB2HSV,
        "RGB <-> YCbCr": cv2.COLOR_RGB2YCrCb,
        "RGB <-> Gray": cv2.COLOR_RGB2GRAY
    }
    return cv2.cvtColor(img, codes[mode])

def rotate(img, angle):
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((w//2, h//2), angle, 1.0)
    return cv2.warpAffine(img, M, (w, h))

def scale(img, factor):
    return cv2.resize(img, None, fx=factor, fy=factor)

def translate(img, dx, dy):
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    h, w = img.shape[:2]
    return cv2.warpAffine(img, M, (w, h))

def affine(img):
    src = np.float32([[0, 0], [50, 50], [100, 10]])
    dst = np.float32([[10, 100], [20, 50], [100, 60]])
    M = cv2.getAffineTransform(src, dst)
    return cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

def perspective(img):
    h, w = img.shape[:2]
    src = np.float32([[0, 0], [w-1, 0], [0, h-1], [w-1, h-1]])
    dst = np.float32([[0, 0], [w-1, 0], [int(w*0.3), h-1], [int(w*0.7), h-1]])
    M = cv2.getPerspectiveTransform(src, dst)
    return cv2.warpPerspective(img, M, (w, h))

def filters(img, method, k=3):
    if method == "Gaussian":
        return cv2.GaussianBlur(img, (k, k), 0)
    if method == "Mean":
        return cv2.blur(img, (k, k))
    if method == "Median":
        return cv2.medianBlur(img, k)
    return img

def morph(img, kind, k=3):
    kernel = np.ones((k, k), np.uint8)
    ops = {
        "Dilation": cv2.dilate,
        "Erosion": cv2.erode,
        "Opening": lambda im, k: cv2.morphologyEx(im, cv2.MORPH_OPEN, k),
        "Closing": lambda im, k: cv2.morphologyEx(im, cv2.MORPH_CLOSE, k),
    }
    if kind in ops:
        return ops[kind](img, kernel)
    return img

def enhance(img, method):
    if method == "Equalize Hist":
        if len(img.shape) == 2:
            return cv2.equalizeHist(img)
        yuv = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
        yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
        return cv2.cvtColor(yuv, cv2.COLOR_YUV2RGB)
    if method == "Contrast Stretch":
        a, b = np.min(img), np.max(img)
        return np.uint8((img - a) * 255 / (b - a))
    if method == "Sharpen":
        k = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        return cv2.filter2D(img, -1, k)
    return img

def detect_edges(img, kind, t1=100, t2=200):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    if kind == "Sobel":
        return cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    if kind == "Laplacian":
        return cv2.Laplacian(gray, cv2.CV_64F)
    if kind == "Canny":
        return cv2.Canny(img, t1, t2)
    return img

# ---------------- Streamlit App ----------------
st.set_page_config(page_title="CV Toolkit", layout="wide")
st.title("📷 Computer Vision Toolkit")
st.caption("All-in-one Image Processing App | OpenCV + Streamlit")

# Upload section
with st.sidebar:
    st.subheader("📤 Upload Image")
    file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "bmp"])
    if file:
        img = load_image(file)
        file_meta = {"filename": file.name, "type": file.type, "size": file.size}
    else:
        st.info("Using default image: sample.jpg")
        img = cv2.cvtColor(cv2.imread("my_photo.jpg"), cv2.COLOR_BGR2RGB)
        file_meta = {"filename": "my_photo.jpg", "type": "jpg", "size": img.nbytes}

# Tabs for features
tabs = st.tabs(["Info", "Colors", "Transform", "Filters", "Enhance", "Edges", "Save"])

# Info
with tabs[0]:
    st.write("**Image Info:**", show_info(img, file_meta))
    st.image(img, caption="Original", channels="RGB")

# Colors
with tabs[1]:
    choice = st.radio("Choose mode", ["RGB <-> BGR", "RGB <-> HSV", "RGB <-> YCbCr", "RGB <-> Gray"])
    proc = color_ops(img, choice)
    st.image(proc, caption=choice, channels="RGB" if len(proc.shape) == 3 else "GRAY")

# Transform
with tabs[2]:
    action = st.selectbox("Transformation", ["Rotate", "Scale", "Translate", "Affine", "Perspective"])
    if action == "Rotate":
        ang = st.slider("Angle", -180, 180, 0)
        proc = rotate(img, ang)
    elif action == "Scale":
        sc = st.slider("Factor", 0.1, 3.0, 1.0)
        proc = scale(img, sc)
    elif action == "Translate":
        dx = st.slider("Shift X", -100, 100, 0)
        dy = st.slider("Shift Y", -100, 100, 0)
        proc = translate(img, dx, dy)
    elif action == "Affine":
        proc = affine(img)
    elif action == "Perspective":
        proc = perspective(img)
    st.image(proc, caption=action)

# Filters
with tabs[3]:
    kind = st.selectbox("Filter / Morph", ["Gaussian", "Mean", "Median", "Dilation", "Erosion", "Opening", "Closing"])
    k = st.slider("Kernel size", 3, 15, 3, step=2)
    if kind in ["Gaussian", "Mean", "Median"]:
        proc = filters(img, kind, k)
    else:
        proc = morph(img, kind, k)
    st.image(proc, caption=kind)

# Enhance
with tabs[4]:
    method = st.radio("Enhancement", ["Equalize Hist", "Contrast Stretch", "Sharpen"])
    proc = enhance(img, method)
    st.image(proc, caption=method)

# Edges
with tabs[5]:
    kind = st.radio("Edge Detection", ["Sobel", "Laplacian", "Canny"])
    if kind == "Canny":
        t1 = st.slider("Threshold 1", 0, 255, 100)
        t2 = st.slider("Threshold 2", 0, 255, 200)
        proc = detect_edges(img, "Canny", t1, t2)
    else:
        proc = detect_edges(img, kind)
    st.image(proc, caption=kind, channels="GRAY")

# Save
with tabs[6]:
    typ = st.radio("Save as", ["PNG", "JPG", "BMP"])
    buf = save_image(img, typ)
    st.write(f"Compressed Size: {len(buf)//1024} KB")
    st.markdown(download_link(buf, typ.lower()), unsafe_allow_html=True)
