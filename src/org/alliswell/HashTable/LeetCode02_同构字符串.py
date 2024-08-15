# 205. 同构字符串
# 简单
#
# 相关标签
# 相关企业
# 给定两个字符串 s 和 t ，判断它们是否是同构的。
#
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
#
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
#
#
#
# 示例 1:
#
# 输入：s = "egg", t = "add"
# 输出：true
# 示例 2：
#
# 输入：s = "foo", t = "bar"
# 输出：false
# 示例 3：
#
# 输入：s = "paper", t = "title"
# 输出：true
#
#
# 提示：
#
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s 和 t 由任意有效的 ASCII 字符组成
#
#
#
#
# 解题思路: 正向和反向都不存在映射冲突则他们是同构字符串
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self.isIsomorphicHelper(s, t) and self.isIsomorphicHelper(t, s)


    def isIsomorphicHelper(self, s: str, t: str) -> bool:
        mapping = {}
        for i in range(len(s)):
            if mapping.get(s[i]) == None:
                mapping[s[i]] = t[i]
            elif mapping.get(s[i]) != t[i]:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))
    print(solution.isIsomorphic("paper", "title"))
    print(solution.isIsomorphic("foo", "tar"))