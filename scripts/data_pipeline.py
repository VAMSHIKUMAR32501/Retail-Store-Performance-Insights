import pandas as pd

# Load datasets
sales_df = pd.read_csv("data/sales_data.csv")
customer_df = pd.read_csv("data/customer_data.csv")
store_df = pd.read_csv("data/store_data.csv")

# Merge datasets
merged_df = sales_df.merge(customer_df, left_on="Store_ID", right_on="Customer_ID")

# Save merged data
merged_df.to_csv("data/merged_data.csv", index=False)
print("Data pipeline execution complete!")
