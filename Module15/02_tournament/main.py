people_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
newPeopleList = []
for index in range(0, len(people_list), 2):
    newPeopleList.append(people_list[index])
print('Первый день:', newPeopleList)
