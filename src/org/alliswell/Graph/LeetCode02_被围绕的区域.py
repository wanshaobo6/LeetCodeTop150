# 130. 被围绕的区域
# 中等
#
# 相关标签
# 相关企业
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' 组成，捕获 所有 被围绕的区域：
#
# 连接：一个单元格与水平或垂直方向上相邻的单元格连接。
# 区域：连接所有 'O' 的单元格来形成一个区域。
# 围绕：如果您可以用 'X' 单元格 连接这个区域，并且区域中没有任何单元格位于 board 边缘，则该区域被 'X' 单元格围绕。
# 通过将输入矩阵 board 中的所有 'O' 替换为 'X' 来 捕获被围绕的区域。
#
#
#
# 示例 1：
#
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
#
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#
# 解释：
#
#
# 在上图中，底部的区域没有被捕获，因为它在 board 的边缘并且不能被围绕。
#
# 示例 2：
#
# 输入：board = [["X"]]
#
# 输出：[["X"]]
#
#
#
# 提示：
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] 为 'X' 或 'O'

from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 将直接或者间接与边界0相连的0置为1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i ==0 or i == len(board)-1 or j == 0 or j == len(board[0])-1:
                    if board[i][j] == "O":
                        self.dfs_mark_1(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "I":
                    board[i][j] = "O"
        print(board)
    def dfs_mark_1(self, board: List[List[str]], i:int, j:int):
        if not (0 <= i < len(board) and 0 <= j < len(board[0])):
            return
        if board[i][j] != "O":
            return
        board[i][j] = "I"
        self.dfs_mark_1(board, i-1, j)
        self.dfs_mark_1(board, i+1, j)
        self.dfs_mark_1(board, i, j-1)
        self.dfs_mark_1(board, i, j+1)

if __name__ == '__main__':
    solution = Solution()
    print(solution.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))