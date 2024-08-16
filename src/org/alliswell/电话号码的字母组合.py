# 17. 电话号码的字母组合
# 中等
# 相关标签
# 相关企业
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
#
#
# 示例 1：
#
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 示例 2：
#
# 输入：digits = ""
# 输出：[]
# 示例 3：
#
# 输入：digits = "2"
# 输出：["a","b","c"]
#
#
# 提示：
#
# 0 <= digits.length <= 4
# digits[i] 是范围 ['2', '9'] 的一个数字。

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if len(digits) == 0:
            return result
        alpha_list = [['a', 'b', 'c'],  # 2
                      ['d', 'e', 'f'],  # 3
                      ['g', 'h', 'i'],  # 4
                      ['j', 'k', 'l'],  # 5
                      ['m', 'n', 'o'],  # 6
                      ['p', 'q', 'r', 's'],  # 7
                      ['t', 'u', 'v'],  # 8
                      ['w', 'x', 'y', 'z']]  # 9
        self.letterCombinations_core(digits, 0, "", alpha_list, result)
        return result

    def letterCombinations_core(self, digits: str, i: int, words: str, alpha_list: List[List[str]], result: List[str]):
        if i >= len(digits):
            result.append(words)
            return
        alpha_idx = ord(digits[i]) - ord('2')
        for w in alpha_list[alpha_idx]:
            self.letterCombinations_core(digits, i+1, words+w, alpha_list, result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations("23"))
    print(solution.letterCombinations(""))
    print(solution.letterCombinations("2"))
