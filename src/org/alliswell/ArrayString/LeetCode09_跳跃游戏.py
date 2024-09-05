# TODO 还有更优解
# 55. 跳跃游戏
# 中等
#
# 相关标签
# 相关企业
# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
# 示例 2：
#
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#
#
# 提示：
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        arr_len = len(nums)
        reachable_arr = [False] * arr_len
        reachable_arr[0] = True
        # print(reachable_arr)
        for idx in range(0, arr_len):
            if reachable_arr[idx] :
                max_dist = min(arr_len-1, idx + nums[idx])
                for reached_idx in range(idx, max_dist+1):
                    reachable_arr[reached_idx] = True
        return reachable_arr[arr_len-1]


    # def canJump(self, nums: List[int]) -> bool:
    #     return self.canJumpCore(nums, 0)
    #
    # def canJumpCore(self, nums: List[int], loc: int) -> bool:
    #     arr_len = len(nums)
    #     if loc >= arr_len:
    #         return False
    #     elif loc == arr_len - 1:
    #         return True
    #     elif nums[loc] == 0:
    #         return False
    #     max_step = min(nums[loc], arr_len -1 - loc)
    #     for step in range(max_step, 0, -1):
    #         if self.canJumpCore(nums, loc + step):
    #             return True
    #     return False

if __name__ == '__main__':
    # nums1: List[int] = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    nums1: List[int] = [1,0,6,9]
    solution = Solution()
    print(solution.canJump(nums1))