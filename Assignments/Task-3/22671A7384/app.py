import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
import time

# Set page configuration
st.set_page_config(
    page_title="OpenCV Image Processor",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 600;
        color: #1f2937;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.2rem;
        font-weight: 600;
        color: #374151;
        margin-bottom: 1rem;
        border-bottom: 2px solid #10b981;
        padding-bottom: 0.5rem;
    }
    .image-container {
        border: 2px solid #e5e7eb;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .stButton > button {
        width: 100%;
        margin: 0.25rem 0;
    }
</style>
""", unsafe_allow_html=True)

class ImageProcessor:
    def __init__(self):
        self.original_image = None
        self.processed_image = None

    def load_image(self, uploaded_file):
        """Load and convert uploaded image to OpenCV format with error handling"""
        if uploaded_file is not None:
            try:
                pil_image = Image.open(uploaded_file)
                if pil_image.mode != 'RGB':
                    pil_image = pil_image.convert('RGB')
                opencv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
                self.original_image = opencv_image
                return opencv_image
            except Exception as e:
                st.error(f"❌ Failed to load image: {e}")
                return None
        return None

    def convert_for_display(self, image):
        """Convert OpenCV image (BGR) to format suitable for Streamlit display"""
        if len(image.shape) == 3:
            return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return image

    # Color Conversion Operations
    def rgb_to_grayscale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def rgb_to_hsv(self, image):
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        return hsv

    def rgb_to_sepia(self, image):
        sepia_filter = np.array([[0.272, 0.534, 0.131],
                                [0.349, 0.686, 0.168],
                                [0.393, 0.769, 0.189]])
        sepia_img = cv2.transform(image, sepia_filter)
        return np.clip(sepia_img, 0, 255).astype(np.uint8)

    def invert_colors(self, image):
        return cv2.bitwise_not(image)

    # Geometric Transformations
    def rotate_image(self, image, angle):
        height, width = image.shape[:2]
        center = (width // 2, height // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, rotation_matrix, (width, height), 
                                borderValue=(255, 255, 255))
        return rotated

    def scale_image(self, image, scale_factor):
        height, width = image.shape[:2]
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        scaled = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
        canvas = np.full_like(image, 255)
        y_offset = max(0, (height - new_height) // 2)
        x_offset = max(0, (width - new_width) // 2)
        if new_height <= height and new_width <= width:
            canvas[y_offset:y_offset+new_height, x_offset:x_offset+new_width] = scaled
        else:
            crop_y = max(0, (new_height - height) // 2)
            crop_x = max(0, (new_width - width) // 2)
            canvas = scaled[crop_y:crop_y+height, crop_x:crop_x+width]
        return canvas

    def translate_image(self, image, tx, ty):
        height, width = image.shape[:2]
        translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
        translated = cv2.warpAffine(image, translation_matrix, (width, height),
                                   borderValue=(255, 255, 255))
        return translated

    def flip_image(self, image, horizontal=False, vertical=False):
        if horizontal and vertical:
            return cv2.flip(image, -1)
        elif horizontal:
            return cv2.flip(image, 1)
        elif vertical:
            return cv2.flip(image, 0)
        return image

    # Filtering Operations
    def gaussian_blur(self, image, kernel_size):
        if kernel_size % 2 == 0:
            kernel_size += 1
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    def sharpen_image(self, image, strength=1.0):
        kernel = np.array([[0, -strength, 0],
                          [-strength, 1 + 4*strength, -strength],
                          [0, -strength, 0]], dtype=np.float32)
        sharpened = cv2.filter2D(image, -1, kernel)
        return np.clip(sharpened, 0, 255).astype(np.uint8)

    def emboss_effect(self, image):
        kernel = np.array([[-2, -1, 0],
                          [-1, 1, 1],
                          [0, 1, 2]], dtype=np.float32)
        embossed = cv2.filter2D(image, -1, kernel)
        return np.clip(embossed + 128, 0, 255).astype(np.uint8)

    def edge_detection(self, image):
        kernel = np.array([[-1, -1, -1],
                          [-1, 8, -1],
                          [-1, -1, -1]], dtype=np.float32)
        edges = cv2.filter2D(image, -1, kernel)
        return np.clip(edges, 0, 255).astype(np.uint8)

    # Enhancement Operations
    def histogram_equalization(self, image):
        if len(image.shape) == 3:
            yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
            yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
            return cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
        else:
            return cv2.equalizeHist(image)

    def contrast_stretch(self, image):
        if len(image.shape) == 3:
            stretched = np.zeros_like(image)
            for i in range(3):
                channel = image[:, :, i]
                min_val, max_val = np.min(channel), np.max(channel)
                if max_val > min_val:
                    stretched[:, :, i] = ((channel - min_val) / (max_val - min_val) * 255).astype(np.uint8)
                else:
                    stretched[:, :, i] = channel
            return stretched
        else:
            min_val, max_val = np.min(image), np.max(image)
            if max_val > min_val:
                return ((image - min_val) / (max_val - min_val) * 255).astype(np.uint8)
            return image

    def adjust_brightness(self, image, brightness):
        adjusted = cv2.add(image, np.ones(image.shape, dtype=np.uint8) * brightness)
        return np.clip(adjusted, 0, 255).astype(np.uint8)

    def gamma_correction(self, image, gamma):
        gamma_corrected = np.power(image / 255.0, gamma) * 255.0
        return np.clip(gamma_corrected, 0, 255).astype(np.uint8)

    # Edge Detection Operations
    def sobel_edge_detection(self, image):
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image
        sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)
        return np.clip(sobel_combined, 0, 255).astype(np.uint8)

    def canny_edge_detection(self, image, low_threshold=50, high_threshold=150):
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image
        edges = cv2.Canny(gray, low_threshold, high_threshold)
        return edges

    def laplacian_edge_detection(self, image):
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        return np.clip(np.absolute(laplacian), 0, 255).astype(np.uint8)

    def prewitt_edge_detection(self, image):
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image
        kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
        kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]], dtype=np.float32)
        prewitt_x = cv2.filter2D(gray, cv2.CV_64F, kernel_x)
        prewitt_y = cv2.filter2D(gray, cv2.CV_64F, kernel_y)
        prewitt_combined = np.sqrt(prewitt_x**2 + prewitt_y**2)
        return np.clip(prewitt_combined, 0, 255).astype(np.uint8)


def main():
    st.markdown('<h1 class="main-header">🖼️ OpenCV Image Processor</h1>', unsafe_allow_html=True)

    # Initialize session state
    if 'processor' not in st.session_state:
        st.session_state.processor = ImageProcessor()
    if 'operation' not in st.session_state:
        st.session_state.operation = None

    processor = st.session_state.processor

    # Sidebar for controls
    with st.sidebar:
        st.markdown('<div class="section-header">📁 Image Upload</div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Choose an image file", type=['png', 'jpg', 'jpeg', 'bmp', 'tiff'])

        if uploaded_file is not None:
            original_image = processor.load_image(uploaded_file)
            if original_image is not None:
                st.success(f"✅ Image loaded: {uploaded_file.name}")
                height, width = original_image.shape[:2]
                st.info(f"📏 Dimensions: {width} × {height} pixels")

                # Color Conversions
                st.markdown('<div class="section-header">🎨 Color Conversions</div>', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("RGBO to Grayscale"):
                        st.session_state.operation = "Grayscale"
                        processor.processed_image = processor.rgb_to_grayscale(original_image)
                    if st.button("RGBO to Sepia"):
                        st.session_state.operation = "Sepia"
                        processor.processed_image = processor.rgb_to_sepia(original_image)
                with col2:
                    if st.button("RGBO to HSV"):
                        st.session_state.operation = "HSV"
                        processor.processed_image = processor.rgb_to_hsv(original_image)
                    if st.button("Invert Colors"):
                        st.session_state.operation = "Invert"
                        processor.processed_image = processor.invert_colors(original_image)

                # Geometric Transformations
                st.markdown('<div class="section-header">🔄 Geometric Transformations</div>', unsafe_allow_html=True)
                st.subheader("🔄 Rotation")
                rotation_angle = st.slider("Rotation Angle", -180, 180, 0, key="rotation")
                if st.button("Apply Rotation"):
                    st.session_state.operation = f"Rotate {rotation_angle}°"
                    processor.processed_image = processor.rotate_image(original_image, rotation_angle)

                st.subheader("📏 Scaling")
                scale_factor = st.slider("Scale Factor", 0.1, 3.0, 1.0, 0.1, key="scale")
                if st.button("Apply Scaling"):
                    st.session_state.operation = f"Scale {scale_factor}x"
                    processor.processed_image = processor.scale_image(original_image, scale_factor)

                st.subheader("↔️ Translation")
                tx = st.slider("Translate X", -100, 100, 0, key="tx")
                ty = st.slider("Translate Y", -100, 100, 0, key="ty")
                if st.button("Apply Translation"):
                    st.session_state.operation = f"Translate ({tx}, {ty})"
                    processor.processed_image = processor.translate_image(original_image, tx, ty)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Flip Horizontal"):
                        st.session_state.operation = "Flip Horizontal"
                        processor.processed_image = processor.flip_image(original_image, horizontal=True)
                with col2:
                    if st.button("Flip Vertical"):
                        st.session_state.operation = "Flip Vertical"
                        processor.processed_image = processor.flip_image(original_image, vertical=True)

                # Filtering Operations
                st.markdown('<div class="section-header">🌟 Filtering Operations</div>', unsafe_allow_html=True)
                st.subheader("🌫️ Gaussian Blur")
                blur_strength = st.slider("Blur Strength", 1, 31, 5, 2, key="blur")
                if st.button("Apply Gaussian Blur"):
                    st.session_state.operation = f"Gaussian Blur {blur_strength}"
                    processor.processed_image = processor.gaussian_blur(original_image, blur_strength)

                st.subheader("✨ Sharpen")
                sharpen_strength = st.slider("Sharpen Strength", 0.1, 3.0, 1.0, 0.1, key="sharpen")
                if st.button("Apply Sharpening"):
                    st.session_state.operation = f"Sharpen {sharpen_strength}"
                    processor.processed_image = processor.sharpen_image(original_image, sharpen_strength)

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Emboss Effect"):
                        st.session_state.operation = "Emboss"
                        processor.processed_image = processor.emboss_effect(original_image)
                with col2:
                    if st.button("Edge Detection"):
                        st.session_state.operation = "Edge Detection"
                        processor.processed_image = processor.edge_detection(original_image)

                # Enhancement Operations
                st.markdown('<div class="section-header">✨ Enhancement Operations</div>', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Histogram Equalization"):
                        st.session_state.operation = "Histogram Equalization"
                        processor.processed_image = processor.histogram_equalization(original_image)
                with col2:
                    if st.button("Contrast Stretch"):
                        st.session_state.operation = "Contrast Stretch"
                        processor.processed_image = processor.contrast_stretch(original_image)

                st.subheader("💡 Brightness")
                brightness = st.slider("Brightness", -100, 100, 0, key="brightness")
                if st.button("Apply Brightness"):
                    st.session_state.operation = f"Brightness {brightness}"
                    processor.processed_image = processor.adjust_brightness(original_image, brightness)

                st.subheader("🌈 Gamma Correction")
                gamma = st.slider("Gamma", 0.1, 3.0, 1.0, 0.1, key="gamma")
                if st.button("Apply Gamma Correction"):
                    st.session_state.operation = f"Gamma {gamma}"
                    processor.processed_image = processor.gamma_correction(original_image, gamma)

                # Edge Detection Operations
                st.markdown('<div class="section-header">🔍 Edge Detection</div>', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Sobel Edge Detection"):
                        st.session_state.operation = "Sobel"
                        processor.processed_image = processor.sobel_edge_detection(original_image)
                    if st.button("Laplacian Edge Detection"):
                        st.session_state.operation = "Laplacian"
                        processor.processed_image = processor.laplacian_edge_detection(original_image)
                with col2:
                    if st.button("Prewitt Edge Detection"):
                        st.session_state.operation = "Prewitt"
                        processor.processed_image = processor.prewitt_edge_detection(original_image)

                st.subheader("🎯 Canny Edge Detection")
                canny_low = st.slider("Low Threshold", 0, 255, 50, key="canny_low")
                canny_high = st.slider("High Threshold", 0, 255, 150, key="canny_high")
                if st.button("Apply Canny Edge Detection"):
                    st.session_state.operation = f"Canny ({canny_low}, {canny_high})"
                    processor.processed_image = processor.canny_edge_detection(original_image, canny_low, canny_high)

                # Compression & Save
                st.markdown('<div class="section-header">💾 Compression & Save</div>', unsafe_allow_html=True)
                format_comp = st.selectbox("Save Format", ["PNG", "JPG", "BMP"], key="save_format")
                if st.button("💾 Save Processed Image"):
                    if processor.processed_image is not None:
                        if len(processor.processed_image.shape) == 3:
                            pil_image = Image.fromarray(processor.convert_for_display(processor.processed_image))
                        else:
                            pil_image = Image.fromarray(processor.processed_image)

                        buf = io.BytesIO()
                        if format_comp == "JPG":
                            pil_image = pil_image.convert("RGB")
                            pil_image.save(buf, format='JPEG', quality=95)
                        else:
                            pil_image.save(buf, format=format_comp)
                        buf.seek(0)
                        file_size_kb = len(buf.getvalue()) / 1024
                        st.success(f"✅ Saved as {format_comp} - Size: {file_size_kb:.2f} KB")
                        st.download_button(
                            label=f"⬇️ Download {format_comp}",
                            data=buf.getvalue(),
                            file_name=f"processed_{uploaded_file.name.split('.')[0]}.{format_comp.lower()}",
                            mime=f"image/{'jpeg' if format_comp == 'JPG' else format_comp.lower()}"
                        )

                st.markdown("---")
                if st.button("🔄 Reset to Original"):
                    processor.processed_image = None
                    st.session_state.operation = None

                # 🎥 Real-time Webcam Mode — 100% WORKING VERSION
        st.markdown('<div class="section-header">🎥 Real-time Webcam (Bonus)</div>', unsafe_allow_html=True)
        run_webcam = st.checkbox("▶️ Start Webcam", key="webcam_toggle")
        
        # Create placeholder OUTSIDE the loop
        FRAME_WINDOW = st.empty()

        if run_webcam:
            # Initialize camera
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            if not cap.isOpened():
                st.error("❌ Cannot access webcam. Check permissions or close other apps.")
                st.stop()

            # Set resolution for stability
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            st.success("✅ Webcam initialized. Press 'Stop' to end.")

            try:
                while run_webcam:  # This will break when user unchecks the box
                    ret, frame = cap.read()
                    
                    if not ret or frame is None or frame.size == 0:
                        st.warning("⚠️ Received empty frame. Skipping...")
                        time.sleep(0.1)
                        continue

                    # Optional: Apply operation
                    if st.session_state.operation:
                        try:
                            op = st.session_state.operation
                            if "Grayscale" in op:
                                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                                frame = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
                            elif "Gaussian Blur" in op:
                                ksize = int(op.split()[-1])
                                if ksize % 2 == 0: ksize += 1
                                frame = cv2.GaussianBlur(frame, (ksize, ksize), 0)
                            elif "Rotate" in op:
                                angle = int(op.split()[1][:-1])
                                h, w = frame.shape[:2]
                                center = (w // 2, h // 2)
                                M = cv2.getRotationMatrix2D(center, angle, 1.0)
                                frame = cv2.warpAffine(frame, M, (w, h))
                            elif "Scale" in op:
                                scale = float(op.split()[1][:-1])
                                h, w = frame.shape[:2]
                                new_w, new_h = int(w * scale), int(h * scale)
                                frame = cv2.resize(frame, (new_w, new_h))
                                # Pad to original size
                                canvas = np.full((h, w, 3), 255, dtype=np.uint8)
                                y1 = max(0, (h - new_h) // 2)
                                x1 = max(0, (w - new_w) // 2)
                                y2 = min(h, y1 + new_h)
                                x2 = min(w, x1 + new_w)
                                frame_cropped = frame[0:y2-y1, 0:x2-x1]
                                canvas[y1:y2, x1:x2] = frame_cropped
                                frame = canvas
                        except Exception as e:
                            st.warning(f"⚠️ Failed to apply {op}: {e}")

                    # ✅ CRITICAL: Convert BGR to RGB for Streamlit
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                    # ✅ CRITICAL: Update placeholder — this forces UI refresh
                    FRAME_WINDOW.image(frame_rgb, channels="RGB", use_container_width=True)

                    # ✅ CRITICAL: Let Streamlit breathe
                    time.sleep(0.03)  # ~30 FPS

                    # ✅ CRITICAL: Re-check checkbox state
                    run_webcam = st.session_state.webcam_toggle

            except Exception as e:
                st.error(f"🛑 Critical error: {e}")
            finally:
                cap.release()
                st.info("📹 Webcam released. Ready for next use.")

    # Main display area
    if uploaded_file is not None and processor.original_image is not None:
        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<div class="section-header">📷 Original Image</div>', unsafe_allow_html=True)
            st.image(processor.convert_for_display(processor.original_image), 
                     caption=f"Original: {uploaded_file.name}", use_container_width=True)

        with col2:
            st.markdown('<div class="section-header">⚙️ Processed Image</div>', unsafe_allow_html=True)
            if processor.processed_image is not None:
                display_image = processor.convert_for_display(processor.processed_image)
                st.image(display_image, caption=f"Applied: {st.session_state.operation}", use_container_width=True)
            else:
                st.info("👈 Select an operation from the sidebar to see the processed result")

        # Status bar
        st.markdown("---")
        cols = st.columns(4)
        cols[0].metric("Operation", st.session_state.operation if st.session_state.operation else "None")
        if processor.processed_image is not None:
            h, w = processor.processed_image.shape[:2]
            c = 3 if len(processor.processed_image.shape) == 3 else 1
            cols[1].metric("Dimensions", f"{w}×{h}×{c}")
        else:
            cols[1].metric("Dimensions", "—")
        cols[2].metric("Format", uploaded_file.type.split('/')[-1].upper())
        cols[3].metric("File Size", f"{uploaded_file.size / 1024:.1f} KB")

    else:
        st.info("👆 Please upload an image file to get started")

        # Show sample operations when no image is loaded
        st.markdown("### 🎯 Available Operations:")

        operations = {
            "🎨 Color Conversions": ["RGBO to Grayscale", "RGBO to HSV", "RGBO to Sepia", "Invert Colors"],
            "🔄 Geometric Transformations": ["Rotation", "Scaling", "Translation", "Flip Horizontal/Vertical"],
            "🌟 Filtering Operations": ["Gaussian Blur", "Sharpen", "Emboss", "Edge Detection"],
            "✨ Enhancement Operations": ["Histogram Equalization", "Contrast Stretch", "Brightness", "Gamma Correction"],
            "🔍 Edge Detection": ["Sobel", "Canny", "Laplacian", "Prewitt"],
            "💾 Compression": ["Save as JPG/PNG/BMP with size comparison"],
            "🎥 Bonus": ["Real-time Webcam Processing"]
        }

        for category, ops in operations.items():
            st.markdown(f"**{category}**")
            st.write(" • ".join(ops))

    # Footer
    st.markdown("---")
    st.caption("📘 Module 1 – Image Processing Fundamentals & Computer Vision | Deadline: Sep 8, 2025")
    st.caption("🛠️ Built with Streamlit + OpenCV | 🟢 Beginner → 🟠 Intermediate → 🔴 Advanced")


if __name__ == "__main__":
    main()