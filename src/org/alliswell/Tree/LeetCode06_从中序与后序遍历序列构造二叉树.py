# 106. 从中序与后序遍历序列构造二叉树
# 中等
#
# 相关标签
# 相关企业
# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
#
#
#
# 示例 1:
#
#
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
# 示例 2:
#
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
#
#
# 提示:
#
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder 和 postorder 都由 不同 的值组成
# postorder 中每一个值都在 inorder 中
# inorder 保证是树的中序遍历
# postorder 保证是树的后序遍历


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List
from typing import Optional
class Solution:
    postorder_idx = 0
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.postorder_idx = len(postorder) - 1
        return self.buildTreeCore(inorder, postorder)


    def buildTreeCore(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if self.postorder_idx < 0:
            return None
        val=postorder[self.postorder_idx]
        split_idx = inorder.index(val)
        assert split_idx != -1
        node = TreeNode(val=val)
        if split_idx < len(inorder) - 1:
            self.postorder_idx -= 1
            node.right = self.buildTreeCore(inorder[split_idx+1:], postorder)
        if split_idx > 0:
            self.postorder_idx -= 1
            node.left = self.buildTreeCore(inorder[0:split_idx], postorder)
        return node

if __name__ == '__main__':
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    solution = Solution()
    result = solution.buildTree(inorder, postorder)
    print(result)