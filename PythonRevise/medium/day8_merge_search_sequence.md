Here are **3 new problems** for today with base and optimized solutions. 🚀  

---

### **Problem 22: Merge Intervals**  
#### **Task**  
Given a list of intervals `[[start1, end1], [start2, end2], ...]`, merge all overlapping intervals.  

**Example:**  
Input: `intervals = [[1,3],[2,6],[8,10],[15,18]]`  
Output: `[[1,6],[8,10],[15,18]]`  

---

#### **Base Approach (Brute Force - Sorting & Checking)**  
1. Sort the intervals by **start time**.  
2. Compare each interval with the next, merging if they overlap.  

```python
def merge_intervals_base(intervals):
    intervals.sort()  # Sort based on start time
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:  # No overlap
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])  # Merge

    return merged

# Example
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals_base(intervals))  # Output: [[1,6],[8,10],[15,18]]
```  

**Complexity:**  
- **O(n log n)** (Sorting dominates)  
- **O(n)** (Result storage)  

---

#### **Optimized Approach (Using Stack - Better for Large Inputs)**  
1. Sort intervals.  
2. Use a **stack** to track merged intervals efficiently.  

```python
def merge_intervals_optimized(intervals):
    intervals.sort()
    stack = [intervals[0]]

    for i in range(1, len(intervals)):
        if stack[-1][1] >= intervals[i][0]:  # Overlap
            stack[-1][1] = max(stack[-1][1], intervals[i][1])
        else:
            stack.append(intervals[i])

    return stack

# Example
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals_optimized(intervals))  # Output: [[1,6],[8,10],[15,18]]
```  

**Complexity:**  
- **O(n log n)** (Sorting)  
- **O(n)** (Stack)  

---

### **Problem 23: Search in Rotated Sorted Array**  
#### **Task**  
Given a **rotated sorted array** and a target value, find the target’s index.  
If not found, return `-1`.  

**Example:**  
Input: `nums = [4,5,6,7,0,1,2], target = 0`  
Output: `4`  

---

#### **Base Approach (Linear Search - O(n))**  
Simply iterate and find the target.  

```python
def search_rotated_base(nums, target):
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1

# Example
nums = [4,5,6,7,0,1,2]
target = 0
print(search_rotated_base(nums, target))  # Output: 4
```  

**Complexity:**  
- **O(n)**  

---

#### **Optimized Approach (Binary Search - O(log n))**  
1. Identify the **sorted half** of the array.  
2. Perform **binary search** in that half.  

```python
def search_rotated_optimized(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:  
                right = mid - 1  # Search left
            else:
                left = mid + 1  # Search right

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:  
                left = mid + 1  # Search right
            else:
                right = mid - 1  # Search left

    return -1

# Example
nums = [4,5,6,7,0,1,2]
target = 0
print(search_rotated_optimized(nums, target))  # Output: 4
```  

**Complexity:**  
- **O(log n)** (Binary search)  
- **O(1)** (No extra space)  

---

### **Problem 24: Longest Consecutive Sequence**  
#### **Task**  
Find the **length of the longest consecutive sequence** in an unsorted array.  

**Example:**  
Input: `nums = [100,4,200,1,3,2]`  
Output: `4` (Because `[1,2,3,4]` is the longest sequence)  

---

#### **Base Approach (Sorting - O(n log n))**  
1. Sort the array.  
2. Iterate and count consecutive sequences.  

```python
def longest_consecutive_base(nums):
    if not nums:
        return 0

    nums = sorted(set(nums))  # Remove duplicates and sort
    longest, current = 1, 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current += 1
        else:
            longest = max(longest, current)
            current = 1

    return max(longest, current)

# Example
nums = [100,4,200,1,3,2]
print(longest_consecutive_base(nums))  # Output: 4
```  

**Complexity:**  
- **O(n log n)** (Sorting)  

---

#### **Optimized Approach (Using Set - O(n))**  
1. Convert `nums` to a **set**.  
2. Start counting sequences from numbers that have no **previous number**.  

```python
def longest_consecutive_optimized(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # Start of a sequence
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest

# Example
nums = [100,4,200,1,3,2]
print(longest_consecutive_optimized(nums))  # Output: 4
```  

**Complexity:**  
- **O(n)** (Each number is processed once)  

---

### **File Name for Today**  
**`day8_merge_search_sequence.py`**  

Let me know when you're ready for the next set! 🚀