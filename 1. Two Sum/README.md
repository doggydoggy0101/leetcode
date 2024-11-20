## :book: Two Sum


### Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.

### Solution
- (Brute force) We can solve by two loops, however, the time complexity is $\mathcal{O}(n^2)$.
- By constructing a hashmap to store complement of numbers that we looked through, we only need one loop. Since the average time of accessing a hashmap is constant, the time complexity is $\mathcal{O}(n)$.
  
```python
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
```
