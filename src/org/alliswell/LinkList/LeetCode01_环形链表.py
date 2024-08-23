# 141. 环形链表
# 简单
# 相关标签
# 相关企业
# 给你一个链表的头节点 head ，判断链表中是否有环。
# 
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
# 
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 示例 2：
# 
# 
# 
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 示例 3：
# 
# 
# 
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
# 
# 
# 提示：
# 
# 链表中节点的数目范围是 [0, 10^4]
# -10^5 <= Node.val <= 10^5
# pos 为 -1 或者链表中的一个 有效索引 。
#

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    # def __init__(self, x):
    #     self.val = x
    #     self.next = None

    def __init__(self, val, next):
        self.val = val
        self.next = next
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        n1 = head
        n2 = head.next
        while n1 is not None and n2 is not None:
            if n1 == n2:
                return True
            n1 = n1.next
            if n2.next is not None:
                n2 = n2.next.next
            else:
                n2 = None
        return False


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(val=1, next=ListNode(val=2 , next=ListNode(val=4 , next=None)))
    head.next.next.next = head
    print(solution.hasCycle(head))