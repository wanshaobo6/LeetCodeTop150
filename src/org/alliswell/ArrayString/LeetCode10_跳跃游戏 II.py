# 45. 跳跃游戏 II
# 中等
#
# 相关标签
# 相关企业
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
#
# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
#
# 0 <= j <= nums[i]
# i + j < n
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
#
#
#
# 示例 1:
#
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 示例 2:
#
# 输入: nums = [2,3,0,1,4]
# 输出: 2
#
#
# 提示:
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# 题目保证可以到达 nums[n-1]


from typing import List
import sys
class Solution:
    def jump(self, nums: List[int]) -> int:
        arr_len = len(nums)
        min_step_arr = [sys.maxsize] * arr_len
        min_step_arr[0] = 0
        for idx in range(0, arr_len):
            max_dist = min(arr_len-1, idx + nums[idx])
            for reach_idx in range(idx + 1, max_dist + 1):
                min_step_arr[reach_idx] = min(min_step_arr[idx] + 1, min_step_arr[reach_idx])
        return min_step_arr[arr_len-1]

if __name__ == '__main__':
    # nums1: List[int] = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    nums1: List[int] = [2,3,1,1,4]
    nums1: List[int] = [3,3,0,1,4]
    solution = Solution()
    print(solution.jump(nums1))