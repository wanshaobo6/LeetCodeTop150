#TODO复习
#
#
# 300. 最长递增子序列
# 中等
#
# 相关标签
# 相关企业
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的
# 子序列
# 。
#
#
# 示例 1：
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#
#
# 提示：
#
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
#
# 进阶：
#
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
# 面试中遇到过这道题?
# 1/5
# 是
# 否
# 通过次数
# 993.1K
# 提交次数
# 1.8M
# 通过率
# 56.1%

# 方法一：动态规划
#
# 思路与算法
#
# 定义 dp[i] 为考虑前 i 个元素，以第 i 个数字结尾的最长上升子序列的长度，注意 nums[i] 必须被选取。
#
# 我们从小到大计算 dp 数组的值，在计算 dp[i] 之前，我们已经计算出 dp[0…i−1] 的值，则状态转移方程为：
#
# dp[i]=max(dp[j])+1,其中0≤j<i且num[j]<num[i]
# 即考虑往 dp[0…i−1] 中最长的上升子序列后面再加一个 nums[i]。由于 dp[j] 代表 nums[0…j] 中以 nums[j] 结尾的最长上升子序列，所以如果能从 dp[j] 这个状态转移过来，那么 nums[i] 必然要大于 nums[j]，才能将 nums[i] 放在 nums[j] 后面以形成更长的上升子序列。
#
# 最后，整个数组的最长上升子序列即所有 dp[i] 中的最大值=max(dp[i]),其中0≤i<len(nums)

from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp_arr = [1] * len(nums)
        for idx in range(1, len(nums)):
            max_seq = 1
            for j in range(idx):
                if nums[j] < nums[idx] and dp_arr[j] + 1 > max_seq:
                    max_seq = dp_arr[j] + 1
            dp_arr[idx] = max_seq
        # print(dp_arr)
        return max(dp_arr)


if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,6,7,9,4,10,5,6]
    # nums = [0,1,0,3,2,3]
    # nums = [7,7,7,7,7,7,7]
    print(solution.lengthOfLIS(nums))