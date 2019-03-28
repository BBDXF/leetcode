"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
输入: [2,2,1]
输出: 1

示例 2:
输入: [4,1,2,1,2]
输出: 4
"""


def singleNumber(nums: list) -> int:
    m = {}
    for v in nums:
        m[v] = m.get(v, 0) + 1
    for k in m.keys():
        if m[k] == 1:
            return k
    return None


assert (singleNumber([2, 2, 1]) == 1)
assert (singleNumber([4, 1, 2, 1, 2]) == 4)

# 这类题没有答案，各种未知错误，暂时停止