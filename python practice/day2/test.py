import unittest
from subprocess import Popen, PIPE, STDOUT
import string
import random

def int_generator(min=0, max=100):
    return random.randint(min, max)

def real_generator(min=0.0, max=1000000.0):
    return random.uniform(min, max)

def TestBase():
    mealCost = real_generator()
    tipPercent = int_generator()
    taxPercent = int_generator()
	
    tip = mealCost * (tipPercent / 100.0)
    tax = mealCost * (taxPercent / 100.0)
    totalCost = mealCost + tip + tax

    stdIn = str(mealCost) + "\r\n" + str(tipPercent) + "\r\n" + str(taxPercent) + "\r\n"
    p = Popen(['python', 'solution.py'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)   
    stdout = p.communicate(input=bytes(stdIn, encoding='utf-8'))[0]
    expectedStdout = "The total meal cost is {} dollars.".format(round(totalCost)) + "\r\n"
    return (stdout.decode(), expectedStdout)

class test(unittest.TestCase): 
    
    def testCase1(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])

    def testCase2(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])

    def testCase3(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase4(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase5(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase6(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase7(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
	
    def testCase8(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase9(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])
		
    def testCase10(self):
        result = TestBase()
        self.assertEqual( result[0], result[1])

if __name__ == '__main__':
    unittest.main()
