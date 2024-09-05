#
#
# 代码
#
# 测试用例
#
# 测试结果
# 测试结果
# 34. 在排序数组中查找元素的第一个和最后一个位置
# 中等
#
# 相关标签
# 相关企业
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
# 示例 2：
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
# 示例 3：
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
#
# 提示：
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums 是一个非递减数组
# -10^9 <= target <= 10^9

from typing import List
class Solution:
    # 先二分查找 然后外扩
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     idx = self.bin_search(nums, target)
    #     if idx == -1:
    #         return [-1, -1]
    #     left, right = idx, idx
    #     while left > 0 and nums[left - 1] == target:
    #         left -= 1
    #     while right < len(nums)-1 and nums[right + 1] == target:
    #         right += 1
    #     return [left, right]
    # def bin_search(self, nums: List[int], target: int) -> int:
    #     if nums is None:
    #         return -1
    #     left, right = 0, len(nums)-1
    #     while left <= right:
    #         mid = (left + right) >> 1
    #         if target == nums[mid]:
    #             return mid
    #         elif target > nums[mid]:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return -1

    # 方法2: 两次二分查找
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) >> 1
            if target == nums[mid]:
                first = mid
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) >> 1
            if target == nums[mid]:
                last = mid
                left = mid + 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return [first, last]
if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange(nums = [5,7,7,8,8,10], target = 7))
    print(solution.searchRange(nums = [2, 2], target = 2))
