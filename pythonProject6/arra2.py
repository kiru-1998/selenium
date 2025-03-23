# from array import *
#
# arr = array('i',[1,2,3,4,5])
# arr1=arr.remove(3)
# print(arr)
#
# from array import *
#
# arr = array('i',[1,2,3,4,5])
# arr1=arr.remove(3)
# print(arr)

from array import *

x = list(range(0,100,3))
arr = array('i',x)
arr1=arr[0:]
arr2 = arr[10::-20]
print(arr2)
print(arr1)