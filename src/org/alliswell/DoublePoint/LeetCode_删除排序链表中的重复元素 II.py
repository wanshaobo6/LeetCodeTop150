# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
# 示例 2：
#
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#
#
# 提示：
#
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列



#解题思想 初始idx=0  当list[idx]=list[idx+1]代表list[idx]要保留  否者的话找到下一个不重复的点 并且这段遍历经过的点都要删除 依此类推

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        pilot = ListNode(val=None, next= head)
        p1 = pilot
        p2 = head

        while p2 is not None and p2.next is not None:
            if p2.val != p2.next.val:
                p1 = p2
                p2 = p2.next
                continue
            else:
                while p2.next is not None and p2.val == p2.next.val:
                    p2 = p2.next
                p1.next = p2.next
                p2 = p2.next
        return pilot.next

if __name__ == '__main__':
    head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=4, next=ListNode(val=5, next=None)))))))
    solution = Solution()
    print(solution.deleteDuplicates(head))