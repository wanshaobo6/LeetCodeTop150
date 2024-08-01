# 14. 最长公共前缀
# 简单
#
# 相关标签
# 相关企业
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
#
#
# 示例 1：
#
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 示例 2：
#
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
#
#
# 提示：
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] 仅由小写英文字母组成
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        j = 0
        strs_len = len(strs)
        while True:
            for i in range(strs_len):
                if len(strs[i]) <= j:
                    return strs[0][0:j]
                if i > 0 and strs[i][j] != strs[i-1][j]:
                    return strs[0][0:j]
            j += 1


if __name__ == '__main__':
    strs = ["flower","fl1","flight"]
    solution = Solution()
    res = solution.longestCommonPrefix(strs)
    print(solution.longestCommonPrefix(strs))