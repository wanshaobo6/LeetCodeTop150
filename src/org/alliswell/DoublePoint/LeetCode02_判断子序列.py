# 392. 判断子序列
# 简单
# 相关标签
# 相关企业
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
#
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
#
# 进阶：
#
# 如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？
#
# 致谢：
#
# 特别感谢 @pbrother 添加此问题并且创建所有测试用例。
#
#
#
# 示例 1：
#
# 输入：s = "abc", t = "ahbgdc"
# 输出：true
# 示例 2：
#
# 输入：s = "axc", t = "ahbgdc"
# 输出：false
#
#
# 提示：
#
# 0 <= s.length <= 100
# 0 <= t.length <= 10^4
# 两个字符串都只由小写字符组成。

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        s_len, t_len = len(s), len(t)
        while p1 < s_len and p2 < t_len:
            if t[p2] != s[p1]:
                p2 += 1
            else:
                p1 += 1
                p2 += 1
        return p1 >= s_len


if __name__ == '__main__':
    solution = Solution()
    print(solution.isSubsequence("abc", "ahbgdc"))
    # print(ord('A')) #65-90
    # print(ord('z')) #97-122
    # print(ord('0')) #48-57