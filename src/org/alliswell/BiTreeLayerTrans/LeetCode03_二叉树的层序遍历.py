# 102. 二叉树的层序遍历
# 中等
#
# 相关标签
# 相关企业
# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
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
# -1000 <= Node.val <= 1000

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
from typing import List
import queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        result = []
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            lay_num = q.qsize()
            lay_list = []
            for i in range(lay_num):
                item = q.get()
                lay_list.append(item.val)
                if item.left is not None:
                    q.put(item.left)
                if item.right is not None:
                    q.put(item.right)
            result.append(lay_list)
        return result

if __name__ == '__main__':
    tree = TreeNode(val= 1, left= TreeNode(val= 2, left= TreeNode(val= 1), right=TreeNode(val=3)), right=TreeNode(val=7, left= TreeNode(val= 6), right=TreeNode(val=9)))
    solution = Solution()
    print(solution.levelOrder(tree))
