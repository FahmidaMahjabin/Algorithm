

import unittest
# function = insertion sort
# input = list of number 
# output = sorted list 
# step1:initialize i = 1 where i is the unsorted element in the list
# step2:ekta kore ith element nibo and
#     step2.1:0 theke ith element er ag porjonto joto element ase tar sathe ith element er compare kore dekhbo j kono 
#     element ith er cheye boro kina 
#         step2.1.1:boro hole insertOneElement
#         step2.1.2:else: go to next element, increase i
# step3:return list

def insertionSort(list1):
    i = 1
    for i in range(len(list1)):
        for j in range(i):
            if list1[i] < list1[j]:
                insertOneElement(list1, i, j)
    return list1

# function = insertOneElement 
# input = list, small element er index(i), large element er Index(j)
# output = list 
# step1:ith element k ekta variable temporary te rakhbo
# step2:(i-1) theke j element porjonto ekta kore element tar porer place e boshabo
# step3:jth place khali hobe then temporary er value jth place e boshabo
# step4:return list
def insertOneElement(list, i, j):
    temporary = list[i]
    for index in range(i-1, j-1, -1):
        list[index+1] = list[index]
    list[j] = temporary
    return list

list1 = [5, 2, 3, 1, 4]
assert insertionSort(list1) == [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]
assert insertionSort(list2) == [1, 2, 3, 4, 5]
list3 = [20]
assert insertionSort(list3) == [20]
assert insertionSort([]) == []