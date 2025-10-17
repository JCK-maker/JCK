# n = int(input("n = "))
# m = int(input("m = "))
# s = n
# x = n
# for i in range(1 , m):
#     x = (s * 10) + (n * i)
#     s = n + x
# print("s =" , s)
'''
a = int(input("a = "))
n = int(input("n = "))
s = a
t = a
for i in range(1 , n) :
    t = t * 10 + a
    s = s + t
print(s)
'''

'''
    任务1：计算n!
    任务2：计算1! + 2! + ... + n!
'''
# n = int(input("n = "))
# s = 1
# x = 1
# for i in range(2 , n + 1):
#     # i = i + 1
#     s = s * i
#     x = x + s
# print("n! =" , s)
# print("1! + 2! + ... +" , n , "! =" , x)

'''
    [9,3,1,2,4,5,6,4,3,8,7,9,3,0,3,4,1,5,6,3,7,0,2,4,8,4,5,6,8,1,8,5,3,5,8,1,9]
    统计每个数字出现的次数
'''
a = [9,3,1,2,4,5,6,4,3,8,7,9,3,0,3,4,1,5,6,3,7,0,2,4,8,4,5,6,8,1,8,5,3,5,8,1,9]

def PX(a):
    n = len(a)
    for i in range(0, 10):
        for PX in range(n):
            for j in range(n - PX - 1):


                if a[j] == i:
                    m = 0
                    m = m + 1
            print(i , "出现", m ,"次")

PX(a)
