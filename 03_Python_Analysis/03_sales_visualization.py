
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load cleaned dataset
project_folder = Path(__file__).resolve().parent.parent

file_path = project_folder / "02_Cleaned_dataset" / "SuperMarket_cleaned_data.csv"

df = pd.read_csv(file_path)

# Create charts folder if it does not exist
charts_folder = project_folder / "06_Charts"
charts_folder.mkdir(exist_ok=True)

# Set chart style
sns.set_theme(style="whitegrid")

# 1. Sales by Branch
branch_sales = df.groupby("Branch")["Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(x=branch_sales.index, y=branch_sales.values)
plt.title("Total Sales by Branch")
plt.xlabel("Branch")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(charts_folder / "01_sales_by_branch.png")
plt.close()

# 2. Sales by Product Line
product_sales = df.groupby("Product line")["Sales"].sum().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=product_sales.values, y=product_sales.index)
plt.title("Total Sales by Product Line")
plt.xlabel("Total Sales")
plt.ylabel("Product Line")
plt.tight_layout()
plt.savefig(charts_folder / "02_sales_by_product_line.png")
plt.close()

# 3. Sales by Customer Type
customer_sales = df.groupby("Customer type")["Sales"].sum()

plt.figure(figsize=(7, 5))
sns.barplot(x=customer_sales.index, y=customer_sales.values)
plt.title("Total Sales by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(charts_folder / "03_sales_by_customer_type.png")
plt.close()

# 4. Payment Method Count
payment_count = df["Payment"].value_counts()

plt.figure(figsize=(7, 5))
sns.barplot(x=payment_count.index, y=payment_count.values)
plt.title("Transactions by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.savefig(charts_folder / "04_payment_method.png")
plt.close()

# 5. Quantity Sold by Product Line
quantity_sales = df.groupby("Product line")["Quantity"].sum().sort_values()

plt.figure(figsize=(10, 6))
sns.barplot(x=quantity_sales.values, y=quantity_sales.index)
plt.title("Quantity Sold by Product Line")
plt.xlabel("Total Quantity Sold")
plt.ylabel("Product Line")
plt.tight_layout()
plt.savefig(charts_folder / "05_quantity_by_product_line.png")
plt.close()

print("ALL CHARTS CREATED SUCCESSFULLY!")

print("\nCharts saved in:")
print(charts_folder)

print("\nCreated 5 charts:")
print("1. Sales by Branch")
print("2. Sales by Product Line")
print("3. Sales by Customer Type")
print("4. Payment Method")
print("5. Quantity by Product Line")
