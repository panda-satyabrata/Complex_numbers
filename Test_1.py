from unittest import TestCase

class TestComplex(TestCase):
    def test_sumofcomplex(self):
        from Complex import Complex
        result = Complex(1,1) + Complex(2,2)
        if isinstance(result, Complex):
            self.assertEqual(result, 3+3i)
            self.assertTrue(succeed("Complex"))
