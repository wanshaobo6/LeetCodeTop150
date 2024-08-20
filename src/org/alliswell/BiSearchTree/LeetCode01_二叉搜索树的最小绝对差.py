# 530. 二叉搜索树的最小绝对差
# 简单
#
# 相关标签
# 相关企业
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
#
# 差值是一个正数，其数值等于两值之差的绝对值。
#
#
#
# 示例 1：
#
#
# 输入：root = [4,2,6,1,3]
# 输出：1
# 示例 2：
#
#
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#
#
# 提示：
#
# 树中节点的数目范围是 [2, 104]
# 0 <= Node.val <= 105
import sys
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    min_diff = sys.maxsize
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.getMinimumDifference_core(root, None)
        return self.min_diff

    def getMinimumDifference_core(self, root: Optional[TreeNode], pre_max: Optional[int]) -> Optional[int]:
        if root is None:
            return None
        left_max = self.getMinimumDifference_core(root.left, pre_max) or pre_max
        if left_max is not None and root.val - left_max < self.min_diff:
            self.min_diff = root.val - left_max
        right_max = self.getMinimumDifference_core(root.right, root.val)
        if right_max is not None:
            return right_max
        return root.val

if __name__ == '__main__':
    # tree = TreeNode(val= 4, left= TreeNode(val= 2, left= TreeNode(val= -10), right= TreeNode(val=3)), right=TreeNode(val=6))
    tree = TreeNode(val= 1, left= None, right=TreeNode(val=2))
    solution = Solution()
    print(solution.getMinimumDifference(tree))
