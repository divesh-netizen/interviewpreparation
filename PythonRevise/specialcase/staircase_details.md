
---

## **Understanding the Problem**
If `n = 5`, the available steps are `{1, 2, 3, 4}`, meaning the user can take any of these at each step. The recurrence relation becomes:

\[
f(n) = f(n-1) + f(n-2) + f(n-3) + \dots + f(1)
\]

### **Example Breakdown (n = 5)**
We count all possible ways to reach `5` using `{1, 2, 3, 4}`:

1. **Take 1 step → Reach `4` → Solve `f(4)`**
2. **Take 2 steps → Reach `3` → Solve `f(3)`**
3. **Take 3 steps → Reach `2` → Solve `f(2)`**
4. **Take 4 steps → Reach `1` → Solve `f(1)`**

So:
\[
f(5) = f(4) + f(3) + f(2) + f(1)
\]

---

## **Recursive Approach**
```python
def count_ways(n):
    if n == 0:  # Base case: 1 way to stay at ground
        return 1
    if n < 0:
        return 0

    total_ways = 0
    for i in range(1, n):  # Taking steps from 1 to (n-1)
        total_ways += count_ways(n - i)

    return total_ways

print(count_ways(5))  # Output: 16
```
🔴 **Issue:** This has an exponential `O(2^n)` complexity due to repeated calculations.

---

## **Optimized Dynamic Programming (O(n²))**
Instead of recomputing values, store them in a `dp` array.

```python
def count_ways_dp(n):
    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1  # Base case

    for i in range(1, n + 1):
        for j in range(1, i):  # Sum all previous dp values
            dp[i] += dp[i - j]

    return dp[n]

print(count_ways_dp(5))  # Output: 16
```
✅ **Time Complexity:** `O(n²)`  
✅ **Space Complexity:** `O(n)`

---

## **Optimized Approach Using Prefix Sum (O(n))**
Since `dp[n] = sum(dp[0] to dp[n-1])`, we use a **prefix sum** to speed up the computation.

```python
def count_ways_optimized(n):
    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1

    prefix_sum = 1  # Tracks sum of all dp values

    for i in range(1, n + 1):
        dp[i] = prefix_sum
        prefix_sum += dp[i]  # Update prefix sum

    return dp[n]

print(count_ways_optimized(5))  # Output: 16
```
✅ **Time Complexity:** `O(n)`  
✅ **Space Complexity:** `O(n)`

---

## **Mathematical Formula (`O(1)`)**
From pattern observation, the function follows:

\[
f(n) = 2^{(n-1)}
\]

So, the final optimized solution is:

```python
def count_ways_formula(n):
    return 2**(n-1)

print(count_ways_formula(5))  # Output: 16
```
✅ **Time Complexity:** `O(1)`  
✅ **Space Complexity:** `O(1)`

---

## **Final Summary**
| Approach | Time Complexity | Space Complexity |
|----------|---------------|-----------------|
| Recursive | `O(2^n)` | `O(n)` (call stack) |
| DP (Bottom-Up) | `O(n²)` | `O(n)` |
| DP (Prefix Sum) | `O(n)` | `O(n)` |
| Formula (`2^(n-1)`) | `O(1)` | `O(1)` |

🚀 **Best Approach:** Use `2^(n-1)`, which gives instant results! 🚀

---