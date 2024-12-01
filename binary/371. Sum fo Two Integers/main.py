import os
import sys

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, "../.."))
from checker import runTestCases


def getSum(a: int, b: int) -> int:
    # during the loop, we set `a` as the solution and `b` as the carry
    # loop stops if `b` or carry is 0
    while b:
        # use `AND` to calculate the carry
        bit_carry = a & b
        # use `XOR` to calculate the solution and restrict to 16-bit
        a = (a ^ b) & 0xFFFF
        # set `b` as the new carry and restrict to 16-bit
        b = (bit_carry << 1) & 0xFFFF

    if a < 0x8000:
        return a
    else:
        return ~(a ^ 0xFFFF)


def main():
    test_cases = [((1, 2), 3), ((2, 3), 5), ((-1, 1), 0)]

    runTestCases(getSum, test_cases)


if __name__ == "__main__":
    main()
