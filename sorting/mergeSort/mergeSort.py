# PseudoCode
# function = merge sort
# input = list of number , lower bound, upper bound
# step1: jodi list e 1 er cheye beshi character thake then list er mid ber korbo 
#     step1.1:list er lower to mid porjonto left portion er jonno merge sort korbo
#     step1.2:list er mid to upper right portion er jonno merge sort korbo
#     step1.3:left and right portion merge kore sortedList e rakhbo e rakhbo
#     step1.4:unsortedList e sorted portion update korbo

# step2:return unsortedList 

def mergeSort(unsortedList, lower, upper):
    
    if lower < upper:
        mid = (lower + upper) // 2;
        mergeSort(unsortedList, lower, mid)
        mergeSort(unsortedList, mid+1, upper)
        return mergeTwoList(unsortedList, lower, mid, upper)

# function = merge sort 
# input = list, lower, upper 
# output = sortedList 
# step1:jodi ekta element thake then return that element 
# step2:else:
#     step2.1:divide the list into middle 
#     step2.1:leftList hobe lower to mid porjonto, go to step1
#     step2.2:rightList hobe mid+1 to upper porjonto, go to step1
#     step2.3:left list and right list k merge korbo 

# function = merge (merge the two sorted List )
# input = lower, upper, mid and unsortedList 
# output = sortedList 
# step1:from lower to mid leftPart 
# step2:initialize i = 0(range of i is lower to mid) where i is the position of notAdded element of leftPartList
# step2:initialize j  = mid+1 (range of j is mid+1 to upper) where j is the position of notAdded element of rightPartList 
# step3:initialize k = 0(range of k is 0 to len of the list)
# step4:while i <= mid and j <= upper compare ith and jth element 
#     step4.1:insert the smallest element in the kth position of unsortedList and increase k and that i or j 
# step5:jodi leftPartList or rightPartList e kono element theke thake then shob element gulo insert korbo kth place e 
# step6:return unsortedList

def merge(unsortedList, lower, mid, upper):
    i = lower
    j = mid+1
    k = 0
    while i <= mid and j <= upper:
        if unsortedList[i] < unsortedList[j]:
            unsortedList[k] = unsortedList[i]
            i += 1
            k += 1
            
        else:
            unsortedList[k] = unsortedList[j]
            j += 1
            k += 1

    while i <= mid:
        unsortedList[k] = unsortedList[i]
        i += 1
        k += 1
    while j <= upper:
        unsortedList[k] = unsortedList[j]
        j += 1
        k += 1
    return unsortedList
list = [2, 3, 10, 1, 4, 9]
print(merge(list, 0, 2, 5))


# function = UpdateList(duita list deya thakbe, first list er kothay insert korte hobe tar index deya ase.First list k update korte hobe)
# function = updateList
# input = list1, list2, index
# output = list1
# step1:list2 theke ekta kore element niye list1 er input index e boshabo 
#     step1.1:index 1 increment korbo

def updateList(list1, list2, lowerIndex):
    for index in range(len(list2)):
        list1[lowerIndex] = list2[index]
        lowerIndex += 1
    return list1

# function = merge two sorted List
# input = unsortedList, lower, mid, upper
# step1: lower to mid k ekta list chinta korbo, and first position i = l dhorbo
# step2:mid to upper k arekta list dhorbo, first position j = m dhorbo 
# step3:jokhon i < m and j < u
#     step3:i and j element compare korbo:
#         step3.1:i choto hole sortedList e ith element add korbo and i increment korbo
#         step3.2:else j choto hole sortedList e jth element add korbo and j increment korbo
# step4:if i <= m then append all the elements upto m
# step5:if j <= u then append all the elements upto u
# step6:return sortedList

def mergeTwoList(unsortedList, lower, mid, upper):
    i = lower 
    j = mid+1
    sortedList = []
    while i <= mid and j <= upper:
        if unsortedList[i] <= unsortedList[j]:
            sortedList.append(unsortedList[i])
            i += 1
        else:
            sortedList.append(unsortedList[j])
            j += 1
    while i <= mid:
        sortedList.append(unsortedList[i])
        i += 1
    while j <= upper:
        sortedList.append(unsortedList[j])
        j += 1
    unsortedList = updateList(unsortedList, sortedList, lower)
    return unsortedList

list1 = [-8, 3, 4, 12, 30, 3]
# print(mergeSort(list1, 0, 5))