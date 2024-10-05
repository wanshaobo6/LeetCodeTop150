# 209. 长度最小的子数组
# 中等
#
# 相关标签
# 相关企业
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
#
# 找出该数组中满足其总和大于等于 target 的长度最小的
# 子数组
# [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
#
#
#
# 示例 1：
#
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 示例 2：
#
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 示例 3：
#
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
#
#
# 提示：
#
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 105
#
#
# 进阶：
#
# 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = 0
        cur_res, left_idx, right_idx = 0, -1, 0
        while right_idx < len(nums):
            cur_res += nums[right_idx]
            while cur_res >= target:
                # 计算最小数组长度
                cur_len = right_idx - left_idx
                min_len = min(min_len, cur_len) if min_len != 0 else cur_len
                # 右移左指针
                left_idx += 1
                cur_res -= nums[left_idx]

            right_idx += 1
        return min_len



if __name__ == '__main__':
    solution = Solution()
    # print(solution.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
    # print(solution.minSubArrayLen( 7, [2,3,1,2,4,3]))
    # print(solution.minSubArrayLen( 4, [1,4,4]))
    print(solution.minSubArrayLen( 11, [1,2,3,4,5]))