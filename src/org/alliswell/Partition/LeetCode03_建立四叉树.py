# 427. 建立四叉树
# 中等
#
# 相关标签
# 相关企业
# 给你一个 n * n 矩阵 grid ，矩阵由若干 0 和 1 组成。请你用四叉树表示该矩阵 grid 。
#
# 你需要返回能表示矩阵 grid 的 四叉树 的根结点。
#
# 四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：
#
# val：储存叶子结点所代表的区域的值。1 对应 True，0 对应 False。注意，当 isLeaf 为 False 时，你可以把 True 或者 False 赋值给节点，两种值都会被判题机制 接受 。
# isLeaf: 当这个节点是一个叶子结点时为 True，如果它有 4 个子节点则为 False 。
# class Node {
# public boolean val;
# public boolean isLeaf;
# public Node topLeft;
# public Node topRight;
# public Node bottomLeft;
# public Node bottomRight;
# }
# 我们可以按以下步骤为二维区域构建四叉树：
#
# 如果当前网格的值相同（即，全为 0 或者全为 1），将 isLeaf 设为 True ，将 val 设为网格相应的值，并将四个子节点都设为 Null 然后停止。
# 如果当前网格的值不同，将 isLeaf 设为 False， 将 val 设为任意值，然后如下图所示，将当前网格划分为四个子网格。
# 使用适当的子网格递归每个子节点。
#
#
# 如果你想了解更多关于四叉树的内容，可以参考 wiki 。
#
# 四叉树格式：
#
# 你不需要阅读本节来解决这个问题。只有当你想了解输出格式时才会这样做。输出为使用层序遍历后四叉树的序列化形式，其中 null 表示路径终止符，其下面不存在节点。
#
# 它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 [isLeaf, val] 。
#
# 如果 isLeaf 或者 val 的值为 True ，则表示它在列表 [isLeaf, val] 中的值为 1 ；如果 isLeaf 或者 val 的值为 False ，则表示值为 0 。
#
#
#
# 示例 1：
#
#
#
# 输入：grid = [[0,1],[1,0]]
# 输出：[[0,1],[1,0],[1,1],[1,1],[1,0]]
# 解释：此示例的解释如下：
# 请注意，在下面四叉树的图示中，0 表示 false，1 表示 True 。
#
# 示例 2：
#
#
#
# 输入：grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
# 输出：[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
# 解释：网格中的所有值都不相同。我们将网格划分为四个子网格。
# topLeft，bottomLeft 和 bottomRight 均具有相同的值。
# topRight 具有不同的值，因此我们将其再分为 4 个子网格，这样每个子网格都具有相同的值。
# 解释如下图所示：
#
#
#
# 提示：
#
# n == grid.length == grid[i].length
# n == 2^x 其中 0 <= x <= 6


# Definition for a QuadTree node.

from typing import List
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> Node:
        return self.construct_core(grid, 0, len(grid)-1, 0, len(grid[0])-1)
    def construct_core(self, grid: List[List[int]], x_s: int, x_e: int, y_s: int, y_e:int) -> Node:
        if self.if_submetrix_same(grid, x_s, x_e, y_s, y_e):
            return Node(True if grid[x_s][y_s] == 1 else False, True, None, None, None, None)
        else:
            x_m = (x_s+x_e) >> 1
            y_m = (y_s+y_e) >> 1
            return Node(val = True, isLeaf = False,
                        topLeft = self.construct_core(grid, x_s, x_m, y_s, y_m),
                        topRight = self.construct_core(grid, x_s, x_m, y_m+1, y_e),
                        bottomLeft = self.construct_core(grid, x_m+1, x_e, y_s, y_m),
                        bottomRight = self.construct_core(grid, x_m+1, x_e, y_m+1, y_e))

    def if_submetrix_same(self, grid: List[List[int]], x_s: int, x_e: int, y_s: int, y_e:int) -> bool:
        if x_s == x_e and y_s == y_e:
            return True
        expect_val = grid[x_s][y_s]
        for i in range(x_s, x_e + 1):
            for j in range(y_s, y_e + 1):
                if grid[i][j] != expect_val:
                    return False
        return True


if __name__ == '__main__':
    grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    # grid = [[0,1],[1,0]]
    solution = Solution()
    result = solution.construct(grid)
    print(result)

