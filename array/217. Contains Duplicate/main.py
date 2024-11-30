import os
import sys
from typing import List

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, "../.."))
from checker import runTestCases


def containsDuplicate(nums: List[int]) -> bool:
    map_nums = {}
    for num in nums:
        # search if a value is in the hashmap
        if num in map_nums:
            return True
        else:
            # make a hashmap with `num` as key and a dummy value `0`
            map_nums[num] = 0
    return False


def main():
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
    ]

    runTestCases(containsDuplicate, test_cases)


if __name__ == "__main__":
    main()
