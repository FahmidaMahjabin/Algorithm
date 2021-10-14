import mergeSort 
import unittest
def sum(a, b):
    return a + b
def testForNoValue():
    assert sum(4, 2) == 6

testForNoValue()

def testMergeSort(list):
    assert mergeSort([list],0,len(list)-1) == list.sort()

list = [3, 10, 2]
testMergeSort(list)