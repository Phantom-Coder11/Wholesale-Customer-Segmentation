# Phase 3: Exploratory Data Analysis (EDA)

## 1. Objective
Phase 3 visually evaluates our cleaned and transformed variables, validating the effectiveness of our Log Transformation, and explores correlations between different types of customer spending.

## 2. Visualizations

### Post-Transformation Distributions (Boxplots)
By plotting the updated boxplots of our Log-Scaled features, we successfully validated the preprocessing. The previously massive tails and exponential skewness vanished. Instead, the features exhibited far more symmetric, normalized distributions. Some distinct outliers remain, but they have been suppressed enough to no longer dominate algorithms.

### Correlation Heatmap
Understanding how products are bought together is vital for business strategy. 
We produced a Pearson Correlation matrix. Key discoveries typically include:
- **Grocery & Detergents_Paper**: Exhibit a strong positive correlation. Customers spending heavily on groceries are highly likely to also buy large amounts of detergents and paper.
- **Milk & Grocery**: Also exhibit strong positive correlation.
- **Fresh vs. Others**: `Fresh` spending tends to be relatively independent of the others, establishing its own unique buying demographic.
