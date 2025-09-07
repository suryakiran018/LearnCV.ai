

import io
import os
import time
import base64
import numpy as np
import cv2
from PIL import Image, ImageOps, ImageStat
import streamlit as st

# -------------------------------
# Helpers
# -------------------------------

def pil_open_bytes(file_bytes):
    return Image.open(io.BytesIO(file_bytes))

def cv2_from_pil(pil_img):
    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

def pil_from_cv2(bgr):
    return Image.fromarray(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))

def ensure_uint8(img):
    # Clamp/convert to 0..255 uint8 for display/saving
    if img.dtype == np.float32 or img.dtype == np.float64:
        img = np.clip(img, 0, 255).astype(np.uint8)
    elif img.dtype != np.uint8:
        img = img.astype(np.uint8)
    return img

def to_gray_if_needed(bgr):
    if len(bgr.shape) == 3 and bgr.shape[2] == 3:
        return cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)
    return bgr

def get_image_info(pil_img, file_bytes=None, file_name=None):
    info = {}
    info["mode"] = pil_img.mode
    info["size_wh"] = pil_img.size  # (W, H)
    info["format"] = getattr(pil_img, "format", None) or (file_name.split(".")[-1].upper() if file_name else "N/A")
    info["dpi"] = pil_img.info.get("dpi", "N/A")
    if file_bytes is not None:
        info["file_size_bytes"] = len(file_bytes)
    else:
        info["file_size_bytes"] = "N/A"
    return info

def bytes_from_image(img: Image.Image, fmt="PNG", quality=95):
    buf = io.BytesIO()
    save_kwargs = {}
    if fmt.upper() in ["JPG", "JPEG"]:
        save_kwargs["quality"] = int(quality)
        save_kwargs["optimize"] = True
    img.save(buf, format=fmt, **save_kwargs)
    return buf.getvalue()

def cv2_encode_bytes(bgr, ext=".png", quality=95):
    params = []
    if ext.lower() in [".jpg", ".jpeg"]:
        params = [cv2.IMWRITE_JPEG_QUALITY, int(quality)]
    success, buf = cv2.imencode(ext, ensure_uint8(bgr), params)
    if not success:
        raise RuntimeError("Encoding failed")
    return buf.tobytes()

def halfsplit_composite(orig_bgr, proc_bgr, vertical=True):
    h, w = orig_bgr.shape[:2]
    proc_bgr = cv2.resize(proc_bgr, (w, h), interpolation=cv2.INTER_LINEAR)
    if vertical:
        mid = w // 2
        left = orig_bgr[:, :mid]
        right = proc_bgr[:, mid:]
        return np.hstack([left, right])
    else:
        mid = h // 2
        top = orig_bgr[:mid, :]
        bottom = proc_bgr[mid:, :]
        return np.vstack([top, bottom])

def contrast_stretch(bgr, low_perc=2.0, high_perc=98.0):
    # Per-channel percentile stretch
    out = np.zeros_like(bgr)
    if len(bgr.shape) == 2:
        low = np.percentile(bgr, low_perc)
        high = np.percentile(bgr, high_perc)
        if high - low < 1e-5:
            return bgr.copy()
        out = np.clip((bgr - low) * 255.0 / (high - low), 0, 255).astype(np.uint8)
        return out
    for c in range(3):
        ch = bgr[:, :, c]
        low = np.percentile(ch, low_perc)
        high = np.percentile(ch, high_perc)
        if high - low < 1e-5:
            out[:, :, c] = ch
        else:
            out[:, :, c] = np.clip((ch - low) * 255.0 / (high - low), 0, 255).astype(np.uint8)
    return out

def unsharp_mask(bgr, ksize=5, amount=1.0):
    blur = cv2.GaussianBlur(bgr, (ksize, ksize), 0)
    sharp = cv2.addWeighted(bgr, 1 + amount, blur, -amount, 0)
    return ensure_uint8(sharp)

def sobel_edges(gray, ksize=3):
    gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=ksize)
    gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=ksize)
    mag = cv2.magnitude(gx, gy)
    mag = np.uint8(np.clip(mag / (mag.max() + 1e-9) * 255, 0, 255))
    return mag

def laplacian_edges(gray, ksize=3):
    lap = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
    lap = np.uint8(np.clip(np.absolute(lap) / (np.max(np.absolute(lap)) + 1e-9) * 255, 0, 255))
    return lap

# -------------------------------
# Streamlit App
# -------------------------------

st.set_page_config(page_title="Image Processing Toolkit (OpenCV + Streamlit)", layout="wide")

st.markdown(
    "<h1 style='margin-bottom:0'>📷 Image Processing Toolkit</h1>"
    "<div style='opacity:0.7;margin-bottom:1rem'>Module 1 – Image Processing Fundamentals & Computer Vision</div>",
    unsafe_allow_html=True
)

# Menu-like actions (simulated)
colA, colB, colC, colD = st.columns([1,1,1,6])
with colA:
    st.caption("File")
with colB:
    st.caption("Open  •  Save  •  Exit")
with colC:
    pass

# File open
uploaded = st.file_uploader("Open → Upload an image", type=["png","jpg","jpeg","bmp","tiff"], accept_multiple_files=False)

# Keep app state
if "orig_bytes" not in st.session_state:
    st.session_state.orig_bytes = None
if "orig_name" not in st.session_state:
    st.session_state.orig_name = None
if "proc_bgr" not in st.session_state:
    st.session_state.proc_bgr = None

if uploaded is not None:
    st.session_state.orig_bytes = uploaded.getvalue()
    st.session_state.orig_name = uploaded.name
    pil_img = pil_open_bytes(st.session_state.orig_bytes).convert("RGB")
    st.session_state.proc_bgr = cv2_from_pil(pil_img)

# Sidebar
st.sidebar.title("🎛️ Operations")

if st.session_state.orig_bytes is None:
    st.info("Upload an image to get started.")
    st.stop()

pil_orig = pil_open_bytes(st.session_state.orig_bytes).convert("RGB")
bgr_orig = cv2_from_pil(pil_orig)
proc = bgr_orig.copy()

# Operation categories
cat = st.sidebar.selectbox(
    "Choose category",
    [
        "Image Info",
        "Color Conversions",
        "Transformations",
        "Bitwise Ops",
        "Filtering & Morphology",
        "Enhancement",
        "Edge Detection",
        "Compression & File Handling",
        "Video Mode (Optional Demo)"
    ]
)

# ---- Image Info ----
if cat == "Image Info":
    st.sidebar.subheader("Image Properties")
    info = get_image_info(pil_orig, st.session_state.orig_bytes, st.session_state.orig_name)

    c1, c2 = st.columns(2)
    with c1:
        st.image(pil_orig, caption="Original", use_container_width=True)
    with c2:
        st.image(pil_orig, caption="Processed (none)", use_container_width=True)

    st.markdown("### Status")
    st.json({
        "Dimensions (H, W, C)": (pil_orig.size[1], pil_orig.size[0], 3),
        "DPI/PPI": info["dpi"],
        "File format": info["format"],
        "Approx. file size (bytes)": info["file_size_bytes"],
    })

# ---- Color Conversions ----
elif cat == "Color Conversions":
    op = st.sidebar.radio(
        "Select conversion",
        [
            "RGB → BGR",
            "RGB ↔ HSV",
            "RGB ↔ YCbCr",
            "RGB ↔ Grayscale"
        ]
    )
    if op == "RGB → BGR":
        proc = cv2.cvtColor(bgr_orig, cv2.COLOR_BGR2RGB)  # show swap effect
    elif op == "RGB ↔ HSV":
        hsv = cv2.cvtColor(bgr_orig, cv2.COLOR_BGR2HSV)
        show = st.sidebar.selectbox("Show space", ["HSV", "Back to RGB"])
        proc = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) if show == "Back to RGB" else cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        if show == "HSV":
            # visualize HSV by converting each channel to pseudo-RGB stack
            h,s,v = cv2.split(hsv)
            hsv_vis = cv2.merge([h,s,v])
            proc = cv2.cvtColor(hsv_vis, cv2.COLOR_HSV2BGR)
    elif op == "RGB ↔ YCbCr":
        ycrcb = cv2.cvtColor(bgr_orig, cv2.COLOR_BGR2YCrCb)
        show = st.sidebar.selectbox("Show space", ["YCbCr", "Back to RGB"])
        proc = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2BGR) if show == "Back to RGB" else ycrcb
        if show == "YCbCr":
            # Convert for safe display
            proc = cv2.cvtColor(proc, cv2.COLOR_YCrCb2BGR)
    elif op == "RGB ↔ Grayscale":
        gray = cv2.cvtColor(bgr_orig, cv2.COLOR_BGR2GRAY)
        mode = st.sidebar.selectbox("Mode", ["Gray", "Back to RGB"])
        proc = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) if mode == "Gray" else bgr_orig

    # Split screen option
    split = st.sidebar.checkbox("Split-screen compare (½ original | ½ processed)", value=True)
    if split:
        show_bgr = halfsplit_composite(bgr_orig, proc, vertical=True)
    else:
        show_bgr = proc

    c1, c2 = st.columns(2)
    with c1:
        st.image(pil_from_cv2(bgr_orig), caption="Original", use_container_width=True)
    with c2:
        st.image(pil_from_cv2(show_bgr), caption="Processed", use_container_width=True)

# ---- Transformations ----
elif cat == "Transformations":
    op = st.sidebar.selectbox(
        "Select transform",
        ["Rotation", "Scaling", "Translation", "Affine Transform", "Perspective Transform"]
    )

    if op == "Rotation":
        angle = st.sidebar.slider("Angle (°)", -180, 180, 30, 1)
        scale = st.sidebar.slider("Scale", 10, 300, 100) / 100.0
        h, w = bgr_orig.shape[:2]
        M = cv2.getRotationMatrix2D((w/2, h/2), angle, scale)
        proc = cv2.warpAffine(bgr_orig, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT101)

    elif op == "Scaling":
        fx = st.sidebar.slider("Scale X", 10, 300, 150) / 100.0
        fy = st.sidebar.slider("Scale Y", 10, 300, 150) / 100.0
        proc = cv2.resize(bgr_orig, None, fx=fx, fy=fy, interpolation=cv2.INTER_AREA if (fx<1 or fy<1) else cv2.INTER_LINEAR)

    elif op == "Translation":
        tx = st.sidebar.slider("Shift X (px)", -500, 500, 50)
        ty = st.sidebar.slider("Shift Y (px)", -500, 500, 50)
        h, w = bgr_orig.shape[:2]
        M = np.float32([[1, 0, tx], [0, 1, ty]])
        proc = cv2.warpAffine(bgr_orig, M, (w, h), borderMode=cv2.BORDER_REFLECT101)

    elif op == "Affine Transform":
        h, w = bgr_orig.shape[:2]
        st.sidebar.caption("Select 3 source and destination points")
        x1 = st.sidebar.slider("src1.x", 0, w, int(0.2*w))
        y1 = st.sidebar.slider("src1.y", 0, h, int(0.2*h))
        x2 = st.sidebar.slider("src2.x", 0, w, int(0.8*w))
        y2 = st.sidebar.slider("src2.y", 0, h, int(0.2*h))
        x3 = st.sidebar.slider("src3.x", 0, w, int(0.2*w))
        y3 = st.sidebar.slider("src3.y", 0, h, int(0.8*h))

        dx1 = st.sidebar.slider("dst1.x", 0, w, int(0.3*w))
        dy1 = st.sidebar.slider("dst1.y", 0, h, int(0.3*h))
        dx2 = st.sidebar.slider("dst2.x", 0, w, int(0.7*w))
        dy2 = st.sidebar.slider("dst2.y", 0, h, int(0.3*h))
        dx3 = st.sidebar.slider("dst3.x", 0, w, int(0.2*w))
        dy3 = st.sidebar.slider("dst3.y", 0, h, int(0.7*h))

        src = np.float32([[x1,y1],[x2,y2],[x3,y3]])
        dst = np.float32([[dx1,dy1],[dx2,dy2],[dx3,dy3]])
        M = cv2.getAffineTransform(src, dst)
        proc = cv2.warpAffine(bgr_orig, M, (w, h), borderMode=cv2.BORDER_REFLECT101)

    elif op == "Perspective Transform":
        h, w = bgr_orig.shape[:2]
        st.sidebar.caption("Select 4 source and destination points")
        def tri(name, default):
            return st.sidebar.slider(name, 0, 100, default)
        # Source corners (normalized)
        sx1 = st.sidebar.slider("src1.x (%)", 0, 100, 10)
        sy1 = st.sidebar.slider("src1.y (%)", 0, 100, 10)
        sx2 = st.sidebar.slider("src2.x (%)", 0, 100, 90)
        sy2 = st.sidebar.slider("src2.y (%)", 0, 100, 10)
        sx3 = st.sidebar.slider("src3.x (%)", 0, 100, 90)
        sy3 = st.sidebar.slider("src3.y (%)", 0, 100, 90)
        sx4 = st.sidebar.slider("src4.x (%)", 0, 100, 10)
        sy4 = st.sidebar.slider("src4.y (%)", 0, 100, 90)

        dx1 = st.sidebar.slider("dst1.x (%)", 0, 100, 5)
        dy1 = st.sidebar.slider("dst1.y (%)", 0, 100, 5)
        dx2 = st.sidebar.slider("dst2.x (%)", 0, 100, 95)
        dy2 = st.sidebar.slider("dst2.y (%)", 0, 100, 10)
        dx3 = st.sidebar.slider("dst3.x (%)", 0, 100, 95)
        dy3 = st.sidebar.slider("dst3.y (%)", 0, 100, 95)
        dx4 = st.sidebar.slider("dst4.x (%)", 0, 100, 5)
        dy4 = st.sidebar.slider("dst4.y (%)", 0, 100, 90)

        src = np.float32([[sx1*w/100,sy1*h/100],[sx2*w/100,sy2*h/100],[sx3*w/100,sy3*h/100],[sx4*w/100,sy4*h/100]])
        dst = np.float32([[dx1*w/100,dy1*h/100],[dx2*w/100,dy2*h/100],[dx3*w/100,dy3*h/100],[dx4*w/100,dy4*h/100]])
        M = cv2.getPerspectiveTransform(src, dst)
        proc = cv2.warpPerspective(bgr_orig, M, (w, h), borderMode=cv2.BORDER_REFLECT101)

    # Bitwise ops note
    st.sidebar.markdown("---")
    st.sidebar.subheader("Bitwise Ops")
    bit = st.sidebar.selectbox("Operation", ["None","AND","OR","XOR","NOT"])
    if bit != "None":
        # Create a simple mask (circle) to demonstrate
        h, w = proc.shape[:2]
        mask = np.zeros((h,w), dtype=np.uint8)
        cv2.circle(mask, (w//2, h//2), min(h,w)//4, 255, -1)
        if bit == "AND":
            proc = cv2.bitwise_and(proc, proc, mask=mask)
        elif bit == "OR":
            proc = cv2.bitwise_or(proc, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR))
        elif bit == "XOR":
            proc = cv2.bitwise_xor(proc, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR))
        elif bit == "NOT":
            proc = cv2.bitwise_not(proc)

    split = st.sidebar.checkbox("Split-screen compare", value=False)
    show_bgr = halfsplit_composite(bgr_orig, proc) if split else proc

    c1, c2 = st.columns(2)
    with c1:
        st.image(pil_from_cv2(bgr_orig), caption="Original", use_container_width=True)
    with c2:
        st.image(pil_from_cv2(show_bgr), caption="Processed", use_container_width=True)

# ---- Filtering & Morphology ----
elif cat == "Filtering & Morphology":
    mode = st.sidebar.selectbox(
        "Select filter/morph operation",
        ["Gaussian", "Median", "Mean (Box)", "Sobel", "Laplacian", "Dilation", "Erosion", "Opening", "Closing"]
    )
    gray = cv2.cvtColor(bgr_orig, cv2.COLOR_BGR2GRAY)

    if mode in ["Gaussian", "Median", "Mean (Box)"]:
        k = st.sidebar.slider("Kernel size (odd)", 3, 31, 7, step=2)
        if mode == "Gaussian":
            sigma = st.sidebar.slider("Sigma", 0, 20, 2)
            proc = cv2.GaussianBlur(bgr_orig, (k, k), sigma)
        elif mode == "Median":
            proc = cv2.medianBlur(bgr_orig, k)
        else:
            proc = cv2.blur(bgr_orig, (k, k))

    elif mode == "Sobel":
        k = st.sidebar.slider("Kernel size (1,3,5,7)", 1, 7, 3, step=2)
        mag = sobel_edges(gray, ksize=k)
        proc = cv2.cvtColor(mag, cv2.COLOR_GRAY2BGR)

    elif mode == "Laplacian":
        k = st.sidebar.slider("Kernel size (1,3,5,7)", 1, 7, 3, step=2)
        lap = laplacian_edges(gray, ksize=k)
        proc = cv2.cvtColor(lap, cv2.COLOR_GRAY2BGR)

    else:
        k = st.sidebar.slider("Kernel size", 3, 31, 7, step=2)
        iters = st.sidebar.slider("Iterations", 1, 10, 1)
        kernel = np.ones((k,k), np.uint8)
        if mode == "Dilation":
            proc = cv2.dilate(bgr_orig, kernel, iterations=iters)
        elif mode == "Erosion":
            proc = cv2.erode(bgr_orig, kernel, iterations=iters)
        elif mode == "Opening":
            proc = cv2.morphologyEx(bgr_orig, cv2.MORPH_OPEN, kernel, iterations=iters)
        elif mode == "Closing":
            proc = cv2.morphologyEx(bgr_orig, cv2.MORPH_CLOSE, kernel, iterations=iters)

    split = st.sidebar.checkbox("Split-screen compare", value=False)
    show_bgr = halfsplit_composite(bgr_orig, proc) if split else proc

    c1, c2 = st.columns(2)
    with c1:
        st.image(pil_from_cv2(bgr_orig), caption="Original", use_container_width=True)
    with c2:
        st.image(pil_from_cv2(show_bgr), caption="Processed", use_container_width=True)

# ---- Enhancement ----
elif cat == "Enhancement":
    op = st.sidebar.selectbox("Select enhancement", ["Histogram Equalization", "Contrast Stretching", "Sharpening"])
    if op == "Histogram Equalization":
        method = st.sidebar.selectbox("Method", ["Grayscale (HE)", "Color (CLAHE on Y)"])
        if method == "Grayscale (HE)":
            gray = cv2.cvtColor(bgr_orig, cv2.COLOR_BGR2GRAY)
            proc = cv2.equalizeHist(gray)
            proc = cv2.cvtColor(proc, cv2.COLOR_GRAY2BGR)
        else:
            ycrcb = cv2.cvtColor(bgr_orig, cv2.COLOR_BGR2YCrCb)
            y, cr, cb = cv2.split(ycrcb)
            clip = st.sidebar.slider("CLAHE clipLimit", 1, 10, 2)
            tile = st.sidebar.slider("TileGridSize", 2, 16, 8)
            clahe = cv2.createCLAHE(clipLimit=clip, tileGridSize=(tile, tile))
            y = clahe.apply(y)
            proc = cv2.cvtColor(cv2.merge([y, cr, cb]), cv2.COLOR_YCrCb2BGR)
    elif op == "Contrast Stretching":
        low = st.sidebar.slider("Low percentile", 0, 20, 2)
        high = st.sidebar.slider("High percentile", 80, 100, 98)
        if high <= low: high = min(100, low + 1)
        proc = contrast_stretch(bgr_orig, low_perc=float(low), high_perc=float(high))
    else:
        k = st.sidebar.slider("Kernel (odd)", 3, 31, 5, step=2)
        amount = st.sidebar.slider("Amount", 0, 300, 120) / 100.0
        proc = unsharp_mask(bgr_orig, ksize=k, amount=amount)

    split = st.sidebar.checkbox("Split-screen compare", value=True)
    show_bgr = halfsplit_composite(bgr_orig, proc) if split else proc

    c1, c2 = st.columns(2)
    with c1:
        st.image(pil_from_cv2(bgr_orig), caption="Original", use_container_width=True)
    with c2:
        st.image(pil_from_cv2(show_bgr), caption="Processed", use_container_width=True)

# ---- Edge Detection ----
elif cat == "Edge Detection":
    mode = st.sidebar.radio("Select operator", ["Sobel", "Canny", "Laplacian"])
    gray = cv2.cvtColor(bgr_orig, cv2.COLOR_BGR2GRAY)

    if mode == "Sobel":
        k = st.sidebar.slider("Kernel size (1,3,5,7)", 1, 7, 3, step=2)
        proc_gray = sobel_edges(gray, ksize=k)
    elif mode == "Canny":
        th1 = st.sidebar.slider("Threshold 1", 0, 255, 50)
        th2 = st.sidebar.slider("Threshold 2", 0, 255, 150)
        proc_gray = cv2.Canny(gray, th1, th2)
    else:
        k = st.sidebar.slider("Kernel size (1,3,5,7)", 1, 7, 3, step=2)
        proc_gray = laplacian_edges(gray, ksize=k)

    proc = cv2.cvtColor(proc_gray, cv2.COLOR_GRAY2BGR)

    split = st.sidebar.checkbox("Split-screen compare", value=True)
    show_bgr = halfsplit_composite(bgr_orig, proc) if split else proc

    c1, c2 = st.columns(2)
    with c1:
        st.image(pil_from_cv2(bgr_orig), caption="Original", use_container_width=True)
    with c2:
        st.image(pil_from_cv2(show_bgr), caption="Processed", use_container_width=True)

# ---- Compression & File Handling ----
elif cat == "Compression & File Handling":
    fmt = st.sidebar.selectbox("Save format", ["PNG", "JPG", "BMP"])
    quality = 95
    if fmt == "JPG":
        quality = st.sidebar.slider("JPEG quality", 1, 100, 90)

    st.sidebar.caption("Click button below to encode and compare size.")
    if st.sidebar.button("Encode & Compare"):
        png_bytes = cv2_encode_bytes(bgr_orig, ext=".png")
        jpg_bytes = cv2_encode_bytes(bgr_orig, ext=".jpg", quality=quality)
        bmp_bytes = cv2_encode_bytes(bgr_orig, ext=".bmp")
        st.session_state.comp_sizes = {
            "PNG (default params)": len(png_bytes),
            f"JPG (q={quality})": len(jpg_bytes),
            "BMP": len(bmp_bytes)
        }
        st.session_state.last_comp_img = bgr_orig.copy()

    if "comp_sizes" in st.session_state:
        st.markdown("### File Size Comparison (bytes)")
        st.json(st.session_state.comp_sizes)
        st.image(pil_from_cv2(st.session_state.last_comp_img), caption="Image used for comparison", use_container_width=True)
    else:
        st.info("Choose format/quality and click 'Encode & Compare'")

    c1, c2 = st.columns(2)
    with c1:
        st.image(pil_from_cv2(bgr_orig), caption="Original", use_container_width=True)
    with c2:
        st.image(pil_from_cv2(bgr_orig), caption="Processed (none)", use_container_width=True)

# ---- Video Mode ----
elif cat == "Video Mode (Optional Demo)":
    st.sidebar.warning("Experimental: Webcam access may not work on all platforms.")
    run = st.sidebar.checkbox("Start webcam")
    op = st.sidebar.selectbox("Operation", ["None","Grayscale","Canny"])
    display = st.empty()

    if run:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            st.error("Cannot open webcam.")
        else:
            st.info("Press 'Stop' checkbox in the sidebar to end the stream.")
            while run:
                ok, frame = cap.read()
                if not ok:
                    st.error("Frame grab failed.")
                    break
                # Apply operation
                if op == "Grayscale":
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
                elif op == "Canny":
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    edges = cv2.Canny(gray, 80, 160)
                    frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

                display.image(pil_from_cv2(frame), use_container_width=True)
                run = st.sidebar.checkbox("Start webcam", value=True)
            cap.release()
    else:
        st.info("Enable 'Start webcam' in the sidebar to begin.")

# ---- Save Processed Image (applies to last shown 'proc' when available) ----
st.markdown("---")
st.subheader("💾 Save Processed Image")
fmt2 = st.selectbox("Format", ["PNG","JPG","BMP"], key="savefmt")
q2 = 95
if fmt2 == "JPG":
    q2 = st.slider("JPEG quality", 1, 100, 92, key="savequal")

# If we are in a branch that didn't define `proc`, default to original
if 'proc' not in locals() or proc is None:
    proc = bgr_orig.copy()

save_bytes = cv2_encode_bytes(proc, ext=f".{fmt2.lower()}", quality=q2)
st.download_button(
    "Download processed image",
    data=save_bytes,
    file_name=f"processed.{fmt2.lower()}",
    mime=f"image/{'jpeg' if fmt2=='JPG' else fmt2.lower()}"
)

# ---- Status Bar ----
st.markdown("---")
st.caption("Status")
info = get_image_info(pil_orig, st.session_state.orig_bytes, st.session_state.orig_name)
h, w = bgr_orig.shape[:2]
channels = 1 if len(bgr_orig.shape)==2 else bgr_orig.shape[2]
st.json({
    "Dimensions (H, W, C)": (h, w, channels),
    "DPI/PPI": info["dpi"],
    "File format": info["format"],
    "Approx. file size (bytes)": info["file_size_bytes"],
})

