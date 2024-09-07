# TODO 复习一下
# 39. 组合总和
# 中等
# 相关标签
# 相关企业
# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
#
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
#
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
#
#
#
# 示例 1：
#
# 输入：candidates = [2,3,6,7], target = 7
# 输出：[[2,2,3],[7]]
# 解释：
# 2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
# 7 也是一个候选， 7 = 7 。
# 仅有这两种组合。
# 示例 2：
#
# 输入: candidates = [2,3,5], target = 8
# 输出: [[2,2,2,2],[2,3,3],[3,5]]
# 示例 3：
#
# 输入: candidates = [2], target = 1
# 输出: []
#
#
# 提示：
#
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# candidates 的所有元素 互不相同
# 1 <= target <= 40

from typing import List
import copy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result_item = []
        result = []
        self.combinationSum_core(candidates, 0, result_item, 0, target, result)
        return result


    def combinationSum_core(self, candidates: List[int], idx: int, result_item: List[int], cur_total: int, target: int, res: List[List[int]]):
        if cur_total == target:
            res.append(copy.copy(result_item))
            return

        if idx >= len(candidates):
            return

        self.combinationSum_core(candidates, idx+1, result_item, cur_total, target, res)

        new_total = cur_total + candidates[idx]
        if new_total <= target:
            result_item.append(candidates[idx])
            self.combinationSum_core(candidates, idx, result_item, new_total, target, res)
            result_item.pop()

if __name__ == '__main__':
    solution = Solution()
    # print(solution.combinationSum(candidates = [2,3,6,7], target = 7))
    # print(solution.combinationSum(candidates = [8,7,4,3], target = 11))
    print(solution.combinationSum(candidates = [2,22,4,17,28,13,39,27,24,37,12,30,5,23,29,8,16,34,15,36,14,10,31], target = 30))
