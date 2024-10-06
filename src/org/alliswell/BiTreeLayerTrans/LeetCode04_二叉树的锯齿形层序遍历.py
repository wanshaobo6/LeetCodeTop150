# 103. 二叉树的锯齿形层序遍历
# 中等
#
# 相关标签
# 相关企业
# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
# 示例 2：
#
# 输入：root = [1]
# 输出：[[1]]
# 示例 3：
#
# 输入：root = []
# 输出：[]
#
#
# 提示：
#
# 树中节点数目在范围 [0, 2000] 内
# -100 <= Node.val <= 100

from typing import Optional
from typing import List
# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        results = []
        stack_1 = [root]
        stack_2 = []
        while len(stack_1) != 0 or len(stack_2) != 0:
            # 正向
            result = []
            while len(stack_1) != 0:
                ele = stack_1.pop()
                result.append(ele.val)
                if ele.left:
                    stack_2.append(ele.left)
                if ele.right:
                    stack_2.append(ele.right)
            if len(result) > 0:
                results.append(result)
            # 反向
            result = []
            while len(stack_2) != 0:
                ele = stack_2.pop()
                result.append(ele.val)
                if ele.right:
                    stack_1.append(ele.right)
                if ele.left:
                    stack_1.append(ele.left)
            if len(result) > 0:
                results.append(result)
        return results

if __name__ == '__main__':
    head = TreeNode(val=3, left= TreeNode(val=9), right= TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=9)))
    solution = Solution()
    print(solution.zigzagLevelOrder(head))