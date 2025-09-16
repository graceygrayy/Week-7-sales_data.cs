import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv("sales_data.csv")

# Total revenue
total_revenue = data["Revenue ($)"].sum()

# Best-selling product
best_product = data.groupby("Product")["Quantity Sold"].sum().idxmax()
best_quantity = data.groupby("Product")["Quantity Sold"].sum().max()

# Day with highest sales
best_day = data.groupby("Date")["Revenue ($)"].sum().idxmax()
best_day_revenue = data.groupby("Date")["Revenue ($)"].sum().max()

# Save results to a text file
with open("sales_summary.txt", "w") as f:
    f.write(f"Total Revenue: ${total_revenue}\n")
    f.write(f"Best-Selling Product: {best_product} ({best_quantity} units sold)\n")
    f.write(f"Highest Sales Day: {best_day} (${best_day_revenue})\n")

# Print results in terminal
print("✅ Analysis Complete! Results saved in sales_summary.txt")

# Bonus: visualize sales trend
data.groupby("Date")["Revenue ($)"].sum().plot(kind="bar", title="Revenue by Date")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.show()

import matplotlib.pyplot as plt

# 1. Line Chart: Revenue over time
plt.figure(figsize=(6,4))
df.groupby("Date")["Revenue"].sum().plot(kind="line", marker="o")
plt.title("Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Total Revenue ($)")
plt.show()

# 2. Bar Chart: Average revenue per product
plt.figure(figsize=(6,4))
df.groupby("Product")["Revenue"].mean().plot(kind="bar", color="skyblue")
plt.title("Average Revenue per Product")
plt.xlabel("Product")
plt.ylabel("Average Revenue ($)")
plt.show()

# 3. Histogram: Distribution of Quantity
plt.figure(figsize=(6,4))
df["Quantity"].plot(kind="hist", bins=10, color="lightgreen", edgecolor="black")
plt.title("Distribution of Quantity Sold")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot: Quantity vs Revenue
plt.figure(figsize=(6,4))
plt.scatter(df["Quantity"], df["Revenue"], color="orange")
plt.title("Quantity vs Revenue")
plt.xlabel("Quantity Sold")
plt.ylabel("Revenue ($)")
plt.show()

# Save results to a text file
with open("sales_summary.txt", "w") as f:
    f.write(f"Total Revenue: {total_revenue}\n")
    f.write(f"Best-Selling Product: {best_product} ({best_quantity} units sold)\n")
    f.write(f"Highest Sales Day: {best_day} (${best_day_revenue})\n")

# ---- STEP 2: Visualizations ----
import matplotlib.pyplot as plt

# Bar chart: total revenue by product
product_revenue = data.groupby("Product")["Revenue ($)"].sum()
product_revenue.plot(kind="bar", title="Revenue by Product")
plt.ylabel("Revenue ($)")
plt.savefig("product_revenue_chart.png")   # saves chart as PNG
plt.close()

# Line chart: revenue over time
daily_revenue = data.groupby("Date")["Revenue ($)"].sum()
daily_revenue.plot(kind="line", marker="o", title="Revenue Over Time")
plt.ylabel("Revenue ($)")
plt.savefig("daily_revenue_chart.png")   # saves chart as PNG
plt.close()

# Print results in terminal
print("✅ Analysis Complete! Results saved in sales_summary.txt")
