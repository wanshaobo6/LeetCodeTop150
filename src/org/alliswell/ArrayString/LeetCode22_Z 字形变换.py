# 6. Z 字形变换
# 中等
#
# 相关标签
# 相关企业
# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
#
#
# 示例 1：
#
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
# 示例 2：
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 示例 3：
#
# 输入：s = "A", numRows = 1
# 输出："A"
#
#
# 提示：
#
# 1 <= s.length <= 1000
# s 由英文字母（小写和大写）、',' 和 '.' 组成
# 1 <= numRows <= 1000


class Solution:

    # 也可以创建numrows个数组 然后便利字符串s决定其中每个字符应该放到哪个数组里面  最后对数组做字符拼接
    # class Solution:
    #     def convert(self, s: str, numRows: int) -> str:
    #         if numRows < 2: return s
    #         res = ["" for _ in range(numRows)]
    #         i, flag = 0, -1
    #         for c in s:
    #             res[i] += c
    #             if i == 0 or i == numRows - 1: flag = -flag
    #             i += flag
    #         return "".join(res)

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ""
        s_len = len(s)
        step_arr = [0,0]
        for i in range(numRows):
            if i == numRows -1:
                step_arr[0] = 2*i
            else:
                step_arr[0] = 2*(numRows - i) - 2
            if i == 0:
                step_arr[1] = 2*(numRows - i) - 2
            else:
                step_arr[1] = 2*i

            j = i
            step = 0
            while j < s_len:
                result += s[j]
                j += step_arr[step]
                step ^= 1
        return result

if __name__ == '__main__':
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 3))
    print(solution.convert("PAYPALISHIRING", 4))
    print(solution.convert("AB", 2))
    print(solution.convert("A", 1))
