# 53. 最大子数组和
# 中等
#
# 相关标签
# 相关企业
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组
# 是数组中的一个连续部分。
#
#
#
# 示例 1：
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 示例 2：
#
# 输入：nums = [1]
# 输出：1
# 示例 3：
#
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#
#
# 提示：
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。


from typing import List
class Solution:
    #Method1 贪心法: 若当前元素所指向的元素之前的和小于0 则丢弃当前元素之前的数列
    # def maxSubArray(self, nums: List[int]) -> int:
    #     global_max = None
    #     cur_max = 0
    #     for num in nums:
    #         cur_max += num
    #         if global_max is None or cur_max > global_max:
    #             global_max = cur_max
    #         if cur_max < 0:
    #             cur_max = 0
    #     return global_max

    #Method2  DP
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i] + nums[i-1], nums[i])
        return max(nums)

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
    print(solution.maxSubArray(nums = [1]))
    print(solution.maxSubArray(nums = [5,4,-1,7,8]))
