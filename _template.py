import os
import sys

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, ".."))
from checker import runTestCases


def fn():
    pass


def main():
    test_cases = [
        # turple of input/output
    ]

    runTestCases(fn, test_cases)


if __name__ == "__main__":
    main()
