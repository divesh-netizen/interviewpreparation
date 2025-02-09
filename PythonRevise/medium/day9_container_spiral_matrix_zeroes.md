Here are **3 new problems** for today with base and optimized solutions. 🚀  

---

### **Problem 25: Container With Most Water**  
#### **Task**  
You are given an array `height` of positive integers. Each integer represents the height of a vertical line at that position. Find two lines that together with the x-axis form a container, such that the container contains the most water.  

**Example:**  
Input: `height = [1,8,6,2,5,4,8,3,7]`  
Output: `49`  

---

#### **Base Approach (Brute Force - O(n²))**  
1. Compare every pair of lines and calculate the area formed by them.  
2. Keep track of the maximum area.  

```python
def max_area_base(height):
    n = len(height)
    max_area = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, area)
    
    return max_area

# Example
height = [1,8,6,2,5,4,8,3,7]
print(max_area_base(height))  # Output: 49
```  

**Complexity:**  
- Time: **O(n²)** (Brute force comparison of all pairs)  
- Space: **O(1)**  

---

#### **Optimized Approach (Two Pointers - O(n))**  
1. Use two pointers: one at the beginning and one at the end of the array.  
2. Calculate the area and move the pointer corresponding to the shorter line.  

```python
def max_area_optimized(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example
height = [1,8,6,2,5,4,8,3,7]
print(max_area_optimized(height))  # Output: 49
```  

**Complexity:**  
- Time: **O(n)** (One pass with two pointers)  
- Space: **O(1)**  

---

### **Problem 26: Spiral Matrix**  
#### **Task**  
Given an `m x n` matrix, return all elements of the matrix in spiral order.  

**Example:**  
Input: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`  
Output: `[1,2,3,6,9,8,7,4,5]`  

---

#### **Base Approach (Simulate the Spiral - O(m*n))**  
1. Traverse in the four directions (right, down, left, up) using boundary checks.  
2. Keep shrinking the matrix after each complete traversal.  

```python
def spiral_order_base(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)  # Take the first row (right direction)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())  # Take the last element of each row (down direction)
        if matrix:
            result += matrix.pop()[::-1]  # Take the last row (left direction)
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))  # Take the first element of each row (up direction)
    return result

# Example
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_order_base(matrix))  # Output: [1,2,3,6,9,8,7,4,5]
```  

**Complexity:**  
- Time: **O(m * n)** (Every element is visited once)  
- Space: **O(m * n)** (To store the result)  

---

#### **Optimized Approach (In-place Spiral)**  
1. Use four boundaries (top, bottom, left, right) to avoid the need to pop elements.  
2. Traverse and adjust the boundaries as the matrix shrinks.  

```python
def spiral_order_optimized(matrix):
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])  # Traverse right
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])  # Traverse down
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])  # Traverse left
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])  # Traverse up
            left += 1

    return result

# Example
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_order_optimized(matrix))  # Output: [1,2,3,6,9,8,7,4,5]
```  

**Complexity:**  
- Time: **O(m * n)**  
- Space: **O(1)** (In-place)  

---

### **Problem 27: Set Matrix Zeroes**  
#### **Task**  
If an element in an `m x n` matrix is `0`, set its entire row and column to `0`.  

**Example:**  
Input:  
```
matrix = [[1,1,1],[1,0,1],[1,1,1]]
```  
Output:  
```
matrix = [[1,0,1],[0,0,0],[1,0,1]]
```  

---

#### **Base Approach (Extra Space - O(m*n))**  
1. Use two sets to keep track of rows and columns that need to be zeroed.  
2. Traverse the matrix and mark the rows and columns with `0`.  

```python
def set_zeroes_base(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0

# Example
matrix = [[1,1,1],[1,0,1],[1,1,1]]
set_zeroes_base(matrix)
print(matrix)  # Output: [[1,0,1],[0,0,0],[1,0,1]]
```  

**Complexity:**  
- Time: **O(m * n)**  
- Space: **O(m + n)** (For row and column sets)  

---

#### **Optimized Approach (In-place - O(1) extra space)**  
1. Use the first row and first column of the matrix itself to mark the zeroes.  
2. Avoid using extra space.  

```python
def set_zeroes_optimized(matrix):
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero, first_col_zero = False, False

    # Check if first row needs to be zeroed
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    # Check if first column needs to be zeroed
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
            break

    # Use first row and column to mark zeroes for other cells
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero out the matrix based on the marks
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Zero the first row if necessary
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Zero the first column if necessary
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0

# Example
matrix = [[1,1,1],[1,0,1],[1,1,1]]
set_zeroes_optimized(matrix)
print(matrix)  # Output: [[1,0,1],[0,0,0],[1,0,1]]
```  

**Complexity:**  
- Time: **O(m * n)**  
- Space: **O(1)** (In-place)  

---

### **File Name for Today**  
**`day9_container_spiral_matrix_zeroes.py`**  

Let me know when you're ready for the next set! 🚀