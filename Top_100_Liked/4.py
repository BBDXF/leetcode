"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        arr1 = nums1
        arr1.extend(nums2)
        arr1.sort(reverse=False)
        sz = len(arr1)
        sz_half = int(sz / 2)
        if sz % 2 == 0:
            return (arr1[sz_half - 1] + arr1[sz_half]) / 2
        return arr1[sz_half]


s = Solution()
print(s.findMedianSortedArrays([1], [3, 4, 5, 6]))

"""
1. 只能想到这一种解法

"""