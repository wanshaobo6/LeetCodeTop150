# TODO 没做出来  https://leetcode.cn/problems/single-number-ii/solutions/8944/single-number-ii-mo-ni-san-jin-zhi-fa-by-jin407891/?envType=study-plan-v2&envId=top-interview-150
# 137. 只出现一次的数字 II
# 中等
# 相关标签
# 相关企业
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
#
# 你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [2,2,3,2]
# 输出：3
# 示例 2：
#
# 输入：nums = [0,1,0,1,0,1,99]
# 输出：99
#
#
# 提示：
#
# 1 <= nums.length <= 3 * 104
# -2^31 <= nums[i] <= 2^31 - 1
# nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones


if __name__ == '__main__':
    solution = Solution()
    # print(solution.singleNumber(nums = [0,1,0,1,0,1,99]))
    print(solution.singleNumber(nums = [2,2,3,2]))