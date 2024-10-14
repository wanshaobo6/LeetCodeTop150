# 399. 除法求值
# 中等
# 相关标签
# 相关企业
# 提示
# 给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。
#
# 另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。
#
# 返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。
#
# 注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。
#
# 注意：未在等式列表中出现的变量是未定义的，因此无法确定它们的答案。
#
#
#
# 示例 1：
#
# 输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# 输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
# 解释：
# 条件：a / b = 2.0, b / c = 3.0
# 问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# 结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
# 注意：x 是未定义的 => -1.0
# 示例 2：
#
# 输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# 输出：[3.75000,0.40000,5.00000,0.20000]
# 示例 3：
#
# 输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# 输出：[0.50000,2.00000,-1.00000,-1.00000]
#
#
# 提示：
#
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj 由小写英文字母与数字组成

from typing import List
from collections import defaultdict
class TransNode:
    def __init__(self, name: str, multiple: float):
        self.name = name
        self.multiple = multiple
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        trans_map = defaultdict(list)
        equations_len = len(equations)
        for i in range(equations_len):
            divisor, dividend = equations[i][0], equations[i][1]
            value = values[i]
            trans_map[divisor].append(TransNode(name=dividend, multiple=value))
            trans_map[dividend].append(TransNode(name=divisor, multiple=1/value))
        queries_len = len(queries)
        result = [-1]*queries_len
        for i in range(queries_len):
            divisor, dividend = queries[i][0], queries[i][1]
            result[i] = self.getMultiple(divisor, 1, dividend, trans_map, set())
        return result

    def getMultiple(self, mid_unit:str, multiple: int, target_unit:str, trans_map:map, trace_set:set) -> int:
        if mid_unit not in trans_map:
            return -1
        if mid_unit == target_unit:
            return multiple
        try:
            trace_set.add(mid_unit)
            for transNode in trans_map[mid_unit]:
                next_multiple = transNode.multiple
                next_unit = transNode.name
                if next_unit in trace_set:
                    continue
                rt_multiple = self.getMultiple(next_unit, multiple*next_multiple, target_unit, trans_map, trace_set)
                if rt_multiple != -1:
                    return rt_multiple
            return -1
        finally:
            trace_set.remove(mid_unit)

if __name__ == '__main__':
    solution = Solution()
    print(solution.calcEquation([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))