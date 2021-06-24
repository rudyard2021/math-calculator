import unittest
from source.function import Function

class TestFunction(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)
        self.function = Function()

    def test_operators(self):
        self.function.start("---3+11-9*5/-15")
        self.assertEqual(self.function.f(), 11)

    def test_variables(self):
        self.function.start("3x^2-8x-10")
        self.assertEqual(self.function.f({"x":2}), -14)

        self.function.start("-10^y+-raiz(x)+raiz(8;3)")
        self.assertEqual(self.function.f({"y":2, "x":36}), -104)

    def test_functions(self):
        err = self.function.start("sin(pi/2)+cos(2pi)+abs(-3)*5-4!")
        self.assertEqual(self.function.f(), -7)

    def test_summa(self):
        err = self.function.start("summa(2^x;x;1;5)+root(125;3)")
        self.assertEqual(self.function.f(), 67)

if __name__ == "__main__":
    unittest.main("")

# python -m unittest tests/test_something.py