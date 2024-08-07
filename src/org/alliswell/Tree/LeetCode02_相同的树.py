# 100. 相同的树
# 简单
#
# 相关标签
# 相关企业
# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
#
#
# 示例 1：
#
#
# 输入：p = [1,2,3], q = [1,2,3]
# 输出：true
# 示例 2：
#
#
# 输入：p = [1,2], q = [1,null,2]
# 输出：false
# 示例 3：
#
#
# 输入：p = [1,2,1], q = [1,1,2]
# 输出：false
#
#
# 提示：
#
# 两棵树上的节点数目都在范围 [0, 100] 内
# -10^4 <= Node.val <= 10^4


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    lt = TreeNode(val= 1, left= TreeNode(val= 2), right=TreeNode(val=3))
    lt = TreeNode(val= 1, left= TreeNode(val= 2), right=TreeNode(val=3))
    rt = TreeNode(val= 1, left= TreeNode(val= 2), right=TreeNode(val=3))
    solution = Solution()
    print(solution.isSameTree(lt, rt))