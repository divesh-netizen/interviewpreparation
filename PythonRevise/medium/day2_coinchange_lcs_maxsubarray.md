Here are your **next 3 intermediate-level problems** for today. Each includes a base approach, an optimized approach, and step-by-step improvements.

---

### **Problem 4: Coin Change**  
#### **Task**  
Given an array of coins and a target amount, find the minimum number of coins needed to make up the amount. If it’s not possible, return -1.

---

#### **Base Approach (Recursive - Brute Force)**  
Try every combination and return the minimum.  

```python
def coin_change_base(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        res = coin_change_base(coins, amount - coin)
        if res != float('inf'):
            min_coins = min(min_coins, res + 1)
    
    return min_coins

# Example
coins = [1, 2, 5]
amount = 11
result = coin_change_base(coins, amount)
print(result if result != float('inf') else -1)  # Output: 3
```  

**Complexity:**  
- Time: \(O(2^n)\) (exponential).  
- Space: \(O(n)\) (recursion depth).  

---

#### **Optimized Approach (Dynamic Programming - Memoization)**  
Store computed values to avoid redundant calculations.  

```python
def coin_change_optimized(coins, amount, memo={}):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        res = coin_change_optimized(coins, amount - coin, memo)
        if res != float('inf'):
            min_coins = min(min_coins, res + 1)
    
    memo[amount] = min_coins
    return min_coins

# Example
coins = [1, 2, 5]
amount = 11
result = coin_change_optimized(coins, amount)
print(result if result != float('inf') else -1)  # Output: 3
```  

**Complexity:**  
- Time: \(O(n \times m)\) where \(n\) is the amount and \(m\) is the number of coins.  
- Space: \(O(n)\) (memoization).  

---

### **Problem 5: Longest Common Subsequence (LCS)**  
#### **Task**  
Given two strings, find the length of the longest subsequence common to both.  

---

#### **Base Approach (Recursive - Brute Force)**  
Try all subsequence combinations.  

```python
def lcs_base(s1, s2, i=0, j=0):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        return 1 + lcs_base(s1, s2, i + 1, j + 1)
    return max(lcs_base(s1, s2, i + 1, j), lcs_base(s1, s2, i, j + 1))

# Example
s1, s2 = "abcde", "ace"
print(lcs_base(s1, s2))  # Output: 3
```  

**Complexity:**  
- Time: \(O(2^n)\).  
- Space: \(O(n)\) (recursion depth).  

---

#### **Optimized Approach (Dynamic Programming - Memoization)**  
Store previously computed results.  

```python
def lcs_optimized(s1, s2, i=0, j=0, memo={}):
    if (i, j) in memo:
        return memo[(i, j)]
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]:
        memo[(i, j)] = 1 + lcs_optimized(s1, s2, i + 1, j + 1, memo)
    else:
        memo[(i, j)] = max(lcs_optimized(s1, s2, i + 1, j, memo), lcs_optimized(s1, s2, i, j + 1, memo))
    return memo[(i, j)]

# Example
s1, s2 = "abcde", "ace"
print(lcs_optimized(s1, s2))  # Output: 3
```  

**Complexity:**  
- Time: \(O(m \times n)\).  
- Space: \(O(m \times n)\) (memoization).  

---

### **Problem 6: Maximum Subarray Sum (Kadane’s Algorithm)**  
#### **Task**  
Find the maximum sum of a contiguous subarray in an array.  

---

#### **Base Approach (Brute Force - Nested Loops)**  
Check all possible subarrays.  

```python
def max_subarray_base(nums):
    max_sum = float('-inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            max_sum = max(max_sum, sum(nums[i:j+1]))
    return max_sum

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_base(nums))  # Output: 6
```  

**Complexity:**  
- Time: \(O(n^2)\).  
- Space: \(O(1)\).  

---

#### **Optimized Approach (Kadane’s Algorithm)**  
Use a single pass to find the maximum sum efficiently.  

```python
def max_subarray_optimized(nums):
    max_sum = nums[0]
    curr_sum = nums[0]
    
    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_optimized(nums))  # Output: 6
```  

**Complexity:**  
- Time: \(O(n)\).  
- Space: \(O(1)\).  

---

### **File Name for Today**  
**`day2_coinchange_lcs_maxsubarray.py`**  

Let me know when you’re ready for the next set of 3 problems! 🚀