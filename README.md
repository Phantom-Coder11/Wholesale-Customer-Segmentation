# Wholesale Customer Segmentation 🛒

This repository demonstrates an end-to-end Unsupervised Machine Learning pipeline for segmenting B2B wholesale customers based on their annual spending behaviors. By identifying distinct purchasing patterns, businesses can tailor their marketing, supply chain, and service strategies.

## 🎯 Business Objective
A wholesale distributor recently gathered data on 440 clients across six product categories: Fresh, Milk, Grocery, Frozen, Detergents/Paper, and Delicatessen. Without any deterministic labels, our objective was to discover hidden structures in the data and group clients into distinct "Buyer Personas" to optimize business operations.

## 🔬 Methodology

1. **Phase 1: Data Understanding & Profiling**
   - Discovered extreme **positive skewness** across the monetary spending data.
   - Identified that heavily skewed outliers ("whales") severely impacted the mean, necessitating mathematical transformation.

2. **Phase 2: Cleaning & Engineering**
   - Applied a **Logarithmic Transformation** (`np.log1p`) to compress extreme values while preserving variance.
   - Used **StandardScaler** to ensure high-volume products (like Fresh vegetables) didn't overshadow low-volume products in Euclidean space.

3. **Phase 3: Exploratory Data Analysis (EDA)**
   - Visualized the transformed distributions.
   - Mapped positive correlations (e.g., Grocery & Detergents/Paper) using a seaborn heatmap.

4. **Phase 4: Clustering & Unsupervised ML**
   - Evaluated K-Means clustering configurations using the **Elbow Method (Inertia)** and **Silhouette Scores**.
   - Mathematically proved **K=3** was the optimal number of natural segments.
   - Reduced 6-dimensional data using **Principal Component Analysis (PCA)** to visually validate the tight clustering in 2D space.

## 💡 Key Results
The model successfully partitioned the 440 clients into three distinct, highly actionable segments:
- **Cluster 0**: Retail-heavy buyers with significant spending in Grocery and Milk.
- **Cluster 1**: 'Horeca' (Hotels/Restaurants/Cafes) exhibiting massive reliance on Fresh food.
- **Cluster 2**: Low-volume buyers across all categories.

## 🛠 Directory Structure
```
├── Wholesale_Customers.ipynb       # Main Jupyter Notebook
├── Wholesale customers data.csv    # Raw Dataset
├── requirements.txt                # Python dependencies
├── .gitignore                      
├── scripts/                        # Utility Python scripts used for notebook generation
└── *.md                            # Deep-dive Phase documentation (Phases 1-4)
```

## 🚀 How to Run Locally
1. Clone this repository to your local machine.
2. Install the required dependencies using: `pip install -r requirements.txt`
3. Launch the central notebook using Jupyter or VS Code:
   ```bash
   jupyter notebook Wholesale_Customers.ipynb
   ```
