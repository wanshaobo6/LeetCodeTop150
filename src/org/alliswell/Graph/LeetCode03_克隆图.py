# 133. 克隆图
# 中等
#
# 相关标签
# 相关企业
# 给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。
#
# 图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。
#
# class Node {
# public int val;
# public List<Node> neighbors;
# }
#
#
# 测试用例格式：
#
# 简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。
#
# 邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。
#
# 给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。
#
#
#
# 示例 1：
#
#
#
# 输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
# 输出：[[2,4],[1,3],[2,4],[1,3]]
# 解释：
# 图中有 4 个节点。
# 节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
# 节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
# 节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
# 节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
# 示例 2：
#
#
#
# 输入：adjList = [[]]
# 输出：[[]]
# 解释：输入包含一个空列表。该图仅仅只有一个值为 1 的节点，它没有任何邻居。
# 示例 3：
#
# 输入：adjList = []
# 输出：[]
# 解释：这个图是空的，它不含任何节点。
#
#
# 提示：
#
# 这张图中的节点数在 [0, 100] 之间。
# 1 <= Node.val <= 100
# 每个节点值 Node.val 都是唯一的，
# 图中没有重复的边，也没有自环。
# 图是连通图，你可以从给定节点访问到所有节点。
# 面试中遇到过这道题?
# 1/5

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# from typing import Optional
# import collections
# class Solution:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         if node is None:
#             return None
#         visited_set = set()
#         next_visit_queue = collections.deque()
#         next_visit_queue.append(node)
#
#         object_map = {}
#
#         while len(next_visit_queue) != 0:
#             n1 = next_visit_queue.pop()
#             if n1 in visited_set:
#                 continue
#             visited_set.add(n1)
#
#             # 对象池
#             clone_node = object_map.get(n1.val)
#             if clone_node is None:
#                 clone_node = Node(n1.val, neighbors=[])
#                 object_map[n1.val] = clone_node
#
#             for neighbor in n1.neighbors:
#                 next_visit_queue.append(neighbor)
#                 clone_neighbor = object_map.get(neighbor.val)
#                 if clone_neighbor is None:
#                     clone_neighbor = Node(val=neighbor.val)
#                     object_map[neighbor.val] = clone_neighbor
#                 clone_node.neighbors.append(clone_neighbor)
#         return object_map.get(node.val)

from typing import Optional
import collections
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        next_visit_queue = collections.deque([node])
        visited_map = {node: Node(val=node.val, neighbors=[])}

        while next_visit_queue:
            n = next_visit_queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited_map:
                    visited_map[neighbor] = Node(val=neighbor.val, neighbors=[])
                    next_visit_queue.append(neighbor)
                visited_map[n].neighbors.append(visited_map[neighbor])
        return visited_map.get(node)


if __name__ == '__main__':
    head = Node(val=1)
    head.neighbors=[Node(val=2, neighbors=[head]), Node(val=3, neighbors=[head])]
    solution = Solution()
    print(solution.cloneGraph(head))
