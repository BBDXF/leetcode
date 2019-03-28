"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums: list, target: int) -> list:
    for (i, v) in enumerate(nums):
        want = target - v
        if want in nums[i+1:]:
            return [i, nums.index(want, i + 1)]


print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
"""
1. 两个for循环也可以，但是没有这个时间复杂度上好一点
2. 使用map查找 82ms
3. 使用index查找 856ms
"""
