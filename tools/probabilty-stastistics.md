# Probability & Statistics

---

## 1. Introduction to Probability & Statistics

### What is Probability?
Probability quantifies the likelihood of events occurring, expressed as a value between 0 (impossible) and 1 (certain). It forms the basis for statistical inference.

### What is Statistics?
Statistics involves collecting, analyzing, interpreting, and presenting data to make informed decisions. It uses probability to model uncertainty and draw conclusions from data.

### Why Study Probability & Statistics?
- **Data Analysis**: Understand patterns and trends in data.
- **Decision Making**: Make predictions and assess risks.
- **Machine Learning**: Underpins algorithms like regression and classification.

---

## 2. Probability Fundamentals

### 2.1. Basic Concepts
- **Sample Space (S)**: All possible outcomes of an experiment (e.g., rolling a die: S = {1, 2, 3, 4, 5, 6}).
- **Event**: A subset of the sample space (e.g., rolling an even number: {2, 4, 6}).
- **Probability of an Event**: P(A) = (Number of favorable outcomes) / (Total outcomes).
  ```python
  # Probability of rolling a 3 with a fair die
  favorable = 1  # {3}
  total = 6  # {1, 2, 3, 4, 5, 6}
  prob = favorable / total
  print(prob)  # Output: 0.16666666666666666
  ```

### 2.2. Probability Rules
- **Addition Rule**: For mutually exclusive events, P(A or B) = P(A) + P(B).
  ```python
  # Probability of rolling a 1 or 2
  prob_1_or_2 = 1/6 + 1/6
  print(prob_1_or_2)  # Output: 0.3333333333333333
  ```
- **Multiplication Rule**: For independent events, P(A and B) = P(A) * P(B).
  ```python
  # Probability of rolling two 3s in a row
  prob_two_3s = (1/6) * (1/6)
  print(prob_two_3s)  # Output: 0.027777777777777776
  ```
- **Conditional Probability**: P(A|B) = P(A and B) / P(B).
  ```python
  # P(ace | red card) in a deck of 52 cards
  prob_red = 26/52
  prob_ace_and_red = 2/52
  prob_ace_given_red = prob_ace_and_red / prob_red
  print(prob_ace_given_red)  # Output: 0.07692307692307693
  ```

### 2.3. Random Variables
- **Discrete**: Takes specific values (e.g., number of heads in coin flips).
- **Continuous**: Takes any value in a range (e.g., height).
- **Probability Distributions**:
  - **Discrete**: Binomial, Poisson.
  - **Continuous**: Normal, Exponential.
  ```python
  from scipy.stats import binom
  # Binomial: 10 coin flips, P(heads) = 0.5, P(exactly 5 heads)
  prob = binom.pmf(k=5, n=10, p=0.5)
  print(prob)  # Output: 0.24609375
  ```

---

## 3. Descriptive Statistics

### 3.1. Measures of Central Tendency
- **Mean**: Average of data.
- **Median**: Middle value when sorted.
- **Mode**: Most frequent value.
```python
import numpy as np
import pandas as pd
data = [1, 2, 2, 3, 4, 5]
print(np.mean(data))  # Output: 2.8333333333333335
print(np.median(data))  # Output: 2.5
print(pd.Series(data).mode()[0])  # Output: 2
```

### 3.2. Measures of Dispersion
- **Variance**: Average squared deviation from the mean.
- **Standard Deviation**: Square root of variance.
- **Range**: Max - Min.
```python
print(np.var(data))  # Output: 1.8055555555555556
print(np.std(data))  # Output: 1.3437096247164249
print(max(data) - min(data))  # Output: 4
```

### 3.3. Percentiles and Quartiles
- **Percentiles**: Value below which a percentage of data falls.
- **Quartiles**: Divide data into four equal parts (Q1, Q2, Q3).
```python
print(np.percentile(data, 25))  # Q1: 2.0
print(np.percentile(data, 50))  # Q2 (Median): 2.5
print(np.percentile(data, 75))  # Q3: 3.75
```

---

## 4. Probability Distributions

### 4.1. Discrete Distributions
- **Binomial**: Models number of successes in n trials.
  ```python
  from scipy.stats import binom
  prob = binom.pmf(k=3, n=5, p=0.6)  # P(3 successes in 5 trials, p=0.6)
  print(prob)  # Output: 0.3456
  ```
- **Poisson**: Models events in a fixed interval.
  ```python
  from scipy.stats import poisson
  prob = poisson.pmf(k=2, mu=3)  # P(2 events, average=3)
  print(prob)  # Output: 0.22404180765538775
  ```

### 4.2. Continuous Distributions
- **Normal (Gaussian)**: Bell-shaped distribution.
  ```python
  from scipy.stats import norm
  prob = norm.pdf(x=0, loc=0, scale=1)  # PDF at x=0, mean=0, std=1
  print(prob)  # Output: 0.3989422804014327
  ```
- **Exponential**: Models time between events.
  ```python
  from scipy.stats import expon
  prob = expon.cdf(x=1, scale=2)  # P(X ≤ 1, mean=2)
  print(prob)  # Output: 0.3934693402873666
  ```

---

## 5. Inferential Statistics

### 5.1. Hypothesis Testing
Test claims about populations using sample data.
- **Null Hypothesis (H₀)**: No effect or difference.
- **Alternative Hypothesis (H₁)**: Effect or difference exists.
- **P-value**: Probability of observing data if H₀ is true.
Example (t-test):
```python
from scipy.stats import ttest_ind
group1 = [10, 12, 14, 15]
group2 = [13, 15, 16, 18]
t_stat, p_value = ttest_ind(group1, group2)
print(p_value)  # Output: P-value (e.g., 0.123)
# If p < 0.05, reject H₀
```

### 5.2. Confidence Intervals
Estimate a population parameter range.
```python
import numpy as np
from scipy.stats import t
data = [10, 12, 14, 15]
mean = np.mean(data)
std = np.std(data, ddof=1)
n = len(data)
ci = t.interval(alpha=0.95, df=n-1, loc=mean, scale=std/np.sqrt(n))
print(ci)  # Output: (10.811, 15.689) (95% CI for mean)
```

### 5.3. Correlation and Regression
- **Correlation**: Measure relationship between variables.
  ```python
  df = pd.DataFrame({'x': [1, 2, 3, 4], 'y': [2, 4, 5, 7]})
  print(df['x'].corr(df['y']))  # Output: 0.9827076298239907
  ```
- **Linear Regression**:
  ```python
  from sklearn.linear_model import LinearRegression
  model = LinearRegression()
  model.fit(df[['x']], df['y'])
  print(model.coef_, model.intercept_)  # Output: Slope, Intercept
  ```

---

## 6. Practical Applications with Pandas

### Data Analysis Example
Analyze a dataset using Pandas and statistical methods:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load data
df = pd.DataFrame({
    'group': ['A']*50 + ['B']*50,
    'value': np.concatenate([np.random.normal(10, 2, 50), np.random.normal(12, 2, 50)])
})

# Descriptive statistics
print(df.groupby('group')['value'].describe())

# Visualize
df.boxplot(column='value', by='group')
plt.title('Value Distribution by Group')
plt.show()

# Hypothesis test
group_a = df[df['group'] == 'A']['value']
group_b = df[df['group'] == 'B']['value']
t_stat, p_value = ttest_ind(group_a, group_b)
print(f"P-value: {p_value}")  # Check if groups differ significantly
```

---

## 7. Useful Methods and Tricks

### Probability Calculations
- **Simulate Probabilities**:
  ```python
  np.random.seed(42)
  trials = np.random.binomial(n=10, p=0.5, size=1000)  # 10 coin flips, 1000 trials
  prob_5_heads = np.mean(trials == 5)
  print(prob_5_heads)  # Approximate binomial probability
  ```

### Statistical Analysis
- **Z-Scores**:
  ```python
  data = np.array([10, 12, 14, 15])
  z_scores = (data - np.mean(data)) / np.std(data, ddof=1)
  print(z_scores)
  ```
- **Outlier Detection**:
  ```python
  q1, q3 = np.percentile(data, [25, 75])
  iqr = q3 - q1
  outliers = data[(data < q1 - 1.5*iqr) | (data > q3 + 1.5*iqr)]
  print(outliers)
  ```

### Pandas Integration
- **Group Statistics**:
  ```python
  df.groupby('group')['value'].agg(['mean', 'std', 'count'])
  ```
- **Rolling Statistics**:
  ```python
  df['rolling_mean'] = df['value'].rolling(window=3).mean()
  ```

### Visualization
- **Distribution Plot**:
  ```python
  import seaborn as sns
  sns.histplot(df['value'], kde=True)
  plt.title('Distribution of Values')
  plt.show()
  ```

---

## 8. Best Practices

- **Set Random Seed**: Ensure reproducibility.
  ```python
  np.random.seed(42)
  ```
- **Validate Assumptions**: Check normality or equal variances before tests.
  ```python
  from scipy.stats import shapiro
  stat, p = shapiro(df['value'])
  print(p)  # If p > 0.05, data is approximately normal
  ```
- **Use Vectorized Operations**: Avoid loops for calculations.
- **Document Findings**: Summarize statistical results clearly.
- **Handle Small Samples**: Use non-parametric tests (e.g., Mann-Whitney U) for small datasets.
  ```python
  from scipy.stats import mannwhitneyu
  stat, p = mannwhitneyu(group_a, group_b)
  print(p)
  ```

---

## 9. Troubleshooting & Tips

### Common Issues
- **Non-Normal Data**: Use non-parametric tests or transform data (e.g., log).
  ```python
  df['log_value'] = np.log(df['value'] + 1)  # Avoid log(0)
  ```
- **Missing Data**: Impute or drop carefully.
  ```python
  df['value'].fillna(df['value'].mean(), inplace=True)
  ```
- **P-value Misinterpretation**: Ensure correct null hypothesis and significance level.

### Performance Tips
- **Use NumPy for Large Datasets**:
  ```python
  np.mean(df['value'].to_numpy())  # Faster than Pandas for large arrays
  ```
- **Parallelize with Dask**:
  ```python
  import dask.dataframe as dd
  ddf = dd.from_pandas(df, npartitions=4)
  print(ddf['value'].mean().compute())
  ```

---

## 10. Resources & Further Learning

- **Official Documentation**: [SciPy Stats](https://docs.scipy.org/doc/scipy/reference/stats.html), [NumPy](https://numpy.org/doc/), [Pandas](https://pandas.pydata.org/docs/)
- **Tutorials**: [StatQuest](https://statquest.org/), [Khan Academy Statistics](https://www.khanacademy.org/math/statistics-probability)
- **Books**: "Introduction to Probability" by Joseph K. Blitzstein, "Statistics" by David Freedman
- **Community**: [Stack Overflow](https://stackoverflow.com/questions/tagged/statistics), [Cross Validated](https://stats.stackexchange.com/)

---