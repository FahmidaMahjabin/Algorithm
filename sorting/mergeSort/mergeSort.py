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
        return merge(unsortedList, lower, mid, upper)
    else:
        return unsortedList

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
# step1:lower to mid value niye ekta new list banabo 
# step2:initialize i = 0 where i is the position of element in the new list that is not sorted yet 
# step3:initialize j = mid+1 where j is the position that is not sorted yet and range (mid+1 to upper)
# step4:compare ith and jth element :
#     step4.1:ith choto hole insert that element in unsortedList and increment i 
#     step4.2:else jth choto hole insert that element in unsortedList and increment j
# step5:kono ekta list er element shesh hoye gele baki list er ja element thakbe shob add korbo
# step6:return unsortedList
def merge(unsortedList, lower, mid, upper):
    leftList = unsortedList[lower:mid+1]
    i = 0
    j = mid + 1
    k = lower
    while i < len(leftList) and j <= upper:
        if leftList[i] < unsortedList[j]:
            unsortedList[k] = leftList[i]
            i += 1
            
        else:
            unsortedList[k] = unsortedList[j]
            j += 1
        k += 1
    while i < len(leftList):
        unsortedList[k] = leftList[i]
        i += 1
        k += 1
    while j <= upper:
        unsortedList[k] = unsortedList[j]
        j += 1
        k += 1
    return unsortedList

print("merge of 1 item", mergeSort([10], 0, 0))

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

print("name of mergeSort:",__name__)
if __name__ == "__main__":
    merge([12, 13, 100, -1, 2, 5], 0, 2, 5)
    print("merge executes")