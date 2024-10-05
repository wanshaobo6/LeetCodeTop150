# 3. 无重复字符的最长子串
# 中等
#
# 相关标签
# 相关企业
#
# 提示
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长
# 子串
# 的长度。
#
#
#
# 示例 1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#
#
# 提示：
#
# 0 <= s.length <= 5 * 104
# s 由英文字母、数字、符号和空格组成


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_succession = 0
        not_dup_set = set()
        left_idx, right_idx = 0, 0
        while right_idx < len(s):
            c = s[right_idx]
            while c in not_dup_set:
                not_dup_set.remove(s[left_idx])
                left_idx += 1
            not_dup_set.add(c)
            max_succession = max(max_succession, len(not_dup_set))
            right_idx += 1
        return max_succession

if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))