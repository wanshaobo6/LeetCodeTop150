# 212. 单词搜索 II
# 困难
# 相关标签
# 相关企业
# 提示
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
#
# 单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
#
#
# 示例 1：
#
#
# 输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
# 示例 2：
#
#
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#
#
# 提示：
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] 是一个小写英文字母
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同

class TrieNode:
    def __init__(self):
        self.s = None
        self.tns = [None] * 26

    def insert(self, s:str) -> None:
        p = self
        for i in range(len(s)):
            u = ord(s[i]) - ord('a')
            if not p.tns[u]:
                p.tns[u] = TrieNode()
            p = p.tns[u]
        p.s = s


from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self._board = board
        self.m, self.n = len(board), len(board[0])
        self.root = TrieNode()
        self.dirs = [[1,0], [-1, 0], [0, 1], [0, -1]]
        self.vis = [[False for _ in range(15)] for _ in range(15)]
        self.ans = set()
        for word in words:
            self.root.insert(word)
        for i in range(self.m):
            for j in range(self.n):
                u = ord(board[i][j]) - ord('a')
                if self.root.tns[u]:
                    self.vis[i][j] = True
                    self.dfs(i, j, self.root.tns[u])
                    self.vis[i][j] = False
        return list(self.ans)
    def dfs(self, i: int, j: int, node:TrieNode):
        if node.s:
            self.ans.add(node.s)
        for d in self.dirs:
            dx, dy = i+d[0], j+d[1]
            if dx < 0 or dx >= self.m or dy < 0 or dy >= self.n:
                continue
            if self.vis[dx][dy]:
                continue
            u = ord(self._board[dx][dy]) - ord('a')
            if node.tns[u]:
                self.vis[dx][dy] = True
                self.dfs(dx, dy, node.tns[u])
                self.vis[dx][dy] = False


if __name__ == '__main__':
    solution = Solution()
    print(solution.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]))
    print(solution.findWords([["a","b"],["c","d"]], ["abdc"]))
    # trieNode = TrieNode()
    # trieNode.insert("abc")
    # trieNode.insert("ddd")
    # print(trieNode)