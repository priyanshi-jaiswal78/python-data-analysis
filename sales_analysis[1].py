import pandas as pd
import numpy as np

# Load the sample sales dataset
df = pd.read_csv("sales_data.csv")

# Calculate total sales for each transaction
df["total_sales"] = df["quantity"] * df["unit_price"]

print("\n--- Sales Data ---")
print(df)

print("\n--- Summary ---")
print(f"Total revenue: ₹{df['total_sales'].sum():,.0f}")
print(f"Total units sold: {df['quantity'].sum():,}")
print(f"Average transaction value: ₹{df['total_sales'].mean():,.0f}")

# Revenue by product
product_sales = (
    df.groupby("product")["total_sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n--- Revenue by Product ---")
print(product_sales)

# Revenue by category
category_sales = (
    df.groupby("category")["total_sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\n--- Revenue by Category ---")
print(category_sales)

# NumPy calculation
sales_values = df["total_sales"].to_numpy()
print("\n--- NumPy Check ---")
print(f"Maximum transaction: ₹{np.max(sales_values):,.0f}")
print(f"Minimum transaction: ₹{np.min(sales_values):,.0f}")
