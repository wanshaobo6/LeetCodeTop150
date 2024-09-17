# 114. 二叉树展开为链表
# 中等
#
# 相关标签
# 相关企业
#
# 提示
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
#
# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。
#
#
# 示例 1：
#
#
# 输入：root = [1,2,5,3,4,null,6]
# 输出：[1,null,2,null,3,null,4,null,5,null,6]
# 示例 2：
#
# 输入：root = []
# 输出：[]
# 示例 3：
#
# 输入：root = [0]
# 输出：[0]
#
#
# 提示：
#
# 树中结点数在范围 [0, 2000] 内
# -100 <= Node.val <= 100


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    #Mirrors算法
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return root
        node = root
        while node.left is not None or node.right is not None:
            tmp = node.left
            if tmp is None:
                node = node.right
                continue
            while tmp.right is not None:
                tmp = tmp.right
            tmp.right = node.right
            node.right = node.left
            node.left = None
            node = node.right
        return root

    # def flatten(self, root: Optional[TreeNode]) -> None:
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #     return self.flatten_core(root)
    #
    # def flatten_core(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if root is None:
    #         return None
    #     tmp_node = root
    #     right = self.flatten_core(tmp_node.right)
    #     tmp_node.right = self.flatten_core(tmp_node.left)
    #     tmp_node.left = None
    #     while tmp_node.right is not None:
    #         tmp_node = tmp_node.right
    #     tmp_node.right = right
    #     return root

if __name__ == '__main__':
    tree = TreeNode(val= 1, left= TreeNode(val= 2, left= TreeNode(val= 1), right=TreeNode(val=3)), right=TreeNode(val=7, left= TreeNode(val= 6), right=TreeNode(val=9)))
    solution = Solution()
    root_tree = solution.flatten(tree)
    print(root_tree)
