# 52. N 皇后 II
# 困难
#
# 相关标签
# 相关企业
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
#
#
#
# 示例 1：
#
#
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 示例 2：
#
# 输入：n = 1
# 输出：1
#
#
# 提示：
#
# 1 <= n <= 9

from typing import List
class Solution:
    result = 0
    step_plans = [[-1, 0], [-1, -1], [-1, 1]]


    def totalNQueens(self, n: int) -> int:
        self.result = 0
        queen_metrix = [[False for _ in range(n)] for _ in range(n)]
        self.totalNQueens_core(queen_metrix, 0, n)
        return self.result


    def totalNQueens_core(self, queen_metrix: List[List[bool]], i: int, n:int) -> int:
        if i == n:
            self.result += 1
            return
        for j in range(n):
            queen_metrix[i][j] = True
            # 验证是否会互相攻击,如果不会则继续放置下一层的皇后
            if self.validQueenMetrix(queen_metrix, i, j):
                self.totalNQueens_core(queen_metrix, i+1, n)
            queen_metrix[i][j] = False

    def validQueenMetrix(self, queen_metrix: List[List[bool]], i: int, j:int) -> bool:
        for step_plan in self.step_plans:
            ni = i + step_plan[0]
            nj = j + step_plan[1]
            while 0 <= ni < len(queen_metrix) and 0 <= nj < len(queen_metrix):
                if queen_metrix[ni][nj]:
                    return False
                ni = ni + step_plan[0]
                nj = nj + step_plan[1]
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.totalNQueens(4))
    print(solution.totalNQueens(1))