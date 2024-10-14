# 210. 课程表 II
# 中等
# 相关标签
# 相关企业
# 提示
# 现在你总共有 numCourses 门课需要选，记为 0 到 numCourses - 1。给你一个数组 prerequisites ，其中 prerequisites[i] = [ai, bi] ，表示在选修课程 ai 前 必须 先选修 bi 。
#
# 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示：[0,1] 。
# 返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 任意一种 就可以了。如果不可能完成所有课程，返回 一个空数组 。
#
#
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：[0,1]
# 解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。
# 示例 2：
#
# 输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# 输出：[0,2,1,3]
# 解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
# 因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
# 示例 3：
#
# 输入：numCourses = 1, prerequisites = []
# 输出：[0]
#
#
# 提示：
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# 所有[ai, bi] 互不相同

from typing import List

class NextNode:
    def __init__(self):
        self.waiting_task_num = 0
        self.next_tasks = []

import queue
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 初始化邻接表
        courses = [NextNode() for _ in range(numCourses)]
        for prerequisite in prerequisites:
            after_task = prerequisite[0]
            before_task = prerequisite[1]
            courses[after_task].waiting_task_num += 1
            courses[before_task].next_tasks.append(after_task)

        result = []
        # while len(result) < numCourses:
        #     # 选择一个没有前置课程的课
        #     run_idx = -1
        #     for i in range(len(courses)):
        #         course = courses[i]
        #         if course.waiting_task_num == 0 and not course.is_run_finished:
        #             run_idx = i
        #             break
        #     # 如果没有可以选择的课
        #     if run_idx == -1:
        #         return []
        #     result.append(run_idx)
        #     select_course = courses[run_idx]
        #     for next_task_idx in select_course.next_tasks:
        #         courses[next_task_idx].waiting_task_num -= 1
        #     select_course.is_run_finished = True

        # 可使用队列来降低时间复杂度
        q = queue.Queue()
        # 1.所有度为0的课程进入队列
        for i in range(numCourses):
            course = courses[i]
            if course.waiting_task_num == 0:
                q.put(i)
        # 2.消费队列中的课程
        while not q.empty():
            run_idx = q.get()
            result.append(run_idx)
            for next_task_idx in courses[run_idx].next_tasks:
                courses[next_task_idx].waiting_task_num -= 1
                if courses[next_task_idx].waiting_task_num == 0:
                    q.put(next_task_idx)
        return result if len(result) == numCourses else []



if __name__ == '__main__':
    solution = Solution()
    print(solution.findOrder(4, [[1,0],[2,0],[2,0],[3,1],[3,2]]))