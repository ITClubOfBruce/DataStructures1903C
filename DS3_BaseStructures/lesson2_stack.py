'''
    什么是栈？
       栈（叠加栈）是一个项的有序集合。
       1. 添加项和移除项都在同一“端”。这一端通常被称为“顶”，另一端被称为“底”
       2. 栈的“底”是有标志性的，因为存储在栈中更靠近“底”的项就是栈中存储时间最长的项，
       3. 最新添加的项在移除项的时候也会被第一个移除
       4. 这种排序的原则称为LIFO法，也就是“后进先出”
    
    栈的抽象数据结构：
        Stack() 创建一个新的空栈，不需要参数，返回一个空栈
        push(item) 入栈，将新项添加到堆栈的顶部
        pop() 出栈    从栈顶删除项，不需要参数，返回被删除的项目，栈被修改
        peek() 返回栈顶的项，不删除它，不需要参数，堆栈不被修改
        isEmpty()  测试栈是否为空，不需要参数，返回布尔值
        size()  返回栈的项目数，不需要参数，返回一个整数
'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def isEmpty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)

s = Stack()
s.push(1)
s.push(2)
s.pop()
s.pop()
print(s.isEmpty())



items = [1,2,3,4,-5]
def getMin(items):
    return min(items)

print(getMin(items))