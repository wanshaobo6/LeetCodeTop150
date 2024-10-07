# 92. 反转链表 II
# 中等
#
# 相关标签
# 相关企业
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
# 示例 2：
#
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#
#
# 提示：
#
# 链表中节点数目为 n
# 1 <= n <= 500
# -500 <= Node.val <= 500
# 1 <= left <= right <= n
#
#
# 进阶： 你可以使用一趟扫描完成反转吗？


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pilot = ListNode(val=-1, next=None)
        tmp = pilot
        stack = []
        cur = 1
        while head:
            if left <= cur <= right:
                stack.append(head)
            else:
                tmp.next = head
                tmp = tmp.next
            head = head.next
            cur += 1
            if cur == right + 1:
                while stack:
                    ele = stack.pop()
                    tmp.next = ele
                    tmp = tmp.next
                    tmp.next = None
        return pilot.next


if __name__ == '__main__':
    # head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))
    # solution = Solution()
    # print(solution.reverseBetween(head, 2, 4))
    head = ListNode(val=3, next=ListNode(val=5))
    solution = Solution()
    print(solution.reverseBetween(head, 1, 2))