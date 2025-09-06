import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
import os
import tempfile

st.set_page_config(page_title="Image Processing Toolkit", layout="wide")

# ----------------------- Utility Functions -----------------------
@st.cache_data(show_spinner=False)
def load_image(uploaded_file):
    if uploaded_file is None:
        return None
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
    # Convert 4-channel BGRA to BGR for consistency
    if img is not None and img.shape[-1] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    return img


def to_pil(img_bgr):
    if img_bgr is None:
        return None
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return Image.fromarray(img_rgb)


def bytes_from_img(img_bgr, fmt="PNG", quality=95):
    pil = to_pil(img_bgr)
    buf = io.BytesIO()
    if fmt.upper() == "JPG":
        pil.save(buf, format="JPEG", quality=quality)
    else:
        pil.save(buf, format=fmt)
    return buf.getvalue()


def get_image_info(img, uploaded_file=None):
    if img is None:
        return {}
    h, w = img.shape[:2]
    c = 1 if img.ndim == 2 else img.shape[2]
    size = None
    fmt = None
    if uploaded_file is not None:
        try:
            uploaded_file.seek(0)
            data = uploaded_file.read()
            size = len(data)
            fmt = uploaded_file.type
            uploaded_file.seek(0)
        except Exception:
            size = None
    return {"height": h, "width": w, "channels": c, "size_bytes": size, "format": fmt}


# ----------------------- Image Processing Ops -----------------------
# Color conversions

def bgr_to_rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def bgr_to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def bgr_to_hsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def bgr_to_ycbcr(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)  # OpenCV uses YCrCb (close to YCbCr)


def rgb_to_bgr_manual(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Transformations

def rotate_image(img, angle):
    h, w = img.shape[:2]
    M = cv2.getRotationMatrix2D((w/2, h/2), angle, 1)
    return cv2.warpAffine(img, M, (w, h))


def scale_image(img, fx, fy):
    return cv2.resize(img, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)


def translate_image(img, tx, ty):
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    h, w = img.shape[:2]
    return cv2.warpAffine(img, M, (w, h))


def affine_transform(img, src_pts, dst_pts):
    M = cv2.getAffineTransform(np.float32(src_pts), np.float32(dst_pts))
    h, w = img.shape[:2]
    return cv2.warpAffine(img, M, (w, h))


def perspective_transform(img, src_pts, dst_pts):
    M = cv2.getPerspectiveTransform(np.float32(src_pts), np.float32(dst_pts))
    h, w = img.shape[:2]
    return cv2.warpPerspective(img, M, (w, h))

# Bitwise

def bitwise_ops(img1, img2, op):
    # Ensure same size
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    if op == "AND":
        return cv2.bitwise_and(img1, img2)
    if op == "OR":
        return cv2.bitwise_or(img1, img2)
    if op == "XOR":
        return cv2.bitwise_xor(img1, img2)
    if op == "NOT":
        return cv2.bitwise_not(img1)
    return img1

# Filtering & Morphology

def apply_filter(img, mode, ksize):
    if ksize % 2 == 0:
        ksize += 1
    if mode == "Gaussian":
        return cv2.GaussianBlur(img, (ksize, ksize), 0)
    if mode == "Median":
        return cv2.medianBlur(img, ksize)
    if mode == "Mean":
        return cv2.blur(img, (ksize, ksize))
    return img


def edge_sobel(img):
    gray = bgr_to_gray(img)
    dx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    dy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    mag = np.sqrt(dx**2 + dy**2)
    mag = np.uint8(np.clip(mag / mag.max() * 255, 0, 255))
    return mag


def edge_laplacian(img):
    gray = bgr_to_gray(img)
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    lap = np.uint8(np.clip(np.abs(lap), 0, 255))
    return lap


def morphological(img, op, ksize):
    kernel = np.ones((ksize, ksize), np.uint8)
    if op == "Dilation":
        return cv2.dilate(img, kernel, iterations=1)
    if op == "Erosion":
        return cv2.erode(img, kernel, iterations=1)
    if op == "Opening":
        return cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    if op == "Closing":
        return cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    return img

# Enhancement

def histogram_equalization(img):
    if img.ndim == 3:
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        y, cr, cb = cv2.split(ycrcb)
        y_eq = cv2.equalizeHist(y)
        merged = cv2.merge((y_eq, cr, cb))
        return cv2.cvtColor(merged, cv2.COLOR_YCrCb2BGR)
    else:
        return cv2.equalizeHist(img)


def contrast_stretch(img):
    in_min = np.percentile(img, 2)
    in_max = np.percentile(img, 98)
    out = (img - in_min) * (255.0 / (in_max - in_min))
    out = np.clip(out, 0, 255).astype(np.uint8)
    return out


def sharpen(img):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    return cv2.filter2D(img, -1, kernel)

# Edge detection (Canny)

def canny_edge(img, t1, t2):
    gray = bgr_to_gray(img)
    edges = cv2.Canny(gray, t1, t2)
    return edges

# ----------------------- Streamlit UI -----------------------

st.title("📷 Image Processing Toolkit — Streamlit + OpenCV")

# Menu bar at top (simple emulation)
menu = st.sidebar.selectbox("Menu", ["File", "Operations Help"])
if menu == "File":
    st.sidebar.write("Use the Upload widget below to open images. Use Save/Export controls in the right panel.")

# Upload
uploaded = st.sidebar.file_uploader("Open — Upload an image", type=["png", "jpg", "jpeg", "bmp", "tiff"])
orig_img = load_image(uploaded)

# Placeholders for processed image
processed_img = None

# Left panel: operations
st.sidebar.header("Operations")
show_info = st.sidebar.checkbox("Show Image Info", value=True)
color_conv = st.sidebar.selectbox("Color Conversions", ["None", "RGB↔BGR", "BGR→HSV", "BGR→YCbCr", "BGR→Grayscale"]) 

st.sidebar.markdown("---")
transformation = st.sidebar.selectbox("Transformations", ["None", "Rotate", "Scale", "Translate", "Affine", "Perspective"]) 

st.sidebar.markdown("---")
filtering = st.sidebar.selectbox("Filtering & Morphology", ["None", "Gaussian", "Median", "Mean", "Sobel Edge", "Laplacian Edge", "Dilation", "Erosion", "Opening", "Closing"]) 

st.sidebar.markdown("---")
enhance = st.sidebar.selectbox("Enhancement & Edge Detection", ["None", "Histogram Equalization", "Contrast Stretching", "Sharpening", "Canny Edge"]) 

st.sidebar.markdown("---")
compression_fmt = st.sidebar.selectbox("Compression / Save Format", ["PNG", "JPG", "BMP"]) 

# Bonus controls (sliders)
st.sidebar.markdown("### Parameters")
angle = st.sidebar.slider("Rotation Angle", -180, 180, 0)
scale = st.sidebar.slider("Scaling Factor (fx=fy)", 10, 300, 100) / 100.0
tx = st.sidebar.slider("Translate X (px)", -200, 200, 0)
ty = st.sidebar.slider("Translate Y (px)", -200, 200, 0)
ksize = st.sidebar.slider("Kernel Size (odd)", 1, 31, 3)
if ksize % 2 == 0:
    ksize += 1
canny_t1 = st.sidebar.slider("Canny Threshold 1", 0, 500, 100)
canny_t2 = st.sidebar.slider("Canny Threshold 2", 0, 500, 200)

# Extra: upload second image for bitwise ops
st.sidebar.markdown("---")
second_img_file = st.sidebar.file_uploader("(Optional) Upload second image for bitwise ops", type=["png","jpg","jpeg","bmp"]) 
second_img = load_image(second_img_file)
bitwise_op = st.sidebar.selectbox("Bitwise Operation", ["None","AND","OR","XOR","NOT"]) 

# Columns for display
col1, col2 = st.columns([0.5, 0.5])

with col1:
    st.subheader("Original Image")
    if orig_img is None:
        st.info("Upload an image using the sidebar to get started.")
    else:
        st.image(to_pil(orig_img), use_column_width=True)

with col2:
    st.subheader("Processed Image")
    processed_placeholder = st.empty()

# Begin processing pipeline
if orig_img is not None:
    img = orig_img.copy()

    # Color conversions
    if color_conv != "None":
        if color_conv == "RGB↔BGR":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # convert back to BGR for further ops
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        elif color_conv == "BGR→HSV":
            hsv = bgr_to_hsv(img)
            # Show HSV visually by converting back to BGR for display
            img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        elif color_conv == "BGR→YCbCr":
            ycb = bgr_to_ycbcr(img)
            img = cv2.cvtColor(ycb, cv2.COLOR_YCrCb2BGR)
        elif color_conv == "BGR→Grayscale":
            img = bgr_to_gray(img)

    # Transformations
    if transformation != "None":
        if transformation == "Rotate":
            img = rotate_image(img, angle)
        elif transformation == "Scale":
            img = scale_image(img, scale, scale)
        elif transformation == "Translate":
            img = translate_image(img, tx, ty)
        elif transformation == "Affine":
            h, w = img.shape[:2]
            src = [[0,0],[w-1,0],[0,h-1]]
            dst = [[0+tx,0+ty],[int(w*0.8),10],[10,int(h*0.8)]]
            img = affine_transform(img, src, dst)
        elif transformation == "Perspective":
            h, w = img.shape[:2]
            src = [[0,0],[w-1,0],[w-1,h-1],[0,h-1]]
            offset = min(w,h)//6
            dst = [[0+offset,0+offset],[w-1-offset,0+offset],[w-1-offset,h-1-offset],[0+offset,h-1-offset]]
            img = perspective_transform(img, src, dst)

    # Bitwise operations
    if bitwise_op != "None":
        if second_img is not None:
            img = bitwise_ops(img, second_img, bitwise_op)
        else:
            if bitwise_op == "NOT":
                img = bitwise_ops(img, img, "NOT")

    # Filtering & Morphology
    if filtering != "None":
        if filtering in ["Gaussian","Median","Mean"]:
            img = apply_filter(img, filtering, ksize)
        elif filtering == "Sobel Edge":
            edges = edge_sobel(img)
            img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        elif filtering == "Laplacian Edge":
            lap = edge_laplacian(img)
            img = cv2.cvtColor(lap, cv2.COLOR_GRAY2BGR)
        elif filtering in ["Dilation","Erosion","Opening","Closing"]:
            # morphology expects single channel for demonstration
            base = bgr_to_gray(img) if img.ndim == 3 else img
            morph = morphological(base, filtering, ksize)
            img = cv2.cvtColor(morph, cv2.COLOR_GRAY2BGR)

    # Enhancement & Edge Detection
    if enhance != "None":
        if enhance == "Histogram Equalization":
            img = histogram_equalization(img)
        elif enhance == "Contrast Stretching":
            img = contrast_stretch(img)
        elif enhance == "Sharpening":
            img = sharpen(img)
        elif enhance == "Canny Edge":
            edges = canny_edge(img, canny_t1, canny_t2)
            img = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    processed_img = img
    processed_placeholder.image(to_pil(processed_img), use_column_width=True)

    # Status bar / image info
    info = get_image_info(processed_img, uploaded)
    st.sidebar.markdown("---")
    st.sidebar.subheader("Image Info (Processed)")
    if info:
        st.sidebar.write(f"Dimensions: {info['width']} x {info['height']} (W x H)")
        st.sidebar.write(f"Channels: {info['channels']}")
        if info['size_bytes'] is not None:
            st.sidebar.write(f"Original file size: {info['size_bytes']/1024:.2f} KB")
        st.sidebar.write(f"Format (orig): {info.get('format', 'unknown')}")

    # Save / Download
    st.sidebar.markdown("---")
    st.sidebar.subheader("Save / Export")
    out_fmt = st.sidebar.selectbox("Export Format", ["PNG","JPG","BMP"], index=["PNG","JPG","BMP"].index(compression_fmt))
    quality = st.sidebar.slider("JPEG Quality", 10, 100, 95)

    if st.sidebar.button("Save Processed Image to disk"):
        if processed_img is not None:
            b = bytes_from_img(processed_img, fmt=out_fmt, quality=quality)
            # save to temp file
            suffix = out_fmt.lower() if out_fmt != "JPG" else "jpg"
            tmp = tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}")
            tmp.write(b)
            tmp.flush()
            tmp.close()
            st.sidebar.success(f"Image saved to {tmp.name}")

    if processed_img is not None:
        b = bytes_from_img(processed_img, fmt=out_fmt, quality=quality)
        st.sidebar.download_button("Download Processed Image", data=b, file_name=f"processed.{out_fmt.lower()}")

else:
    # nothing uploaded
    processed_placeholder.image([])

# Footer / status bar
st.markdown("---")
st.caption("Status: Use the sidebar to upload images and apply operations. This toolkit is meant for learning — modify and extend as needed for your assignment.")

# End of file
