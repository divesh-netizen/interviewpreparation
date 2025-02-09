Awesome! Let’s dive into the next three problems to keep the momentum going! 🚀  

---

### **Problem 4: Check if Two Strings Are Anagrams**  
#### Task:  
Write a function to check if two strings are anagrams (contain the same characters in the same frequency).  

---

#### **Base Approach**  
Sort both strings and compare them.  

```python
def are_anagrams_base(s1, s2):
    return sorted(s1) == sorted(s2)

# Example
print(are_anagrams_base("listen", "silent"))  # Output: True
print(are_anagrams_base("hello", "world"))    # Output: False
```  

**Complexity**:  
- Time: \(O(n \log n)\) (sorting both strings).  
- Space: \(O(n)\) (temporary sorted strings).  

---

#### **Optimized Approach**  
Use a frequency counter (dictionary) to compare character counts.  

```python
def are_anagrams_optimized(s1, s2):
    if len(s1) != len(s2):
        return False
    freq = {}
    for char in s1:
        freq[char] = freq.get(char, 0) + 1
    for char in s2:
        if char not in freq or freq[char] == 0:
            return False
        freq[char] -= 1
    return True

# Example
print(are_anagrams_optimized("listen", "silent"))  # Output: True
print(are_anagrams_optimized("hello", "world"))    # Output: False
```  

**Complexity**:  
- Time: \(O(n)\) (counting characters).  
- Space: \(O(1)\) (assuming limited character set).  

---

#### **Transition Steps**:  
1. The base approach sorts both strings, which is intuitive but not optimal.  
2. Observing that only character frequencies matter, we switch to counting characters with a dictionary for \(O(n)\) performance.  

---

### **Problem 5: Find All Pairs in an Array That Sum to a Target**  
#### Task:  
Given an array and a target sum, find all unique pairs of numbers that add up to the target.  

---

#### **Base Approach**  
Use two nested loops to check all possible pairs.  

```python
def find_pairs_base(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

# Example
print(find_pairs_base([1, 2, 3, 4, 5], 6))  # Output: [(1, 5), (2, 4)]
```  

**Complexity**:  
- Time: \(O(n^2)\) (nested loops).  
- Space: \(O(1)\) (no extra space used).  

---

#### **Optimized Approach**  
Use a set to track seen elements and find pairs in one pass.  

```python
def find_pairs_optimized(arr, target):
    seen = set()
    pairs = []
    for num in arr:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

# Example
print(find_pairs_optimized([1, 2, 3, 4, 5], 6))  # Output: [(2, 4), (1, 5)]
```  

**Complexity**:  
- Time: \(O(n)\) (one pass).  
- Space: \(O(n)\) (for the set).  

---

#### **Transition Steps**:  
1. The base approach uses brute force to check every pair.  
2. To optimize, we notice we can track complements in a set for constant-time lookups, reducing time complexity to \(O(n)\).  

---

### **Problem 6: Find the First Non-Repeating Character in a String**  
#### Task:  
Write a function to find the first character that doesn’t repeat in a string.  

---

#### **Base Approach**  
Use two loops: the first to pick a character and the second to check if it repeats.  

```python
def first_non_repeating_base(s):
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return s[i]
    return None

# Example
print(first_non_repeating_base("swiss"))  # Output: "w"
print(first_non_repeating_base("aabbcc"))  # Output: None
```  

**Complexity**:  
- Time: \(O(n^2)\) (nested loops due to `count`).  
- Space: \(O(1)\).  

---

#### **Optimized Approach**  
Use a dictionary to count character frequencies in one pass, then find the first character with a count of 1.  

```python
def first_non_repeating_optimized(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None

# Example
print(first_non_repeating_optimized("swiss"))  # Output: "w"
print(first_non_repeating_optimized("aabbcc"))  # Output: None
```  

**Complexity**:  
- Time: \(O(n)\) (two passes: one for counting, one for finding).  
- Space: \(O(1)\) (assuming limited character set).  

---

#### **Transition Steps**:  
1. The base approach checks each character’s frequency with `count()`, leading to redundant work.  
2. By counting frequencies in one pass and storing them in a dictionary, we reduce the time complexity significantly.  

---

Let me know if you'd like to continue or need further clarifications! 😊