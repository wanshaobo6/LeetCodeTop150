# 2. 两数相加
# 中等
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#
#
# 示例 1：
#
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
# 示例 2：
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
# 示例 3：
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
#
# 提示：
#
# 每个链表中的节点数在范围 [1, 100] 内
# 0 <= Node.val <= 9
# 题目数据保证列表表示的数字不含前导零

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l2 if l1 is None else l1

        res = ListNode(val=None)

        h1, h2, h3 = l1, l2, res
        add_flag = 0
        while h1 and h2:
            val_total = h1.val + h2.val + add_flag
            h3.next = ListNode(val=val_total%10)
            add_flag = val_total // 10
            h1 = h1.next
            h2 = h2.next
            h3 = h3.next
        while h1:
            val_total = h1.val + add_flag
            h3.next = ListNode(val=val_total%10)
            add_flag = val_total // 10
            h1 = h1.next
            h3 = h3.next
        while h2:
            val_total = h2.val + add_flag
            h3.next = ListNode(val=val_total%10)
            add_flag = val_total // 10
            h2 = h2.next
            h3 = h3.next
        if add_flag == 1:
            h3.next = ListNode(val=1)
        return res.next

if __name__ == '__main__':
    list_1 = ListNode(val=5, next=ListNode(val=2, next=ListNode(val=1, next=ListNode(val=6, next=ListNode(val=8, next=None)))))
    list_2 = ListNode(val=5, next=ListNode(val=2, next=ListNode(val=1, next=ListNode(val=6, next=ListNode(val=8, next=None)))))
    solution = Solution()
    result = solution.addTwoNumbers(list_1, list_2)
    print(result)
