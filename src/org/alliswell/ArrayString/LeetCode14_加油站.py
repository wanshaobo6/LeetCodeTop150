# 134. 加油站
# 中等
#
# 相关标签
# 相关企业
# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。
#
#
#
# 示例 1:
#
# 输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# 输出: 3
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
# 示例 2:
#
# 输入: gas = [2,3,4], cost = [3,4,3]
# 输出: -1
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。
#
#
# 提示:
#
# gas.length == n
# cost.length == n
# 1 <= n <= 10^5
# 0 <= gas[i], cost[i] <= 10^4

from typing import List
import sys
class Solution:
    # 官方题解:
    #    1.如果整体加的油大于用的油, 环路一定能走完
    #    2.亏空最严重的一个点必须放在最后一步走，等着前面剩余的救助
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        spare = 0
        min_spare = sys.maxsize
        min_index = 0

        for i in range(len(gas)):
            spare += gas[i] - cost[i]
            if spare < min_spare:
                min_spare = spare
                min_index = i
        if spare < 0:
            return -1
        else:
            return (min_index + 1) % len(gas)

    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     arr_len = len(gas)
    #     rest_arr = [0] * arr_len
    #     for idx in range(0, arr_len):
    #         rest_arr[idx] = gas[idx] - cost[idx]
    #
    #     best_start_point = -1
    #     cur_gas_vol = 0
    #     min_gas_vol = sys.maxsize
    #     #两次循环找到亏油最大的一段路程
    #     for log_idx in range(0, 2*arr_len):
    #         idx = log_idx % arr_len
    #         cur_gas_vol += rest_arr[idx]
    #         if cur_gas_vol >= 0:
    #             cur_gas_vol = 0
    #         if cur_gas_vol < min_gas_vol:
    #             min_gas_vol = cur_gas_vol
    #             best_start_point = (idx + 1) % arr_len
    #
    #     cur_gas_vol = 0
    #     #判断从该点出发是否能够行驶一周
    #     for log_idx in range(best_start_point, best_start_point + arr_len):
    #         idx = log_idx % arr_len
    #         cur_gas_vol += rest_arr[idx]
    #         if cur_gas_vol < 0:
    #             return -1
    #     return best_start_point


if __name__ == '__main__':
    gas: List[int] = [5,4,12,1,11]
    cost: List[int] = [5,4,12,1,11]
    solution = Solution()
    print(solution.canCompleteCircuit(gas, cost))