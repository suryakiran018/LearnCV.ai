## 1. Introduction to NumPy

### What is NumPy?
NumPy (**Numerical Python**) is a library for working with arrays and performing mathematical operations efficiently. 

- It provides support for multi-dimensional arrays, along with a collection of functions for **linear algebra, statistics, and more**.

### Installation
Install NumPy using pip:
```bash
pip install numpy
```

Import NumPy in Python:
```python
import numpy as np
```

---

## 2. NumPy Arrays

### Creating Arrays
NumPy's core object is the `ndarray`. Create arrays using various methods:
```python
# From a list
arr = np.array([1, 2, 3, 4])
print(arr)  # Output: [1 2 3 4]

# 2D array
arr_2d = np.array([[1, 2], [3, 4]])
print(arr_2d)
# Output:
# [[1 2]
#  [3 4]]

# Zeros, ones, or empty arrays
zeros = np.zeros((2, 3))  # 2x3 array of zeros
ones = np.ones((2, 3))    # 2x3 array of ones
empty = np.empty((2, 3))  # 2x3 uninitialized array

# Range of values
arange = np.arange(0, 10, 2)  # Output: [0 2 4 6 8]
linspace = np.linspace(0, 1, 5)  # Output: [0.   0.25 0.5  0.75 1.  ]
```

### Array Attributes
Inspect array properties:
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)    # Output: (2, 3)
print(arr.ndim)     # Output: 2
print(arr.size)     # Output: 6
print(arr.dtype)    # Output: int64
```

---

## 3. Array Indexing and Slicing

### Indexing
Access elements using indices:
```python
arr = np.array([10, 20, 30, 40])
print(arr[0])  # Output: 10

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d[1, 2])  # Output: 6
```

### Slicing
Extract subarrays:
```python
arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])  # Output: [20 30 40]

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[0:2, 1:3])
# Output:
# [[2 3]
#  [5 6]]
```

### Boolean Indexing
Filter arrays based on conditions:
```python
arr = np.array([1, 2, 3, 4, 5])
print(arr[arr > 3])  # Output: [4 5]
```

---

## 4. Array Operations

### Element-wise Operations
Perform operations on each element:
```python
arr = np.array([1, 2, 3])
print(arr + 2)      # Output: [3 4 5]
print(arr * 2)      # Output: [2 4 6]
print(np.sqrt(arr)) # Output: [1.         1.41421356 1.73205081]
```

### Broadcasting
Apply operations across arrays of different shapes:
```python
arr = np.array([[1, 2], [3, 4]])
scalar = 10
print(arr + scalar)
# Output:
# [[11 12]
#  [13 14]]
```

### Matrix Operations
Perform matrix multiplication and other operations:
```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))  # Matrix multiplication
# Output:
# [[19 22]
#  [43 50]]

print(a.T)  # Transpose
# Output:
# [[1 3]
#  [2 4]]
```

---

## 5. Mathematical and Statistical Functions

### Universal Functions (ufuncs)
Apply mathematical functions element-wise:
```python
arr = np.array([0, np.pi/2, np.pi])
print(np.sin(arr))  # Output: [0. 1. 0.]
```

### Statistical Functions
Compute statistics:
```python
arr = np.array([1, 2, 3, 4, 5])
print(np.mean(arr))   # Output: 3.0
print(np.std(arr))    # Output: 1.4142135623730951
print(np.min(arr))    # Output: 1
print(np.max(arr))    # Output: 5
print(np.sum(arr))    # Output: 15
```

---

## 6. Reshaping and Manipulating Arrays

### Reshaping
Change the shape of an array:
```python
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print(reshaped)
# Output:
# [[1 2 3]
#  [4 5 6]]
```

### Flattening
Convert multi-dimensional arrays to 1D:
```python
arr_2d = np.array([[1, 2], [3, 4]])
flattened = arr_2d.flatten()
print(flattened)  # Output: [1 2 3 4]
```

### Concatenation
Combine arrays:
```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.concatenate((a, b), axis=0))  # Vertical stacking
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
```

---

## 7. Advanced NumPy Features

### Random Number Generation
Generate random numbers:
```python
# Random integers
rand_ints = np.random.randint(1, 10, size=(2, 3))
print(rand_ints)
# Example Output:
# [[4 7 2]
#  [9 1 5]]

# Random floats
rand_floats = np.random.random((2, 3))
print(rand_floats)
# Example Output:
# [[0.12345678 0.87654321 0.45678912]
#  [0.78912345 0.23456789 0.67890123]]
```

### Linear Algebra
Solve linear equations, compute eigenvalues, etc.:
```python
a = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
solution = np.linalg.solve(a, b)  # Solve ax = b
print(solution)  # Output: [-4.   4.5]
```

### Saving and Loading Arrays
Save arrays to disk and load them:
```python
arr = np.array([1, 2, 3])
np.save('array.npy', arr)
loaded_arr = np.load('array.npy')
print(loaded_arr)  # Output: [1 2 3]
```

---

## 8. Performance Tips

### Vectorization
Use NumPy's vectorized operations instead of loops:
```python
# Slow: Using a loop
arr = np.array([1, 2, 3, 4])
result = np.zeros(4)
for i in range(len(arr)):
    result[i] = arr[i] * 2

# Fast: Vectorized
result = arr * 2
```

### Memory Efficiency
Use appropriate data types to save memory:
```python
arr = np.array([1, 2, 3], dtype=np.int8)  # Use 8-bit integers
```

---

## 9. Practical Workflows

### Data Preprocessing

Normalize data (e.g., scale to [0, 1]):
```python
data = np.array([10, 20, 30, 40, 50])
normalized = (data - np.min(data)) / (np.max(data) - np.min(data))
print(normalized)  # Output: [0. 0.25 0.5 0.75 1.]integers
```

### Handling Missing Data

Replace NaN values:
```python
arr = np.array([1, np.nan, 3, 4])
arr[np.isnan(arr)] = 0
print(arr)  # Output: [1. 0. 3. 4.]
```

### Working with Large Datasets

Use `np.memmap` for memory-efficient handling of large arrays:
```python
arr = np.memmap('large_array.dat', dtype='float32', mode='w+', shape=(10000, 10000))
arr[:] = np.random.rand(10000, 10000)  # Fill with random data
```

---

## 10. Best Practices

- **Use Descriptive Variable Names**: E.g., `matrix_a` instead of `a`.
- **Check Array Shapes**: Ensure compatibility before operations.
- **Leverage Broadcasting**: Avoid unnecessary loops.
- **Document Code**: Add comments for complex operations.
- **Test Edge Cases**: Handle empty arrays or invalid inputs.

---

## 11. Troubleshooting & Common Issues

### Shape Mismatch
Ensure arrays have compatible shapes for operations:
```python
a = np.array([[1, 2], [3, 4]])
b = np.array([1, 2])
# This will work due to broadcasting
print(a + b)
```

### Data Type Issues
Check `dtype` to avoid precision errors:
```python
arr = np.array([1.5, 2.7], dtype=np.int32)  # Loses decimal precision
print(arr)  # Output: [1 2]
```
---

## 12. NumPy Useful Functions (With Use-Cases)

### Array Creation & Initialization

| Function                             | Use                                  |
| ------------------------------------ | ------------------------------------ |
| `np.array()`                         | Convert list or tuple to NumPy array |
| `np.zeros(shape)`                    | Create array filled with 0s          |
| `np.ones(shape)`                     | Create array filled with 1s          |
| `np.full(shape, value)`              | Array with a constant value          |
| `np.eye(n)`                          | Identity matrix                      |
| `np.arange(start, stop, step)`       | Range of numbers                     |
| `np.linspace(start, stop, num)`      | Evenly spaced values                 |
| `np.random.rand()`                   | Random floats (0–1)                  |
| `np.random.randint(low, high, size)` | Random integers                      |
| `np.empty(shape)`                    | Create an uninitialized array        |

### Array Info & Shape Manipulation

| Function                         | Use                         |
| -------------------------------- | --------------------------- |
| `arr.shape`                      | Get shape of array          |
| `arr.reshape(new_shape)`         | Change shape                |
| `arr.flatten()`                  | Flatten to 1D               |
| `arr.ravel()`                    | Flatten (faster view)       |
| `arr.transpose()` or `arr.T`     | Transpose dimensions        |
| `np.expand_dims(arr, axis)`      | Add a dimension             |
| `np.squeeze(arr)`                | Remove single dimensions    |
| `np.resize(arr, new_shape)`      | Resize (can repeat values)  |
| `np.concatenate([a, b], axis=0)` | Join arrays                 |
| `np.stack([a, b], axis=0)`       | Stack arrays along new axis |

### Math, Logic, Image-Friendly Ops

| Function                            | Use                                      |
| ----------------------------------- | ---------------------------------------- |
| `np.clip(arr, min, max)`            | Limit values (good for brightness edits) |
| `np.where(condition, x, y)`         | Conditional selection                    |
| `np.mean(arr)`                      | Average value                            |
| `np.sum(arr)`                       | Total sum                                |
| `np.min(arr)` / `np.max(arr)`       | Min / max values                         |
| `np.std(arr)`                       | Standard deviation                       |
| `np.argmin(arr)` / `np.argmax(arr)` | Index of min/max                         |
| `np.unique(arr)`                    | Unique values (e.g., in masks)           |
| `np.isnan(arr)` / `np.isinf(arr)`   | Check for NaNs / Infs                    |
| `np.dot(a, b)`                      | Dot product (used in CNNs, ML)           |

### Bonus Tips for CV Projects

| Use Case            | NumPy Tricks                            |
| ------------------- | --------------------------------------- |
| **Grayscale image** | `img_gray = np.mean(img, axis=2)`       |
| **Invert image**    | `img_inv = 255 - img`                   |
| **Thresholding**    | `img_bin = np.where(img > 128, 255, 0)` |
| **ROI cropping**    | `roi = img[100:200, 150:250]`           |
| **Image masking**   | `img[mask == 0] = 0`                    |

---

## 13. Resources & Further Learning

- **Official Documentation**: [NumPy Docs](https://numpy.org/doc/stable/)
- **Tutorials**: [Scientific Python Lectures](https://scipy-lectures.org/)
- **Books**: "Python for Data Analysis" by Wes McKinney

---