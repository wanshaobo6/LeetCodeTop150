# 98. 验证二叉搜索树
# 中等
#
# 相关标签
# 相关企业
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
# 有效 二叉搜索树定义如下：
#
# 节点的左
# 子树
# 只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
#
#
# 示例 1：
#
#
# 输入：root = [2,1,3]
# 输出：true
# 示例 2：
#
#
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#
#
# 提示：
#
# 树中节点数目范围在[1, 104] 内
# -2^31 <= Node.val <= 2^31 - 1

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        bst_iterator = BSTIterator(root)
        pre = None
        while bst_iterator.hasNext():
            val = bst_iterator.next()
            if pre is not None and pre >= val:
                return False
            pre = val
        return True

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.node_stack = []
        while root:
            self.node_stack.append(root)
            root = root.left

    def next(self) -> int:
        if not self.hasNext():
            return -1
        node = self.node_stack.pop()
        tmp_node = node.right
        if tmp_node:
            self.node_stack.append(tmp_node)
            while tmp_node.left:
                self.node_stack.append(tmp_node.left)
                tmp_node = tmp_node.left
        return node.val

    def hasNext(self) -> bool:
        return len(self.node_stack) != 0


if __name__ == '__main__':
    # tree = TreeNode(val=7, left=TreeNode(val=3), right=TreeNode(val=15, left=TreeNode(val=9), right=TreeNode(val=20)))
    tree = TreeNode(val=0, left=None, right=TreeNode(val=-1))
    solution = Solution()
    print(solution.isValidBST(tree))