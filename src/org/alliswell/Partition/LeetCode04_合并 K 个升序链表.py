# 23. 合并 K 个升序链表
# 困难
#
# 相关标签
# 相关企业
# 给你一个链表数组，每个链表都已经按升序排列。
#
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
# 示例 1：
#
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#     1->4->5,
# 1->3->4,
# 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 示例 2：
#
# 输入：lists = []
# 输出：[]
# 示例 3：
#
# 输入：lists = [[]]
# 输出：[]
#
#
# 提示：
#
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
from typing import List
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        return self.mergeLists_core(lists, 0 ,len(lists)-1)

    def mergeLists_core(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return lists[left]
        mid = (left + right) >> 1
        l_list = self.mergeLists_core(lists, left, mid)
        r_list = self.mergeLists_core(lists, mid+1, right)
        return self.mergeSortedList(l_list, r_list)


    def mergeSortedList(self, lists_1: Optional[ListNode], lists_2: Optional[ListNode]) -> Optional[ListNode]:
        pilot = ListNode()
        tmp_node = pilot
        while lists_1 is not None and lists_2 is not None:
            if lists_1.val <= lists_2.val:
                tmp_node.next = lists_1
                lists_1 = lists_1.next
            else:
                tmp_node.next = lists_2
                lists_2 = lists_2.next
            tmp_node = tmp_node.next

        if lists_1 is not None:
            tmp_node.next = lists_1
        elif lists_2 is not None:
            tmp_node.next = lists_2
        return pilot.next

if __name__ == '__main__':
    list_1 = ListNode(val=0, next=ListNode(val=2, next=ListNode(val=4, next=ListNode(val=6, next=ListNode(val=8, next=None)))))
    list_2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=5, next=ListNode(val=7, next=ListNode(val=9, next=ListNode(val=11, next=None))))))
    list_2 = ListNode(val=-100, next=ListNode(val=100, next=None))
    solution = Solution()
    tmp = solution.mergeKLists([ListNode()])
    print("Hello")
    # print(solution.mergeSortedList(list_1, list_2))
