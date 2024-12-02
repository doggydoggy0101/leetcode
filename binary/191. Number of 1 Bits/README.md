## :book:Number of 1 Bits

### Problem
Given a positive integer `n`, write a function that returns the number of 
set bits in its binary representation.

### Approach 1
One straightforward way is to convert the integer to a binary string, then count `"1"` in the binary string. The time complexity is $\mathcal{O}(\log n)$, where $\log n$ is the length of the binary string.

```python
def hammingWeight(n: int) -> int:
    # convert integer to binary string
    bit_string = str(bin(n))[2:]
    # use python default string count
    return bit_string.count("1")
```

### Approach 2
Another way is by bit manipulations (please refer to [LeetCode 371](../371.%20Sum%20fo%20Two%20Integers/) for more details). For each iteration, we check the most right bit by `n & 1`, then right shift `n` until there is no bit. The time complexity is still $\mathcal{O}(\log n)$, since we are essentially looping through $\log n$ bits, however, the space complexity is $\mathcal{O}(1)$ in this case.

```python
def hammingWeight(n: int) -> int:
    count = 0
    while n != 0:
        # use `AND` to check the most right bit
        if n & 1:
            count += 1
        # right shift `n`
        n = n >> 1
    return count
```

### Comparison

|                  | string conversion     | bit manipulation      |
|------------------|-----------------------|-----------------------|
| time complexity  | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ |
| space complexity | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$      |