# import two_sum

name = "tach"
print(f"my name is {name}")
def two_sum(nums_array, target):
    seen = {}
    for i,num in enumerate(nums_array):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


nums = [1,2,5,69,4,70,79,1]
result = two_sum(nums,71)
# two_sum(nums,3)
print(f"the result is {result}")

