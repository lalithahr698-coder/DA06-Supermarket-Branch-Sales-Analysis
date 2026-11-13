
-- DA06: Supermarket Branch Sales Analysis
-- SQL Analysis Queries

-- Query 1: Total Sales
SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM supermarket_sales;


-- Query 2: Sales by Branch
SELECT
    Branch,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM supermarket_sales
GROUP BY Branch
ORDER BY Total_Sales DESC;


-- Query 3: Sales by City
SELECT
    City,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM supermarket_sales
GROUP BY City
ORDER BY Total_Sales DESC;


-- Query 4: Sales by Product Line
SELECT
    `Product line`,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM supermarket_sales
GROUP BY `Product line`
ORDER BY Total_Sales DESC;


-- Query 5: Sales by Customer Type
SELECT
    `Customer type`,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    COUNT(*) AS Total_Transactions
FROM supermarket_sales
GROUP BY `Customer type`
ORDER BY Total_Sales DESC;


-- Query 6: Payment Method Count
SELECT
    Payment,
    COUNT(*) AS Total_Transactions
FROM supermarket_sales
GROUP BY Payment
ORDER BY Total_Transactions DESC;


-- Query 7: Average Rating by Product Line
SELECT
    `Product line`,
    ROUND(AVG(Rating), 2) AS Average_Rating
FROM supermarket_sales
GROUP BY `Product line`
ORDER BY Average_Rating DESC;


-- Query 8: Quantity Sold by Product Line
SELECT
    `Product line`,
    SUM(Quantity) AS Total_Quantity
FROM supermarket_sales
GROUP BY `Product line`
ORDER BY Total_Quantity DESC;
