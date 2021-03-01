import unittest
import lib_calc

class TddTest(unittest.TestCase):
    def testAdd(self):
        result = lib_calc.add(10, 20)
        self.assertEqual(result, 31)

    def testSubtract(self):
        result = lib_calc.substract(20, 10)
        if result > 10:
            boolval = False
        else:
            boolval = True

        self.assertTrue(boolval)

    def testDivision(self):
        self.assertRaises(ZeroDivisionError, lib_calc.division, 4, 1)

    def testMultiply(self):
        nonechk = True

        result = lib_calc.multiply(10, 9)

        if result > 100:
            nonechk = None

        self.assertIsNone(nonechk)

if __name__ == '__main__':
    unittest.main()
