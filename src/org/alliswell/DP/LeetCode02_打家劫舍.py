# 198. 打家劫舍
# 中等
#
# 相关标签
# 相关企业
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
#
#
#
# 示例 1：
#
# 输入：[1,2,3,1]
# 输出：4
# 解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
# 偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2：
#
# 输入：[2,7,9,3,1]
# 输出：12
# 解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
# 偷窃到的最高金额 = 2 + 9 + 1 = 12 。
#
#
# 提示：
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

from typing import List
class Solution:

    # 递归
    # def rob(self, nums: List[int]) -> int:
    #     return self.rob_core(nums, len(nums)-1)
    # def rob_core(self, nums: List[int], loc: int) -> int:
    #     if loc < 0:
    #         return 0
    #     return max(self.rob_core(nums, loc-1), nums[loc] + self.rob_core(nums, loc-2))


     def rob(self, nums: List[int]) -> int:
        dp_arr = [0] * len(nums)
        for idx in range(0, len(nums)):
            rob_profit = nums[idx]
            if idx-2 >= 0:
                rob_profit += dp_arr[idx-2]
            not_rob_profit = 0
            if idx-1 >= 0:
                not_rob_profit = dp_arr[idx-1]
            dp_arr[idx] = max(rob_profit, not_rob_profit)

        return dp_arr[len(dp_arr)-1]


if __name__ == '__main__':
    solution = Solution()
    nums = [2,7,9,3,1]
    # nums = [1,2,3,1]
    print(solution.rob(nums))