# 🔬 **Practice Lab - 3: Real-time Data Processing & Visualization**

## 🎯 **Objective**

To practice **real-world data handling** using

* `scipy` for numerical analysis,
* `matplotlib` for visualization,
* `flask` for building a small web interface,
* and **`web scraping/datasets`** for real-time data sources.

---

## 🛠️ **Real-Time Lab Tasks**

### Task 1: Data Collection

* **Option A: Web Scraping**

  * Scrape live weather data (e.g., from [weather.com](https://weather.com) or [IMD](https://mausam.imd.gov.in/)).
  * Scrape stock prices (e.g., from [Yahoo Finance](https://finance.yahoo.com/)).
    👉 Use `requests + BeautifulSoup4`.

* **Option B: Use Datasets**

  * Kaggle dataset links:

    * [COVID-19 Dataset](https://www.kaggle.com/datasets/imdevskp/corona-virus-report)
    * [World Happiness Report](https://www.kaggle.com/datasets/unsdsn/world-happiness)
    * [IPL Data](https://www.kaggle.com/datasets/manasgarg/ipl)

---

### Task 2: Data Processing with `scipy`

* Perform **basic statistics**: mean, median, standard deviation.
* Use `scipy.stats` for hypothesis testing (e.g., compare two cities’ weather temperatures).
* Use `scipy.optimize` for curve fitting (e.g., trendline for stock price data).

---

### Task 3: Visualization with `matplotlib`

* Plot **time-series graphs** (temperature/stock prices).
* Create **bar charts** (team wins in IPL).
* Create **heatmaps** for correlations.

---

### Task 4: Build a Mini Web App with `flask`

* Create a simple **dashboard**:

  * Upload a CSV dataset (or fetch scraped data).
  * Show statistical results (`scipy`).
  * Display interactive plots (`matplotlib` → convert plots into PNG/HTML).

---
## 💻 **Example Flow**

1. Scrape **today’s Hyderabad weather data**.
2. Process data using **scipy** (`mean`, `variance`, trend analysis).
3. Visualize with **matplotlib** (temperature variation).
4. Display results on a **flask app dashboard**.

---
---

# 🛒 **Lab Project 3.2: E-commerce Price History Tracker**

## 🎯 **Objective**

* Scrape product prices (Amazon, Flipkart, etc.).
* Store historical prices for analysis.
* Use `scipy` for statistics & trend analysis.
* Visualize with `matplotlib`.
* Display insights with `flask` web dashboard.

---

## 🛠️ **Steps**

### Step 1: Web Scraping

* Scrape product **name, price, rating**.
* Use `requests + BeautifulSoup` (or `playwright`/`selenium` for dynamic pages).
* Example: Track a laptop or mobile price daily.
* Store data in **CSV / SQLite DB**.

---

### Step 2: Data Processing with `scipy`

* Compute **mean, median, std deviation** of prices.
* Detect **outliers** (fake discounts).
* Use `scipy.signal` for **trend detection**.

---

### Step 3: Visualization with `matplotlib`

* Line chart: price vs time.
* Bar chart: comparison of multiple sellers.
* Scatter plot: price vs rating.

---

### Step 4: Flask Dashboard

* Upload product URL → Start tracking.
* Show **price history chart**.
* Display alerts (e.g., “Lowest price in last 30 days!”).
* Optionally: Send **email/SMS alerts** when price drops.

---
---

## ✅ **Rubric for Evaluation**

| Criteria                               | Marks  |
| -------------------------------------- | ------ |
| Data Collection (Scraping/API/Dataset) | 5      |
| Data Processing (scipy use)            | 10     |
| Visualization (matplotlib)             | 10     |
| Flask Integration (Mini App)           | 5      |
| Presentation & Demo                    | 5      |
| **Total**                              | **35** |

---

## 🙏 **Credits / Acknowledgements**

We acknowledge the use of open-source libraries, datasets, and references that make this **E-commerce Price History Tracker** lab possible:

* **Python Libraries**

  * [`requests`](https://docs.python-requests.org/en/latest/) & [`BeautifulSoup4`](https://www.crummy.com/software/BeautifulSoup/) for web scraping.
  * [`scipy`](https://scipy.org/) for statistical analysis and trend detection.
  * [`matplotlib`](https://matplotlib.org/) for visualizations.
  * [`flask`](https://flask.palletsprojects.com/) for building the web dashboard.
  * Live scraping examples (educational use only, respecting website terms & conditions).

* **Community References**

  * [Kaggle Community](https://www.kaggle.com/) for curated datasets.
  * [Real Python Tutorials](https://realpython.com/) for practical Flask and web scraping guides.

---

> This lab is intended solely for **academic and practice purposes**.

> Full credit goes to the original authors and maintainers for their contribution to the open-source and data science education community.

---
