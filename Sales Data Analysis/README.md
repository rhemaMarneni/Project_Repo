# Sales Data Analysis

Analyzing sales data using pandas and functional programming concepts including lambda functions and stream operations.

**Data Source:** https://www.kaggle.com/datasets/kyanyoga/sample-sales-data

#### Aggregate Functions
- `total_sales(df)` - Calculate the total sales across all orders
- `sales_by_country(df)` - Calculate total sales grouped by country
- `sales_by_product(df)` - Calculate total sales grouped by product line
- `sales_by_year(df)` - Calculate total sales grouped by year
- `average_sales_per_order_line(df)` - Calculate the average sales amount per order line
- `top_product_by_sales(df)` - Get the top 10 product lines by total sales
- `large_orders(df, threshold)` - Filter orders where sales exceed the specified threshold

#### Counting Functions
- `total_orders(df)` - Count the total number of unique orders
- `total_customers(df)` - Count the total number of unique customers
- `total_products(df)` - Count the total number of unique products

#### Filtering Functions
- `filter_by_status(df, status)` - Filter orders by their status (e.g., 'Shipped', 'Cancelled')

#### Sorting Functions
- `sort_products_by_sales(df)` - Sort products by total sales in descending order
- `sort_countries_by_avg(df)` - Sort countries by average sales per order in descending order
- `sort_products_by_quantity(df)` - Sort products by total quantity ordered in descending order

## Tools/Languages Used

- Python 3.7+
- pandas

## Installation

```bash
pip install pandas
```

## Usage

Run the main script to perform the analysis:

```bash
python main.py
```

## To Run Unit Tests

```bash
python -m pytest tests/test_analysis.py -v
```

## Example Output

Sales Data Analysis
===================
Data Summary:
Total SALES: 10,032,628.85
Total customers: 92
Total orders: 307
Total products: 109
Average SALES per order line: 3,553.89
Large orders: 1168

Sales by country:
  Australia: 630,623.10
  Austria: 202,062.53
  Belgium: 108,412.62
  Canada: 224,078.56
  Denmark: 245,637.15
  Finland: 329,581.91
  France: 1,110,916.52
  Germany: 220,472.09
  Ireland: 57,756.43
  Italy: 374,674.31
  Japan: 188,167.81
  Norway: 307,463.70
  Philippines: 94,015.73
  Singapore: 288,488.41
  Spain: 1,215,686.92
  Sweden: 210,014.21
  Switzerland: 117,713.56
  UK: 478,880.46
  USA: 3,627,982.83

Sales by product:
  Classic Cars: 3,919,615.66
  Motorcycles: 1,166,388.34
  Planes: 975,003.57
  Ships: 714,437.13
  Trains: 226,243.47
  Trucks and Buses: 1,127,789.84
  Vintage Cars: 1,903,150.84

Sales by year:
  2003: 3,516,979.54
  2004: 4,724,162.60
  2005: 1,791,486.71

Top products by sales:
  Classic Cars: 3,919,615.66
  Vintage Cars: 1,903,150.84
  Motorcycles: 1,166,388.34
  Trucks and Buses: 1,127,789.84
  Planes: 975,003.57
  Ships: 714,437.13
  Trains: 226,243.47

Filtering by status:
  Shipped orders: 2617
  Cancelled orders: 60
  Total sales for shipped orders: 9,291,501.08
  Total sales for cancelled orders: 194,487.48

Top 5 products by sales:
  S18_3232: 288,245.42
  S10_1949: 191,073.03
  S10_4698: 170,401.07
  S12_1108: 168,585.32
  S18_2238: 154,623.95

Best product:
  S18_3232: 288,245.42

Top 5 countries by average sales:
  Denmark: 3,899.00
  Switzerland: 3,797.21
  Sweden: 3,684.46
  Austria: 3,673.86
  Singapore: 3,651.75

Top 5 most ordered products by quantity:
  S18_3232: 1,774.00
  S24_3856: 1,052.00
  S18_4600: 1,031.00
  S700_4002: 1,029.00
  S12_4473: 1,024.00
