Here are **3 new problems** for today with base and optimized solutions. 🚀  

---

### **Problem 19: Unique Paths**  
#### **Task**  
A robot is located at the top-left corner of an `m x n` grid. The robot can **only move right or down** at any step.  
Find the number of unique paths to reach the bottom-right corner.  

**Example:**  
Input: `m = 3, n = 7`  
Output: `28`  

---

#### **Base Approach (Recursive - Brute Force)**  
Try all possible paths recursively.  

**Steps:**  
1. Base case: If `m == 1` or `n == 1`, return `1` (only one way).  
2. Recursive case: Move **right** or **down**.  

```python
def unique_paths_base(m, n):
    if m == 1 or n == 1:
        return 1
    return unique_paths_base(m - 1, n) + unique_paths_base(m, n - 1)

# Example
print(unique_paths_base(3, 7))  # Output: 28
```  

**Complexity:**  
- Time: **O(2^(m+n))** (Exponential, very inefficient)  
- Space: **O(m + n)** (Recursion depth)  

---

#### **Optimized Approach (Dynamic Programming - Bottom-Up)**  
Use a **DP table** to store results for subproblems.  

**Steps:**  
1. Create a `dp` table with size `[m][n]` initialized to `1` (since there's only one way to reach the first row/column).  
2. Use `dp[i][j] = dp[i-1][j] + dp[i][j-1]` for the rest of the grid.  

```python
def unique_paths_optimized(m, n):
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]

# Example
print(unique_paths_optimized(3, 7))  # Output: 28
```  

**Complexity:**  
- Time: **O(m * n)**  
- Space: **O(m * n)**  

---

### **Problem 20: Rotate Image (90° Clockwise)**  
#### **Task**  
Given an `N x N` matrix, rotate it **90° clockwise** in place.  

**Example:**  
Input:  
```
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
```  
Output:  
```
matrix = [[7,4,1],
          [8,5,2],
          [9,6,3]]
```  

---

#### **Base Approach (Extra Matrix - O(n²) Space)**  
Create a **new matrix** and place elements at rotated positions.  

```python
def rotate_image_base(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]

    return rotated

# Example
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_image_base(matrix))
```  

**Complexity:**  
- Time: **O(n²)**  
- Space: **O(n²)** (New matrix)  

---

#### **Optimized Approach (Transpose + Reverse - In-Place)**  
1. **Transpose:** Swap `matrix[i][j]` with `matrix[j][i]`.  
2. **Reverse Each Row** to achieve the 90° rotation.  

```python
def rotate_image_optimized(matrix):
    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()

# Example
matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate_image_optimized(matrix)
print(matrix)
```  

**Complexity:**  
- Time: **O(n²)**  
- Space: **O(1)** (In-place)  

---

### **Problem 21: Word Break**  
#### **Task**  
Given a string `s` and a list of words `wordDict`, return `True` if `s` can be segmented into words from `wordDict`.  

**Example:**  
Input: `s = "leetcode", wordDict = ["leet", "code"]`  
Output: `True`  

---

#### **Base Approach (Recursion - Brute Force)**  
Try all possible word splits recursively.  

```python
def word_break_base(s, wordDict):
    if not s:
        return True

    for word in wordDict:
        if s.startswith(word) and word_break_base(s[len(word):], wordDict):
            return True

    return False

# Example
print(word_break_base("leetcode", ["leet", "code"]))  # Output: True
```  

**Complexity:**  
- Time: **Exponential \(O(2^n)\)** (Inefficient)  
- Space: **O(n)** (Recursion depth)  

---

#### **Optimized Approach (Dynamic Programming - Bottom-Up)**  
Use a **DP array** where `dp[i]` stores if `s[:i]` can be broken.  

**Steps:**  
1. Create `dp` of size `len(s) + 1`, initialize `dp[0] = True`.  
2. Check if any substring `s[j:i]` exists in `wordDict` and `dp[j]` is `True`.  

```python
def word_break_optimized(s, wordDict):
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[-1]

# Example
print(word_break_optimized("leetcode", ["leet", "code"]))  # Output: True
```  

**Complexity:**  
- Time: **O(n²)**  
- Space: **O(n)**  

---

### **File Name for Today**  
**`day7_paths_rotate_wordbreak.py`**  

Let me know when you're ready for the next set! 🚀