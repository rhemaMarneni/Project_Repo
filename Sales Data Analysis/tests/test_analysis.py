import unittest
import pandas as pd
import sys
from pathlib import Path

# Adding parent directory to path to import src module
sys.path.insert(0, str(Path(__file__).parent.parent))

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
            'YEAR_ID': [2003, 2003, 2003, 2004, 2004],
            'QTR_ID': [1, 2, 3, 1, 2],
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
        self.assertIn(2004, result.index)
        # 2003 has 3 orders: 2871.0 + 2765.9 + 3884.34
        expected_2003 = 2871.0 + 2765.9 + 3884.34
        self.assertAlmostEqual(result[2003], expected_2003, places=2)
        # 2004 has 2 orders: 3746.7 + 5205.27
        expected_2004 = 3746.7 + 5205.27
        self.assertAlmostEqual(result[2004], expected_2004, places=2)

    def test_average_sales_per_order_line(self):
        """Test average_sales_per_order_line function."""
        result = average_sales_per_order_line(self.df)
        expected = (2871.0 + 2765.9 + 3884.34 + 3746.7 + 5205.27) / 5
        self.assertAlmostEqual(result, expected, places=2)

    def test_sales_by_year_and_quarter(self):
        """Test sales_by_year_and_quarter function."""
        result = sales_by_year_and_quarter(self.df)
        self.assertIsInstance(result, pd.Series)
        # Check that it groups by both year and quarter
        self.assertIn((2003, 1), result.index)
        self.assertIn((2003, 2), result.index)
        self.assertIn((2003, 3), result.index)
        self.assertIn((2004, 1), result.index)
        self.assertIn((2004, 2), result.index)

    def test_best_quarter_each_year(self):
        """Test best_quarter_each_year function."""
        result = best_quarter_each_year(self.df)
        self.assertIsInstance(result, pd.Series)
        # Should return quarter number for each year
        self.assertIn(2003, result.index)
        self.assertIn(2004, result.index)
        # Best quarter should be the one with highest sales (quarter 3 for 2003: 3884.34)
        self.assertEqual(result[2003], 3)
        # Quarter 2 for 2004: 5205.27
        self.assertEqual(result[2004], 2)

    def test_worst_quarter_each_year(self):
        """Test worst_quarter_each_year function."""
        result = worst_quarter_each_year(self.df)
        self.assertIsInstance(result, pd.Series)
        # Should return quarter number for each year
        self.assertIn(2003, result.index)
        self.assertIn(2004, result.index)
        # Worst quarter should be the one with lowest sales
        # 2003: Q1=2871.0, Q2=2765.9, Q3=3884.34 -> Q2 is worst
        self.assertEqual(result[2003], 2)
        # 2004: Q1=3746.7, Q2=5205.27 -> Q1 is worst
        self.assertEqual(result[2004], 1)

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
        # All products have same product line in test data
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

    def test_sort_countries_by_sales(self):
        """Test sort_countries_by_sales function."""
        result = sort_countries_by_sales(self.df)
        self.assertIsInstance(result, pd.Series)
        # Check that values are sorted in descending order
        values = result.values
        self.assertTrue(all(values[i] >= values[i+1] for i in range(len(values)-1)))
        # Check that countries are in the result
        self.assertIn('USA', result.index)
        self.assertIn('France', result.index)

    def test_sales_by_customer(self):
        """Test sales_by_customer function."""
        result = sales_by_customer(self.df)
        self.assertIsInstance(result, pd.Series)
        # Check that all customers are in the result
        self.assertIn('Customer1', result.index)
        self.assertIn('Customer2', result.index)
        self.assertIn('Customer3', result.index)
        self.assertIn('Customer4', result.index)
        # Customer1 appears twice, so should have sum of two sales
        expected_customer1 = 2871.0 + 3746.7
        self.assertAlmostEqual(result['Customer1'], expected_customer1, places=2)

    def test_sort_products_by_quantity(self):
        """Test sort_products_by_quantity function."""
        result = sort_products_by_quantity(self.df)
        self.assertIsInstance(result, pd.Series)
        # Check that values are sorted in descending order
        values = result.values
        self.assertTrue(all(values[i] >= values[i+1] for i in range(len(values)-1)))


if __name__ == '__main__':
    unittest.main()

