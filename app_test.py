from app import app, forex_converter
from unittest import TestCase

class forexConverterTestCase(TestCase):
    
    def test_forex_converter(self):
        self.assertEqual(forex_converter(1, 'USD', 'USD'), 1.0)

    # testing routes
    def test_forex_converter_status(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text = True)

            self.assertEqual(res.status_code, 200)
            self.assertIn("<div class='h1 fw-bold'>Currency Converter</div>", html)

    def test_forex_converter_status(self):
        with app.test_client() as client:
            res = client.get('/result')
            html = res.get_data(as_text = True)
            
            self.assertEqual(res.status_code, 200)
            self.assertIn("<div class='h1 fw-bold'>Your Conversion Result Is:</div>", html)