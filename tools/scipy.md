# SciPy Guide

## 1. Introduction to SciPy

### What is SciPy?
SciPy (**Scientific Python**) is an open-source library in Python, extending NumPy with specialized modules for advanced mathematical operations, data analysis, and scientific applications. It is widely used in fields like physics, engineering, and data science.

SciPy offers modules for optimization, linear algebra, integration, interpolation, signal processing, and more.

### Installing SciPy
Install SciPy using pip:
```bash
pip install scipy
```

### Importing SciPy
SciPy submodules are imported individually:
```python
import numpy as np
from scipy import optimize, integrate, interpolate, linalg, signal, stats
```

---

## 2. Core SciPy Modules

SciPy organizes its functionality into submodules. Below are the most commonly used ones with examples.

### 2.1. Linear Algebra (`scipy.linalg`)
Provides advanced linear algebra operations beyond NumPy.

- **Matrix Inverse**:
  ```python
  from scipy import linalg
  A = np.array([[1, 2], [3, 4]])
  A_inv = linalg.inv(A)
  print(A_inv)
  # Output:
  # [[-2.   1. ]
  #  [ 1.5 -0.5]]
  ```

- **Eigenvalues and Eigenvectors**:
  ```python
  eigenvalues, eigenvectors = linalg.eig(A)
  print(eigenvalues)  # Output: [-0.37228132+0.j  5.37228132+0.j]
  ```

### 2.2. Optimization (`scipy.optimize`)
Solve optimization problems, such as finding minima or roots.

- **Minimize a Function**:
  ```python
  from scipy import optimize
  def f(x): return x**2 + 2*x + 1
  result = optimize.minimize(f, x0=0)
  print(result.x)  # Output: [-1.] (minimum at x = -1)
  ```

- **Root Finding**:
  ```python
  def f(x): return x**3 - x - 2
  root = optimize.root(f, x0=1)
  print(root.x)  # Output: [1.25992105]
  ```

### 2.3. Integration (`scipy.integrate`)
Perform numerical integration.

- **Single Integral**:
  ```python
  from scipy import integrate
  def f(x): return x**2
  result, error = integrate.quad(f, 0, 1)  # Integrate x^2 from 0 to 1
  print(result)  # Output: 0.3333333333333333 (1/3)
  ```

- **Ordinary Differential Equations (ODEs)**:
  ```python
  from scipy.integrate import odeint
  def dy_dt(y, t): return -2 * y  # dy/dt = -2y
  t = np.linspace(0, 5, 100)
  y = odeint(dy_dt, y0=1, t=t)
  print(y[:5])  # Output: First few values of solution
  ```

### 2.4. Interpolation (`scipy.interpolate`)
Interpolate data points to create smooth functions.

- **1D Interpolation**:
  ```python
  from scipy import interpolate
  x = np.array([0, 1, 2, 3])
  y = np.array([0, 1, 4, 9])
  f = interpolate.interp1d(x, y, kind='cubic')
  x_new = np.array([0.5, 1.5, 2.5])
  print(f(x_new))  # Output: Interpolated values
  ```

### 2.5. Signal Processing (`scipy.signal`)
Analyze and process signals.

- **Convolution**:
  ```python
  from scipy import signal
  t = np.linspace(0, 1, 100)
  sig1 = np.sin(2 * np.pi * t)
  sig2 = np.ones(10)
  conv = signal.convolve(sig1, sig2, mode='valid')
  print(conv[:5])  # Output: First few convolved values
  ```

- **Filtering**:
  ```python
  b, a = signal.butter(4, 0.2)  # 4th-order low-pass filter
  filtered = signal.filtfilt(b, a, sig1)
  print(filtered[:5])  # Output: First few filtered values
  ```

### 2.6. Statistics (`scipy.stats`)
Perform statistical analysis and work with probability distributions.

- **Normal Distribution**:
  ```python
  from scipy import stats
  mean, std = 0, 1
  norm_dist = stats.norm(mean, std)
  print(norm_dist.pdf(0))  # Output: 0.3989422804014327 (PDF at x=0)
  ```

- **T-Test**:
  ```python
  data1 = np.random.normal(0, 1, 100)
  data2 = np.random.normal(0.5, 1, 100)
  t_stat, p_val = stats.ttest_ind(data1, data2)
  print(p_val)  # Output: P-value for t-test
  ```

---

## 3. Working with NumPy Arrays
SciPy builds on NumPy, so all operations use NumPy arrays. Ensure compatibility by using `np.array` for inputs:
```python
arr = np.array([1, 2, 3])
print(linalg.norm(arr))  # Output: 3.7416573867739413 (Euclidean norm)
```

---

## 4. Advanced SciPy Features

### 4.1. Sparse Matrices (`scipy.sparse`)
Handle large, sparse matrices efficiently.

- **Create a Sparse Matrix**:
  ```python
  from scipy import sparse
  data = np.array([1, 2, 3])
  row = np.array([0, 1, 2])
  col = np.array([0, 1, 2])
  sparse_mat = sparse.csr_matrix((data, (row, col)), shape=(3, 3))
  print(sparse_mat.toarray())
  # Output:
  # [[1 0 0]
  #  [0 2 0]
  #  [0 0 3]]
  ```

### 4.2. Fourier Transforms (`scipy.fft`)
Perform Fast Fourier Transforms for frequency analysis.

- **FFT**:
  ```python
  from scipy import fft
  t = np.linspace(0, 1, 100)
  signal = np.sin(2 * np.pi * 10 * t)
  freq = fft.fft(signal)
  print(np.abs(freq[:5]))  # Output: First few frequency components
  ```

### 4.3. Spatial Algorithms (`scipy.spatial`)
Compute distances, Delaunay triangulations, and more.

- **Euclidean Distance**:
  ```python
  from scipy import spatial
  points = np.array([[0, 0], [3, 4]])
  dist = spatial.distance.euclidean(points[0], points[1])
  print(dist)  # Output: 5.0
  ```

---

## 5. Best Practices

- **Use NumPy Arrays**: Always pass NumPy arrays to SciPy functions for compatibility.
- **Check Input Shapes**: Ensure arrays have correct dimensions for operations.
  ```python
  A = np.array([[1, 2], [3, 4]])
  b = np.array([5, 6])
  x = linalg.solve(A, b)  # Ensure A is square, b has matching size
  ```
- **Leverage Documentation**: Refer to [SciPy Docs](https://docs.scipy.org/doc/scipy/) for detailed function parameters.
- **Optimize Performance**: Use sparse matrices or vectorized operations for large datasets.

---

## 6. Troubleshooting & Tips

### Common Issues
- **Shape Mismatch**:
  ```python
  A = np.array([[1, 2], [3, 4]])
  b = np.array([5, 6, 7])  # Wrong size
  # Fix: Ensure b has length equal to A’s rows
  ```
- **Convergence Issues in Optimization**:
  Use appropriate initial guesses or methods:
  ```python
  result = optimize.minimize(f, x0=0, method='Nelder-Mead')  # Robust method
  ```

### Performance Tips
- Use `scipy.sparse` for large, sparse datasets to save memory.
- Avoid loops; leverage SciPy’s vectorized functions:
  ```python
  data = np.random.rand(1000)
  result = stats.norm.pdf(data)  # Vectorized PDF calculation
  ```

---

## 7. Resources & Further Learning

- **Official Documentation**: [SciPy Docs](https://docs.scipy.org/doc/scipy/)
- **Books**: "SciPy and NumPy: An Overview for Developers" by Eli Bressert
- **Community**: [Stack Overflow](https://stackoverflow.com/questions/tagged/scipy), [SciPy GitHub](https://github.com/scipy/scipy)

---