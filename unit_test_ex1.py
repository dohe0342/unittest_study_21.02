import unittest
import lib_calc

class TddTest(unittest.TestCase):
    #def __init__(self):
    #    super(TddTest, self).__init__()

    def testAdd(self):
        result = lib_calc.add(10, 20)
        if result == 30:
            print('testAdd OK')

    def testSubstract(self):
        result = lib_calc.substract(20, 30)
        if result > 0:
            boolval = True
        else:
            boolval = False

        if boolval == False:
            print('testSubstract Error')

    def testDivision(self):
        try:
            lib_calc.division(4, 0)
        except Exception as e:
            print(e)

    def testMultiply(self):
        result = lib_calc.multiply(10, 9)

        if result < 100:
            print('testMultiply Error')

if __name__ == '__main__':
    unittest.main()