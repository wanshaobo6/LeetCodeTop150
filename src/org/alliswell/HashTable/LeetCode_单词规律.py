# 290. 单词规律
# 简单
#
# 相关标签
# 相关企业
# 给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 s 中的每个非空单词之间存在着双向连接的对应规律。
#
#
#
# 示例1:
#
# 输入: pattern = "abba", s = "dog cat cat dog"
# 输出: true
# 示例 2:
#
# 输入:pattern = "abba", s = "dog cat cat fish"
# 输出: false
# 示例 3:
#
# 输入: pattern = "aaaa", s = "dog cat cat dog"
# 输出: false
#
#
# 提示:
#
# 1 <= pattern.length <= 300
# pattern 只包含小写英文字母
# 1 <= s.length <= 3000
# s 只包含小写英文字母和 ' '
# s 不包含 任何前导或尾随对空格
# s 中每个单词都被 单个空格 分隔

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split(" ")
        if len(pattern) != len(s_arr):
            return False
        first_arise_idx_arr = [-1] * 26
        cmp_arr = [-1] * len(pattern)
        for i in range(len(pattern)):
            idx = ord(pattern[i])-97
            first_arise_loc = first_arise_idx_arr[idx]
            # 如果之前没有出现过
            if first_arise_loc == -1:
               first_arise_idx_arr[idx] = i
            else:
               cmp_arr[i] = first_arise_loc

        print(first_arise_idx_arr)
        print(cmp_arr)

        for i in range(len(cmp_arr)):
            if cmp_arr[i] != -1:
                continue
            for j in range(i+1, len(cmp_arr)):
                if cmp_arr[j] != -1:
                    continue
                if s_arr[i] == s_arr[j]:
                    return False

        for i in range(len(s_arr)):
            if cmp_arr[i] == -1 or s_arr[i] == s_arr[cmp_arr[i]]:
                continue
            else:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.wordPattern("abba", "dog cat cat dog"))