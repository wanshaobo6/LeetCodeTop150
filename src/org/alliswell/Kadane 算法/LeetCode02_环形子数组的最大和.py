# TODO Review
#
# 代码
#
# 测试用例
#
# 测试结果
# 测试结果
# 918. 环形子数组的最大和
# 中等
#
# 相关标签
# 相关企业
#
# 提示
# 给定一个长度为 n 的环形整数数组 nums ，返回 nums 的非空 子数组 的最大可能和 。
#
# 环形数组 意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i] 的前一个元素是 nums[(i - 1 + n) % n] 。
#
# 子数组 最多只能包含固定缓冲区 nums 中的每个元素一次。形式上，对于子数组 nums[i], nums[i + 1], ..., nums[j] ，不存在 i <= k1, k2 <= j 其中 k1 % n == k2 % n 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,-2,3,-2]
# 输出：3
# 解释：从子数组 [3] 得到最大和 3
# 示例 2：
#
# 输入：nums = [5,-3,5]
# 输出：10
# 解释：从子数组 [5,5] 得到最大和 5 + 5 = 10
# 示例 3：
#
# 输入：nums = [3,-2,2,-3]
# 输出：3
# 解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3
#
#
# 提示：
#
# n == nums.length
# 1 <= n <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 104

import sys
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_s, cur_max, min_s, cur_min, total = -sys.maxsize, 0, sys.maxsize, 0, 0
        for num in nums:
            total += num
            cur_max, cur_min = cur_max + num, cur_min + num
            if cur_max > max_s:
                max_s = cur_max
            if cur_min < min_s:
                min_s = cur_min
            if cur_max < 0:
                cur_max = 0
            if cur_min > 0:
                cur_min = 0
        return max_s if total == min_s else max(max_s, total-min_s)

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxSubarraySumCircular([1,-2,3,-2]))
    print(solution.maxSubarraySumCircular([5,-3,5]))
    print(solution.maxSubarraySumCircular([3,-2,2,-3]))