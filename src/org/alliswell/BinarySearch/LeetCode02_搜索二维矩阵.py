# 74. 搜索二维矩阵
# 中等
#
# 相关标签
# 相关企业
# 给你一个满足下述两条属性的 m x n 整数矩阵：
#
# 每行中的整数从左到右按非严格递增顺序排列。
# 每行的第一个整数大于前一行的最后一个整数。
# 给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
# 示例 2：
#
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
#
#
# 提示：
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4

from typing import List
class Solution:

    # 时间复杂度O(log(m+n))
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     m = len(matrix)
    #     n = len(matrix[0])
    #
    #     left = 0
    #     right = m*n-1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         row = mid // n
    #         col = mid % n
    #         if matrix[row][col] < target:
    #             left = mid + 1
    #         elif matrix[row][col] > target:
    #             right = mid - 1
    #         else:
    #             return True
    #     return False

    # 排除法 复杂度O(m+n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m and j >= 0:  # 还有剩余元素
            if matrix[i][j] == target:
                return True  # 找到 target
            if matrix[i][j] < target:
                i += 1  # 这一行剩余元素全部小于 target，排除
            else:
                j -= 1  # 这一列剩余元素全部大于 target，排除
        return False



if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = -1
    print(solution.searchMatrix(matrix, target))