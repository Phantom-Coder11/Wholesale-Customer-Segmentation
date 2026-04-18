import pandas as pd

df = pd.read_csv("Wholesale customers data.csv")

print("--- DATA INFO ---")
df.info()

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DESCRIPTIVE STATISTICS ---")
print(df.describe())
