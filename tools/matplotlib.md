# Matplotlib Guide

## 1. Introduction to Matplotlib

### What is Matplotlib?
Matplotlib is a Python library for creating 2D and 3D plots, charts, and visualizations. It supports a wide range of plot types, including line plots, scatter plots, bar charts, histograms, and more, with extensive customization options.

### Why Use Matplotlib?
- **Versatility**: Supports diverse plot types and customizations.
- **Integration**: Works seamlessly with NumPy, SciPy, and pandas.

### Installing Matplotlib
Install Matplotlib using pip:
```bash
pip install matplotlib
```

### Importing Matplotlib
Use the `pyplot` module for most plotting tasks:
```python
import matplotlib.pyplot as plt
import numpy as np
```

---

## 2. Matplotlib Basics

### Creating a Simple Plot
Create a basic line plot:
```python
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
```

### Figure and Axes
Matplotlib uses a `Figure` (the entire window) and `Axes` (the plot area) to organize plots:
```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Sine Wave")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.grid(True)
plt.show()
```

### Saving Plots
Save a plot to a file:
```python
plt.plot(x, y)
plt.savefig("sine_wave.png", dpi=300, bbox_inches="tight")
plt.close()
```

---

## 3. Common Plot Types

### 3.1. Line Plot
Plot continuous data:
```python
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label="sin(x)", color="blue", linestyle="--")
plt.plot(x, y2, label="cos(x)", color="red")
plt.legend()
plt.title("Sine and Cosine")
plt.show()
```

### 3.2. Scatter Plot
Plot discrete data points:
```python
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, color="green", marker="o", s=100, alpha=0.6)
plt.title("Random Scatter")
plt.show()
```

### 3.3. Bar Plot
Display categorical data:
```python
categories = ["A", "B", "C"]
values = [4, 3, 2]
plt.bar(categories, values, color="purple")
plt.title("Bar Chart")
plt.show()
```

### 3.4. Histogram
Visualize data distribution:
```python
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30, color="orange", edgecolor="black")
plt.title("Histogram")
plt.show()
```

### 3.5. Pie Chart
Show proportions:
```python
labels = ["A", "B", "C"]
sizes = [215, 130, 245]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", colors=["red", "blue", "green"])
plt.title("Pie Chart")
plt.show()
```

### 3.6. Subplots
Create multiple plots in one figure:
```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x, np.sin(x), "b-")
ax1.set_title("Sine")
ax2.plot(x, np.cos(x), "r-")
ax2.set_title("Cosine")
plt.tight_layout()
plt.show()
```

---

## 4. Customization

### Colors and Styles
Customize line styles, colors, and markers:
```python
plt.plot(x, y, color="#FF5733", linestyle="--", linewidth=2, marker="o", markersize=5)
plt.show()
```

### Annotations
Add text or arrows:
```python
plt.plot(x, y)
plt.annotate("Max", xy=(np.pi/2, 1), xytext=(np.pi/2, 1.5),
             arrowprops=dict(facecolor="black", shrink=0.05))
plt.show()
```

### Axis Limits and Ticks
Control axis ranges and labels:
```python
plt.plot(x, y)
plt.xlim(0, 5)
plt.ylim(-1.5, 1.5)
plt.xticks(np.arange(0, 5.1, 1))
plt.show()
```

### Logarithmic Scale
Use logarithmic axes:
```python
x = np.logspace(0, 3, 100)
y = x**2
plt.plot(x, y)
plt.xscale("log")
plt.yscale("log")
plt.title("Log-Log Plot")
plt.show()
```

---

## 5. Advanced Matplotlib Features

### 5.1. 3D Plots
Create 3D visualizations:
```python
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, cmap="viridis")
plt.title("3D Surface Plot")
plt.show()
```

### 5.2. Animations
Create animated plots:
```python
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
line, = ax.plot(x, np.sin(x))
def update(frame):
    line.set_ydata(np.sin(x + frame/10))
    return line,
ani = FuncAnimation(fig, update, frames=100, interval=50)
plt.show()
```

### 5.3. Plotting with Pandas
Integrate with pandas DataFrames:
```python
import pandas as pd
df = pd.DataFrame({"x": x, "sin": np.sin(x), "cos": np.cos(x)})
df.plot(x="x", y=["sin", "cos"], title="Sine and Cosine")
plt.show()
```

---

## 6. Matplotlib: Most Useful Functions

### 6.1 Basic Plotting

| Function                        | Description              |
| ------------------------------- | ------------------------ |
| `plt.plot(x, y)`                | Line plot of `y` vs. `x` |
| `plt.scatter(x, y)`             | Scatter plot of points   |
| `plt.bar(x, height)`            | Vertical bar chart       |
| `plt.barh(y, width)`            | Horizontal bar chart     |
| `plt.hist(data, bins=10)`       | Histogram                |
| `plt.boxplot(data)`             | Box and whisker plot     |
| `plt.pie(sizes, labels=labels)` | Pie chart                |

### 6.2 Figure and Axes Management

| Function                           | Description                              |
| ---------------------------------- | ---------------------------------------- |
| `plt.figure(figsize=(w, h))`       | Create a new figure                      |
| `plt.subplot(nrows, ncols, index)` | Add subplot (e.g., `plt.subplot(2,2,1)`) |
| `fig, ax = plt.subplots()`         | Create figure and axes object            |
| `fig.add_subplot(...)`             | Add subplot to existing figure           |

### 6.3 Labels and Titles

| Function                                               | Description                        |
| ------------------------------------------------------ | ---------------------------------- |
| `plt.title("Title")`                                   | Set plot title                     |
| `plt.xlabel("X Axis")`                                 | Label x-axis                       |
| `plt.ylabel("Y Axis")`                                 | Label y-axis                       |
| `ax.set_title()`, `ax.set_xlabel()`, `ax.set_ylabel()` | Same for object-oriented interface |

### 6.4 Ticks and Limits

| Function             | Description        |
| -------------------- | ------------------ |
| `plt.xlim(min, max)` | Set x-axis limits  |
| `plt.ylim(min, max)` | Set y-axis limits  |
| `plt.xticks([...])`  | Set custom x-ticks |
| `plt.yticks([...])`  | Set custom y-ticks |

### 6.5 Legends and Annotations
| Function                                                        | Description                                    |
| --------------------------------------------------------------- | ---------------------------------------------- |
| `plt.legend()`                                                  | Add legend (use `label=...` in plot functions) |
| `plt.annotate(text, xy=(x, y), xytext=(tx, ty), arrowprops={})` | Add annotations                                |

### 6.6 Styling

| Function                   | Description                                                   |
| -------------------------- | ------------------------------------------------------------- |
| `plt.grid(True)`           | Add grid lines                                                |
| `plt.style.use('style')`   | Use a style (e.g. `'ggplot'`, `'seaborn'`)                    |
| `plt.set_cmap('colormap')` | Set color map (e.g. `'viridis'`)                              |
| `plt.colorbar()`           | Show color bar (for heatmaps, scatter plots with color, etc.) |

### 6.6 Image Display

| Function              | Description                          |
| --------------------- | ------------------------------------ |
| `plt.imshow(img)`     | Display an image (NumPy array)       |
| `plt.matshow(matrix)` | Display a matrix as color-coded grid |
#### Saving & Displaying
| Function                           | Description             |
| ---------------------------------- | ----------------------- |
| `plt.savefig("file.png", dpi=300)` | Save figure to file     |
| `plt.show()`                       | Display the plot window |

## 7. Best Practices

- **Use Descriptive Labels**: Always label axes, titles, and legends for clarity.
- **Choose Appropriate Colors**: Use distinct, colorblind-friendly colors (e.g., `viridis` cmap).
- **Optimize for Output**: Adjust `dpi` and `bbox_inches` for high-quality saved plots.
- **Close Plots**: Use `plt.close()` to free memory, especially in loops.
- **Leverage Styles**: Use predefined styles for consistent aesthetics:
  ```python
  plt.style.use("ggplot")  # Apply ggplot style
  plt.plot(x, y)
  plt.show()
  ```

---

## 8. Troubleshooting & Tips

### Common Issues
- **Figure Not Displaying**: Ensure `plt.show()` is called or use `%matplotlib inline` in Jupyter.
- **Font Issues**: Set a default font for consistency:
  ```python
  plt.rcParams["font.family"] = "Arial"
  ```
- **Overlapping Elements**: Use `plt.tight_layout()` to adjust spacing.

### Performance Tips
- **Downsample Data**: For large datasets, reduce points to improve rendering speed:
  ```python
  x = np.linspace(0, 10, 10000)
  y = np.sin(x)
  plt.plot(x[::10], y[::10])  # Plot every 10th point
  plt.show()
  ```

- **Use Vectorized Operations**: Avoid loops; rely on NumPy for data preparation.

---

## 9. Resources & Further Learning

- **Official Documentation**: [Matplotlib Docs](https://matplotlib.org/stable/contents.html)
- **Books**: "Python Data Science Handbook" by Jake VanderPlas
- **Community**: [Stack Overflow](https://stackoverflow.com/questions/tagged/matplotlib), [Matplotlib GitHub](https://github.com/matplotlib/matplotlib)

---