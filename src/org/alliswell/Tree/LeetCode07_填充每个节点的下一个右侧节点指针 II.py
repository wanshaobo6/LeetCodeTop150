# 117. 填充每个节点的下一个右侧节点指针 II
# 中等
#
# 相关标签
# 相关企业
# 给定一个二叉树：
#
# struct Node {
#     int val;
# Node *left;
# Node *right;
# Node *next;
# }
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。
#
# 初始状态下，所有 next 指针都被设置为 NULL 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,4,5,null,7]
# 输出：[1,#,2,3,#,4,5,7,#]
#       解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。
# 示例 2：
#
# 输入：root = []
# 输出：[]
#
#
# 提示：
#
# 树中的节点数在范围 [0, 6000] 内
#                              -100 <= Node.val <= 100
# 进阶：
#
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序的隐式栈空间不计入额外空间复杂度。


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = []
        queue.append(root)

        while len(queue) != 0:
            lay_len = len(queue)
            pre_node = None
            for i in range(lay_len):
                node = queue[0]
                queue = queue[1:]
                if pre_node:
                    pre_node.next = node
                    pre_node = pre_node.next
                else:
                    pre_node = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

if __name__ == '__main__':
    root = Node(val=1, left=Node(val=2, left=Node(val=4), right=Node(val=5)), right = Node(val=3, right=Node(val=7)))
    solution = Solution()
    result = solution.connect(root)
    print(result)