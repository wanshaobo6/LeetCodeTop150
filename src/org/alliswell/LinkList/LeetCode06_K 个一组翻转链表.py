# 25. K 个一组翻转链表
# 困难
#
# 相关标签
# 相关企业
# 给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,4,5], k = 2
# 输出：[2,1,4,3,5]
# 示例 2：
#
#
#
# 输入：head = [1,2,3,4,5], k = 3
# 输出：[3,2,1,4,5]
#
#
# 提示：
# 链表中的节点数目为 n
# 1 <= k <= n <= 5000
# 0 <= Node.val <= 1000
#
#
# 进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？


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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        pilot = ListNode(val=-1, next=None)
        tmp = pilot
        stack = []
        cur = 0
        while True:
            if head and cur < k:
                stack.append(head)
                head = head.next
            else:
                if cur == k:
                    # 栈中元素满k个
                    while stack:
                        ele = stack.pop()
                        tmp.next = ele
                        tmp = tmp.next
                        tmp.next = None
                elif not head:
                    # 如果没有下一次循环
                    while stack:
                        ele = stack[0]
                        stack = stack[1:]
                        tmp.next = ele
                        tmp = tmp.next
                        tmp.next = None
                if not head:
                    break
            cur = (cur + 1) % (k+1)
        return pilot.next

if __name__ == '__main__':
    solution = Solution()
    head = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))
    print(solution.reverseKGroup(head, 1))