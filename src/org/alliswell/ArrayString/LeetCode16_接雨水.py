#
#
# 代码
#
# 测试用例
#
# 测试结果
# 测试结果
# 42. 接雨水
# 困难
#
# 相关标签
# 相关企业
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 示例 1：
#
#
#
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
# 示例 2：
#
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#
#
# 提示：
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5


from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        full_cap, cur_height = 0, 0
        while left <= right:
            left_val = height[left]
            right_val = height[right]
            full_cap += (right-left+1)*(min(left_val, right_val) - cur_height)
            cur_height = min(left_val, right_val)
            if left_val <= right_val:
                #从左往右找到下一个大于left_val的数
                while left <= right and height[left] <= left_val:
                    left += 1
            else:
                #从右到左找到下一个大于right_val的数
                while left <= right and height[right] <= right_val:
                    right -= 1
        return full_cap - sum(height)


if __name__ == '__main__':
    solution = Solution()
    print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(solution.trap([4,2,0,3,2,5]))