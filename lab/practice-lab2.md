# Practice Lab - 2: NumPy & ML Model Design (Hands-On)

## 🎯 Objective

Strengthen your numerical programming and model-design skills by building, testing, and documenting core algorithms and small ML models using **NumPy** (no high-level libraries for core algorithms) and clean OOP where appropriate.

---

## 💻 Lab Problems (Choose **one**)

### Easy

* **Linear Regression (closed-form + gradient descent)** from scratch using NumPy. Include regularization (Ridge).
* **Train/test split + evaluation pipeline**: scalers, train/val/test split, and metric functions (MSE, MAE, R²).

### Medium

* Implement **Logistic Regression** (binary) with L2 regularization, numerical stability (log-sum-exp), and SGD / mini-batch.
* **K-Nearest Neighbours** (KD-tree optional) with distance metrics and weighted voting.
* Build a small **feed-forward neural network** (1-3 hidden layers) with ReLU/sigmoid/tanh, forward/backward passes, and options for batch normalization.

### Hard

* Implement **CNN primitives** (conv2d, maxpool) and train a small CNN on a subset of MNIST (vectorized, no deep-learning frameworks).
* Build a **simple autoencoder** for dimensionality reduction and demonstrate reconstruction quality/latent interpolation.
* Implement and compare **optimization algorithms**: SGD, SGD+Momentum, RMSProp, Adam — show convergence plots and analysis.

---

---

## [An Engineer’s Trek into Machine Learning](https://www.ml4devs.com/en/articles/machine-learning-intro-for-developers/)

<img src="https://www.ml4devs.com/images/illustrations/ml-intro-types-of-models.webp" alt="ML-models"/>

[source](https://www.ml4devs.com)

---

## 🛠️ Lab Instructions for Students

1. **Select one problem** from the list and read requirements carefully.
2. Design components before coding. Provide a **class diagram / flow diagram** showing modules (e.g., DataLoader, Model, Optimizer, Trainer, Metrics).
3. Write code in **Python + NumPy**. You may use matplotlib for plots and scikit-learn only for dataset loading/benchmarking (not for model internals).
4. Keep code **vectorized** — avoid Python loops over samples whenever possible.
5. Include a **unit test file** that checks core routines (shapes, gradients via numerical check, loss decreases on toy data).
6. Provide a **short report (PDF)**: problem statement, design decisions, key algorithms, experiments, plots (loss/accuracy), and conclusions.
7. Submit repository or ZIP containing code, tests, and report.

---

## Example: Linear Regression Lab (compact blueprint)

* **Design (UML-like)**:

  * `DataLoader` → loads CSV or sklearn dataset
  * `LinearModel` (implements `predict`, `loss`, `grad`)
  * `Optimizer` (`SGD` with learning rate)
  * `Trainer` (loop, early stopping)
* **Deliverables**:

  * `linear_model.py`, `optimizer.py`, `trainer.py`, `tests/`
  * Report with comparison: closed-form vs gradient descent; effect of learning rate and regularization.
* **Tests**:

  * Shapes check, loss decreases over epochs, gradient numeric check < 1e-5.

---

## Example: Small Feed-Forward NN (tips)

* Implement layers as classes (`Linear`, `ReLU`, `Sigmoid`) with `forward(X)` and `backward(dout)` returning gradients.
* Keep layer parameters in a dict for easy saving/loading.
* Use **Cross-Entropy** with stable softmax.
* Train on a small portion of MNIST or a toy dataset — show learning curves and confusion matrix.

---

## Suggested Deliverable Template (for students)

* `README.md` with run instructions
* `src/` with code modules
* `tests/` with unit tests (use pytest)
* `notebooks/` optional exploratory notebook
* `report.pdf` (2-4 pages): problem, design, results, discussion

---

## ✅ Evaluation Rubric (Total 35)

| Criteria                         | Marks  |
| -------------------------------- | ------ |
| Problem Understanding & Scope    | 5      |
| Code Correctness & Vectorization | 10     |
| Modular Design & OOP Use         | 7      |
| Experiments & Plots (analysis)   | 6      |
| Tests / Reproducibility          | 4      |
| Presentation (report clarity)    | 3      |
| **Total**                        | **35** |

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