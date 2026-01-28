numList = [1, 4, -3, 0, 10]
newNumList = []
move = int(input('Сдвиг: '))
for index in range(-move, len(numList) - move):
    newNumList.append(numList[index])
print('Изначальный список:', numList)
print('Сдвинутый список:', newNumList)
