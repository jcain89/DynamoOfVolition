import unittest
import UnitTests

if __name__ == "__main__":
    print("Hello!")
    suite = unittest.findTestCases(UnitTests)
    result = unittest.TestResult()
    suite.run(result, debug=True)
    print(f"result ={result}")

