# TODO REVIEW
# 373. 查找和最小的 K 对数字
# 中等
#
# 相关标签
# 相关企业
# 给定两个以 非递减顺序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。
#
# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。
#
# 请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。
#
#
#
# 示例 1:
#
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 示例 2:
#
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
#
#
# 提示:
#
# 1 <= nums1.length, nums2.length <= 10^5
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1 和 nums2 均为 升序排列
# 1 <= k <= 10^4
# k <= nums1.length * nums2.length
import sys
from typing import List
import heapq

class Wrapper:
    def __init__(self, u:int, v:int):
        self.u = u
        self.v = v
        self.sum = u + v

    def __lt__(self, other):
        return self.sum < other.sum


# class Solution:
    # 超时答案
    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    #     hp = []
    #     res = []
    #
    #     i = 0
    #     while i < len(nums1):
    #         for j in range(len(nums2)):
    #             heapq.heappush(hp, [nums1[i]+nums2[j], nums1[i], nums2[j]])
    #         i += 1
    #         if i < len(nums1):
    #             threshold = nums1[i] + nums2[0]
    #         else:
    #             threshold = sys.maxsize
    #         while len(hp) != 0 and hp[0][0] <= threshold:
    #             item = heapq.heappop(hp)
    #             res.append([item[1], [item[2]]])
    #             k -= 1
    #             if k == 0:
    #                 return res
    #     return res
    #
    # 正确答案: https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/?envType=study-plan-v2&envId=top-interview-150
    class Solution:
        def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
            m, n = len(nums1), len(nums2)
            ans = []
            pq = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
            while pq and len(ans) < k:
                _, i, j = heappop(pq)
                ans.append([nums1[i], nums2[j]])
                if j + 1 < n:
                    heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
            return ans


if __name__ == '__main__':
    hp = []
    heapq.heappush(hp, [1, 2])
    heapq.heappush(hp, [5, 3])
    heapq.heappush(hp, [-5, -3])
    heapq.heappush(hp, [9995, 3])
    heapq.heappush(hp, [9995, -11111013])
    print(heapq.heappop(hp))
    print(heapq.heappop(hp))
    print(heapq.heappop(hp))
    print(heapq.heappop(hp))
    solution = Solution()
    # print(solution.kSmallestPairs([1,7,11], [2,4,6], 3))
    print(solution.kSmallestPairs([1,1,2], [1,2,3], 2))