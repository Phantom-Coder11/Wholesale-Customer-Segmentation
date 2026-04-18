# Phase 2: Data Cleaning & Preprocessing

## 1. Objective
Following the discoveries in Phase 1 (extreme skewed distributions and enormous outliers), Phase 2 handles transforming the raw data into a mathematically robust format for clustering algorithms.

## 2. Execution Steps

### Deduplication
We executed `df.drop_duplicates()`. Since the ID isn't provided and the rows might just have overlapping values, we verified the count. No duplicates were accidentally introduced, meaning all 440 client records were retained as distinct data points.

### Log Transformation (`np.log1p`)
The continuous spending variables exhibited fierce positive skew (e.g., maximum purchases extending dramatically beyond the 75th percentile). Un-transformed, a K-Means algorithm would group customers based solely on the massive outliers, rendering the clusters useless for the majority of the data. 

To counteract this:
- We applied a **natural logarithmic transformation** to compress the scale.
- We used `numpy.log1p` instead of standard `np.log` safely handle any potential zero-spend categories, avoiding math errors.

### Feature Scaling
After logarithm transformation, we applied **Standard Scaler**.
- Even logged, spending on 'Fresh' products usually eclipses smaller categories like 'Delicassen'. Standard Scaler centers all variables to a mean of 0 and standard deviation of 1.
- This ensures that a unit difference in Delicassen spends carries the exact same mathematical weight as a unit difference in Fresh spends when calculating Euclidean distances for our clusters.

## 3. Saving the Processed Data
Finally, we ensured our test data was strictly isolated. We combined the unmodified `Channel` and `Region` parameters with our transformed continuous parameters and wrote it to `data/Cleaned_Wholesale_Data.csv`.
