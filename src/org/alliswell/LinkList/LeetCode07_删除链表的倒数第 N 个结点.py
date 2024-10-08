# 19. 删除链表的倒数第 N 个结点
# 中等
#
# 相关标签
# 相关企业
#
# 提示
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 示例 2：
#
# 输入：head = [1], n = 1
# 输出：[]
# 示例 3：
#
# 输入：head = [1,2], n = 1
# 输出：[1]
#
#
# 提示：
#
# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current = self
        result = str(current.val)
        while current.next is not None:
            current = current.next
            result += "->" + str(current.val)
        return result
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pilot = ListNode(val=None, next=head)
        point_1 = pilot
        point_2 = pilot

        for i in range(n):
            point_2 = point_2.next
        while point_2.next is not None:
            point_1 = point_1.next
            point_2 = point_2.next

        if point_1.next is not None:
            point_1.next = point_1.next.next

        return pilot.next
if __name__ == '__main__':
    solution = Solution()
    head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=4, next=ListNode(val=5, next=None)))))))
    print(solution.removeNthFromEnd(head, 7))
