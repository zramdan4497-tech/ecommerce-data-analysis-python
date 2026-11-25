# E-commerce Data Analysis with Python

An end-to-end exploratory data analysis of e-commerce orders using Python, Pandas, NumPy, and Matplotlib: cleaning, enrichment, trends, category and geography performance, acquisition channels, customer behavior, and discount impact.

## Dataset
`data/ecommerce_orders.csv` - 2,000 synthetic orders with dates, customers, countries, acquisition channels, categories, quantities, prices, discounts, order status, and payment methods. The data is generated for demonstration; no real customer data is used.

## Questions the analysis answers
- How does delivered revenue trend month over month?
- Which product categories drive revenue and volume?
- Which countries and cities order the most?
- Which acquisition channels bring the most valuable orders?
- What share of customers come back, and what is an average customer worth?
- How do discounts relate to revenue, and what share of orders get cancelled or returned?

## Repository contents
| Path | What it is |
|---|---|
| `data/ecommerce_orders.csv` | The synthetic orders dataset |
| `notebooks/ecommerce_eda.ipynb` | The full analysis as a Jupyter notebook with commentary |
| `src/analysis.py` | The same analysis as a plain Python script |
| `requirements.txt` | Python dependencies |

## How to run
```bash
pip install -r requirements.txt
python src/analysis.py          # prints the tables and saves charts to an outputs/ folder
# or open the notebook
jupyter notebook notebooks/ecommerce_eda.ipynb
```

## Key findings
- Revenue is broadly stable with seasonal peaks; Electronics leads category revenue, followed by Furniture and Appliances
- Egypt brings the majority of orders, with meaningful volume from Saudi Arabia and the UAE
- Social Media and Organic Search bring the most delivered revenue
- About two thirds of customers are repeat buyers, and a repeat customer spends roughly 4x a one-time customer
- Undiscounted orders drive most delivered revenue, with discounted orders (5-15%) adding a smaller share; cancelled and returned orders together are about a quarter of all orders, a rate worth reducing

## Skills demonstrated
- Data cleaning and feature engineering with Pandas
- Group-by aggregation, pivot-style summaries, and derived metrics
- Data visualization with Matplotlib
- Turning raw order data into business findings
