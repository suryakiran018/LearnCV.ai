# Scikit-Learn Guide

**Scikit-Learn**, a powerful Python library for machine learning. Built on NumPy, SciPy, and Matplotlib, Scikit-Learn offers tools for data preprocessing, supervised and unsupervised learning, model evaluation, and more, making it a cornerstone for data science and machine learning tasks.

---

## 1. Introduction to Scikit-Learn

### What is Scikit-Learn?
Scikit-Learn is an open-source machine learning library in Python that provides simple and efficient tools for data mining, data analysis, and machine learning. It supports tasks like classification, regression, clustering, dimensionality reduction, and model selection.

### Why Use Scikit-Learn?
- **Ease of Use**: Consistent API with intuitive interfaces.
- **Comprehensive**: Covers a wide range of machine learning algorithms.
- **Integration**: Works seamlessly with NumPy, Pandas, and Matplotlib/Seaborn.
- **Community**: Extensive documentation and active support.

### Installing Scikit-Learn
Install using pip:
```bash
pip install scikit-learn
```

### Importing Scikit-Learn
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, mean_squared_error
```

---

## 2. Scikit-Learn Workflow

The typical machine learning workflow in Scikit-Learn includes:
1. **Data Preparation**: Load and preprocess data (e.g., handle missing values, scale features).
2. **Model Selection**: Choose an appropriate algorithm (e.g., regression, classification).
3. **Training**: Fit the model to training data.
4. **Evaluation**: Assess model performance using metrics.
5. **Prediction**: Use the model for predictions.
6. **Tuning**: Optimize hyperparameters using cross-validation or grid search.

### Example: Basic Workflow (Regression)
```python
# Load data
df = pd.DataFrame({
    'square_feet': [1500, 2000, 2500, 3000],
    'price': [300000, 400000, 500000, 600000]
})

# Prepare data
X = df[['square_feet']]
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")

# Visualize
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, model.predict(X), color='red', label='Fit')
plt.xlabel('Square Feet')
plt.ylabel('Price')
plt.legend()
plt.title('Linear Regression')
plt.show()
```

---

## 3. Core Scikit-Learn Modules

### 3.1. Data Preprocessing (`sklearn.preprocessing`)
Prepare data for modeling.

- **Standardization**:
  ```python
  scaler = StandardScaler()
  X_scaled = scaler.fit_transform(X)
  ```

- **Encoding Categorical Variables**:
  ```python
  from sklearn.preprocessing import LabelEncoder, OneHotEncoder
  encoder = LabelEncoder()
  df['category'] = encoder.fit_transform(df['category'])
  ```

- **Handling Missing Values**:
  ```python
  from sklearn.impute import SimpleImputer
  imputer = SimpleImputer(strategy='mean')
  X_imputed = imputer.fit_transform(X)
  ```

### 3.2. Supervised Learning
- **Linear Regression**:
  ```python
  model = LinearRegression()
  model.fit(X_train, y_train)
  print(model.coef_, model.intercept_)
  ```

- **Logistic Regression**:
  ```python
  model = LogisticRegression()
  model.fit(X_train, y_train)
  y_pred = model.predict(X_test)
  print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
  ```

- **Support Vector Machines (SVM)**:
  ```python
  from sklearn.svm import SVC
  model = SVC(kernel='rbf')
  model.fit(X_train, y_train)
  ```

- **Decision Trees**:
  ```python
  from sklearn.tree import DecisionTreeClassifier
  model = DecisionTreeClassifier(max_depth=3)
  model.fit(X_train, y_train)
  ```

### 3.3. Unsupervised Learning
- **K-Means Clustering**:
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=3, random_state=42)
  df['cluster'] = kmeans.fit_predict(X)
  sns.scatterplot(data=df, x='feature1', y='feature2', hue='cluster')
  plt.title('K-Means Clustering')
  plt.show()
  ```

- **Principal Component Analysis (PCA)**:
  ```python
  from sklearn.decomposition import PCA
  pca = PCA(n_components=2)
  X_pca = pca.fit_transform(X)
  print(pca.explained_variance_ratio_)
  ```

### 3.4. Model Selection and Evaluation
- **Train-Test Split**:
  ```python
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  ```

- **Cross-Validation**:
  ```python
  from sklearn.model_selection import cross_val_score
  scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
  print(f"Cross-Validation Scores: {scores.mean():.2f} ± {scores.std():.2f}")
  ```

- **Grid Search**:
  ```python
  from sklearn.model_selection import GridSearchCV
  param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
  grid = GridSearchCV(SVC(), param_grid, cv=5)
  grid.fit(X_train, y_train)
  print(grid.best_params_)
  ```

### 3.5. Metrics
Evaluate model performance:
- **Regression**:
  ```python
  from sklearn.metrics import mean_squared_error, r2_score
  print(f"R² Score: {r2_score(y_test, y_pred):.2f}")
  ```

- **Classification**:
  ```python
  from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
  print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.2f}")
  print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
  ```

---

## 4. Integration with Pandas and Visualization
Combine Scikit-Learn with Pandas and Seaborn/Matplotlib for data science tasks.

### Example: Classification with Visualization
```python
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Train classifier
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(multi_class='ovr')
model.fit(X_train, y_train)

# Visualize decision boundaries (2 features for simplicity)
X_subset = X[['sepal length (cm)', 'sepal width (cm)']]
model.fit(X_subset, y)
x_min, x_max = X_subset.iloc[:, 0].min() - 1, X_subset.iloc[:, 0].max() + 1
y_min, y_max = X_subset.iloc[:, 1].min() - 1, X_subset.iloc[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1), np.arange(y_min, y_max, 0.1))
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4, cmap='viridis')
sns.scatterplot(data=df, x='sepal length (cm)', y='sepal width (cm)', hue='target', palette='deep')
plt.title('Logistic Regression Decision Boundaries')
plt.show()
```

---

## 5. Useful Scikit-Learn Methods

### Preprocessing
- `StandardScaler().fit_transform(X)`: Scale features to zero mean and unit variance.
- `SimpleImputer(strategy='mean')`: Impute missing values.
- `LabelEncoder().fit_transform(y)`: Encode categorical labels.
- `OneHotEncoder(sparse=False)`: One-hot encode categorical features.

### Supervised Learning
- `LinearRegression().fit(X, y)`: Linear regression.
- `LogisticRegression().fit(X, y)`: Logistic regression for classification.
- `RandomForestClassifier(n_estimators=100)`: Random forest for classification.
- `GradientBoostingClassifier()`: Gradient boosting for classification.

### Unsupervised Learning
- `KMeans(n_clusters=3)`: K-means clustering.
- `PCA(n_components=2)`: Principal component analysis.
- `DBSCAN(eps=0.5, min_samples=5)`: Density-based clustering.

### Model Selection
- `train_test_split(X, y, test_size=0.2)`: Split data into train/test sets.
- `cross_val_score(model, X, y, cv=5)`: Perform k-fold cross-validation.
- `GridSearchCV(model, param_grid)`: Hyperparameter tuning.

### Metrics
- `accuracy_score(y_true, y_pred)`: Classification accuracy.
- `mean_squared_error(y_true, y_pred)`: Regression error.
- `confusion_matrix(y_true, y_pred)`: Confusion matrix for classification.
- `classification_report(y_true, y_pred)`: Detailed classification metrics.

---

## 6. Scikit-Learn Tricks and Tips

### 1. **Pipeline for Streamlined Workflow**
Combine preprocessing and modeling:
```python
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
```

### 2. **Feature Selection**
Select important features:
```python
from sklearn.feature_selection import SelectKBest, f_regression
selector = SelectKBest(score_func=f_regression, k=2)
X_selected = selector.fit_transform(X, y)
```

### 3. **Handle Imbalanced Data**
Use oversampling or class weights:
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(class_weight='balanced')
model.fit(X_train, y_train)
```

### 4. **Parallel Processing**
Speed up grid search:
```python
grid = GridSearchCV(SVC(), param_grid, cv=5, n_jobs=-1)  # Use all CPU cores
grid.fit(X_train, y_train)
```

### 5. **Save and Load Models**
Persist models using `joblib`:
```python
from joblib import dump, load
dump(model, 'model.joblib')
loaded_model = load('model.joblib')
```

### 6. **Feature Importance**
Inspect model feature importance:
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
importances = pd.Series(model.feature_importances_, index=X.columns)
sns.barplot(x=importances, y=importances.index)
plt.title('Feature Importance')
plt.show()
```

### 7. **Cross-Validation with Custom Scoring**
Define custom metrics:
```python
from sklearn.metrics import make_scorer
custom_scorer = make_scorer(mean_squared_error, greater_is_better=False)
scores = cross_val_score(model, X, y, cv=5, scoring=custom_scorer)
```

### 8. **Handle Large Datasets**
Use incremental learning for large data:
```python
from sklearn.linear_model import SGDClassifier
model = SGDClassifier()
for X_chunk, y_chunk in data_generator:  # Assume data_generator yields chunks
    model.partial_fit(X_chunk, y_chunk, classes=np.unique(y))
```

### 9. **Visualize Learning Curves**
Diagnose bias/variance:
```python
from sklearn.model_selection import learning_curve
train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=5)
plt.plot(train_sizes, train_scores.mean(axis=1), label='Train')
plt.plot(train_sizes, test_scores.mean(axis=1), label='Test')
plt.legend()
plt.title('Learning Curves')
plt.show()
```

### 10. **Combine with Seaborn**
Visualize predictions:
```python
df['predicted'] = model.predict(X)
sns.scatterplot(data=df, x='feature1', y='feature2', hue='predicted', style='target')
plt.title('Actual vs Predicted')
plt.show()
```

---

## 7. Best Practices

- **Preprocess Consistently**: Apply the same preprocessing to train and test sets using pipelines.
- **Validate Models**: Use cross-validation to avoid overfitting.
- **Tune Hyperparameters**: Leverage `GridSearchCV` or `RandomizedSearchCV`.
- **Handle Missing Data**: Impute or remove missing values before modeling.
- **Document Experiments**: Track model performance and parameters in notebooks.

---

## 8. Troubleshooting & Tips

### Common Issues
- **Missing Data**:
  ```python
  X = SimpleImputer(strategy='mean').fit_transform(X)
  ```
- **Overfitting**: Regularize models or reduce complexity:
  ```python
  model = LogisticRegression(C=0.1)  # Lower C for stronger regularization
  ```
- **Shape Mismatch**:
  ```python
  print(X.shape, y.shape)  # Debug shapes before fitting
  ```

### Performance Tips
- **Use Pipelines**: Ensure consistent preprocessing and avoid data leakage.
- **Sparse Matrices**: Use `scipy.sparse` for high-dimensional data.
- **Parallelize**: Set `n_jobs=-1` for parallel processing in grid search or cross-validation.
- **Optimize Data Types**: Use `float32` instead of `float64` for large datasets:
  ```python
  X = X.astype(np.float32)
  ```

---

## 9. Resources & Further Learning

- **Official Documentation**: [Scikit-Learn Docs](https://scikit-learn.org/stable/)
- **Tutorials**: [Scikit-Learn Tutorials](https://scikit-learn.org/stable/tutorial/index.html), [Kaggle Machine Learning](https://www.kaggle.com/learn/machine-learning)
- **Books**: "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" by Aurélien Géron
- **Community**: [Stack Overflow](https://stackoverflow.com/questions/tagged/scikit-learn), [Scikit-Learn GitHub](https://github.com/scikit-learn/scikit-learn)

---