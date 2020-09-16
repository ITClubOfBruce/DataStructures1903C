'''
    python 中的列表
    my_list = [1,2,3,4,5,6,7]
'''

'''
   1. 列表的创建
'''
import timeit
from timeit import Timer

def test1():
    my_list = []
    for i in range(1000):
        my_list = my_list + [i]

def test2():
    my_list = []
    for i in range(1000):
        my_list.append(i)

def test3():
    my_list = [i for i in range(0,1000)]

def test4():
    my_list = list(range(1000))

t1 = Timer("test1()","from __main__ import test1")
print("连接",t1.timeit(number=1000),"秒")

t2 = Timer("test2()","from __main__ import test2")
print("append",t2.timeit(number=1000),"秒")

t3 = Timer("test3()","from __main__ import test3")
print("列表推导式",t3.timeit(number=1000),"秒")

t4 = Timer("test4()","from __main__ import test4")
print("list range",t4.timeit(number=1000),"秒")



'''
    2. 测试pop()(从列表最后删除一个元素)和pop(0)（删除列表第一个元素）
    pop()  O(1)
    pop(i)  O(n)
'''
l = list(range(2000000))
pop_zero = Timer('l.pop(0)',"from __main__ import l")
print("pop_zero",pop_zero.timeit(number=1000),"秒")

pop_end = Timer("l.pop()","from __main__ import l")
print("pop_end",pop_end.timeit(number=1000),"秒")



'''
    insert(i,item)  O(n)
    reverse     O(n)
    sort()      O(nlogn)
'''
l = list(range(2000000))
l_insert = Timer("l.insert(10,100)","from __main__ import l")
print("l_insert",l_insert.timeit(number=1000),"秒")




'''
    验证列表索引操作是O(1),   index
    将时间复杂度改成O(n)
    a = [1,2,3,4,5]
    a.index("3",1,3)
'''

# a = ['a','b','c','d','e','f']
# print(a.index("b",0,10))







