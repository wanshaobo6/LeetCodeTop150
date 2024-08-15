# 125. 验证回文串
# 简单
# 相关标签
# 相关企业
# 如果在将所有大写字符转换为小写字符、并移除所有非字母数字字符之后，短语正着读和反着读都一样。则可以认为该短语是一个 回文串 。
#
# 字母和数字都属于字母数字字符。
#
# 给你一个字符串 s，如果它是 回文串 ，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入: s = "A man, a plan, a canal: Panama"
# 输出：true
# 解释："amanaplanacanalpanama" 是回文串。
# 示例 2：
#
# 输入：s = "race a car"
# 输出：false
# 解释："raceacar" 不是回文串。
# 示例 3：
#
# 输入：s = " "
# 输出：true
# 解释：在移除非字母数字字符之后，s 是一个空字符串 "" 。
# 由于空字符串正着反着读都一样，所以是回文串。
#

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left <= right:
            while left <= right and self.alphaNumVal(ord(s[left])) < 0:
                left += 1
            while left <= right and self.alphaNumVal(ord(s[right])) < 0:
                right -= 1
            if left <= len(s)-1 and right >= 0 and left <= right and self.alphaNumVal(ord(s[left])) != self.alphaNumVal(ord(s[right])):
                return False
            left += 1
            right -= 1
        return True

    def alphaNumVal(self, val: int) -> int:
        if 65<= val <= 90:
            return val + 32
        elif 97 <= val <= 122 or 48 <= val <= 57:
            return val
        else:
            return -1
if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    s = "a a"
    solution = Solution()
    print(solution.isPalindrome(s))
    # print(ord('A')) #65-90
    # print(ord('z')) #97-122
    # print(ord('0')) #48-57