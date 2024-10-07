# 138. 随机链表的复制
# 中等
#
# 相关标签
# 相关企业
#
# 提示
# 给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。
#
# 构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。
#
# 例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。
#
# 返回复制链表的头节点。
#
# 用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
#
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 你的代码 只 接受原链表的头节点 head 作为传入参数。
#
#
#
# 示例 1：
#
#
#
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
# 示例 2：
#
#
#
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
# 示例 3：
#
#
#
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
#
#
# 提示：
#
# 0 <= n <= 1000
# -10^4 <= Node.val <= 10^4
# Node.random 为 null 或指向链表中的节点。

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# from typing import Optional
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        random_map = {}
        copy_head = Node(x=0)
        copy_pre_node = copy_head
        origin_node = head
        while origin_node:
            copy_node = Node(x=origin_node.val, random=None, next=None)
            #建立随机映射
            random_map[origin_node] = copy_node
            #复制指针后移
            copy_pre_node.next = copy_node
            copy_pre_node = copy_pre_node.next
            #原始指针后移
            origin_node = origin_node.next

        copy_pre_node = copy_head.next
        origin_node = head
        while copy_pre_node and origin_node:
            if origin_node.random:
                copy_pre_node.random = random_map[origin_node.random]
            origin_node = origin_node.next
            copy_pre_node = copy_pre_node.next
        return copy_head.next


if __name__ == '__main__':
    node2 = Node(x=2, random=None, next=None)
    node2.random = node2
    head1 = Node(x=1, random=node2, next=node2)
    solution = Solution()
    print(solution.copyRandomList(head1))