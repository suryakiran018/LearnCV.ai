# Image Processing Toolkit – Submission Pack

## Files
- `app.py` – Streamlit GUI application (OpenCV-based)
- `ImageToolkit.ipynb` – Theory + practice notebook
- `Report_Template.md` – Fill this and export to PDF for submission

## How to run
1. Install dependencies:

   ```bash
   pip install streamlit opencv-python numpy pillow
   ```
2. Launch app:

   ```bash
   streamlit run app.py
   ```
3. Open the local URL and use the sidebar to try operations. Save processed output via the button at the bottom.

## Notes
- The app simulates a **Menu Bar** within Streamlit constraints.
- Status bar updates dimensions, file format, DPI (if present), and file size.

- Bonus:

  - Sliders for kernels, rotation, scaling, thresholds

  - Split-screen comparison

  - Experimental webcam demo (may require local run permissions)
