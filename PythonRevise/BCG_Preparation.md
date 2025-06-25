
---

## ✅ **Batch 1 of 20 (Q1–Q5)**

---

### **Q1: Two Sum**

**Problem:**
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the target.

**Example:**
Input: `nums = [2, 7, 11, 15], target = 9`
Output: `[0, 1]`

---

#### 🔹 Basic Approach: Brute Force

**Time:** O(n²) | **Space:** O(1)

```python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```

---

#### 🔹 Optimal Approach: Hash Map

**Time:** O(n) | **Space:** O(n)

```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

**Explanation:** Store numbers as you iterate, and check if the complement exists in the dictionary.

---

### **Q2: Valid Anagram**

**Problem:**
Check if `s` and `t` are anagrams of each other.

**Example:**
Input: `s = "listen", t = "silent"` → Output: `True`

---

#### 🔹 Basic Approach: Sort and Compare

**Time:** O(n log n) | **Space:** O(n)

```python
def is_anagram(s, t):
    return sorted(s) == sorted(t)
```

---

#### 🔹 Optimal Approach: Count Frequencies

**Time:** O(n) | **Space:** O(1) for 26 chars

```python
from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)
```

**Explanation:** Count characters and compare counts.

---

### **Q3: Longest Substring Without Repeating Characters**

**Problem:**
Find the length of the longest substring without repeating characters.

**Example:**
Input: `s = "abcabcbb"` → Output: `3` ("abc")

---

#### 🔹 Basic Approach: Brute Force Substrings

**Time:** O(n²) | **Space:** O(n)

```python
def length_of_longest_substring(s):
    max_len = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    return max_len
```

---

#### 🔹 Optimal Approach: Sliding Window

**Time:** O(n) | **Space:** O(n)

```python
def length_of_longest_substring(s):
    char_index = {}
    start = max_len = 0
    for i, c in enumerate(s):
        if c in char_index and char_index[c] >= start:
            start = char_index[c] + 1
        char_index[c] = i
        max_len = max(max_len, i - start + 1)
    return max_len
```

**Explanation:** Expand window until a duplicate appears, then move start pointer.

---

### **Q4: Group Anagrams**

**Problem:**
Group strings that are anagrams into the same list.

**Example:**
Input: `["eat", "tea", "tan", "ate", "nat", "bat"]`
Output: `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

---

#### 🔹 Basic Approach: Sort Key

**Time:** O(n \* k log k) | **Space:** O(nk)

```python
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    return list(anagrams.values())
```

---

#### 🔹 Optimal Approach: Frequency Tuple as Key

**Time:** O(n \* k) | **Space:** O(nk)

```python
from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        anagrams[tuple(count)].append(word)
    return list(anagrams.values())
```

**Explanation:** Use a frequency tuple instead of sorting.

---

### **Q5: Top K Frequent Elements**

**Problem:**
Return the `k` most frequent elements from the array.

**Example:**
Input: `nums = [1,1,1,2,2,3], k = 2` → Output: `[1,2]`

---

#### 🔹 Basic Approach: Sort by Frequency

**Time:** O(n log n) | **Space:** O(n)

```python
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [item for item, freq in count.most_common(k)]
```

---

#### 🔹 Optimal Approach: Bucket Sort

**Time:** O(n) | **Space:** O(n)

```python
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in count.items():
        buckets[freq].append(num)

    res = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res
```

**Explanation:** Use bucket sort indexed by frequency to get top k.

---

Great! Let’s move on to the **next 5 questions (Q6–Q10)** focusing on **Sliding Window** and **Two Pointers** — both are highly tested patterns in CodeSignal assessments.

---

## ✅ **Batch 2 of 20 (Q6–Q10)**

---

### **Q6: Maximum Sum Subarray of Size K**

**Problem:**
Given an array of integers `arr` and an integer `k`, find the maximum sum of any contiguous subarray of size `k`.

**Example:**
Input: `arr = [2, 1, 5, 1, 3, 2], k = 3` → Output: `9` (`[5,1,3]`)

---

#### 🔹 Basic Approach: Brute Force

**Time:** O(nk) | **Space:** O(1)

```python
def max_sum_subarray_k(arr, k):
    max_sum = float('-inf')
    for i in range(len(arr) - k + 1):
        window_sum = sum(arr[i:i+k])
        max_sum = max(max_sum, window_sum)
    return max_sum
```

---

#### 🔹 Optimal Approach: Sliding Window

**Time:** O(n) | **Space:** O(1)

```python
def max_sum_subarray_k(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum
```

**Explanation:** Slide the window of size `k` forward by subtracting the element left behind and adding the new one.

---

### **Q7: Minimum Window Substring**

**Problem:**
Given strings `s` and `t`, return the minimum window in `s` that contains all characters in `t`.

**Example:**
Input: `s = "ADOBECODEBANC", t = "ABC"` → Output: `"BANC"`

---

#### 🔹 Basic Approach: Brute Force (TLE on large input)

**Time:** O(n³) | **Space:** O(1)

(Not implemented due to inefficiency)

---

#### 🔹 Optimal Approach: Sliding Window + Hash Map

**Time:** O(n) | **Space:** O(n)

```python
from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    t_count = Counter(t)
    window_count = {}
    have, need = 0, len(t_count)
    res, res_len = [-1, -1], float("inf")
    l = 0

    for r in range(len(s)):
        c = s[r]
        window_count[c] = window_count.get(c, 0) + 1

        if c in t_count and window_count[c] == t_count[c]:
            have += 1

        while have == need:
            # update result
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1
            # shrink window
            window_count[s[l]] -= 1
            if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                have -= 1
            l += 1

    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""
```

---

### **Q8: Container With Most Water**

**Problem:**
Given `height[i]` representing vertical lines, find two lines that together with the x-axis form a container, such that the container contains the most water.

**Example:**
Input: `[1,8,6,2,5,4,8,3,7]` → Output: `49`

---

#### 🔹 Basic Approach: Brute Force

**Time:** O(n²) | **Space:** O(1)

```python
def max_area(height):
    max_area = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
    return max_area
```

---

#### 🔹 Optimal Approach: Two Pointers

**Time:** O(n) | **Space:** O(1)

```python
def max_area(height):
    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
        area = min(height[l], height[r]) * (r - l)
        max_area = max(max_area, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_area
```

**Explanation:** Use two pointers from both ends and move inward, always favoring the taller wall.

---

### **Q9: Longest Repeating Character Replacement**

**Problem:**
You can replace at most `k` characters to make the longest substring with the same character. Return the length of this substring.

**Example:**
Input: `s = "ABAB", k = 2` → Output: `4`

---

#### 🔹 Optimal Approach: Sliding Window

**Time:** O(n) | **Space:** O(26)

```python
def character_replacement(s, k):
    count = {}
    maxf = 0
    l = 0
    res = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        if (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res
```

**Explanation:** Track the most frequent character in the window and check if replacing others exceeds `k`.

---

### **Q10: Longest Subarray with Sum <= K (Positive Numbers Only)**

**Problem:**
Given an array of positive integers and an integer `k`, return the length of the longest subarray whose sum is less than or equal to `k`.

**Example:**
Input: `nums = [1,2,1,0,1], k = 4` → Output: `4`

---

#### 🔹 Optimal Approach: Sliding Window

**Time:** O(n) | **Space:** O(1)

```python
def longest_subarray_sum_k(nums, k):
    left = 0
    curr_sum = 0
    max_len = 0

    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum > k:
            curr_sum -= nums[left]
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len
```

---

Great! Now let’s move to **Batch 3 (Q11–Q15)** focusing on **Recursion, Backtracking, Subsets, and Permutations** — key areas for CodeSignal-style problem solving.

---

## ✅ **Batch 3 of 20 (Q11–Q15)**

---

### **Q11: Subsets (Power Set)**

**Problem:**
Given a set of distinct integers `nums`, return all possible subsets.

**Example:**
Input: `[1,2,3]`
Output: `[[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]`

---

#### 🔹 Basic Recursive Approach

**Time:** O(2^n) | **Space:** O(2^n)

```python
def subsets(nums):
    res = []

    def backtrack(i, path):
        if i == len(nums):
            res.append(path[:])
            return
        # include
        path.append(nums[i])
        backtrack(i + 1, path)
        path.pop()
        # exclude
        backtrack(i + 1, path)

    backtrack(0, [])
    return res
```

**Explanation:** At every step, either include the number or skip it. Classic binary decision tree.

---

### **Q12: Permutations**

**Problem:**
Return all permutations of a list of distinct integers.

**Example:**
Input: `[1,2,3]`
Output: `[[1,2,3], [1,3,2], [2,1,3], ...]`

---

#### 🔹 Backtracking Approach

**Time:** O(n!) | **Space:** O(n)

```python
def permute(nums):
    res = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

    backtrack([])
    return res
```

**Explanation:** Track used elements and build path recursively.

---

### **Q13: Combination Sum**

**Problem:**
Given a list of candidate numbers (no duplicates) and a target, return all unique combinations that sum to the target. You can reuse numbers.

**Example:**
Input: `candidates = [2,3,6,7], target = 7`
Output: `[[2,2,3],[7]]`

---

#### 🔹 Backtracking with DFS

**Time:** Exponential (worst-case)

```python
def combination_sum(candidates, target):
    res = []

    def backtrack(start, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])  # reuse same
            path.pop()

    backtrack(0, [], 0)
    return res
```

**Explanation:** Use DFS to explore all combinations starting from current index.

---

### **Q14: Generate Parentheses**

**Problem:**
Generate all combinations of well-formed parentheses for given `n` pairs.

**Example:**
Input: `n = 3`
Output: `["((()))", "(()())", "(())()", "()(())", "()()()"]`

---

#### 🔹 Backtracking with Count

**Time:** O(2^n) | **Space:** O(n)

```python
def generate_parenthesis(n):
    res = []

    def backtrack(open_count, close_count, path):
        if len(path) == 2 * n:
            res.append(path)
            return
        if open_count < n:
            backtrack(open_count + 1, close_count, path + '(')
        if close_count < open_count:
            backtrack(open_count, close_count + 1, path + ')')

    backtrack(0, 0, '')
    return res
```

**Explanation:** Open bracket can be added as long as count < n. Close can be added only if it won’t unbalance.

---

### **Q15: Word Search**

**Problem:**
Given a 2D board and a word, return true if the word exists in the grid using DFS (horizontal/vertical only, no reuse of cells).

**Example:**
Input:

```text
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
word = "ABCCED"
```

Output: `True`

---

#### 🔹 Backtracking with DFS

**Time:** O(m × n × 4^L) | **Space:** O(L) for recursion

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False

        temp = board[r][c]
        board[r][c] = "#"  # mark visited
        found = (
            dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or
            dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
        )
        board[r][c] = temp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```

**Explanation:** Use DFS from each cell. Mark as visited using a placeholder and backtrack.

---

Perfect! Now let's dive into **Batch 4 (Q16–Q20)** focused on **Dynamic Programming (DP)** — a major topic in technical interviews and CodeSignal evaluations.

---

## ✅ **Batch 4 of 20 (Q16–Q20)**

---

### **Q16: Climbing Stairs**

**Problem:**
You can climb 1 or 2 steps at a time. Given `n`, return the number of ways to reach the top.

**Example:**
Input: `n = 4` → Output: `5`

---

#### 🔹 Basic Approach: Recursion (Inefficient)

**Time:** O(2ⁿ)

```python
def climb_stairs(n):
    if n <= 1:
        return 1
    return climb_stairs(n - 1) + climb_stairs(n - 2)
```

---

#### 🔹 Optimal Approach: DP with Tabulation

**Time:** O(n) | **Space:** O(n)

```python
def climb_stairs(n):
    if n <= 1:
        return 1
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

**Explanation:** Same as Fibonacci. Each step depends on the last 2.

---

### **Q17: House Robber**

**Problem:**
You can't rob two adjacent houses. Maximize the sum of money.

**Example:**
Input: `[2,7,9,3,1]` → Output: `12` (2 + 9 + 1)

---

#### 🔹 Basic Recursive Approach

**Time:** O(2ⁿ)

```python
def rob(nums):
    def helper(i):
        if i >= len(nums):
            return 0
        return max(helper(i + 1), nums[i] + helper(i + 2))
    return helper(0)
```

---

#### 🔹 Optimal Approach: Bottom-Up DP

**Time:** O(n) | **Space:** O(1)

```python
def rob(nums):
    rob1, rob2 = 0, 0
    for n in nums:
        new_rob = max(rob2, rob1 + n)
        rob1 = rob2
        rob2 = new_rob
    return rob2
```

**Explanation:** Track rob amount of current and previous house.

---

### **Q18: Longest Increasing Subsequence (LIS)**

**Problem:**
Return the length of the longest increasing subsequence.

**Example:**
Input: `[10,9,2,5,3,7,101,18]` → Output: `4`

---

#### 🔹 Basic DP Approach

**Time:** O(n²) | **Space:** O(n)

```python
def length_of_LIS(nums):
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

**Explanation:** For each element, check LIS ending before it.

---

#### 🔹 Optimal Approach: Binary Search

**Time:** O(n log n)

```python
import bisect

def length_of_LIS(nums):
    sub = []
    for x in nums:
        i = bisect.bisect_left(sub, x)
        if i == len(sub):
            sub.append(x)
        else:
            sub[i] = x
    return len(sub)
```

**Explanation:** `sub` doesn't hold final subsequence but helps compute LIS length.

---

### **Q19: Coin Change (Min Coins)**

**Problem:**
Given coins `[1,2,5]` and amount `11`, return min coins needed → Output: `3` (5+5+1)

---

#### 🔹 Basic Recursive Approach

**Time:** O(n^amount)

```python
def coin_change(coins, amount):
    if amount == 0: return 0
    if amount < 0: return -1
    res = float('inf')
    for coin in coins:
        sub = coin_change(coins, amount - coin)
        if sub == -1: continue
        res = min(res, 1 + sub)
    return res if res != float('inf') else -1
```

---

#### 🔹 Optimal Approach: DP Bottom-Up

**Time:** O(n × amount) | **Space:** O(amount)

```python
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != float('inf') else -1
```

**Explanation:** Build up solutions for each value from `1` to `amount`.

---

### **Q20: Maximum Product Subarray**

**Problem:**
Find the contiguous subarray that has the largest product.

**Example:**
Input: `[2,3,-2,4]` → Output: `6`

---

#### 🔹 Optimal DP Approach

**Time:** O(n) | **Space:** O(1)

```python
def max_product(nums):
    max_prod = nums[0]
    cur_max, cur_min = nums[0], nums[0]

    for n in nums[1:]:
        temp_max = max(n, cur_max * n, cur_min * n)
        cur_min = min(n, cur_max * n, cur_min * n)
        cur_max = temp_max
        max_prod = max(max_prod, cur_max)

    return max_prod
```

**Explanation:** Track both min and max at each step (because negative × negative = positive).

---

Awesome! Let’s move on to **Batch 5 (Q21–Q25)**, covering **Graph Traversal** using **BFS and DFS** — another high-priority topic for CodeSignal and system-level problem-solving.

---

## ✅ **Batch 5 of 20 (Q21–Q25)**

---

### **Q21: Number of Islands**

**Problem:**
Given a 2D grid of `'1'`s (land) and `'0'`s (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

**Example:**
Input:

```python
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```

Output: `3`

---

#### 🔹 DFS Approach

**Time:** O(m × n) | **Space:** O(m × n)

```python
def num_islands(grid):
    if not grid:
        return 0

    def dfs(r, c):
        if (r < 0 or r >= len(grid) or 
            c < 0 or c >= len(grid[0]) or 
            grid[r][c] == '0'):
            return
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                dfs(r, c)
                islands += 1
    return islands
```

---

### **Q22: Clone Graph**

**Problem:**
Given a reference to a node in a connected undirected graph, return a deep copy (clone) of the graph.

**Example Input:**

```text
Node with val 1 connected to [2, 4]
Node with val 2 connected to [1, 3]
...
```

---

#### 🔹 DFS + HashMap

**Time:** O(V + E) | **Space:** O(V)

```python
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors or []

def clone_graph(node):
    old_to_new = {}

    def dfs(n):
        if not n:
            return None
        if n in old_to_new:
            return old_to_new[n]

        copy = Node(n.val)
        old_to_new[n] = copy
        for nei in n.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node)
```

**Explanation:** Use a map to avoid revisiting and infinitely looping on cycles.

---

### **Q23: Course Schedule (Topological Sort)**

**Problem:**
Can you finish all courses? Each course has prerequisites. Return `True` if it's possible (no cycle in graph).

**Example:**
Input: `numCourses = 2, prerequisites = [[1,0]]` → Output: `True`

---

#### 🔹 DFS Cycle Detection

**Time:** O(V + E) | **Space:** O(V)

```python
def can_finish(numCourses, prerequisites):
    from collections import defaultdict
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    visiting = set()
    visited = set()

    def dfs(crs):
        if crs in visiting:
            return False
        if crs in visited:
            return True
        visiting.add(crs)
        for nei in graph[crs]:
            if not dfs(nei):
                return False
        visiting.remove(crs)
        visited.add(crs)
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False
    return True
```

---

### **Q24: Pacific Atlantic Water Flow**

**Problem:**
From a grid of heights, return cells from which water can flow to both Pacific and Atlantic oceans.

**Example:**
Input:

```python
heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
```

Output: Coordinates where water can flow to both oceans.

---

#### 🔹 Multi-DFS from Edges

**Time:** O(mn) | **Space:** O(mn)

```python
def pacific_atlantic(heights):
    if not heights:
        return []

    rows, cols = len(heights), len(heights[0])
    pacific, atlantic = set(), set()

    def dfs(r, c, visited, prevHeight):
        if ((r < 0 or r >= rows or c < 0 or c >= cols) or
            (r, c) in visited or heights[r][c] < prevHeight):
            return
        visited.add((r, c))
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            dfs(r+dr, c+dc, visited, heights[r][c])

    for c in range(cols):
        dfs(0, c, pacific, heights[0][c])
        dfs(rows-1, c, atlantic, heights[rows-1][c])
    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0])
        dfs(r, cols-1, atlantic, heights[r][cols-1])

    return list(pacific & atlantic)
```

---

### **Q25: Word Ladder (Shortest Transformation Sequence)**

**Problem:**
Transform `beginWord` to `endWord` by changing one letter at a time, such that each transformed word is in `wordList`.

**Example:**
Input:
`beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]`
Output: `5` (`hit → hot → dot → dog → cog`)

---

#### 🔹 BFS + Set for Fast Lookup

**Time:** O(N \* 26) | **Space:** O(N)

```python
from collections import deque

def ladder_length(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, length + 1))
    return 0
```

**Explanation:** Use BFS to explore all words one letter away and track steps.

---


Awesome! Let’s dive into **Batch 6 (Q26–Q30)** focusing on **Greedy Algorithms and Intervals** — high-yield problems often featured in coding tests like CodeSignal.

---

## ✅ **Batch 6 of 20 (Q26–Q30)**

---

### **Q26: Jump Game**

**Problem:**
Given an array `nums`, where each element represents your max jump length at that position, determine if you can reach the last index.

**Example:**
Input: `nums = [2,3,1,1,4]` → Output: `True`

---

#### 🔹 Greedy Approach

**Time:** O(n) | **Space:** O(1)

```python
def can_jump(nums):
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + num)
    return True
```

**Explanation:** Track the furthest index reachable as you iterate.

---

### **Q27: Jump Game II (Min Jumps)**

**Problem:**
Return the minimum number of jumps needed to reach the last index.

**Example:**
Input: `nums = [2,3,1,1,4]` → Output: `2`

---

#### 🔹 Greedy Window Approach

**Time:** O(n) | **Space:** O(1)

```python
def jump(nums):
    jumps = 0
    farthest = 0
    end = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == end:
            jumps += 1
            end = farthest
    return jumps
```

**Explanation:** When you reach the edge of the current jump range, make another jump.

---

### **Q28: Merge Intervals**

**Problem:**
Given a list of intervals, merge all overlapping intervals.

**Example:**
Input: `[[1,3],[2,6],[8,10],[15,18]]`
Output: `[[1,6],[8,10],[15,18]]`

---

#### 🔹 Sort + Merge

**Time:** O(n log n) | **Space:** O(n)

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)
    return merged
```

**Explanation:** Sort by start, merge if overlapping.

---

### **Q29: Insert Interval**

**Problem:**
Given a list of non-overlapping intervals sorted by start time, insert a new interval and merge if needed.

**Example:**
Input: `intervals = [[1,3],[6,9]], newInterval = [2,5]`
Output: `[[1,5],[6,9]]`

---

#### 🔹 Merge While Inserting

**Time:** O(n) | **Space:** O(n)

```python
def insert(intervals, newInterval):
    result = []
    i = 0

    # Add intervals before newInterval
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    # Add the rest
    while i < len(intervals):
        result.append(intervals[i])
        i += 1

    return result
```

---

### **Q30: Non-overlapping Intervals (Minimum to Remove)**

**Problem:**
Return the minimum number of intervals to remove to make the rest non-overlapping.

**Example:**
Input: `[[1,2],[2,3],[3,4],[1,3]]` → Output: `1`

---

#### 🔹 Greedy Based on End Time

**Time:** O(n log n) | **Space:** O(1)

```python
def erase_overlap_intervals(intervals):
    intervals.sort(key=lambda x: x[1])
    end = float('-inf')
    count = 0

    for start, stop in intervals:
        if start >= end:
            end = stop
        else:
            count += 1
    return count
```

**Explanation:** Always keep interval with smallest end to maximize room for future ones.

---

Awesome! Let’s proceed with **Batch 7 (Q31–Q35)**, focusing on **Heaps, Priority Queues, and Scheduling Problems** — crucial for real-time systems, streaming data, and greedy optimization.

---

## ✅ **Batch 7 of 20 (Q31–Q35)**

---

### **Q31: Kth Largest Element in Array**

**Problem:**
Find the `k`th largest element in an unsorted array.

**Example:**
Input: `nums = [3,2,1,5,6,4], k = 2` → Output: `5`

---

#### 🔹 Min Heap Approach

**Time:** O(n log k) | **Space:** O(k)

```python
import heapq

def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
```

**Explanation:** Maintain a min-heap of size `k`, top element is the `k`th largest.

---

### **Q32: K Closest Points to Origin**

**Problem:**
Given a list of points on the plane, return the `k` closest to the origin `(0, 0)`.

**Example:**
Input: `[[1,3],[-2,2]], k = 1` → Output: `[[-2,2]]`

---

#### 🔹 Max Heap Approach

**Time:** O(n log k) | **Space:** O(k)

```python
import heapq

def k_closest(points, k):
    heap = []
    for x, y in points:
        dist = -(x**2 + y**2)
        heapq.heappush(heap, (dist, [x, y]))
        if len(heap) > k:
            heapq.heappop(heap)
    return [point for _, point in heap]
```

**Explanation:** Use a max-heap with negative distances to track k closest.

---

### **Q33: Task Scheduler**

**Problem:**
You are given tasks and a cooldown `n`. Return the minimum time to finish all tasks with cooldown between same tasks.

**Example:**
Input: `tasks = ["A","A","A","B","B","B"], n = 2`
Output: `8`

---

#### 🔹 Greedy with Max Frequency

**Time:** O(n) | **Space:** O(1)

```python
from collections import Counter

def least_interval(tasks, n):
    freq = list(Counter(tasks).values())
    max_freq = max(freq)
    max_count = freq.count(max_freq)
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)
```

**Explanation:** Arrange most frequent tasks first, fill gaps with others or idle.

---

### **Q34: Top K Frequent Elements**

**Problem:**
Return the `k` most frequent elements.

**Example:**
Input: `nums = [1,1,1,2,2,3], k = 2` → Output: `[1,2]`

---

#### 🔹 Heap + Frequency Map

**Time:** O(n log k) | **Space:** O(n)

```python
from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

**Explanation:** Use heap to extract top k from frequency dictionary.

---

### **Q35: Merge K Sorted Lists**

**Problem:**
Merge `k` sorted linked lists into one sorted list.

**Example:**
Input:

```python
lists = [
  [1,4,5],
  [1,3,4],
  [2,6]
]
```

Output: `[1,1,2,3,4,4,5,6]`

---

#### 🔹 Min Heap Approach

**Time:** O(N log k) | **Space:** O(k)

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode()
    curr = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
```

**Explanation:** Push the smallest node from each list into heap. Always extract the smallest and push next from that list.

---


Perfect! Now let’s continue with **Batch 8 (Q36–Q40)** focusing on **Bit Manipulation** and **Number Theory** — essential for low-level optimization and tricky logic puzzles often seen in interviews.

---

## ✅ **Batch 8 of 20 (Q36–Q40)**

---

### **Q36: Single Number (Every Element Appears Twice Except One)**

**Problem:**
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

**Example:**
Input: `nums = [4,1,2,1,2]` → Output: `4`

---

#### 🔹 Bitwise XOR Approach

**Time:** O(n) | **Space:** O(1)

```python
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

**Explanation:**
XOR cancels out duplicate numbers: `a ^ a = 0`, `0 ^ b = b`. So the result will be the unique number.

---

### **Q37: Counting Bits**

**Problem:**
Given an integer `n`, return an array where `ans[i]` is the number of 1’s in the binary representation of `i`.

**Example:**
Input: `n = 5` → Output: `[0,1,1,2,1,2]`

---

#### 🔹 DP with Bit Shift

**Time:** O(n) | **Space:** O(n)

```python
def count_bits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp
```

**Explanation:**
`dp[i] = dp[i // 2] + (i % 2)` → Use result from half + 1 if LSB is 1.

---

### **Q38: Hamming Distance**

**Problem:**
Given two integers, return the number of positions at which the corresponding bits are different.

**Example:**
Input: `x = 1, y = 4` → Output: `2`

---

#### 🔹 XOR and Count

**Time:** O(1) | **Space:** O(1)

```python
def hamming_distance(x, y):
    return bin(x ^ y).count('1')
```

**Explanation:**
XOR to highlight differing bits, then count 1s.

---

### **Q39: Sum of Two Integers (No + or -)**

**Problem:**
Calculate the sum of two integers without using `+` or `-`.

**Example:**
Input: `a = 1, b = 2` → Output: `3`

---

#### 🔹 Bitwise Full Adder Simulation

**Time:** O(1) | **Space:** O(1)

```python
def get_sum(a, b):
    MAX = 0x7FFFFFFF
    MASK = 0xFFFFFFFF
    while b != 0:
        a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
    return a if a <= MAX else ~(a ^ MASK)
```

**Explanation:**
Simulate binary addition with XOR and AND + shift.

---

### **Q40: Power of Two**

**Problem:**
Given an integer, return true if it's a power of two.

**Example:**
Input: `n = 8` → Output: `True`

---

#### 🔹 Bitwise Check

**Time:** O(1) | **Space:** O(1)

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
```

**Explanation:**
A power of 2 in binary has only one `1`. `(n & (n-1))` removes the lowest set bit — should be 0 for powers of 2.

---

Excellent! Let’s move on to **Batch 9 (Q41–Q45)** covering **Math, Primes, and Combinatorics** — these types of questions test your grasp of number theory, pattern recognition, and performance optimization in calculations.

---

## ✅ **Batch 9 of 20 (Q41–Q45)**

---

### **Q41: Count Primes Less Than n**

**Problem:**
Return the number of prime numbers less than a non-negative number `n`.

**Example:**
Input: `n = 10` → Output: `4` (`2, 3, 5, 7`)

---

#### 🔹 Sieve of Eratosthenes

**Time:** O(n log log n) | **Space:** O(n)

```python
def count_primes(n):
    if n < 2:
        return 0
    is_prime = [True] * n
    is_prime[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    return sum(is_prime)
```

**Explanation:**
Mark all multiples of each prime as non-prime starting from its square.

---

### **Q42: Power of Three**

**Problem:**
Return true if `n` is a power of 3.

**Example:**
Input: `n = 27` → Output: `True`

---

#### 🔹 Logarithmic Modulus or Division

**Time:** O(log n)

```python
def is_power_of_three(n):
    if n < 1:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1
```

---

#### 🔹 Max Integer Power Divisibility

**Time:** O(1)

```python
def is_power_of_three(n):
    return n > 0 and 3**19 % n == 0  # 3^19 is max power of 3 within 32-bit int
```

---

### **Q43: Excel Sheet Column Number**

**Problem:**
Given a column title like `"AB"`, return its corresponding column number.

**Example:**
Input: `"AB"` → Output: `28`

---

#### 🔹 Base-26 Conversion

**Time:** O(n)

```python
def title_to_number(column_title):
    result = 0
    for c in column_title:
        result = result * 26 + (ord(c) - ord('A') + 1)
    return result
```

**Explanation:**
Treat characters as base-26 digits (A=1, B=2, ..., Z=26).

---

### **Q44: Trailing Zeroes in Factorial**

**Problem:**
Given an integer `n`, return the number of trailing zeroes in `n!`.

**Example:**
Input: `n = 100` → Output: `24`

---

#### 🔹 Count Factors of 5

**Time:** O(log n)

```python
def trailing_zeroes(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count
```

**Explanation:**
Each 5 in the factorial contributes a trailing zero, count multiples of 5, 25, etc.

---

### **Q45: Pascal’s Triangle**

**Problem:**
Generate the first `numRows` of Pascal’s triangle.

**Example:**
Input: `5` → Output:

```python
[
 [1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1]
]
```

---

#### 🔹 Build Row by Row

**Time:** O(n²) | **Space:** O(n²)

```python
def generate(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
```

**Explanation:**
Each cell is the sum of two values from the previous row.

---

Great! Now let's continue with **Batch 10 (Q46–Q50)** focusing on **Stack, Queue, and Monotonic Stack** — these are essential for solving problems related to parsing, histograms, and sliding window optimization.

---

## ✅ **Batch 10 of 20 (Q46–Q50)**

---

### **Q46: Valid Parentheses**

**Problem:**
Given a string containing only `()[]{}`, determine if it's valid — meaning every opening bracket has a corresponding closing one in the correct order.

**Example:**
Input: `"([{}])"` → Output: `True`

---

#### 🔹 Stack Approach

**Time:** O(n) | **Space:** O(n)

```python
def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    return not stack
```

**Explanation:**
Push opening brackets, and on encountering a closing bracket, check for match at the top.

---

### **Q47: Min Stack**

**Problem:**
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

---

#### 🔹 Two-Stack Approach

**Time:** O(1) for all ops

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')]

    def push(self, val):
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
```

**Explanation:**
Use an auxiliary stack to keep track of current minimums.

---

### **Q48: Daily Temperatures**

**Problem:**
Given an array of temperatures, return an array that tells how many days to wait until a warmer temperature.

**Example:**
Input: `[73, 74, 75, 71, 69, 72, 76, 73]` → Output: `[1,1,4,2,1,1,0,0]`

---

#### 🔹 Monotonic Stack

**Time:** O(n) | **Space:** O(n)

```python
def daily_temperatures(temps):
    res = [0] * len(temps)
    stack = []

    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)
    return res
```

**Explanation:**
Use a decreasing stack to keep track of indices waiting for a warmer day.

---

### **Q49: Largest Rectangle in Histogram**

**Problem:**
Given an array of bar heights, return the area of the largest rectangle in the histogram.

**Example:**
Input: `[2,1,5,6,2,3]` → Output: `10`

---

#### 🔹 Monotonic Stack + Sentinel

**Time:** O(n) | **Space:** O(n)

```python
def largest_rectangle_area(heights):
    heights.append(0)  # sentinel to flush stack
    stack = [-1]
    max_area = 0

    for i, h in enumerate(heights):
        while heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area
```

**Explanation:**
Maintain increasing stack. When a shorter bar appears, calculate areas for taller bars that ended.

---

### **Q50: Sliding Window Maximum**

**Problem:**
Return the maximum in every window of size `k`.

**Example:**
Input: `nums = [1,3,-1,-3,5,3,6,7], k = 3` → Output: `[3,3,5,5,6,7]`

---

#### 🔹 Monotonic Queue (Deque)

**Time:** O(n) | **Space:** O(k)

```python
from collections import deque

def max_sliding_window(nums, k):
    q = deque()
    res = []

    for i, n in enumerate(nums):
        # Remove elements out of window
        while q and q[0] <= i - k:
            q.popleft()
        # Remove smaller elements from back
        while q and nums[q[-1]] < n:
            q.pop()
        q.append(i)
        if i >= k - 1:
            res.append(nums[q[0]])
    return res
```

**Explanation:**
Use deque to maintain indices of useful elements (in decreasing order of value).

---

Great! Let's continue with **Batch 11 (Q51–Q55)** focusing on **Tries, String Manipulation, and Pattern Matching** — crucial for problems involving dictionaries, search engines, and input validation.

---

## ✅ **Batch 11 of 20 (Q51–Q55)**

---

### **Q51: Implement Trie (Prefix Tree)**

**Problem:**
Implement a trie with `insert`, `search`, and `startsWith` operations.

---

#### 🔹 Trie Node Class-Based Approach

**Time:** O(n) per operation | **Space:** O(n \* k)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end

    def startsWith(self, prefix):
        return self._find(prefix) is not None

    def _find(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
```

---

### **Q52: Longest Common Prefix**

**Problem:**
Find the longest common prefix among an array of strings.

**Example:**
Input: `["flower","flow","flight"]` → Output: `"fl"`

---

#### 🔹 Horizontal Scanning

**Time:** O(n \* m) | **Space:** O(1)

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
```

**Explanation:**
Start with the first string as prefix, reduce it until all match.

---

### **Q53: Group Shifted Strings**

**Problem:**
Group strings that are shifted versions of each other (`abc` → `bcd`, `xyz` → `yza`).

**Example:**
Input: `["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]`

---

#### 🔹 Normalize with Difference Pattern

**Time:** O(n \* k) | **Space:** O(n)

```python
from collections import defaultdict

def group_shifted_strings(strings):
    def normalize(s):
        if len(s) == 1:
            return "single"
        offset = ord(s[0])
        return tuple((ord(c) - offset) % 26 for c in s)

    groups = defaultdict(list)
    for word in strings:
        groups[normalize(word)].append(word)
    return list(groups.values())
```

---

### **Q54: Word Search II (Find Words in Grid)**

**Problem:**
Given a board and a list of words, return all words present in the board.

---

#### 🔹 Trie + DFS

**Time:** O(M × N × L) | **Space:** O(W × L)

```python
def find_words(board, words):
    trie = {}
    for word in words:
        node = trie
        for char in word:
            node = node.setdefault(char, {})
        node["#"] = word  # end marker

    res = []
    rows, cols = len(board), len(board[0])

    def dfs(r, c, node):
        char = board[r][c]
        if char not in node:
            return
        next_node = node[char]
        word_match = next_node.pop("#", False)
        if word_match:
            res.append(word_match)

        board[r][c] = "#"
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                dfs(nr, nc, next_node)
        board[r][c] = char

        if not next_node:
            node.pop(char)

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie)

    return res
```

**Explanation:**
Build a trie from the word list and run DFS from each grid cell.

---

### **Q55: Isomorphic Strings**

**Problem:**
Two strings are isomorphic if characters in one string can be replaced to get the other string (same mapping throughout).

**Example:**
Input: `s = "egg", t = "add"` → Output: `True`

---

#### 🔹 HashMap + Set Tracking

**Time:** O(n) | **Space:** O(n)

```python
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    s_map = {}
    t_map = {}
    for sc, tc in zip(s, t):
        if s_map.get(sc) != t_map.get(tc):
            return False
        s_map[sc] = t_map[tc] = tc
    return True
```

**Alternative:**
Use first-seen index pattern:

```python
def is_isomorphic(s, t):
    return [s.index(c) for c in s] == [t.index(c) for c in t]
```

---

Excellent! Let’s proceed with **Batch 12 (Q56–Q60)** focused on **Sliding Window Variants and Subarray Challenges** — these problems test efficiency and mastery over pointer manipulation and real-time data processing.

---

## ✅ **Batch 12 of 20 (Q56–Q60)**

---

### **Q56: Minimum Size Subarray Sum**

**Problem:**
Given an array of positive integers `nums` and a target `target`, return the minimum length of a contiguous subarray of which the sum ≥ `target`.

**Example:**
Input: `target = 7, nums = [2,3,1,2,4,3]` → Output: `2`

---

#### 🔹 Sliding Window

**Time:** O(n) | **Space:** O(1)

```python
def min_subarray_len(target, nums):
    left = 0
    total = 0
    min_len = float('inf')

    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len
```

**Explanation:**
Expand the window to reach the target, then shrink to minimize it.

---

### **Q57: Subarray Sum Equals K**

**Problem:**
Given an integer array `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.

**Example:**
Input: `nums = [1,1,1], k = 2` → Output: `2`

---

#### 🔹 Prefix Sum + HashMap

**Time:** O(n) | **Space:** O(n)

```python
from collections import defaultdict

def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_map = defaultdict(int)
    prefix_map[0] = 1

    for num in nums:
        prefix_sum += num
        count += prefix_map.get(prefix_sum - k, 0)
        prefix_map[prefix_sum] += 1

    return count
```

**Explanation:**
Track running sum and how often each sum has occurred.

---

### **Q58: Longest Subarray with Sum ≤ K**

**Problem:**
Given an array of **positive integers** and a number `k`, return the length of the longest subarray with sum ≤ `k`.

**Example:**
Input: `nums = [1,2,1,0,1], k = 4` → Output: `4`

---

#### 🔹 Sliding Window (Positive Integers Only)

**Time:** O(n) | **Space:** O(1)

```python
def longest_subarray_sum_k(nums, k):
    left = 0
    total = 0
    max_len = 0

    for right in range(len(nums)):
        total += nums[right]
        while total > k:
            total -= nums[left]
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len
```

**Explanation:**
Window grows until it exceeds `k`, then shrink it.

---

### **Q59: Max Consecutive Ones III**

**Problem:**
Given a binary array `nums` and integer `k`, return the max number of consecutive `1`s you can get after flipping at most `k` `0`s.

**Example:**
Input: `nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2` → Output: `6`

---

#### 🔹 Sliding Window with Zero Counter

**Time:** O(n) | **Space:** O(1)

```python
def longest_ones(nums, k):
    left = 0
    zeros = 0
    max_len = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len
```

**Explanation:**
Use a sliding window that tolerates up to `k` zeros.

---

### **Q60: Longest Substring with At Most K Distinct Characters**

**Problem:**
Given a string `s` and an integer `k`, return the length of the longest substring with at most `k` distinct characters.

**Example:**
Input: `s = "eceba", k = 2` → Output: `3` (`"ece"`)

---

#### 🔹 Sliding Window + HashMap

**Time:** O(n) | **Space:** O(k)

```python
from collections import defaultdict

def length_of_longest_substring_k_distinct(s, k):
    left = 0
    count = defaultdict(int)
    max_len = 0

    for right in range(len(s)):
        count[s[right]] += 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len
```

**Explanation:**
Use a hash map to track frequency of characters and maintain at most `k` distinct.

---

Awesome! Let's move on to **Batch 13 (Q61–Q65)**, covering **2D Matrix Challenges and Binary Search Patterns** — both are essential for spatial data problems and optimization with sorted structures.

---

## ✅ **Batch 13 of 20 (Q61–Q65)**

---

### **Q61: Search a 2D Matrix**

**Problem:**
You are given a 2D matrix where each row is sorted and the first integer of each row is greater than the last integer of the previous row. Determine if a target value exists in the matrix.

**Example:**

```python
matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
], target = 3
```

Output: `True`

---

#### 🔹 Binary Search as 1D

**Time:** O(log(m×n)) | **Space:** O(1)

```python
def search_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    low, high = 0, m * n - 1

    while low <= high:
        mid = (low + high) // 2
        value = matrix[mid // n][mid % n]
        if value == target:
            return True
        elif value < target:
            low = mid + 1
        else:
            high = mid - 1

    return False
```

---

### **Q62: Kth Smallest Element in a Sorted Matrix**

**Problem:**
Given a `n x n` matrix where each row and column is sorted, return the kth smallest element.

**Example:**

```python
matrix = [
 [1, 5, 9],
 [10, 11, 13],
 [12, 13, 15]
], k = 8
```

Output: `13`

---

#### 🔹 Min Heap or Binary Search on Value

**Time:** O(n log(max - min)) | **Space:** O(1)

```python
def kth_smallest(matrix, k):
    n = len(matrix)
    low, high = matrix[0][0], matrix[-1][-1]

    def count_less_equal(x):
        count = 0
        row, col = n - 1, 0
        while row >= 0 and col < n:
            if matrix[row][col] <= x:
                count += row + 1
                col += 1
            else:
                row -= 1
        return count

    while low < high:
        mid = (low + high) // 2
        if count_less_equal(mid) < k:
            low = mid + 1
        else:
            high = mid
    return low
```

---

### **Q63: Median of Two Sorted Arrays**

**Problem:**
Find the median of two sorted arrays with combined O(log(min(n, m))) time.

**Example:**
Input: `nums1 = [1,3], nums2 = [2]` → Output: `2.0`

---

#### 🔹 Binary Search Partitioning

**Time:** O(log(min(n, m))) | **Space:** O(1)

```python
def find_median_sorted_arrays(nums1, nums2):
    A, B = nums1, nums2
    if len(A) > len(B):
        A, B = B, A

    m, n = len(A), len(B)
    total = m + n
    half = total // 2

    l, r = 0, m
    while l <= r:
        i = (l + r) // 2
        j = half - i

        Aleft = A[i - 1] if i > 0 else float('-inf')
        Aright = A[i] if i < m else float('inf')
        Bleft = B[j - 1] if j > 0 else float('-inf')
        Bright = B[j] if j < n else float('inf')

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1
```

---

### **Q64: Search in Rotated Sorted Array**

**Problem:**
Find target in rotated sorted array.

**Example:**
Input: `nums = [4,5,6,7,0,1,2], target = 0` → Output: `4`

---

#### 🔹 Modified Binary Search

**Time:** O(log n) | **Space:** O(1)

```python
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1
```

---

### **Q65: Find Peak Element**

**Problem:**
Find a peak element in the array where `nums[i] > nums[i+1]`.

**Example:**
Input: `[1,2,1,3,5,6,4]` → Output: index `5` or `1`

---

#### 🔹 Binary Search

**Time:** O(log n) | **Space:** O(1)

```python
def find_peak_element(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left
```

**Explanation:**
Move toward the larger neighbor until you find a peak.

---

Great! Let’s proceed with **Batch 14 (Q66–Q70)** focused on **Linked Lists and Two-Pointer Techniques** — key topics for pointer management, in-place updates, and recursive logic.

---

## ✅ **Batch 14 of 20 (Q66–Q70)**

---

### **Q66: Reverse a Linked List**

**Problem:**
Reverse a singly linked list.

**Example:**
Input: `1 → 2 → 3 → 4 → 5` → Output: `5 → 4 → 3 → 2 → 1`

---

#### 🔹 Iterative Two-Pointer

**Time:** O(n) | **Space:** O(1)

```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

---

#### 🔹 Recursive Approach

**Time:** O(n) | **Space:** O(n)

```python
def reverse_list(head):
    if not head or not head.next:
        return head
    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

---

### **Q67: Merge Two Sorted Lists**

**Problem:**
Merge two sorted linked lists into one sorted list.

**Example:**
`1 → 2 → 4`, `1 → 3 → 4` → Output: `1 → 1 → 2 → 3 → 4 → 4`

---

#### 🔹 Iterative Dummy Node

**Time:** O(n + m) | **Space:** O(1)

```python
def merge_two_lists(l1, l2):
    dummy = tail = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            tail.next, l1 = l1, l1.next
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
```

---

### **Q68: Detect Cycle in Linked List**

**Problem:**
Return `True` if a cycle is detected in a linked list.

---

#### 🔹 Floyd’s Tortoise and Hare

**Time:** O(n) | **Space:** O(1)

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

**Explanation:**
If a cycle exists, fast and slow pointers will meet.

---

### **Q69: Remove N-th Node From End**

**Problem:**
Remove the N-th node from the end of the list in one pass.

**Example:**
Input: `1 → 2 → 3 → 4 → 5`, n = 2 → Output: `1 → 2 → 3 → 5`

---

#### 🔹 Two-Pointer Gap Technique

**Time:** O(n) | **Space:** O(1)

```python
def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    first = second = dummy

    for _ in range(n + 1):
        first = first.next

    while first:
        first, second = first.next, second.next

    second.next = second.next.next
    return dummy.next
```

---

### **Q70: Palindrome Linked List**

**Problem:**
Check whether a linked list is a palindrome.

---

#### 🔹 Two Pointers + Reverse Half

**Time:** O(n) | **Space:** O(1)

```python
def is_palindrome(head):
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    # Check palindrome
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```

**Explanation:**
Find middle, reverse second half, compare both halves.

---

Perfect! Let’s move ahead with **Batch 15 (Q71–Q75)** focusing on **Trees and Binary Search Trees (BSTs)** — a core topic in coding rounds, especially for recursive and traversal-based problems.

---

## ✅ **Batch 15 of 20 (Q71–Q75)**

---

### **Q71: Maximum Depth of Binary Tree**

**Problem:**
Return the maximum depth of a binary tree.

**Example:**
Input:

```
    3
   / \
  9  20
     / \
    15  7
```

Output: `3`

---

#### 🔹 Recursive DFS

**Time:** O(n) | **Space:** O(h)

```python
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

---

### **Q72: Invert Binary Tree**

**Problem:**
Invert a binary tree (mirror it).

**Example:**
Input:

```
    4
   / \
  2   7
 / \ / \
1  3 6  9
```

Output:

```
    4
   / \
  7   2
 / \ / \
9  6 3  1
```

---

#### 🔹 Recursive Swap

**Time:** O(n) | **Space:** O(h)

```python
def invert_tree(root):
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```

---

### **Q73: Validate Binary Search Tree**

**Problem:**
Return `True` if a binary tree is a valid BST.

---

#### 🔹 DFS with Bounds

**Time:** O(n) | **Space:** O(h)

```python
def is_valid_bst(root):
    def helper(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (helper(node.left, low, node.val) and
                helper(node.right, node.val, high))
    return helper(root)
```

**Explanation:**
Each node must respect the min-max range passed down the tree.

---

### **Q74: Lowest Common Ancestor (LCA) in BST**

**Problem:**
Given a BST and two nodes `p` and `q`, return their lowest common ancestor.

---

#### 🔹 BST Navigation

**Time:** O(h) | **Space:** O(1)

```python
def lowest_common_ancestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
```

**Explanation:**
In a BST, if both are left or right, move accordingly; else root is the LCA.

---

### **Q75: Serialize and Deserialize Binary Tree**

**Problem:**
Serialize a tree to a string and deserialize it back.

---

#### 🔹 BFS (Level-Order Encoding)

**Time:** O(n) | **Space:** O(n)

```python
from collections import deque

class Codec:
    def serialize(self, root):
        if not root:
            return ""
        q = deque([root])
        result = []
        while q:
            node = q.popleft()
            if node:
                result.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                result.append("null")
        return ','.join(result)

    def deserialize(self, data):
        if not data:
            return None
        nodes = data.split(',')
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i += 1
            if nodes[i] != "null":
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i += 1
        return root
```

---

Great! Let’s continue with **Batch 16 (Q76–Q80)**, focusing on **Binary Tree Traversals and Path Problems** — these involve recursion, backtracking, and depth-first search, all of which are popular in CodeSignal and interview challenges.

---

## ✅ **Batch 16 of 20 (Q76–Q80)**

---

### **Q76: Binary Tree Inorder Traversal**

**Problem:**
Return the inorder traversal of a binary tree (left → root → right).

---

#### 🔹 Iterative with Stack

**Time:** O(n) | **Space:** O(n)

```python
def inorder_traversal(root):
    res, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res
```

---

### **Q77: Binary Tree Level Order Traversal**

**Problem:**
Return level-by-level (BFS) traversal of a binary tree.

---

#### 🔹 Queue + BFS

**Time:** O(n) | **Space:** O(n)

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    res, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level)
    return res
```

---

### **Q78: Path Sum (Has Path of Given Sum)**

**Problem:**
Given a binary tree and a target sum, return true if there is a root-to-leaf path with the sum.

---

#### 🔹 DFS Recursive

**Time:** O(n) | **Space:** O(h)

```python
def has_path_sum(root, target_sum):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target_sum
    return (has_path_sum(root.left, target_sum - root.val) or
            has_path_sum(root.right, target_sum - root.val))
```

---

### **Q79: All Root-to-Leaf Paths**

**Problem:**
Return all root-to-leaf paths in a binary tree.

**Example:**
For

```
    1
   / \
  2   3
   \
    5
```

Output: `["1->2->5", "1->3"]`

---

#### 🔹 DFS with Path String

**Time:** O(n) | **Space:** O(n)

```python
def binary_tree_paths(root):
    res = []

    def dfs(node, path):
        if not node:
            return
        if not node.left and not node.right:
            res.append(path + str(node.val))
            return
        dfs(node.left, path + str(node.val) + "->")
        dfs(node.right, path + str(node.val) + "->")

    dfs(root, "")
    return res
```

---

### **Q80: Diameter of Binary Tree**

**Problem:**
Return the length of the longest path between any two nodes in the tree.

---

#### 🔹 Postorder DFS with Height

**Time:** O(n) | **Space:** O(h)

```python
def diameter_of_binary_tree(root):
    diameter = 0

    def height(node):
        nonlocal diameter
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    height(root)
    return diameter
```

**Explanation:**
At every node, the path through it is `left + right`. Track the maximum.

---


Excellent! Now let’s move on to **Batch 17 (Q81–Q85)**, covering **Backtracking** — a vital topic for problems that involve exploring all possible solutions under constraints, including **Sudoku, N-Queens, Word Search, and combinations**.

---

## ✅ **Batch 17 of 20 (Q81–Q85)**

---

### **Q81: Word Search I**

**Problem:**
Given a grid of letters and a word, determine if the word exists in the grid. The word must be constructed from letters of sequentially adjacent cells (horizontally or vertically), without reusing a cell.

---

#### 🔹 DFS Backtracking

**Time:** O(m × n × L) | **Space:** O(L)

```python
def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False

        tmp, board[r][c] = board[r][c], '#'
        found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or
                 dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
        board[r][c] = tmp
        return found

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False
```

---

### **Q82: Sudoku Solver**

**Problem:**
Fill in the empty cells of a partially completed Sudoku board ('.' as placeholder).

---

#### 🔹 Backtracking + Validity Check

**Time:** O(9⁸²) worst | **Space:** O(1)

```python
def solve_sudoku(board):
    def is_valid(r, c, ch):
        for i in range(9):
            if board[r][i] == ch or board[i][c] == ch:
                return False
            if board[3*(r//3)+i//3][3*(c//3)+i%3] == ch:
                return False
        return True

    def solve():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    for ch in '123456789':
                        if is_valid(r, c, ch):
                            board[r][c] = ch
                            if solve():
                                return True
                            board[r][c] = '.'
                    return False
        return True

    solve()
```

---

### **Q83: N-Queens**

**Problem:**
Place `n` queens on an `n×n` board such that no two queens attack each other. Return all possible board configurations.

---

#### 🔹 Backtracking with Column & Diagonal Sets

**Time:** O(n!) | **Space:** O(n)

```python
def solve_n_queens(n):
    res = []
    cols = set()
    diag1 = set()
    diag2 = set()

    def backtrack(r, board):
        if r == n:
            res.append(board[:])
            return
        for c in range(n):
            if c in cols or (r-c) in diag1 or (r+c) in diag2:
                continue
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            board.append('.' * c + 'Q' + '.' * (n - c - 1))
            backtrack(r + 1, board)
            board.pop()
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0, [])
    return res
```

---

### **Q84: Combination Sum II (No Reuse of Elements)**

**Problem:**
Given `candidates` and a `target`, return all unique combinations that sum to `target`. Each number may be used only once.

---

#### 🔹 Backtracking + Skip Duplicates

**Time:** O(2ⁿ) | **Space:** O(n)

```python
def combination_sum2(candidates, target):
    res = []
    candidates.sort()

    def backtrack(start, path, total):
        if total == target:
            res.append(path[:])
            return
        if total > target:
            return
        prev = -1
        for i in range(start, len(candidates)):
            if candidates[i] == prev:
                continue
            path.append(candidates[i])
            backtrack(i + 1, path, total + candidates[i])
            path.pop()
            prev = candidates[i]

    backtrack(0, [], 0)
    return res
```

---

### **Q85: Restore IP Addresses**

**Problem:**
Given a string containing only digits, return all possible valid IP address combinations.

**Example:**
Input: `"25525511135"` → Output: `["255.255.11.135", "255.255.111.35"]`

---

#### 🔹 Backtracking + String Building

**Time:** O(1) | **Space:** O(1) (bounded by fixed IP parts)

```python
def restore_ip_addresses(s):
    res = []

    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                res.append('.'.join(path))
            return
        for end in range(start + 1, min(len(s), start + 4)):
            part = s[start:end]
            if (part.startswith('0') and len(part) > 1) or int(part) > 255:
                continue
            backtrack(end, path + [part])

    backtrack(0, [])
    return res
```

---

Great! Let's continue with **Batch 18 (Q86–Q90)** focused on **String Algorithms and Palindromic Patterns** — useful for problems involving symmetry, substrings, and DP-style string manipulation.

---

## ✅ **Batch 18 of 20 (Q86–Q90)**

---

### **Q86: Longest Palindromic Substring**

**Problem:**
Find the longest palindromic substring in a given string.

**Example:**
Input: `"babad"` → Output: `"bab"` or `"aba"`

---

#### 🔹 Expand Around Center

**Time:** O(n²) | **Space:** O(1)

```python
def longest_palindrome(s):
    res = ""

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    for i in range(len(s)):
        res = max(res, expand(i, i), expand(i, i+1), key=len)
    return res
```

**Explanation:**
Try all centers (odd and even), expand as long as valid.

---

### **Q87: Palindromic Substrings (Count All)**

**Problem:**
Count how many palindromic substrings exist in a string.

**Example:**
Input: `"aaa"` → Output: `6` (`"a"`, `"a"`, `"a"`, `"aa"`, `"aa"`, `"aaa"`)

---

#### 🔹 Expand Around Center

**Time:** O(n²) | **Space:** O(1)

```python
def count_substrings(s):
    count = 0

    def expand(l, r):
        nonlocal count
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1

    for i in range(len(s)):
        expand(i, i)
        expand(i, i + 1)

    return count
```

---

### **Q88: Longest Palindromic Subsequence**

**Problem:**
Return the length of the longest palindromic subsequence (not substring).

**Example:**
Input: `"bbbab"` → Output: `4` (`"bbbb"`)

---

#### 🔹 Dynamic Programming

**Time:** O(n²) | **Space:** O(n²)

```python
def longest_palindrome_subseq(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]

    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]
```

---

### **Q89: Regular Expression Matching**

**Problem:**
Implement `isMatch(s, p)` with `'.'` and `'*'` pattern rules.

---

#### 🔹 DP Matching

**Time:** O(m×n) | **Space:** O(m×n)

```python
def is_match(s, p):
    dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
    dp[0][0] = True

    for j in range(2, len(p)+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, len(s)+1):
        for j in range(1, len(p)+1):
            if p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2] or (dp[i-1][j] if p[j-2] in {s[i-1], '.'} else False)
    return dp[-1][-1]
```

---

### **Q90: Wildcard Matching (`?` and `*`)**

**Problem:**
`?` matches single char, `*` matches any sequence (including empty). Implement wildcard matching.

---

#### 🔹 DP with Memoization

**Time:** O(m×n) | **Space:** O(m×n)

```python
from functools import lru_cache

def is_match(s, p):
    @lru_cache(None)
    def dp(i, j):
        if j == len(p):
            return i == len(s)
        if i == len(s):
            return all(x == '*' for x in p[j:])
        if p[j] == '*':
            return dp(i, j+1) or dp(i+1, j)
        if p[j] == '?' or p[j] == s[i]:
            return dp(i+1, j+1)
        return False

    return dp(0, 0)
```

---

Great! Let’s continue with **Batch 19 (Q91–Q95)**, focusing on **Greedy String Compression, Encoding/Decoding, and Interleaving Strings** — these cover string parsing, pattern recognition, and dynamic state tracking.

---

## ✅ **Batch 19 of 20 (Q91–Q95)**

---

### **Q91: String Compression**

**Problem:**
Compress the string in-place using counts (e.g., `["a","a","b","b","c","c","c"]` → `["a","2","b","2","c","3"]`). Return the new length.

---

#### 🔹 Two Pointers

**Time:** O(n) | **Space:** O(1)

```python
def compress(chars):
    write = anchor = 0

    for read in range(len(chars)):
        if read + 1 == len(chars) or chars[read] != chars[read + 1]:
            chars[write] = chars[anchor]
            write += 1
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
            anchor = read + 1

    return write
```

---

### **Q92: Decode String**

**Problem:**
Decode a string like `"3[a2[c]]"` into `"accaccacc"`.

---

#### 🔹 Stack-Based Expansion

**Time:** O(n) | **Space:** O(n)

```python
def decode_string(s):
    stack = []
    curr_num = 0
    curr_str = ''

    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        elif c == '[':
            stack.append((curr_str, curr_num))
            curr_str, curr_num = '', 0
        elif c == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + num * curr_str
        else:
            curr_str += c

    return curr_str
```

---

### **Q93: Encode and Decode Strings (Design Problem)**

**Problem:**
Design methods to encode a list of strings to a single string and decode back.

---

#### 🔹 Length-Prefixed Encoding

**Time:** O(n) | **Space:** O(n)

```python
class Codec:
    def encode(self, strs):
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s):
        i, res = 0, []
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i + length])
            i += length
        return res
```

**Explanation:**
Use `length#value` as the encoding pattern to avoid delimiter conflicts.

---

### **Q94: Interleaving String**

**Problem:**
Check if `s3` is formed by interleaving `s1` and `s2`.

**Example:**
Input: `s1 = "aab", s2 = "axy", s3 = "aaxaby"` → Output: `True`

---

#### 🔹 DP Grid

**Time:** O(m×n) | **Space:** O(m×n)

```python
def is_interleave(s1, s2, s3):
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]
    dp[0][0] = True

    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i > 0 and s1[i-1] == s3[i+j-1]:
                dp[i][j] |= dp[i-1][j]
            if j > 0 and s2[j-1] == s3[i+j-1]:
                dp[i][j] |= dp[i][j-1]
    return dp[-1][-1]
```

---

### **Q95: Multiply Strings (Without Converting to Int)**

**Problem:**
Multiply two non-negative strings `"123"` × `"456"` and return `"56088"`.

---

#### 🔹 Digit-by-Digit Simulation

**Time:** O(m × n) | **Space:** O(m + n)

```python
def multiply(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"

    res = [0] * (len(num1) + len(num2))

    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            mul = int(num1[i]) * int(num2[j])
            pos1 = i + j
            pos2 = i + j + 1
            total = mul + res[pos2]

            res[pos1] += total // 10
            res[pos2] = total % 10

    result = ''.join(map(str, res)).lstrip('0')
    return result
```

**Explanation:**
Simulate manual multiplication and carry forward the digits.

---


Awesome! You’ve made it to the final stretch — here’s **Batch 20 (Q96–Q100)**, featuring **advanced and challenge-style problems** that test multiple concepts like DFS, DP, graphs, and simulations — similar to what you might see in CodeSignal's last question or harder interview rounds.

---

## ✅ **Batch 20 of 20 (Q96–Q100)**

---

### **Q96: Number of Distinct Islands**

**Problem:**
Given a 2D grid of 0s and 1s, return the number of distinct islands. Two islands are distinct if their shape is different (position-independent).

---

#### 🔹 DFS with Path Encoding

**Time:** O(m × n) | **Space:** O(m × n)

```python
def num_distinct_islands(grid):
    rows, cols = len(grid), len(grid[0])
    seen = set()

    def dfs(r, c, direction):
        if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0):
            return "O"
        grid[r][c] = 0
        return (direction +
                dfs(r + 1, c, "D") +
                dfs(r - 1, c, "U") +
                dfs(r, c + 1, "R") +
                dfs(r, c - 1, "L"))

    shapes = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                shape = dfs(r, c, "S")
                shapes.add(shape)
    return len(shapes)
```

---

### **Q97: Alien Dictionary (Topological Sort)**

**Problem:**
Given a list of words sorted lexicographically by an alien language, return a valid character order.

---

#### 🔹 Graph + Topological Sort

**Time:** O(V + E) | **Space:** O(V)

```python
from collections import defaultdict, deque

def alien_order(words):
    adj = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}

    for w1, w2 in zip(words, words[1:]):
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in adj[c1]:
                    adj[c1].add(c2)
                    indegree[c2] += 1
                break
        else:
            if len(w1) > len(w2):
                return ""

    q = deque([c for c in indegree if indegree[c] == 0])
    res = []
    while q:
        c = q.popleft()
        res.append(c)
        for nei in adj[c]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return ''.join(res) if len(res) == len(indegree) else ""
```

---

### **Q98: Regular Expression Matching with Wildcard Sets**

**Problem:**
Support custom matching where `.` = any one char, `*` = zero or more of the **previous character**.

---

#### 🔹 DP Table

**Time:** O(m × n) | **Space:** O(m × n)

```python
def is_match(s, p):
    m, n = len(s), len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True

    for j in range(2, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == '.' or p[j-1] == s[i-1]:
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                dp[i][j] = dp[i][j-2] or (dp[i-1][j] if s[i-1] == p[j-2] or p[j-2] == '.' else False)
    return dp[m][n]
```

---

### **Q99: Trapping Rain Water**

**Problem:**
Given an elevation map, compute how much water it can trap after raining.

---

#### 🔹 Two Pointer Accumulation

**Time:** O(n) | **Space:** O(1)

```python
def trap(height):
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water
```

---

### **Q100: The Skyline Problem**

**Problem:**
Given a list of buildings, return the key points of the skyline formed.

---

#### 🔹 Sweep Line + Max Heap

**Time:** O(n log n) | **Space:** O(n)

```python
import heapq

def get_skyline(buildings):
    events = []
    for L, R, H in buildings:
        events.append((L, -H, R))  # entering event
        events.append((R, 0, 0))   # exiting event

    events.sort()
    res = [[0, 0]]
    live = [(0, float("inf"))]

    for x, negH, R in events:
        while live[0][1] <= x:
            heapq.heappop(live)
        if negH:
            heapq.heappush(live, (negH, R))
        if res[-1][1] != -live[0][0]:
            res.append([x, -live[0][0]])
    return res[1:]
```

---

