import unittest
from src.etl.source1.process import Source1ETL
from src.etl.source2.process import Source2ETL

class TestETLProcesses(unittest.TestCase):

    def setUp(self):
        self.source1_etl = Source1ETL()
        self.source2_etl = Source2ETL()

    def test_source1_extract(self):
        data = self.source1_etl.extract()
        self.assertIsNotNone(data)
        # Add more assertions based on expected data structure

    def test_source1_transform(self):
        raw_data = self.source1_etl.extract()
        transformed_data = self.source1_etl.transform(raw_data)
        self.assertIsNotNone(transformed_data)
        # Add more assertions based on expected transformation

    def test_source1_load(self):
        data_to_load = {'key': 'value'}  # Example data
        result = self.source1_etl.load(data_to_load)
        self.assertTrue(result)
        # Add more assertions based on expected load result

    def test_source2_extract(self):
        data = self.source2_etl.extract()
        self.assertIsNotNone(data)
        # Add more assertions based on expected data structure

    def test_source2_transform(self):
        raw_data = self.source2_etl.extract()
        transformed_data = self.source2_etl.transform(raw_data)
        self.assertIsNotNone(transformed_data)
        # Add more assertions based on expected transformation

    def test_source2_load(self):
        data_to_load = {'key': 'value'}  # Example data
        result = self.source2_etl.load(data_to_load)
        self.assertTrue(result)
        # Add more assertions based on expected load result

if __name__ == '__main__':
    unittest.main()