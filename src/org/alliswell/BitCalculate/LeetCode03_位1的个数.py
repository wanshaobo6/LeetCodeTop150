# 191. 位1的个数
# 简单
#
# 相关标签
# 相关企业
# 编写一个函数，获取一个正整数的二进制形式并返回其二进制表达式中
# 设置位
# 的个数（也被称为汉明重量）。
#
#
#
# 示例 1：
#
# 输入：n = 11
# 输出：3
# 解释：输入的二进制串 1011 中，共有 3 个设置位。
# 示例 2：
#
# 输入：n = 128
# 输出：1
# 解释：输入的二进制串 10000000 中，共有 1 个设置位。
# 示例 3：
#
# 输入：n = 2147483645
# 输出：30
# 解释：输入的二进制串 11111111111111111111111111111101 中，共有 30 个设置位。
#
#
# 提示：
#
# 1 <= n <= 2^31 - 1
#
#
# 进阶：
#
# 如果多次调用这个函数，你将如何优化你的算法？

class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     result = 0
    #     for i in range(31):
    #         if (1 << i) & n != 0:
    #             result += 1
    #     return result


    # n&(n-1) 得到的结果每次都能消去一个1
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n != 0:
            n = n&(n-1)
            result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(11))
    print(solution.hammingWeight(128))
    print(solution.hammingWeight(2147483645))