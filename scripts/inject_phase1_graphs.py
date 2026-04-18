import nbformat as nbf

notebook_path = 'Wholesale_Customers.ipynb'
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

new_markdown_source = """### Visualizing Data Disruptions (Skewness & Outliers)
While earlier we used `df.describe()` to mathematically identify variations, providing a visual representation paints a much clearer picture for clients. Below, we've produced two key visualization types:
1. **Histograms (with Mean and Median lines)**: This shows the distribution shape. We can clearly see the distribution is heavily pulled to the right, signifying 'Positive Skewness'. The 'Mean' is heavily disrupted upwards by massive spenders, abandoning the 'Median'. 
2. **Boxplots**: A standard approach to find outliers. The solid boxes represent where the central 50% of our clients lie. The dots scattered high above are our 'disruptions'—individual clients purchasing massively larger quantities than a normal customer."""

new_code_source = """import warnings
warnings.filterwarnings('ignore')

continuous_features = ['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']

# 1. Histograms to show Skewness
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 10))
fig.suptitle('Distributions of Annual Spending (Highlighting Extreme Skewness)', fontsize=18, y=1.02)
axes = axes.flatten()

for i, col in enumerate(continuous_features):
    sns.histplot(df[col], kde=True, ax=axes[i], color='skyblue', bins=40)
    median_val = df[col].median()
    mean_val = df[col].mean()
    axes[i].axvline(median_val, color='red', linestyle='--', linewidth=2, label=f'Median: {median_val:.0f}')
    axes[i].axvline(mean_val, color='navy', linestyle='-', linewidth=2, label=f'Mean: {mean_val:.0f}')
    axes[i].set_title(f'{col} Spending')
    axes[i].legend()

plt.tight_layout()
plt.show()

# 2. Boxplots to emphasize Outliers
plt.figure(figsize=(14, 7))
sns.boxplot(data=df[continuous_features], palette='pastel')
plt.title('Boxplots of Annual Spending (Highlighting Extreme Outliers vs Interquartile Range)', fontsize=16)
plt.ylabel('Annual Spending (Monetary Units)')
plt.xticks(rotation=45)
plt.show()"""

new_md_cell = nbf.v4.new_markdown_cell(new_markdown_source)
new_code_cell = nbf.v4.new_code_cell(new_code_source)

# Find the index of the cell containing df.describe()
insert_idx = -1
for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code' and 'df.describe()' in cell.source:
        insert_idx = i + 1
        break

if insert_idx != -1:
    nb.cells.insert(insert_idx, new_md_cell)
    nb.cells.insert(insert_idx + 1, new_code_cell)
    
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print("Successfully injected Phase 1 graphs into the notebook.")
else:
    print("Could not find the df.describe() cell.")
