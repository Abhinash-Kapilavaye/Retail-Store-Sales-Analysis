import pandas as pd

# 1.Load the Dataset
sales=pd.read_csv("data/retail_sales.csv")

# 2.Display th first five rows

print(sales.head(5))

# 3. check dataset information

sales.info()

# 3. check for missing values

print(sales.isnull().sum())

# 4. check for duplicate records

print(sales.duplicated().sum())

# 5.Display the shape
print(sales.shape)

# 6. Display the column names
print(sales.columns)

# 7. Display the data types of each column
print(sales.dtypes)

# 8. Display the summary statistics of the dataset
print(sales.describe())

# 9. Convert the 'date' column to datetime format
sales["Order_Date"] = pd.to_datetime(sales["Order_Date"])

# 10. create revenue column
sales["Revenue"] = sales["Quantity"] * sales["Unit_Price"]

# 11. find total quantity sold and total revenue
total_quantity_sold = sales["Quantity"].sum()
total_revenue = sales["Revenue"].sum()

print(f"Total Quantity Sold: {total_quantity_sold}")
print(f"Total Revenue: {total_revenue}")

# 12.identify the highest revenue category and region
print(sales.groupby("Category")["Revenue"].sum().idxmax())
print(sales.groupby("Region")["Revenue"].sum().idxmax())

# 13. Extract the month from Order_Date and calculate monthly revenue.
sales["Month"]= sales["Order_Date"].dt.month
print(sales.groupby("Month")["Revenue"].sum())


import matplotlib.pyplot as plt

# graph1: revenue by prooduct

product_revenue=(sales.groupby("Product")["Revenue"].sum().sort_values(ascending=False))
plt.figure(figsize=(8, 5))
product_revenue.plot(kind="bar")

plt.title("Total Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/product_revenue.png", dpi=300)
plt.show()


# Graph 2: Monthly Revenue Trend
monthly_revenue = (
    sales.groupby("Month")["Revenue"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(8, 5))
plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.xticks([1, 2, 3, 4])
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("outputs/monthly_revenue.png", dpi=300)
plt.show()
