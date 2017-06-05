from unittest import TestCase

class TestComplex(TestCase):
    def test_sumofcomplex(self):
        from Complex import Complex
        result = angle(Complex(1,1))
        if isinstance(result, dict):
            self.assertEqual(result, 45)
            self.assertTrue(succeed("Complex"))
        else:
            self.assertFalse(incorrect_output())
