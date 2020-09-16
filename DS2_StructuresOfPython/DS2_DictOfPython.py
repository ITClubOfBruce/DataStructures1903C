'''
    2. 字典 Dict
    除了复制和迭代是O(n);
    in，删除，访问 O(1)
    字典的包含关系始终比列表快

    info={}
    添加 info['id'] = 1000
    修改 info['id'] = 3000
    删除 del info['id']   或者删除整个字典 del info
    清空 info.clear()
    包含,遍历：for key in info.keys()
          for value in info.values()
          for item in info.items()
          for key,value in info.items()  
'''
import timeit
from timeit import Timer

info={"name":"Bruce","age":"30"}
def test():
    for i in range(1001):
        for key,value in info.items():
            pass

t = Timer("test()","from __main__ import test")
print("test dict",t.timeit(number=1000),"秒")


def test1():
    for i in range(1001):
        d = dict()

t1 = Timer("test1()","from __main__ import test1")
print("dict()生成",t1.timeit(number=1000),"秒")