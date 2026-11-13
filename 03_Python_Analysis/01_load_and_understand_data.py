
# ==========================================
# DA06 - Supermarket Branch Sales Analysis
# Step 1: Load and Understand the Dataset
# ==========================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from pathlib import Path

# Step 1: Locate the cleaned CSV file
project_folder = Path(__file__).resolve().parent.parent

file_path = (
    project_folder
    / "02_Cleaned_dataset"
    / "SuperMarket_Cleaned_data.csv"
)

# Step 2: Load the dataset
df = pd.read_csv(file_path)

print("\nDATASET LOADED SUCCESSFULLY!")

# Step 3: Display first five records
print("\nFIRST FIVE RECORDS:")
print(df.head())

# Step 4: Display last five records
print("\nLAST FIVE RECORDS:")
print(df.tail())

# Step 5: Check dataset dimensions
print("\nDATASET SHAPE:")
print(df.shape)

# Step 6: Check column information
print("\nDATASET INFORMATION:")
df.info()

# Step 7: Statistical summary
print("\nSTATISTICAL SUMMARY:")
print(df.describe())

# Step 8: Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Step 9: Check duplicate records
print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())
