# 189. 轮转数组
# 中等
#
# 相关标签
# 相关企业
#
# 提示
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
#
#
#
# 示例 1:
#
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
# 示例 2:
#
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释:
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
#
#
# 提示：
#
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.reverse(nums, 0, len(nums) - 1)
        mod_k = k % len(nums)
        self.reverse(nums, 0, mod_k - 1)
        self.reverse(nums, mod_k, len(nums) - 1)


    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left <= right:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] =tmp
            left += 1
            right -= 1


if __name__ == '__main__':
    nums1: List[int] = [1, 1, 2, 2, 2, 3, 3, 3, 2, 1, 6]
    solution = Solution()
    # solution.reverse(nums1, 0, 3)
    solution.rotate(nums1, 4)
    print(nums1)