import unittest
# function = quick sort 
# input = list of numbers, lowerBound(lb), upperBound(ub)
# output = same list in a sorted way 
# step1:list e jodi 1 er beshi element thake tahole , partition korbo 
# step2:pivot er cheye choto element niye partition 1 and apply quickSort on that part as long as there is one element
# step2:pivot er cheye boro element niye partition 2 and apply quickSort on partition2 as long as there is one element

def quickSort(list, lb, ub):
    
    if lb < ub:
        pivot = partition(list, lb, ub)
        quickSort(list, lb, pivot-1)
        quickSort(list, pivot+1, ub)
    return list

# function = partition (ekta list k pivot element er position e dui vag korte hobe and return that pivot element position)
# input = list of numbers, lowerBound, upperBound 
# outPut = pivot position 
# step1:list er last element k pivot element dhori 
# step2:let i = -1 where i represents the position of last smaller element than the pivot 
# step3:let j = lb where j represents the comparing element woth the pivot 
# step4: compare jth element with the pivot:
#     step4.1:jodi jth element <= pivot then oi element ta pivot er left e boshbe 
#     step4.2:i increment korbo and ith and jth element swap korbo 
# step5:last e ith position porjonto shob pivot er choro element bosheche, i+1 position e pivot 

def partition(list, lb, ub):
    pivot = list[ub]
    i = lb-1
    for j in range(lb, ub):
        if list[j] <= pivot:
            i += 1
            swap(list, i, j)
    swap(list, i+1, ub)
    return i+1

def swap(list, i, j):
    temporary = list[i]
    list[i] = list[j]
    list[j] = temporary
if __name__ == "__main__":
    list1 = [4, 5, 3, 2]
    assert quickSort(list1, 0, 3) == [2, 3, 4, 5]
    list2= [10, 7, 5, 2]
    print(quickSort(list2, 0, 3))
    assert quickSort(list2, 0, 3) == [2, 5, 7, 10]
    list3 = [10, 8, -2, 3, 16, 100]
    assert quickSort(list3, 0, 5) == [-2, 3, 8, 10, 16, 100]
    list4 = []
    assert quickSort(list4, 0, 0) == []
