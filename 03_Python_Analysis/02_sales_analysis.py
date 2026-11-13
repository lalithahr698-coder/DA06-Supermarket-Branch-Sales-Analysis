
import pandas as pd
from pathlib import Path

# Load cleaned dataset
project_folder = Path(__file__).resolve().parent.parent

file_path = project_folder / "02_Cleaned_dataset" / "SuperMarket_cleaned_data.csv"

df = pd.read_csv(file_path)

print("\n========== SUPERMARKET SALES ANALYSIS ==========")

# 1. Total sales
print("\n1. TOTAL SALES:")
print(round(df["Sales"].sum(), 2))

# 2. Sales by branch
print("\n2. SALES BY BRANCH:")
branch_sales = df.groupby("Branch")["Sales"].sum().sort_values(ascending=False)
print(branch_sales.round(2))

# 3. Sales by city
print("\n3. SALES BY CITY:")
city_sales = df.groupby("City")["Sales"].sum().sort_values(ascending=False)
print(city_sales.round(2))

# 4. Sales by product line
print("\n4. SALES BY PRODUCT LINE:")
product_sales = df.groupby("Product line")["Sales"].sum().sort_values(ascending=False)
print(product_sales.round(2))

# 5. Sales by customer type
print("\n5. SALES BY CUSTOMER TYPE:")
customer_sales = df.groupby("Customer type")["Sales"].sum().sort_values(ascending=False)
print(customer_sales.round(2))

# 6. Payment method count
print("\n6. PAYMENT METHOD COUNT:")
payment_count = df["Payment"].value_counts()
print(payment_count)

# 7. Average customer rating by product line
print("\n7. AVERAGE RATING BY PRODUCT LINE:")
rating_analysis = df.groupby("Product line")["Rating"].mean().sort_values(ascending=False)
print(rating_analysis.round(2))

# 8. Quantity sold by product line
print("\n8. QUANTITY SOLD BY PRODUCT LINE:")
quantity_analysis = df.groupby("Product line")["Quantity"].sum().sort_values(ascending=False)
print(quantity_analysis)

print("\n========== ANALYSIS COMPLETED ==========")
