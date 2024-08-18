# 230. 二叉搜索树中第 K 小的元素
# 中等
#
# 相关标签
# 相关企业
#
# 提示
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 小的元素（从 1 开始计数）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
# 示例 2：
#
#
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3



# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    rank = 0
    result = -1
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0
        self.kthSmallest(root.left, k)
        self.rank += 1
        if self.rank == k:
            self.result = root.val
        self.kthSmallest(root.right, k)
        return self.result

if __name__ == '__main__':
    solution = Solution()
    tree_node = TreeNode(val=3, left=TreeNode(val=1, left=None, right=TreeNode(val=2)), right=TreeNode(val=4))
    print(solution.kthSmallest(tree_node, 2))
