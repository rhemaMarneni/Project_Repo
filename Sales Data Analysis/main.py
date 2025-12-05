from src.analysis import (
    total_sales,
    sales_by_country,
    sales_by_product,
    sales_by_year,
    average_sales_per_order_line,
    top_product_by_sales,
    large_orders,
    total_orders,
    total_customers,
    total_products,
    filter_by_status,
    sort_products_by_sales,
    sort_countries_by_avg,
    sort_products_by_quantity,
)
from pathlib import Path
import pandas as pd


def main():
    csv_path = Path("data/sales_data_sample.csv")

    # Read the CSV file using pandas
    df = pd.read_csv(csv_path, encoding='latin-1')

    print("Sales Data Analysis")
    print("===================")

    format_currency = lambda x: f"{x:,.2f}"
    format_item = lambda item: print(f"  {item[0]}: {format_currency(item[1])}")
    get_count = lambda df: df.shape[0]
    get_total_sales = lambda df: df['SALES'].sum()

    print("Data Summary:")

    avg_sales = average_sales_per_order_line(df)
    large_orders_df = large_orders(df, avg_sales)

    print(f"Total SALES: {format_currency(total_sales(df))}")
    print(f"Total customers: {total_customers(df)}")
    print(f"Total orders: {total_orders(df)}")
    print(f"Total products: {total_products(df)}")
    print(f"Average SALES per order line: {format_currency(avg_sales)}")
    print(f"Large orders: {get_count(large_orders_df)}")


    print("\nSales by country:")
    list(map(format_item, sales_by_country(df).items()))

    print("\nSales by product:")
    list(map(format_item, sales_by_product(df).items()))

    print("\nSales by year:")
    list(map(format_item, sales_by_year(df).items()))

    top_products = top_product_by_sales(df)
    print(f"\nTop products by sales:")
    list(map(format_item, top_products.items()))

    print("\nFiltering by status:")
    shipped_filtered_df = filter_by_status(df, "Shipped")
    cancelled_filtered_df = filter_by_status(df, "Cancelled")
    print(f"  Shipped orders: {get_count(shipped_filtered_df)}")
    print(f"  Cancelled orders: {get_count(cancelled_filtered_df)}")
    print(f"  Total sales for shipped orders: {format_currency(get_total_sales(shipped_filtered_df))}")
    print(f"  Total sales for cancelled orders: {format_currency(get_total_sales(cancelled_filtered_df))}")

    print("\nTop 5 products by sales:")
    list(map(format_item, sort_products_by_sales(df).head(5).items()))

    print("\nBest product:")
    best_product = sort_products_by_sales(df).head(1)
    get_best = lambda s: (s.index[0], s.iloc[0])
    product, total = get_best(best_product)
    print(f"  {product}: {format_currency(total)}")

    print("\nTop 5 countries by average sales:")
    list(map(format_item, sort_countries_by_avg(df).head(5).items()))

    print("\nTop 5 most ordered products by quantity:")
    list(map(format_item, sort_products_by_quantity(df).head(5).items()))

if __name__ == "__main__":
    main()