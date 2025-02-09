Awesome! Here are **3 new problems** for today. Each comes with base and optimized approaches, plus explanations.  

---

### **Problem 13: Longest Consecutive Sequence**  
#### **Task**  
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.  
Example:  
Input: `nums = [100, 4, 200, 1, 3, 2]`  
Output: `4` (Because `[1,2,3,4]` is the longest consecutive sequence)  

---

#### **Base Approach (Sorting and Checking Consecutiveness)**  
Sort the array and count consecutive sequences.  

**Steps**:  
1. Sort the array.  
2. Iterate through it, checking if the next number is consecutive.  
3. Maintain a counter for consecutive elements.  

```python
def longest_consecutive_base(nums):
    if not nums:
        return 0

    nums.sort()
    longest, current = 1, 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current += 1
        elif nums[i] != nums[i - 1]:  # Avoid duplicates
            longest = max(longest, current)
            current = 1

    return max(longest, current)

# Example
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_base(nums))  # Output: 4
```  

**Complexity:**  
- Time: \(O(n \log n)\) (Sorting takes \(O(n \log n)\))  
- Space: \(O(1)\)  

---

#### **Optimized Approach (Using HashSet for O(n) solution)**  
Store numbers in a set and check for sequence starting points.  

**Steps**:  
1. Insert all numbers into a **set** for \(O(1)\) lookups.  
2. Iterate through each number. If it’s the **start of a sequence** (`num - 1` is not in the set), start counting.  
3. Track the longest sequence.  

```python
def longest_consecutive_optimized(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # Start of a sequence
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest

# Example
nums = [100, 4, 200, 1, 3, 2]
print(longest_consecutive_optimized(nums))  # Output: 4
```  

**Complexity:**  
- Time: \(O(n)\)  
- Space: \(O(n)\)  

---

### **Problem 14: Container With Most Water**  
#### **Task**  
Given an array where `height[i]` represents the height of a vertical line, find two lines that form a container holding the most water.  
Example:  
Input: `height = [1,8,6,2,5,4,8,3,7]`  
Output: `49`  

---

#### **Base Approach (Brute Force - Checking All Pairs)**  
Try all pairs of lines and calculate the area.  

**Steps**:  
1. Iterate over each pair of lines.  
2. Compute the area as `min(height[i], height[j]) * (j - i)`.  
3. Track the maximum area.  

```python
def max_area_base(height):
    max_water = 0
    n = len(height)

    for i in range(n):
        for j in range(i + 1, n):
            max_water = max(max_water, min(height[i], height[j]) * (j - i))

    return max_water

# Example
height = [1,8,6,2,5,4,8,3,7]
print(max_area_base(height))  # Output: 49
```  

**Complexity:**  
- Time: \(O(n^2)\)  
- Space: \(O(1)\)  

---

#### **Optimized Approach (Two-Pointer Method)**  
Move two pointers inward to find the max area efficiently.  

**Steps**:  
1. Use two pointers (`left` at `0`, `right` at `n-1`).  
2. Compute the area, update max area if needed.  
3. Move the smaller-height pointer inward.  

```python
def max_area_optimized(height):
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        max_water = max(max_water, min(height[left], height[right]) * (right - left))
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Example
height = [1,8,6,2,5,4,8,3,7]
print(max_area_optimized(height))  # Output: 49
```  

**Complexity:**  
- Time: \(O(n)\)  
- Space: \(O(1)\)  

---

### **Problem 15: Subarray Sum Equals K**  
#### **Task**  
Given an array of integers and an integer `k`, find the total number of continuous subarrays whose sum equals `k`.  
Example:  
Input: `nums = [1,1,1], k = 2`  
Output: `2`  

---

#### **Base Approach (Brute Force - Checking All Subarrays)**  
Try all possible subarrays and check their sum.  

**Steps**:  
1. Iterate over all start indices.  
2. Iterate over all end indices, summing elements.  
3. If the sum equals `k`, count the subarray.  

```python
def subarray_sum_base(nums, k):
    count = 0
    n = len(nums)

    for start in range(n):
        total = 0
        for end in range(start, n):
            total += nums[end]
            if total == k:
                count += 1

    return count

# Example
nums = [1,1,1]
k = 2
print(subarray_sum_base(nums, k))  # Output: 2
```  

**Complexity:**  
- Time: \(O(n^2)\)  
- Space: \(O(1)\)  

---

#### **Optimized Approach (Using HashMap for \(O(n)\) solution)**  
Use a hashmap to store cumulative sums and count subarrays efficiently.  

**Steps**:  
1. Keep a cumulative sum and store its occurrences in a hashmap.  
2. If `current_sum - k` exists in the hashmap, add its count to the result.  

```python
def subarray_sum_optimized(nums, k):
    count = 0
    prefix_sum = 0
    prefix_map = {0: 1}

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

    return count

# Example
nums = [1,1,1]
k = 2
print(subarray_sum_optimized(nums, k))  # Output: 2
```  

**Complexity:**  
- Time: \(O(n)\)  
- Space: \(O(n)\)  

---

### **File Name for Today**  
**`day5_sequence_container_subarray.py`**  

Let me know when you're ready for the next set! 🚀