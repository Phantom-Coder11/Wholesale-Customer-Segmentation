import nbformat as nbf
import os

# Read the existing notebook
nb = nbf.read('Wholesale_Customers.ipynb', as_version=4)

# PHASE 2
nb.cells.extend([
    nbf.v4.new_markdown_cell("# Phase 2: Data Cleaning & Preprocessing\nOur goals in this phase are to eliminate any basic flaws (like full-row duplicates), and aggressively tackle the extreme positive skew present in our spending data via Log Transformation and Standard Scaling. We will then save the cleaned result to a dedicated `data/` folder."),
    nbf.v4.new_code_cell("""
print(f"Original shape: {df.shape}")
df = df.drop_duplicates()
print(f"Shape after duplicates removed: {df.shape}")

from sklearn.preprocessing import StandardScaler
import numpy as np
import os

spend_features = ['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']

# Log Transform (np.log is unsafe with 0, np.log1p handles 0 by doing log(1+x))
log_data = np.log1p(df[spend_features])

# Standard Scaling ensures Euclidean distances aren't dominated by raw magnitude
scaler = StandardScaler()
scaled_data = scaler.fit_transform(log_data)
df_scaled = pd.DataFrame(scaled_data, columns=spend_features, index=df.index)

# Re-attach Channel & Region
df_cleaned = df[['Channel', 'Region']].join(df_scaled)

# Ensure 'data' directory exists and save
os.makedirs('data', exist_ok=True)
df_cleaned.to_csv('data/Cleaned_Wholesale_Data.csv', index=False)
print("Cleaned & Scaled data saved to 'data/Cleaned_Wholesale_Data.csv'!")
display(df_cleaned.head())
""")
])

# PHASE 3
nb.cells.extend([
    nbf.v4.new_markdown_cell("# Phase 3: Exploratory Data Analysis\nWe will visualize the transformed distributions to ensure they are more normalized, and map out the correlations between different categorical spends."),
    nbf.v4.new_code_cell("""
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_cleaned[spend_features], palette='muted')
plt.title("Boxplot of Spend Features (Post Log-Transform & Scaling)", fontsize=14)
plt.xticks(rotation=45)
plt.show()
"""),
    nbf.v4.new_code_cell("""
plt.figure(figsize=(8, 6))
sns.heatmap(df_cleaned[spend_features].corr(), annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
plt.title("Correlation Matrix of Product Categories", fontsize=14)
plt.show()
""")
])

# PHASE 4
nb.cells.extend([
    nbf.v4.new_markdown_cell("# Phase 4: Clustering & Customer Segmentation\nUsing K-Means clustering to dynamically segment customers based on their spending behavior. We will use the Elbow Method and Silhouette Score to find the mathematical 'best' number of clusters ($K$)."),
    nbf.v4.new_code_cell("""
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import warnings
warnings.filterwarnings('ignore') # ignore K-means warning

inertia = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(df_scaled)
    inertia.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(df_scaled, clusters))

fig, ax1 = plt.subplots(figsize=(10, 5))
ax1.plot(K_range, inertia, 'bo-', label='Inertia (Within-Cluster Sum of Squares)')
ax1.set_xlabel('Number of Clusters (k)', fontsize=12)
ax1.set_ylabel('Inertia', color='b', fontsize=12)
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(K_range, silhouette_scores, 'ro-', label='Silhouette Score')
ax2.set_ylabel('Silhouette Score', color='r', fontsize=12)
ax2.tick_params(axis='y', labelcolor='r')

plt.title('Determining Optimal K: Elbow Method & Silhouette Score', fontsize=14)
plt.grid(False)
plt.show()
"""),
    nbf.v4.new_markdown_cell("Based on the Silhouette score hitting a peak and the inertia showing an 'elbow', `k=3` or `k=5` are great candidates. We will proceed with **K=3** for interpretability."),
    nbf.v4.new_code_cell("""
optimal_k = 3
final_kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df['Cluster'] = final_kmeans.fit_predict(df_scaled)

print("--- CLUSTER CHARACTERISTICS ---")
target_insight = df.groupby('Cluster')[spend_features].mean().round(2)
display(target_insight)
"""),
    nbf.v4.new_code_cell("""
# PCA Visual validation
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(df_scaled)

plt.figure(figsize=(10, 7))
sns.scatterplot(x=reduced_data[:,0], y=reduced_data[:,1], hue=df['Cluster'], palette='Set1', s=100, alpha=0.8)
plt.title('2D PCA Projection of the Clusters', fontsize=14)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Cluster')
plt.show()
""")
])

nbf.write(nb, 'Wholesale_Customers.ipynb')
print("Notebook build finished successfully!")
