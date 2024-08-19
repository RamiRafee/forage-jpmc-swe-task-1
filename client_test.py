import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    expected_results = [
            ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2),
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
    ]
    for quote, expected in zip(quotes, expected_results):
      self.assertEqual(getDataPoint(quote), expected)
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 118.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 
             'top_bid': {'price': 119.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    expected_results = [
            ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),
            ('DEF', 119.87, 118.68, (119.87 + 118.68) / 2)
    ]
    for quote, expected in zip(quotes, expected_results):
      self.assertEqual(getDataPoint(quote), expected)
  

  def test_getRatio_validInputs(self):
      self.assertEqual(getRatio(120, 60), 2.0)
      self.assertEqual(getRatio(100, 50), 2.0)
      self.assertEqual(getRatio(75, 25), 3.0)

  def test_getRatio_divideByZero(self):
      self.assertEqual(getRatio(120, 0), -1)
      self.assertEqual(getRatio(0, 0), -1)

  def test_getDataPoint_malformedData(self):
      malformed_quotes = [
          {'top_bid': {'price': 120.48, 'size': 109}, 'stock': 'ABC'},  # Missing top_ask
          {'top_ask': {'price': 121.2, 'size': 36}, 'stock': 'DEF'},    # Missing top_bid
      ]
      for quote in malformed_quotes:
          with self.assertRaises(KeyError):
              getDataPoint(quote)
  
  def test_getDataPoint_negativePrices(self):
      quotes = [
          {'top_ask': {'price': -121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 
            'top_bid': {'price': -120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      ]
      expected_results = [
          ('ABC', -120.48, -121.2, (-120.48 + -121.2) / 2),
      ]
      
      for quote, expected in zip(quotes, expected_results):
          self.assertEqual(getDataPoint(quote), expected)

if __name__ == '__main__':
    unittest.main()
