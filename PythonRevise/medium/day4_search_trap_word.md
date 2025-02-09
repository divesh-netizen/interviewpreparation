Here are your **3 new problems** for today. Each includes an example solution, base approach steps, and an optimized approach.  

---

### **Problem 10: Search in Rotated Sorted Array**  
#### **Task**  
You are given a rotated sorted array and a target. Find the index of the target in \(O(\log n)\) time.  
Example:  
Input: `nums = [4,5,6,7,0,1,2], target = 0`  
Output: `4`  

---

#### **Base Approach (Linear Search - Brute Force)**  
Check every element in the array until we find the target.  

**Steps**:  
1. Iterate through the array.  
2. If the element matches the target, return the index.  
3. If not found, return `-1`.  

```python
def search_base(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

# Example
nums = [4,5,6,7,0,1,2]
target = 0
print(search_base(nums, target))  # Output: 4
```  

**Complexity:**  
- Time: \(O(n)\)  
- Space: \(O(1)\)  

---

#### **Optimized Approach (Binary Search in Rotated Array)**  
Use binary search by identifying the sorted half of the array.  

**Steps**:  
1. Find the middle element.  
2. If `mid` is the target, return `mid`.  
3. If the left half is sorted:
   - Check if the target lies within the left half; if yes, search left, else search right.  
4. If the right half is sorted:
   - Check if the target lies within the right half; if yes, search right, else search left.  

```python
def search_optimized(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

# Example
nums = [4,5,6,7,0,1,2]
target = 0
print(search_optimized(nums, target))  # Output: 4
```  

**Complexity:**  
- Time: \(O(\log n)\)  
- Space: \(O(1)\)  

---

### **Problem 11: Trapping Rain Water**  
#### **Task**  
Given an array of heights representing walls, compute the total water trapped.  
Example:  
Input: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`  
Output: `6`  

---

#### **Base Approach (Brute Force - Checking Every Element)**  
For each bar, find the maximum height to the left and right, and calculate the trapped water.  

**Steps**:  
1. For each element, find the highest bar to the left and right.  
2. The trapped water at an index is `min(left_max, right_max) - height[i]`.  
3. Sum up the trapped water for all indices.  

```python
def trap_base(height):
    n = len(height)
    water = 0
    
    for i in range(n):
        left_max = max(height[:i+1])
        right_max = max(height[i:])
        water += min(left_max, right_max) - height[i]

    return water

# Example
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap_base(height))  # Output: 6
```  

**Complexity:**  
- Time: \(O(n^2)\)  
- Space: \(O(1)\)  

---

#### **Optimized Approach (Two-Pointer Method)**  
Use two pointers to keep track of max heights and compute trapped water efficiently.  

**Steps**:  
1. Use two pointers (`left` and `right`).  
2. Track `left_max` and `right_max`.  
3. Move the pointer with a lower height and compute water trapped.  

```python
def trap_optimized(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += max(0, left_max - height[left])
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += max(0, right_max - height[right])

    return water

# Example
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap_optimized(height))  # Output: 6
```  

**Complexity:**  
- Time: \(O(n)\)  
- Space: \(O(1)\)  

---

### **Problem 12: Word Search**  
#### **Task**  
Given an \(m \times n\) board and a word, check if the word exists in the board (adjacent letters can be used but cannot be reused).  
Example:  
Input:  
```python
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
```
Output: `True`  

---

#### **Base Approach (Backtracking - Brute Force)**  
Use DFS to explore all possible paths.  

**Steps**:  
1. Start from each cell in the board.  
2. If the first letter matches, call DFS to check all possible paths.  
3. Use backtracking to mark visited cells and restore them after recursion.  

```python
def exist_base(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False

        temp = board[r][c]
        board[r][c] = "#"  # Mark visited

        found = (dfs(r + 1, c, index + 1) or
                 dfs(r - 1, c, index + 1) or
                 dfs(r, c + 1, index + 1) or
                 dfs(r, c - 1, index + 1))

        board[r][c] = temp  # Restore the board
        return found

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True

    return False

# Example
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
print(exist_base(board, word))  # Output: True
```  

**Complexity:**  
- Time: \(O(m \times n \times 4^k)\)  
- Space: \(O(k)\) (recursion depth).  

---

### **File Name for Today**  
**`day4_search_trap_word.py`**  

Let me know when you’re ready for the next set of problems! 🚀