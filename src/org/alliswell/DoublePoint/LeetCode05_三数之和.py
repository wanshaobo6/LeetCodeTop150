# TODO 没做出来
# 15. 三数之和
# 中等
# 相关标签
# 相关企业
# 提示
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
#
#
# 示例 1：
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
# 示例 2：
#
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
# 示例 3：
#
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#
#
# 提示：
#
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105
#-7 -5 -3 2 5 8

#解法
# 排序 + 双指针
#
# 本题的难点在于如何去除重复解。
#
# 算法流程：
#
# 特判，对于数组长度 n，如果数组为 null 或者数组长度小于 3，返回 []。
# 对数组进行排序。
# 遍历排序后数组：
# 若 nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 0，直接返回结果。
# 对于重复元素：跳过，避免出现重复解
# 令左指针 L=i+1，右指针 R=n−1，当 L<R 时，执行循环：
# 当 nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,R 移到下一位置，寻找新的解
# 若和大于 0，说明 nums[R] 太大，R 左移
# 若和小于 0，说明 nums[L] 太小，L 右移
#
# 作者：吴彦祖
# 链接：https://leetcode.cn/problems/3sum/solutions/39722/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not nums or n < 3:
            return []
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L = i+1
            R = n-1
            while L < R:
                val = nums[i] + nums[L] + nums[R]
                if val == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < n and nums[L] == nums[L-1]:
                        L += 1
                    while R > 0 and nums[R] == nums[R+1]:
                        R -= 1
                elif val > 0:
                    R -= 1
                else:
                    L += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.threeSum(nums = [-1,0,1,2,-1,-4]))
    print(solution.threeSum(nums = [0,1,1]))
    print(solution.threeSum(nums = [0,0,0]))
