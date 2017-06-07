from unittest import TestCase
from Complex import Complex

class TestComplex(TestCase):
    
    def test_divisionofcomplex(self):
        result = Complex(2,3) / (Complex(1,2))
        self.assertEqual(result, Complex(1.5999999999999996,-0.19999999999999996))
        
