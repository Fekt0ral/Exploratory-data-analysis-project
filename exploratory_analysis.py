import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter("ignore", FutureWarning)

# Load .csv file to df
df = pd.DataFrame(pd.read_csv(
    "transactions.csv", 
    parse_dates=["transaction_date"]))

# Check missing values
print("\n=== Data info ===")
missing_data = df.isnull()
for col in missing_data.columns.values.tolist():
    print(missing_data[col].value_counts())
    print("")

# Check incorrect values
print(f"Prices less than 0: {(df['price'] <= 0).sum()}")
print(f"Quantity less than 0: {(df['quantity'] <= 0).sum()}\n")

# Update missing and incorrect values
df["gender"].replace(np.nan, "Unknown", inplace=True)
df["age"].replace(np.nan, df["age"].mean(), inplace=True)
df["age"] = df["age"].astype('int')
df = df[df["price"] > 0]
df = df[df["quantity"] > 0]

# Create new column
df["total_amount"] = df["price"] * df["quantity"]

# Visualize age distribution
plt.figure()
plt.hist(x=df["age"], bins=30, edgecolor='black')
plt.xlabel("Age")
plt.ylabel("Count")
plt.title("Age distribution")
plt.tight_layout()
plt.savefig("age_distribution.png")
plt.close()

# Visualize total_amount by gender
plt.figure()
sns.boxplot(x="gender", y="total_amount", data=df)
plt.xlabel("Gender")
plt.ylabel("Total amount")
plt.title("Total amount distribution by gender")
plt.tight_layout()
plt.savefig("amount_by_gender.png")
plt.close()

# Visualize total_amount by country
plt.figure()
country_total_amount = df.groupby("country")["total_amount"].sum()
plt.bar(country_total_amount.index, country_total_amount.values)
plt.xlabel("Country")
plt.ylabel("Total revenue")
plt.title("Total revenue by country")
plt.tight_layout()
plt.savefig("amount_by_country.png")
plt.close()

# Visualize top-5 most profitale categories
plt.figure()
top_five_categories = df.groupby("product_category")\
    ["price"].sum().sort_values(ascending=False)[:5]
plt.bar(top_five_categories.index, top_five_categories.values)
plt.xlabel("Product category")
plt.ylabel("Total revenue")
plt.title("Top 5 product categories by revenue")
plt.ylim(0, top_five_categories.max() * 1.1)
plt.tight_layout()
plt.savefig("top_5_categories.png")
plt.close()

# Add month column
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

df["month"] = pd.Categorical(
    df["transaction_date"].dt.month.map(dict(zip(range(1, 13), months))),
    categories=months,
    ordered=True
)

# Visualize number of orders by months
plt.figure()
orders_per_month = df.groupby("month").size().reindex(months)
plt.bar(orders_per_month.index, orders_per_month.values)
plt.xlabel("Month")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.title("Months distribution")
plt.tight_layout()
plt.savefig("orders_by_months.png")
plt.close()

# Most profitable and unprofitable months
grouped_months = df.groupby("month")["total_amount"].sum()
print(f"Most profitable month: {grouped_months.idxmax()} - {grouped_months.max()}")
print(f"most unprofitable month: {grouped_months.idxmin()} - {grouped_months.min()}\n")

# Corr between age, quantity, total_amount
corr_group = df[["age", "quantity", "total_amount"]]
corr_grouped = corr_group.groupby(["age", "quantity"], as_index=False).mean()
corr_grouped_pivot = corr_grouped.pivot(index="age", columns="quantity")
corr_grouped_pivot = corr_grouped_pivot.fillna(0)

# Visualize heat map of corr
plt.figure(figsize=(8,7))
sns.heatmap(
    corr_grouped_pivot,
    cmap="YlGnBu", 
    fmt=".2f",
    xticklabels=[1,2,3,4],
    )
plt.title("Revenue heat map between age and quantity")
plt.xlabel("Quantity")
plt.ylabel("Age")
plt.tight_layout()
plt.savefig("age_quantity_revenue.png")
plt.close()

# Pie chart of payment_method
plt.figure()
payment_counts = df["payment_method"].value_counts()
plt.pie(
    payment_counts,
    labels=payment_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    counterclock=False
    )
plt.title("Payment methods distribution")
plt.legend(title="Payment Method", loc="best")
plt.tight_layout()
plt.savefig("payment_methods_distribution.png")
plt.close()

# Save df
df.to_csv("transactions_cleaned.csv")