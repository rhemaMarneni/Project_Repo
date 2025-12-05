import unittest
import pandas as pd
import sys
from pathlib import Path

# Adding parent directory to path to import src module
sys.path.insert(0, str(Path(__file__).parent.parent))

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


class TestAnalysis(unittest.TestCase):
    """Test cases for analysis functions."""

    def setUp(self):
        """Set up test data."""
        self.df = pd.DataFrame({
            'ORDERNUMBER': [10107, 10121, 10134, 10145, 10159],
            'SALES': [2871.0, 2765.9, 3884.34, 3746.7, 5205.27],
            'COUNTRY': ['USA', 'France', 'France', 'USA', 'USA'],
            'PRODUCTLINE': ['Motorcycles', 'Motorcycles', 'Motorcycles', 'Motorcycles', 'Motorcycles'],
            'PRODUCTCODE': ['S10_1678', 'S10_1678', 'S10_1678', 'S10_1678', 'S10_1678'],
            'YEAR_ID': [2003, 2003, 2003, 2003, 2003],
            'STATUS': ['Shipped', 'Shipped', 'Shipped', 'Cancelled', 'Shipped'],
            'QUANTITYORDERED': [30, 34, 41, 45, 49],
            'CUSTOMERNAME': ['Customer1', 'Customer2', 'Customer3', 'Customer1', 'Customer4']
        })

    def test_total_sales(self):
        """Test total_sales function."""
        result = total_sales(self.df)
        expected = 2871.0 + 2765.9 + 3884.34 + 3746.7 + 5205.27
        self.assertAlmostEqual(result, expected, places=2)

    def test_sales_by_country(self):
        """Test sales_by_country function."""
        result = sales_by_country(self.df)
        self.assertIn('USA', result.index)
        self.assertIn('France', result.index)
        self.assertAlmostEqual(result['USA'], 2871.0 + 3746.7 + 5205.27, places=2)
        self.assertAlmostEqual(result['France'], 2765.9 + 3884.34, places=2)

    def test_sales_by_product(self):
        """Test sales_by_product function."""
        result = sales_by_product(self.df)
        self.assertIn('Motorcycles', result.index)
        expected_total = 2871.0 + 2765.9 + 3884.34 + 3746.7 + 5205.27
        self.assertAlmostEqual(result['Motorcycles'], expected_total, places=2)

    def test_sales_by_year(self):
        """Test sales_by_year function."""
        result = sales_by_year(self.df)
        self.assertIn(2003, result.index)
        expected_total = 2871.0 + 2765.9 + 3884.34 + 3746.7 + 5205.27
        self.assertAlmostEqual(result[2003], expected_total, places=2)

    def test_average_sales_per_order_line(self):
        """Test average_sales_per_order_line function."""
        result = average_sales_per_order_line(self.df)
        expected = (2871.0 + 2765.9 + 3884.34 + 3746.7 + 5205.27) / 5
        self.assertAlmostEqual(result, expected, places=2)

    def test_top_product_by_sales(self):
        """Test top_product_by_sales function."""
        result = top_product_by_sales(self.df)
        self.assertIsInstance(result, pd.Series)
        self.assertLessEqual(len(result), 10)
        self.assertIn('Motorcycles', result.index)

    def test_large_orders(self):
        """Test large_orders function."""
        threshold = 3000.0
        result = large_orders(self.df, threshold)
        self.assertIsInstance(result, pd.DataFrame)
        # Should include orders with sales > 3000
        self.assertTrue(all(result['SALES'] > threshold))

    def test_total_orders(self):
        """Test total_orders function."""
        result = total_orders(self.df)
        # All order numbers are unique in test data
        self.assertEqual(result, 5)

    def test_total_customers(self):
        """Test total_customers function."""
        result = total_customers(self.df)
        # Customer1 appears twice, Customer2, Customer3, Customer4 appear once
        self.assertEqual(result, 4)

    def test_total_products(self):
        """Test total_products function."""
        result = total_products(self.df)
        # All products have same code in test data
        self.assertEqual(result, 1)

    def test_filter_by_status(self):
        """Test filter_by_status function."""
        result = filter_by_status(self.df, 'Shipped')
        self.assertIsInstance(result, pd.DataFrame)
        self.assertTrue(all(result['STATUS'] == 'Shipped'))
        self.assertEqual(len(result), 4)  # 4 shipped orders in test data

    def test_sort_products_by_sales(self):
        """Test sort_products_by_sales function."""
        result = sort_products_by_sales(self.df)
        self.assertIsInstance(result, pd.Series)
        # Check that values are sorted in descending order
        values = result.values
        self.assertTrue(all(values[i] >= values[i+1] for i in range(len(values)-1)))

    def test_sort_countries_by_avg(self):
        """Test sort_countries_by_avg function."""
        result = sort_countries_by_avg(self.df)
        self.assertIsInstance(result, pd.Series)
        # Check that values are sorted in descending order
        values = result.values
        self.assertTrue(all(values[i] >= values[i+1] for i in range(len(values)-1)))

    def test_sort_products_by_quantity(self):
        """Test sort_products_by_quantity function."""
        result = sort_products_by_quantity(self.df)
        self.assertIsInstance(result, pd.Series)
        # Check that values are sorted in descending order
        values = result.values
        self.assertTrue(all(values[i] >= values[i+1] for i in range(len(values)-1)))


if __name__ == '__main__':
    unittest.main()

