## :book: Sum of Two Integers

### Problem
Given two integers `a `and `b`, return the sum of the two integers without using the operators `+` and `-`.

### Approach 1
We use the relationship

$$
a+b=\ln(e^{a+b})=\ln(e^a\cdot e^b)
$$

I personally think this approach is very clever, however, the input values grow exponentially. For example, test cases such as `a=1000` will fail because $e^{1000}$ is too large for computers to handle. We could also use $\log_2$ instead of $\ln$ to have a larger domain.

```python
def getSum(a: int, b: int) -> int:
    return math.log(2**a * 2**b, 2)
```

### Approach 2
```python
def getSum(a: int, b: int) -> int:
    return sum([a, b])
```

### Approach 3
I guess the proper way is by bit manipulations, e.g., `AND`, `OR`, and `XOR`. Below we give the truth table of these of these logic gates:
| A | B | `AND` | `OR` | `XOR` |
|---|---|-------|------|-------|
| T | T | T     | T    | F     |
| T | F | F     | T    | T     |
| F | T | F     | T    | T     |
| F | F | F     | F    | F     |

Since we cannot use the operators `+` and `-`, we simmulate the addition process by `XOR` and `AND`.

**`XOR` for addition:**
- $1+1=1$ `XOR` $1=0$ (needs to add 1 value to the left bit)
- $1+0=1$ `XOR` $0=1$ 
- $0+1=0$ `XOR` $1=1$ 
- $0+0=0$ `XOR` $0=0$

**`AND` for adding 1 value to the left bit:**
- $1$ `AND` $1=1$ (indeed needs to add 1 value to the left bit)
- $1$ `AND` $0=0$ 
- $0$ `AND` $1=0$ 
- $0$ `AND` $0=0$

The process is as follows:

1. compute the carry by `a & b`
2. left shift the carry by `carry << 1`
3. compute the solution by `a ^ b`
4. if the carry is not 0, set the solution as `a` and carry as `b`, return to step 1

```python
def getSum(a: int, b: int) -> int:
    # during the loop, we set `a` as the solution and `b` as the carry
    # loop stops if `b` or carry is 0
    while b:
        # use `AND` to calculate the carry
        bit_carry = a & b
        # use `XOR` to calculate the solution
        a = a ^ b
        # set `b` as the new carry
        b = bit_carry << 1
    return a
```

> explain counter example

Note that python allows infinite-length integers, since `-1000 < a, b < 1000`, we restrict `a, b` to be 16-bit. This can be done by `x & 0xFFFF`, where `0xFFFF` is the hexadecimal of a 16-bit 1's.

> explain negative/positive case

```python
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
```
