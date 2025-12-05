# Sales Data Analysis

Analyzing sales data using pandas and functional programming concepts including lambda functions and stream operations.

**Data Source:** https://www.kaggle.com/datasets/kyanyoga/sample-sales-data
I chose this dataset because the data is representative of the common factors used for sales analysis.

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

## Languages/Libraries Used

- Python 3.7+
- pandas

## Installation

```bash
pip install pandas
```

## To run project

```bash
python main.py
```

## To Run All Unit Tests

```bash
python -m pytest tests/test_analysis.py -v
```

```
## Example Output

```
============== DATA SUMMARY ==============

Total Sales: $10,032,628.85
Total customers: 92
Total orders: 307
Total products: 7
Average Sales per order line: $3,553.89
Large orders (above 75th percentile): 705

============== SALES ANALYSIS BY COUNTRY ==============


Overall Sales:
  Australia: $630,623.10
  Austria: $202,062.53
  Belgium: $108,412.62
  Canada: $224,078.56
  Denmark: $245,637.15
  Finland: $329,581.91
  France: $1,110,916.52
  Germany: $220,472.09
  Ireland: $57,756.43
  Italy: $374,674.31
  Japan: $188,167.81
  Norway: $307,463.70
  Philippines: $94,015.73
  Singapore: $288,488.41
  Spain: $1,215,686.92
  Sweden: $210,014.21
  Switzerland: $117,713.56
  UK: $478,880.46
  USA: $3,627,982.83

Top 5 performing countries:
  USA: $3,627,982.83
  Spain: $1,215,686.92
  France: $1,110,916.52
  Australia: $630,623.10
  UK: $478,880.46

Bottom 5 performing countries:
  Japan: $188,167.81
  Switzerland: $117,713.56
  Belgium: $108,412.62
  Philippines: $94,015.73
  Ireland: $57,756.43

============== SALES ANALYSIS BY PRODUCTLINE ==============

Product Category Sales:
  Classic Cars: $3,919,615.66
  Motorcycles: $1,166,388.34
  Planes: $975,003.57
  Ships: $714,437.13
  Trains: $226,243.47
  Trucks and Buses: $1,127,789.84
  Vintage Cars: $1,903,150.84

Quantities sold:
  Classic Cars: $33,992.00
  Vintage Cars: $21,069.00
  Motorcycles: $11,663.00
  Trucks and Buses: $10,777.00
  Planes: $10,727.00
  Ships: $8,127.00
  Trains: $2,712.00

Best Selling product:
  Classic Cars: making $3,919,615.66 in sales

Worst Selling product:
  Trains: making $226,243.47 in sales

============== YEARLY ANALYSIS ==============

Sales by year:
  2003: $3,516,979.54
  2004: $4,724,162.60
  2005: $1,791,486.71

Quarterly analysis for each year:
YEAR_ID  QTR_ID
2003     1          445094.69
         2          562365.22
         3          649514.54
         4         1860005.09
2004     1          833730.68
         2          766260.73
         3         1109396.27
         4         2014774.92
2005     1         1071992.36
         2          719494.35
Name: SALES, dtype: float64

Best quarter for each year:
  2003: 4
  2004: 4
  2005: 1

Worst quarter for each year:
  2003: 1
  2004: 2
  2005: 2

============== FILTERING BY STATUS ==============

  Shipped orders: 2617
  Cancelled orders: 60
  Total sales for shipped orders: 9,291,501.08
  Lost revenue from cancelled orders: 194,487.48

============== CUSTOMER LEVEL ANALYSIS ==============

Most frequent customers:
  AV Stores, Co.: $157,807.81
  Alpha Cognac: $70,488.44
  Amica Models & Co.: $94,117.26
  Anna's Decorations, Ltd: $153,996.13
  Atelier graphique: $24,179.96

Least frequent customers:
  Vida Sport, Ltd: $117,713.56
  Vitachrome Inc.: $88,041.26
  Volvo Model Replicas, Co: $75,754.88
  West Coast Collectables Co.: $46,084.64
  giftsbymail.co.uk: $78,240.84
```
