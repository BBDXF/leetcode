"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        cur = self
        rets = ""
        while cur.next is not None:
            rets += "%s ->" % (cur.val,)
            cur = cur.next
        rets += "%s" % (cur.val,)
        return rets


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        retNode = None
        curAdd = 0
        curl1 = l1
        curl2 = l2
        while True:
            curv = (curl1.val + curl2.val + curAdd) % 10
            curAdd = int((curl1.val + curl2.val + curAdd) / 10)

            if retNode is None:
                curNode = ListNode(curv)
                retNode = curNode
            else:
                curNode.next = ListNode(curv)
                curNode = curNode.next

            curl1 = curl1.next
            curl2 = curl2.next
            if curl1 is None and curl2 is None and curAdd == 0:
                break
            if curl1 is None:
                curl1 = ListNode(0)
            if curl2 is None:
                curl2 = ListNode(0)
        return retNode


l1 = ListNode(1)
# l1.next = ListNode(4)
# l1.next.next = ListNode(3)

l2 = ListNode(9)
l2.next = ListNode(9)
# l2.next.next = ListNode(4)

s = Solution()
print(s.addTwoNumbers(l1, l2))

"""
1. 普通循环
"""
