# 21. 合并两个有序链表
# 简单
#
# 相关标签
# 相关企业
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#
#
# 示例 1：
#
#
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 示例 2：
#
# 输入：l1 = [], l2 = []
# 输出：[]
# 示例 3：
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#
#
# 提示：
#
# 两个链表的节点数目范围是 [0, 50]
# -100 <= Node.val <= 100
# l1 和 l2 均按 非递减顺序 排列

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        head1 = list1
        head2 = list2
        pilot = ListNode()
        pilot_head = pilot
        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                pilot_head.next = head1
                head1 = head1.next
            else:
                pilot_head.next = head2
                head2 = head2.next
            pilot_head = pilot_head.next

        if head1 is not None:
            pilot_head.next = head1
        if head2 is not None:
            pilot_head.next = head2

        return pilot.next

if __name__ == '__main__':
    node1 = ListNode(val=1, next=ListNode(val=2 , next=ListNode(val=4 )))
    node2 = ListNode(val=1, next=ListNode(val=3 , next=ListNode(val=4 )))
    solution = Solution()
    result = solution.mergeTwoLists(node1, node2)
    print(result)