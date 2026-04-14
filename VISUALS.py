import pandas as pd
import matplotlib.pyplot as plt
# 1. LOAD DATASET
df = pd.read_csv("DATA_SET.csv")
# ======== BAR CHART : TOP CITIES BY TOTAL SALES =========
# 1. Calculate total sales for each city
city_sales = df.groupby("City")["Sales"].sum()
# 2. Select the Top 10 cities
top_cities = city_sales.sort_values(ascending=False).head(10)
# 3. Create bar chart
plt.figure(figsize=(11, 6))
plt.bar(top_cities.index, top_cities.values, color="cornflowerblue")
# 4. Add title and labels
plt.title("Top 10 Cities by Total Sales", fontsize=14, fontweight="bold")
plt.xlabel("City")
plt.ylabel("Total Sales")
# 5. Improve readability
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.6)
# 6. Show plot
plt.show()

# ======== LINE PLOT : SALES TREND OVER TIME =====
# 1. Convert Order Date to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
# 2. Remove rows with invalid dates
df = df.dropna(subset=["Order Date"])
# 3. Calculate total sales per date
daily_sales = df.groupby("Order Date")["Sales"].sum()
# 4. Create line plot
plt.figure(figsize=(12, 5))
plt.plot(
    daily_sales.index,
    daily_sales.values,
    color="green",
    linestyle="-",
    linewidth=2,
    marker="o",
    markersize=4)
# 5. Add title and labels
plt.title("Sales Trend Over Time", fontsize=14, fontweight="bold")
plt.xlabel("Order Date")
plt.ylabel("Total Sales")
# 6. Improve readability
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)
# 7. Show plot
plt.show()
# ======== SCATTER PLOT : DISCOUNT VS SALES ================
# 1. Create scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(
    df["Discount"],
    df["Sales"],
    color="purple",
    alpha=0.5)
# 2. Add title and labels
plt.title("Relationship Between Discount and Sales", fontsize=14, fontweight="bold")
plt.xlabel("Discount")
plt.ylabel("Sales")
# 3. Add grid
plt.grid(True, linestyle="--", alpha=0.5)
# 4. Show plot
plt.show()
# ======== PIE CHART : SALES BY CUSTOMER SEGMENT ===========
# 1. Calculate total sales per customer segment
segment_sales = df.groupby("Segment")["Sales"].sum()
# 2. Define colors and explode effect
colors = ["gold", "lightskyblue", "lightcoral"]
explode = [0.05] * len(segment_sales)
# 3. Create pie chart
plt.figure(figsize=(7, 7))
plt.pie(
    segment_sales,
    labels=segment_sales.index,
    autopct="%1.1f%%",
    startangle=90,
    colors=colors,
    explode=explode,
    shadow=True,
    textprops={"fontsize": 11})
# 4. Add title and legend
plt.title("Sales Distribution by Customer Segment", fontsize=14, fontweight="bold")
plt.legend(title="Customer Segment")
# 5. Show plot
plt.show()
