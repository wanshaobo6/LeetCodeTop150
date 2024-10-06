# 162. 寻找峰值
# 中等
#
# 相关标签
# 相关企业
# 峰值元素是指其值严格大于左右相邻值的元素。
#
# 给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞ 。
#
# 你必须实现时间复杂度为 O(log n) 的算法来解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,1]
# 输出：2
# 解释：3 是峰值元素，你的函数应该返回其索引 2。
# 示例 2：
#
# 输入：nums = [1,2,1,3,5,6,4]
# 输出：1 或 5
# 解释：你的函数可以返回索引 1，其峰值元素为 2；
# 或者返回索引 5， 其峰值元素为 6。
#
#
# 提示：
#
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# 对于所有有效的 i 都有 nums[i] != nums[i + 1]



#TODO 复习
#注意：你可以假设 nums[-1] = nums[n] = -∞ 。
#所以往上坡方向去找 一定能找到峰值
# 思路
#
# 标签：二分查找
# 过程：
# 首先要注意题目条件，在题目描述中出现了 nums[-1] = nums[n] = -∞，这就代表着 只要数组中存在一个元素比相邻元素大，那么沿着它一定可以找到一个峰值
# 根据上述结论，我们就可以使用二分查找找到峰值
# 查找时，左指针 l，右指针 r，以其保持左右顺序为循环条件
# 根据左右指针计算中间位置 m，并比较 m 与 m+1 的值，如果 m 较大，则左侧存在峰值，r = m，如果 m + 1 较大，则右侧存在峰值，l = m + 1
# 时间复杂度：O(logN)
# 解答：https://leetcode.cn/problems/find-peak-element/submissions/570375614/?envType=study-plan-v2&envId=top-interview-150

from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left



if __name__ == '__main__':
    solution = Solution()
    print(solution.findPeakElement(nums = [1,2,1,3,5,6,4]))