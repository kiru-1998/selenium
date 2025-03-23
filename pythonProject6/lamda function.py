# def add(x,y):
#     c=x+y
#     print(c)
# (add(10,2))
from functools import reduce

# lamda function compare to def function
# # f= lambda a,b:a+b
# # result=f(5,6)
# # print(result)
#
# f=lambda a,b:a*b
# result=f(10,5)
# print(result)

# n=[1,2,3,4,5,6,7,8]
# def even(n):
#     for i in n:
#         i+=1
#         if i%2==0:
#             print(i)
#
# even(n)


# nums=[1,2,3,4,5,6,7,8]
#
# even = list(filter(lambda n:n%2==0,nums))
#
# print(even)
# add = list(map(lambda n:n*2,nums))
# print(add)
# sum=reduce









# n = [1,2,3,4,5,6,7,8,9]
#
# def even(n):
#     for i in n:
#         if i%2==0:
#             print(i)
# even(n)


# nums=[2,3,4,6,8,7,9]

# f=lambda n:n*2
# result=f(3)
# print
# def even(n):
#     return n%2==0

nums=[2,3,4,6,8,7,9]

even =list(filter(lambda n:n%2==0,nums))
double= list(map(lambda n:n*2,even))
print(even)
print(double)

