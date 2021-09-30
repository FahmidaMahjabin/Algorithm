# function = selection Sort
# input = unsortedList
# output = sortedList
# step1:initialize i = 0 where i is the sortedElement position
# step2:smallest element ber korbo unsorted part theke 
# step3:smallest element ith position er element er sathe swap korbo
# step4:return updated List

def selectionSort(unsortedList):
    for i in range(len(unsortedList)):
        smallestithIndex = findIndexOfSmallest(unsortedList, i)
        temporary = unsortedList[i]
        unsortedList[i] = unsortedList[smallestithIndex]
        unsortedList[smallestithIndex] = temporary
    return unsortedList
        
    

# function = findSmallestNumber
# input = list, position i
# output = smallestNumber er index
# step1:list er i position er element k smallest dhore nibo 
# step2:compare that smallestelement with the current element 
# step3:if current element is smaller than the smallest then save the current element as smallest
# step4:do the same thing from step2 for all the elements 
# step5:return smallest er index
def findIndexOfSmallest(listOfNumber, i):
    smallest = listOfNumber[i]
    indexOfSmallest = i
    for index in range(i, len(listOfNumber)):
        if smallest > listOfNumber[index]:
            smallest = listOfNumber[index]
            indexOfSmallest = index
    return indexOfSmallest
listOfNumber = [10, -8, 12, 4, 3, 30]
print(selectionSort(listOfNumber))