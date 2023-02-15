from datetime import datetime

Array = list(range(100))
Array.reverse()
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
    print("Кількість перестановок: ", count)
    print("Число порівнянь: ", count1)
    print(datetime.now() - start_time)

print("Bubble sort")
BubbleSort(Array)


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
    print("Кількість перестановок: ", count)
    print("Число порівнянь: ", count1)
    print(datetime.now() - start_time)

print("Improved bubble sort")
ImprovedBubbleSort(Array)


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

print("Insertion sort")
InsertionSort(Array)
