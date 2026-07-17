-- 1. Total Sales

SELECT 
SUM(Sales) AS Total_Sales
FROM superstore;


-- 2. Total Profit

SELECT
SUM(Profit) AS Total_Profit
FROM superstore;


-- 3. Total Orders

SELECT
COUNT(*) AS Total_Orders
FROM superstore;


-- 4. Sales by Category

SELECT
Category,
SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category
ORDER BY Total_Sales DESC;


-- 5. Profit by Region

SELECT
Region,
SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Region
ORDER BY Total_Profit DESC;


-- 6. Top 10 Sub-Categories

SELECT
"Sub-Category",
SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY "Sub-Category"
ORDER BY Total_Sales DESC
LIMIT 10;


-- 7. Sales by Segment

SELECT
Segment,
SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Segment
ORDER BY Total_Sales DESC;