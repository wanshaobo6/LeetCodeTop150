# 242. 有效的字母异位词
# 简单
#
# 相关标签
# 相关企业
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
#
#
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#
#
# 提示:
#
# 1 <= s.length, t.length <= 5 * 104
# s 和 t 仅包含小写字母
#
#
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        a_val = 97
        for w in s:
            arr[ord(w) - a_val] += 1
        for w in t:
            arr[ord(w) - a_val] -= 1

        for t in arr:
            if t != 0:
                return False
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.isAnagram("aaaabzb", "aaaabbz"))