# 如果 a+b+c = 1000，并且 a^2 + b^2 = c^2。求a,b,c可能的组合
'''
    a,b,c三个数的取值范围：0-1000
'''
# import time

# start_time = time.time()

# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c==1000 and a**2+b**2==c**2:
#                 print("a,b,c:%d,%d,%d"%(a,b,c))

# end_time = time.time()

# print("运行的时间是:%f"%(end_time-start_time))

'''
a,b,c:0,500,500
a,b,c:200,375,425
a,b,c:375,200,425
a,b,c:500,0,500
运行的时间是:153.769141
'''

# import time

# start_time = time.time()

# for a in range(0,1001):  
#     for b in range(0,1001):   
#         c = 1000-a-b
#         if a**2 + b**2 == c**2: 
#             print("a,b,c:%d,%d,%d"%(a,b,c))

# end_time = time.time()

# print("运行的时间是:%f"%(end_time-start_time))



'''
    时间复杂度
    时间复杂度的表示法：大O记法
    O(n^3)  O(n^2)
    时间复杂度分类
    关注：最坏时间复杂度
'''

'''
    练习：计算前n个数的和
'''
# import time

# def sum_of_n(n):
#     start_time = time.time()
#     the_sum = 0
#     for i in range(1,n+1):
#         the_sum = the_sum + i
#     end_time = time.time()
#     return the_sum,end_time-start_time


import time

def sum_of_n(n):
    return (n*(n+1)/2)

start_time = time.time()
print(sum_of_n(1000000000))
end_time = time.time()

print(end_time - start_time)



