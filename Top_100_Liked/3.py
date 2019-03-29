"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        for (i, v) in enumerate(s):
            d = []
            for j in range(i, len(s)):
                if s[j] in d:
                    l = j - i
                    # print(i, j, l, d)
                    if l > maxlen:
                        maxlen = l
                    d = []
                    break
                else:
                    d.append(s[j])
            if len(d) > 0:
                l = len(d)
                if l > maxlen:
                    maxlen = l
                # print("last", d, l, maxlen)
        return maxlen


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))

"""
1. 使用双循环遍历，在for结束时处理一下最后一个字段问题
2. 使用find/index一类辅助第二个for循环
"""