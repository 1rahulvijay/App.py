import pandas as pd
import unittest

class TestDataFrameOperations(unittest.TestCase):
    def setUp(self):
        # Set up some sample data
        self.df = pd.DataFrame({'A': [1, 2, 3, 4],
                                'B': [5, 6, 7, 8]})

    def test_add_column(self):
        # Test adding a new column
        self.df['C'] = self.df['A'] + self.df['B']
        self.assertTrue('C' in self.df.columns)
        self.assertTrue(all(self.df['C'] == [6, 8, 10, 12]))

    def test_drop_column(self):
        # Test dropping a column
        self.df.drop(columns=['B'], inplace=True)
        self.assertTrue('B' not in self.df.columns)

    def test_docstrings(self):
        # Test the examples in docstrings
        self.assertEqual(pd.DataFrame.mean.__doc__, 'Return the mean of the values for the requested axis.')
        # Add more docstring tests as needed

    def test_assertions(self):
        # Test some assertions
        self.assertEqual(len(self.df.columns), 2)  # Initially, DataFrame has 2 columns

if __name__ == '__main__':
    unittest.main()
