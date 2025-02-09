
---

### **Problem 7: Reverse Words in a String**  
#### Task:  
Given a string, reverse the order of words. Words are separated by spaces.  

---

#### **Base Approach**  
Split the string into words, reverse the list of words, and join them back.  

```python
def reverse_words_base(s):
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

# Example
print(reverse_words_base("Hello World"))  # Output: "World Hello"
print(reverse_words_base("Python is great"))  # Output: "great is Python"
```  

**Complexity**:  
- Time: \(O(n)\) (splitting and joining).  
- Space: \(O(n)\) (temporary list of words).  

---

#### **Optimized Approach**  
Process the string in-place by identifying word boundaries and reversing the words directly (saves on splitting and extra storage).  

```python
def reverse_words_optimized(s):
    def reverse_section(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    arr = list(s)
    n = len(arr)
    reverse_section(arr, 0, n - 1)  # Reverse the entire string
    
    start = 0
    for end in range(n + 1):
        if end == n or arr[end] == " ":
            reverse_section(arr, start, end - 1)  # Reverse each word
            start = end + 1
    
    return "".join(arr)

# Example
print(reverse_words_optimized("Hello World"))  # Output: "World Hello"
print(reverse_words_optimized("Python is great"))  # Output: "great is Python"
```  

**Complexity**:  
- Time: \(O(n)\) (one pass for reversing the string and another for reversing each word).  
- Space: \(O(1)\) (in-place operation).  

---

#### **Transition Steps**:  
1. The base approach splits and reverses the string, which is simple but uses additional space.  
2. The optimized approach processes the string in-place using pointer manipulation to save space.  

---

### **Problem 8: Merge Two Sorted Arrays**  
#### Task:  
Merge two sorted arrays into one sorted array without using extra space.  

---

#### **Base Approach**  
Merge using a new list and sort the result.  

```python
def merge_sorted_base(arr1, arr2):
    return sorted(arr1 + arr2)

# Example
print(merge_sorted_base([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(merge_sorted_base([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
```  

**Complexity**:  
- Time: \(O((n + m) \log (n + m))\) (sorting the combined array).  
- Space: \(O(n + m)\) (new array).  

---

#### **Optimized Approach**  
Use a two-pointer technique to merge the arrays in-place.  

```python
def merge_sorted_optimized(arr1, arr2):
    i, j, k = len(arr1) - 1, len(arr2) - 1, len(arr1) + len(arr2) - 1
    arr1.extend([0] * len(arr2))  # Extend arr1 to hold both arrays
    
    while j >= 0:
        if i >= 0 and arr1[i] > arr2[j]:
            arr1[k] = arr1[i]
            i -= 1
        else:
            arr1[k] = arr2[j]
            j -= 1
        k -= 1
    return arr1

# Example
print(merge_sorted_optimized([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
print(merge_sorted_optimized([1, 2, 3], [4, 5, 6]))  # Output: [1, 2, 3, 4, 5, 6]
```  

**Complexity**:  
- Time: \(O(n + m)\) (one pass through both arrays).  
- Space: \(O(1)\) (in-place operation).  

---

#### **Transition Steps**:  
1. The base approach merges and sorts, which is easy but inefficient for sorted arrays.  
2. The optimized approach uses two pointers to merge in linear time.  

---

### **Problem 9: Count Subarrays with a Given Sum**  
#### Task:  
Find the number of contiguous subarrays that sum to a given value \(k\).  

---

#### **Base Approach**  
Use two loops to calculate the sum for every subarray.  

```python
def count_subarrays_base(arr, k):
    count = 0
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            if curr_sum == k:
                count += 1
    return count

# Example
print(count_subarrays_base([1, 1, 1], 2))  # Output: 2
print(count_subarrays_base([1, 2, 3], 3))  # Output: 2
```  

**Complexity**:  
- Time: \(O(n^2)\) (nested loops for subarray sums).  
- Space: \(O(1)\).  

---

#### **Optimized Approach**  
Use a hash map to store prefix sums and reduce the problem to \(O(n)\).  

```python
def count_subarrays_optimized(arr, k):
    prefix_sum = {0: 1}
    curr_sum = 0
    count = 0
    for num in arr:
        curr_sum += num
        if curr_sum - k in prefix_sum:
            count += prefix_sum[curr_sum - k]
        prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1
    return count

# Example
print(count_subarrays_optimized([1, 1, 1], 2))  # Output: 2
print(count_subarrays_optimized([1, 2, 3], 3))  # Output: 2
```  

**Complexity**:  
- Time: \(O(n)\) (single pass).  
- Space: \(O(n)\) (hash map).  

---

#### **Transition Steps**:  
1. The base approach iterates through all subarrays, making it slow.  
2. The optimized approach uses prefix sums and a hash map to track required subarray sums efficiently.  

---

### **File Name**  
**`day3_reverse_merge_subarray.py`**  

Let me know if you'd like to dive into another set or discuss anything! 😊