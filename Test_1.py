from unittest import TestCase

class TestComplex(TestCase):
    def test_sumofcomplex(self):
        from Complex import Complex
        result = Complex(1,1).angle()
        if isinstance(result, dict):
            self.assertEqual(result, 45)
            self.assertTrue(succeed("Complex"))
