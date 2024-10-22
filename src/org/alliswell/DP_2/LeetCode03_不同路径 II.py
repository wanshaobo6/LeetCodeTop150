# 63. 不同路径 II
# 中等
#
# 相关标签
# 相关企业
#
# 提示
# 给定一个 m x n 的整数数组 grid。一个机器人初始位于 左上角（即 grid[0][0]）。机器人尝试移动到 右下角（即 grid[m - 1][n - 1]）。机器人每次只能向下或者向右移动一步。
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。机器人的移动路径中不能包含 任何 有障碍物的方格。
#
# 返回机器人能够到达右下角的不同路径数量。
#
# 测试用例保证答案小于等于 2 * 109。
#
#
#
# 示例 1：
#
#
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 示例 2：
#
#
# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1
#
#
# 提示：
#
# m == obstacleGrid.length
# n == obstacleGrid[i].length
# 1 <= m, n <= 100
# obstacleGrid[i][j] 为 0 或 1
# 面试中遇到过这道题?
# 1/5
# 是
# 否
# 通过次数
# 541.6K
# 提交次数
# 1.3M
# 通过率
# 41.7%

from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp_arr = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp_arr[i][j] = 1
                elif obstacleGrid[i][j] == 1:
                    continue
                else:
                    left, top = 0, 0
                    if i-1 >= 0 and obstacleGrid[i-1][j] != 1:
                        top = dp_arr[i-1][j]
                    if j-1 >= 0 and obstacleGrid[i][j-1] != 1:
                        left = dp_arr[i][j-1]
                    dp_arr[i][j] = left + top
        return dp_arr[m-1][n-1]

if __name__ == '__main__':
    solution = Solution()
    # print(solution.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    # print(solution.uniquePathsWithObstacles([[0,1],[0,0]]))
    print(solution.uniquePathsWithObstacles([[0,0]]))