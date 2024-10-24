# 76. 最小覆盖子串
# 困难
#
# 相关标签
# 相关企业
#
# 提示
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
#
#
# 注意：
#
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
# 示例 1：
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
# 示例 2：
#
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
# 示例 3:
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
#
#
# 提示：
#
# m == s.length
# n == t.length
# 1 <= m, n <= 10^5
# s 和 t 由英文字母组成
#
#
# 进阶：你能设计一个在 o(m+n) 时间内解决此问题的算法吗？


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count, diff_count, dict_map = 0, 0, {}
        for tc in t:
            if tc in dict_map:
                dict_map[tc] += 1
            else:
                dict_map[tc] = 1
                diff_count += 1
        min_str, left, right = "", 0, 0

        while right < len(s) and left < len(s) :
            # 右指找到能构成覆盖子串的右边界
            while count != diff_count and right < len(s):
                c = s[right]
                if c in dict_map:
                    dict_map[c] -= 1
                    if dict_map[c] == 0:
                        count += 1
                right += 1
            # 右指找到能构成覆盖子串的左边界
            while count == diff_count and  left < right:
                c = s[left]
                if c in dict_map:
                    if dict_map[c] == 0:
                        # 计算子串长度
                        substr_len = right - left
                        if min_str == "" or len(min_str) > substr_len:
                            min_str = s[left: right]
                        count -= 1
                    dict_map[c] += 1
                left += 1
        return min_str

if __name__ == '__main__':
    solution = Solution()
    # print(solution.minWindow("ADOBECODEBANC", "ABC"))
    # print(solution.minWindow("aa", "a"))
    # print(solution.minWindow("aa", "aa"))
    print(solution.minWindow("bdab", "ab"))