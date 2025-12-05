"""Analysis categories functions for sales data."""

from src.analysis_utils import (
    total_sales,
    sales_by_country,
    sales_by_product,
    sales_by_year,
    sales_by_year_and_quarter,
    best_quarter_each_year,
    worst_quarter_each_year,
    average_sales_per_order_line,
    large_orders,
    total_orders,
    total_customers,
    total_products,
    filter_by_status,
    sort_products_by_sales,
    sort_countries_by_sales,
    sort_products_by_quantity,
    sales_by_customer,
)

from src.utils import (
    format_currency,
    format_currency_item,
    get_count,
    format_item,
    get_percentile,
)


def overall_analysis(df):
    """Overall analysis of the sales data."""
    print("============== DATA SUMMARY ==============\n")

    avg_sales = average_sales_per_order_line(df)
    percentile_75 = get_percentile(df, "SALES", 0.75)
    large_orders_df = large_orders(df, percentile_75)

    print(f"Total Sales: ${format_currency(total_sales(df))}")
    print(f"Total customers: {total_customers(df)}")
    print(f"Total orders: {total_orders(df)}")
    print(f"Total products: {total_products(df)}")
    print(f"Average Sales per order line: ${format_currency(avg_sales)}")
    print(f"Large orders (above 75th percentile): {len(large_orders_df)}")


def country_level_analysis(df):
    """Analysis of the sales data by country."""
    print("\n============== SALES ANALYSIS BY COUNTRY ==============\n")
    print("\nOverall Sales:")
    list(map(format_currency_item, sales_by_country(df).items()))

    print("\nTop 5 performing countries:")
    list(map(format_currency_item, sort_countries_by_sales(df).head(5).items()))

    print("\nBottom 5 performing countries:")
    list(map(format_currency_item, sort_countries_by_sales(df).tail(5).items()))

def product_level_analysis(df):
    """Analysis of the sales data by product line."""
    print("\n============== SALES ANALYSIS BY PRODUCTLINE ==============\n")
    print("Product Category Sales:")
    list(map(format_currency_item, sales_by_product(df).items()))

    print("\nQuantities sold:")
    list(map(format_currency_item, sort_products_by_quantity(df).items()))

    product_performance = sort_products_by_sales(df).head(1)
    print("\nBest Selling product:")
    get_best = lambda s: (s.index[0], s.iloc[0])
    best_product, best_total = get_best(product_performance)
    print(f"  {best_product}: making ${format_currency(best_total)} in sales")

    print("\nWorst Selling product:")
    get_worst = lambda s: (s.index[-1], s.iloc[-1])
    worst_product, worst_total = get_worst(sort_products_by_sales(df).tail(1))
    print(f"  {worst_product}: making ${format_currency(worst_total)} in sales")

def yearly_analysis(df):
    """Analysis of the sales data by year."""
    print("\n============== YEARLY ANALYSIS ==============\n")
    print("Sales by year:")
    list(map(format_currency_item, sales_by_year(df).items()))

    print("\nQuarterly analysis for each year:")
    quarterly_analysis = sales_by_year_and_quarter(df)
    print(quarterly_analysis)


    print("\nBest quarter for each year:")
    list(map(format_item, best_quarter_each_year(df).items()))

    print("\nWorst quarter for each year:")
    list(map(format_item, worst_quarter_each_year(df).items()))

def order_status_analysis(df):
    """Analysis of the sales data by order status."""
    print("\n============== FILTERING BY STATUS ==============\n")
    shipped_filtered_df = filter_by_status(df, "Shipped")
    cancelled_filtered_df = filter_by_status(df, "Cancelled")
    print(f"  Shipped orders: {get_count(shipped_filtered_df)}")
    print(f"  Cancelled orders: {get_count(cancelled_filtered_df)}")
    print(f"  Total sales for shipped orders: {format_currency(total_sales(shipped_filtered_df))}")
    print(f"  Lost revenue from cancelled orders: {format_currency(total_sales(cancelled_filtered_df))}")


def customer_level_analysis(df):
    """Analysis of the sales data by customer level."""
    print("\n============== CUSTOMER LEVEL ANALYSIS ==============\n")

    print("Most frequent customers:")
    list(map(format_currency_item, sales_by_customer(df).head(5).items()))

    print("\nLeast frequent customers:")
    list(map(format_currency_item, sales_by_customer(df).tail(5).items()))
