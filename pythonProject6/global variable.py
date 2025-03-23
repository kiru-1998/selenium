
#scenario1
# a=10
# def something():
#     a=15
#
#     print('like',a)
# something()
# print('this',a)

#a=10
# def something():
#
#     print('fun', a)
#
# something()
# print(a)

# a=10
# def something():
#     global a
#     a=15
#     print('fun', a)
#
# something()
# print(a)

# a=10
# print(id(a))
# def something():
#     a=9
#     x=globals()[a]
#     print(id(a))
#     b=10
#     print('fun', a)
#
# something()
# print(a)

# a=10
# print(id(a))
# def something():
#     a=9
#     x=globals()['a']
#     print(id(x))
#     print(a)
#
# something()
# print(a)

def count(lst):

    even=0
    odd=0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd
lst = [1,2,3,4,5,6,7,8,9,10]

even,odd = count(lst)

print(count(lst))


















