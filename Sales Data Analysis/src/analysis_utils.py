"""Analysis utils for sales data."""

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


def sales_by_year_and_quarter(df):
    """
    Calculate total sales grouped by year and quarter.
    """
    return df.groupby(['YEAR_ID', 'QTR_ID'])['SALES'].sum()

def best_quarter_each_year(df):
    """
    Calculate the best quarter for each year.
    """
    s = sales_by_year_and_quarter(df)
    return s.groupby(level=0).idxmax().apply(lambda t: int(t[1]))

def worst_quarter_each_year(df):
    """
    Calculate the worst quarter for each year.
    """
    s = sales_by_year_and_quarter(df)
    return s.groupby(level=0).idxmin().apply(lambda t: int(t[1]))

def average_sales_per_order_line(df):
    """
    Calculate the average sales amount per order line.
    """
    return df['SALES'].mean()


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
    return df['PRODUCTLINE'].nunique()


def filter_by_status(df, status: str):
    """
    Filter orders by their status (e.g., 'Shipped', 'Cancelled').
    """
    return df[df["STATUS"] == status]


def sort_products_by_sales(df):
    """
    Sort products by total sales in descending order.
    """
    return df.groupby("PRODUCTLINE")["SALES"].sum().sort_values(ascending=False)


def sort_countries_by_sales(df):
    """
    Sort countries by sales values per order in descending order.
    """
    return df.groupby("COUNTRY")["SALES"].sum().sort_values(ascending=False)


def sort_products_by_quantity(df):
    """
    Sort products by total quantity ordered in descending order.
    """
    qty = df.groupby("PRODUCTLINE")["QUANTITYORDERED"].sum()
    return qty.sort_values(ascending=False)


def sales_by_customer(df):
    """
    Calculate total sales grouped by customer.
    """
    return df.groupby("CUSTOMERNAME")["SALES"].sum()


def total_orders_per_customer(df):
    """
    Calculate total orders grouped by customer.
    """
    return df.groupby("CUSTOMERNAME")["ORDERNUMBER"].nunique()