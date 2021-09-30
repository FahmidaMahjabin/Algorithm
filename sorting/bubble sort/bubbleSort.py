# PseudoCode
# function = bubble sort
# input = unsortedList
# output = sort in increasing order
# step1:list er first theke last porjonto ekta kore element nibo
#     step1.1:ei element er jonno ,0 index theke last theke oi index er ag porjonto
#         ekta kore index nibo
#         step1.1.1:oi index er jonno porer duita element sort korbo
# step2:return list

def bubbleSort(listOfNumber):
    for i in range(len(listOfNumber)-1):
        for j in range(0, len(listOfNumber)-1-i):
            listOfNumber = sortTwoNumbers(listOfNumber, j)
    return listOfNumber
        
# function = sortTwoNumbers
# input = list, position of first element
# output = sort two element
# step1:first position of the element theke number1 and number2 ber korbo
# step2:compare number1 > number2
#     step2.2: then swap their position 
# step3:return updated list

def sortTwoNumbers(unsortedList, indexOfNumber1):
    number1 = unsortedList[indexOfNumber1]
    number2 = unsortedList[indexOfNumber1 + 1]
    if number1 > number2:
        temporary = number1
        unsortedList[indexOfNumber1] = number2
        unsortedList[indexOfNumber1 + 1] = temporary
    return unsortedList

list1 = [10, -1, 2, 8, 18]
print(bubbleSort(list1))