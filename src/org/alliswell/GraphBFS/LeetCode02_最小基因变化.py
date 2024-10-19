# 433. 最小基因变化
# 中等
#
# 相关标签
# 相关企业
# 基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。
#
# 假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。
#
# 例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
# 另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 bank 中）
#
# 给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数。如果无法完成此基因变化，返回 -1 。
#
# 注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。
#
#
#
# 示例 1：
#
# 输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
# 输出：1
# 示例 2：
#
# 输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# 输出：2
# 示例 3：
#
# 输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
# 输出：3
#
#
# 提示：
#
# start.length == 8
# end.length == 8
# 0 <= bank.length <= 10
# bank[i].length == 8
# start、end 和 bank[i] 仅由字符 ['A', 'C', 'G', 'T'] 组成

from collections import deque
from typing import List
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def can_transfer(from_gen: str, to_gen:str) -> bool:
            diff_cnt = 0
            for i in range(8):
                if from_gen[i] != to_gen[i]:
                    diff_cnt+=1
            return diff_cnt == 1

        visit = set()
        queue = deque([(startGene, 0)])
        while queue:
            start, step = queue.popleft()
            visit.add(start)
            for next_gen in bank:
                if next_gen in visit or not can_transfer(start, next_gen):
                    continue
                if next_gen == endGene:
                    return step + 1
                queue.append((next_gen, step+1))

        return -1

if __name__ == '__main__':
    solution = Solution()
    print(solution.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
    print(solution.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]))
    print(solution.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"]))