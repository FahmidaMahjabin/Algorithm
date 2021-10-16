from mergeSort import *
import unittest
def sum(a, b):
    return a + b
def testForNoValue():
    assert sum(4, 2) == 6

testForNoValue()

def testMergeSort(list1):
    list2 = list1.copy()
    mergeSortResult = mergeSort(list1,0,len(list1)-1)
    print("after mergeSort list1:", list1)
    print("list2 before sort", list2)
    list2.sort()
    print("list2 after sort", list2)
    assert mergeSortResult == list2

list1 = [3, 10, 2]

# function = make a list from another list 
# input = list 
# step1:list theke ekta kore element 

# print("using buildin function:", list2)
# print("using mergeSort:", mergeSort(list1,0,len(list1)-1))
testMergeSort(list1)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
# print(cars)
list2 = list1 
list1.append(-4)
# print(list2)

# 1.obj1.sort():
#     self = obj1
#     ......
#     value of the expression sorted object ['BMW', 'Ford', 'Volvo']
