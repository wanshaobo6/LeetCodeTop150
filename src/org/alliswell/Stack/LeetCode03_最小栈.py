# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#
# 实现 MinStack 类:
#
# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。
#
#
# 示例 1:
#
# 输入：
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
#
# 输出：
# [null,null,null,null,-3,null,0,-2]
#
# 解释：
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#
#
# 提示：
#
# -2^31 <= val <= 2^31 - 1
# pop、top 和 getMin 操作总是在 非空栈 上调用
# push, pop, top, and getMin最多被调用 3 * 10^4 次


class MinStack:

    def __init__(self):
        self.data_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.data_stack.append(val)
        if len(self.min_stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        top = None
        if len(self.data_stack) > 0:
            top = self.data_stack.pop()
        if len(self.min_stack) > 0 and top is not None and self.min_stack[-1] == top:
            self.min_stack.pop()

    def top(self) -> int:
        if len(self.data_stack) > 0:
            return self.data_stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    min_stack = MinStack()
    min_stack.push(2)
    min_stack.push(0)
    min_stack.push(3)
    min_stack.push(0)
    print(min_stack.getMin())
    print(min_stack.pop())
    print(min_stack.getMin())
    print(min_stack.pop())
    print(min_stack.getMin())
    print(min_stack.pop())
    print(min_stack.getMin())
