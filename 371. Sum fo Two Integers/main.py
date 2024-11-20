import os
import sys
import math

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, ".."))
from checker import runTestCases


def getSum(a: int, b: int) -> int:
    return math.log(2**a * 2**b, 2)


def main():
    test_cases = [
        ((1, 2), 3),
        ((2, 3), 5),
    ]

    runTestCases(getSum, test_cases)


if __name__ == "__main__":
    main()
