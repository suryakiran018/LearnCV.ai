# Data Science Guide

**Data Science**, a multidisciplinary field that uses scientific methods, algorithms, and systems to extract insights from structured and unstructured data. 

It covers foundational concepts, tools, techniques, and workflows, with clear explanations, examples, and code snippets, suitable for beginners and advanced practitioners.

---

## 1. Introduction to Data Science

### What is Data Science?
Data Science combines `statistics`, `computer science`, and `domain expertise` to analyze data, uncover patterns, and make data-driven decisions. It is used in industries like finance, healthcare, marketing, and more.

### Why Data Science?
- **Insights**: Turns raw data into actionable knowledge.
- **Automation**: Powers predictive models and machine learning.
- **Versatility**: Applicable across domains, from business to science.

### Key Skills
- Programming (Python, R)
- Statistics and Mathematics
- Data Wrangling and Visualization
- Machine Learning and Deep Learning
- Domain Knowledge

---

## 2. Foundations

### Programming
Python is the most popular language for data science due to its rich ecosystem.
- **Install Python**: Use Anaconda or pip.
  ```bash
  pip install numpy pandas matplotlib seaborn scikit-learn
  ```
- **Basic Python**:
  ```python
  # Lists and loops
  data = [1, 2, 3, 4]
  squared = [x**2 for x in data]
  print(squared)  # Output: [1, 4, 9, 16]
  ```

### Mathematics and Statistics
- **Linear Algebra**: Vectors, matrices (used in machine learning).
  ```python
  import numpy as np
  matrix = np.array([[1, 2], [3, 4]])
  inverse = np.linalg.inv(matrix)
  print(inverse)
  ```
- **Statistics**: Mean, median, standard deviation, hypothesis testing.
  ```python
  from scipy import stats
  data = np.array([1, 2, 3, 4, 5])
  print(np.mean(data), np.std(data))  # Output: 3.0 1.4142135623730951
  ```

### Data Science Workflow
1. **Problem Definition**: Define objectives (e.g., predict sales).
2. **Data Collection**: Gather data from databases, APIs, or files.
3. **Data Cleaning**: Handle missing values, outliers.
4. **Exploratory Data Analysis (EDA)**: Visualize and summarize data.
5. **Modeling**: Build and evaluate models.
6. **Deployment**: Integrate models into production.

---

## 3. Data Manipulation and Analysis

### Pandas
Pandas is used for data manipulation and analysis.
- Load and explore a CSV:
  ```python
  import pandas as pd
  df = pd.read_csv('data.csv')
  print(df.head())  # Display first 5 rows
  ```
- Handle missing values:
  ```python
  df.fillna(df.mean(), inplace=True)  # Fill missing with mean
  ```
- Group and aggregate:
  ```python
  grouped = df.groupby('category').mean()
  print(grouped)
  ```

### NumPy
NumPy supports numerical operations on arrays.
- Create and manipulate arrays:
  ```python
  import numpy as np
  arr = np.array([1, 2, 3])
  print(arr * 2)  # Output: [2 4 6]
  ```

---

## 4. Data Visualization

### Matplotlib
Create static plots:
```python
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label='sin(x)')
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.show()
```

### Seaborn
Build advanced visualizations:
```python
import seaborn as sns
sns.histplot(df['column'], bins=30)
plt.title('Histogram')
plt.show()
```

### Plotly (Interactive)
Create interactive plots:
```python
import plotly.express as px
fig = px.scatter(df, x='column1', y='column2', color='category')
fig.show()
```

---

## 5. Machine Learning with Scikit-Learn

### Supervised Learning
- **Regression** (e.g., Linear Regression):
  ```python
  from sklearn.linear_model import LinearRegression
  from sklearn.model_selection import train_test_split
  X = df[['feature1', 'feature2']]
  y = df['target']
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
  model = LinearRegression()
  model.fit(X_train, y_train)
  print(model.score(X_test, y_test))  # R² score
  ```
- **Classification** (e.g., Logistic Regression):
  ```python
  from sklearn.linear_model import LogisticRegression
  model = LogisticRegression()
  model.fit(X_train, y_train)
  predictions = model.predict(X_test)
  ```

### Unsupervised Learning
- **Clustering** (e.g., K-Means):
  ```python
  from sklearn.cluster import KMeans
  kmeans = KMeans(n_clusters=3)
  clusters = kmeans.fit_predict(X)
  df['cluster'] = clusters
  ```

### Model Evaluation
- Metrics: Accuracy, precision, recall, F1-score.
  ```python
  from sklearn.metrics import accuracy_score
  print(accuracy_score(y_test, predictions))
  ```

---

## 6. Advanced Topics

### Deep Learning
Use **TensorFlow** or **PyTorch** for neural networks.
- Simple neural network with TensorFlow:
  ```python
  import tensorflow as tf
  model = tf.keras.Sequential([
      tf.keras.layers.Dense(64, activation='relu', input_shape=(X.shape[1],)),
      tf.keras.layers.Dense(1)
  ])
  model.compile(optimizer='adam', loss='mse')
  model.fit(X_train, y_train, epochs=10)
  ```

### Feature Engineering
- **Scaling**: Normalize features.
  ```python
  from sklearn.preprocessing import StandardScaler
  scaler = StandardScaler()
  X_scaled = scaler.fit_transform(X)
  ```
- **Encoding**: Convert categorical data.
  ```python
  df['category'] = pd.get_dummies(df['category'])
  ```

### Big Data
- Use **Dask** or **Spark** for large datasets.
  ```python
  import dask.dataframe as dd
  ddf = dd.from_pandas(df, npartitions=4)
  print(ddf.mean().compute())
  ```

---

## 7. Data Science Workflow Example
Build a predictive model for a dataset (e.g., house prices):
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('house_prices.csv')

# Clean data
df = df.dropna()

# Features and target
X = df[['square_feet', 'bedrooms']]
y = df['price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
print(f'R² Score: {model.score(X_test, y_test)}')

# Visualize predictions
plt.scatter(y_test, model.predict(X_test))
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted House Prices')
plt.show()
```

---

## 8. Deployment and Production
Deploy models using **Flask** or **FastAPI**:
```python
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    X = np.array([[data['square_feet'], data['bedrooms']]])
    prediction = model.predict(X)
    return jsonify({'price': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
```

Deploy to platforms like Heroku or AWS:
```bash
pip freeze > requirements.txt
gunicorn app:app
```

---

## 9. Best Practices

- **Clean Data Thoroughly**: Handle missing values, outliers, and duplicates.
- **Document Code**: Use comments and notebooks for clarity.
- **Version Control**: Use Git/GitHub for collaboration.
  ```bash
  git commit -m "Add data cleaning script"
  ```
- **Reproducible Research**: Use Jupyter notebooks or scripts with seeds.
  ```python
  np.random.seed(42)
  ```
- **Automate Pipelines**: Use tools like Airflow for workflows.

---

## 10. Troubleshooting & Tips

### Common Issues
- **Missing Data**: Impute or drop missing values.
  ```python
  df['column'].fillna(df['column'].median(), inplace=True)
  ```
- **Overfitting**: Use regularization (e.g., Ridge, Lasso) or cross-validation.
  ```python
  from sklearn.linear_model import Ridge
  model = Ridge(alpha=1.0)
  ```
- **Memory Issues**: Use Dask or chunked processing for large datasets.

### Performance Tips
- **Optimize Models**: Tune hyperparameters with GridSearchCV.
  ```python
  from sklearn.model_selection import GridSearchCV
  param_grid = {'alpha': [0.1, 1.0, 10.0]}
  grid = GridSearchCV(Ridge(), param_grid)
  grid.fit(X_train, y_train)
  ```
- **Cache Results**: Save processed data to avoid recomputation.
  ```python
  df.to_pickle('processed_data.pkl')
  ```

---

## 11. Learning Path Suggestion
1. **Foundations**: Learn Python, NumPy, Pandas, and basic statistics.
2. **Visualization**: Master Matplotlib, Seaborn, and Plotly.
3. **Machine Learning**: Use Scikit-Learn for supervised and unsupervised learning.
4. **Projects**: Build 3–5 projects (e.g., predict house prices, classify images).
5. **Advanced**: Explore deep learning (TensorFlow) and big data (Dask/Spark).
6. **Deployment**: Deploy models with Flask/FastAPI and host on cloud platforms.

---

## 12. Resources & Further Learning
- **Official Documentation**: [NumPy](https://numpy.org/doc/), [Pandas](https://pandas.pydata.org/docs/), [Scikit-Learn](https://scikit-learn.org/stable/)
- **Tutorials**: [Kaggle Learn](https://www.kaggle.com/learn), [DataCamp](https://www.datacamp.com/)
- **Books**: "Python for Data Analysis" by Wes McKinney, "Hands-On Machine Learning" by Aurélien Géron
- **Community**: [Stack Overflow](https://stackoverflow.com/questions/tagged/data-science), [Kaggle](https://www.kaggle.com/)

---