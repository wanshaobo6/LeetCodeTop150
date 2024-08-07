# 104. 二叉树的最大深度
# 简单
#
# 相关标签
# 相关企业
# 给定一个二叉树 root ，返回其最大深度。
#
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
#
#
#
# 示例 1：
#
#
#
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
# 示例 2：
#
# 输入：root = [1,null,2]
# 输出：2
#
#
# 提示：
#
# 树中节点的数量在 [0, 104] 区间内。
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == '__main__':
    lt = TreeNode(val= 1, left= TreeNode(val= 2, left= TreeNode(val= 1), right=TreeNode(val=3)), right=TreeNode(val=7, left= TreeNode(val= 6), right=TreeNode(val=9, right=TreeNode(val=1))))
    solution = Solution()
    print(solution.maxDepth(lt))