def twoSum(nums, target):
    # Step 1: Initialize an empty dictionary called `seen`.
    seen = {}
    
    # Step 2: Loop through each element in `nums` using `enumerate` to get both the index and the value.
    for i, num in enumerate(nums):
        
        # Step 3: Calculate the `complement` of the current number.
        # The `complement` is the value we need to find in the array to reach the target sum.
        complement = target - num
        
        # Step 4: Check if the `complement` is in the `seen` dictionary.
        # If it is, that means we have already encountered a number that, together with `num`, makes the target.
        if complement in seen:
            # If the complement is found, return the index of `complement` from `seen` and the current index `i`.
            return [seen[complement], i]
        
        # Step 5: If `complement` is not in `seen`, add the current number `num` to `seen` with its index `i`.
        # This allows us to quickly check for `complement` in future iterations.
        seen[num] = i


nums = [2, 7, 11, 15]
target = 9
indices = twoSum(nums,target)
print(indices,f"The numbers are {indices[0]} and {indices[1]}")#returns the indices
