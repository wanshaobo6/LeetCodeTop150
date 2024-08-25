# 148. 排序链表
# 中等
#
# 相关标签
# 相关企业
# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
#
#
#
# 示例 1：
#
#
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
# 示例 2：
#
#
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
# 示例 3：
#
# 输入：head = []
# 输出：[]
#
#
# 提示：
#
# 链表中节点的数目在范围 [0, 5 * 10^4] 内
# -10^5 <= Node.val <= 10^5
#
#
# 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？


from typing import Optional
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current = self
        res = ""
        while current:
            res += str(current.val)
            if current.next:
                res += '->'
            current = current.next
        return res
class Solution:
    # def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None
    #     split_nodes = []
    #     while head is not None:
    #         split_nodes.append(head)
    #         tmp = head
    #         head = head.next
    #         tmp.next = None
    #     return self.divide_conquer(split_nodes, 0, len(split_nodes)-1)
    #
    # def divide_conquer(self, split_nodes: List[ListNode], left: int, right: int) -> Optional[ListNode]:
    #     if left == right:
    #         return split_nodes[left]
    #     mid = (left + right) >> 1
    #     left_sorted_list = self.divide_conquer(split_nodes, left, mid)
    #     right_sorted_list = self.divide_conquer(split_nodes, mid + 1, right)
    #     return self.mergeTwoLists(left_sorted_list, right_sorted_list)
    #
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     if list1 is None and list2 is None:
    #         return None
    #     head1 = list1
    #     head2 = list2
    #     pilot = ListNode()
    #     pilot_head = pilot
    #     while head1 is not None and head2 is not None:
    #         if head1.val <= head2.val:
    #             pilot_head.next = head1
    #             head1 = head1.next
    #         else:
    #             pilot_head.next = head2
    #             head2 = head2.next
    #         pilot_head = pilot_head.next
    #
    #     if head1 is not None:
    #         pilot_head.next = head1
    #     if head2 is not None:
    #         pilot_head.next = head2
    #
    #     return pilot.next

    #Method2 快慢指针切割链表中点
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # cut the LinkedList at the mid index
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # save and cut.
        mid, slow.next = slow.next, None
        # recursive for cutting.
        left, right = self.sortList(head), self.sortList(mid)
        # merge `left` and `right` linked list and return it.
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next

if __name__ == '__main__':
    list_1 = ListNode(val=10, next=ListNode(val=2, next=ListNode(val=1, next=ListNode(val=6, next=ListNode(val=8, next=None)))))
    solution = Solution()
    result = solution.sortList(list_1)
    print(result)
