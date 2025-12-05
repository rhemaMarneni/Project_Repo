from src.analysis import (
    overall_analysis,
    country_level_analysis,
    product_level_analysis,
    yearly_analysis,
    order_status_analysis,
    customer_level_analysis,
)

from pathlib import Path
import pandas as pd

def main():
    # Read the CSV file using pandas
    csv_path = Path("data/sales_data_sample.csv")
    df = pd.read_csv(csv_path, encoding='latin-1')

    overall_analysis(df)
    country_level_analysis(df)
    product_level_analysis(df)
    yearly_analysis(df)
    order_status_analysis(df)
    customer_level_analysis(df)

if __name__ == "__main__":
    main()