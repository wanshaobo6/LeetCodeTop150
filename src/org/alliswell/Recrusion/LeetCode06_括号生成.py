# 22. 括号生成
# 中等
#
# 相关标签
# 相关企业
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
#
# 输入：n = 1
# 输出：["()"]
#
#
# 提示：
#
# 1 <= n <= 8


from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generateParenthesis_core(n, n, "", result)
        return result

    def generateParenthesis_core(self, left_rest: int, right_rest: int, mid_str: str, result: List[str]):
        if left_rest == 0 and right_rest == 0:
            result.append(mid_str)
            return

        if 0 < left_rest <= right_rest:
            self.generateParenthesis_core(left_rest-1, right_rest, mid_str + '(', result)

        if right_rest > 0 and right_rest > left_rest:
            self.generateParenthesis_core(left_rest, right_rest-1, mid_str + ')', result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
    print(solution.generateParenthesis(1))
