import pandas as pd
import sqlite3


# Load CSV file
df = pd.read_csv("data/raw/SampleSuperstore.csv", encoding="latin1")


# Create SQLite database
connection = sqlite3.connect("ecommerce.db")


# Convert dataframe into SQL table
df.to_sql("superstore", connection, if_exists="replace", index=False)


print("="*50)
print("TOTAL SALES")
print("="*50)

query = """
SELECT SUM(Sales) AS Total_Sales
FROM superstore;
"""

print(pd.read_sql(query, connection))


print("\n" + "="*50)
print("TOTAL PROFIT")
print("="*50)

query = """
SELECT SUM(Profit) AS Total_Profit
FROM superstore;
"""

print(pd.read_sql(query, connection))


print("\n" + "="*50)
print("SALES BY CATEGORY")
print("="*50)

query = """
SELECT 
Category,
SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC;
"""

print(pd.read_sql(query, connection))


print("\n" + "="*50)
print("PROFIT BY REGION")
print("="*50)

query = """
SELECT
Region,
SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Region
ORDER BY Total_Profit DESC;
"""

print(pd.read_sql(query, connection))


connection.close()

print("\nSQL Analysis Completed Successfully!")