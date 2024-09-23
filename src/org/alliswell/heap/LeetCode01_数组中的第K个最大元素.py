# 215. 数组中的第K个最大元素
# 中等
#
# 相关标签
# 相关企业
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1:
#
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
# 示例 2:
#
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4
#
#
# 提示：
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4

from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        list = heapq.nlargest(k, nums)
        return list[len(list) - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findKthLargest([3,2,1,5,6,4], 2))
    print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))