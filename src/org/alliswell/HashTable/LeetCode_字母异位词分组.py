# 49. 字母异位词分组
# 中等
#
# 相关标签
# 相关企业
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
#
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。
#
#
#
# 示例 1:
#
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 示例 2:
#
# 输入: strs = [""]
# 输出: [[""]]
# 示例 3:
#
# 输入: strs = ["a"]
# 输出: [["a"]]
#
#
# 提示：
#
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] 仅包含小写字母

from typing import List
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         result = []
#         feature_arr = []
#         for str in strs:
#             current_feature = [0] * 26
#             for c in str:
#                 current_feature[ord(c) - 97] += 1
#             exist = False
#             for idx in range(len(feature_arr)):
#                 feature = feature_arr[idx]
#                 if feature == current_feature:
#                     group = result[idx]
#                     group.append(str)
#                     exist = True
#                     break
#             if not exist:
#                 result.append([str])
#                 feature_arr.append(current_feature)
#         return result


import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)

        return list(mp.values())


if __name__ == '__main__':
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(solution.groupAnagrams(strs))