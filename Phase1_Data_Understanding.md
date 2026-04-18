# Phase 1: Data Understanding - Wholesale Customer Data

## 1. Objective
Our first step is to load the `Wholesale customers data.csv` dataset and familiarize ourselves with its basic structure. We want to check what columns we're dealing with, identify any data quality issues (like missing values), and establish a baseline understanding of what the ranges and types of our features look like.

## 2. Dataset Overview
After loading the dataset using pandas, we extracted the following metadata:

### Shape & Data Types
The dataset consists of **440 rows** and **8 columns**. 
- All 8 features are loaded as `int64` (integers).
- The memory usage is fairly lightweight (27.6 KB), and no complex text extraction is necessary.

### Feature Breakdown
There are two categorical features (though encoded numerically):
- `Channel`: Customer channel (Horeca (Hotel/Restaurant/Cafe) [1] or Retail channel [2]).
- `Region`: Geographic region of the customer (Lisbon [1], Oporto [2], or Other Region [3]).

The remaining **6 features** are continuous and represent the annual spending in monetary units across various product categories:
- `Fresh`: Annual spend on fresh products (e.g., vegetables, meats).
- `Milk`: Annual spend on dairy.
- `Grocery`: Annual spend on grocery products.
- `Frozen`: Annual spend on frozen products.
- `Detergents_Paper`: Annual spend on cleaning/paper supplies.
- `Delicassen`: Annual spend on delicatessen.

### Missing Values
A check using `isnull().sum()` reveals that the dataset is completely intact. There are **0 missing values** across all columns.

## 3. Initial Descriptive Findings
By running `df.describe()`, we found clear indicators of **severe skewness / outliers**:
- **Huge discrepancies between Percentiles**: In almost all continuous spend categories, the maximum value is exponentially higher than the median (50th percentile) or 75th percentile.
  - Example (`Fresh`): Mean is 12,000, Median is 8,504, but Maximum is 112,151.
  - Example (`Detergents_Paper`): Mean is 2,881, Median is 816, but Maximum is 40,827.
- **Positive Skew**: For feature vectors representing monetary spends, this suggests a log-normal distribution — meaning the vast majority of clients spend relatively moderate amounts, while a few "whale" clients spend extraordinarily large sums. 

### Visualizing the Disruptions
While `df.describe()` highlights the issues mathematically, we also integrated graphical representations to better illustrate the skewness and outliers in the original unscaled data:
- **Histograms with Mean/Median Lines**: Visually demonstrates how the right-tailed extreme values physically pull the `Mean` away from the `Median`, providing a concrete look at the "positive skew".
- **Boxplots**: Demonstrates the massive disruptions (outliers) that hover at values 10x-20x the size of the densely packed interquartile (IQR) box. This visually prepares stakeholders for the necessity of mathematical scaling in Phase 2.
## 4. Next Steps for Phase 2
Understanding the skewness here dictates our actions for Phase 2:
1. **Outlier Detection**: We need to formally visualize and evaluate these extreme tails (e.g., using box plots or IQR calculations).
2. **Transformations**: Before clustering, keeping the data strongly positively skewed will destroy model viability since algorithms like K-Means rely on Euclidean distances. We'll need to apply a **logarithmic transformation** and **feature scaling** (like `StandardScaler`) so that categories with huge natural values (like `Fresh`) do not dominate those with smaller natural values (like `Delicassen`).
