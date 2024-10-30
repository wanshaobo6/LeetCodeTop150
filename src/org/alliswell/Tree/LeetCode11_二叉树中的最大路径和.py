# 二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
#
# 路径和 是路径中各节点值的总和。
#
# 给你一个二叉树的根节点 root ，返回其 最大路径和 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3]
# 输出：6
# 解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
# 示例 2：
#
#
# 输入：root = [-10,9,20,null,null,15,7]
# 输出：42
# 解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
#
#
# 提示：
#
# 树中节点数目范围是 [1, 3 * 104]
# -1000 <= Node.val <= 1000
import sys


# Definition for a binary tree node.
# 后根遍历遍历二叉树。 遍历到根结点时判断以当前节点连接左右分支是否能达到最大值。 判断完成后将自己归为左分支的一个节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    result = -sys.maxsize
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.transTree(root)
        return self.result

    def transTree(self, cur_node: Optional[TreeNode]):
        if not cur_node:
            return None
        self.transTree(cur_node.left)
        self.transTree(cur_node.right)
        h_v, v_v = cur_node.val, cur_node.val
        if cur_node.left and cur_node.left.val > 0 and cur_node.right and cur_node.right.val > 0:
            h_v += cur_node.left.val + cur_node.right.val
            v_v += max(cur_node.left.val,  cur_node.right.val)
        elif cur_node.left and cur_node.left.val > 0:
            h_v += cur_node.left.val
            v_v = h_v
        elif cur_node.right and cur_node.right.val > 0:
            h_v += cur_node.right.val
            v_v = h_v
        if h_v > self.result:
            self.result = h_v
        cur_node.val = v_v
        return cur_node

if __name__ == '__main__':
    root = TreeNode(val=-10, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
    solution = Solution()
    print(solution.maxPathSum(root))