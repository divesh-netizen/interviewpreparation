Here are **3 new problems** for today with base and optimized solutions. 🚀  

---

### **Problem 16: Coin Change**  
#### **Task**  
Given an array `coins` representing different denominations and an integer `amount`, return the minimum number of coins to make up that amount. If it's not possible, return `-1`.  

**Example:**  
Input: `coins = [1, 2, 5], amount = 11`  
Output: `3` (5 + 5 + 1)  

---

#### **Base Approach (Recursive - Brute Force)**  
Try every possible combination recursively.  

**Steps:**  
1. Start with the given amount and subtract each coin value recursively.  
2. Keep track of the minimum number of coins needed.  
3. If the amount becomes zero, return `0`. If negative, return `inf`.  

```python
def coin_change_base(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    min_coins = float('inf')
    for coin in coins:
        min_coins = min(min_coins, 1 + coin_change_base(coins, amount - coin))

    return min_coins if min_coins != float('inf') else -1

# Example
coins = [1, 2, 5]
amount = 11
print(coin_change_base(coins, amount))  # Output: 3
```  

**Complexity:**  
- Time: **Exponential \(O(2^n)\)** (Very inefficient)  
- Space: **O(n)** (Recursive call stack)  

---

#### **Optimized Approach (Dynamic Programming - Bottom-Up)**  
Use an array to store the minimum coins needed for each amount.  

**Steps:**  
1. Create a DP array of size `amount + 1`, initialized to `inf`, with `dp[0] = 0`.  
2. Iterate through each amount and check all coin denominations.  
3. Use the recurrence relation: `dp[i] = min(dp[i], dp[i - coin] + 1)`.  
4. Return `dp[amount]` if it's not `inf`.  

```python
def coin_change_optimized(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example
coins = [1, 2, 5]
amount = 11
print(coin_change_optimized(coins, amount))  # Output: 3
```  

**Complexity:**  
- Time: **O(n * m)** (n = amount, m = coins)  
- Space: **O(n)**  

---

### **Problem 17: Kth Largest Element in an Array**  
#### **Task**  
Find the `k`th largest element in an unsorted array.  

**Example:**  
Input: `nums = [3,2,3,1,2,4,5,5,6], k = 4`  
Output: `4`  

---

#### **Base Approach (Sorting)**  
Sort the array and return the \( k \)th last element.  

```python
def kth_largest_base(nums, k):
    nums.sort()
    return nums[-k]

# Example
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(kth_largest_base(nums, k))  # Output: 4
```  

**Complexity:**  
- Time: **O(n log n)** (Sorting)  
- Space: **O(1)**  

---

#### **Optimized Approach (Min-Heap)**  
Use a **heap** to efficiently find the \( k \)th largest element.  

**Steps:**  
1. Maintain a **min-heap** of size `k`.  
2. Iterate through `nums`, pushing elements into the heap.  
3. If heap size exceeds `k`, remove the smallest element.  
4. The top of the heap is the `k`th largest element.  

```python
import heapq

def kth_largest_optimized(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return heapq.heappop(min_heap)

# Example
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(kth_largest_optimized(nums, k))  # Output: 4
```  

**Complexity:**  
- Time: **O(n log k)**  
- Space: **O(k)**  

---

### **Problem 18: Decode Ways**  
#### **Task**  
A message containing letters **A-Z** is encoded as:  
- `'A' -> "1"`, `'B' -> "2"`, ..., `'Z' -> "26"`  

Given a string `s` containing only digits, return the **number of ways** to decode it.  

**Example:**  
Input: `s = "226"`  
Output: `3` (Decoded as `"BZ"`, `"VF"`, `"BBF"`)  

---

#### **Base Approach (Recursion - Brute Force)**  
Check every possible way to split the string.  

```python
def decode_ways_base(s):
    if not s:
        return 1
    if s[0] == '0':
        return 0

    count = decode_ways_base(s[1:])  # Take one digit
    if len(s) >= 2 and "10" <= s[:2] <= "26":
        count += decode_ways_base(s[2:])  # Take two digits

    return count

# Example
s = "226"
print(decode_ways_base(s))  # Output: 3
```  

**Complexity:**  
- Time: **Exponential \(O(2^n)\)**  
- Space: **O(n)**  

---

#### **Optimized Approach (Dynamic Programming - Bottom-Up)**  
Use an array to store solutions for subproblems.  

**Steps:**  
1. Create a `dp` array where `dp[i]` stores the number of ways to decode `s[:i]`.  
2. Handle single-digit and two-digit cases.  
3. Use `dp[i] = dp[i-1] + dp[i-2]` when valid.  

```python
def decode_ways_optimized(s):
    if not s or s[0] == '0':
        return 0

    dp = [0] * (len(s) + 1)
    dp[0], dp[1] = 1, 1  # Base cases

    for i in range(2, len(s) + 1):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        if "10" <= s[i - 2:i] <= "26":
            dp[i] += dp[i - 2]

    return dp[-1]

# Example
s = "226"
print(decode_ways_optimized(s))  # Output: 3
```  

**Complexity:**  
- Time: **O(n)**  
- Space: **O(n)**  

---

### **File Name for Today**  
**`day6_coin_kth_decode.py`**  

Let me know when you're ready for the next set! 🚀