# 101. 对称二叉树
# 简单
# 相关标签
# 相关企业
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 示例 2：
#
#
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#
#
# 提示：
#
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isSymmetricCore(root.left, root.right)

    def isSymmetricCore(self, l_tree: Optional[TreeNode], r_tree: Optional[TreeNode]) -> bool:
        if l_tree is None and r_tree is None:
            return True
        elif l_tree is None or r_tree is None:
            return False
        elif l_tree.val != r_tree.val:
            return False
        return self.isSymmetricCore(l_tree.left, r_tree.right) and self.isSymmetricCore(l_tree.right, r_tree.left)

if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode(val= 1, left= TreeNode(val= 2, left= TreeNode(val= 1), right=TreeNode(val=3)), right=TreeNode(val=2, left= TreeNode(val= 3), right=TreeNode(val=1, right=TreeNode(val=1))))
    print(solution.isSymmetric(tree))