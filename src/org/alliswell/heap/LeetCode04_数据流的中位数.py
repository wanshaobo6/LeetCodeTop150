# 295. 数据流的中位数
#
# 相关标签
# 相关企业
# 中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。
#
# 例如 arr = [2,3,4] 的中位数是 3 。
# 例如 arr = [2,3] 的中位数是 (2 + 3) / 2 = 2.5 。
# 实现 MedianFinder 类:
#
# MedianFinder() 初始化 MedianFinder 对象。
#
# void addNum(int num) 将数据流中的整数 num 添加到数据结构中。
#
# double findMedian() 返回到目前为止所有元素的中位数。与实际答案相差 10-5 以内的答案将被接受。
#
# 示例 1：
#
# 输入
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# 输出
# [null, null, null, 1.5, null, 2.0]
#
# 解释
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // 返回 1.5 ((1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
# 提示:
#
# -105 <= num <= 105
# 在调用 findMedian 之前，数据结构中至少有一个元素
# 最多 5 * 104 次调用 addNum 和 findMedian

import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.size = 0

    def addNum(self, num: int) -> None:
        size = self.size
        if size % 2 == 0:
            replaced = heapq.heappushpop(self.min_heap, num)
            heapq.heappush(self.max_heap, -replaced)
        else:
            replaced = -heapq.heappushpop(self.max_heap, -num)
            heapq.heappush(self.min_heap, replaced)
        self.size += 1

    def findMedian(self) -> float:
        size = self.size
        if size % 2 == 0:
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return - self.max_heap[0]

if __name__ == '__main__':
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())
    medianFinder.addNum(4)
    print(medianFinder.findMedian())
    medianFinder.addNum(5)
    print(medianFinder.findMedian())

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

