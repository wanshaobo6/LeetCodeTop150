# 146. LRU 缓存
# 中等
#
# 相关标签
# 相关企业
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
#
#
#
# 示例：
#
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#
#
# 提示：
#
# 1 <= capacity <= 3000
# 0 <= key <= 10000
# 0 <= value <= 10^5
# 最多调用 2 * 10^5 次 get 和 put
from typing import Optional
class Entry:
    def __init__(self, key:Optional[int], value:Optional[int], pre:Optional['Entry'], next:Optional['Entry']):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.head = Entry(key=None, value=None, pre=None, next=None)
        self.tail = Entry(key=None, value=None, pre=None, next=None)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        entry = self.map.get(key)
        # 值不存在
        if not entry:
            return -1
        if self.size > 1:
            self.move_node_2_tail(entry)
        return entry.value

    def put(self, key: int, value: int) -> None:
        entry = self.map.get(key)
        if entry:
            entry.value = value
            self.move_node_2_tail(entry)
        else:
            entry = Entry(key=key, value=value, pre=self.tail.pre, next=self.tail)
            self.tail.pre.next = entry
            self.tail.pre = entry
            self.map[key] = entry
            if self.size < self.capacity:
                self.size += 1
            else:
                deprecated = self.remove_oldest_ele()
                del self.map[deprecated.key]

    def move_node_2_tail(self, entry:Optional['Entry']):
        entry.pre.next = entry.next
        entry.next.pre = entry.pre
        entry.pre = self.tail.pre
        entry.next = self.tail
        self.tail.pre.next = entry
        self.tail.pre = entry

    def remove_oldest_ele(self) -> Optional['Entry']:
        deprecated_ele = self.head.next
        self.head.next = deprecated_ele.next
        deprecated_ele.next.pre = self.head
        deprecated_ele.next = None
        deprecated_ele.pre = None
        return deprecated_ele

if __name__ == '__main__':
    # obj = LRUCache(2)
    # obj.put(1, 1)
    # obj.put(2, 2)
    # print(obj.get(1))
    # obj.put(3, 3)
    # print(obj.get(2))
    # obj.put(4, 4)
    # print(obj.get(1))
    # print(obj.get(3))
    # print(obj.get(4))
    obj = LRUCache(1)
    obj.put(2, 1)
    print(obj.get(2))