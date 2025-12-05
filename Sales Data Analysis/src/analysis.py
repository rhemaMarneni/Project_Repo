def total_sales(df):
    """
    Calculate the total sales across all orders.
    """
    return df['SALES'].sum()


def sales_by_country(df):
    """
    Calculate total sales grouped by country.
    """
    return df.groupby('COUNTRY')['SALES'].sum()


def sales_by_product(df):
    """
    Calculate total sales grouped by product line.
    """
    return df.groupby('PRODUCTLINE')['SALES'].sum()


def sales_by_year(df):
    """
    Calculate total sales grouped by year.
    """
    return df.groupby('YEAR_ID')['SALES'].sum()


def average_sales_per_order_line(df):
    """
    Calculate the average sales amount per order line.
    """
    return df['SALES'].mean()


def top_product_by_sales(df):
    """
    Get the top 10 product lines by total sales.
    """
    return df.groupby('PRODUCTLINE')['SALES'].sum().nlargest(10)


def large_orders(df, threshold):
    """
    Filter orders where sales exceed the specified threshold.
    """
    return df[df['SALES'] > threshold]


def total_orders(df):
    """
    Count the total number of unique orders.
    """
    return df['ORDERNUMBER'].nunique()


def total_customers(df):
    """
    Count the total number of unique customers.
    """
    return df['CUSTOMERNAME'].nunique()


def total_products(df):
    """
    Count the total number of unique products.
    """
    return df['PRODUCTCODE'].nunique()


def filter_by_status(df, status: str):
    """
    Filter orders by their status (e.g., 'Shipped', 'Cancelled').
    """
    return df[df["STATUS"] == status]


def sort_products_by_sales(df):
    """
    Sort products by total sales in descending order.
    """
    return df.groupby("PRODUCTCODE")["SALES"].sum().sort_values(ascending=False)


def sort_countries_by_avg(df):
    """
    Sort countries by average sales per order in descending order.
    """
    return df.groupby("COUNTRY")["SALES"].mean().sort_values(ascending=False)


def sort_products_by_quantity(df):
    """
    Sort products by total quantity ordered in descending order.
    """
    qty = df.groupby("PRODUCTCODE")["QUANTITYORDERED"].sum()
    return qty.sort_values(ascending=False)