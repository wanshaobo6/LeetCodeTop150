# 72. 编辑距离
# 中等
#
# 相关标签
# 相关企业
# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
#
# 示例 1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2：
#
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#
# 提示：
#
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_len = len(word1)
        word2_len = len(word2)
        if word1_len == 0 or word2_len == 0:
            return word1_len if word2_len == 0 else word2_len
        dp2 = [[0 for _ in range(word1_len)] for _ in range(word2_len)]
        for i in range(word2_len):
            for j in range(word1_len):
                if i == 0 and j == 0:
                    dp2[i][j] = 0 if word1[j] == word2[i] else 1
                elif i == 0 or j == 0:
                    left_or_top = dp2[i-1][j] if i-1 >= 0 else dp2[i][j-1]
                    dp2[i][j] = max(i, j) if word1[j] == word2[i] else  left_or_top + 1
                elif word1[j] == word2[i]:
                    dp2[i][j] = dp2[i-1][j-1]
                else:
                    dp2[i][j] = min(dp2[i-1][j], dp2[i][j-1], dp2[i-1][j-1])+1
        return dp2[word2_len-1][word1_len-1]

if __name__ == '__main__':
    solution = Solution()
    # print(solution.minDistance("intention", "iat"))
    print(solution.minDistance("1", "2"))