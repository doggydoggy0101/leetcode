## :book: Sum of Two Integers
Given two integers `a `and `b`, return the sum of the two integers without using the operators `+` and `-`.

### Approach 1
We use the relationship:
$$
a+b=\ln(e^{a+b})=\ln(e^a\cdot e^b)
$$

```python
def getSum(a: int, b: int) -> int:
    return math.log(math.exp(a) * math.exp(b))
```

I personally think this approach is very clever, however, the input values grow exponentially. For example, test cases such as `a=1000` will fail because $e^{1000}$ is too large for computers to handle.

### Approach 2
```python
def getSum(a: int, b: int) -> int:
    return sum([a, b])
```

### Approach 3
It seems like the proper way is by [bit manipulation](https://leetcode.com/problems/sum-of-two-integers/solutions/84278/a-summary-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently).
