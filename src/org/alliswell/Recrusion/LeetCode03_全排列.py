# 46. 全排列
# 中等
# 相关标签
# 相关企业
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 示例 2：
#
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
# 示例 3：
#
# 输入：nums = [1]
# 输出：[[1]]
#
#
# 提示：
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同

from typing import List

import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        result_item = []
        result = []
        self.permute_core(nums, 0, visited, result_item, result)
        return result


    def permute_core(self, nums: List[int], index: int, visited: set, result_item: List[int], res: List[List[int]]):
        if index >= len(nums):
            res.append(copy.copy(result_item))
            return
        for num in nums:
            if num in visited:
                continue
            visited.add(num)
            result_item.append(num)
            self.permute_core(nums, index+1, visited, result_item, res)
            visited.remove(num)
            result_item.pop()

if __name__ == '__main__':
    solution = Solution()
    print(solution.permute(nums = [1,2,3]))
    print(solution.permute(nums = [0, 1]))
    print(solution.permute(nums = [1]))