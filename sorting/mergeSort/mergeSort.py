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
print(mergeSort(list1, 0, 5))