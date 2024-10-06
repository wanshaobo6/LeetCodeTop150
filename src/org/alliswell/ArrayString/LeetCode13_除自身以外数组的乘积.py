# 238. 除自身以外数组的乘积
# 中等
# 相关标签
# 相关企业
# 提示
# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
#
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
#
# 请 不要使用除法，且在 O(n) 时间复杂度内完成此题。
#
#
#
# 示例 1:
#
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]
# 示例 2:
#
# 输入: nums = [-1,1,0,-3,3]
# 输出: [0,0,9,0,0]
#
#
# 提示：
#
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans, tmp = [1] * len(nums), 1
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1] # 下三角
        for i in range(len(nums) - 2, -1, -1):
            tmp *= nums[i + 1]                # 上三角
            ans[i] *= tmp                     # 下三角 * 上三角
        return ans



if __name__ == '__main__':
    nums1: List[int] = [1,3,1,4]
    solution = Solution()
    print(solution.productExceptSelf(nums1))