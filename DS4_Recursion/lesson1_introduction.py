'''
    递归：递归是一种解决问题的方法。
    它把问题分解为越来越小的子问题，直到问题的规模小到可以被简单直接解决。
    特征：通常为了达到分解问题的效果 “ 递归过程要引入一个调用自身的函数 ”
    解决问题类型：
'''

'''
    使用递归，计算列表元素的和

def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum = the_sum + i
    return the_sum

print(list_sum([1,2,3,4,5]))
'''

'''
    禁止使用while或者for
    (((1+2)+3)+4)+5
    num_list[i]+num_list[i+1]
    list_sum(num_list) = first(num_list)+listSum(rest(num_list))

import time

num_list = [x for x in range(1,501)]

def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0]+list_sum(num_list[1:])

start_time = time.time()
for i in range(1001):
    list_sum(num_list)
end_time = time.time()

print(end_time-start_time)

'''



'''
    递归的三大定律：
        1. 递归算法必须有个结束条件
        2. 递归算法必须改变自己的状态并向基本结束条件演进
        3. 递归算法必须递归的调用自身
'''

'''
    计算某个数的阶乘   5! = 1*2*3*4*5
    0！= 1

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)


print(fact(1))

'''



'''
    将整数转换为任意进制表示的字符串形式
    十进制   二进制       八进制    十六进制
      7     00000111       7           7
     10     00001010      12           A

7/2   商3余1  3/2 商1余1  1/2 余1
7/8  7
7/16 7

'''

def to_str(n,base):
    convert_string = '0123456789ABCDEF'
    if n<base:
        return convert_string[n]
    else:
        return to_str(n//base,base)+convert_string[n%base]

print(to_str(10,16))



'''
    1. 写一个函数，接收一个字符串作为参数，并返回一个反向的新的字符串
    2. 使用递归判断回文字符串
'''


