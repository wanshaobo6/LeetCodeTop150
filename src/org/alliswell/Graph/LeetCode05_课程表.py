# 207. 课程表
# 中等
# 相关标签
# 相关企业
# 提示
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
# 示例 2：
#
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
#
#
# 提示：
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# prerequisites[i] 中的所有课程对 互不相同

from typing import List
class NextNode:
    def __init__(self):
        self.waiting_task_num = 0
        self.is_run_finished = False
        self.next_tasks = []

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 初始化邻接表
        courses = [NextNode() for _ in range(numCourses)]
        for prerequisite in prerequisites:
            after_task = prerequisite[0]
            before_task = prerequisite[1]
            courses[after_task].waiting_task_num += 1
            courses[before_task].next_tasks.append(after_task)

        for i in range(numCourses):
            # 选择一个没有前置课程的课
            run_idx = -1
            for i in range(len(courses)):
                course = courses[i]
                if course.waiting_task_num == 0 and not course.is_run_finished:
                    run_idx = i
                    break
            # 如果没有可以选择的课
            if run_idx == -1:
                return False
            select_course = courses[run_idx]
            for next_task_idx in select_course.next_tasks:
                courses[next_task_idx].waiting_task_num -= 1
            select_course.is_run_finished = True
        return True

if __name__ == '__main__':
    solution = Solution()
    print(solution.canFinish(4, [[1,0],[2,0],[2,0],[3,1],[3,2]]))