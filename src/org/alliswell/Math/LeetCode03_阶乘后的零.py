# 172. 阶乘后的零
# 中等
#
# 相关标签
# 相关企业
# 给定一个整数 n ，返回 n! 结果中尾随零的数量。
#
# 提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1
#
#
#
# 示例 1：
#
# 输入：n = 3
# 输出：0
# 解释：3! = 6 ，不含尾随 0
# 示例 2：
#
# 输入：n = 5
# 输出：1
# 解释：5! = 120 ，有一个尾随 0
# 示例 3：
#
# 输入：n = 0
# 输出：0
#
#
# 提示：
#
# 0 <= n <= 10^4

# TODO Review https://leetcode.cn/problems/factorial-trailing-zeroes/solutions/47030/xiang-xi-tong-su-de-si-lu-fen-xi-by-windliang-3/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n // 5
            n = n // 5
        return count

if __name__ == '__main__':
    solution = Solution()
    print(solution.trailingZeroes(7))