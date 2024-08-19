# 54. 螺旋矩阵
# 中等
#
# 相关标签
# 相关企业
#
# 提示
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：
#
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        metrix_cnt = m*n
        result = []
        visited_metrix = [[False for _ in range(n)] for _ in range(m)]
        visited_cnt = 0
        plan_arr = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        plan_idx = 0

        x,y =0,0
        while visited_cnt < metrix_cnt:
            expect_x = x + plan_arr[plan_idx][0]
            expect_y = y + plan_arr[plan_idx][1]
            if expect_x < 0 or expect_x >= m or expect_y < 0 or expect_y >= n or visited_metrix[expect_x][expect_y]:
                plan_idx = (plan_idx + 1) % 4

            visited_metrix[x][y] = True
            visited_cnt += 1
            result.append(matrix[x][y])

            x = x + plan_arr[plan_idx][0]
            y = y + plan_arr[plan_idx][1]

        return result

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(solution.spiralOrder(matrix))
