# 5. 最长回文子串
# 中等
#
# 相关标签
# 相关企业
#
# 提示
# 给你一个字符串 s，找到 s 中最长的
# 回文
#
# 子串
# 。
#
#
#
# 示例 1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 示例 2：
#
# 输入：s = "cbbd"
# 输出："bb"
#
#
# 提示：
#
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成

class Solution:
    def longestPalindrome(self, s: str) -> str:
        str = "#".join(s)
        result = s[0]
        for i in range(len(str)):
            left,right = i, i
            while left-1 >= 0 and right+1 < len(str) and str[left-1] == str[right+1]:
                left -= 1
                right += 1
            max_len = (right - left) // 2 if str[i] != "#" and str[left] == "#" else ((right - left) // 2 + 1)
            if max_len > len(result):
                result = str[left:right+1].replace("#", "")
        return result

if __name__ == '__main__':
    solution = Solution()
    # print(solution.longestPalindrome("babab"))
    # print(solution.longestPalindrome("a"))
    print(solution.longestPalindrome("ccc"))