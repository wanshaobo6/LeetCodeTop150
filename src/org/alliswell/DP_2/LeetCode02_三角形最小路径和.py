# 120. 三角形最小路径和
# 中等
#
# 相关标签
# 相关企业
# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
#
# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
#
#
#
# 示例 1：
#
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
# 2
# 3 4
# 6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
# 示例 2：
#
# 输入：triangle = [[-10]]
# 输出：-10
#
#
# 提示：
#
# 1 <= triangle.length <= 200
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -104 <= triangle[i][j] <= 104
#
#
# 进阶：
#
# 你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？

from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        for i in range(1, height):
            pre_row = triangle[i-1]
            cur_row = triangle[i]
            cur_row[0] = pre_row[0] + cur_row[0]
            cur_row[-1] = pre_row[-1] + cur_row[-1]
            for j in range(1, len(cur_row)-1):
                cur_row[j] = min(pre_row[j], pre_row[j-1]) + cur_row[j]
        return min(triangle[height-1])

if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))