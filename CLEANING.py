import pandas as pd
# 1. LOAD DATA
df = pd.read_csv("DATA_SET.csv")
# 2. INSPECT THE DATASET
print("Dataset Description:")
print(df.describe(include="all"))
print("First 10 rows:")
print(df.head(10))
print("Last 10 rows:")
print(df.tail(10))
print("Column Names and Data Types:")
print(df.dtypes)
print("Missing Values Per Column:")
print(df.isnull().sum())
# 3. HANDLE WRONG DATA TYPE
# Convert Quantity to numeric (invalid values become NaN)
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
# 4. SUMMARY STATISTICS
# Quantity sum
quantity_sum = df["Quantity"].sum()
# Sales MEAN, MAX, MIN
sales_mean = df["Sales"].mean()
sales_max = df["Sales"].max()
sales_min = df["Sales"].min()
print("Summary Statistics:")
print(f"Total Quantity (sum): {quantity_sum}")
print(f"Sales Mean: {sales_mean}")
print(f"Sales Max: {sales_max}")
print(f"Sales Min: {sales_min}")
# 5. HANDLE MISSING DATA
# Removing rows that contain any missing values
df_dropna = df.dropna()
# Filling missing values (example: fill numeric columns with 0)
df_filled = df.fillna(0)
print("After Dropping Rows with Missing Values:")
print(df_dropna.isna().sum())
print("After Filling Missing Values with 0:")
print(df_filled.isna().sum())
# 6. FILTERING DATA
# Quantity > 10
quantity_10 = df[df["Quantity"] > 10]
print("Quantity > 10:")
print(quantity_10)
# 7. GROUP BY DATA
# Mean Sales for each City
each_city_average_sales = df.groupby("City")["Sales"].mean()
# Total Profit for each City
each_city_profit_sum= df.groupby("City")["Profit"].sum()
print("Each city average sales:")
print(each_city_average_sales)
print("Each city profit sum:")
print(each_city_profit_sum)