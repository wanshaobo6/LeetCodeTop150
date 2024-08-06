# 139. 单词拆分
# 中等
#
# 相关标签
# 相关企业
# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
#
# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。
#
#
#
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
# 注意，你可以重复使用字典中的单词。
# 示例 3：
#
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#
#
# 提示：
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s 和 wordDict[i] 仅由小写英文字母组成
# wordDict 中的所有字符串 互不相同

from typing import List
class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     return self.wordBreakCore(s, len(s)-1, wordDict)
    #
    # def wordBreakCore(self, s: str, s_loc: int, wordDict: List[str]) -> bool:
    #     if s_loc < 0:
    #         return True
    #
    #     result = False
    #     for word in wordDict:
    #         word_len = len(word)
    #         result = result or (self.str_match(s, s_loc-word_len+1, s_loc, word) and self.wordBreakCore(s, s_loc-word_len, wordDict))
    #         if result:
    #             break
    #     return result

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_len = len(s)
        dp_arr = [False] * s_len
        match_loc = 0
        while match_loc < s_len:
            for word in wordDict:
                word_len = len(word)
                if match_loc + word_len <= s_len and not dp_arr[match_loc + word_len - 1] and self.str_match(s, match_loc, match_loc+word_len-1, word):
                    dp_arr[match_loc + word_len - 1] = True
            while match_loc < s_len and not dp_arr[match_loc]:
                match_loc += 1
            match_loc += 1
        return dp_arr[s_len - 1]




    def str_match(self, s: str, s_start: int, s_end:int, word:str) -> bool:
        if s_start < 0 or s_end >= len(s) or s_start > s_end or len(word) != (s_end - s_start + 1):
            return False
        for idx in range(0, s_end-s_start+1):
            if s[s_start+idx] != word[idx]:
                return False
        return True

if __name__ == '__main__':
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]

    # s = "applepenapple"
    # wordDict = ["apple", "pen"]
    solution = Solution()
    print(solution.wordBreak(s, wordDict))