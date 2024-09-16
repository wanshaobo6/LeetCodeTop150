# 105. 从前序与中序遍历序列构造二叉树
# 中等
#
# 相关标签
# 相关企业
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
#
#
#
# 示例 1:
#
#
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
# 示例 2:
#
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
#
#
# 提示:
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder 和 inorder 均 无重复 元素
# inorder 均出现在 preorder
# preorder 保证 为二叉树的前序遍历序列
# inorder 保证 为二叉树的中序遍历序列

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    preorder_idx = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if self.preorder_idx >= len(preorder):
            return None
        val=preorder[self.preorder_idx]
        split_idx = inorder.index(val)
        assert split_idx != -1
        node = TreeNode(val=val)
        if split_idx > 0:
            self.preorder_idx += 1
            node.left = self.buildTree(preorder, inorder[0:split_idx])
        if split_idx < len(inorder) - 1:
            self.preorder_idx += 1
            node.right = self.buildTree(preorder, inorder[split_idx+1:])
        return node


if __name__ == '__main__':
    # preorder = [3,9,20,15,7]
    # inorder = [9,3,15,20,7]
    preorder = [3,1,2,4]
    inorder = [1,2,3,4]
    solution = Solution()
    res = solution.buildTree(preorder, inorder)
    print(solution.buildTree(preorder, inorder))