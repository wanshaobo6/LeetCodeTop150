# 79. 单词搜索
# 中等
#
# 相关标签
# 相关企业
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例 1：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
# 示例 2：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# 输出：true
# 示例 3：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# 输出：false
#
#
# 提示：
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board 和 word 仅由大小写英文字母组成
#
#
# 进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？


from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.visit(board, i, j, word, 0, visited):
                    return True
        return False

    def visit(self, board: List[List[str]], i:int, j:int, word: str, p:int, visited: List[List[bool]]) -> bool:
        if p >= len(word):
            return True
        elif i <0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
            return False
        elif word[p] == board[i][j]:
            visited[i][j] = True
            result = self.visit(board, i-1, j, word, p+1, visited) or self.visit(board, i+1, j, word, p+1, visited) or self.visit(board, i, j-1, word, p+1, visited) or self.visit(board, i, j+1, word, p+1, visited)
            visited[i][j] = False
            return result
        else:
            return False

if __name__ == '__main__':
    solution = Solution()
    print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
    print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
    print(solution.exist([["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]], "aaaaaaaaaaaa"))