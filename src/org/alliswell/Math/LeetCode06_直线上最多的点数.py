# 149. 直线上最多的点数
# 困难
#
# 相关标签
# 相关企业
# 给你一个数组 points ，其中 points[i] = [xi, yi] 表示 X-Y 平面上的一个点。求最多有多少个点在同一条直线上。
#
#
#
# 示例 1：
#
#
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：3
# 示例 2：
#
#
# 输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# 输出：4
#
#
# 提示：
#
# 1 <= points.length <= 300
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# points 中的所有点 互不相同

from typing import List
import collections
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points_len = len(points)
        max_points = 1
        for i in range(points_len-1):
            gradient_map = collections.defaultdict(lambda: 1)
            for j in range(i + 1, points_len):
                gradient = self.getGradient(points[i], points[j])
                gradient_map[gradient] += 1
            cur_max_points = max(gradient_map.values())
            if cur_max_points > max_points:
                max_points = cur_max_points
        return max_points
    def getGradient(self, p1: List[int], p2: List[int]) -> float:
        if p1[0] == p2[0]:
            return 0
        if p1[1] == p2[1]:
            return float('inf')
        return (p1[1] - p2[1])/(p1[0] - p2[0])


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxPoints(points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
    print(solution.maxPoints(points = [[1,1],[2,2],[3,3]]))
