# 637. 二叉树的层平均值
# 简单
#
# 相关标签
# 相关企业
# 给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10-5 以内的答案可以被接受。
#
#
#
# 示例 1：
#
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[3.00000,14.50000,11.00000]
# 解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
# 因此返回 [3, 14.5, 11] 。
# 示例 2:
#
#
#
# 输入：root = [3,9,20,15,7]
# 输出：[3.00000,14.50000,11.00000]
#
#
# 提示：
#
# 树中节点数量在 [1, 104] 范围内
# -231 <= Node.val <= 231 - 1


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from typing import List

import queue
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []
        root.layer = 1

        result = []
        pre_layer = 1
        sum = 0
        cnt = 0
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            item = q.get()
            cur_layer = item.layer
            if item.left is not None:
                item.left.layer = cur_layer + 1
                q.put(item.left)
            if item.right is not None:
                item.right.layer = cur_layer + 1
                q.put(item.right)

            if pre_layer == cur_layer:
                sum += item.val
                cnt += 1
            else:
                result.append(sum / cnt)
                sum = item.val
                cnt = 1
                pre_layer = cur_layer
        result.append(sum / cnt)
        return result

if __name__ == '__main__':
    tree = TreeNode(val= 1, left= TreeNode(val= 2, left= TreeNode(val= 1), right=TreeNode(val=3)), right=TreeNode(val=7, left= TreeNode(val= 6), right=TreeNode(val=9)))
    solution = Solution()
    root_tree = solution.averageOfLevels(tree)
    print(root_tree)
