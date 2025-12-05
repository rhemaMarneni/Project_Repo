"""Utility functions for formatting and printing data."""

def format_currency(x):
    """Format a number as currency with comma separators."""
    return f"{x:,.2f}"


def format_item(item):
    """Format and print an item (key, value) pair with no formatting."""
    print(f"  {item[0]}: {item[1]}")

def get_count(df):
    """Get the count of rows in a DataFrame."""
    return df.shape[0]


def format_currency_item(item):
    """Format and print an item (key, value) pair with currency formatting."""
    print(f"  {item[0]}: ${format_currency(item[1])}")

def get_percentile(df, column, percentile):
    """
    Get the percentile of a column.
    """
    return df[column].quantile(percentile)