# Kadane's Algorithm



def maxSub(nums):
    # Initializing the current and max subarrays
    curr = max_sub = nums[0]
    for num in nums[1:]:
        curr = max(num, curr + num)
        max_sub = max(max_sub, curr)
    return max_sub

nums = [-2,1,-3,4,-1,2,1,-5,4]

print(maxSub(nums))