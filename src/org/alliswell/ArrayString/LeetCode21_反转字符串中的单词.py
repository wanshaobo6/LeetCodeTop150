# 151. 反转字符串中的单词
# 中等
#
# 相关标签
# 相关企业
# 给你一个字符串 s ，请你反转字符串中 单词 的顺序。
#
# 单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
#
# 返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
#
# 注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。
#
#
#
# 示例 1：
#
# 输入：s = "the sky is blue"
# 输出："blue is sky the"
# 示例 2：
#
# 输入：s = "  hello world  "
# 输出："world hello"
# 解释：反转后的字符串中不能存在前导空格和尾随空格。
# 示例 3：
#
# 输入：s = "a good   example"
# 输出："example good a"
# 解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。
#
#
# 提示：
#
# 1 <= s.length <= 10^4
# s 包含英文大小写字母、数字和空格 ' '
# s 中 至少存在一个 单词
#
#
# 进阶：如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 O(1) 额外空间复杂度的 原地 解法

class Solution:

    def reverseWords(self, s: str) -> str:
        s = s.strip()                            # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1])          # 添加单词
            while i >= 0 and s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i                                # j 指向下个单词的尾字符
        return ' '.join(res)                     # 拼接并返回

    def reverseWords1(self, s: str) -> str:
        words_stack = []
        right_idx = len(s) - 1
        res = ''
        while right_idx >= 0:
            #找到非空字符
            while right_idx >= 0 and s[right_idx] == ' ':
                right_idx -= 1
            #入栈
            while right_idx >= 0 and s[right_idx] != ' ':
                words_stack.append(s[right_idx])
                right_idx -= 1
            if len(res) != 0 and len(words_stack) != 0:
                res += ' '
            while len(words_stack) != 0:
                res += words_stack.pop()
        return res

if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseWords("a good   example"))
    print(solution.reverseWords("  hello world  "))