# 86. 分隔链表
# 中等
#
# 相关标签
# 相关企业
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
# 你应当 保留 两个分区中每个节点的初始相对位置。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
# 示例 2：
#
# 输入：head = [2,1], x = 2
# 输出：[1,2]
#
#
# 提示：
#
# 链表中节点的数目在范围 [0, 200] 内
# -100 <= Node.val <= 100
# -200 <= x <= 200


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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        pilot = ListNode(val=1, next=head)
        slow_node, fast_node= pilot, pilot
        while fast_node and fast_node.next:
            val = fast_node.next.val
            if val < x:
                if slow_node.next == fast_node.next:
                    slow_node = slow_node.next
                    fast_node = fast_node.next
                    continue
                lt_node = fast_node.next
                fast_node.next = lt_node.next
                # 将值比较小的节点放到前面
                lt_node.next = slow_node.next
                slow_node.next = lt_node
                slow_node = slow_node.next
            else:
                fast_node = fast_node.next
        return pilot.next


if __name__ == '__main__':
    head = ListNode(val=1, next=ListNode(val=4, next=ListNode(val=3, next=ListNode(val=0, next=ListNode(val=2, next=ListNode(val=5, next=ListNode(val=2, next=None)))))))
    solution = Solution()
    print(solution.partition(head, 3))