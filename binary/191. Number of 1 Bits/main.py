import os
import sys

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, "../.."))
from checker import runTestCases


def hammingWeight(n: int) -> int:
    count = 0
    while n != 0:
        # use `AND` to check the most right bit
        if n & 1:
            count += 1
        # right shift `n`
        n = n >> 1
    return count


def main():
    test_cases = [(11, 3), (128, 1), (2147483645, 30)]

    runTestCases(hammingWeight, test_cases)


if __name__ == "__main__":
    main()
