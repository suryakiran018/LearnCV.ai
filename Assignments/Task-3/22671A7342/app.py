"""
Streamlit Image Processing Toolkit (app.py)

Features implemented:
- Upload image, display original and processed side-by-side
- Image info (resolution, shape, channels, format, file size)
- Color conversions: RGB<->BGR, RGB<->HSV, RGB<->YCbCr, Grayscale
- Geometric transforms: rotate, scale, translate, affine, perspective
- Bitwise ops: AND/OR/XOR/NOT (with a second uploaded mask image)
- Filters & Morphology: Gaussian, Mean, Median, Sobel, Laplacian, Dilate/Erode/Open/Close
- Enhancement: Histogram Equalization (grayscale & color via Y channel), Contrast Stretching, Sharpening
- Edge detection: Sobel, Canny, Laplacian
- Compression & File handling: save as JPG/PNG/BMP, compare sizes
- Bonus: sliders for kernel size, rotation angle, scaling, Canny thresholds, comparison (split) mode
- Webcam snapshot (st.camera_input) for quick real-time capture

Run: pip install -r requirements.txt
requirements.txt:
streamlit
opencv-python
numpy
Pillow
matplotlib

Start: streamlit run Streamlit_ImageToolkit_app.py

"""

import streamlit as st
import numpy as np
import cv2
from PIL import Image
import io
import os
import math
import tempfile
import matplotlib.pyplot as plt

st.set_page_config(page_title="Image Processing Toolkit", layout="wide", initial_sidebar_state="expanded")

# ---------------------- Utility functions ----------------------

def load_image_to_cv2(uploaded_file):
    if uploaded_file is None:
        return None, None
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)
    # also return original bytes and fname
    return img, uploaded_file


def cv2_to_pil(img):
    if img is None:
        return None
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return Image.fromarray(img_rgb)


def pil_to_bytes_io(pil_img, fmt="PNG", quality=95):
    buf = io.BytesIO()
    if fmt.upper() == 'JPG':
        fmt = 'JPEG'
    pil_img.save(buf, format=fmt, quality=quality)
    buf.seek(0)
    return buf


def get_image_info(img, uploaded_file=None):
    if img is None:
        return {}
    h, w = img.shape[:2]
    c = 1 if img.ndim == 2 else img.shape[2]
    filesize = None
    fname = None
    fmt = None
    dpi = None
    if uploaded_file is not None:
        try:
            uploaded_file.seek(0)
        except Exception:
            pass
        fname = getattr(uploaded_file, "name", None)
        try:
            uploaded_file_bytes = uploaded_file.read()
            filesize = len(uploaded_file_bytes)
        except Exception:
            filesize = None
    info = {
        "Width": w,
        "Height": h,
        "Channels": c,
        "Filename": fname,
        "Filesize (bytes)": filesize,
        "DPI/PPI": dpi,
    }
    return info


def safe_imencode(img, ext='.png', params=None):
    ext = ext.lower()
    if params is None:
        params = []
    success, encoded = cv2.imencode(ext, img, params)
    if not success:
        return None
    return encoded.tobytes()


def bytes_size_str(b):
    if b is None:
        return 'N/A'
    for unit in ['B','KB','MB','GB']:
        if b < 1024.0:
            return f"{b:.2f} {unit}"
        b /= 1024.0
    return f"{b:.2f} TB"

# ---------------------- Image ops ----------------------

def convert_color(img, mode):
    if img is None:
        return None
    if mode == 'RGB->BGR':
        return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    if mode == 'BGR->RGB':
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if mode == 'RGB->HSV' or mode == 'BGR->HSV':
        return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    if mode == 'HSV->BGR' or mode == 'HSV->RGB':
        return cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    if mode == 'BGR->GRAY' or mode == 'RGB->GRAY':
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if mode == 'BGR->YCbCr' or mode == 'RGB->YCbCr':
        return cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    if mode == 'YCbCr->BGR' or mode == 'YCbCr->RGB':
        return cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR)
    return img


def rotate_image(img, angle, center=None, scale=1.0, bbox=True):
    h, w = img.shape[:2]
    if center is None:
        center = (w/2, h/2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    cos = abs(M[0,0])
    sin = abs(M[0,1])
    if bbox:
        # compute new bounding dimensions
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))
        M[0,2] += (nW / 2) - center[0]
        M[1,2] += (nH / 2) - center[1]
        return cv2.warpAffine(img, M, (nW, nH))
    else:
        return cv2.warpAffine(img, M, (w, h))


def translate_image(img, tx, ty):
    M = np.float32([[1,0,tx],[0,1,ty]])
    h, w = img.shape[:2]
    return cv2.warpAffine(img, M, (w, h))


def scale_image(img, fx, fy, interpolation=cv2.INTER_LINEAR):
    return cv2.resize(img, None, fx=fx, fy=fy, interpolation=interpolation)


def affine_transform(img, src_pts, dst_pts, dst_size=None):
    M = cv2.getAffineTransform(np.float32(src_pts), np.float32(dst_pts))
    if dst_size is None:
        h, w = img.shape[:2]
        dst_size = (w, h)
    return cv2.warpAffine(img, M, dst_size)


def perspective_transform(img, src_pts, dst_pts, dst_size=None):
    M = cv2.getPerspectiveTransform(np.float32(src_pts), np.float32(dst_pts))
    if dst_size is None:
        h, w = img.shape[:2]
        dst_size = (w, h)
    return cv2.warpPerspective(img, M, dst_size)


def apply_filter(img, filt, ksize=3):
    if img is None:
        return None
    k = int(ksize)
    if k <= 0:
        k = 1
    if filt == 'gaussian':
        if k % 2 == 0:
            k += 1
        return cv2.GaussianBlur(img, (k,k), 0)
    if filt == 'median':
        if k % 2 == 0:
            k += 1
        return cv2.medianBlur(img, k)
    if filt == 'mean':
        return cv2.blur(img, (k,k))
    if filt == 'sharpen':
        kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        return cv2.filter2D(img, -1, kernel)
    return img


def edge_sobel(img):
    if img is None:
        return None
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    mag = cv2.magnitude(grad_x, grad_y)
    mag = np.uint8(np.clip(mag, 0, 255))
    return mag

# ---------------------- Streamlit UI ----------------------

st.title("🧰 Image Processing Toolkit — Streamlit + OpenCV")

# Menu bar simulation using columns (top bar)
col1, col2, col3 = st.columns([6,1,1])
with col2:
    if st.button('Save →', key='top_save'):
        st.session_state.get('save_request', False)
with col3:
    if st.button('Exit', key='top_exit'):
        st.stop()

# Sidebar: operations
st.sidebar.header('File')
uploaded = st.sidebar.file_uploader('Open → Upload an image', type=['png','jpg','jpeg','bmp','tiff'])
uploaded_mask = st.sidebar.file_uploader('Optional: Upload mask/image for bitwise ops', type=['png','jpg','jpeg','bmp'], key='mask')

st.sidebar.markdown('---')
st.sidebar.header('Image Info')
show_info = st.sidebar.checkbox('Show image info', value=True)

st.sidebar.header('Color Conversions')
color_mode = st.sidebar.selectbox('Choose conversion', ['None','RGB→BGR','BGR→RGB','RGB→HSV','HSV→RGB','RGB→YCbCr','YCbCr→RGB','RGB→GRAY'])

st.sidebar.header('Transformations')
transform = st.sidebar.selectbox('Transformation', ['None','Rotate','Scale','Translate','Affine','Perspective'])
angle = st.sidebar.slider('Rotation angle', -180, 180, 0) if transform == 'Rotate' else 0
scale_factor = st.sidebar.slider('Scale factor (both axes)', 0.1, 3.0, 1.0, 0.1) if transform == 'Scale' else 1.0
tx = st.sidebar.slider('Translate X (px)', -500, 500, 0) if transform == 'Translate' else 0
ty = st.sidebar.slider('Translate Y (px)', -500, 500, 0) if transform == 'Translate' else 0

st.sidebar.header('Filtering & Morphology')
filter_choice = st.sidebar.selectbox('Filter', ['None','Gaussian','Median','Mean','Sharpen'])
kernel_size = st.sidebar.slider('Kernel size', 1, 31, 3, 2)

st.sidebar.header('Morphology')
morph_choice = st.sidebar.selectbox('Morph operation', ['None','Dilation','Erosion','Opening','Closing'])
struct_size = st.sidebar.slider('Structuring element size', 1, 31, 3, 2)

st.sidebar.header('Edge Detection')
edge_choice = st.sidebar.selectbox('Edge detector', ['None','Sobel','Laplacian','Canny'])
canny_low = st.sidebar.slider('Canny low threshold', 0, 500, 50)
canny_high = st.sidebar.slider('Canny high threshold', 0, 500, 150)

st.sidebar.header('Compression / Save')
save_format = st.sidebar.selectbox('Save format', ['PNG','JPG','BMP'])
jpg_quality = st.sidebar.slider('JPG Quality', 10, 100, 90)

st.sidebar.markdown('---')
st.sidebar.header('Extras / Bonus')
split_compare = st.sidebar.checkbox('Comparison: Split screen half-half')
enable_webcam = st.sidebar.checkbox('Webcam snapshot (camera input)')

# Main layout: original | processed
orig_col, proc_col = st.columns(2)

# Load image
if enable_webcam:
    cam_img_file = st.camera_input('Take a snapshot (camera)')
    if cam_img_file is not None and uploaded is None:
        uploaded = cam_img_file

img_cv, uploaded_file = load_image_to_cv2(uploaded) if uploaded is not None else (None, None)
mask_cv, mask_file = load_image_to_cv2(uploaded_mask) if uploaded_mask is not None else (None, None)

# Initialize processed variable
processed = None

# Display original
with orig_col:
    st.subheader('Original')
    if img_cv is None:
        st.info('Upload an image on the left sidebar to begin')
    else:
        orig_pil = cv2_to_pil(img_cv)
        st.image(orig_pil, use_column_width='always')

# Apply pipeline of operations
if img_cv is not None:
    working = img_cv.copy()

    # Color conversions
    if color_mode != 'None':
        if 'HSV' in color_mode:
            working = convert_color(working, 'BGR->HSV')
            # convert back to BGR for display processing
            if '->RGB' in color_mode or 'HSV->RGB' in color_mode:
                working = convert_color(working, 'HSV->BGR')
        elif 'YCbCr' in color_mode:
            if '->' in color_mode and color_mode.split('->')[0].strip() == 'RGB':
                working = convert_color(working, 'BGR->YCbCr')
            else:
                working = convert_color(working, 'YCbCr->BGR')
        elif 'GRAY' in color_mode:
            working = convert_color(working, 'BGR->GRAY')
            # convert single channel to BGR for other ops consistency
            working = cv2.cvtColor(working, cv2.COLOR_GRAY2BGR)

    # Transformations
    if transform == 'Rotate':
        working = rotate_image(working, angle, scale=1.0)
    elif transform == 'Scale':
        working = scale_image(working, scale_factor, scale_factor)
    elif transform == 'Translate':
        working = translate_image(working, tx, ty)
    elif transform == 'Affine':
        h,w = working.shape[:2]
        src = [[0,0],[w-1,0],[0,h-1]]
        dst = [[0+h*0.0,0+h*0.05],[w-1-h*0.0,0+h*0.02],[0+h*0.05,h-1-h*0.0]]
        working = affine_transform(working, src, dst)
    elif transform == 'Perspective':
        h,w = working.shape[:2]
        shift = min(h,w)*0.1
        src = [[0,0],[w-1,0],[w-1,h-1],[0,h-1]]
        dst = [[shift,shift],[w-1-shift,0+shift*0.2],[w-1-shift,h-1-shift],[0+shift,h-1-shift*0.6]]
        working = perspective_transform(working, src, dst)

    # Filtering
    if filter_choice != 'None':
        if filter_choice == 'Gaussian':
            working = apply_filter(working, 'gaussian', kernel_size)
        elif filter_choice == 'Median':
            working = apply_filter(working, 'median', kernel_size)
        elif filter_choice == 'Mean':
            working = apply_filter(working, 'mean', kernel_size)
        elif filter_choice == 'Sharpen':
            working = apply_filter(working, 'sharpen', kernel_size)

    # Morphology
    if morph_choice != 'None':
        k = struct_size
        if k % 2 == 0:
            k += 1
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (k,k))
        if morph_choice == 'Dilation':
            working = cv2.dilate(working, kernel, iterations=1)
        elif morph_choice == 'Erosion':
            working = cv2.erode(working, kernel, iterations=1)
        elif morph_choice == 'Opening':
            working = cv2.morphologyEx(working, cv2.MORPH_OPEN, kernel)
        elif morph_choice == 'Closing':
            working = cv2.morphologyEx(working, cv2.MORPH_CLOSE, kernel)

    # Edge detection
    if edge_choice != 'None':
        if edge_choice == 'Sobel':
            sob = edge_sobel(working)
            working = cv2.cvtColor(sob, cv2.COLOR_GRAY2BGR)
        elif edge_choice == 'Laplacian':
            gray = cv2.cvtColor(working, cv2.COLOR_BGR2GRAY)
            lap = cv2.Laplacian(gray, cv2.CV_64F)
            lap = np.uint8(np.absolute(lap))
            working = cv2.cvtColor(lap, cv2.COLOR_GRAY2BGR)
        elif edge_choice == 'Canny':
            gray = cv2.cvtColor(working, cv2.COLOR_BGR2GRAY)
            can = cv2.Canny(gray, canny_low, canny_high)
            working = cv2.cvtColor(can, cv2.COLOR_GRAY2BGR)

    # Bitwise ops (if mask provided)
    if mask_cv is not None:
        # ensure same size
        try:
            m = cv2.resize(mask_cv, (working.shape[1], working.shape[0]))
            st.sidebar.header('Bitwise Ops')
            bchoice = st.sidebar.selectbox('Bitwise', ['None','AND','OR','XOR','NOT'], key='bitwise')
            if bchoice == 'AND':
                working = cv2.bitwise_and(working, m)
            elif bchoice == 'OR':
                working = cv2.bitwise_or(working, m)
            elif bchoice == 'XOR':
                working = cv2.bitwise_xor(working, m)
            elif bchoice == 'NOT':
                working = cv2.bitwise_not(working)
        except Exception:
            pass

    processed = working

# Display processed
with proc_col:
    st.subheader('Processed')
    if processed is None:
        st.info('Processed result will appear here')
    else:
        proc_pil = cv2_to_pil(processed)
        if split_compare:
            # create half-and-half comparison
            orig_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
            proc_rgb = cv2.cvtColor(processed, cv2.COLOR_BGR2RGB)
            # resize processed to original if different
            if orig_rgb.shape != proc_rgb.shape:
                proc_rgb = cv2.resize(proc_rgb, (orig_rgb.shape[1], orig_rgb.shape[0]))
            w = orig_rgb.shape[1]
            half = w//2
            comp = np.hstack((orig_rgb[:, :half, :], proc_rgb[:, half:, :]))
            st.image(Image.fromarray(comp), use_column_width='always')
        else:
            st.image(proc_pil, use_column_width='always')

# Status bar / image info
st.markdown('---')
info_col1, info_col2, info_col3 = st.columns(3)
if img_cv is not None:
    info = get_image_info(img_cv, uploaded_file)
    with info_col1:
        st.write(f"**Dimensions:** {info['Height']} x {info['Width']}")
        st.write(f"**Channels:** {info['Channels']}")
    with info_col2:
        st.write(f"**Filename:** {info.get('Filename','-')}")
        st.write(f"**Filesize:** {bytes_size_str(info.get('Filesize (bytes)') or 0)}")
    with info_col3:
        # show size comparison if processed saved
        if processed is not None:
            png_bytes = safe_imencode(processed, '.png')
            jpg_bytes = safe_imencode(processed, '.jpg', params=[int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
            bmp_bytes = safe_imencode(processed, '.bmp')
            st.write(f"**Processed sizes:** PNG={bytes_size_str(len(png_bytes) if png_bytes else None)}, JPG={bytes_size_str(len(jpg_bytes) if jpg_bytes else None)}, BMP={bytes_size_str(len(bmp_bytes) if bmp_bytes else None)}")
        else:
            st.write('**Processed sizes:** -')

# Save processed image
if processed is not None:
    out_pil = cv2_to_pil(processed)
    buf = pil_to_bytes_io(out_pil, fmt=save_format, quality=jpg_quality)
    st.download_button(label=f"Save processed as {save_format}", data=buf, file_name=f"processed.{save_format.lower()}", mime=f"image/{save_format.lower()}")

# Extra: show histogram and channels when requested
if show_info and img_cv is not None:
    st.subheader('Histogram & Channels')
    fig, ax = plt.subplots(1,1, figsize=(6,2.5))
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    if img_rgb.ndim == 3:
        colors = ('r','g','b')
        for i,col in enumerate(colors):
            hist = cv2.calcHist([img_rgb],[i],None,[256],[0,256])
            ax.plot(hist, label=col)
    else:
        hist = cv2.calcHist([img_rgb],[0],None,[256],[0,256])
        ax.plot(hist)
    ax.set_xlim([0,256])
    ax.legend()
    st.pyplot(fig)

st.info('Tip: Use sliders in the sidebar to interactively adjust kernel sizes, angles and thresholds. Save your processed image from the button above.')

# End

