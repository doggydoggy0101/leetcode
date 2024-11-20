import os
import sys
from typing import List

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, ".."))
from checker import runTestCases


def twoSum(nums: List[int], target: int) -> List[int]:
    map_num = {}
    for idx, num in enumerate(nums):
        complement = target - num
        # search if the complement is in the hashmap
        if complement in map_num:
            # return index of complement and current index
            return [map_num[complement], idx]
        else:
            # make a hashmap with `num` as key and `idx` as its value
            map_num[num] = idx


def main():
    test_cases = [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
    ]

    runTestCases(twoSum, test_cases)


if __name__ == "__main__":
    main()
