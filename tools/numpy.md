# NumPy Guide

## 1. Introduction to NumPy

### What is NumPy?
NumPy (Numerical Python) is a Python library for working with multi-dimensional arrays and matrices. It provides fast, vectorized operations and a wide range of mathematical functions, making it essential for numerical and scientific computing.

### Why Use NumPy?
- **Performance**: Arrays are stored in contiguous memory, enabling faster computations than Python lists.
- **Functionality**: Supports linear algebra, random number generation, and more.
- **Integration**: Works seamlessly with Pandas, SciPy, Matplotlib, and Scikit-Learn.

### Installing NumPy
Install using pip:
```bash
pip install numpy
```

### Importing NumPy
```python
import numpy as np
```

---

## 2. Core Data Structure: NumPy Arrays

### Creating Arrays
NumPy’s primary data structure is the `ndarray` (n-dimensional array).

- **From Lists**:
  ```python
  arr = np.array([1, 2, 3])
  print(arr)  # Output: [1 2 3]
  ```

- **Multi-Dimensional Arrays**:
  ```python
  arr_2d = np.array([[1, 2], [3, 4]])
  print(arr_2d)
  # Output:
  # [[1 2]
  #  [3 4]]
  ```

- **Special Arrays**:
  ```python
  zeros = np.zeros((2, 3))  # 2x3 array of zeros
  ones = np.ones((2, 3))   # 2x3 array of ones
  eye = np.eye(3)          # 3x3 identity matrix
  arange = np.arange(0, 10, 2)  # Array: [0, 2, 4, 6, 8]
  linspace = np.linspace(0, 1, 5)  # Array: [0. 0.25 0.5 0.75 1.]
  ```

### Array Attributes
- **Shape**: Dimensions of the array.
  ```python
  print(arr_2d.shape)  # Output: (2, 2)
  ```
- **Data Type**: Type of elements.
  ```python
  print(arr.dtype)  # Output: int64 (or similar)
  ```
- **Size**: Total number of elements.
  ```python
  print(arr_2d.size)  # Output: 4
  ```

---

## 3. Essential Array Operations

### Element-Wise Operations
Perform operations on each element:
```python
arr = np.array([1, 2, 3])
print(arr + 2)  # Output: [3 4 5]
print(arr * 2)  # Output: [2 4 6]
print(np.sqrt(arr))  # Output: [1. 1.41421356 1.73205081]
```

### Broadcasting
Apply operations across arrays of different shapes:
```python
arr_2d = np.array([[1, 2], [3, 4]])
scalar = 2
print(arr_2d * scalar)
# Output:
# [[2 4]
#  [6 8]]
```

### Indexing and Slicing
- **Basic Indexing**:
  ```python
  print(arr[1])  # Output: 2
  print(arr_2d[0, 1])  # Output: 2
  ```
- **Slicing**:
  ```python
  print(arr[1:3])  # Output: [2 3]
  print(arr_2d[:, 1])  # Output: [2 4]
  ```

### Boolean Indexing
Filter arrays based on conditions:
```python
print(arr[arr > 1])  # Output: [2 3]
```

---

## 4. Array Manipulation

### Reshaping
Change array shape:
```python
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print(reshaped)
# Output:
# [[1 2 3]
#  [4 5 6]]
```

### Flattening
Convert to 1D array:
```python
flat = reshaped.flatten()
print(flat)  # Output: [1 2 3 4 5 6]
```

### Concatenation and Stacking
- **Concatenate**:
  ```python
  arr1 = np.array([1, 2])
  arr2 = np.array([3, 4])
  concat = np.concatenate((arr1, arr2))
  print(concat)  # Output: [1 2 3 4]
  ```
- **Stack (Vertical/Horizontal)**:
  ```python
  arr1 = np.array([[1, 2], [3, 4]])
  arr2 = np.array([[5, 6], [7, 8]])
  vstack = np.vstack((arr1, arr2))  # Vertical stack
  hstack = np.hstack((arr1, arr2))  # Horizontal stack
  ```

### Splitting
Split arrays:
```python
arr = np.array([1, 2, 3, 4, 5, 6])
split = np.split(arr, 3)
print(split)  # Output: [array([1, 2]), array([3, 4]), array([5, 6])]
```

---

## 5. Mathematical and Statistical Functions

### Basic Operations
```python
arr = np.array([1, 2, 3])
print(np.sum(arr))  # Output: 6
print(np.mean(arr))  # Output: 2.0
print(np.std(arr))  # Output: 0.816496580927726
print(np.min(arr), np.max(arr))  # Output: 1 3
```

### Linear Algebra
- **Dot Product**:
  ```python
  arr1 = np.array([1, 2])
  arr2 = np.array([3, 4])
  print(np.dot(arr1, arr2))  # Output: 11 (1*3 + 2*4)
  ```
- **Matrix Multiplication**:
  ```python
  mat1 = np.array([[1, 2], [3, 4]])
  mat2 = np.array([[5, 6], [7, 8]])
  print(np.matmul(mat1, mat2))
  # Output:
  # [[19 22]
  #  [43 50]]
  ```
- **Inverse**:
  ```python
  print(np.linalg.inv(mat1))
  ```

### Random Number Generation
Generate random data:
```python
np.random.seed(42)  # For reproducibility
random_arr = np.random.rand(2, 3)  # 2x3 array of random floats (0 to 1)
print(random_arr)
randint = np.random.randint(0, 10, 5)  # 5 random integers
print(randint)  # Output: [6 3 7 4 6]
```

---

## 6. Advanced NumPy Features

### Fancy Indexing
Use arrays as indices:
```python
arr = np.array([10, 20, 30, 40])
indices = [0, 2]
print(arr[indices])  # Output: [10 30]
```

### Masked Arrays
Handle missing or invalid data:
```python
import numpy.ma as ma
arr = np.array([1, -1, 3, -999])
masked_arr = ma.masked_array(arr, mask=[0, 0, 0, 1])  # Mask -999
print(masked_arr)  # Output: [1 -1 3 --]
```

### Broadcasting Rules
Operate on arrays of different shapes if compatible:
```python
arr = np.array([[1, 2], [3, 4]])
row = np.array([10, 20])
print(arr + row)  # Adds row to each row of arr
# Output:
# [[11 22]
#  [13 24]]
```

### Saving and Loading
- **Save**:
  ```python
  np.save('array.npy', arr)
  ```
- **Load**:
  ```python
  loaded_arr = np.load('array.npy')
  ```

---

## 7. Useful NumPy Methods

### Array Creation
- `np.full((2, 3), 5)`: Create array filled with a specific value.
- `np.random.choice([1, 2, 3], size=5)`: Random sampling.
- `np.diag([1, 2, 3])`: Diagonal matrix.

### Array Manipulation
- `np.ravel(arr)`: Flatten array (similar to `flatten` but may return a view).
- `np.transpose(arr)` or `arr.T`: Transpose array.
- `np.expand_dims(arr, axis=0)`: Add dimension.
- `np.squeeze(arr)`: Remove single-dimensional entries.

### Mathematical Functions
- `np.where(arr > 2, arr, 0)`: Conditional replacement.
  ```python
  arr = np.array([1, 2, 3, 4])
  print(np.where(arr > 2, arr, 0))  # Output: [0 0 3 4]
  ```
- `np.clip(arr, 2, 4)`: Limit values to a range.
- `np.cumsum(arr)`: Cumulative sum.
- `np.unique(arr)`: Unique elements.

### Statistical Functions
- `np.median(arr)`: Median of array.
- `np.percentile(arr, 50)`: 50th percentile.
- `np.corrcoef(arr1, arr2)`: Correlation coefficient.

### Linear Algebra
- `np.linalg.norm(arr)`: Compute norm.
- `np.linalg.eig(mat)`: Eigenvalues and eigenvectors.
- `np.linalg.svd(mat)`: Singular value decomposition.

---

## 8. NumPy Tricks and Tips

### 1. **Vectorize Operations**
Avoid loops for better performance:
```python
# Bad
result = []
for i in range(len(arr)):
    result.append(arr[i] * 2)
# Good
result = arr * 2
```

### 2. **Memory Optimization**
Use appropriate data types:
```python
arr = np.array([1, 2, 3], dtype=np.int8)  # Use 8-bit integers
print(arr.nbytes)  # Output: 3 (bytes)
```

### 3. **Boolean Operations**
Combine conditions efficiently:
```python
mask = (arr > 1) & (arr < 3)
print(arr[mask])  # Output: [2]
```

### 4. **Efficient Indexing**
Use `np.take` for advanced indexing:
```python
indices = [0, 2]
print(np.take(arr, indices))  # Output: [1 3]
```

### 5. **Random Sampling**
Sample without replacement:
```python
sample = np.random.choice(arr, size=2, replace=False)
```

### 6. **Array Comparison**
Check equality or closeness:
```python
arr1 = np.array([1, 2])
arr2 = np.array([1, 2.00000001])
print(np.allclose(arr1, arr2, atol=1e-8))  # Output: True
```

### 7. **Conditional Assignment**
Use `np.select` for complex conditions:
```python
conditions = [arr < 2, arr >= 2]
choices = [0, 1]
result = np.select(conditions, choices, default=-1)
print(result)  # Output: [0 1 1]
```

### 8. **Efficient Matrix Operations**
Use `@` for matrix multiplication:
```python
result = mat1 @ mat2  # Same as np.matmul
```

### 9. **Debugging Shapes**
Print shapes during development:
```python
def debug_shape(arr):
    print(f"Shape: {arr.shape}")
    return arr
debug_shape(arr_2d)
```

### 10. **Handle Large Arrays**
Use memory-mapped arrays for large datasets:
```python
mmap_arr = np.memmap('large_array.dat', dtype='float32', mode='w+', shape=(1000, 1000))
```

---

## 9. NumPy with Visualization
Integrate with Matplotlib for plotting:
```python
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Wave")
plt.show()
```

---

## 10. Best Practices

- **Use Vectorized Operations**: Avoid loops for efficiency.
- **Specify Data Types**: Use `dtype` to optimize memory (e.g., `int8`, `float32`).
- **Avoid Copies**: Use views (`arr[:2]`) instead of copies where possible.
- **Check Shapes**: Ensure array shapes align for operations.
- **Leverage Documentation**: Refer to [NumPy Docs](https://numpy.org/doc/stable/) for details.

---

## 11. Troubleshooting & Tips

### Common Issues
- **Shape Mismatch**:
  ```python
  arr1 = np.array([1, 2])
  arr2 = np.array([3, 4, 5])  # Incompatible shapes
  # Fix: Reshape or broadcast
  arr2 = arr2[:2]
  print(arr1 + arr2)
  ```
- **Memory Errors**: Use `np.memmap` or chunk processing for large arrays.
- **Data Type Issues**: Check `dtype` with `arr.dtype`.

### Performance Tips
- **Use `np.where` for Conditionals**:
  ```python
  result = np.where(arr > 2, arr, 0)
  ```
- **Avoid Unnecessary Copies**:
  ```python
  view = arr[:2]  # View, not copy
  copy = arr.copy()  # Explicit copy
  ```
- **Parallelize with NumPy**: Use `numexpr` or `joblib` for large computations.

---

## 12. Resources & Further Learning

- **Official Documentation**: [NumPy Docs](https://numpy.org/doc/stable/)
- **Tutorials**: [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html), [Kaggle NumPy](https://www.kaggle.com/learn/python)
- **Books**: "Python for Data Analysis" by Wes McKinney
- **Community**: [Stack Overflow](https://stackoverflow.com/questions/tagged/numpy), [NumPy GitHub](https://github.com/numpy/numpy)

---