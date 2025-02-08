import pandas as pd

# Load sales data
sales_df = pd.read_csv("data/sales_data.csv")

# Remove missing values
sales_df.dropna(inplace=True)

# Convert Date column to datetime format
sales_df["Date"] = pd.to_datetime(sales_df["Date"])

# Save cleaned data
sales_df.to_csv("data/sales_data_cleaned.csv", index=False)
print("Data cleaning complete!")
