# 199. 二叉树的右视图
# 中等
#
# 相关标签
# 相关企业
# 给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
#
#
#
# 示例 1:
#
#
#
# 输入: [1,2,3,null,5,null,4]
# 输出: [1,3,4]
# 示例 2:
#
# 输入: [1,null,3]
# 输出: [1,3]
# 示例 3:
#
# 输入: []
# 输出: []
#
#
# 提示:
#
# 二叉树的节点个数的范围是 [0,100]
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List
from typing import Optional

import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        queue = collections.deque()
        queue.append(root)

        while len(queue) != 0:
            lay_size = len(queue)
            result.append(queue[lay_size-1].val)
            for _ in range(lay_size):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return result


if __name__ == '__main__':
    solution = Solution()
    lt = TreeNode(val= 1, left= TreeNode(val= 2, left= TreeNode(val= 4)), right=TreeNode(val=3))
    print(solution.rightSideView(lt))
