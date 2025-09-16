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
