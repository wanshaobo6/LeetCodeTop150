#
#
# 代码
#
# 测试用例
#
# 测试结果
# 测试结果
# 226. 翻转二叉树
# 简单
#
# 相关标签
# 相关企业
# 给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [4,2,7,1,3,6,9]
# 输出：[4,7,2,9,6,3,1]
# 示例 2：
#
#
#
# 输入：root = [2,1,3]
# 输出：[2,3,1]
# 示例 3：
#
# 输入：root = []
# 输出：[]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None or (root.left == None and root.right == None):
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

if __name__ == '__main__':
    lt = TreeNode(val= 1, left= TreeNode(val= 2, left= TreeNode(val= 1), right=TreeNode(val=3)), right=TreeNode(val=7, left= TreeNode(val= 6), right=TreeNode(val=9)))
    solution = Solution()
    res = solution.invertTree(lt)
    print(res)