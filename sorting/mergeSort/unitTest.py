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

# function = test for mergeSort
# testCases:1)no element 
# 2)1 element, 
# 3)large sample1
# 4)medium sample 
list1 = [3, 2]
list2 = [3, 2]
if list1 == list2:
    print("list1 and list2 equal")
def testMergeSort():
    testCases = [
        {"testName":"one element", "input": [[3],0,0], "expected":[3]},
        {"testName":"no element", "input": [[],0, 0], "expected": []},
        {"testName":"large elements", "input": [[20, 2, 10,-10, 500, 3, 4 ],0, 6], "expected": [-10, 2, 3, 4, 10, 20, 500]},
        {"testName":"sorted", "input": [[-8, 3, 4, 10, 20],0, 4], "expected": [-8, 3, 4, 10, 20]},
        {"testName":"reverse order", "input": [[600, 10, 3, -1],0, 3], "expected": [-1, 3, 10, 600]}
    ]
    
    for case in testCases:
        print(case["input"][0])
        assert mergeSort(case["input"][0], case["input"][1], case["input"][2] ) == case["expected"], case["testName"]

testMergeSort()



