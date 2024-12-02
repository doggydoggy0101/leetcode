import os
import sys
from typing import List
from functools import reduce

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(__dir__, "../.."))
from checker import runTestCases


def productExceptSelf(nums: List[int]) -> List[int]:
    num_zeros = nums.count(0)
    len_nums = len(nums)
    if num_zeros > 1:
        answer = [0] * len_nums
    elif num_zeros == 1:
        answer = [0] * len_nums
        idx = nums.index(0)
        del nums[idx]
        # `recude(fn, list)` passes `fn` to all `list` elements
        answer[idx] = reduce(lambda x, y: x * y, nums)
    else:
        answer = [1] * len_nums
        prefix, suffix = 1, 1
        # multiplying and updating prefix from the start
        for idx in range(len_nums):
            answer[idx] *= prefix
            prefix *= nums[idx]
        # multipying and updating suffix from the end
        for idx in range(len_nums - 1, -1, -1):
            answer[idx] *= suffix
            suffix *= nums[idx]
    return answer


def main():
    test_cases = [([1, 2, 3, 4], [24, 12, 8, 6]), ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0])]

    runTestCases(productExceptSelf, test_cases)


if __name__ == "__main__":
    main()
