## :book: Contains Duplicate

### Problem
Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

### Solution
Similar to [LeetCode 1](../1.%20Two%20Sum/), we construct a hashmap to store the `nums` we have seen. Thereby, we only need one for loop. Since the average time of accessing a hashmap is constant, the time complexity is $\mathcal{O}(n)$.
```python
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
```
