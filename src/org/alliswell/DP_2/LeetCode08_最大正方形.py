# 221. 最大正方形
# 中等
#
# 相关标签
# 相关企业
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# 输出：4
# 示例 2：
#
#
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
# 示例 3：
#
# 输入：matrix = [["0"]]
# 输出：0
#
#
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] 为 '0' 或 '1'
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        def max_square_on_p(matrix: List[List[str]], r: int, c:int, pre_square_len:int) -> int:
            if pre_square_len == 0:
                return 1 if matrix[r][c] == "1" else 0
            cnt = 1
            for i in range(1, 1 + pre_square_len):
                # 判断上面的单元格是否为1  判断左边的单元格是否为1
                top_r, left_c = r - i, c - i
                if top_r < 0 or left_c < 0 or matrix[top_r][c] != "1" or matrix[r][left_c] != "1":
                    return cnt
                cnt += 1
            return cnt

        maximal_square, dp_2 = 0, [0]*c

        for i in range(r):
            for j in range(c-1, -1, -1):
                if i == 0 or j == 0:
                    dp_2[j] = 1 if matrix[i][j] == "1" else 0
                else:
                    if matrix[i][j] == "0":
                        dp_2[j] = 0
                    else:
                        dp_2[j] = max_square_on_p(matrix, i, j, dp_2[j-1])
                maximal_square = max(maximal_square, dp_2[j])
            print(dp_2)
        return maximal_square * maximal_square

if __name__ == '__main__':
    solution = Solution()
    # print(solution.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(solution.maximalSquare([["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]))

[["1","0","1","1","0","1"]
 ["1","1","1","1","1","1"]
 ["0","1","1","0","1","1"]
 ["1","1","1","0","1","0"]
 ["0","1","1","1","1","1"]
 ["1","1","0","1","1","1"]]