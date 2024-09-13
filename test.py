import unittest
import pandas as pd
from datetime import datetime
df = pd.read_csv('HINDALCO_1D.csv')
class TestTradingStrategy(unittest.TestCase):
    def validate_input_data(self,df):
        if not all(df['open'].apply(lambda x: isinstance(x, float))):
            raise ValueError("Open prices must be decimal")
        if not all(df['high'].apply(lambda x: isinstance(x, float))):
            raise ValueError("High prices must be decimal")
        if not all(df['low'].apply(lambda x: isinstance(x, float))):
            raise ValueError("Low prices must be decimal")
        if not all(df['close'].apply(lambda x: isinstance(x, float))):
            raise ValueError("Close prices must be decimal")
        if not all(df['volume'].apply(lambda x: isinstance(x, int))):
            raise ValueError("Volume must be integer")
        if not all(df['instrument'].apply(lambda x: isinstance(x, str))):
            raise ValueError("Instrument must be a string")
        if not all(pd.to_datetime(df['datetime'], errors='coerce').notna()):
            raise ValueError("Datetime must be valid datetime format")
        return True
    
    def setUp(self):
        self.valid_data = pd.DataFrame({
            'datetime': [datetime(2023, 9, 12), datetime(2023, 9, 13)],
            'open': [100.0, 102.0],
            'high': [105.0, 106.0],
            'low': [99.0, 101.0],
            'close': [104.0, 105.0],
            'volume': [1000, 1500],
            'instrument': ['AAPL', 'AAPL']
        })
        
        self.invalid_data = pd.DataFrame({
            'datetime': [datetime(2023, 9, 12), datetime(2023, 9, 13)],
            'open': [100.0, 102.0],
            'high': [105.0, 106.0],
            'low': [99.0, 101.0],
            'close': [104.0, 105.0],
            'volume': ['1000', '1500'],  
            'instrument': ['AAPL', 'AAPL']
        })
    
    def test_valid_input(self):
        result = self.validate_input_data(self.valid_data)
        self.assertTrue(result)
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.validate_input_data(self.invalid_data)

if __name__ == '__main__':
    unittest.main()
