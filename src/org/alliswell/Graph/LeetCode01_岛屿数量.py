# 200. 岛屿数量
# 中等
# 相关标签
# 相关企业
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
#
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
#
# 此外，你可以假设该网格的四条边均被水包围。
#
#
#
# 示例 1：
#
# 输入：grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
# ]
# 输出：1
# 示例 2：
#
# 输入：grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
# ]
# 输出：3
#
#
# 提示：
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] 的值为 '0' 或 '1'


from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        row_len = len(grid)
        col_len = len(grid[0])
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == '1':
                    self.inject(grid, i, j, '1', '2')
                    result += 1
        return result


    def inject(self, grid: List[List[str]], index_i: int, index_j: int, expect_val: str, inject_val: str):
        row_len = len(grid)
        col_len = len(grid[0])
        if index_i < 0 or index_i >= row_len or index_j < 0 or index_j >= col_len:
            return
        elif grid[index_i][index_j] != expect_val:
            return

        grid[index_i][index_j] = inject_val
        self.inject(grid, index_i-1, index_j, expect_val, inject_val)
        self.inject(grid, index_i+1, index_j, expect_val, inject_val)
        self.inject(grid, index_i, index_j-1, expect_val, inject_val)
        self.inject(grid, index_i, index_j+1, expect_val, inject_val)

if __name__ == '__main__':
    solution = Solution()
    # grid = [
    #     ["1","1","1","1","0"],
    #     ["1","1","0","1","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","0","0","0"]
    # ]
    #
    # grid = [
    #     ["1","1","0","0","0"],
    #     ["1","1","0","0","0"],
    #     ["0","0","1","0","0"],
    #     ["0","0","0","1","1"]
    # ]

    grid =[["1","0","1","1","0","1","1"]]
    # solution.inject(grid, 0, 0, '1', '2')
    print(solution.numIslands(grid))