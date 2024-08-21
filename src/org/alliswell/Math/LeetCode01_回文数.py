# 9. 回文数
# 简单
#
# 相关标签
# 相关企业
#
# 提示
# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
#
# 回文数
# 是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 例如，121 是回文，而 123 不是。
#
#
# 示例 1：
#
# 输入：x = 121
# 输出：true
# 示例 2：
#
# 输入：x = -121
# 输出：false
# 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3：
#
# 输入：x = 10
# 输出：false
# 解释：从右向左读, 为 01 。因此它不是一个回文数。
#
#
# 提示：
#
# -2^31 <= x <= 2^31 - 1
#
#
# 进阶：你能不将整数转为字符串来解决这个问题吗？

class Solution:
    # 重点如果反转后存在溢出的话就一定不是回文数
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_x = 0
        tmp = x
        while tmp != 0:
            single_pos = tmp % 10
            reversed_x = reversed_x * 10 + single_pos
            tmp = tmp // 10
        if reversed_x == x:
            return True
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(13521))
    print(solution.isPalindrome(13531))
    print(solution.isPalindrome(0))