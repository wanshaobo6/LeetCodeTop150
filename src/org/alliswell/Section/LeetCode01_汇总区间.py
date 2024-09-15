# 228. 汇总区间
<<<<<<< HEAD
# 已解答
# 简单
#
=======
# 简单
>>>>>>> 20240915 solved 1
# 相关标签
# 相关企业
# 给定一个  无重复元素 的 有序 整数数组 nums 。
#
# 返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表 。也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
#
# 列表中的每个区间范围 [a,b] 应该按如下格式输出：
#
# "a->b" ，如果 a != b
# "a" ，如果 a == b
#
#
# 示例 1：
#
# 输入：nums = [0,1,2,4,5,7]
# 输出：["0->2","4->5","7"]
# 解释：区间范围是：
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# 示例 2：
#
# 输入：nums = [0,2,3,4,6,8,9]
# 输出：["0","2->4","6","8->9"]
# 解释：区间范围是：
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
#
#
# 提示：
#
# 0 <= nums.length <= 20
# -2^31 <= nums[i] <= 2^31 - 1
# nums 中的所有值都 互不相同
# nums 按升序排列

from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums or len(nums) <= 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        result = []
        start_idx = 0
        succession = 1
        for num_idx in range(1, len(nums)):
            if nums[num_idx] == nums[start_idx] + succession:
                succession += 1
            else:
                if succession == 1:
                    result.append(str(nums[start_idx]))
                else:
                    result.append(str(nums[start_idx]) + "->" + str(nums[start_idx+succession-1]))
                start_idx = num_idx
                succession = 1
            if num_idx == len(nums) - 1:
                if succession == 1:
                    result.append(str(nums[start_idx]))
                else:
                    result.append(str(nums[start_idx]) + "->" + str(nums[start_idx+succession-1]))
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.summaryRanges(nums = [0,1,2,4,5,7]))
    print(solution.summaryRanges(nums = [0,2,3,4,6,8,9]))
