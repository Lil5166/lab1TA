import algorithm_random
from datetime import datetime

Array = list(range(15))
random.shuffle(Array)
print(Array)

def BubbleSort(Array):
    start_time = datetime.now()
    count = 0
    count1 = 0
    reshuffle = 1
    while reshuffle > 0:
        reshuffle = 0
        for i in range(0, len(Array) - 1):
            count1 += 1
            if Array[i] > Array[i + 1]:
                Array[i], Array[i + 1] = Array[i + 1], Array[i]
                reshuffle = reshuffle + 1
                count += 1


    print(Array)
    print("Кількість перестановок: ",count)
    print("Число порівнянь: ", count1)
    print(datetime.now() - start_time)

def ImprovedBubbleSort(Array):
    start_time = datetime.now()
    count = 0
    count1 = 0
    for i in range(0, len(Array)):
        count1 += 1
        for j in range(0, len(Array) - i - 1):
            if Array[j] > Array[j + 1]:
                temp = Array[j]
                Array[j] = Array[j + 1]
                Array[j + 1] = temp
                count += 1
    print(Array)
    print("Кількість перестановок: ",count)
    print("Число порівнянь: ", count1)
    print(datetime.now() - start_time)


def InsertionSort(Array):
    start_time = datetime.now()
    count = 0
    count1 = 0
    for i in range(1, len(Array)):
        count1 += 1
        temp = Array[i]
        j = i - 1
        while j >= 0 and temp < Array[j]:
            Array[j + 1] = Array[j]
            j = j - 1
            count += 1
        Array[j + 1] = temp
    print(Array)
    print("Кількість перестановок: ", count)
    print("Число порівнянь: ", count1)
    print(datetime.now() - start_time)

print("Алгоритм сортування бульбашкою")
BubbleSort(Array)
print("Модифікований алгоритм сортування бульбашкою")
ImprovedBubbleSort(Array)
print("Insertion_sort")
InsertionSort(Array)