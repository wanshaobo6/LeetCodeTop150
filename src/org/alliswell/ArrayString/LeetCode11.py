# 274. H 指数
# 中等
#
# 相关标签
# 相关企业
#
# 提示
# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。
#
# 根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，并且 至少 有 h 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个。
#
#
#
# 示例 1：
#
# 输入：citations = [3,0,6,1,5]
# 输出：3
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
# 由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
# 示例 2：
#
# 输入：citations = [1,3,1]
# 输出：1
#
#
# 提示：
#
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000


from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        list.sort(citations)
        h = 0
        arr_len = len(citations)
        for idx in range(0, arr_len):
            ch = min(arr_len - idx, citations[idx])
            if ch > h:
                h = ch
            if h >= arr_len -1 - idx:
                break
        return h


if __name__ == '__main__':
    # nums1: List[int] = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    nums1: List[int] = [1,3,1,3,4]
    solution = Solution()
    print(solution.hIndex(nums1))