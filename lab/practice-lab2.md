# 🧪 Practice Lab – 2: NumPy & ML Model Design

## 🎯 **Objective:**
Practice building and testing basic machine learning algorithms **from scratch** using only **NumPy** (no TensorFlow/PyTorch for model internals). Also practice clean coding with **OOP** (Object-Oriented Programming).

---

## 💻 Lab Problems (Choose one)

### **Easy Level**

1. **Linear Regression** – do both:

   * Closed-form solution (normal equation)
   * Gradient Descent (add Ridge regularization)
2. **Data Split & Evaluation** – create functions to:

   * Split data into train/validation/test sets
   * Apply scaling
   * Calculate metrics (MSE, MAE, R²)

---

### **Medium Level**

1. **Logistic Regression (Binary)**:

   * L2 regularization
   * Stable math using log-sum-exp
   * SGD or mini-batch gradient descent
2. **K-Nearest Neighbours (KNN)**:

   * Different distance metrics
   * Weighted voting
3. **Small Feed-Forward Neural Network**:

   * 1–3 hidden layers
   * Activation functions (ReLU, Sigmoid, Tanh)
   * Batch normalization option

---

### **Hard Level**

1. **CNN Basics**:

   * Implement conv2d and maxpool functions
   * Train a small CNN on part of MNIST
2. **Simple Autoencoder**:

   * Reduce dimensions
   * Show reconstruction quality
3. **Optimization Algorithms**:

   * Implement and compare: SGD, Momentum, RMSProp, Adam
   * Show and analyze convergence plots

---

## [An Engineer’s Trek into Machine Learning](https://www.ml4devs.com/en/articles/machine-learning-intro-for-developers/)

<img src="https://www.ml4devs.com/images/illustrations/ml-intro-types-of-models.webp" alt="ML-models"/>

[source](https://www.ml4devs.com)

---

## 🛠️ Lab Instructions

1. **Pick one** problem from above.
2. Plan your code before starting — draw a small diagram of your components:

   * Example: DataLoader → Model → Optimizer → Trainer → Metrics
3. Write **Python + NumPy** code (vectorized, avoid loops over each sample).
4. You can use `matplotlib` for plots, and `scikit-learn` only for:

   * Loading datasets
   * Checking results (not for internal model work)
5. Create **unit tests** to check:

   * Correct shapes
   * Gradients (numeric check)
   * Loss decreases during training
6. Write a **short report** (2–4 pages, PDF):

   * Problem statement
   * Design choices
   * Algorithms used
   * Experiments + plots
   * Key results and conclusions
7. Submit your **code + tests + report** in a ZIP or GitHub repo.

---

## 📂 Suggested Project Structure

```
README.md          # Instructions to run
dataset/           # dataset files (.csv / .png / .xsl)
results/           # experimentation results 
src/               # Code files
  |_model.py
  |_train.py
  |_utils.py
  |_dataloader.py
  |_main.py
  |_eval.py
  |_test.py
tests/             # Unit tests
report.pdf         # Your short write-up
```

---

## 📊 Example: Linear Regression

**Components:**

* DataLoader → loads dataset
* LinearModel → predict, loss, gradient
* Optimizer → SGD with learning rate
* Trainer → training loop, early stopping

**Tests:**

* Shapes match
* Loss decreases each epoch
* Gradient error < 1e-5

---

## 🏆 Marks Distribution (Total 35)

| Criteria                 | Marks  |
| ------------------------ | ------ |
| Understanding problem    | 5      |
| Correct, vectorized code | 10     |
| Modular design, OOP      | 7      |
| Experiments & analysis   | 6      |
| Tests & reproducibility  | 4      |
| Report clarity           | 3      |
| **Total**                | **35** |

---

## 🙏 **Credits / Acknowledgements**

We acknowledge the use of open-source educational content and inspiration from the following sources:


* **NumPy Documentation** – [https://numpy.org/doc/](https://numpy.org/doc/)
* **Matplotlib Documentation** – [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
* **Python Data Science Handbook** by Jake VanderPlas (O’Reilly, open-access version available online)
* **scikit-learn Documentation** – [https://scikit-learn.org/](https://scikit-learn.org/)
* **An Engineer’s Trek into Machine Learning** – [www.ml4devs.com](https://www.ml4devs.com/en/articles/machine-learning-intro-for-developers/)
* **CS231n: Convolutional Neural Networks for Visual Recognition** – [http://cs231n.stanford.edu/](http://cs231n.stanford.edu/)
* **Dive into Deep Learning (D2L.ai)** – [https://d2l.ai/](https://d2l.ai/)
* **Machine Learning Mastery – Code Algorithm from Scratch** – [https://machinelearningmastery.com/](https://machinelearningmastery.com/start-here/#code_algorithms)

---

> This lab is intended solely for **academic and practice purposes**.

> Full credit goes to the original authors and maintainers for their contribution to the open-source and data science education community.

---