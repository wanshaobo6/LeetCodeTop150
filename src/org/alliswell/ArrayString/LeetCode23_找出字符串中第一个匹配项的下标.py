# 28. 找出字符串中第一个匹配项的下标
# 简单
#
# 相关标签
# 相关企业
# 给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串的第一个匹配项的下标（下标从 0 开始）。如果 needle 不是 haystack 的一部分，则返回  -1 。
#
#
#
# 示例 1：
#
# 输入：haystack = "sadbutsad", needle = "sad"
# 输出：0
# 解释："sad" 在下标 0 和 6 处匹配。
# 第一个匹配项的下标是 0 ，所以返回 0 。
# 示例 2：
#
# 输入：haystack = "leetcode", needle = "leeto"
# 输出：-1
# 解释："leeto" 没有在 "leetcode" 中出现，所以返回 -1 。
#
#
# 提示：
#
# 1 <= haystack.length, needle.length <= 104
# haystack 和 needle 仅由小写英文字符组成

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def compute_lps(pattern):
            # 计算最长前缀后缀数组（Longest Prefix Suffix array）
            lps = [0] * len(pattern)
            len_pattern = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[len_pattern]:
                    len_pattern += 1
                    lps[i] = len_pattern
                    i += 1
                else:
                    if len_pattern!= 0:
                        len_pattern = lps[len_pattern - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        m = len(needle)
        n = len(haystack)
        if m == 0:
            return 0
        lps = compute_lps(needle)
        i = 0  # haystack 的索引
        j = 0  # needle 的索引
        while i < n:
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            if j == m:
                return i - j
            elif i < n and needle[j]!= haystack[i]:
                if j!= 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1