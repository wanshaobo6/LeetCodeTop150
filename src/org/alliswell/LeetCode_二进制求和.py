# 67. 二进制求和
# 简单
#
# 相关标签
# 相关企业
# 给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
#
#
#
# 示例 1：
#
# 输入:a = "11", b = "1"
# 输出："100"
# 示例 2：
#
# 输入：a = "1010", b = "1011"
# 输出："10101"
#
#
# 提示：
#
# 1 <= a.length, b.length <= 104
# a 和 b 仅由字符 '0' 或 '1' 组成
# 字符串如果不是 "0" ，就不含前导零


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)
        if a_len > b_len:
            diff = a_len - b_len
            b = ('0' * diff) + b
        elif a_len < b_len:
            diff = b_len - a_len
            a = ('0' * diff) + a

        result = ""
        flag = 0
        for i in range(len(a)-1, -1, -1):
            c1 = ord(a[i]) - ord('0')
            c2 = ord(b[i]) - ord('0')
            total = c1 + c2 + flag
            result = str(total % 2) + result
            flag = total // 2

        if flag == 1:
            result = '1' + result
        return result

        # 0 0 0 -- ok
        # 0 0 1 -- ok
        # 0 1 0 -- ok
        # 0 1 1 -- ok 进位
        # 1 0 0 -- ok
        # 1 0 1 --ok 进位
        # 1 1 0 -- OK  进位
        # 1 1 1 -- ok  进位


if __name__ == '__main__':
    solution = Solution()
    a = "1010"
    b = "1011"
    # a = "11111"
    # b = "1"
    print(solution.addBinary(a,b))
