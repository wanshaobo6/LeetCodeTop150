# 77. 组合
# 中等
# 相关标签
# 相关企业
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：n = 4, k = 2
# 输出：
# [
#     [2,4],
#     [3,4],
#     [2,3],
#     [1,2],
#     [1,3],
#     [1,4],
# ]
# 示例 2：
#
# 输入：n = 1, k = 1
# 输出：[[1]]
#
#
# 提示：
#
# 1 <= n <= 20
# 1 <= k <= n
# 面试中遇到过这道题?
# 1/5
# 是
# 否
# 通过次数
# 766.7K
# 提交次数
# 992.2K
# 通过率
# 77.3%

from typing import List

import copy
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []
        result = []
        self.combine_core(1, n, [], k, result)
        return result


    def combine_core(self, cur: int,  n: int, arr: List[int], k: int, res: List[List[int]]):
        if len(arr) == k:
            res.append(copy.copy(arr))
        elif len(arr) < k:
            if cur <= n and (n - cur + 1) >= (k - len(arr)):
                arr.append(cur)
                self.combine_core(cur+1,  n, arr, k, res)
                arr.pop()
                self.combine_core(cur+1,  n, arr, k, res)




    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     if k > n:
    #         return []
    #     select_marks = [False] * (n + 1)
    #     result = []
    #     self.combine_core(select_marks, 1, 0, k, result)
    #     return result
    #
    #
    # def combine_core(self, select_marks: List[bool], index: int, k_c: int, k: int, res: List[List[int]]):
    #     if k_c == k:
    #         item = []
    #         for i in range(len(select_marks)):
    #             if select_marks[i]:
    #                 item.append(i)
    #         res.append(item)
    #     elif k_c < k:
    #         if index < len(select_marks) and (len(select_marks) - index) >= (k - k_c):
    #             select_marks[index] = True
    #             self.combine_core(select_marks, index+1, k_c+1, k, res)
    #             select_marks[index] = False
    #             self.combine_core(select_marks, index+1, k_c, k, res)


if __name__ == '__main__':
    solution = Solution()
    print(solution.combine(n = 4, k = 2))
