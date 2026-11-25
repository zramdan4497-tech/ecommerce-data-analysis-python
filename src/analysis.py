"""Exploratory data analysis of a synthetic e-commerce orders dataset.

Sections:
 1. Load and inspect
 2. Clean and enrich
 3. Revenue trends over time
 4. Category performance
 5. Geography
 6. Acquisition channels
 7. Customer behavior
 8. Discounts and order status
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load and inspect -------------------------------------------------------
df = pd.read_csv("data/ecommerce_orders.csv", parse_dates=["order_date"])
print(df.shape)
print(df.head())
print(df.dtypes)
print(df.isna().sum())

# 2. Clean and enrich -------------------------------------------------------
df["revenue"] = df["quantity"] * df["unit_price"] * (1 - df["discount_pct"] / 100)
df["month"] = df["order_date"].dt.to_period("M").astype(str)
delivered = df[df["order_status"] == "delivered"]

# 3. Revenue trends over time ----------------------------------------------
monthly = delivered.groupby("month")["revenue"].agg(["sum", "count"])
monthly.columns = ["revenue", "orders"]
print(monthly)

ax = monthly["revenue"].plot(kind="line", figsize=(10, 4), title="Monthly delivered revenue")
ax.set_ylabel("Revenue (EGP)")
plt.tight_layout()
plt.savefig("outputs/monthly_revenue.png", dpi=120)

# 4. Category performance ---------------------------------------------------
cat = delivered.groupby("product_category").agg(
    revenue=("revenue", "sum"),
    units=("quantity", "sum"),
    avg_order=("revenue", "mean"),
).sort_values("revenue", ascending=False)
print(cat)

cat["revenue"].plot(kind="bar", figsize=(8, 4), title="Revenue by category")
plt.ylabel("Revenue (EGP)")
plt.tight_layout()
plt.savefig("outputs/category_revenue.png", dpi=120)

# 5. Geography --------------------------------------------------------------
geo = delivered.groupby("country")["revenue"].sum().sort_values(ascending=False)
print(geo)

geo.plot(kind="bar", figsize=(8, 4), title="Revenue by country")
plt.ylabel("Revenue (EGP)")
plt.tight_layout()
plt.savefig("outputs/revenue_by_country.png", dpi=120)

# 6. Acquisition channels ---------------------------------------------------
ch = delivered.groupby("acquisition_channel").agg(
    revenue=("revenue", "sum"), orders=("order_id", "count")
)
ch["avg_order_value"] = ch["revenue"] / ch["orders"]
print(ch.sort_values("revenue", ascending=False))

# 7. Customer behavior ------------------------------------------------------
cust = delivered.groupby("customer_id").agg(
    orders=("order_id", "count"), total_spent=("revenue", "sum")
)
repeat_rate = (cust["orders"] > 1).mean() * 100
print(f"Repeat customer rate: {repeat_rate:.1f}%")
print(f"Average customer lifetime value: {cust['total_spent'].mean():,.0f} EGP")
top10 = cust.sort_values("total_spent", ascending=False).head(10)
print(top10)

# 8. Discounts and order status ---------------------------------------------
print(df.groupby("order_status")["order_id"].count())
disc = delivered.groupby("discount_pct")["revenue"].agg(["sum", "count"])
print(disc)

disc["sum"].plot(kind="bar", figsize=(7, 4), title="Revenue by discount level")
plt.ylabel("Revenue (EGP)")
plt.tight_layout()
plt.savefig("outputs/revenue_by_discount.png", dpi=120)
