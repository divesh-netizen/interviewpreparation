Here are your **3 new questions** for today. Each includes an example solution, base approach steps, and the corresponding optimized approach.

---

### **Problem 7: Merge Intervals**  
#### **Task**  
Given a collection of intervals, merge all overlapping intervals.  
Example:  
Input: `[[1,3], [2,6], [8,10], [15,18]]`  
Output: `[[1,6], [8,10], [15,18]]`  

---

#### **Base Approach (Brute Force)**  
Sort the intervals and then compare each interval to see if it overlaps with the next one. If they do, merge them.  

**Steps**:  
1. Sort the intervals based on the starting value of each interval.
2. Loop through the sorted list:
   - If the current interval overlaps with the next one, merge them.
   - If not, add the current interval to the result.
  
```python
def merge_intervals_base(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort by the first element
    result = [intervals[0]]  # Start with the first interval
    
    for i in range(1, len(intervals)):
        current = intervals[i]
        last = result[-1]
        
        # If intervals overlap, merge them
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            result.append(current)
    
    return result

# Example
intervals = [[1,3], [2,6], [8,10], [15,18]]
print(merge_intervals_base(intervals))  # Output: [[1,6], [8,10], [15,18]]
```  

**Complexity:**  
- Time: \(O(n \log n)\) due to sorting.  
- Space: \(O(n)\) for the result.  

---

#### **Optimized Approach**  
The base approach is already optimized as we are using sorting and merging intervals in one pass.  

**Explanation**:  
1. Sorting ensures that the intervals are processed in order of their starting points.
2. A single pass through the sorted intervals is all that's needed to merge them efficiently.  

```python
# Same code as the base approach, already optimal
def merge_intervals_optimized(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort by the first element
    result = [intervals[0]]  # Start with the first interval
    
    for i in range(1, len(intervals)):
        current = intervals[i]
        last = result[-1]
        
        # If intervals overlap, merge them
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            result.append(current)
    
    return result

# Example
intervals = [[1,3], [2,6], [8,10], [15,18]]
print(merge_intervals_optimized(intervals))  # Output: [[1,6], [8,10], [15,18]]
```  

---

### **Problem 8: Rotate Image (Matrix Rotation)**  
#### **Task**  
Given an \(n \times n\) 2D matrix, rotate the matrix by 90 degrees (clockwise).  
Example:  
Input:  
```
[
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```  
Output:  
```
[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
```

---

#### **Base Approach (Brute Force)**  
Transpose the matrix, then reverse each row.  

**Steps**:  
1. Transpose the matrix (convert rows to columns).
2. Reverse each row to achieve a 90-degree clockwise rotation.
  
```python
def rotate_image_base(matrix):
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for row in matrix:
        row.reverse()
    
    return matrix

# Example
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(rotate_image_base(matrix))  
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```  

**Complexity:**  
- Time: \(O(n^2)\) for transposing and reversing rows.  
- Space: \(O(1)\) for in-place operations.  

---

#### **Optimized Approach**  
The base approach is already optimized with an in-place solution, so no additional optimization is necessary.

---

### **Problem 9: Find Peak Element**  
#### **Task**  
An element is a peak if it is greater than or equal to its neighbors. Find a peak element in an array.  
Example:  
Input: `[1, 2, 3, 1]`  
Output: `3` (peak at index 2)

---

#### **Base Approach (Brute Force)**  
Traverse the array and check if each element is greater than or equal to its neighbors.

**Steps**:  
1. Loop through each element in the array.
2. Check if the element is greater than or equal to its neighbors.
3. Return the element if it satisfies the peak condition.
  
```python
def find_peak_element_base(nums):
    n = len(nums)
    for i in range(n):
        if (i == 0 or nums[i] >= nums[i - 1]) and (i == n - 1 or nums[i] >= nums[i + 1]):
            return nums[i]
    return -1

# Example
nums = [1, 2, 3, 1]
print(find_peak_element_base(nums))  # Output: 3
```  

**Complexity:**  
- Time: \(O(n)\) to check all elements.  
- Space: \(O(1)\) for in-place comparison.  

---

#### **Optimized Approach (Binary Search)**  
Use binary search to find a peak in \(O(\log n)\).  
The idea is to explore the middle element and compare it with its neighbors. Based on that comparison, choose the direction to search.  

**Steps**:  
1. Start with the middle element.
2. If it's a peak, return it.
3. If the middle element is smaller than the next element, search the right half.
4. If it's smaller than the previous element, search the left half.  

```python
def find_peak_element_optimized(nums):
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if (mid == 0 or nums[mid - 1] <= nums[mid]) and (mid == len(nums) - 1 or nums[mid + 1] <= nums[mid]):
            return nums[mid]
        elif mid > 0 and nums[mid - 1] > nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1

# Example
nums = [1, 2, 3, 1]
print(find_peak_element_optimized(nums))  # Output: 3
```  

**Complexity:**  
- Time: \(O(\log n)\) due to binary search.  
- Space: \(O(1)\) for in-place comparison.  

---

### **File Name for Today**  
**`day3_merge_rotate_peak.py`**  

Let me know when you’re ready for the next set of problems! 😊