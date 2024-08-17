# 219. 存在重复元素 II
# 简单
#
# 相关标签
# 相关企业
# 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3,1], k = 3
# 输出：true
# 示例 2：
#
# 输入：nums = [1,0,1,1], k = 1
# 输出：true
# 示例 3：
#
# 输入：nums = [1,2,3,1,2,3], k = 2
# 输出：false
#
#
#
#
# 提示：
#
# 1 <= nums.length <= 10^5
# -109 <= nums[i] <= 10^9
# 0 <= k <= 10^5

from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        idx_map = {}
        for idx in range(len(nums)):
            comple_idx = idx_map.get(nums[idx])
            if comple_idx is not None and idx - comple_idx <= k:
                return True
            idx_map[nums[idx]] = idx
        return False

if __name__ == '__main__':
    solution = Solution()
    # print(solution.containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
    # print(solution.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
    # print(solution.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
    print(solution.containsNearbyDuplicate(nums = [9, 9], k = 2))