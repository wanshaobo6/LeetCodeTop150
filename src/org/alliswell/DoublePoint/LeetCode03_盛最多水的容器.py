# 11. 盛最多水的容器
# 中等
# 相关标签
# 相关企业
# 提示
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
#
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 返回容器可以储存的最大水量。
#
# 说明：你不能倾斜容器。
#
#
#
# 示例 1：
#
#
#
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
# 示例 2：
#
# 输入：height = [1,1]
# 输出：1

from typing import List
class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     max_area = -1
    #     for i in range(len(height)-1):
    #         for j in range(i+1, len(height)):
    #             area = min(height[j], height[i]) * (j - i)
    #             if area > max_area:
    #                 max_area = area
    #     return max_area


    def maxArea(self, height: List[int]) -> int:
        max_area = -1
        left, right = 0, len(height)-1
        while left < right:
            if height[left] < height[right]:
                area = (right - left) * height[left]
                left += 1
            elif height[left] > height[right]:
                area = (right - left) * height[right]
                right -= 1
            else:
                area = (right - left) * height[right]
                right -= 1
                left += 1
            if area > max_area:
                max_area = area
        return max_area

if __name__ == '__main__':
    solution = Solution()

    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
    print(solution.maxArea([1,1]))
    print(solution.maxArea([]))
    print(solution.maxArea([1]))
