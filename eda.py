import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/SampleSuperstore.csv", encoding="latin1")


# 1. Total Sales
print("="*50)
print("TOTAL SALES")
print("="*50)
print(df["Sales"].sum())


# 2. Total Profit
print("\n" + "="*50)
print("TOTAL PROFIT")
print("="*50)
print(df["Profit"].sum())


# 3. Total Orders
print("\n" + "="*50)
print("TOTAL ORDERS")
print("="*50)
print(len(df))


# 4. Average Sales
print("\n" + "="*50)
print("AVERAGE SALES")
print("="*50)
print(df["Sales"].mean())


# 5. Sales by Category
print("\n" + "="*50)
print("SALES BY CATEGORY")
print("="*50)
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))


# 6. Profit by Region
print("\n" + "="*50)
print("PROFIT BY REGION")
print("="*50)
print(df.groupby("Region")["Profit"].sum().sort_values(ascending=False))


# 7. Top 10 Sub-Categories
print("\n" + "="*50)
print("TOP 10 SUB-CATEGORIES BY SALES")
print("="*50)
print(
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)


# 8. Sales by Segment
print("\n" + "="*50)
print("SALES BY SEGMENT")
print("="*50)
print(df.groupby("Segment")["Sales"].sum().sort_values(ascending=False))