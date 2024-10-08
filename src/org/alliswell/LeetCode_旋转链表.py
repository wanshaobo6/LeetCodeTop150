# 61. 旋转链表
# 中等
# 相关标签
# 相关企业
# 给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[4,5,1,2,3]
# 示例 2：
#
#
# 输入：head = [0,1,2], k = 4
# 输出：[2,0,1]
#
#
# 提示：
#
# 链表中节点的数目在范围 [0, 500] 内
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9

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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        tmp = head
        # 将链表连成环
        len = 0
        while tmp:
            len += 1
            if not tmp.next:
                tmp.next = head
                break
            tmp = tmp.next
        jump_step = (len - 1) - (k % len)
        tmp = head
        for i in range(jump_step):
            tmp = tmp.next
        new_head = tmp.next
        tmp.next = None
        return new_head

if __name__ == '__main__':
    head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))
    solution = Solution()
    # res = solution.rotateRight(head,1)
    # res = solution.rotateRight(head,2)
    # res = solution.rotateRight(head,3)
    # res = solution.rotateRight(head,4)
    # res = solution.rotateRight(head,5)
    res = solution.rotateRight(head,6)
    print(res)