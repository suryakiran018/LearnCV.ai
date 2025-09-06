# Matplotlib Guide

## 1. Introduction to Matplotlib

### What is Matplotlib?
Matplotlib is a Python library for creating 2D and 3D plots, charts, and visualizations. It supports a variety of plot types, including line plots, scatter plots, histograms, and more, with extensive customization options.

### Why Use Matplotlib?
- **Versatility**: Supports diverse plot types for data exploration and presentation.
- **Integration**: Works with NumPy, Pandas, and SciPy for data science workflows.
- **Customizability**: Offers fine-grained control over plot appearance.

### Installing Matplotlib
Install using pip:
```bash
pip install matplotlib
```

### Importing Matplotlib
Use the `pyplot` module for most plotting tasks:
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
```

---

## 2. Matplotlib Basics

### Creating a Simple Plot
Create a basic line plot with NumPy:
```python
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)')
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.show()
```

### Figure and Axes
Matplotlib organizes plots using `Figure` (the entire canvas) and `Axes` (individual plot areas):
```python
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, 'b-', label='sin(x)')
ax.set_title("Sine Wave")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.legend()
ax.grid(True)
plt.show()
```

### Saving Plots
Save plots to files with customizable resolution:
```python
plt.plot(x, y)
plt.savefig("sine_wave.png", dpi=300, bbox_inches="tight")
plt.close()  # Close to free memory
```

---

## 3. Common Plot Types

### 3.1. Line Plot
Visualize continuous data:
```python
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, 'b--', label='sin(x)')
plt.plot(x, y2, 'r-', label='cos(x)')
plt.legend()
plt.title("Sine and Cosine")
plt.show()
```

### 3.2. Scatter Plot
Plot discrete data points:
```python
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, color='green', s=100, alpha=0.6, label='Points')
plt.title("Random Scatter")
plt.legend()
plt.show()
```

### 3.3. Bar Plot
Display categorical data:
```python
categories = ['A', 'B', 'C']
values = [4, 3, 2]
plt.bar(categories, values, color='purple')
plt.title("Bar Chart")
plt.show()
```

### 3.4. Histogram
Visualize data distributions:
```python
data = np.random.normal(0, 1, 1000)
plt.hist(data, bins=30, color='orange', edgecolor='black')
plt.title("Histogram")
plt.show()
```

### 3.5. Box Plot
Show data distribution and outliers:
```python
data = [np.random.normal(0, 1, 100), np.random.normal(2, 1.5, 100)]
plt.boxplot(data, labels=['Group 1', 'Group 2'])
plt.title("Box Plot")
plt.show()
```

### 3.6. Subplots
Create multiple plots in one figure:
```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.plot(x, np.sin(x), 'b-')
ax1.set_title("Sine")
ax2.plot(x, np.cos(x), 'r-')
ax2.set_title("Cosine")
plt.tight_layout()
plt.show()
```

---

## 4. Integration with Pandas
Matplotlib integrates seamlessly with Pandas for plotting DataFrames:
```python
df = pd.DataFrame({
    'x': np.linspace(0, 10, 100),
    'sin': np.sin(np.linspace(0, 10, 100)),
    'cos': np.cos(np.linspace(0, 10, 100))
})
df.plot(x='x', y=['sin', 'cos'], title="Sine and Cosine", figsize=(8, 5))
plt.show()
```

Pandas with Matplotlib for grouped data:
```python
df = pd.DataFrame({
    'category': ['A', 'A', 'B', 'B'],
    'value': [10, 15, 20, 25]
})
df.groupby('category')['value'].mean().plot(kind='bar', color='teal')
plt.title("Mean Value by Category")
plt.show()
```

---

## 5. Customization

### Colors and Styles
Customize appearance:
```python
plt.plot(x, y, color='#FF5733', linestyle='--', linewidth=2, marker='o', markersize=5)
plt.show()
```

### Annotations
Add text or arrows:
```python
plt.plot(x, y)
plt.annotate('Peak', xy=(np.pi/2, 1), xytext=(np.pi/2, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```

### Axis Customization
Set limits and ticks:
```python
plt.plot(x, y)
plt.xlim(0, 5)
plt.ylim(-1.5, 1.5)
plt.xticks(np.arange(0, 5.1, 1))
plt.yticks([-1, 0, 1])
plt.show()
```

### Logarithmic Scale
For exponential data:
```python
x = np.logspace(0, 3, 100)
y = x**2
plt.plot(x, y)
plt.xscale('log')
plt.yscale('log')
plt.title("Log-Log Plot")
plt.show()
```

### Styles
Use predefined styles for consistent aesthetics:
```python
plt.style.use('ggplot')
plt.plot(x, y)
plt.show()
```

---

## 6. Advanced Matplotlib Features

### 6.1. 3D Plots
Create 3D visualizations:
```python
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
Z = np.sin(np.sqrt(X**2 + Y**2))
ax.plot_surface(X, Y, Z, cmap='viridis')
plt.title("3D Surface Plot")
plt.show()
```

### 6.2. Animations
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

### 6.3. Heatmaps
Visualize matrix data:
```python
data = np.random.rand(10, 10)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title("Heatmap")
plt.show()
```

---

## 7. Useful Matplotlib Methods

### Plotting Methods
- `plt.plot()`: Line plots.
- `plt.scatter()`: Scatter plots.
- `plt.bar()`: Bar charts.
- `plt.hist()`: Histograms.
- `plt.boxplot()`: Box plots.
- `plt.contour()`: Contour plots.
- `plt.imshow()`: Image/heatmap plots.

### Figure and Axes Methods
- `fig.subplots(nrows, ncols)`: Create subplot grid.
- `ax.set_xlim()`, `ax.set_ylim()`: Set axis limits.
- `ax.set_xticks()`, `ax.set_yticks()`: Customize ticks.
- `ax.legend()`: Add legend.
- `ax.grid(True)`: Enable grid.

### Customization Methods
- `plt.style.use('style_name')`: Apply styles (e.g., 'seaborn', 'bmh').
- `plt.rcParams`: Set global settings.
  ```python
  plt.rcParams['font.size'] = 12
  plt.rcParams['font.family'] = 'Arial'
  ```

---

## 8. Matplotlib Tricks and Tips

### 1. **Use Context Managers**
Manage figures to avoid memory leaks:
```python
with plt.style.context('seaborn'):
    plt.plot(x, y)
    plt.show()
```

### 2. **Efficient Plotting for Large Data**
Downsample large datasets:
```python
x = np.linspace(0, 10, 10000)
y = np.sin(x)
plt.plot(x[::10], y[::10])  # Plot every 10th point
plt.show()
```

### 3. **Custom Colormaps**
Create custom colormaps:
```python
from matplotlib.colors import LinearSegmentedColormap
colors = ['blue', 'white', 'red']
cmap = LinearSegmentedColormap.from_list('custom', colors)
plt.scatter(x, y, c=y, cmap=cmap)
plt.colorbar()
plt.show()
```

### 4. **Interactive Plots in Jupyter**
Enable interactive mode:
```python
%matplotlib notebook
plt.plot(x, y)
plt.show()
```

### 5. **Annotate with DataFrame**
Annotate points using Pandas:
```python
df = pd.DataFrame({'x': x[:5], 'y': y[:5]})
plt.scatter(df['x'], df['y'])
for i, row in df.iterrows():
    plt.annotate(f'({row["x"]:.1f}, {row["y"]:.1f})', (row['x'], row['y']))
plt.show()
```

### 6. **Save Multiple Formats**
Save in multiple formats efficiently:
```python
for fmt in ['png', 'pdf']:
    plt.plot(x, y)
    plt.savefig(f'plot.{fmt}', dpi=300, bbox_inches='tight')
    plt.close()
```

### 7. **Logarithmic Bins for Histograms**
Use logarithmic bins for skewed data:
```python
data = np.random.lognormal(0, 1, 1000)
plt.hist(data, bins=np.logspace(np.log10(data.min()), np.log10(data.max()), 30))
plt.xscale('log')
plt.show()
```

### 8. **Tight Layout**
Avoid overlapping elements:
```python
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x, y)
ax2.plot(x, y)
plt.tight_layout()
plt.show()
```

### 9. **Custom Tick Formatting**
Format axis ticks:
```python
from matplotlib.ticker import FuncFormatter
plt.plot(x, y)
plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.1f}π'))
plt.show()
```

### 10. **Seamless Pandas Integration**
Use Pandas plotting with Matplotlib customization:
```python
ax = df.plot.scatter(x='x', y='sin', c='cos', cmap='viridis')
ax.set_title("Colored Scatter")
plt.colorbar(ax.collections[0], label='cos(x)')
plt.show()
```

---

## 9. Best Practices

- **Label Everything**: Always include titles, axis labels, and legends.
- **Use Vectorized Data**: Leverage NumPy arrays for efficiency.
- **Close Figures**: Use `plt.close()` in loops to free memory.
- **Choose Appropriate Colors**: Use colorblind-friendly colormaps (e.g., `viridis`).
- **Optimize for Output**: Adjust `dpi` and `bbox_inches` for high-quality exports.

---

## 10. Troubleshooting & Tips

### Common Issues
- **Plot Not Displaying**: Ensure `plt.show()` or use `%matplotlib inline` in Jupyter.
- **Overlapping Labels**: Use `plt.tight_layout()` or adjust manually.
- **Font Issues**: Set consistent fonts:
  ```python
  plt.rcParams['font.family'] = 'Arial'
  ```

### Performance Tips
- **Downsample Large Data**: Plot fewer points for faster rendering.
- **Use `plt.clf()`**: Clear figure between plots to avoid overlap.
- **Vector Graphics**: Save as SVG or PDF for scalable outputs:
  ```python
  plt.savefig('plot.svg')
  ```

---

## 11. Resources & Further Learning

- **Official Documentation**: [Matplotlib Docs](https://matplotlib.org/stable/contents.html)
- **Tutorials**: [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html), [Kaggle Visualization](https://www.kaggle.com/learn/data-visualization)
- **Books**: "Python Data Science Handbook" by Jake VanderPlas
- **Community**: [Stack Overflow](https://stackoverflow.com/questions/tagged/matplotlib), [Matplotlib GitHub](https://github.com/matplotlib/matplotlib)

---                                             