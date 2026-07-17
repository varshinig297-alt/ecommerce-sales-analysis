import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/SampleSuperstore.csv", encoding="latin1")

print("="*50)
print("FIRST 5 ROWS")
print("="*50)
print(df.head())


print("\n" + "="*50)
print("DATASET INFORMATION")
print("="*50)
print(df.info())


print("\n" + "="*50)
print("MISSING VALUES")
print("="*50)
print(df.isnull().sum())


print("\n" + "="*50)
print("STATISTICAL SUMMARY")
print("="*50)
print(df.describe())


print("\n" + "="*50)
print("COLUMN NAMES")
print("="*50)
print(df.columns)