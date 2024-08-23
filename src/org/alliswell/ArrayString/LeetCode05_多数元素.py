# 169. 多数元素
# 简单
#
# 相关标签
# 相关企业
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
# 示例 1：
#
# 输入：nums = [3,2,3]
# 输出：3
# 示例 2：
#
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
#
#
# 提示：
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109
#
#
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。


from typing import List
class Solution:
    # Boyer-Moore投票法:如果一个数组有大于一半的数相同，那么任意删去两个不同的数字，新数组还是会有相同的性质。
    def majorityElement(self, nums: List[int]) -> int:
        consistent = nums[0]
        times = 1
        for i in range(1, len(nums), 1):
            if nums[i] == consistent:
                times += 1
            else:
                if times == 0:
                    consistent = nums[i]
                else:
                    times -= 1
        return consistent

# Hash表
# def majorityElement(self, nums: List[int]) -> int:
#     half_len = len(nums) / 2
#     print(half_len)
#     empty_dict = {}
#     for i in nums1:
#         times = empty_dict.get(str(i), 0)
#         new_times = times + 1
#         empty_dict[str(i)] = new_times
#         if new_times > half_len:
#             return i
#


if __name__ == '__main__':
    nums1: List[int] = [1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3]
    solution = Solution()
    print(solution.majorityElement(nums1))
