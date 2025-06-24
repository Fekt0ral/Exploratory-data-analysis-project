# Exploratory Data Analysis of E-commerce Transactions

This project performs exploratory data analysis (EDA) on a synthetic dataset of e-commerce transactions. The main goals are data cleaning, feature engineering, descriptive statistics, and insightful visualizations.

## Dataset

- **File**: `transactions.csv`
- **Fields**: `transaction_id`, `customer_id`, `gender`, `age`, `country`, `product_category`, `price`, `quantity`, `payment_method`, `transaction_date`

## Key Steps

- Handling missing and incorrect data
- Feature engineering:
  - `total_amount = price * quantity`
  - Extracting transaction month
- Visualizations:
  - Age distribution histogram
  - Total amount boxplot by gender
  - Revenue by country and product category
  - Monthly order and revenue analysis
  - Correlation heatmap between age, quantity, and revenue
  - Payment method distribution (pie chart)
- Saving cleaned dataset and figures

## Output

- `transactions_cleaned.csv` — cleaned dataset
- `age_distribution.png`
- `amount_by_gender.png`
- `amount_by_country.png`
- `top_5_categories.png`
- `orders_by_months.png`
- `age_quantity_revenue.png`
- `payment_methods_distribution.png`

## How to Run

```bash
pip install -r requirements.txt
python main.py
```