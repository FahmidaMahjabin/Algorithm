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



# function = make a list from another list 
# input = list 
# step1:list theke ekta kore element 

# print("using buildin function:", list2)
# print("using mergeSort:", mergeSort(list1,0,len(list1)-1))
# testMergeSort(list1)

# test case:1 (no element)
# def testMSforNoelement(list1):


# 1.obj1.sort():
#     self = obj1
#     ......
#     value of the expression sorted object ['BMW', 'Ford', 'Volvo']

# 1.function = testMergeSort 
# input = unsorted list 
# output = none 
# step1:lower, mid, upper ber korbo 
# step2:merge function er result and mergeTwoList er result compare kore dekhbo
def testMerge(list):
    upper = len(list) - 1
    mid = (0+upper) // 2
    sortedList1 = merge(list, 0, mid, upper)
    print("result from merge function:", sortedList1)
    sortedList2 = mergeTwoList(list, 0, mid , upper)
    print("result from mergeTwoList:", sortedList2)
    assert sortedList1 == sortedList2
list1 = [-3, -10, 100, 2,-1]
print(testMerge(list1))   

# test for merge
list1 =  [-8, 3, 4, 12, 30, 3]
assert merge([-8,3],0, 1, 1) == [-8, 3]
assert merge([-8,3],0, 1, 1) == [-8, 3]
assert merge([-8,3, 4],0, 1, 2) == [-8, 3, 4]
assert merge([-8, 3, 4, 12, 30, 3],3, 4, 4) == [-8, 3, 4, 12, 30, 3]
assert merge([-8, 3, 4, 12, 30, 3],3, 4, 5) == [-8, 3, 4, 3, 12, 30]
assert merge([],0, 0, 0) == []
assert merge([-10, -3, 100, -1, 2, 500], 0, 2, 5) == [-10, -3, -1, 2, 100, 500]
assert merge([12, 13, 100, -1, 2, 5], 0, 2, 5) == [-1, 2, 5, 12, 13, 100]
print("name from unitTest:",__name__)




