# 201. 数字范围按位与
# 中等
#
# 相关标签
# 相关企业
# 给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。
#
#
#
# 示例 1：
#
# 输入：left = 5, right = 7
# 输出：4
# 示例 2：
#
# 输入：left = 0, right = 0
# 输出：0
# 示例 3：
#
# 输入：left = 1, right = 2147483647
# 输出：0
#
#
# 提示：
#
# 0 <= left <= right <= 2^31 - 1


# m:  S S S 0 X X X X
# n:  S S S 1 X X X X
# 这个问题就是求left和right的最长公共前缀
# 解答：https://leetcode.cn/problems/bitwise-and-of-numbers-range/submissions/570465347/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right:
            return left
        res = left ^ right
        count = 0
        # 统计左边0的个数
        for i in range(31, -1, -1):
            if res >> i == 1:
                break
            else:
                count += 1
        count = 31-count
        return (left >> count) << count




if __name__ == '__main__':
    solution = Solution()
    print(solution.rangeBitwiseAnd(5, 7))
    print(solution.rangeBitwiseAnd(0, 0))
    print(solution.rangeBitwiseAnd(1, 2147483647))