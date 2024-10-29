Here are 10 popular array-related questions from LeetCode that are often asked in coding interviews, along with detailed Python solutions:

### 1. **Two Sum**
- **Problem:** Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the target.  
  **Assumption:** Each input has exactly one solution, and you may not use the same element twice.

- **Solution:**
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```
- **Explanation:**  
  We use a dictionary to store each number and its index. For each number, we check if the difference between the target and the current number exists in the dictionary. If it does, we return the indices of the two numbers.

### 2. **Best Time to Buy and Sell Stock**
- **Problem:** You are given an array where each element represents the price of a stock on a particular day. Find the maximum profit you can achieve by buying and then selling. You must buy before you sell.

- **Solution:**
```python
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
```
- **Explanation:**  
  Keep track of the minimum price seen so far and compute the potential profit for each day by subtracting the current price from the minimum price. Update the maximum profit whenever a higher profit is found.

### 3. **Contains Duplicate**
- **Problem:** Given an array of integers, determine if any value appears at least twice.

- **Solution:**
```python
def contains_duplicate(nums):
    return len(nums) != len(set(nums))
```
- **Explanation:**  
  Convert the list to a set (which removes duplicates) and compare the length. If the lengths are different, the array contains duplicates.

### 4. **Product of Array Except Self**
- **Problem:** Given an array `nums`, return an array `answer` such that `answer[i]` is the product of all the elements except `nums[i]`.

- **Solution:**
```python
def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]
    right_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]
    return answer
```
- **Explanation:**  
  First pass through the array builds the product of all numbers to the left of each element. The second pass multiplies by the product of all numbers to the right.

### 5. **Maximum Subarray**
- **Problem:** Find the contiguous subarray (containing at least one number) that has the largest sum and return its sum.

- **Solution:**
```python
def max_subarray(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global
```
- **Explanation:**  
  This is Kadane's algorithm. At each step, decide whether to start a new subarray at the current element or extend the existing subarray. Track the maximum sum encountered.

### 6. **Find Minimum in Rotated Sorted Array**
- **Problem:** Suppose an array is sorted in ascending order and then rotated at an unknown pivot. Find the minimum element.

- **Solution:**
```python
def find_min(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
```
- **Explanation:**  
  Use binary search to find the minimum element by comparing the middle element to the rightmost element. Adjust the search range accordingly.

### 7. **Search in Rotated Sorted Array**
- **Problem:** Given a rotated sorted array and a target value, return the index if found. Otherwise, return -1.

- **Solution:**
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
- **Explanation:**  
  Use binary search by determining if the target lies in the sorted portion of the array, either on the left or right side.

### 8. **Merge Intervals**
- **Problem:** Given a collection of intervals, merge overlapping intervals.

- **Solution:**
```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
```
- **Explanation:**  
  Sort intervals by the start value, then merge intervals by checking if they overlap with the previous merged interval.

### 9. **Insert Interval**
- **Problem:** Given a set of non-overlapping intervals and a new interval, insert the new interval and merge if necessary.

- **Solution:**
```python
def insert(intervals, new_interval):
    result = []
    for interval in intervals:
        if interval[1] < new_interval[0]:
            result.append(interval)
        elif interval[0] > new_interval[1]:
            result.append(new_interval)
            new_interval = interval
        else:
            new_interval[0] = min(new_interval[0], interval[0])
            new_interval[1] = max(new_interval[1], interval[1])
    result.append(new_interval)
    return result
```
- **Explanation:**  
  Add intervals to the result list while merging overlapping intervals with the new one.

### 10. **3Sum**
- **Problem:** Given an array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

- **Solution:**
```python
def three_sum(nums):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result
```
- **Explanation:**  
  Sort the array, then for each element, use the two-pointer technique to find triplets that sum to zero.

These are essential array problems that help sharpen problem-solving and algorithmic thinking, often appearing in coding interviews.
