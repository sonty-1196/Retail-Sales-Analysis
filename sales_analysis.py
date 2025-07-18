import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Sample - Superstore.csv" , encoding = 'latin1')
df.head() # this shows the dataset in tabular format.

df.isnull().sum() # this finds for missing values
df.duplicated() # search for duplicate columns-rows

print(df.columns)

region_sales = df.groupby("Region")['Sales'].sum().sort_values(ascending = False) # group data between Region and Sales
print(region_sales)

top_products = df.groupby("Product Name")['Sales'].sum().sort_values(ascending = False).head(5) # group data between Sales and Product
print(region_sales)
print(top_products)

region_sales.plot(kind = 'bar' , figsize = (10 , 5) , color = 'skyblue')

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation = 45)
plt.show()

top_products.plot(kind = 'bar' , figsize = (10,6) , color = 'gold')

plt.title("Top 5 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")
plt.show()

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = df.groupby(df['Order Date'].dt.to_period("M"))['Sales'].sum() # converts the date order to year-month format
print(monthly_sales)

# Graph plot for Monthly aggregation / trends
monthly_sales.plot(kind = "line" , figsize = (8,6) , color = "green")

plt.title("Monthly Sales Trend")
plt.xlabel("Monthly-Year Sales")
plt.ylabel("Total Sales")
plt.show()         

category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending = False)
print(category_sales)

category_sales.plot(kind = 'bar' , figsize = (6,5) , color = 'blue')

plt.title("Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.show()

segment_sales = df.groupby("Segment")['Sales'].sum().sort_values(ascending = False)
print(segment_sales)

segment_sales.plot(kind = 'bar', figsize = (7 , 5) , color = "green")

plt.title("Sales by Customer Segment")
plt.xlabel("Customer Type")
plt.ylabel("Total Sales")
plt.show()


shipmode_sales = df.groupby('Ship Mode')['Sales'].sum().sort_values(ascending=False)
print(shipmode_sales)

shipmode_sales.plot(kind='bar', color='orange', figsize=(8,5), title='Total Sales by Ship Mode')

plt.xlabel('Ship Mode')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()

# Create pivot table: rows = Region, columns = Category, values = Total Sales(sum)
pivot_sales = pd.pivot_table(df, values='Sales', index='Region', columns='Category', aggfunc='sum', fill_value=0)
print(pivot_sales)

pivot_sales.plot(kind='bar', figsize=(10,6) )
plt.title("Sales by Region and Category")

plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.legend(title='Category') # helps to understand which bar belongs to which category(product type).
plt.show()

# identifying key customers contributing to most revenue

top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending = False).head(5)
print(top_customers)

top_customers.plot(kind = "bar" , figsize = (6,5) , color = "blue")

plt.title("Top 5 customers by Sales")
plt.xlabel("Customer Name")
plt.ylabel("Total Sales Contribution")
plt.xticks(rotation = 45)
plt.show() # chart reflects Sean Miller contributes the most in revenue


