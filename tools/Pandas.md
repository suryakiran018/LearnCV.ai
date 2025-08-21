# Pandas Guide

## 1. Introduction to Pandas

### What is Pandas?
Pandas is an open-source library for data manipulation and analysis, providing two primary data structures: **Series** (1D) and **DataFrame** (2D). It excels in handling tabular data, time series, and data cleaning tasks.

### Why Use Pandas?
- **Ease of Use**: Intuitive syntax for data operations.
- **Flexibility**: Handles diverse data formats (CSV, Excel, SQL, JSON).
- **Integration**: Works seamlessly with NumPy, Matplotlib, and Scikit-Learn.

### Installing Pandas
Install Pandas using pip:
```bash
pip install pandas
```

### Importing Pandas
```python
import pandas as pd
import numpy as np
```

---

## 2. Core Data Structures

### Series
A Series is a one-dimensional array-like object with an index.
```python
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)
# Output:
# a    1
# b    2
# c    3
# d    4
# dtype: int64
```

### DataFrame
A DataFrame is a two-dimensional table with rows and columns.
```python
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35], 'city': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
print(df)
# Output:
#       name  age     city
# 0    Alice   25  New York
# 1      Bob   30   London
# 2  Charlie   35    Paris
```

---

## 3. Data Import and Export

### Reading Data
Load data from various formats:
```python
# CSV
df = pd.read_csv('data.csv')

# Excel
df = pd.read_excel('data.xlsx')

# JSON
df = pd.read_json('data.json')

# SQL
import sqlite3
conn = sqlite3.connect('database.db')
df = pd.read_sql_query('SELECT * FROM table_name', conn)
```

### Writing Data
Save DataFrames to files:
```python
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
df.to_json('output.json')
```

---

## 4. Data Exploration

### Basic Inspection
- **View Data**:
  ```python
  df.head()  # First 5 rows
  df.tail(3)  # Last 3 rows
  df.info()  # Column types and non-null counts
  df.describe()  # Summary statistics
  ```
- **Shape and Columns**:
  ```python
  print(df.shape)  # Output: (rows, columns)
  print(df.columns)  # Output: Index(['name', 'age', 'city'], dtype='object')
  ```

### Filtering and Selection
- **Select Columns**:
  ```python
  df['name']  # Single column (Series)
  df[['name', 'age']]  # Multiple columns (DataFrame)
  ```
- **Filter Rows**:
  ```python
  df[df['age'] > 30]  # Rows where age > 30
  df.query('age > 30')  # Alternative using query
  ```
- **Loc and Iloc**:
  ```python
  df.loc[0, 'name']  # Label-based indexing
  df.iloc[0, 1]  # Integer-based indexing (row 0, column 1)
  ```

---

## 5. Data Cleaning

### Handling Missing Values
- **Check for Missing Values**:
  ```python
  df.isna().sum()  # Count missing values per column
  ```
- **Fill Missing Values**:
  ```python
  df.fillna({'age': df['age'].mean(), 'city': 'Unknown'})  # Fill with mean or constant
  ```
- **Drop Missing Values**:
  ```python
  df.dropna()  # Drop rows with any missing values
  ```

### Removing Duplicates
```python
df.drop_duplicates(subset=['name'], keep='first')  # Keep first occurrence
```

### Data Type Conversion
```python
df['age'] = df['age'].astype(int)  # Convert to integer
df['date'] = pd.to_datetime(df['date'])  # Convert to datetime
```

### Replacing Values
```python
df['city'] = df['city'].replace('New York', 'NYC')  # Replace specific values
```

---

## 6. Data Transformation

### Grouping and Aggregation
Group data and apply functions:
```python
# Group by city and calculate mean age
df.groupby('city')['age'].mean()
# Output:
# city
# London    30.0
# NYC       25.0
# Paris     35.0
# Name: age, dtype: float64
```

Multiple aggregations:
```python
df.groupby('city').agg({'age': ['mean', 'min'], 'name': 'count'})
```

### Merging and Joining
Combine DataFrames:
- **Merge**:
  ```python
  df2 = pd.DataFrame({'name': ['Alice', 'Bob'], 'salary': [50000, 60000]})
  merged = pd.merge(df, df2, on='name', how='left')
  ```
- **Concat**:
  ```python
  df3 = pd.concat([df, df2], axis=0)  # Stack vertically
  ```

### Pivoting and Melting
- **Pivot**:
  ```python
  pivoted = df.pivot(index='name', columns='city', values='age')
  ```
- **Melt** (Unpivot):
  ```python
  melted = pd.melt(df, id_vars=['name'], value_vars=['age', 'city'])
  ```

---

## 7. Advanced Pandas Methods

### Applying Functions
Apply custom functions to columns or rows:
```python
df['age_squared'] = df['age'].apply(lambda x: x**2)
# Or using vectorized operations (faster):
df['age_squared'] = df['age'] ** 2
```

Apply to entire DataFrame:
```python
df.apply(lambda x: x if x.name == 'age' else x.str.upper() if x.dtype == "object" else x)
```

### Window Functions
Calculate rolling or expanding statistics:
```python
df['rolling_mean'] = df['age'].rolling(window=3).mean()
```

### Time Series
Handle time-based data:
```python
df['date'] = pd.date_range('2025-01-01', periods=len(df))
df.set_index('date').resample('M').mean()  # Monthly aggregation
```

---

## 8. Useful Pandas Methods

### DataFrame Methods
- `df.sort_values('age', ascending=False)`: Sort by column.
- `df.value_counts('city')`: Count unique values.
- `df.rename(columns={'name': 'full_name'})`: Rename columns.
- `df.drop('age', axis=1)`: Drop column.
- `df.nlargest(3, 'age')`: Top 3 rows by age.
- `df.sample(n=2, random_state=42)`: Random sample of rows.

### Series Methods
- `s.unique()`: Unique values.
- `s.map({'Alice': 'A', 'Bob': 'B'})`: Map values.
- `s.str.contains('li')`: String pattern matching.
- `s.cumsum()`: Cumulative sum.

### Indexing and Selection
- `df.set_index('name')`: Set column as index.
- `df.reset_index()`: Reset index to default.
- `df.at[0, 'name']`: Fast scalar access (faster than `loc`).

---

## 9. Pandas Tricks and Tips

### 1. **Chain Operations**
Use method chaining for concise code:
```python
df = (df.dropna()
      .query('age > 20')
      .sort_values('age')
      .reset_index(drop=True))
```

### 2. **Memory Optimization**
Reduce memory usage:
```python
df['age'] = df['age'].astype('int8')  # Use smaller data types
df = df[['name', 'age']]  # Select only needed columns
```

### 3. **Categorical Data**
Use `category` type for repetitive data:
```python
df['city'] = df['city'].astype('category')
```

### 4. **Styling DataFrames**
Highlight data in Jupyter:
```python
df.style.highlight_max('age').background_gradient(cmap='Blues')
```

### 5. **Parallel Processing**
Use `pandas` with `multiprocessing` or `Dask` for large datasets:
```python
import dask.dataframe as dd
ddf = dd.from_pandas(df, npartitions=4)
result = ddf.groupby('city').mean().compute()
```

### 6. **Efficient Filtering**
Use `isin` for multiple conditions:
```python
df[df['city'].isin(['NYC', 'Paris'])]
```

### 7. **String Operations**
Manipulate strings efficiently:
```python
df['name'] = df['name'].str.lower().str.replace(' ', '_')
```

### 8. **Conditional Updates**
Update values based on conditions:
```python
df.loc[df['age'] > 30, 'category'] = 'Senior'
```

### 9. **Pivot Table**
Create Excel-like pivot tables:
```python
df.pivot_table(index='city', columns='name', values='age', aggfunc='mean')
```

### 10. **Debugging with `pipe`**
Add custom functions in a pipeline:
```python
def debug(df):
    print(df.shape)
    return df
df.pipe(debug).groupby('city').mean()
```

---

## 10. Pandas with Visualization
Integrate with Matplotlib/Seaborn:
```python
import matplotlib.pyplot as plt
import seaborn as sns
sns.boxplot(x='city', y='age', data=df)
plt.title('Age Distribution by City')
plt.show()
```

---

## 11. Best Practices

- **Use Vectorized Operations**: Avoid loops; use NumPy/Pandas methods.
  ```python
  # Bad
  for i in range(len(df)):
      df.iloc[i, 1] = df.iloc[i, 1] * 2
  # Good
  df['age'] = df['age'] * 2
  ```
- **Document Code**: Add comments or use Jupyter notebooks.
- **Handle Missing Data Early**: Clean data before analysis.
- **Optimize Memory**: Use appropriate data types and drop unused columns.
- **Test with Small Data**: Validate code on a subset before scaling.

---

## 12. Troubleshooting & Tips

### Common Issues
- **KeyError**: Check column names with `df.columns`.
- **Performance Issues**: Use `df.itertuples()` instead of `iterrows()` for iteration:
  ```python
  for row in df.itertuples():
      print(row.name, row.age)
  ```
- **Data Type Issues**: Verify types with `df.dtypes`.

### Performance Tips
- **Use `categorical` for Repeated Strings**:
  ```python
  df['category'] = df['category'].astype('category')
  ```
- **Chunk Large Files**:
  ```python
  for chunk in pd.read_csv('large_data.csv', chunksize=1000):
      process(chunk)
  ```
- **Avoid Copies**:
  ```python
  df_subset = df[['name', 'age']].copy()  # Explicit copy to avoid SettingWithCopyWarning
  ```

---

## 13. Resources & Further Learning

- **Official Documentation**: [Pandas Docs](https://pandas.pydata.org/docs/)
- **Tutorials**: [Kaggle Pandas](https://www.kaggle.com/learn/pandas), [DataCamp Pandas](https://www.datacamp.com/courses/pandas)
- **Books**: "Python for Data Analysis" by Wes McKinney
- **Community**: [Stack Overflow](https://stackoverflow.com/questions/tagged/pandas), [Pandas GitHub](https://github.com/pandas-dev/pandas)

---