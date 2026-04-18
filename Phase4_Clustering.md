# Phase 4: Model Training (Customer Segmentation)

## 1. Objective
As this dataset lacks a deterministic target variable, our objective was unsupervised learning. We aim to group the 440 wholesale clients into distinct "clusters" displaying similar purchasing behaviors. 

## 2. Finding the Optimal '$K$'
K-Means clustering requires us to define the number of clusters ($K$) beforehand. We utilized two mathematical strategies to find the best $K$:
- **Elbow Method (Inertia)**: Measuring the sum of squared distances of samples to their cluster center. 
- **Silhouette Score**: Measuring how similar an object is to its own cluster compared to other clusters (values from -1 to 1).

Plotting K from 2 to 10 revealed that $K=3$ provides highly cohesive groupings. The silhouette score hits a strong local peak, while inertia begins to slope less steeply.

## 3. K-Means Execution
We trained `KMeans(n_clusters=3)` on our scaled, transformed data. By aggregating the original, unscaled spending values grouped by cluster, we can assign business definitions:
- **Cluster 0**: Potentially retail buyers with heavy Grocery/Milk needs.
- **Cluster 1**: Potentially 'Horeca' (restaurants) with massive reliance on Fresh food.
- **Cluster 2**: Low-volume buyers across the board.

## 4. PCA Validation
To visually validate the model, we can't plot 6 dimensions. Therefore, we used Principal Component Analysis (PCA) to distill the 6 continuous variables into a 2-Dimensional X/Y plane for visualization. 

The resulting scatter plot shows the 3 clusters grouping exceptionally cleanly with very little boundary overlap, indicating our preprocessing (log + scaling) established an incredibly robust environment for our final Model.
