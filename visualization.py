import pandas as pd
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv("data/raw/SampleSuperstore.csv", encoding="latin1")


# 1. Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("visuals/sales_by_category.png")
plt.close()


# 2. Profit by Region
region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(8,5))
region_profit.plot(kind="bar")
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("visuals/profit_by_region.png")
plt.close()


# 3. Sales by Segment
segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(6,6))
segment_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Segment")
plt.ylabel("")

plt.savefig("visuals/sales_by_segment.png")
plt.close()


# 4. Top 10 Sub-Categories
sub_category_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
sub_category_sales.plot(kind="bar")
plt.title("Top 10 Sub-Categories by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("visuals/top10_subcategories.png")
plt.close()


print("All visualizations created successfully!")