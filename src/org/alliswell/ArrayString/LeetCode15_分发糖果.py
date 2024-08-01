#TODO看题解
# 135. 分发糖果
# 困难
#
# 相关标签
# 相关企业
# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
#
# 你需要按照以下要求，给这些孩子分发糖果：
#
# 每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。
#
#
#
# 示例 1：
#
# 输入：ratings = [1,0,2]
# 输出：5
# 解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
# 示例 2：
#
# 输入：ratings = [1,2,2]
# 输出：4
# 解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
# 第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
#
#
# 提示：
#
# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 104

from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        candy_arr = [1] * length
        for idx in range(1, length):
            rating_diff = ratings[idx] - ratings[idx-1]
            if rating_diff > 0:
                candy_arr[idx] = candy_arr[idx-1] + 1
            elif rating_diff < 0:
                for pre_idx in range(idx-1, -1, -1):
                    cur_idx = pre_idx + 1
                    if ratings[pre_idx] > ratings[cur_idx] and candy_arr[pre_idx] == candy_arr[cur_idx]:
                        candy_arr[pre_idx] += 1
                    else:
                        break
        return sum(candy_arr)


if __name__ == '__main__':
    # ratings: List[int] = [1,0,2]
    ratings: List[int] = [3,4,7,7,3]
    solution = Solution()
    print(solution.candy(ratings))