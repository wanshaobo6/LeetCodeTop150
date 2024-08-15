# 完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,4,5,6]
# 输出：6
# 示例 2：
#
# 输入：root = []
# 输出：0
# 示例 3：
#
# 输入：root = [1]
# 输出：1
#
#
# 提示：
#
# 树中节点的数目范围是[0, 5 * 104]
# 0 <= Node.val <= 5 * 104
# 题目数据保证输入的树是 完全二叉树
#
#
# 进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    # def countNodes(self, root: Optional[TreeNode]) -> int:
    #     if root is None:
    #         return 0
    #     return self.countNodes(root.left) + self.countNodes(root.right) + 1

    #本质就是二分查找： 比较左右两颗子树的高度： 1.如果当前节点左右子树高度相等：当前节点的左子树就是一颗满二叉树，可以直接计算左子树节点个树为：2的左子树高度次方。
    # 总的节点个树，则只需再加上右子树的节点树。把右子节点树继续递归求解。 2.如果当前节点左右子树高度不相等：则左子树可能不是满二叉树，且右子树是满二叉树，
    # 则利用右子树高度就可以求出右子树节点个树。此时只需继续递归求解左子树，就可以得到总节点树。
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_level = self.countLevel(root.left)
        right_level = self.countLevel(root.right)
        if left_level == right_level:
            return self.countNodes(root.right) + (1 << left_level)
        else:
            return self.countNodes(root.left) + (1 << right_level)

    def countLevel(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.countLevel(root.left), self.countLevel(root.right) )+ 1


if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode(val= 1, left= TreeNode(val= 2, left= TreeNode(val= 1), right=TreeNode(val=3)), right=TreeNode(val=7, left= TreeNode(val= 6), right=TreeNode(val=9)))
    print(solution.countNodes(tree))
