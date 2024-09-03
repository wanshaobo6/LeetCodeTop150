# 236. 二叉树的最近公共祖先
# 中等
# 相关标签
# 相关企业
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
#
#
# 示例 1：
#
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
# 示例 2：
#
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
# 示例 3：
#
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
#
#
# 提示：
#
# 树中节点数目在范围 [2, 105] 内。
# -10^9 <= Node.val <= 10^9
# 所有 Node.val 互不相同 。
# p != q
# p 和 q 均存在于给定的二叉树中。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int, left: 'TreeNode', right: 'TreeNode'):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.result = None
        self.findCommonAncestor(root, p, q)
        return self.result

    def findCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> int:
        if not root:
            return 0
        find_cnt = self.findCommonAncestor(root.left, p, q)+ self.findCommonAncestor(root.right, p, q)
        if root.val == p.val or root.val == q.val:
            find_cnt += 1
        if find_cnt == 2 and self.result is None:
            self.result = root
        return find_cnt

if __name__ == '__main__':
    solution = Solution()
    # tree = TreeNode(val= 1, left= TreeNode(val= 2, left= TreeNode(val= 1), right=TreeNode(val=3)), right=TreeNode(val=7, left= TreeNode(val= 6), right=TreeNode(val=9)))
    print(solution.lowestCommonAncestor(None, None, None))
