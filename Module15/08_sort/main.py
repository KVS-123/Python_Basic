startList = [1, 4, -3, 0, 10]
print('Изначальный список:', startList)
sortedList = []
for _ in range(len(startList)):
    minElement = startList[0]
    for el in startList:
        if minElement > el:
            minElement = el
    else:
        startList.remove(minElement)
    sortedList.append(minElement)
print('Отсортированный список:', sortedList)
