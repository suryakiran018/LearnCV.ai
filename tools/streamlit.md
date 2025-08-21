# Streamlit Guide

**Streamlit**, an open-source Python library for building interactive web applications for data science and machine learning. 

Streamlit simplifies creating data-driven apps with minimal code, integrating seamlessly with NumPy, Pandas, Matplotlib, Seaborn, Scikit-Learn, and other data science libraries.

---

## 1. Introduction to Streamlit

### What is Streamlit?
Streamlit is a Python library that enables developers to create web-based, interactive data applications quickly. It’s designed for data scientists to showcase models, visualizations, and data insights without extensive web development knowledge.

### Why Use Streamlit?
- **Simplicity**: Build apps with Python, no HTML/CSS/JavaScript required.
- **Interactivity**: Supports widgets like sliders, buttons, and file uploaders.
- **Integration**: Works with Pandas, Matplotlib, Seaborn, Scikit-Learn, and SQL.
- **Rapid Deployment**: Deploy apps to Streamlit Community Cloud or other platforms.

### Installing Streamlit
Install using pip:
```bash
pip install streamlit
```

Run a Streamlit app:
```bash
streamlit run app.py
```

### Basic Structure
A Streamlit app is a single Python script that runs top-to-bottom, re-rendering on user interaction.

---

## 2. Streamlit Basics

### Creating a Simple App
Create a file `app.py`:
```python
import streamlit as st

st.title("My First Streamlit App")
st.write("Welcome to Streamlit!")
st.markdown("This is a **data-driven** app.")
```

Run the app:
```bash
streamlit run app.py
```

### Key Components
- **Text**: Display text with `st.write`, `st.markdown`, `st.title`, `st.header`.
- **Widgets**: Interactive elements like `st.button`, `st.slider`, `st.selectbox`.
- **Data Display**: Show Pandas DataFrames with `st.dataframe` or `st.table`.
- **Visualizations**: Embed Matplotlib/Seaborn/Plotly plots with `st.pyplot` or `st.plotly_chart`.

---

## 3. Common Streamlit Components

### 3.1. Text and Markdown
Display formatted text:
```python
st.title("Data Dashboard")
st.header("Analysis Results")
st.markdown("Explore **data** with interactive controls.")
st.write("Plain text or Python objects:", [1, 2, 3])
```

### 3.2. Widgets
Add interactivity:
- **Button**:
  ```python
  if st.button("Click Me"):
      st.write("Button clicked!")
  ```
- **Slider**:
  ```python
  value = st.slider("Select a value", 0, 100, 50)
  st.write(f"Selected: {value}")
  ```
- **Selectbox**:
  ```python
  option = st.selectbox("Choose an option", ["A", "B", "C"])
  st.write(f"You selected: {option}")
  ```
- **Text Input**:
  ```python
  name = st.text_input("Enter your name")
  st.write(f"Hello, {name}!")
  ```
- **File Uploader**:
  ```python
  uploaded_file = st.file_uploader("Upload a CSV")
  if uploaded_file:
      df = pd.read_csv(uploaded_file)
      st.dataframe(df)
  ```

### 3.3. Data Display
Show Pandas DataFrames or NumPy arrays:
```python
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})
st.dataframe(df)  # Interactive table
st.table(df)      # Static table
```

### 3.4. Visualizations
Embed Matplotlib/Seaborn plots:
```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
sns.lineplot(x=x, y=y, ax=ax)
ax.set_title("Sine Wave")
st.pyplot(fig)
```

Embed Plotly for interactivity:
```python
import plotly.express as px
fig = px.scatter(df, x='Age', y='Name', title="Scatter Plot")
st.plotly_chart(fig)
```

---

## 4. Integration with Data Science Libraries

### Pandas and NumPy
Create a data exploration app:
```python
st.title("Data Explorer")
uploaded_file = st.file_uploader("Upload CSV")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df.head())
    st.write("Summary Statistics:")
    st.write(df.describe())
```

### Scikit-Learn
Build a model prediction app:
```python
from sklearn.linear_model import LinearRegression
st.title("House Price Predictor")
square_feet = st.slider("Square Feet", 500, 5000, 2000)
bedrooms = st.slider("Bedrooms", 1, 5, 3)
model = LinearRegression()
# Assume trained model
X = np.array([[square_feet, bedrooms]])
prediction = model.predict(X)[0]
st.write(f"Predicted Price: ${prediction:.2f}")
```

### Matplotlib/Seaborn
Interactive visualization with filters:
```python
st.title("Interactive Plot")
column = st.selectbox("Select Column", df.columns)
fig, ax = plt.subplots()
sns.histplot(df[column], kde=True, ax=ax)
st.pyplot(fig)
```

### SQL
Connect to a database:
```python
import sqlite3
conn = sqlite3.connect('example.db')
df = pd.read_sql_query("SELECT * FROM users", conn)
st.dataframe(df)
```

---

## 5. Layout and Customization

### Sidebar
Add controls in a sidebar:
```python
st.sidebar.title("Settings")
theme = st.sidebar.selectbox("Theme", ["light", "dark"])
if theme == "dark":
    st.markdown("<style>body {background-color: #333; color: white;}</style>", unsafe_allow_html=True)
```

### Columns
Arrange content in columns:
```python
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
    st.dataframe(df)
with col2:
    st.write("Column 2")
    fig, ax = plt.subplots()
    sns.histplot(df['Age'], ax=ax)
    st.pyplot(fig)
```

### Containers
Group content:
```python
with st.container():
    st.write("Inside Container")
    st.button("Click")
```

### Themes
Customize appearance:
```python
st.set_page_config(page_title="My App", layout="wide")  # Wide or centered layout
```

---

## 6. Advanced Streamlit Features

### 6.1. Session State
Persist data across interactions:
```python
if 'count' not in st.session_state:
    st.session_state.count = 0
if st.button("Increment"):
    st.session_state.count += 1
st.write(f"Count: {st.session_state.count}")
```

### 6.2. Caching
Cache expensive computations:
```python
@st.cache_data
def load_data(file):
    return pd.read_csv(file)
df = load_data(uploaded_file)
```

Cache models:
```python
@st.cache_resource
def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model
```

### 6.3. Forms
Group inputs for batch submission:
```python
with st.form("user_form"):
    name = st.text_input("Name")
    age = st.slider("Age", 1, 100)
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write(f"Name: {name}, Age: {age}")
```

### 6.4. File Downloads
Allow users to download data:
```python
csv = df.to_csv(index=False)
st.download_button("Download CSV", data=csv, file_name="data.csv")
```

---

## 7. Useful Streamlit Methods

### Text and Display
- `st.title()`, `st.header()`, `st.subheader()`: Headings.
- `st.write()`: Display text or objects.
- `st.markdown()`: Render Markdown.
- `st.dataframe()`, `st.table()`: Display DataFrames.

### Widgets
- `st.button(label)`: Trigger actions.
- `st.slider(label, min, max, default)`: Numeric input.
- `st.selectbox(label, options)`: Dropdown menu.
- `st.text_input(label)`: Text input.
- `st.file_uploader(label)`: File upload.

### Visualizations
- `st.pyplot(fig)`: Display Matplotlib/Seaborn plots.
- `st.plotly_chart(fig)`: Display Plotly plots.
- `st.image(image)`: Display images.

### Layout
- `st.sidebar`: Add widgets to sidebar.
- `st.columns(n)`: Create column layout.
- `st.container()`: Group content.
- `st.form(key)`: Group inputs for submission.

---

## 8. Streamlit Tricks and Tips

### 1. **Dynamic Filtering**
Filter data interactively:
```python
column = st.selectbox("Filter Column", df.columns)
value = st.slider("Max Value", float(df[column].min()), float(df[column].max()))
filtered_df = df[df[column] <= value]
st.dataframe(filtered_df)
```

### 2. **Interactive Model Predictions**
Update predictions in real-time:
```python
st.title("Real-Time Prediction")
feature1 = st.slider("Feature 1", 0, 100)
feature2 = st.slider("Feature 2", 0, 100)
X = np.array([[feature1, feature2]])
prediction = model.predict(X)[0]
st.write(f"Prediction: {prediction:.2f}")
```

### 3. **Custom CSS**
Style with Markdown:
```python
st.markdown("""
    <style>
        .stButton>button {background-color: #4CAF50; color: white;}
    </style>
""", unsafe_allow_html=True)
```

### 4. **Progress Bar**
Show progress for long tasks:
```python
import time
progress = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress.progress(i + 1)
```

### 5. **Error Handling**
Handle invalid inputs:
```python
try:
    value = int(st.text_input("Enter a number"))
    st.write(f"Value: {value}")
except ValueError:
    st.error("Please enter a valid number!")
```

### 6. **Multi-Page Apps**
Use `st.set_page_config` and multiple files:
```python
# pages/page1.py
st.title("Page 1")
st.write("Welcome to Page 1")
```
Organize in a `pages/` folder and run the main app.

### 7. **Interactive Visualizations**
Use Plotly for interactivity:
```python
fig = px.scatter(df, x='Age', y='Name', color='Age')
st.plotly_chart(fig, use_container_width=True)
```

### 8. **Cache Large Data**
Cache database queries:
```python
@st.cache_data
def load_sql_data(query):
    conn = sqlite3.connect('example.db')
    return pd.read_sql_query(query, conn)
df = load_sql_data("SELECT * FROM users")
```

### 9. **Streamlit Components**
Use custom components (e.g., `streamlit-components`):
```python
from streamlit.components.v1 import html
html("<b>Custom HTML</b>")
```

### 10. **Deploy to Streamlit Cloud**
Deploy apps:
1. Push code to a GitHub repository.
2. Connect to [Streamlit Community Cloud](https://streamlit.io/cloud).
3. Configure `requirements.txt`:
   ```
   streamlit
   pandas
   numpy
   matplotlib
   seaborn
   scikit-learn
   ```

---

## 9. Best Practices

- **Keep Code Simple**: Write clear, modular code in a single script.
- **Use Caching**: Cache expensive operations with `@st.cache_data` or `@st.cache_resource`.
- **Validate Inputs**: Handle user input errors gracefully.
- **Optimize Visuals**: Use Plotly for interactive plots, Matplotlib/Seaborn for static.
- **Document Apps**: Add Markdown for user instructions.

---

## 10. Troubleshooting & Tips

### Common Issues
- **App Not Updating**: Ensure script reruns on changes (`streamlit run app.py`).
- **Performance Issues**: Cache data and downsample large datasets:
  ```python
  df = df.sample(1000)
  ```
- **Widget State Loss**: Use `st.session_state` for persistence.

### Performance Tips
- **Cache Models and Data**: Use `@st.cache_resource` for Scikit-Learn models.
- **Downsample Visuals**: Reduce data for faster plotting:
  ```python
  df = df.iloc[::10]
  ```
- **Use Plotly**: For faster, interactive visualizations.

---

## 11. Resources & Further Learning

- **Official Documentation**: [Streamlit Docs](https://docs.streamlit.io/)
- **Tutorials**: [Streamlit Tutorial](https://docs.streamlit.io/library/get-started), [Kaggle Streamlit](https://www.kaggle.com/learn)
- **Books**: "Getting Started with Streamlit for Data Science" by Tyler Richards
- **Community**: [Streamlit Community](https://discuss.streamlit.io/), [Stack Overflow](https://stackoverflow.com/questions/tagged/streamlit)

---